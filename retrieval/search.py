"""
Retrieval: given a query string, return the top-k most relevant chunks.

This module never talks to the LLM -- it only does the vector search
and hydrates results with readable metadata from the JSON sidecar
vectorstore.store persists alongside the FAISS index. See generation/
for what happens to these results next.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

import faiss

from embeddings.encoder import EmbeddingEncoder


class EmbeddingModelMismatchError(Exception):
    """Raised when the encoder used at query time doesn't match the
    model the FAISS index was actually built with.

    Comparing two different models' vectors is meaningless (they don't
    share a coordinate space), so this must be caught before running a
    search rather than silently returning garbage results.
    """


@dataclass
class RetrievedChunk:
    """One search result: a chunk plus how well it matched the query."""

    chunk: dict[str, Any]     # metadata (filename, text, heading, ...)
    score: float                 # cosine similarity, roughly in [0, 1]
    rank: int                      # 1-based position in the ranked results


# Splits a compound question like "what is ai? and BM-25?" into separate
# sub-questions, on '?' boundaries.
_SUBQUERY_SPLIT_RE = re.compile(r"(?<=[?])\s*")
# A leading conjunction left over after splitting, e.g. "and BM-25?".
_LEADING_CONJUNCTION_RE = re.compile(r"^(?:and|&|,)\s+", re.IGNORECASE)
_MIN_SUBQUERY_LENGTH = 3


def _split_into_subqueries(query: str) -> list[str]:
    """Break a compound question into separate sub-questions.

    A single embedding of a multi-topic query (e.g. "what is ai? and
    BM-25?") tends to drift toward one topic in vector space and can
    crowd the other topic out of top-k entirely, even though each
    topic retrieves well on its own. search() retrieves each
    sub-question independently and merges the results to avoid that.

    Splitting is deliberately conservative -- on '?' boundaries only,
    not on "and" -- since ordinary single questions often contain
    "and" as normal phrasing (e.g. "What is PageRank and how does it
    work?"), and splitting those would strand a subject-less fragment.
    A question with one or zero '?' characters returns as a list of
    one, so the common single-question case is untouched.
    """
    parts = [p.strip() for p in _SUBQUERY_SPLIT_RE.split(query) if p.strip()]
    if len(parts) < 2:
        return [query.strip()]

    cleaned = [_LEADING_CONJUNCTION_RE.sub("", p).strip() for p in parts]
    cleaned = [p for p in cleaned if len(p) >= _MIN_SUBQUERY_LENGTH]
    return cleaned if len(cleaned) > 1 else [query.strip()]


def search(
    query: str,
    index: faiss.Index | None,
    metadata: list[dict[str, Any]],
    manifest: dict[str, Any] | None,
    encoder: EmbeddingEncoder,
    top_k: int,
) -> list[RetrievedChunk]:
    """Return the top-k chunks most similar to `query`.

    Returns an empty list immediately -- without touching FAISS at all
    -- if there is no index yet or it's empty. Callers (see
    generation/client.py) turn an empty result into the "couldn't find
    relevant information" refusal.

    Compound questions are split and retrieved independently, then
    merged; see _split_into_subqueries.
    """
    if index is None or index.ntotal == 0:
        return []

    if manifest is not None and manifest["embedding_model"] != encoder.model_name:
        raise EmbeddingModelMismatchError(
            f"The index was built with '{manifest['embedding_model']}', but the "
            f"current embedding model is '{encoder.model_name}'. Rebuild the "
            "index after changing the embedding model."
        )

    subqueries = _split_into_subqueries(query)
    query_vectors = encoder.encode(subqueries, is_query=True)
    all_scores, all_vector_ids = index.search(query_vectors, top_k)

    # Merge per-subquery results into one set, keyed by vector id so a
    # chunk that matches more than one sub-question is only kept once
    # (at its best score).
    best_by_vector_id: dict[int, tuple[float, dict[str, Any]]] = {}
    for scores, vector_ids in zip(all_scores, all_vector_ids):
        for vec_id, score in zip(vector_ids, scores):
            vec_id = int(vec_id)
            # FAISS pads short result sets with -1 when top_k > ntotal.
            if vec_id == -1 or vec_id >= len(metadata):
                continue
            score = float(score)
            current = best_by_vector_id.get(vec_id)
            if current is None or score > current[0]:
                best_by_vector_id[vec_id] = (score, metadata[vec_id])

    ranked = sorted(best_by_vector_id.values(), key=lambda pair: pair[0], reverse=True)
    return [
        RetrievedChunk(chunk=chunk, score=score, rank=rank)
        for rank, (score, chunk) in enumerate(ranked, start=1)
    ]

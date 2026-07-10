"""
Retrieval: given a query string, return the top-k most relevant chunks.

This module never talks to the LLM -- it only does the vector search
and hydrates results with readable metadata from the JSON sidecar
vectorstore.store persists alongside the FAISS index. See generation/
for what happens to these results next.
"""

from __future__ import annotations

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
    generation/client.py) turn an empty result into the required
    "couldn't find relevant information" refusal.
    """
    if index is None or index.ntotal == 0:
        return []

    if manifest is not None and manifest["embedding_model"] != encoder.model_name:
        raise EmbeddingModelMismatchError(
            f"The index was built with '{manifest['embedding_model']}', but the "
            f"current embedding model is '{encoder.model_name}'. Rebuild the "
            "index after changing the embedding model."
        )

    query_vector = encoder.encode([query])
    scores, vector_ids = index.search(query_vector, top_k)

    # FAISS pads short result sets with -1 when top_k > ntotal; drop those.
    found = [
        (int(vec_id), float(score))
        for vec_id, score in zip(vector_ids[0], scores[0])
        if vec_id != -1
    ]

    results: list[RetrievedChunk] = []
    for rank, (vec_id, score) in enumerate(found, start=1):
        # metadata's list position is each chunk's faiss_vector_id (see
        # vectorstore.store.rebuild_pipeline), so this is a direct index,
        # not a search -- no database or file lookup needed per result.
        if vec_id >= len(metadata):
            # Index and metadata are out of sync (shouldn't normally
            # happen -- both are written together in rebuild_pipeline).
            # Skip rather than crash the whole search.
            continue
        results.append(RetrievedChunk(chunk=metadata[vec_id], score=score, rank=rank))

    return results

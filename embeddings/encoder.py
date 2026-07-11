"""
Embeddings: turn chunk text into vectors using sentence-transformers.

This module only knows how to turn text into numbers and how to
fingerprint a set of chunks -- it does not know about FAISS or how
that fingerprint is persisted. See vectorstore/store.py for what
happens to the vectors this produces.
"""

from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer

from ingestion.chunker import Chunk
from utils.hashing import sha256_of_strings


class EmbeddingModelError(Exception):
    """Raised when a sentence-transformers model name can't be loaded.

    sentence-transformers/huggingface_hub can raise several different
    exception types for a bad model name (unknown repo, no network,
    invalid name format, ...); this wraps all of them into one
    predictable error so callers only need to catch one thing.
    """


class EmbeddingEncoder:
    """Wraps a single sentence-transformers model."""

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        try:
            self._model = SentenceTransformer(model_name)
        except Exception as exc:
            raise EmbeddingModelError(
                f"Could not load embedding model '{model_name}': {exc}"
            ) from exc

    @property
    def embedding_dim(self) -> int:
        """Vector length this model produces, e.g. 384 for MiniLM."""
        return self._model.get_embedding_dimension()

    def encode(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        """Encode a list of texts into L2-normalized float32 vectors.

        Normalizing here lets vectorstore.build_index's IndexFlatIP search
        behave as cosine similarity -- see that function for why.
        """
        if not texts:
            return np.empty((0, self.embedding_dim), dtype=np.float32)

        vectors = self._model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return np.asarray(vectors, dtype=np.float32)


def compute_dataset_hash(
    chunks: list[Chunk], model_name: str, chunk_size: int, overlap: int
) -> str:
    """Fingerprint a set of chunks plus the settings used to build them.

    This is the cache key the vector store compares against the last
    successful build (manifest.json's dataset_hash, see
    vectorstore/store.py) to decide whether re-embedding is actually
    necessary. It changes if any chunk's text changes, if chunks are
    added or removed, or if the embedding model / chunk size / overlap
    changes -- and stays identical otherwise, even if files were just
    re-read from disk. Chunks are sorted by id first so the hash does
    not depend on file/OS iteration order.
    """
    parts = [model_name, str(chunk_size), str(overlap)]
    for chunk_id, text in sorted((c.chunk_id, c.text) for c in chunks):
        parts.append(chunk_id)
        parts.append(text)
    return sha256_of_strings(parts)

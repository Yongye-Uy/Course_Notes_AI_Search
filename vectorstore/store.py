"""
Vector store: owns the FAISS index lifecycle -- build, save, load, and
rebuild -- plus the metadata.json/manifest.json sidecar files that
hold what FAISS itself can't (see BuildResult for their shape). No
database is used; everything lives in vectorstore/index/ as plain
files, so the app needs no extra infrastructure to deploy.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import faiss
import numpy as np

from config import Config
from embeddings.encoder import EmbeddingEncoder, compute_dataset_hash
from ingestion.chunker import chunk_documents
from ingestion.loader import load_all_documents

logger = logging.getLogger(__name__)

INDEX_FILENAME = "index.faiss"
METADATA_FILENAME = "metadata.json"
MANIFEST_FILENAME = "manifest.json"


@dataclass
class BuildResult:
    """What rebuild_pipeline() did, and everything needed to query."""

    index: faiss.Index | None
    metadata: list[dict[str, Any]]   # chunk info, position == faiss vector id
    manifest: dict[str, Any] | None    # what the index was last built from
    doc_count: int
    chunk_count: int
    warnings: list[str] = field(default_factory=list)
    rebuilt: bool = False   # False if an existing, up-to-date index was reused


def build_index(vectors: np.ndarray) -> faiss.Index:
    """Build a flat inner-product FAISS index from a set of vectors.

    IndexFlatIP over L2-normalized vectors is mathematically equivalent
    to cosine similarity. "Flat" (exact, brute-force) search is fine at
    the scale of a single course's notes, so an approximate index type
    like IVF or HNSW isn't needed here.
    """
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    if len(vectors) > 0:
        index.add(vectors)
    return index


def save_index(index: faiss.Index, index_dir: Path) -> None:
    """Write the FAISS index to disk."""
    index_dir.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(index_dir / INDEX_FILENAME))


def load_index(index_dir: Path) -> faiss.Index | None:
    """Read the FAISS index from disk.

    Returns None (not an exception) if no index file exists yet -- a
    fresh checkout, or a dataset that's never been built, is a normal
    state, not an error.
    """
    path = index_dir / INDEX_FILENAME
    if not path.exists():
        return None
    return faiss.read_index(str(path))


def save_metadata(metadata: list[dict[str, Any]], index_dir: Path) -> None:
    """Write chunk metadata to disk, ordered so that list position
    equals each chunk's FAISS vector id."""
    index_dir.mkdir(parents=True, exist_ok=True)
    path = index_dir / METADATA_FILENAME
    path.write_text(json.dumps(metadata), encoding="utf-8")


def load_metadata(index_dir: Path) -> list[dict[str, Any]] | None:
    """Read chunk metadata from disk, or None if it doesn't exist yet."""
    path = index_dir / METADATA_FILENAME
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(manifest: dict[str, Any], index_dir: Path) -> None:
    """Write the build manifest (dataset hash, model, counts, timestamp)."""
    index_dir.mkdir(parents=True, exist_ok=True)
    path = index_dir / MANIFEST_FILENAME
    path.write_text(json.dumps(manifest), encoding="utf-8")


def load_manifest(index_dir: Path) -> dict[str, Any] | None:
    """Read the build manifest from disk, or None if nothing's built yet."""
    path = index_dir / MANIFEST_FILENAME
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def needs_rebuild(manifest: dict[str, Any] | None, current_hash: str) -> bool:
    """True if nothing has been built yet, or if the notes, chunk
    settings, or embedding model changed since the last build."""
    if manifest is None:
        return True
    return manifest["dataset_hash"] != current_hash


def rebuild_pipeline(
    config: Config, embedding_model: str, force: bool = False
) -> BuildResult:
    """Run the full ingest -> chunk -> embed -> index -> persist pipeline.

    Ingesting and chunking are cheap and always run. Embedding and
    rebuilding the FAISS index are expensive, so that part is skipped
    when nothing has changed since the last build -- see needs_rebuild
    -- unless force=True.
    """
    documents, warnings = load_all_documents(config.dataset_dir)

    if not documents:
        # Nothing to ingest. Don't touch whatever index may already
        # exist on disk from a previous run -- just report the current
        # (empty) dataset state so the caller can show "0 documents".
        return BuildResult(
            index=load_index(config.index_dir),
            metadata=load_metadata(config.index_dir) or [],
            manifest=load_manifest(config.index_dir),
            doc_count=0,
            chunk_count=0,
            warnings=warnings,
            rebuilt=False,
        )

    chunks = chunk_documents(documents, config.chunk_size, config.chunk_overlap)
    dataset_hash = compute_dataset_hash(
        chunks, embedding_model, config.chunk_size, config.chunk_overlap
    )

    existing_index = load_index(config.index_dir)
    existing_manifest = load_manifest(config.index_dir)
    if not force and existing_index is not None and not needs_rebuild(existing_manifest, dataset_hash):
        logger.info("Dataset unchanged since last build -- skipping rebuild.")
        return BuildResult(
            index=existing_index,
            metadata=load_metadata(config.index_dir) or [],
            manifest=existing_manifest,
            doc_count=len(documents),
            chunk_count=len(chunks),
            warnings=warnings,
            rebuilt=False,
        )

    encoder = EmbeddingEncoder(embedding_model)
    vectors = encoder.encode([c.text for c in chunks])

    index = build_index(vectors)
    save_index(index, config.index_dir)

    # faiss_vector_id is each chunk's insertion position in the index
    # (0..n-1) -- assigning it here, in the same order vectors were
    # added above, is what lets a FAISS search result (a list of
    # positions) be turned back into readable text: metadata[vector_id].
    metadata = [
        {
            "chunk_id": chunk.chunk_id,
            "doc_id": chunk.doc_id,
            "filename": chunk.filename,
            "chunk_index": chunk.chunk_index,
            "heading_path": chunk.heading_path,
            "text": chunk.text,
            "char_count": chunk.char_count,
            "faiss_vector_id": vector_id,
        }
        for vector_id, chunk in enumerate(chunks)
    ]
    save_metadata(metadata, config.index_dir)

    manifest = {
        "dataset_hash": dataset_hash,
        "embedding_model": embedding_model,
        "chunk_size": config.chunk_size,
        "chunk_overlap": config.chunk_overlap,
        "doc_count": len(documents),
        "chunk_count": len(chunks),
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    save_manifest(manifest, config.index_dir)

    return BuildResult(
        index=index,
        metadata=metadata,
        manifest=manifest,
        doc_count=len(documents),
        chunk_count=len(chunks),
        warnings=warnings,
        rebuilt=True,
    )

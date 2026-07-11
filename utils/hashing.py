"""Generic hashing helpers shared across modules."""

from __future__ import annotations

import hashlib


def sha256_of_strings(parts: list[str]) -> str:
    """Return a stable SHA-256 hex digest of a sequence of strings.

    A null byte separates parts so ["ab", "c"] and ["a", "bc"] never
    collide. Order matters -- sort `parts` first if the hash must be
    independent of input order.
    """
    hasher = hashlib.sha256()
    for part in parts:
        hasher.update(part.encode("utf-8"))
        hasher.update(b"\x00")
    return hasher.hexdigest()

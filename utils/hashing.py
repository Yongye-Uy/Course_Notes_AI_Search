"""Generic hashing helpers shared across modules."""

from __future__ import annotations

import hashlib


def sha256_of_strings(parts: list[str]) -> str:
    """Return a stable SHA-256 hex digest of a sequence of strings.

    A null-byte separator is written between parts so that, e.g.,
    ["ab", "c"] and ["a", "bc"] never collide to the same digest.
    Order matters -- callers that want a hash independent of input
    order (e.g. a set of chunks that could come back in any order)
    must sort `parts` themselves before calling this.
    """
    hasher = hashlib.sha256()
    for part in parts:
        hasher.update(part.encode("utf-8"))
        hasher.update(b"\x00")
    return hasher.hexdigest()

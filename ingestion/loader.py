"""
Document loading: find every Markdown file in dataset/ and read it into
a plain Document object. This module does not chunk or embed anything --
it only turns files on disk into text in memory. See ingestion/chunker.py
for the next step.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

# Matches a Markdown heading line, e.g. "# Week 1" or "## Intro".
# Group 1 captures the '#' markers (their count is the heading level),
# group 2 captures the heading text.
_HEADING_LINE_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass
class Document:
    """One ingested course-notes file."""

    doc_id: str        # stable id derived from the filename, used as a DB key
    filename: str       # e.g. "Week 1 SEIR.md"
    filepath: Path        # absolute path on disk
    title: str              # first Markdown heading, or the filename if none
    content: str              # raw file text, unmodified


def discover_files(dataset_dir: Path) -> list[Path]:
    """Find every .md file under dataset_dir.

    Sorted so that processing order (and therefore doc_id / chunk_id
    assignment) is deterministic between runs -- otherwise re-running
    the pipeline on unchanged files could produce a different-looking
    diff for no real reason.
    """
    if not dataset_dir.exists():
        return []
    return sorted(dataset_dir.glob("**/*.md"))


def find_headings(content: str) -> list[tuple[int, int, str]]:
    """Find every genuine Markdown heading line in content.

    A '#'-prefixed line only counts as a heading if it is preceded by
    a blank line (or is the first line of the file) -- this is how
    Markdown headings are conventionally written, and it is what
    reliably tells them apart from Python comments such as
    "# Embed the question" that show up inline inside this dataset's
    unfenced code examples. (Verified against every course-notes file:
    every '#' line that was actually a code comment was packed directly
    against the surrounding code with no blank line before it.)

    Returns a list of (line_index, level, heading_text) tuples in
    document order, where level is 1-6 (the number of '#' characters).
    Used both for title extraction here and for section-aware chunking
    in ingestion/chunker.py.
    """
    lines = content.splitlines()
    headings: list[tuple[int, int, str]] = []
    for i, line in enumerate(lines):
        match = _HEADING_LINE_RE.match(line)
        if match is None:
            continue
        preceded_by_blank = i == 0 or lines[i - 1].strip() == ""
        if preceded_by_blank:
            level = len(match.group(1))
            headings.append((i, level, match.group(2)))
    return headings


def _extract_title(content: str, fallback: str) -> str:
    """Return the text of the first genuine Markdown heading in content,
    or `fallback` (normally the filename) if the file has none.

    Many of this project's course notes started life as PDF/PPTX slide
    decks and were converted to Markdown without real heading syntax,
    so falling back to the filename is the common case, not an edge
    case -- it must produce a sensible title on its own.
    """
    headings = find_headings(content)
    return headings[0][2] if headings else fallback


def load_document(path: Path) -> Document | None:
    """Read one Markdown file into a Document.

    Returns None (and logs a warning) instead of raising if the file
    can't be read or decoded, so one corrupted file never stops the
    whole ingestion batch -- see load_all_documents().
    """
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        logger.warning("Skipping %s: %s", path.name, exc)
        return None

    doc_id = path.stem
    title = _extract_title(content, fallback=path.stem)

    return Document(
        doc_id=doc_id,
        filename=path.name,
        filepath=path,
        title=title,
        content=content,
    )


def load_all_documents(dataset_dir: Path) -> tuple[list[Document], list[str]]:
    """Load every Markdown file under dataset_dir.

    Returns (documents, warnings). An empty dataset_dir (or one with no
    .md files) returns ([], []) -- this is a normal, expected state
    (e.g. before the user has added any notes yet), not an error, so it
    is not raised as an exception. Callers decide how to present "zero
    documents" to the user.
    """
    warnings: list[str] = []
    documents: list[Document] = []

    for path in discover_files(dataset_dir):
        doc = load_document(path)
        if doc is None:
            warnings.append(f"Skipped {path.name}: could not read this file.")
            continue
        documents.append(doc)

    return documents, warnings

"""
Chunking: split each loaded Document into retrievable Chunk pieces.

Strategy: section-aware first (split on genuine Markdown headings, see
ingestion/loader.find_headings), then paragraph-packed fixed-size with
overlap inside each section. A document with no headings at all -- the
common case in this project's dataset, since most notes started life
as PDF/PPTX slides with no real Markdown heading syntax -- simply
becomes one big "section" and is chunked the same way.
"""

from __future__ import annotations

from dataclasses import dataclass

from ingestion.loader import Document, find_headings


@dataclass
class Chunk:
    """One retrievable piece of a document."""

    chunk_id: str        # f"{doc_id}::{chunk_index}", unique across the dataset
    doc_id: str
    filename: str
    chunk_index: int       # 0-based position within the document
    heading_path: str        # e.g. "Week 3 > Gradient Descent", or "" if none
    text: str
    char_count: int


def split_into_sections(content: str) -> list[tuple[str, str]]:
    """Split document text into (heading_path, section_text) pairs.

    A document with no headings becomes a single section with
    heading_path="". Any text before the first heading (or the whole
    document, if headings exist but content also precedes them) is
    kept as its own section rather than dropped.
    """
    if not content.strip():
        return []

    headings = find_headings(content)
    if not headings:
        return [("", content.strip())]

    lines = content.splitlines()
    sections: list[tuple[str, str]] = []

    # Any text before the first heading still counts as content.
    preamble = "\n".join(lines[: headings[0][0]]).strip()
    if preamble:
        sections.append(("", preamble))

    # Build a nested heading path (e.g. "Week 3 > Gradient Descent") by
    # keeping a stack of the currently "open" headings at each level.
    stack: list[tuple[int, str]] = []
    for i, (line_no, level, text) in enumerate(headings):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, text))
        heading_path = " > ".join(t for _, t in stack)

        start = line_no + 1
        end = headings[i + 1][0] if i + 1 < len(headings) else len(lines)
        section_text = "\n".join(lines[start:end]).strip()
        if section_text:
            sections.append((heading_path, section_text))

    return sections


def _hard_slice(text: str, chunk_size: int, overlap: int) -> list[str]:
    """Fixed-size sliding window over text with no paragraph awareness.

    Only used as a fallback for a single paragraph that is by itself
    longer than chunk_size -- paragraph packing alone can't split that
    case, so we fall back to plain character slicing to guarantee no
    chunk ever exceeds chunk_size.
    """
    step = chunk_size - overlap
    slices = []
    i = 0
    while i < len(text):
        slices.append(text[i : i + chunk_size])
        i += step
    return slices


def chunk_section(section_text: str, chunk_size: int, overlap: int) -> list[str]:
    """Pack a section's paragraphs into chunks of up to chunk_size
    characters, carrying `overlap` characters from the end of one
    chunk into the start of the next.

    Paragraphs (blank-line-separated blocks) are never split apart
    unless a single paragraph alone exceeds chunk_size, in which case
    it is hard-sliced on its own (see _hard_slice). Packing whole
    paragraphs together -- rather than slicing at a fixed character
    count everywhere -- is what keeps chunk boundaries from landing
    mid-sentence in the common case.
    """
    if overlap >= chunk_size:
        raise ValueError(
            f"chunk_overlap ({overlap}) must be smaller than chunk_size ({chunk_size})."
        )

    paragraphs = [p.strip() for p in section_text.split("\n\n") if p.strip()]
    if not paragraphs:
        return []

    chunks: list[str] = []
    current = ""

    for para in paragraphs:
        if len(para) > chunk_size:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(_hard_slice(para, chunk_size, overlap))
            continue

        candidate = f"{current}\n\n{para}" if current else para
        if len(candidate) <= chunk_size:
            current = candidate
            continue

        # Adding this paragraph would overflow the current chunk: close
        # it out, then start the next one with the tail of the previous
        # chunk (the overlap) plus this paragraph.
        chunks.append(current)
        tail = current[-overlap:] if overlap > 0 else ""
        current = f"{tail}\n\n{para}" if tail else para

    if current:
        chunks.append(current)

    return chunks


def chunk_document(doc: Document, chunk_size: int, overlap: int) -> list[Chunk]:
    """Chunk a single Document, numbering chunks sequentially across
    the whole document (not restarting per section)."""
    chunks: list[Chunk] = []
    index = 0
    for heading_path, section_text in split_into_sections(doc.content):
        for piece in chunk_section(section_text, chunk_size, overlap):
            chunks.append(
                Chunk(
                    chunk_id=f"{doc.doc_id}::{index}",
                    doc_id=doc.doc_id,
                    filename=doc.filename,
                    chunk_index=index,
                    heading_path=heading_path,
                    text=piece,
                    char_count=len(piece),
                )
            )
            index += 1
    return chunks


def chunk_documents(
    docs: list[Document], chunk_size: int, overlap: int
) -> list[Chunk]:
    """Chunk every document in `docs` and return one flat list of Chunks
    -- this is the entry point embeddings/vectorstore build from."""
    all_chunks: list[Chunk] = []
    for doc in docs:
        all_chunks.extend(chunk_document(doc, chunk_size, overlap))
    return all_chunks

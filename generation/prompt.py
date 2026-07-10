"""
Prompt construction and citation extraction for grounded generation.

The prompt instructs the model to answer only from numbered CONTEXT
excerpts and to cite them as [Source N]. A small integer is far more
reliable to extract from free-form model output than asking the model
to echo a filename back verbatim (models paraphrase, truncate, or
misspell filenames; they don't misspell "3").
"""

from __future__ import annotations

import re

from retrieval.search import RetrievedChunk

# The exact sentence required when nothing relevant is found. Both
# generation/client.py (the empty-retrieval short-circuit) and the
# prompt below use this same constant, so the UI only ever needs to
# check for one fixed string.
REFUSAL_MESSAGE = "I couldn't find relevant information in the provided course notes."

_SYSTEM_PROMPT = f"""You are a course assistant answering questions about a student's own course notes. Answer ONLY using the numbered CONTEXT excerpts below -- never use outside knowledge, even if you know the answer.

When you use information from an excerpt, cite it inline as [Source N], where N is that excerpt's number.

If the context does not contain enough information to answer the question, respond with exactly this sentence and nothing else:
"{REFUSAL_MESSAGE}"
"""

# Matches citations like "[Source 1]" or "[Source 12]" in the model's
# answer. Two things vary in practice, observed directly from the
# NVIDIA endpoint's responses during testing across repeated calls to
# the *same* prompt:
#   - the space between "Source" and the number is sometimes a
#     Unicode narrow no-break space (U+202F), not a plain ASCII space
#     -- so \s* is used instead of a literal " ".
#   - the brackets themselves are sometimes full-width CJK brackets
#     "【...】" instead of ASCII "[...]" -- so both are accepted.
_CITATION_RE = re.compile(r"[\[【]Source\s*(\d+)[\]】]")


def build_messages(question: str, retrieved: list[RetrievedChunk]) -> list[dict[str, str]]:
    """Build the chat messages list to send to the LLM.

    `retrieved` must already be in rank order -- rank 1 becomes
    [Source 1], rank 2 becomes [Source 2], and so on, so the numbers
    the model cites line up with RetrievedChunk.rank.
    """
    context_blocks = [
        f"[Source {r.rank}] (from {r.chunk['filename']}, chunk {r.chunk['chunk_index']}):\n"
        f"{r.chunk['text']}"
        for r in retrieved
    ]
    context_text = "\n\n".join(context_blocks)
    user_prompt = f"CONTEXT:\n{context_text}\n\nQUESTION: {question}"

    return [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]


def extract_cited_sources(
    answer_text: str, retrieved: list[RetrievedChunk]
) -> list[RetrievedChunk]:
    """Find every [Source N] the model actually cited in its answer.

    Returns the matching subset of `retrieved`, in order of first
    citation, with duplicates removed. The UI uses this to flag which
    of the displayed sources were actually used -- the model may
    retrieve five chunks but only end up citing two of them.
    """
    by_rank = {r.rank: r for r in retrieved}
    seen: set[int] = set()
    cited: list[RetrievedChunk] = []

    for match in _CITATION_RE.finditer(answer_text):
        rank = int(match.group(1))
        if rank in seen:
            continue
        chunk = by_rank.get(rank)
        if chunk is not None:
            seen.add(rank)
            cited.append(chunk)

    return cited

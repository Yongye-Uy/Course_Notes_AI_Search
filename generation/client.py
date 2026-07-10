"""
NVIDIA OpenAI-compatible client wrapper, plus generate_answer() -- the
top-level function that ties prompt building, the LLM call, and
citation extraction together into one grounded, cited answer.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from openai import APIError, OpenAI

from config import Config
from generation.prompt import REFUSAL_MESSAGE, build_messages, extract_cited_sources
from retrieval.search import RetrievedChunk


class MissingAPIKeyError(Exception):
    """Raised when NVIDIA_API_KEY is not configured."""


@dataclass
class AnswerResult:
    """Everything the UI needs to render one generated answer.

    `error` is set instead of an exception being raised, so app.py can
    show a banner with a simple `if result.error:` check rather than
    wrapping every call site in try/except.
    """

    answer_text: str
    cited_sources: list[RetrievedChunk] = field(default_factory=list)
    error: str | None = None


def get_client(config: Config) -> OpenAI:
    """Build an OpenAI-compatible client pointed at NVIDIA's endpoint.

    Checked at call time, not import time, so the rest of the app can
    start and render a friendly banner even before .env is filled in.
    Raises MissingAPIKeyError immediately instead of letting the API
    call fail later with a confusing generic 401.
    """
    if not config.nvidia_api_key:
        raise MissingAPIKeyError(
            "NVIDIA_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return OpenAI(base_url=config.nvidia_base_url, api_key=config.nvidia_api_key)


def generate_answer(
    question: str,
    retrieved: list[RetrievedChunk],
    config: Config,
    temperature: float,
) -> AnswerResult:
    """Generate a grounded, cited answer from retrieved chunks.

    If retrieval found nothing, the refusal message is returned
    directly and the LLM is never called -- cheaper, fully
    deterministic, and removes any chance of the model hallucinating
    an answer around an empty context.
    """
    if not retrieved:
        return AnswerResult(answer_text=REFUSAL_MESSAGE)

    try:
        client = get_client(config)
    except MissingAPIKeyError as exc:
        return AnswerResult(answer_text="", error=str(exc))

    messages = build_messages(question, retrieved)

    try:
        completion = client.chat.completions.create(
            model=config.nvidia_model,
            messages=messages,
            temperature=temperature,
            top_p=1,
            max_tokens=config.max_tokens,
            stream=False,
        )
    except APIError as exc:
        # Covers auth failures, connection errors, rate limits, and
        # other API-side problems -- all subclass openai.APIError.
        return AnswerResult(answer_text="", error=f"Generation failed: {exc}")

    answer_text = completion.choices[0].message.content or ""
    cited_sources = extract_cited_sources(answer_text, retrieved)

    return AnswerResult(answer_text=answer_text, cited_sources=cited_sources)

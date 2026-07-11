"""
Central configuration for the Course Notes AI Search System.

Every tunable setting used by the app lives here, loaded from a local
.env file. No other module should read os.environ directly or hardcode
a path, model name, or credential -- everything imports `config` from
this file instead.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Load variables from a local .env file (if present) into the process
# environment. Must happen before the os.getenv() calls below run.
load_dotenv()

# Folder this file lives in -- used to build absolute paths so the app
# behaves the same no matter what directory it's launched from.
PROJECT_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Config:
    """All configurable settings for the application, grouped by layer."""

    # --- Dataset & vector index storage paths ---
    dataset_dir: Path = PROJECT_ROOT / "dataset"
    index_dir: Path = PROJECT_ROOT / "vectorstore" / "index"

    # --- Chunking ---
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "500"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "50"))

    # --- Retrieval ---
    top_k_default: int = int(os.getenv("TOP_K_DEFAULT", "5"))

    # --- Embeddings ---
    embedding_model_default: str = os.getenv(
        "EMBEDDING_MODEL_DEFAULT", "all-MiniLM-L6-v2"
    )

    # --- Generation: NVIDIA's OpenAI-compatible endpoint ---
    # Never hardcode the key -- it must come from .env only.
    nvidia_api_key: str | None = os.getenv("NVIDIA_API_KEY")
    nvidia_base_url: str = os.getenv(
        "NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"
    )
    nvidia_model: str = os.getenv("NVIDIA_MODEL", "openai/gpt-oss-120b")
    temperature_default: float = float(os.getenv("TEMPERATURE_DEFAULT", "1.0"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "4096"))


# A single shared instance every module imports: `from config import config`.
config = Config()


# Short, known-good list of embedding models offered in the Streamlit
# dropdown. Restricting the choice to this list (rather than free-text
# entry) is what prevents the "invalid embedding model" error case from
# ever reaching sentence-transformers in the first place.
AVAILABLE_EMBEDDING_MODELS: list[str] = [
    "all-MiniLM-L6-v2",
    "all-mpnet-base-v2",
    "multi-qa-MiniLM-L6-cos-v1",
]

# Plain-English labels for the dropdown -- the real sentence-transformers
# names above are what actually get loaded and stored (in the FAISS
# build hash and manifest.json), this dict only changes what the
# user sees in the UI.
EMBEDDING_MODEL_LABELS: dict[str, str] = {
    "all-MiniLM-L6-v2": "Basic (fast)",
    "all-mpnet-base-v2": "Smart (more accurate, slower)",
    "multi-qa-MiniLM-L6-cos-v1": "Balanced (tuned for Q&A)",
}


def validate_config() -> list[str]:
    """Check for common setup problems and return plain-English descriptions
    of anything wrong. Never raises -- the Streamlit app calls this at
    startup and renders each problem as a banner instead of crashing, so
    the UI is still browsable before setup is fully finished.
    """
    problems: list[str] = []

    if not config.nvidia_api_key:
        problems.append(
            "NVIDIA_API_KEY is not set. Copy .env.example to .env and add "
            "your key before asking questions."
        )

    if not config.dataset_dir.exists():
        problems.append(
            f"Dataset folder '{config.dataset_dir}' does not exist. "
            "Create it and add your .md course notes."
        )

    return problems

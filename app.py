"""
Streamlit entrypoint: Course Notes AI Search.

Ties every other layer together -- ingestion/chunking/embeddings via
vectorstore.rebuild_pipeline(), retrieval.search(), and
generation.generate_answer() -- behind a query box, an answer panel,
and a sources panel. See config.py for every setting used here.
"""

from __future__ import annotations

import time
from datetime import datetime

import streamlit as st

from config import AVAILABLE_EMBEDDING_MODELS, EMBEDDING_MODEL_LABELS, config, validate_config
from embeddings.encoder import EmbeddingEncoder
from generation.client import generate_answer
from retrieval.search import EmbeddingModelMismatchError, search
from vectorstore import store

# A generous cap, not a real limit on legitimate questions -- mainly a
# guard against pasting a huge block of text that would waste an LLM
# call on something that was never a real course-notes question.
MAX_QUESTION_LENGTH = 1000

# Fixed test queries for the Evaluation tab, kept here since it's a
# short, static list specific to this app's UI. The last case is
# deliberately off-topic (no expected_answer) to exercise the refusal
# path.
EVAL_CASES: list[dict] = [
    {
        "question": "What is PageRank and how does it work?",
        "expected_answer": (
            "PageRank, created by Larry Page and Sergey Brin, ranks pages by "
            "treating links as votes of importance, modeled as a random surfer "
            "moving between pages."
        ),
    },
    {
        "question": "What is Retrieval-Augmented Generation (RAG)?",
        "expected_answer": (
            "RAG grounds an LLM's answer by retrieving relevant chunks from a "
            "document collection and passing them to the model as context."
        ),
    },
    {
        "question": "How do you evaluate an information retrieval system?",
        "expected_answer": (
            "IR systems are commonly evaluated with metrics such as precision "
            "and recall over ranked results."
        ),
    },
    {
        "question": "What is a vector database and how is it used in Neural IR?",
        "expected_answer": (
            "A vector database stores embeddings and supports similarity "
            "search, used in Neural IR to find semantically related content."
        ),
    },
    {
        "question": "Explain content-based filtering in recommender systems.",
        "expected_answer": (
            "Content-based filtering recommends items similar to ones a user "
            "already liked, based on item features rather than other users."
        ),
    },
    {
        "question": "What are the key stages of web crawling?",
        "expected_answer": (
            "Web crawling involves fetching pages, extracting data and links, "
            "and following those links to discover further pages."
        ),
    },
    {
        "question": "What ethical issues arise in information retrieval systems?",
        "expected_answer": (
            "Ethical concerns in IR include bias in ranking, privacy, and the "
            "spread of misinformation."
        ),
    },
    {
        # Deliberately outside the course notes -- correct behavior is the
        # fixed refusal message, not a hallucinated answer.
        "question": "What is the capital of France?",
        "expected_answer": None,
    },
    {
        # Regression test for a compound query spanning two courses' notes;
        # see retrieval.search._split_into_subqueries for why this needs
        # special handling.
        "question": "What is AI? And what is BM-25?",
        "expected_answer": (
            "Should address both parts: a definition of AI, and a "
            "definition of BM-25 as a keyword-based ranking function."
        ),
    },
]

st.set_page_config(page_title="Course Notes AI Search", page_icon="📚", layout="wide")

# Holds the most recent question's results so the Answer/Sources panels
# survive reruns triggered by moving a slider, instead of disappearing.
if "last_result" not in st.session_state:
    st.session_state.last_result = None


@st.cache_resource(show_spinner="Loading embedding model and checking the index...")
def get_resources(embedding_model: str):
    """Load the encoder and an up-to-date FAISS index for one embedding model.

    Cached per embedding_model, so switching models in the sidebar busts the
    cache naturally. rebuild_pipeline() only re-embeds when the dataset or
    settings changed, so this stays cheap on a cache hit.
    """
    encoder = EmbeddingEncoder(embedding_model)
    build_result = store.rebuild_pipeline(config, embedding_model)
    return encoder, build_result


st.title("Course Notes AI Search")
st.caption(
    "Ask a question and get an answer grounded only in your own course notes, "
    "with citations back to the source chunks."
)

with st.expander("ℹ️ How this works"):
    st.markdown(
        "1. Your question and every note chunk are converted into vectors "
        "by the embedding model.\n"
        "2. **Top-K** (sidebar) controls how many of the closest-matching "
        "chunks are retrieved as sources.\n"
        "3. The AI answers using only those retrieved chunks, and each "
        "source below shows whether it was actually **cited** in the answer."
    )

for problem in validate_config():
    st.error(problem)

# --- Sidebar: settings ---
st.sidebar.header("Settings")
top_k = st.sidebar.slider(
    "Top-K (chunks to retrieve)",
    min_value=1,
    max_value=15,
    value=config.top_k_default,
    help=(
        "How many matching note excerpts to retrieve and show as sources "
        "for the answer. Higher = more supporting context, but may pull "
        "in less relevant excerpts."
    ),
)

# Not exposed as a slider -- it only changes the wording of the answer,
# not retrieval or grounding, and users found it a confusing control.
# Fixed at the NVIDIA sample's default.
temperature = config.temperature_default

embedding_model = st.sidebar.selectbox(
    "Embedding model",
    AVAILABLE_EMBEDDING_MODELS,
    index=AVAILABLE_EMBEDDING_MODELS.index(config.embedding_model_default),
    format_func=lambda name: EMBEDDING_MODEL_LABELS.get(name, name),
    help=(
        "The AI model used to match your question against your notes. "
        "'Smart' is more accurate but slower; 'Basic' is fastest."
    ),
)

if st.sidebar.button("Rebuild Index", help="Re-scan dataset/ and rebuild from scratch."):
    get_resources.clear()
    with st.spinner("Rebuilding index..."):
        store.rebuild_pipeline(config, embedding_model, force=True)
    st.rerun()

encoder = None
build_result = None
try:
    encoder, build_result = get_resources(embedding_model)
except Exception as exc:
    st.sidebar.error(f"Could not load embedding model or index: {exc}")

st.sidebar.subheader("Dataset statistics")
doc_count = build_result.doc_count if build_result is not None else 0
chunk_count = build_result.chunk_count if build_result is not None else 0

stat_col1, stat_col2 = st.sidebar.columns(2)
stat_col1.metric("Documents", doc_count)
stat_col2.metric("Chunks", chunk_count)

manifest = build_result.manifest if build_result is not None else None
if manifest is None:
    st.sidebar.badge("Index not built", color="gray")
else:
    built_model_label = EMBEDDING_MODEL_LABELS.get(
        manifest["embedding_model"], manifest["embedding_model"]
    )
    built_at = datetime.fromisoformat(manifest["built_at"])
    st.sidebar.badge("Index built", icon=":material/check_circle:", color="green")
    st.sidebar.caption(
        f"{built_at:%Y-%m-%d %H:%M} · {manifest['chunk_count']} chunks · {built_model_label}"
    )

if build_result is not None:
    if build_result.warnings:
        with st.sidebar.expander(f"{len(build_result.warnings)} file(s) skipped during load"):
            for warning in build_result.warnings:
                st.write(warning)

    if build_result.doc_count == 0:
        st.info(
            f"No documents found in `{config.dataset_dir}`. Add .md course notes "
            "and click Rebuild Index."
        )
    else:
        dataset_titles = sorted({m["filename"].removesuffix(".md") for m in build_result.metadata})
        with st.sidebar.expander("📂 What's in this dataset"):
            st.caption("Topics currently indexed and searchable:")
            for title in dataset_titles:
                st.write(f"- {title}")


# --- Main area ---
search_tab, eval_tab = st.tabs(["🔍 Search", "🧪 Evaluation"])

with search_tab:
    with st.form("search_form"):
        question = st.text_input("Ask a question about your course notes")
        submitted = st.form_submit_button("Search")

    if submitted:
        if not question.strip():
            st.warning("Please enter a question.")
        elif len(question) > MAX_QUESTION_LENGTH:
            st.warning(
                f"Question is too long ({len(question)} characters, max "
                f"{MAX_QUESTION_LENGTH}). Please shorten it."
            )
        elif encoder is None or build_result is None:
            st.error("Search is unavailable until the setup problems above are resolved.")
        else:
            with st.spinner("Searching and generating an answer..."):
                start = time.perf_counter()
                try:
                    retrieved = search(
                        question, build_result.index, build_result.metadata,
                        build_result.manifest, encoder, top_k,
                    )
                except EmbeddingModelMismatchError as exc:
                    st.error(str(exc))
                    retrieved = None

                if retrieved is not None:
                    answer_result = generate_answer(question, retrieved, config, temperature)
                    elapsed = time.perf_counter() - start

                    st.session_state.last_result = {
                        "question": question,
                        "retrieved": retrieved,
                        "answer_result": answer_result,
                        "elapsed": elapsed,
                    }

    result = st.session_state.last_result
    if result is None:
        st.info("Ask a question above to see a grounded, cited answer with sources here.")
    else:
        st.subheader("Answer")
        answer_result = result["answer_result"]
        if answer_result.error:
            st.error(answer_result.error)
        else:
            st.markdown(answer_result.answer_text)
            st.caption(f"Answered in {result['elapsed']:.1f}s")

        st.subheader("Sources")
        retrieved = result["retrieved"]
        if not retrieved:
            st.info("No sources found.")
        else:
            cited_chunk_ids = {r.chunk["chunk_id"] for r in answer_result.cited_sources}
            for r in retrieved:
                is_cited = r.chunk["chunk_id"] in cited_chunk_ids
                heading = f" · {r.chunk['heading_path']}" if r.chunk["heading_path"] else ""

                with st.container(border=True):
                    header_col, badge_col = st.columns([5, 1])
                    with header_col:
                        st.markdown(f"**[{r.rank}] {r.chunk['filename']}**")
                        st.caption(f"chunk {r.chunk['chunk_index']}{heading}")
                    with badge_col:
                        if is_cited:
                            st.badge("Cited", icon=":material/check_circle:", color="green")

                    st.progress(min(max(r.score, 0.0), 1.0), text=f"Similarity {r.score:.0%}")

                    with st.expander("Show excerpt"):
                        st.write(r.chunk["text"])

with eval_tab:
    st.write(
        "Runs a fixed set of test questions through the same retrieval + "
        "generation pipeline as the Search tab. Results are shown below "
        "for this session only (not saved to disk)."
    )

    if st.button("Run Evaluation", disabled=encoder is None or build_result is None):
        progress = st.progress(0.0, text="Running evaluation queries...")
        eval_results = []

        for i, case in enumerate(EVAL_CASES):
            eval_retrieved = search(
                case["question"], build_result.index, build_result.metadata,
                build_result.manifest, encoder, top_k,
            )
            eval_answer = generate_answer(case["question"], eval_retrieved, config, temperature)

            eval_results.append((case, eval_retrieved, eval_answer))
            progress.progress((i + 1) / len(EVAL_CASES), text=f"Ran {i + 1}/{len(EVAL_CASES)} queries")

        progress.empty()
        st.session_state.eval_results = eval_results

    eval_results = st.session_state.get("eval_results")
    if eval_results:
        for case, eval_retrieved, eval_answer in eval_results:
            with st.expander(case["question"]):
                st.markdown("**Generated answer**")
                if eval_answer.error:
                    st.error(eval_answer.error)
                else:
                    st.write(eval_answer.answer_text)

                if case["expected_answer"]:
                    st.markdown("**Expected answer (for comparison)**")
                    st.write(case["expected_answer"])

                st.markdown("**Retrieved chunks**")
                if not eval_retrieved:
                    st.write("No sources found.")
                else:
                    for r in eval_retrieved:
                        st.write(
                            f"[{r.rank}] {r.chunk['filename']} - chunk {r.chunk['chunk_index']} "
                            f"- similarity {r.score:.3f}"
                        )

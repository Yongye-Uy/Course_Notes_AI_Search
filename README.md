# Course Notes AI Search System

A Retrieval-Augmented Generation (RAG) search system developed for the **CS382 Search Engine & Information Retrieval** final project.

The system allows users to search their own course notes and receive answers based only on the uploaded documents. It uses vector search with FAISS and generates grounded responses using the NVIDIA AI API. Every answer includes the source notes used to generate the response.

---

## Features

- Search course notes using RAG
- Supports Markdown (`.md`) files
- FAISS vector search
- Sentence Transformer embeddings
- NVIDIA AI for answer generation
- Source citations for every answer
- Streamlit web interface
- Automatic index rebuild when the dataset changes

---

## Technologies

- Python 3.11+
- Streamlit
- FAISS
- Sentence Transformers
- NVIDIA AI API
- Markdown

---

# System Architecture

> ![alt text](image.png)

---

## Project Structure

```
dataset/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
│
├── ingestion/
├── embeddings/
├── vectorstore/
├── retrieval/
├── generation/
└── utils/
```

---

## How It Works

1. Load all Markdown course notes from the `dataset` folder.
2. Split the notes into smaller chunks.
3. Convert each chunk into embeddings.
4. Store the embeddings in a FAISS vector index.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant note chunks.
7. Send the retrieved content to the NVIDIA AI model.
8. Display the answer with source citations.

---

## Installation

### Requirements

- Python 3.11 or newer

### Install

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file.

```
NVIDIA_API_KEY=your_api_key
NVIDIA_MODEL=nvidia/nemotron-3-super-120b-a12b
```

Add your Markdown course notes into the `dataset` folder.

---

## Run the Project

```bash
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

The first run will create the FAISS index.

Later runs will reuse the existing index unless the dataset changes.

---

## Adding New Notes

1. Add a new `.md` file into the `dataset` folder.
2. Click **Rebuild Index** in the sidebar, or restart the application.

The system will automatically update the vector index.

---

## Settings

The sidebar allows you to change:

- Top-K retrieval
- Embedding model
- Rebuild vector index
- Dataset information

---

## Evaluation

**Evaluation Results**
I ran 9 fixed test questions through the same search-and-answer pipeline used in the Search tab. This was tested against the live dataset: 30 files and 656 chunks, using the all-MiniLM-L6-v2 model.

| # | Question | Top similarity | Result | Notes |
|---|---|---|---|---|
| 1 | What is PageRank and how does it work? | 0.835 | correct | Grounded answer with inline citations. |
| 2 | What is Retrieval-Augmented Generation (RAG)? | 0.557 | correct | Grounded, cites the RAG Architecture notes. |
| 3 | How do you evaluate an information retrieval system? | 0.587 | correct | Grounded in the IR Evaluation notes. |
| 4 | What is a vector database and how is it used in Neural IR? | 0.626 | correct | Grounded in the Neural IR notes. |
| 5 | Explain content-based filtering in recommender systems. | 0.609 | correct | Grounded in the Recommender Systems notes. |
| 6 | What are the key stages of web crawling? | 0.636 | correct | Grounded in the Web Crawling notes. |
| 7 | What ethical issues arise in information retrieval systems? | 0.539 | correct | Grounded in the Ethics in AI notes. |
| 8 | What is the capital of France? (deliberately off-topic) | 0.274 | correctly refused | Caught by the grounding rule, not just because retrieval came back empty. |
| 9 | What is AI? And what is BM-25? (compound, two topics) | 0.796 / 0.541 | correct | Both halves answered and cited correctly. This is the test case for the two-part question fix above. |

## Embedding Model

We use the all MiniLM L6 v2 model to create dense vectors. This ensures we use semantic search instead of simple keyword matching like TF IDF.

```python
from embeddings.encoder import EmbeddingEncoder
encoder = EmbeddingEncoder("all-MiniLM-L6-v2")
vectors = encoder.encode(["search query"])
```

---

## Limitations

- Works best with well-formatted Markdown notes.
- OCR errors from converted PDFs may reduce retrieval quality.
- Conversation history is not saved.
- Very complex multi-part questions may reduce retrieval accuracy.

---

## Deployment

This project can be deployed on **Streamlit Community Cloud**.

### Steps

1. Upload the project to GitHub.
2. Create a new Streamlit app.
3. Add the NVIDIA API key in **Secrets**.

```toml
NVIDIA_API_KEY="your_api_key"
NVIDIA_MODEL="nvidia/nemotron-3-super-120b-a12b"
```

4. Deploy the application.

---

## Future Improvements

Possible improvements include:

- Support for PDF documents without conversion.
- Better query decomposition for complex questions.
- Conversation history.
- More evaluation datasets.
- Additional embedding models.

---

## Author

Developed as the final project for

**CS382 – Search Engine & Information Retrieval**
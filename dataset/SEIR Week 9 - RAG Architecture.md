WEEK9
RAG
ARCHITECTURE
CS382-SEARCH ENGINE&INFORMATION RETRIVAL
INSTRUCTOR: CHHAY KEOKANITHA

How do we get an AI to answer questions
about our private data without retraining the
entire model from scratch?

THE ANSWER IS
Retrieval-Augmented Generation (RAG)
Retrieval: Finding relevant information from a
database.
Augmented: Adding that information to
the user's original question.
Generation: Asking the LLM to write an
answer using only the added
information.

THE OPEN-BOOK TEST ANALOGY
Traditional LLM RAG
(Closed-book exam) (Open-book exam)
The student has read billions of When you ask a question, the system
books in the past, but right now, first runs to a massive library (your
they have to answer questions database), finds the exact pages that
purely from memory. contain the answer.

WHY TRADITIONAL
LLMS FAIL
The high cost of retraining
01.
Fine-tuning is complicated and expensive.
Training cutoffs
02.
LLM was trained in 2025 has no idea what happened
in 2026.
No access to private data
03.
Private data can’t be access.
Hallucinations
04.
If they don't know a fact, they'll guess.
Context window limitations
05.
LLM has limited amount of text it can process at
once.

RAG gives the LLM access to real-time, private
data without needing to retrain the model.

THE OPEN-BOOK SOLUTION
RAG gives the LLM an open book before
it answers. The key steps are:
01 Search your own document collection
for the most relevant passages.
02 Paste those passages directly into the
LLM's prompt as context.
03 The LLM answers only from what it
can read right now, not from memory.

THE TWO PIPELINES AT A GLANCE
Indexing (runs once):
Query (runs every query):

RAG PIPELINE COMPONENTS
| Component | What it does | Class analogy |
| --------- | ------------ | ------------- |
Raw data-hese are your PDFs, database
| Documents |     | The whole textbook |
| --------- | --- | ------------------ |
records, text files, or scraped websites.
Splits a long doc into short overlapping Tearing a textbook into sticky-note-
Chunker
|     | segments | sized pieces |
| --- | -------- | ------------ |
Converts each chunk into a vector (list of GPS coordinates for meaning, similar
Embedder
|     | numbers) | ideas cluster nearby |
| --- | -------- | -------------------- |
Vector store Stores vectors for similarity search A library filed by meaning, not by title
A librarian who fetches the 3 most
| Retriever | Returns the top-k most similar chunks |     |
| --------- | ------------------------------------- | --- |
relevant pages for your question
Reads retrieved context, writes a An open-book exam student, only uses
LLM
|     | grounded answer | pages in front of them |
| --- | --------------- | ---------------------- |

Retrieval-Augmented Generation is the bridge
between incredible reasoning engines (LLMs)
and reliable factual knowledge (your data).

WHAT WE'RE
BUILDING TODAY
| 01. Find Dataset |     |     | 02. Clean Dataset |     |     |     |     |
| ---------------- | --- | --- | ----------------- | --- | --- | --- | --- |
Based  on  selected  topic, Strip  out  noise.  Save  as  .txt. This
gather  10+  pages  of  text is the  knowledge your AI will  live
| on your bot topic. |     |     | inside.         |     |     |     |     |
| ------------------ | --- | --- | --------------- | --- | --- | --- | --- |
| 03. Vector Index   |     |     | 04. Exit Ticket |     |     |     |     |
Your  text  gets  chunked, Each  person  submits  individually.
| converted               | into  | vectors, | Answer 4 questions including the |        |        |       |      |
| ----------------------- | ----- | -------- | -------------------------------- | ------ | ------ | ----- | ---- |
| and stored in ChromaDB. |       |          | exact                            | chunk  | count  | from  | your |
output.

Advanced RAG & Buidling AI Chatbot
Coming soon... I mean Next Week.

WEEK9
THANK YOU
CS382-SEARCH
ENGINE&INFORMATION
RETRIVAL
INSTRUCTOR: CHHAY
KEOKANITHA
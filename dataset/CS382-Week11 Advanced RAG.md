THE JAILBREAK CHALLENGE
Can you break a bot that isn't yours?

SSiittuuaattiioonn PPooiinnttss
Write 3 attack prompts to test another
YYoouurr aattttaacckk bbrreeaakkss aannootthheerr
team's bot ++22 aattttaacckkeerrss
tteeaamm''ss bboott
Defenders watch the output and
YYoouurr bboott ssuurrvviivveess aallll aattttaacckkss ++33 ddeeffeennddeerrss
document what happens
BBoott rreepplliieess ppoolliitteellyy iinnsstteeaadd ooff
++11 bboonnuuss
ccrraasshhiinngg
Fix your prompt live if it breaks that
earns bonus points YYoouu iiddeennttiiffyy tthhee wweeaakknneessss aanndd
++22 ddeeffeennddeerrss
ffiixx iitt lliivvee
Surviving all attacks scores more than breaking one, the strongest bot wins.
If nobody breaks, the instructor attacks live. If all bots survive that too, every team gets full marks.

WEEK11
ADVANCED
RAG ARCHITECTURE
Redefining Technology for a Smarter Tomorrow
INSTRUCTURE: CS382-SEARCH ENGINE &
CHHAY KEOKANITHA INFORMATION RETRIEVAL

YOUR CHATBOT ANSWERS QUESTIONS.
BUT DOES IT ANSWER THEM WELL?
Today we learn how to measure quality and how
to make retrieval smarter.

YOUR BOT WORKS.
BUT HOW DO YOU KNOW IT WORKS WELL?
| Faithfulness | Answer    | Context   |
| ------------ | --------- | --------- |
|              | Relevance | Relevance |
Is the answer
|          | Did it answer what | Did it use the right |
| -------- | ------------------ | -------------------- |
| correct? | was asked?         | chunks?              |
These three questions are the foundation of RAG Evaluation.

RAG EVALUATION METRICS
|              | Metric | Question It Answers      | Good Score Means        |                       | Class Analogy |
| ------------ | ------ | ------------------------ | ----------------------- | --------------------- | ------------- |
|              |        | Is the answer based only |                         | Only use the textbook |               |
| Faithfulness |        |                          | Bot doesn't hallucinate |                       |               |
|              |        | on retrieved chunks?     |                         | pages in front of you |               |
|              |        | Did the bot actually     |                         | Your answer matches   |               |
Answer
|     |     | answer the question | Bot stays on topic | what was asked in the |     |
| --- | --- | ------------------- | ------------------ | --------------------- | --- |
Relevance
|         |     | asked?                 |     | exam                  |     |
| ------- | --- | ---------------------- | --- | --------------------- | --- |
| Context |     | Did ChromaDB fetch the |     | Librarian fetched the |     |
Retrieval is accurate
| Relevance |     | right chunks? |     | correct pages |     |
| --------- | --- | ------------- | --- | ------------- | --- |
Ideal score across all three metrics: as close to 1.0 as possible (scale 0–1)

HOW TO MEASURE RAG
01. 02.
Pick a test question Record the bot's answer
Choose something your bot Save: question, retrieved
should know from its dataset. chunks, and the final answer.
03. 04. 05.
Score faithfulness Score relevance Improve and repeat
Ask: does every Ask: does the answer Adjust system prompt or
sentence in the answer actually address the chunk size and re-test
come from a chunk? question?

QUICK SELF-CHECK
✓ Bot says 'I don't know' when chunk is
missing
✓
Bot doesn't add facts not in the
context
✓
Retrieved chunks actually mention
the topic
✗
Bot answers off-topic questions
confidently
✗ Bot quotes from general knowledge,
not chunks

VECTOR SEARCH IS SMART.
BUT IT MISSES EXACT KEYWORDS.
Vector Search Only Keyword Search Only
• Finds semantically similar chunks • Finds exact word matches
• Great for meaning-based queries • Great for names, codes, IDs
• Misses exact product codes or names • Misses synonyms or paraphrases
• Misses rare keywords • No understanding of meaning
Hybrid Search combines both →

HYBRID SEARCH AT A GLANCE
| User           | BM25    |               | Vector | Score  |              | Top-K  |
| -------------- | ------- | ------------- | ------ | ------ | ------------ | ------ |
| Query          | Keyword |               | Search | Fusion |              | Chunks |
| BM25 (Keyword) |         | Vector Search |        |        | Score Fusion |        |
• Exact word frequency
• Semantic similarity matching • Combine both ranked lists
matching
• Understands meaning and • Reciprocal Rank Fusion (RRF)
• Fast, no GPU needed
context
• Better together than either
• Best for: names, codes,
• Best for: concept questions
alone
titles

HYBRID SEARCH — CODE PATTERN
from rank_bm25 import BM25Okapi
pip install rank-bm25
# BM25 keyword search
tokenized = [c.split() for c in chunks]
bm25 = BM25Okapi(tokenized)
bm25_scores = bm25.get_scores(query.split())
Exact keyword scoring
# Vector search (ChromaDB)
q_vec = embedder.encode([query]).tolist()
Semantic vector scoring
results = collection.query(
query_embeddings=q_vec, n_results=10)
# Reciprocal Rank Fusion
Merge both ranked lists
def rrf(rank, k=60):
return 1 / (k + rank)
Final top-3 for the prompt
# Combine and re-rank
combined = fuse(bm25_scores, vector_scores)
top_chunks = combined[:3]

SIMPLE RAG  VS.  ADVANCED RAG
Simple RAG (Week 9) Advanced RAG (This Week)
✗
| Vector search only | ✓   | Hybrid: BM25 + vector search |
| ------------------ | --- | ---------------------------- |
✓
| ✗ Fixed chunk size |     | Adaptive chunking strategies |
| ------------------ | --- | ---------------------------- |
| ✗ No quality check | ✓   |                              |
Faithfulness + relevance scores
✓
✗ Bot answers even with bad chunks Bot says 'I don't know' when unsure
✗ ✓
| Hard to debug when wrong |     | Evaluation loop guides improvement |
| ------------------------ | --- | ---------------------------------- |

WEEK11
THANK YOU
Redefining Technology for a Smarter Tomorrow
CS382-SEARCH ENGINE & INFORMATION RETRIEVAL
INSTRUCTURE: CHHAY KEOKANITHA

NOW
LET’S PLAY GAME!
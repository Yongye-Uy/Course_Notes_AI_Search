WWWEEEEEEKKK111444
Recap: IR Ethics
RRReeecccooommmmmmeeennndddeeerrr
Recommender
Systems
System
Content-Based
Lab
Content-Based Filtering
Bridge to Final
Project
Presented By: CS382:
CHHAY KEOKANITHA SEARCH ENGINE & INFORMATION RETRIEVAL

WWWhhhaaattt   IIIsss   aaa   RRReeecccooommmmmmeeennndddeeerrr   SSSyyysssttteeemmm???
|               | (01) | (02)          | (03)   |
| ------------- | ---- | ------------- | ------ |
| Content-Based |      | Collaborative | Hybrid |
Filtering
Combines both
| Recommends items | Recommends items liked |     |     |
| ---------------- | ---------------------- | --- | --- |
similar to ones a user by other users with similar approaches for stronger,
| already liked, using item |     |     | more robust |
| ------------------------- | --- | --- | ----------- |
taste.
recommendations.
features.

CCCooonnnttteeennnttt---BBBaaassseeeddd FFFiiilllttteeerrriiinnnggg
Recommends items to a user based on the features of items
that user already liked, not on what other users did.
It is the recommender-systems analogue of a search engine that ranks
documents by similarity to a query - except the “query” is the user's own
preference profile.

HHHooowww   IIIttt   WWWooorrrkkksss
|         | 1   |     | 2   |            | 3   |         | 4   |        | 5   |
| ------- | --- | --- | --- | ---------- | --- | ------- | --- | ------ | --- |
| Extract |     |     |     | Build User |     | Compute |     | Rank & |     |
Vectorize
| Features |     |     |     | Profile |     | Similarity |     | Recommend |     |
| -------- | --- | --- | --- | ------- | --- | ---------- | --- | --------- | --- |
Recommends items to a user based on the features of items
that user already liked, not on what other users did.
Genres, tags, Turn features Average vectors Cosine similarity Return the
text description into numbers of items the user between profile highest-scoring
| of each item |     | (e.g. TF-IDF) |     |     | liked | & items |     | unseen items |     |
| ------------ | --- | ------------- | --- | --- | ----- | ------- | --- | ------------ | --- |

KKKeeeyyy CCCooonnnccceeeppptttsss
Feature Vector A numeric representation of an item's
attributes — e.g. [Action=1,
Comedy=0, Romance=1].
Weighs a word by how important it is
TF-IDF
to one document versus the whole
collection.
Measures the angle between two
Cosine Similarity
vectors; score from 0 (unrelated) to 1
(identical direction).

WWWooorrrkkkeeeddd   EEExxxaaammmpppllleee
A user liked Movie A (Action, Sci-Fi). Which unseen movie is the closer match?
|                 | Item | Action | Comedy |     | Sci-Fi | Cos-Sim to User |           |
| --------------- | ---- | ------ | ------ | --- | ------ | --------------- | --------- |
| Movie A (liked) |      | 1      |        | 0   | 1      |                 | (profile) |
0.99 →
| Movie B |     | 1   |     | 0   | 1   |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
recommend
| Movie C |     | 0   |     | 1   | 0   | 0.02 → skip |     |
| ------- | --- | --- | --- | --- | --- | ----------- | --- |
Because Movie B shares the same feature vector as what the user liked, its cosine similarity
is near 1, a strong content-based match.

SSStttrrreeennngggttthhhsss &&& LLLiiimmmiiitttaaatttiiiooonnnsss
Strengths Limitations
Works for brand-new items (no Overspecialization - the “filter
cold start), as long as features bubble” problem
exist
Needs good feature engineering
Transparent , you can explain why to work well
an item was suggested
Can't borrow insight from what
Personalized to one user's own similar users liked
taste

LLLaaabbb TTTiiimmmeee
Build a Content-Based Recommender
Vectorize a dataset of item descriptions
with TF-IDF
Build a user profile vector from a small
set of “liked” items
Rank all items by cosine similarity to the
profile
Mini project: extend it with your own
dataset and evaluate the top-5
recommendations qualitatively

Today: Content-Based Filtering
BBBrrriiidddgggeee tttooo YYYooouuurrr
Turn content into feature vectors
Compare vectors with cosine similarity
Rank results by relevance
Ahead: Your RAG-Based Search
FFFiiinnnaaalll PPPrrrooojjjeeecccttt
Turn documents into embeddings
Retrieve by vector similarity search
Rank & pass results to the LLM to generate
an answer

FFFiiinnnaaalll PPPrrrooojjjeeecccttt BBBrrriiieeefff
Document ingestion: a real collection in
your chosen domain (20+ documents)
Chunking: split documents with a
A RAG-based AI search system
defensible strategy
that retrieves answers from
Embeddings: real vector representations
YOUR documents and generates
of your chunks
grounded, cited responses - Retrieval: similarity search returning top-k
relevant chunks
through a real, working interface.
Generation: an LLM answer grounded in
retrieved text, with citations
A working interface: query box, answer,
sources, at least one setting

SSSyyysssttteeemmm   AAArrrccchhhiiittteeeccctttuuurrreee
|          | 1   |       | 2   |        | 3   |          | 4   |          | 5   | 6         |
| -------- | --- | ----- | --- | ------ | --- | -------- | --- | -------- | --- | --------- |
| Ingest & |     |       |     | Vector |     |          |     | Generate |     |           |
|          |     | Embed |     |        |     | Retrieve |     |          |     | Interface |
| Chunk    |     |       |     | Store  |     |          |     | (LLM)    |     |           |
Recommends items to a user based on the features of
items that user already liked, not on what other users
did.
Load
|            |     |              |     |                 |     |               |     | Grounded    |     | Query in,   |
| ---------- | --- | ------------ | --- | --------------- | --- | ------------- | --- | ----------- | --- | ----------- |
| documents, |     | Turn chunks  |     | Index vectors   |     | Top-k chunks  |     |             |     |             |
|            |     |              |     |                 |     |               |     | answer with |     | answer +    |
| split into |     | into vectors |     | for fast search |     | by similarity |     |             |     |             |
|            |     |              |     |                 |     |               |     | citations   |     | sources out |
chunks

IIInnnttteeerrrfffaaaccceee RRReeeqqquuuiiirrreeemmmeeennntttsss
Header / Project Title
Query Input + Submit
Settings
Answer Panel
(generated, grounded response)
• top-k slider
• answer mode
Sources Panel • dataset info
(expandable: doc name + similarity score +
snippet)

SSSuuuggggggeeesssttteeeddd   TTTeeeccchhh   SSStttaaaccckkk
| Layer |     | Simple Option | Stronger Option |
| ----- | --- | ------------- | --------------- |
Flask/FastAPI + custom
| Interface | Streamlit or Gradio |     |     |
| --------- | ------------------- | --- | --- |
HTML/JS
OpenAI / Anthropic / Cohere
Embeddings sentence-transformers (local, free)
API
| Vector Store | In-memory cosine similarity |     | FAISS or Chroma |
| ------------ | --------------------------- | --- | --------------- |
Same, with deeper prompt/eval
| Generation | Claude or GPT via API |     |     |
| ---------- | --------------------- | --- | --- |
work
The requirement is the architecture, not a specific library - substitute freely.

Milestones
LINK
(02) Your own documents
(01) Starter project (03) Real embeddings
ingested & chunked
running locally; + retrieval working
domain/dataset chosen end-to-end
(04) LLM generation
(05) Evaluation written (06) Live demo +
wired in; interface
up; interface & docs presentation +
functional
polished portfolio submission

WWWEEEEEEKKK111444
Thank you!
TThhaannkk yyoouu!!
Good Luck On Your Final Project!
Presented By: CS382:
CHHAY KEOKANITHA SEARCH ENGINE & INFORMATION RETRIEVAL
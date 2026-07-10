WEEK8
NEURAL IR &
VECTOR DATABASES
From keyword matching to semantic search and the infrastructure that scales it.
CS382 – Search Engines & Information Retrieval
Present by Chhay Keokanitha

Google processes 8.5 billion
searches per day.
It does NOT read your query.
So what does it actually do?

Reminiscing BM25 & TF-IDF
HOW BM25 WORKS WHY IT FAILS
1. Count word frequency in doc
Query: "car"
2. Penalize very common words Missed: automobile, vehicle, ride
3. Rank by match score
Query: "heart attack"
4. Return highest scored docs
Missed: myocardial infarction
Example: Query ="fast vehicle"
Query: "sad movie"
Matches: = "fast" "vehicle"
Missed: tearjerker, emotional film

| Unlike  | traditional  |     | keyword  |     | methods  | (like |
| ------- | ------------ | --- | -------- | --- | -------- | ----- |
Neural
BM25) that rely on exact matching, Neural
| IR  translates  |     | text  | into  | high-dimensional |     |     |
| --------------- | --- | ----- | ----- | ---------------- | --- | --- |
Information
| vector   | representations  |     |           | (embeddings)  |          | to  |
| -------- | ---------------- | --- | --------- | ------------- | -------- | --- |
| capture  | semantic         |     | meaning,  |               | intent,  | and |
Retrieval
context.

The Neural Fix: Embeddings
V E C T O R S P A C E
encoder("car") → [0.82, 0.14, 0.95 ...]
banana
encoder("automobile") → [0.80, 0.13, 0.97 ...]
fruit
encoder("banana") → [0.02, 0.91, 0.11 ...]
automobile
car
Fruits cluster
→
Similar meaning similar vector
truck
The neural network learns that "car" and "automobile" Vehicles cluster
belong in the same neighborhood with no explicit rules.

BI-ENCODER CROSS-ENCODER
Encode query & doc separately Query & doc processed together
Two Neural Architectures

The Speed vs. Accuracy Trade-off
BI-ENCODER
→
Pre-compute doc vectors millisecond search
Scales to billions of documents
Query & doc never interact during encoding
CROSS-ENCODER
Full attention between query & doc
Much more accurate relevance score
→
Cannot pre-compute must run at query time

The Modern Playbook
The Hybrid Pattern: Retrieve Re-Rank
User Query
WHY THIS WORKS
Natural language input
Speed from Bi-Encoder:
Pre-computed doc vectors allow
Bi-Encoder
millisecond ANN lookup across millions
Top 100 candidates (fast) of docs.
Accuracy from Cross-Encoder
Cross-Encoder
Runs only on Top-100 candidates, the
Re-rank to Top 10 (accurate) heavy computation is now tractable.
Best of Both
Final Results Quality of full-attention models with
near-real-time latency.
Best of both worlds

You've encoded 1 billion
documents. A query arrives.
You have 200ms.
What would you do?

The Brute-Force Trap
1B × cosine similarity = impossibly slow
Calculating exact cosine similarity against all 1 billion elements sequentially (0(N)
complexity) is impossibly slow.

Vector
| A  vector  |     | database      | stores  | and             | indexes |
| ---------- | --- | ------------- | ------- | --------------- | ------- |
| data       | as  | mathematical  |         | representations |         |
Database
called vector embeddings.

Traditional Database Vector Database
Structured rows, columns, and exact
High-dimensional dense vector spaces.
schemas.
Matches exact value queries (WHERE Matches mathematical similarity
name = 'Alice'). (find_nearest(q_vec)).
Relies on Approximate Nearest Neighbor
Relies on rigid B-tree indexes.
(ANN) indexes like HNSW.

Hierarchical Navigable Small World
(HNSW): The Multi-Floor Building Analogy
Floor 3 (Top Floor): Extremely
sparse graph network containing
only major "highway" connections.
Floor 2 (Middle Floor): Medium
density graph network for localized
transitions.
Floor 1 (Ground Floor): Ultra-dense
network where all adjacent
neighbors are connected.
→ → → → →
Algorithm: Enter at top big jumps to the right zone drop down finer search repeat until Floor 1 return nearest

THE VECTOR DB ECOSYSTEM
Pick the Right Tool
| Pinecone        | Weaviate      | Qdrant          |
| --------------- | ------------- | --------------- |
| Production SaaS | Hybrid search | Raw performance |
Fully managed, simple API Built-in Neural IR modules Rust-based, blazing fast
pgvector
| Chroma      | Milvus        |                   |
| ----------- | ------------- | ----------------- |
| Prototyping | Massive scale | Existing Postgres |
Local-first, zero config Billions of vectors Just an extension, familiar

OFFLINE + ONLINE PIPELINE
OFFLINE (done once) ONLINE (every query)
User Query
Documents
→
Bi-Encoder
→
Encoder
↕
→
Vector DB (ANN)
→
Embeddings
→
Cross-Encoder
→
Vector DB
→
Final Results

Enough with the talk. Let’s built the core
of how Google, Spotify,
ChatGPT's memory, and Netflix work.
The difference is scale - not concept.

|     |     | L A B |   P R | A C | T I C | E   |     |     |     |
| --- | --- | ----- | ----- | --- | ----- | --- | --- | --- | --- |
Build a Semantic
Movie Search Engine
| 01     | 02    |     |     |     |     | 03    |     |                  | 04  |
| ------ | ----- | --- | --- | --- | --- | ----- | --- | ---------------- | --- |
| Encode | Store |     |     |     |     | Query |     | Filter + Compare |     |
Natural language
Load 500 movie plots Insert vectors +
→
|     |     |     |     | search  |     |     |  retrieve | Add genre filter. Beat |     |
| --- | --- | --- | --- | ------- | --- | --- | --------- | ---------------------- | --- |
→
 embed with metadata into
the BM25 baseline.
Top-5 semantic
SentenceTransformer ChromaDB collection
matches

WEEK8
THANK YOU
| F O | R   Y | O U | R   A | T T E | N T | I O N |
| --- | ----- | --- | ----- | ----- | --- | ----- |
CS382 – Search Engines & Information Retrieval  Present by Chhay Keokanitha
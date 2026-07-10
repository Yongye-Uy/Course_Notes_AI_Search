PARAGON INTERNATIONAL UNIVERSITY WEEK 4
BM25
Probabilistic Ranking
Presented by : Chhay Keokanitha
CS-382 Search Engine & Information Retrieval

Quick Recall: What Was TF-IDF?
TF-IDF Formula TF-IDF Limitations
1
TF(t,d) × IDF(t) Problem 1: Term Frequency Grows Infinitely
If "search" appears 5× vs 10×, the score doubles — but
relevance doesn't!
TF = how often term appears in doc
IDF = log(N / df) ← penalises common words
Problem 2: No Length Normalization
A 1000-word doc beats a 50-word doc just by having
Simple & effective
more room for terms.
Does NOT cap term frequency
Ignores document length
“BM25 was designed to fix both of these.”
8 What’s Next for Us?

Probabilistic
Given query Q and document D,
Retrieval
estimate:
Models
P(relevant | D, Q)
Probabilistic retrieval models
rank documents based on the
Rank by this probability,
probability of their relevance to a
higher P = top result. user query, aiming to maximize
search effectiveness.

What is
BM25 is a probabilistic ranking function - it
answers:
"What is the probability this document is
relevant to this query?"
BM25?
It measures term frequency and document
relevance more accurately.
(Best
It accounts for document length
normalization, giving fair weight to all
documents.
It is widely used in tools like Elasticsearch,
Match 25)
Whoosh and Lucene.
It helps to deliver more relevant search results
based on keyword matching and context.

The BM25
Formula
|     | k   |     | b   |     | IDF |     | avgdl |
| --- | --- | --- | --- | --- | --- | --- | ----- |
₁
| Term Saturation |     |               | Length |     | Inverse Doc | Avg Document |        |
| --------------- | --- | ------------- | ------ | --- | ----------- | ------------ | ------ |
|                 |     | Normalisation |        |     | Frequency   |              | Length |
Typical: 1.2 – 2.0 Typical: 0.75 Smoothed formula Corpus statistic
Controls how fast b=0: no length penalty. log((N- Mean token count
extra term b=1: full normalisation df+0.5)/(df+0.5)+1). across the full corpus.
occurrences add to by avg doc length. Rare terms score Computed once at
| score. High k₁ = no cap. |     |     |     | higher. |     | index time. |     |
| ------------------------ | --- | --- | --- | ------- | --- | ----------- | --- |

BM25: Building Intuition
|     |     | BM25 (k₁=1.2) |     |     |     | TF-IDF (linear) |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --------------- | --- | --- | --- | --- |
Diminishing Returns
10
Mentioning a word 10x doesn't mean 10x
relevance. BM25 caps contribution —
resists keyword spam.
8
Document Length Penalty
6
Short doc with 'AI' twice is more relevant
than a 10,000-word book with 'AI' twice.
4
Rare Term Bonus
2
'quantum' in a news corpus is rare → high
IDF → big score boost. 'the' gets near-zero.
0
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .   | .   | .   | .   | .   | .   | .   | .   | .   | .   | .   |
| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 0   | 1   |
|     |     |     |     |     |     |     |     |     | 1   | 1   |

Two Brillion Innovation in BM25
① Term Frequency Saturation ② Document Length Normalisation
Problem: Problem:
TF-IDF boosts scores linearly Longer documents contain more terms, creates
A document with 100 mentions ≠ 100× more unfair advantage over shorter, focused content
relevant than one with 5
Leads to keyword stuffing bias Innovation:
BM25 adjusts scores using document length
Innovation: Controlled by parameter b (typically ≈ 0.75)
BM25 applies saturation
Score increases quickly → then levels off Behavior:
b = 1 → strong penalty for long documents
Impact: b = 0 → no normalization
Extra repetitions contribute less over time
Focus shifts from frequency → meaningful Impact:
presence Rewards term density, not document size
Short, relevant docs can outrank long, diluted ones

TF-IDF  vs  BM25
|     | Feature |     | TF-IDF |     | BM25 |
| --- | ------- | --- | ------ | --- | ---- |
Term Freq. Scaling Linear — unbounded Saturated via k₁ parameter
Doc Length Norm Cosine norm (global) Explicit b parameter (local)
Smoothed IDF — handles edge
| Rare Term Boost |     | Standard IDF |     |     |     |
| --------------- | --- | ------------ | --- | --- | --- |
cases
Tunable Params None after weighting k₁ and b — corpus-tuneable
| Performance |     | Good baseline         |     | State-of-art for sparse IR |     |
| ----------- | --- | --------------------- | --- | -------------------------- | --- |
| Typical Use |     | Teaching, prototyping |     | Production search engines  |     |

BM25 is The default BM25
parameters (k1=1.5,
b=0.75) work well for
a probabilistic ranking
most corpora but
model that improves
should be
on TF-IDF with TF
saturation (k1) and
Key tuned
length normalization (b)
Takeaways BM25 is the
BM25 performs best
backbone of
when combined with
Elasticsearch and
Solr, query
industry
expansion &
standard semantic
search
for keyword search

2
1
Implement BM25
Set up notebook,
from Scratch,
Install libraries, clean
Compute DF, IDF,
& tokenize text
and scoring formula
Lab Time!
3
4
Run all cells
Validate with library,
error-free and
compare with TF-
submit Colab link to
IDF, adjust k₁ & b
Classroom

PARAGON INTERNATIONAL UNIVERSITY
WEEK 4
Thank
Let’s Create Something
Amazing Together
Presented by : Chhay Keokanitha
You
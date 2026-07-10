CS382: Search Engines & Information Retrieval - Week 4
IR EVALUATION &
QUERY PROCESSING
BEYOND KEYWORDS: HOW WE
MEASURE AND IMPROVE SEARCH
Presented by: Chhay Keokanitha Paragon International University

Is a search engine "good" because it's fast,
or because the results are right?

THE CORE PROBLEM:
SATISFACTION VS. RELEVANCE
A document is relevant if it addresses the user's
information need, not just because it contains the query
word.
Today's Goals
1.Quantify "Good" using Precision and Recall.
2.Improve "Good" using Query Expansion.

THE CONFUSION
MATRIX IN IR
TRUE NEGATIVES
(TN)
FALSE NEGATIVES
Irrelevant documents
(FN) correctly ignored
(Usually too many to
FALSE POSITIVES Relevant documents
count in IR).
that were missed
(FP)
TRUE POSITIVES (The "Silence").
Irrelevant documents
(TP)
that were retrieved
Relevant documents
(The "Noise").
that were correctly
retrieved

PRECISION - THE QUALITY METRIC
Precision focuses on the accuracy of positive predictions,
answering: Of all the items flagged as positive, how many
were truly positive?
FORMULA
SCENARIO
If you search for "Apple" and get 10 results:
5 are about the fruit
5 are about the tech company
Your precision for the fruit is 50%.

RECALL - THE COMPLETENESS METRIC
The fraction of all relevant documents in the
collection that were successfully retrieved.
FORMULA
SCENARIO
If there are 100 relevant papers on "COVID-19" in a
database and your system only finds 10, your recall is 10%.

THE F1-SCORE
F1 Score is a metric used to evaluate the performance of a classification
model. It combines precision and recall into a single value and is
especially useful when the dataset has imbalanced classes.

FORMULA
It punishes systems
WHY?
that "cheat."
If a system returns every document in the
EXAMPLE library, it has 100% Recall but 0.0001%
Precision. The F1-score will be near zero.

EXERCISE : COMPUTING METRICS
Sc en ar io 2 0 docu men t s t ot a l, 6  a r e r eleva n t .
| Sys  | tem |   A | Ret | u r n | s 10 docs (4   |          |  r eleva   | n t ). |     |
| ---- | --- | --- | --- | ----- | -------------- | -------- | ---------- | ------ | --- |
| Sys  | tem |   B | Ret | u r n | s 5            |  docs (5 |  r eleva   | n t ). |     |
| Task |     |     | Ca  | lcu   | la t e P, R, a |          | n d F1 for |  bot   | h . |
W h ich  syst em is sa fer  for  a  doct or ? W h ich  is bet t er  for
| Disc | u ssion |     |     |     |     |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
a  st u den t  doin g  a  5 -min u t e h omew or k a ssig n men t ?

QUERY PROCESSING
Query processing in Information Retrieval (IR) is
the core mechanism that translates a userʼs rough
"information need" into a specific list of relevant
documents.
The Problem:
Users use "natural language"; documents use
"technical language."
Goal: Bridge the gap through Query Expansion.

THE CORE PROCESSING PIPELINE
When you type a search, the system doesn't just "look for the words."
It follows a multi-stage workflow:
| Par   | sin | g     | an d |     |        |        | Stop  | Word | Qu  | er  | y    |
| ----- | --- | ----- | ---- | --- | ------ | ------ | ----- | ---- | --- | --- | ---- |
|       |     |       |      | Nor | m aliz | at ion |       |      |     |     |      |
| Token |     | iz at | ion  |     |        |        | Rem   | oval | Exp | an  | sion |

MINI-CHALLENGE
QUERY "Remote Work Benefits"
List 3 terms that would increase Recall and 1 term
EXPANSION
CHALLENGE that might accidentally destroy Precision.

METADATA FILTERING & QUERY
REFINEMENT IN IR

METADATA FILTERING QUERY REFINEMENT
Uses structured data (e.g., author, Improves the original query to
date, category, price) better match user intent
Narrows search results using filters
Techniques:
Add constraints (e.g., price < $1000,
Example: brand = Dell)
Query: “machine learningˮ Query expansion (add related terms)
→ Filter by: Year (2023–2025), Type Query reformulation (clarify meaning)
(Research papers), Author Interactive refinement (user adjusts
filters)

COMBINING BOTH
Apply filters + improve query together
|      |     | “elect | r ic ca |     | r sˮ |     |     |     |     |     |
| ---- | --- | ------ | ------- | --- | ---- | --- | --- | --- | --- | --- |
| Exam | ple |        |         |     |      |     |     |     |     |     |
  → Add filt er s: S UV, pr ice < $ 4 0,000, r ecen t  models
|      |     |   → Expa |       | n d: EV, elect |         |       | r ic veh |     | icle     |     |
| ---- | --- | -------- | ----- | -------------- | ------- | ----- | -------- | --- | -------- | --- |
| Resu | l t | M or     | e  ac | c u            | r at e  | an d  | r elev   | an  | t   sear | c h |

= restrict results
METADATA FILTERING
= improve query
QUERY REFINEMENT
Together → better precision + better user experience

SUMMARY
Key Takeaway: Evaluation shows where we are; Query Processing shows where
we can go. Understanding Precision and Recall helps us measure search quality,
while query expansion techniques help us improve it.
NEXT WEEK
LAB SUBMISSION
Indexing and Crawling the Web
Complete worksheet & expansion logic
Presented by: Chhay Keokanitha Paragon International University
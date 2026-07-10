Search
PARAGON INTERNATIONAL UNIVERSITY - CS382
Classic IR: Boolean & Vector
Space Models
Your Journey to Build Your Own Search Engine
PRESENT BY: CHHAY KEOKANITHA

Search
PARAGON INTERNATIONAL UNIVERSITY - CS382
💭
 How does Google decide which result is FIRST?
| Matching words? | Popularity? | Meaning? |
| --------------- | ----------- | -------- |

Search
The Boolean
Retrieval Model
Documents are viewed as a "Bag of Words."
The Boolean Retrieval Model is a classic information retrieval system that identifies relevant
documents based on exact matches, using Boolean logic operators (AND, OR, NOT) to
combine query terms. It treats documents as sets of words, offering binary results - a
document either matches the query or it does not.
AND: all terms must exist OR: any term can exist NOT: excludes specific terms

Search
Boolean Example
Query:
(search OR AI) AND NOT machine
Documents:
D1: AI improves search engines
D2: Search engines use indexing
D3: AI and machine learning
Which documents match?

Search
The Binary
Incidence Matrix
This is the "brain" of the Boolean engine. You can represent your entire library (corpus) as a table of 1s and 0s.
1 = Term is present.
0 = Term is absent.
Doc 3: "Data Science with
| Term | Doc 1: "Python for Data" |     | Doc 2: "Java Basics" |     |     |
| ---- | ------------------------ | --- | -------------------- | --- | --- |
R"
| Python |     | 1   |     | 0   | 0   |
| ------ | --- | --- | --- | --- | --- |
| Data   |     | 1   |     | 0   | 1   |
| Java   |     | 0   |     | 1   | 0   |

Search
Advantages and
Disadvantages
Pros:
Simple to understand, precise, and efficient for large datasets.
Cons:
Does not support ranking, cannot handle partial matches or synonyms (e.g., "car" vs. "automobile"), and requires users
to know exact terminology.
Over-constrained: Query is too specific $\rightarrow$ 0 results.
Under-constrained: Query is too broad $\rightarrow$ 50,000 results.

Search
PARAGON INTERNATIONAL UNIVERSITY - CS382
What if we could…
Measure importance?
Rank results?
Find the BEST match?

Search
The Vector Space Model (VSM)
| an  | algebraic  | framework  | for  information |     |
| --- | ---------- | ---------- | ---------------- | --- |
retrieval and natural language processing that
| represents  |     | text  documents  | as  vectors  | in  a |
| ----------- | --- | ---------------- | ------------ | ----- |
multi-dimensional space.
| Goal:  |   To       | turn  "language"  | into  "math"  | so  we   |
| ------ | ---------- | ----------------- | ------------- | -------- |
| can    | calculate  | the  distance     | between       | a  query |
and a document.
Documents = vectors Words = dimensions Similarity = closeness

Search
Advantages and Limitations
Advantages:
Simple to implement, supports partial matching
(ranking), and handles large document collections
efficiently.
Limitations:
Ignores word order and syntax.
No Semantic Understanding: Synonyms or
semantically related terms are not recognized
(e.g., “car” vs “automobile”).

Search
Not all words are created equal.
The "Noise" ("the", "a", "is"): Appear in almost every document. But the search value is Near Zero. They don't help us
distinguish Doc A from Doc B.
The "Signal" ("AI", "Quantum", "Krav Maga"): Appear rarely in the collection but frequently in specific topics. Search Value is
High because these are the "keywords."
The Goal: We need a mathematical way to reward "Signal" and penalize "Noise."

Search
The TF-IDF Formula
This is the "Heart" of classic search engines.
t: The term (word) you are looking at.
d: The specific document.
N: Total number of documents in your "library."
DF(t): Document Frequency (how many docs contain this word?).

Search
TF (Term Frequency)
Term Frequency (TF): Measures how often a word appears in a document. A higher frequency suggests greater
importance. If a document mentions "AI" five times, it’s probably more relevant than a document that mentions it once.
Formula:
Example: Doc = "AI search AI"
Raw Count: 2
Normalized TF: ⅔ approx. 0.66 (Total words = 3)
In Python, you'll use collections.Counter to build this dictionary in one line.

Search
IDF (Inverse Document
Frequency)
Inverse Document Frequency (IDF): Reduces the weight of common words across multiple documents while increasing
the weight of rare words. If a term appears in fewer documents, it is more likely to be meaningful and specific.
Formula:
Example: The Common Word ("is"), Total Docs ($N$): 10,000 , Document Frequency (DF):
10,000 (It appears in every single document)
The Math: R atio = 10,000 / 10,000 = 1
IDF = log (1) = 0
10
Result: The weight is 0. Even if a document mentions "is" 50 times, its TF-IDF score stays 0.
It is invisible to the search engine.

Search
The "Sweet Spot" Intuition
To win the ranking game, a word must be:
1.Frequent in ONE specific document (High TF).
2.Rare across the REST of the collection (High IDF).
| Word  | Local (TF) | Global (IDF) | Final TF-IDF    |
| ----- | ---------- | ------------ | --------------- |
| "the" | High       | Very Low     | Zero/Negligible |
| "AI"  | High       | High         | MAXIMUM         |

Search
Mini Case Study
1.Documents:
D1: "AI search AI"
D2: "search engine"
2.The Scenario:
A user searches for "AI".
"search" appears in 100% of documents (IDF = 0).
"AI" appears in 50% of documents (IDF > 0).
3.Result:
Even though "search" is in both docs, "AI" is the "informative" word.
D1 will rank significantly higher because it "owns" the rarer term.

Search
From Theory to Code
Now we build a search engine
Compute DF Rank Results
Tokenize text
Create a global dictionary to Compare the user query
Clean the text. Convert
track how many documents against your document
sentences into lists of
in the collection contain scores and sort() the results
words using .lower() and
each unique word. from highest to lowest.
.split().
Compute TF
Compute TF-IDF
Create a dictionary for each
Iterate through your tokens
document to count word
and apply the formula.
occurrences.
Submission Instructions: Open your notebook in Google Colab > Click “Share” (top right)
Google Colab > Change access to “Anyone with the link → Viewer” > Copy the link > Submit the link in
Google Classroom under the "Assignment of Week 3" post.

Search
PARAGON INTERNATIONAL UNIVERSITY - CS382
THANK YOU!
PRESENT BY: CHHAY KEOKANITHA
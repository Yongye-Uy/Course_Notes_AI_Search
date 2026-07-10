Python for IR & Text Processing

 CS382 – Week 2: From Raw Text to Searchable Index

Chhay Keokanitha

Mission

By the end of this lab, you will generate a
JSON file containing word frequencies
from a sample text.

C++ vs.
Python

In 2026, we use Python for IR because developer
time is more expensive than CPU time.

C++: 50 lines to clean a string, manage
memory, and handle pointers.
Python: 4 lines using NLTK and built-in
string methods.

The IR Preprocessing Pipeline

In Information Retrieval (IR), the Preprocessing Pipeline is a sequence of text
transformations that converts raw, human language into a standardized format
that a computer can efficiently index and search.

Raw Data

Case
Folding

Tokeniza
-tion

Filtering

Stemming

The "Dirty" input.

Standardizing to
lowercase.

Chopping sentences
into words.

Removing "Stop-
words" (the, is, a).

Reducing words to
their root (running
to run).

What is Stemming?

The Rule: We "lose" the suffix to "gain" a
match in our search engine.

Example: Informative, Information,
Informed -> inform

Tool: We will use the Porter Stemmer
algorithm today.

Connections

Connection

Connect

The "JSON" Goal

This file is the "Brain" we need for Week 3 (TF-IDF Ranking).

The "Golden Rules"

The 5-Minute Rule: If you are stuck for
5 minutes, ask a neighbor. If they can’t
fix it, raise your hand.

The "Print" Rule: If you don't know
what's happening, print(your_variable).

Deadline: Upload your index.json to the
Google Classroom before the end of
the session.

Let’s Code!

Step 1: Open the Colab Link from the LMS.

Step 2: CRITICAL: Click File > Save a copy

in Drive.

Step 3: Run the "Setup" cell at the top.

Step 4: Follow the "Sprints" in the

notebook.

Help: Use the "Hints & Snippets" section at

the bottom of the notebook!

GoogleColab

Thank You

"The code you write makes you a programmer. The code
you delete makes you a good one."

— Mario Fusco.


PARAGON INTERNATIONAL UNIVERSITY - CS382
| T   | H   | E   |   M |     | A   | G   | I C |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B   | E   | H   | I N |     | D   |   T | H   | E   |
| S   | E   | A   | R   | C   | H   |   B | O   | X   |
SEARCH ENGINES & INFORMATION RETRIEVAL
PRESENT  BY: CHHAY KEOKANITHA

Who searched online today?
What’s the weirdest search
you’ve ever done?

You search every day…
today you learn how it actually works.

PARAGON INTERNATIONAL UNIVERSITY - CS382
COURSE JOURNEY
What you will learn:
How search engines work
How data is organized and retrieved
How to build a simple search system
Final Outcome:
Build your own mini search engine
Skills:
Problem-solving, data thinking, system design
The Goal: “Moving from User to Engineer.”

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
WHY THIS MATTERS?
Every day, you decide what to watch, buy, learn, and believe…
→
And almost every time you search first
Billions of searches daily Top 3 results = most clicks Page 2 = invisible

Ranking matters more than Relevance.

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
THE "BIG FIVE" OF IR
Query
1.
What the user wants/ what YOU type.
Document
2.
What the system stores.
Index
3.
how system organizes data
Relevance
4.
Does this match the intent?
Ranking
5.
What is the best match?

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
IR VS DATABASE
Check the requests below. If you think there is only one exact, right answer, mark 'DATABASE!' If
you think the answer depends on context, opinion, or ranking, mark 'IR!'
Query Answer
What is my current bank account balance?
Show me my current GPA.
The best pizza in Phnom Penh.
How tall is Mount Everest?
Apple
That movie where the guy stays on a planet alone and grows potatoes.
restaraunt phnom penh open now

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
IR VS DATABASE
Check the requests below. If you think there is only one exact, right answer, mark 'DATABASE!' If
you think the answer depends on context, opinion, or ranking, mark 'IR!'
Query Answer
What is my current bank account balance? Database
Show me my current GPA. Database
The best pizza in Phnom Penh. IR
How tall is Mount Everest? Both
Apple IR Disambiguation
That movie where the guy stays on a planet alone and grows potatoes. IR Semantic Search
restaraunt phnom penh open now IR handles Uncertainty

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
THE CORE PHILOSOPHY
Database (Data Retrieval) IR (Information Retrieval)
Focuses on finding a needle in a Focuses on finding the best needle
haystack. It assumes the user among many similar needles. It assumes
knows exactly what they want and the user’s request might be vague and the
that the data is perfectly organized. data is messy (like the internet).

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
TECHNICAL COMPARISON TABLE
| Feature | Database System (DB)              | Information Retrieval (IR)         |
| ------- | --------------------------------- | ---------------------------------- |
|         | Structured: Tables, rows, columns | Unstructured: Text, images, video, |
Data Structure
|     | (SQL).                      | web pages.                   |
| --- | --------------------------- | ---------------------------- |
|     | Formal: Select * From Users | Natural: "How to fix a leaky |
Query Style
|     | Where ID=101.                | faucet?"                            |
| --- | ---------------------------- | ----------------------------------- |
|     | Exact: 100% match or nothing | Partial: Uses similarity scores and |
Matching Logic
|     | (Boolean).                           | "best guess."                   |
| --- | ------------------------------------ | ------------------------------- |
|     | A Set: A list of items that meet the | A Ranking: Results ordered from |
Result Type
|     | criteria.                          | most to least relevant.        |
| --- | ---------------------------------- | ------------------------------ |
|     | Zero: A typo in a query returns an | High: Corrects "restaraunt" to |
Error Tolerance
|     | error.                         | "restaurant."                     |
| --- | ------------------------------ | --------------------------------- |
|     | Correctness: Data must be 100% | Relevance: Data must be useful to |
Primary Goal
|     | accurate. | the user. |
| --- | --------- | --------- |

PARAGON INTERNATIONAL UNIVERSITY - CS382
SEARCH ENGINE BATTLE
Step 2: Run the Same Query
Step 1: Form Groups
“Best travel destinations 2026”
Each group = ONE search engine:
“How to make money online”
Google | Bing | DuckDuckGo | YouTube
Find:
Top 3 results
Pick the BEST one
Step 3: Discuss (60 sec)
Step 4: Defend Your Engine (30 sec)
Why is your result ranked #1?
What’s different or surprising?
“Our best result is ___ because ___”

Search engines don’t just find information…
they decide what matters.

PARAGON INTERNATIONAL UNIVERSITY - CS382
CORE CONCEPT:
RELEVANCE
Relevance = How useful a result is for the user
NOT always:
The most accurate
The most popular
The same for everyone
There is no single “best” result.
It depends on:
The user
The context
The search engine

PARAGON INTERNATIONAL UNIVERSITY - CS382
IR MODELING
HOW SEARCH ENGINES THINK
| Boolean Search |     | Keyword Search | Context Search |
| -------------- | --- | -------------- | -------------- |
Uses logic: AND / OR / NOT Matches words in your query Tries to understand meaning &
Very strict, very precise Doesn’t fully understand meaning intent
Uses behavior, location, trends
| Example: | Example: |     |     |
| -------- | -------- | --- | --- |
→
| apple AND phone  |  only | Search: “cheap laptop” | Example: |
| ---------------- | ----- | ---------------------- | -------- |
“apple” 🍎 vs Apple 💻
| results with BOTH |     | Results: pages that contain cheap |     |
| ----------------- | --- | --------------------------------- | --- |
→
| apple NOT fruit  |  removes | + laptop | “jaguar” 🐆 vs Jaguar 🚗 |
| ---------------- | -------- | -------- | ---------------------- |
🍎 results
Problem:
Might miss better results with
different wording (“affordable
notebook”)

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
WHY WERE YOUR RESULTS DIFFERENT?
There is NO single “correct” result
 Personalization
|  Ranking Logic           | Data                     |     |                 |
| ------------------------ | ------------------------ | --- | --------------- |
| Each engine decides what | Not all engines have the |     | Location        |
| matters:                 | same content             |     | Search history  |
→
| Popularity  | If it’s not indexed  |  it | Your behavior |
| ----------- | -------------------- | --- | ------------- |
| Freshness   | doesn’t exist        |     |               |
Engagement

PARAGON INTERNATIONAL
UNIVERSITY - MIS 380
COURSE JOURNEY
Learn Information Retrieval by exploring how search really
works. Build your own search systems, experiment with
ranking and relevance, and understand how data is
transformed into meaningful results in real-world
applications.
Homework (20%) Participation & Activities (20%)
Midterm & Final Project (60%)
Discussions, critiques, and mini
Build your own design work (Case A fully researched and prototyped
exercises.
studies, sketches, critiques). app/solution.

PARAGON INTERNATIONAL UNIVERSITY - CS382
WRAP-UP
IR is Everywhere
Good Ranking = Success
You are now IR Engineers
Every time you open an app after this class, ask yourself:"
a.Why is this result #1? (Is it relevance, or is it an ad?)
b.How did it know I wanted this? (Did it use my location?
My history?)
c.What would happen if I changed one word in my query?

PARAGON INTERNATIONAL UNIVERSITY - CS382
HOMEWORK
1.Pick a topic you are passionate about
(e.g., "Mechanical Keyboards").
2.Search it on 3 different platforms.
3.Write 1 sentence: Which platform
understood your intent best and why?

THANK
YOU!
PRESENT BY: CHHAY KEOKANITHA
WEEK12
THE PAGERANK
ALGORITHM
How links turn the web into a popularity vote and how we compute it.
Presented By: CS382:
CHHAY KEOKANITHA SEARCH ENGINE & INFORMATION RETRIEVAL

BEYOND KEYWORD
FREQUENCIES
The Lexical Limitation
Early search models relied solely on TF-IDF
lexical matching. Spammers quickly exploited
this by stuffing pages with invisible keywords,
destroying search relevance.
The Link-Structure Pivot
Google's seminal insight treated the World Wide
Web as a directed graph, where pages are
nodes and hyperlinks are directed edges
representing citations or paths.

LINKS AS VOTES OF
CONFIDENCE
Recursive definition
| Not  | all  hyperlinks  |     | are   | created  | equal.         | A  link  | from |
| ---- | ---------------- | --- | ----- | -------- | -------------- | -------- | ---- |
| an   | authoritative    |     | node  | passes   | significantly  |          | more |
value than a link from a minor personal blog.
A vote of confidence
| A  web  | page  | has  | high  | PageRank  | if  it  | is  linked  | to  |
| ------- | ----- | ---- | ----- | --------- | ------- | ----------- | --- |
by many other pages, OR if it is linked to by a few
highly authoritative pages.

THE RANDOM SURFER MODEL
Imagine a person clicking links forever, completely at random.
At each page, they pick one of the outgoing links uniformly at random.
Sometimes they get bored and jump to a totally random page instead (the damping factor).
Standard Surfing Dead Ends Spider Traps
The surfer lands on a Pages with zero out- Self-contained loops
random page and links trap the surfer. keep surfers infinitely
recursively clicks This bleeds probability circular, inflating their
outbound hyperlinks with mass completely out of scores artificially.
equal probability. the graph.
PageRank = the fraction of time the surfer spends on each page, in the long run.

THE TELEPORTATION SOLUTION
Resolving Structural Anomalies
| To  prevent  |     | dead  |              | ends  |     | and    | spider  | traps      | from |     |
| ------------ | --- | ----- | ------------ | ----- | --- | ------ | ------- | ---------- | ---- | --- |
| breaking     |     | the   | probability  |       |     | flow,  | we      | introduce  |      | a   |
damping factor (typically d = 0.85).
| With       | 85%  | probability,  |     |     |        | the  | surfer  | continues |      |     |
| ---------- | ---- | ------------- | --- | --- | ------ | ---- | ------- | --------- | ---- | --- |
| following  |      | structured    |     |     | links  | on   | the     | page.     | With |     |
Damping Factor (d)
| 15%  | probability,  |     |     | the  | surfer  |     | "teleports"  |     | to  | a   |
| ---- | ------------- | --- | --- | ---- | ------- | --- | ------------ | --- | --- | --- |
totally random page across the entire web.

PageRank is an algorithm originally developed by
Larry Page and Sergey Brin (Google’s Founders) to
rank web pages in search engine results.
Core Idea: A page is important if it is linked to by other important pages.

SOLVED EXAMPLE
Here we will apply page rank algorithm and find the final page rank values for
the following given pages → A, B, C, D
A → B, C
B
B → C
A
C
C → A
D
D → A

THE PAGERANK FORMULA
B
N: Total nodes in graph. There are four pages → hence N= 4
d: Damping parameter d = 0.85
A C
PR(p): PageRank score of page p (what we're solving for)
L(q): is the number of outbound links from page q.
D
q → p: Any page q that has a link pointing to p.

PAGERANK EQUATIONS FOR EACH PAGE
B
A C
D

PAGERANK ITERATION 1
Using Initial Values
B
A
C
D

PAGERANK ITERATION 2
Using Iteration 1 Values

PAGERANK ITERATION 3
Using Iteration 2 Values

PAGERANK ITERATION 4
To until convergence
B
A C
D
Convergence is reached when the values
stop changing significantly (<= 0.0001
difference between iterations).

THE POWER ITERATION WORKFLOW
2. Distribute 4. Converge
Calculate incoming Loop until variation
scores from links drops below tiny
simultaneously. delta threshold.
1. Initialize 3. Teleport
Every page starts Apply the global
with an equal (1-d)/N offset to
probability of 1/N. prevent losses.

HANDLING GRAPH PITFALLS
Spider Traps Dead Ends / Sinks
A closed loop of nodes. Without Nodes without outgoing edges. They act
teleportation, PageRank is pooled as "leaks" that drain the rank out of the
inside, eventually reducing all external graph system during iterative steps.
node ranks to zero.

“
The web page link graph is the most robust signal of quality
we have. Keyword text represents what users claim,
whereas inbound links are what users validate.
— SERGEY BRIN, STANFORD IR CONFERENCE

LET'S CODE!
Access your CS382 Google Colab Lab Notebook now to build your manual iteration loop.
Part 1 Build the Graph Part 2 Implement PageRank
Load a sample edge-list dataset and Code the iterative update from scratch,
construct a directed graph with NetworkX. no nx.pagerank() yet.
Part 3 Visualize Results Part 4 Apply & Reflect
Run on a new dataset, compare to
Render the graph with node size/color
NetworkX's built-in function, answer
scaled to PageRank score.
reflection questions.

WEEK12
TTHHAANNKK
YYoouu
Presented By: CS382:
CHHAY KEOKANITHA SEARCH ENGINE & INFORMATION RETRIEVAL
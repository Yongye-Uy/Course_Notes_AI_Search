Chapter IV:

Unsupervised Learning

Sreang Rathanak

Outline

1. Unsupervised Learning

2. Representations

3. Structure

4. Types of unsupervised learning

5. K-means Clustering

6. Summary

2

1. Unsupervised Learning

Unsupervised learning is a type of machine learning where the algorithm learns to
identify patterns in data without being explicitly told what those patterns are. The
goal of unsupervised learning is to uncover hidden structure or relationships in the
data, or to ﬁnd groups or clusters of similar data points.

In unsupervised learning, the input data is not labeled and the algorithm must ﬁnd
a  way  to  organize  the  data  into  meaningful  groups  or  patterns.  This  is  done  by
identifying similarities or differences between the data points and grouping them
accordingly.

3

1. Unsupervised Learning

The Labeled Data

4

1. Unsupervised Learning

Unlabeled Data

5

1. Unsupervised Learning

Where are the labels?

● Labelling data is expensive/costly
● Labelling data may be unreliable
● Labelling data may be impossible

And  real  learning  (i.e.:  humans)  happens  in  an  unsupervised  way!  (very  little
supervision was provided when you were learning as an infant)

6

1. Unsupervised Learning

In unsupervised learning, we are given only  a data matrix (X):

No explicit label is provided (no Y)

7

1. Unsupervised Learning

Where are we mapping this data matrix?

8

1. Unsupervised Learning

What function do we learn?

How do we compute outputs for the samples?

The problem in unsupervised learning are:

● What to learn?
● How to learn?

9

1. Unsupervised Learning

In  general,  we  cannot  solve  the  unsupervised  learning  problem  with  making
assumptions.

10

2. Representation

We try to learn new representation of the data:

11

2. Representation

12

2. Representation

13

2. Representation

What do we want to learn? We learn representations.

14

3. Structure

We want to preserve relevant structure in the data:

Where:

●    preserves relevant information useful for your objective; relevant

information is kept, noise is discarded.

● Natural structure of the data is preserved; relevant relationships between data

points are maintained.

We basically deﬁne relevant structures through assumptions

15

3. Structure

Some simple and intuitive assumptions about structure”

● Locality: points close to each other in the original space are similar; it should

be mapped similar representations.

● Smoothness: transition in representations should be smooth

16

3. Structure

Even simple assumptions require careful evaluation. So how do we measure the
closeness of the points that are close to each other?

17

3. Structure

In unsupervised learning, we try to learn representations while also preserving
relevant structure.

This requires making assumptions.

● If we design an unsupervised learning algorithm, we need to decide what

structure matters;

● If we use existing algorithm, we need to understand what structure they

preserve.

Assumptions are strongly related to the aim of unsupervised learning.

18

4. Types of Unsupervised learning

Unsupervised learning algorithms include

● K-means clustering
● Hierarchical clustering
● Principal Component Analysis (PCA)
● t-SNE
● Association rule mining

19

5. K-means clustering

● Partitional clustering approach
● Number of clusters, K, must be speciﬁed
● Each cluster is associated with a centroid (center point)
● Each point is assigned to the cluster with the closest centroid
● The basic algorithm is very simple

20

Example of K-means Clustering

21

Example of K-means Clustering

22

5. K-means Clustering

● Simple iterative algorithm.

○
○
○

Choose initial centroids;
repeat {assign each point to a nearest centroid; re-compute cluster centroids}
until centroids stop changing.

● Initial centroids are often chosen randomly.
Clusters produced can vary from one run to another

○

● The centroid is (typically) the mean of the points in the cluster, but other deﬁnitions

are possible

● K-means will converge for common proximity measures with appropriately deﬁned

centroid

● Most of the convergence happens in the ﬁrst few iterations.

○

Often the stopping condition is changed to ‘Until relatively few points change clusters’

● Complexity is O( n * K * I * d )

○

n = number of points, K = number of clusters, I = number of iterations, d = number of attributes

23

K-means Objective Function

● A common objective function (used with Euclidean distance measure) is

Sum of Squared Error (SSE)

○
○

For each point, the error is the distance to the nearest cluster center
To get SSE, we square these errors and sum them.

● x is a data point in cluster Ci and mi is the centroid (mean) for cluster

Ci

● SSE improves in each iteration of K-means until it reaches a local or

global minima.

24

Two different K-means Clusterings

25

Importance of Choosing Initial Centroids …

26

Importance of Choosing Initial Centroids …

27

Importance of Choosing Initial Centroids

Depending on the choice of initial centroids, B and C may get merged or
remain separate

28

Problems with Selecting Initial Points

● If there are K ‘real’ clusters then the chance of selecting one centroid

from each cluster is small.

○ Chance is relatively small when K is large
○
If clusters are the same size, n, then

●
●

For example, if K = 10, then probability = 10!/1010 = 0.00036
Sometimes the initial centroids will re-adjust themselves in ‘right’ way, and
sometimes they don’t

● Consider an example of ﬁve pairs of clusters

29

Solutions to Initial Centroids Problem

● Multiple runs

○ Helps, but probability is not on your side

● Use some strategy to select the k initial centroids and then select among

these initial centroids

○

Select most widely separated

■

K-means++ is a robust way of doing this selection
○ Use hierarchical clustering to determine initial centroids

● Bisecting K-means

○ Not as susceptible to initialization issues

30

Multiple Run: Handling Empty Clusters

● Basic K-means algorithm can yield empty clusters
● Several strategies:

○ Choose the point that contributes most to SSE
○ Choose a point from the cluster with the highest SSE
○

If there are several empty clusters, the above can be repeated several times.

31

Pre-processing and Post-processing

● Pre-processing

○ Normalize the data
○

Eliminate outliers

● Post-processing

○
Eliminate small clusters that may represent outliers
○
Split ‘loose’ clusters, i.e., clusters with relatively high SSE
○ Merge clusters that are ‘close’ and that have relatively low SSE
○ Can use these steps during the clustering process

■

ISODATA (Iterative Self-Organizing Data Analysis Technique):

● Minimum  number  of  members  in  a  cluster  is  fall  below  then  that  cluster

eliminated;

● Maximum  standard  deviation  (std.  dev)  exceeds  the  threshold  then  that

cluster is split into two

32

Bisecting K-means

● Bisecting K-means algorithm

○

Variant of K-means that can produce a partitional or a hierarchical clustering

33

Bisecting K-means Example

34

  Limitations of K-means

● K-means has problems when clusters are of differing

○
Sizes
○ Densities
○ Non-globular shapes

● K-means has problems when the data contains outliers.
○ One possible solution is to remove outliers before clustering

35

Limitations of K-means: Differing Sizes

36

Limitations of K-means: Differing Density

37

Limitations of K-means: Non-globular Shapes

38

Overcoming K-means Limitations

39

Overcoming K-means Limitations

40

Overcoming K-means Limitations

41

6. Summary

● Unsupervised  learning  is  a  type  of  machine  learning  where  the  model  is

trained on unlabeled data to identify patterns and structure in the data.
learn  to  represent  the  data

learning  algorithms

● Unsupervised

in  a

lower-dimensional space, making it easier to analyze and visualize.

● Representation learning is the process of learning a representation of the data

that captures its underlying structure, patterns, and relationships.

● Structure  learning  is  the  process  of  discovering  the  hidden  structure  in  the

data, such as clusters, groups, or hierarchies.

● K-means clustering is an unsupervised learning algorithm that partitions a set

of data points into k clusters based on their similarity to one another.

● The  goal  of  K-means  clustering  is  to  minimize  the  distance  between  each

data point and the center of its corresponding cluster.

42

Thanks for your attention!

43


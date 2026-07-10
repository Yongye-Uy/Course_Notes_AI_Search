Chapter III:
Supervised Learning
Sreang Rathanak

Outline
1. Learning
2. Supervised Learning
2.1. Supervised Learning: Regression
2.2. Supervised Learning: Classification
3. Classification: Nearest Neighbor Classifiers
4. Summary
2

1. Learning
”The activity or process of gaining knowledge or skill by studying, practicing, being
taught, or experiencing something.”
Merriam Webster dictionary
“A computer program is said to learn from experience E with respect to some class
of tasks T and performance measure P, if its performance at tasks in T, as measured
by P, improves with experience E” Tom Mitchell
3

1. Learning
An agent is learning if it improves its performance on future tasks after making
observations about the world.
Any component of an agent can be improved by learning from data. The
improvements, and the techniques used to make them, depend on four major
factors:
● Which component is to be improved
● What prior knowledge the agent already has
● What representation is used for the data and the component
● What feedback is available to learn from
4

1. Learning
Types of machine learning:
● Supervised learning: have labeled examples of the correct behavior
● Unsupervised learning: no labeled examples – instead, looking for
“interesting” patterns in the data
● Reinforcement learning: learning system (agent) interacts with the world and
learns to maximize a scalar reward signal
5

2. Supervised Learning
Supervised learning is a type of machine learning in which an algorithm learns to
make predictions or decisions based on labeled training data.
6

2. Supervised Learning
The goal of supervised learning is to learn a function or model that can predict the
output variable for new inputs that were not seen during training.
The algorithm learns by adjusting its internal parameters based on the prediction
error, which is the difference between the predicted output and the actual output
for the labeled examples in the training data.
There are two types of supervised learning: classification and regression.
7

2.1. Supervised Learning: Regression
Regression Algorithms:
● Linear Regression ● Random Forest Regression
● Polynomial Regression ● Support Vector Regression
● Ridge Regression ● Gradient Boosting Regression
● Lasso Regression ● XGBoost Regression
● ElasticNet Regression ● LightGBM Regression
● Decision Tree Regression ● CatBoost Regression
8

Example of Regression
| ● Given | (x1, y1),   | (x2, y2),     | ..., (xn,  | yn)     |     |
| ------- | ----------- | ------------- | ---------- | ------- | --- |
| ● Learn | a function  | f(x)          | to predict | y given | x   |
| ●  y is | real-valued | == regression |            |         |     |
9

Homework
10

2.1. Supervised Learning: Classification
Classification Algorithms:
● XGBoost Classification
● Logistic Regression
● LightGBM Classification
● Decision Tree Classification
● CatBoost Classification
● Random Forest Classification
● Neural Network Classification
● Naive Bayes Classification
● K-Nearest Neighbors
● Support Vector Classification
Classification
● Gradient Boosting Classification
11

Example of Classification
| ● Given | (x1, y1),   | (x2, y2),         | ..., (xn,  | yn)     |     |
| ------- | ----------- | ----------------- | ---------- | ------- | --- |
| ● Learn | a function  | f(x)              | to predict | y given | x   |
| ● y is  | categorical | == classification |            |         |     |
12

3. Classification: Nearest Neighbor Classifiers
Basic idea: If it walks like a duck, quacks like a duck, then it’s probably a duck
13

3. Classification: Nearest Neighbor Classifiers
Requires the following:
● A set of labeled records
● Proximity metric to compute distance/similarity
between a pair of records (e.g., Euclidean
distance)
● The value of k, the number of nearest neighbors to
retrieve
● A method for using class labels of K nearest
neighbors to determine the class label of
unknown record (e.g., by taking majority vote)
14

3. Classification: Nearest Neighbor Classifiers
● Take the majority vote of class labels among the k-nearest
neighbors
● Weight the vote according to distance
○ weight factor, 𝑤 = 1/𝑑2
15

3. Classification: Nearest Neighbor Classifiers
● Attributes may have to be scaled to prevent distance measures from being
dominated by one of the attributes
○ Example:
■ height of a person may vary from 1.5m to 1.8m
■ weight of a person may vary from 90lb to 300lb
■ income of a person may vary from $10K to $1M
● Time series are often standardized to have 0 means a standard deviation
of 1
16

3. Classification: Nearest Neighbor Classifiers
● Nearest neighbor classifiers are local classifiers
● They can produce decision boundaries of arbitrary shapes.
17

Algorithm
18

4. Summary
Advantages:
● Accuracy: Supervised learning algorithms can achieve high accuracy levels
when trained on large and representative datasets.
● Efficiency: Supervised learning algorithms can quickly learn to recognize
patterns and make accurate predictions based on new input data.
● Wide range of applications: Supervised learning is used in many real-world
applications, such as image and speech recognition, natural language
processing, fraud detection, and recommendation systems.
● Transparency: Supervised learning algorithms are often transparent and can
provide insights into the decision-making process.
19

4. Summary
Disadvantages:
● Limited applicability: Supervised learning algorithms require labeled data, which can be
expensive and time-consuming to obtain. This limits their applicability in domains where
labeled data is scarce or non-existent.
● Overfitting: Supervised learning algorithms can overfit to the training data, which means
they learn the noise in the data instead of the underlying patterns. This can lead to poor
generalization and low accuracy on new data.
● Bias: Supervised learning algorithms can also be biased towards certain groups or classes
if the training data is unbalanced or if the algorithm is not designed to handle bias.
● Dependence on input quality: The accuracy of supervised learning algorithms is highly
dependent on the quality of the input data. If the input data is noisy, incomplete, or biased,
the accuracy of the model can suffer.
20

Thanks for your attention!
21
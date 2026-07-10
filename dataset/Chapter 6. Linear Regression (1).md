Chapter VI
Linear Regression
Sreang Rathanak
December 14, 2024
| SreangRathanak | ChapterVI | December14,2024 | 1/6 |
| -------------- | --------- | --------------- | --- |

Linear Regression
Linear Regression is a modeling technique that predicts an output value, y,
as a linear combination or equation of a set of independent numeric input
variables, x .
i
| Multiple independent | variables: |               |     |     |
| -------------------- | ---------- | ------------- | --- | --- |
|                      | Y = c +a   | x +a x +...+a | x   |     |
|                      |            | 1 1 2 2       | n n |     |
Simple linear regression:
Y = ax +b
| SreangRathanak |     | ChapterVI | December14,2024 | 2/6 |
| -------------- | --- | --------- | --------------- | --- |

Linear Regression
| SreangRathanak | ChapterVI | December14,2024 | 3/6 |
| -------------- | --------- | --------------- | --- |

Linear Regression
Given a set of x’s and y’s, the constants b and a can be determined with
| the following | calculations | (derived | in calculus): |     |     |
| ------------- | ------------ | -------- | ------------- | --- | --- |
The intercept (b) and slope (a) in simple linear regression can be
| calculated | as follows: |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
This is of little use being only one variable, but the process is easily
extendible to multiple x’s using matrix algebra methods. The equation is
still a line but in n-space, where n is the (number of independent
| variables)     | + 1. |     |           |                 |     |
| -------------- | ---- | --- | --------- | --------------- | --- |
| SreangRathanak |      |     | ChapterVI | December14,2024 | 4/6 |

Cost function
Root Mean Squared Error (RMSE) is a measure of the difference between
| the predicted | (pred) | and true | (y) values: |     |     |
| ------------- | ------ | -------- | ----------- | --- | --- |
(cid:118)
|     |     | (cid:117)  | n           |     |     |
| --- | --- | ---------- | ----------- | --- | --- |
|     |     | (cid:117)1 | (cid:88)    |     |     |
|     |     | J =        | (pred −y )2 |     | (1) |
|     |     | (cid:116)  | i i         |     |     |
n
i=1
| where | n is the number | of data | points. |     |     |
| ----- | --------------- | ------- | ------- | --- | --- |
Gradient Descent: To update a and b values in order to reduce Cost
| function | (minimizing | RMSE value). |     |     |     |
| -------- | ----------- | ------------ | --- | --- | --- |
To start with random a and b values and then iteratively updating the
| values,        | reaching minimum | cost. |           |                 |     |
| -------------- | ---------------- | ----- | --------- | --------------- | --- |
| SreangRathanak |                  |       | ChapterVI | December14,2024 | 5/6 |

| Thanks         | for your  | attention! |                 |     |
| -------------- | --------- | ---------- | --------------- | --- |
| SreangRathanak | ChapterVI |            | December14,2024 | 6/6 |
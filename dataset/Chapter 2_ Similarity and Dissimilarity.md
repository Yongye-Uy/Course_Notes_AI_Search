Chapter II
Data: Similarity and Dissimilarity
Sreang Rathanak
November 23, 2024
| SreangRathanak | ChapterII | November23,2024 | 1/22 |
| -------------- | --------- | --------------- | ---- |

Outline
| Similarity | and Dissimilarity | Measures |     |     |
| ---------- | ----------------- | -------- | --- | --- |
1
| 2 Similarity | Distance   | Measure         |     |     |
| ------------ | ---------- | --------------- | --- | --- |
| 3 Common     | Properties | of a Distance   |     |     |
| Common       | Properties | of a Similarity |     |     |
4
| SreangRathanak |     | ChapterII | November23,2024 | 2/22 |
| -------------- | --- | --------- | --------------- | ---- |

| 1.        | Similarity     | and      | Dissimilarity |          | Measures       |                  |                 |      |
| --------- | -------------- | -------- | ------------- | -------- | -------------- | ---------------- | --------------- | ---- |
|           | Similarity     | measure: |               |          |                |                  |                 |      |
|           | Numerical      |          | measure       | of how   | alike          | two data objects | are.            |      |
|           | Is higher      |          | when objects  | are      | more           | alike.           |                 |      |
|           | Often          | falls    | in the range  | [0,1].   |                |                  |                 |      |
|           | Dissimilarity  | measure: |               |          |                |                  |                 |      |
|           | Numerical      |          | measure       | of how   | different      | two data         | objects are.    |      |
|           | Lower          | when     | objects       | are more | alike.         |                  |                 |      |
|           | Minimum        |          | dissimilarity | is often | 0.             | Upper limit      | varies.         |      |
| Proximity | refers         | to       | a similarity  | or       | dissimilarity. |                  |                 |      |
|           | SreangRathanak |          |               |          | ChapterII      |                  | November23,2024 | 3/22 |

| 1.1. Similarity/Dissimilarity | for Simple | Attributes |     |
| ----------------------------- | ---------- | ---------- | --- |
The following table shows the similarity and dissimilarity between two
objects, x and y, with respect to a single, simple attribute.
| SreangRathanak | ChapterII | November23,2024 | 4/22 |
| -------------- | --------- | --------------- | ---- |

| 2. Similarity | Distance | Measure |     |     |     |
| ------------- | -------- | ------- | --- | --- | --- |
Five most popular similarity measures are the very basic building block for
activities such as Recommendation engines, clustering, Different
| classification | problems, | Email spam | classification | problems.       |      |
| -------------- | --------- | ---------- | -------------- | --------------- | ---- |
| SreangRathanak |           | ChapterII  |                | November23,2024 | 5/22 |

2.1. Euclidean Distance
| SreangRathanak | ChapterII | November23,2024 | 6/22 |
| -------------- | --------- | --------------- | ---- |

| 2.1. Euclidean | Distance |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
(cid:118)
|     |     | (cid:117) | n   |     |     |
| --- | --- | --------- | --- | --- | --- |
(cid:117)(cid:88)
|     | d(x,y) | = (cid:116) | (x −y )2 |     | (1) |
| --- | ------ | ----------- | -------- | --- | --- |
i i
i=1
where n is the number of dimensions (attributes) and x and y are,
|                 |               |           |                  | k               | k    |
| --------------- | ------------- | --------- | ---------------- | --------------- | ---- |
| respectively,   | the kth       |           |                  |                 |      |
| attributes      | (components)  | or data   | objects x and y. |                 |      |
| Standardization | is necessary, | if scales | differ.          |                 |      |
| SreangRathanak  |               | ChapterII |                  | November23,2024 | 7/22 |

| Example        | of Euclidean | Distance  |                 |      |
| -------------- | ------------ | --------- | --------------- | ---- |
| SreangRathanak |              | ChapterII | November23,2024 | 8/22 |

| 2.2. Manhattan | distance |     |     |     |
| -------------- | -------- | --- | --- | --- |
The distance between two points is calculated as the sum of the absolute
differences of their Cartesian coordinates. Or, the total sum of the
| difference between | the x-coordinates | and y-coordinates. |     |     |
| ------------------ | ----------------- | ------------------ | --- | --- |
Manhattan distance between two points P 1 (x 1 ,y 1 ) and P 2 (x 2 ,y 2 ) is
given by:
n
(cid:88)
|     | d(x,y) | = |x i −y i | |     | (2) |
| --- | ------ | ------------- | --- | --- |
i=1
Where n is the number of dimensions (attributes) and x k and y k are,
respectively, the kth attributes (components) or data object x and y.
| SreangRathanak |     | ChapterII | November23,2024 | 9/22 |
| -------------- | --- | --------- | --------------- | ---- |

| 2.3. Minkowski | Distance |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- |
Minkowski Distance is a generalization of Euclidean Distance and the
| Manhattan distance. |     |           |     |     |     |     |
| ------------------- | --- | --------- | --- | --- | --- | --- |
| (cid:32)            |     | (cid:33)1 |     |     |     |     |
|                     | n   | r         |     |     |     |     |
(cid:88)
| d(x,y) = | |x −y | |r  | (3) |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
k k
k=1
| r = 1. City      | block      | (Manhattan, | taxicab,      | L1 norm)        | distance. |     |
| ---------------- | ---------- | ----------- | ------------- | --------------- | --------- | --- |
| r = 2. Euclidean |            | distance    | (L2-Norm or   | Ruler distance) |           |     |
| r → ∞            | “supremum” | (Lmax       | norm, L norm) | distance        |           |     |
This is the maximum difference between any component of the vectors
| SreangRathanak |     |     | ChapterII |     | November23,2024 | 10/22 |
| -------------- | --- | --- | --------- | --- | --------------- | ----- |

| 2.3. Minkowski | Distance: | Example   |                 |       |
| -------------- | --------- | --------- | --------------- | ----- |
| SreangRathanak |           | ChapterII | November23,2024 | 11/22 |

2.4. Cosine Similarity
| SreangRathanak | ChapterII | November23,2024 | 12/22 |
| -------------- | --------- | --------------- | ----- |

| 2.4. Cosine | Similarity         |               |     |     |
| ----------- | ------------------ | ------------- | --- | --- |
| If d and    | d are two document | vectors, then |     |     |
| 1           | 2                  |               |     |     |
⟨d ,d ⟩
cos(d ,d ) = 1 2
1 2
|     |     | ∥d ∥∥d ∥ |     |     |
| --- | --- | -------- | --- | --- |
1 2
where ⟨d 1 ,d 2 ⟩ indicates the inner product or vector dot product of vectors
d and d , and ∥d∥ is the length of vector d. The outcome is neatly
| 1              | 2         |           |                 |       |
| -------------- | --------- | --------- | --------------- | ----- |
| bounded        | in [0,1]. |           |                 |       |
| SreangRathanak |           | ChapterII | November23,2024 | 13/22 |

| 2.4.     | Cosine   | Similarity        |     | Example |              |         |     |
| -------- | -------- | ----------------- | --- | ------- | ------------ | ------- | --- |
| Example: |          | Cosine Similarity |     | of      | Two Document | Vectors |     |
| Given    | document | vectors:          |     |         |              |         |     |
d 1 = [3,2,0,5,0,0,0,2,0,0]
d = [1,0,0,0,0,0,0,1,0,2]
2
Inner product
| ⟨d     | 1 ,d 2 ⟩ | = 3·1+2·0+0·0+5·0+0·0+0·0+0·0+2·1+0·0+0·2 |     |     |     |     | = 5 |
| ------ | -------- | ----------------------------------------- | --- | --- | --- | --- | --- |
| Length | of       | d :                                       |     |     |     |     |     |
1
√
(cid:112)
| ∥d  | ∥ = | 32+22+02+52+02+02+02+22+02+02 |     |     |     | = 42 ≈ | 6.481 |
| --- | --- | ----------------------------- | --- | --- | --- | ------ | ----- |
1
| Length | of  | d : |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
2
√
(cid:112)
| ∥d  | ∥ = | 12+02+02+02+02+02+02+12+02+22 |     |     |     | = 6 ≈ | 2.449 |
| --- | --- | ----------------------------- | --- | --- | --- | ----- | ----- |
2
Cosine Similarity:
|     |                |          |     | ⟨d 1 ,d | 2 ⟩ 5         |                 |       |
| --- | -------------- | -------- | --- | ------- | ------------- | --------------- | ----- |
|     |                | cos(d ,d | ) = |         | =             | ≈ 0.3150        |       |
|     |                | 1        | 2   | ∥d ∥∥d  | ∥ 6.481·2.449 |                 |       |
|     |                |          |     | 1       | 2             |                 |       |
|     | SreangRathanak |          |     |         | ChapterII     | November23,2024 | 14/22 |

| 2.5. Jaccard | similarity     |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
| Set &        | Set Operations |     |     |     |     |
Set: An (unordered) collection of objects {a,b,c}. We use the notation
with elements separated by commas inside curly brackets {}. Sets are
| unordered, | so {a,b} | = {b,a}. |     |     |     |
| ---------- | -------- | -------- | --- | --- | --- |
Cardinality: The cardinality of set A, denoted by |A|, counts how many
| elements | are in A. |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- |
Intersection: The intersection between two sets A and B is denoted
| A∩B and | reveals all | items that | are in both sets | A and B. |     |
| ------- | ----------- | ---------- | ---------------- | -------- | --- |
Union: The union between two sets A and B is denoted A∪B and reveals
| all items      | that are in | either set | A or B.   |                 |       |
| -------------- | ----------- | ---------- | --------- | --------------- | ----- |
| SreangRathanak |             |            | ChapterII | November23,2024 | 15/22 |

2.5. Jaccard similarity
| SreangRathanak | ChapterII | November23,2024 | 16/22 |
| -------------- | --------- | --------------- | ----- |

| 2.6. Similarity | Between |     | Binary Vectors |     |     |     |
| --------------- | ------- | --- | -------------- | --- | --- | --- |
Common Situation: Objects x and y have only binary attributes,
| typically with | values       | between       | 0 and 1.      |             |                 |       |
| -------------- | ------------ | ------------- | ------------- | ----------- | --------------- | ----- |
| Compute        | Similarities | using         | the following | quantities: |                 |       |
| f01:           | The number   | of attributes | where         | x was 0 and | y was 1.        |       |
| f10:           | The number   | of attributes | where         | x was 1 and | y was 0.        |       |
| f00:           | The number   | of attributes | where         | x was 0 and | y was 0.        |       |
| f11:           | The number   | of attributes | where         | x was 1 and | y was 1.        |       |
| SreangRathanak |              |               | ChapterII     |             | November23,2024 | 17/22 |

| 2.6. Similarity | Between | Binary | Vectors |     |     |     |
| --------------- | ------- | ------ | ------- | --- | --- | --- |
Simple Matching and Jaccard Coefficients (JC for asymmetric binary
attribute)
| SMC =          | number of   | matches    | / number  | of attributes | = (f +f         | )/(f  |
| -------------- | ----------- | ---------- | --------- | ------------- | --------------- | ----- |
|                |             |            |           |               | 11              | 00 01 |
| +f 10 +f       | 11 +f 00 )  |            |           |               |                 |       |
| JC =           | number of   | 11 matches | / number  | of non-zero   | attributes      | =     |
| (f 11 ) / (f   | 01 + f 10 + | f 11 )     |           |               |                 |       |
| SreangRathanak |             |            | ChapterII |               | November23,2024 | 18/22 |

| 2.6. | Similarity    | Between |     | Binary | Vectors: | Example |     |     |
| ---- | ------------- | ------- | --- | ------ | -------- | ------- | --- | --- |
|      | x= 1000000000 |         |     |        |          |         |     |     |
|      | y= 0000001001 |         |     |        |          |         |     |     |
f 01 = 2 (the number of attributes where x was 0 and y was 1)
|     | f = | 1 (the number | of  | attributes | where x | was 1 and | y was | 0)  |
| --- | --- | ------------- | --- | ---------- | ------- | --------- | ----- | --- |
10
|     | f = | 7 (the number | of  | attributes | where x | was 0 and | y was | 0)  |
| --- | --- | ------------- | --- | ---------- | ------- | --------- | ----- | --- |
00
|     | f = | 0 (the number | of  | attributes | where x | was 1 and | y was | 1)  |
| --- | --- | ------------- | --- | ---------- | ------- | --------- | ----- | --- |
11
|     | SMC            | = (f +f     | )/(f | +f +f     | +f ) =        | (0+7)/(2+1+0+7) |                 | = 0.7 |
| --- | -------------- | ----------- | ---- | --------- | ------------- | --------------- | --------------- | ----- |
|     |                | 11 00       | 01   | 10 11     | 00            |                 |                 |       |
|     | JC             | = (f ) / (f | +    | f + f )   | = (0)/(2+1+0) |                 | = 0             |       |
|     |                | 11          | 01   | 10 11     |               |                 |                 |       |
|     | SreangRathanak |             |      | ChapterII |               |                 | November23,2024 | 19/22 |

| 3. Common | Properties | of a Distance |     |     |     |
| --------- | ---------- | ------------- | --- | --- | --- |
Distances, such as the Euclidean distance, have some well-known
properties.
1) Positivity:d(x,y)¿=0 for all x and y and d(x,y)=0 if and only if x=y.
| 2) Symmetry: | d(x, y) = | d(y, x) for all | x and y. |     |     |
| ------------ | --------- | --------------- | -------- | --- | --- |
3) Triangle Inequality: d(x, z) ¡= d(x, y) + d(y, z) for all points x, y, and
z.
where d(x, y) is the distance (dissimilarity) between points (data objects),
x and y.
Measures that satisfy all three properties are known as metrics.
| A distance     | that satisfies | these properties | is a metric. |                 |       |
| -------------- | -------------- | ---------------- | ------------ | --------------- | ----- |
| SreangRathanak |                | ChapterII        |              | November23,2024 | 20/22 |

| 4. Common     | Properties | of a            | Similarity  |     |     |
| ------------- | ---------- | --------------- | ----------- | --- | --- |
| Similarities, | also have  | some well-known | properties. |     |     |
1) s(x, y) = 1 (or maximum similarity) only if x = y. (does not always
| hold, e.g., | cosine)       |                         |     |     |     |
| ----------- | ------------- | ----------------------- | --- | --- | --- |
| 2) s(x, y)  | = s(y, x) for | all x and y. (Symmetry) |     |     |     |
where s(x, y) is the similarity between points (data objects), x and y.
| SreangRathanak |     | ChapterII |     | November23,2024 | 21/22 |
| -------------- | --- | --------- | --- | --------------- | ----- |

| Thanks         | for your  | attention! |                 |       |
| -------------- | --------- | ---------- | --------------- | ----- |
| SreangRathanak | ChapterII |            | November23,2024 | 22/22 |
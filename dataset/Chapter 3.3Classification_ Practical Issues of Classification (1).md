|                 | Chapter          | III               |     |     |
| --------------- | ---------------- | ----------------- | --- | --- |
| Classification: | Practical Issues | of Classification |     |     |
Sreang Rathanak
|                | December 30, | 2024 |                 |      |
| -------------- | ------------ | ---- | --------------- | ---- |
| SreangRathanak | ChapterIII   |      | December30,2024 | 1/18 |

Outline
1 Missing Values
2 Confusion Matrix
3 Accuracy
4 Alternative Measures
SreangRathanak ChapterIII December30,2024 2/18

| 1. Missing | Values |     |     |     |
| ---------- | ------ | --- | --- | --- |
Missing values affect decision tree construction in three different ways:
| Affects how | impurity measures | are computed |     |     |
| ----------- | ----------------- | ------------ | --- | --- |
Affects how to distribute instance with missing value to child nodes
| Affects how | a test instance | with missing | value is classified |     |
| ----------- | --------------- | ------------ | ------------------- | --- |
Other Issues:
Data Fragmentation
Search Strategy
Expressiveness
Tree Replication
| SreangRathanak |     | ChapterIII | December30,2024 | 3/18 |
| -------------- | --- | ---------- | --------------- | ---- |

| 2. Confusion | Matrix |     |     |     |
| ------------ | ------ | --- | --- | --- |
Confusion matrix: useful for quickly calculating precision and recall given
| the predicted | labels from | a model. |     |     |
| ------------- | ----------- | -------- | --- | --- |
A confusion matrix for binary classification shows the four different
outcomes:
true positive, false positive, true negative, and false negative.
The actual values form the rows, and the predicted values (labels)
| form | the columns. |     |     |     |
| ---- | ------------ | --- | --- | --- |
The intersection of the rows and columns show one of the four
outcomes.
| SreangRathanak |     | ChapterIII | December30,2024 | 4/18 |
| -------------- | --- | ---------- | --------------- | ---- |

2. Confusion Matrix
Let:
a : True Positive (TP)
b : False Negative (FN)
c : False Positive (FP)
d : True Negative (TN)
SreangRathanak ChapterIII December30,2024 5/18

3. Accuracy
| SreangRathanak | ChapterIII | December30,2024 | 6/18 |
| -------------- | ---------- | --------------- | ---- |

| 3. Problem with    | Accuracy     |            |                 |      |
| ------------------ | ------------ | ---------- | --------------- | ---- |
| Consider a 2-class | problem      |            |                 |      |
| Number of Class    | NO examples  | = 990      |                 |      |
| Number of Class    | YES examples | = 10       |                 |      |
| SreangRathanak     |              | ChapterIII | December30,2024 | 7/18 |

| 3. Problem with    | Accuracy     |       |     |     |
| ------------------ | ------------ | ----- | --- | --- |
| Consider a 2-class | problem      |       |     |     |
| Number of Class    | NO examples  | = 990 |     |     |
| Number of Class    | YES examples | = 10  |     |     |
If a model predicts everything to be class NO, accuracy is 990/1000
= 99 %
This is misleading because the model does not detect any class YES
example
Detecting the rare class is usually more interesting (e.g., frauds,
| intrusions, defects, | etc) |            |                 |      |
| -------------------- | ---- | ---------- | --------------- | ---- |
| SreangRathanak       |      | ChapterIII | December30,2024 | 8/18 |

Which Model is BETTER?
| SreangRathanak | ChapterIII | December30,2024 | 9/18 |
| -------------- | ---------- | --------------- | ---- |

Which Model is BETTER?
| SreangRathanak | ChapterIII | December30,2024 | 10/18 |
| -------------- | ---------- | --------------- | ----- |

Which Model is BETTER?
| SreangRathanak | ChapterIII | December30,2024 | 11/18 |
| -------------- | ---------- | --------------- | ----- |

| 4. Alternative | Measures |     |     |     |
| -------------- | -------- | --- | --- | --- |
Precision determines the fraction of records that actually turns out to
be positive in the group the classifier has declared as a positive class.
Recall measures the fraction of positive examples correctly predicted
by the classifier.
| F1 represents | a harmonic | mean between | recall and precision. |     |
| ------------- | ---------- | ------------ | --------------------- | --- |
The harmonic mean of two numbers x and y tends to be closer to the
| smaller | of the two | number. |     |     |
| ------- | ---------- | ------- | --- | --- |
A high vale of F1-measure ensures that both precision and recall are
| reasonably     | high. |            |                 |       |
| -------------- | ----- | ---------- | --------------- | ----- |
| SreangRathanak |       | ChapterIII | December30,2024 | 12/18 |

4. Alternative Measures
| SreangRathanak | ChapterIII | December30,2024 | 13/18 |
| -------------- | ---------- | --------------- | ----- |

| 4. Alternative | Measures |     |     |     |
| -------------- | -------- | --- | --- | --- |
Building a model that maximizes both precision and recall is the key
| challenge      | of classification | algorithms. |                 |       |
| -------------- | ----------------- | ----------- | --------------- | ----- |
| SreangRathanak |                   | ChapterIII  | December30,2024 | 14/18 |

4. Alternative Measures
| SreangRathanak | ChapterIII | December30,2024 | 15/18 |
| -------------- | ---------- | --------------- | ----- |

4. Alternative Measures
| SreangRathanak | ChapterIII | December30,2024 | 16/18 |
| -------------- | ---------- | --------------- | ----- |

4. Alternative Measures
| SreangRathanak | ChapterIII | December30,2024 | 17/18 |
| -------------- | ---------- | --------------- | ----- |

| Thanks         | for your   | attention! |                 |       |
| -------------- | ---------- | ---------- | --------------- | ----- |
| SreangRathanak | ChapterIII |            | December30,2024 | 18/18 |
Convolutional Neural Network
Sreang Rathanak

Neural Network
2

Neural Network
3

Neural Network
● For multiple cells (units), use matrix W to
connect inputs to outputs
● These cascade in layers
4

Neural Network
5

Convolutional Neural Network
Some patterns are much smaller than the whole image
Can represent a small region with fewer parameters
“beak” detector
6

Convolutional Neural Network
● CNNs are a type of neural network architecture specifically designed for
analyzing visual data, such as images and videos.
● They have become highly effective and widely used in various computer
vision tasks.
● CNNs have revolutionized the field of computer vision and have achieved
state-of-the-art performance in many applications.
7

Convolutional Neural Network
A CNN is a neural network with some convolutional layers (and some other
layers). A convolutional layer has a number of filters that does convolutional
operation.
Filter
8

Convolutional Neural Network
| These are the network parameters to be learned. |     |     |     | 1 -1 | -1  |     |
| ----------------------------------------------- | --- | --- | --- | ---- | --- | --- |
|                                                 |     |     |     | -1 1 | -1  |     |
|                                                 | 1 0 | 0 0 | 0 1 |      |     |     |
Filter 1
|     |     |     |     | -1 -1 | 1   |          |
| --- | --- | --- | --- | ----- | --- | -------- |
|     | 0 1 | 0 0 | 1 0 |       |     |          |
|     | 0 0 | 1 1 | 0 0 |       |     |          |
|     |     |     |     | -1 1  | -1  |          |
|     | 1 0 | 0 0 | 1 0 |       |     |          |
|     |     |     |     | -1 1  | -1  |          |
|     | 0 1 | 0 0 | 1 0 |       |     | Filter 2 |
|     |     |     |     | -1 1  | -1  |          |
|     | 0 0 | 1 0 | 1 0 |       |     |          |
Each filter detects a small pattern (3 x 3).
9
6 x 6 image

Convolutional Neural Network
1 -1 -1
These are the network parameters to be learned.
Filter 1
-1 1 -1
| 1 0 | 0 0 | 0 1 |
| --- | --- | --- |
stride=1
-1 -1 1
| 0 1 | 0 0 | 1 0 |
| --- | --- | --- |
Dot Product
| 0 0 | 1 1 | 0 0 |
| --- | --- | --- |
3 -1
| 1 0 | 0 0 | 1 0 |
| --- | --- | --- |
| 0 1 | 0 0 | 1 0 |
| 0 0 | 1 0 | 1 0 |
10
6 x 6 image

Convolutional Neural Network
1 -1 -1
These are the network parameters to be learned.
Filter 1
-1 1 -1
| 1 0 | 0 0 | 0 1 | stride=2 |
| --- | --- | --- | -------- |
-1 -1 1
Dot Product
| 0 1 | 0 0 | 1 0 |     |
| --- | --- | --- | --- |
3 -3
| 0 0 | 1 1 | 0 0 |     |
| --- | --- | --- | --- |
| 1 0 | 0 0 | 1 0 |     |
| 0 1 | 0 0 | 1 0 |     |
| 0 0 | 1 0 | 1 0 |     |
11
6 x 6 image

Convolutional Neural Network
stride=1
12
6 x 6 image

Convolutional Neural Network
13

Convolutional Neural Network
14

Convolutional Neural Network
15

Convolutional Neural Network
16

Convolutional Neural Network
17

Convolutional Neural Network
18

Convolutional Neural Network
19

Convolutional Neural Network
20

Convolutional Neural Network
21

Convolutional Neural Network
22

Convolutional Neural Network
23

Convolutional Neural Network
24

Convolutional Neural Network
25

Convolutional Neural Network
26

Convolutional Neural Network
27

Convolutional Neural Network
28

Convolutional Neural Network
29

Convolutional Neural Network
30

Convolutional Neural Network
31

Convolutional Neural Network
32

Applications of CNN
33

Applications of CNN
34

Summary
● CNNs are specialized neural network architectures for visual data analysis.
● They have achieved significant success in computer vision tasks.
● Key components of CNNs include convolutional layers, pooling layers,
activation functions, and fully connected layers.
● Convolutional layers apply learnable filters to capture local patterns and
features.
● Pooling layers downsample feature maps while retaining important features.
● Activation functions introduce non-linearity to learn complex relationships
between features.
● Fully connected layers connect neurons for predictions and classification.
35

Summary
● CNNs are trained using a loss function to measure the difference between
predicted outputs and ground truth labels.
● Optimization algorithms, like stochastic gradient descent (SGD), update
network parameters during training.
● Regularization techniques, such as dropout and weight decay, prevent
overfitting.
● CNNs automatically extract relevant features from visual data without manual
feature engineering.
● They are effective in image classification, object detection, and image
segmentation.
● CNNs have revolutionized computer vision tasks and continue to advance
accuracy and performance.
36

Thanks for your attention!
37
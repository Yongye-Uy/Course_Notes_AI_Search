Chapter V:

Artiﬁcial Neural Networks (ANNs)

Sreang Rathanak

Outline

1. Artificial Neural Networks
2. Basic Architecture of Perceptron
3. Perceptron Learning Rule
4. Nonlinearly Separable Data
5. Multi-layer Neural Network
6. Multi-Layer Network Architecture
7. Activation Functions
8. Gradient Descent

2

1. Artiﬁcial Neural Networks

Basic Idea: A complex non-linear function can be learned
as a composition of simple processing units.

ANN is a collection of simple processing units (nodes) that
are connected by directed links (edges)

-

-

Every node receives signals from incoming edges, performs
computations, and transmits signals to outgoing edges
Analogous to human brain where nodes are neurons and signals are
electrical impulses

- Weight of an edge determines the strength of connection between the

nodes
Simplest ANN: Perceptron (single neuron)

-

3

Perceptron

4

2. Basic Architecture of Perceptron

Learns linear decision boundaries

●
● Similar to logistic regression (activation function is sign instead of sigmoid)

Activation Function

5

Perceptron Example

Output Y is 1 if at least two of the three inputs are equal to 1

6

Perceptron Example

7

3. Perceptron Learning Rule

-
-

k: iteration number
λ: learning rate

8

3. Perceptron Learning Rule(Cont.)

Weight update formula:

Intuition:

- Update weight based on error: e = (y - ŷ)
-
-
-

If y = ŷ, e=0: no update needed
If y > ŷ, e=2: weight must be increased so  that  ŷ will increase
If y < ŷ, e=-2: weight must be decreased so that  ŷ will decrease

9

Example of Perceptron Learning

Weight updates over all epochs

10

3. Perceptron Learning Rule(Cont.)

Since y is a linear combination of input variables,

=> decision  boundary is linear

For nonlinearly separable problems, perceptron
learning algorithm will fail because no linear
hyperplane can separate the data perfectly

11

4. Nonlinearly Separable Data

XOR classification problem. No linear hyperplane can separate the two classes.

12

5. Multi-layer Neural Network

- More than one hidden layer of computing nodes
- Every node in a hidden layer operates on

activations from preceding layer and transmits
activations forward to nodes of next layer

- Also referred to as “feedforward neural networks”

13

5. Multi-layer Neural Network(Cont.)

- Multi-layer neural networks with at least one hidden layer can solve any

type of classification task involving nonlinear decision surfaces

14

1. Artiﬁcial Neural Networks

Basic Idea: A complex non-linear function can be learned
as a composition of simple processing units.

ANN is a collection of simple processing units (nodes) that
are connected by directed links (edges)

-

-

Every node receives signals from incoming edges, performs
computations, and transmits signals to outgoing edges
Analogous to human brain where nodes are neurons and signals are
electrical impulses

- Weight of an edge determines the strength of connection between the

nodes
Simplest ANN: Perceptron (single neuron)

-

15

Why Multiple Hidden Layers?

- Activations at hidden layers can be viewed as features extracted as

functions of inputs

- Every hidden layer represents a level of abstraction
- Complex features are compositions of simpler features

- Number of layers is known as depth of ANN

- Deeper networks express complex hierarchy of features

16

6. Multi-Layer Network Architecture

Activation Function

Linear Predictor

Activation value at node i at layer l

17

Activation Functions

18

Learning Multi-layer Neural Network

- Can we apply perceptron learning rule to each node, including hidden

nodes?

- Perceptron learning rule computes error term e = y - ŷ and updates

weights accordingly

- Problem: how to determine the true value of y for hidden nodes?

-

 Approximate error in hidden nodes by error in the output nodes

- Problem:

- Not clear how adjustment in the hidden nodes affect overall

error

- No guarantee of convergence to optimal solution

-

19

Gradient Descent

Loss Function to measure errors across all training points

Squared Loss:

Gradient descent: Update parameters in the direction of “maximum descent” in
the loss function across all points

λ: learning rate

Stochastic gradient descent (SGD): update the weight for every instance
(minibatch SGD: update over min-batches of instances)

20

Computing Gradients

Using chain rule of differentiation (on a single instance):

For sigmoid activation function:

How can we compute for every layer?

21

Backpropagation Algorithm

- At output layer L:

- At a hidden layer l (using chain rule):

- Gradients at layer l can be computed using gradients at layer l + 1
- Start from layer L and “backpropagate” gradients to all previous layers

- Use gradient descent to update weights at every epoch
- For next epoch, use updated weights to compute loss fn. and its gradient
-

Iterate until convergence (loss does not change)

22

Design Issues in ANN Learning

- Number of nodes in input layer

- One input node per binary/continuous attribute
-

k or log2 k nodes for each categorical attribute with k values

- Number of nodes in output layer
- One output for binary class problem
-

k or log2 k nodes for k-class problem

- Number of hidden layers and nodes per layer
-
- Learning rate, max. number of epochs, mini-batch size for mini-batch SGD,

Initial weights and biases

…

23

Characteristics of ANN

- Multilayer ANN are universal approximators but could suffer from overfitting

if the network is too large

- Gradient descent may converge to local minimum
- Model building can be very time-consuming, but testing can be very fast
- Can handle redundant and irrelevant attributes because weights are

automatically learnt for all attributes

- Sensitive to noise in training data
- Difficult to handle missing attributes

24

Thanks for your attention!

25


Computer Vision

Sreang Rathanak

Practice

Implement simple face recognition system to recognize given face with users’
face in database.

2

1. What is Computer Vision?

● Vision is about discovering from images what is present in the scene and where it is.
● In Computer Vision a camera (or several cameras) is linked to a computer. The computer
interprets images of a real scene to obtain information useful for tasks such as navigation,
manipulation and recognition.

What is NOT Computer Vision

● Image  processing:  image  enhancement,  image  restoration,  image  compression.  Take  an

image and process it to produce a new image which is, in some way, more desirable.

● Computational Photography: extending the capabilities of digital cameras through the use
of computation to enable the capture of enhanced or entirely novel images of the world.

3

2. Why Computer Vision?

● Replicate human vision to allow a machine to see

– Central to that problem of Artiﬁcial Intelligence

– Many industrial applications

● Gain insight into how we see

– Vision is explored extensively by neuroscientists to gain an understanding

of how the brain operate

4

3. Applications

● Object Recognition and Classiﬁcation
● Face Recognition
● Image and Video Analysis
● Augmented Reality (AR)
● Medical Imaging and Healthcare
● Robotics and Autonomous Systems
● Optical Character Recognition (OCR)
● Gesture Recognition
● Video Surveillance
● Agriculture and Food Industry

5

4. Computer Vision Techniques and Algorithms

● Image Filtering
● Feature Extraction
● Object Recognition
● Image Segmentation
● Tracking
● Deep Learning
● 3D Reconstruction
● Image Synthesis
● Video Analysis

6

4.1. Image Filtering

Filtering:

● Filtering in the context of image processing refers to the process of modifying

or enhancing an image by applying a ﬁlter operation to its pixels.

● A  ﬁlter  is  a  mathematical  operation  that  is  applied  to  the  pixel  values  of  an

image or a portion of an image to achieve a desired effect.

Why?

● To get useful information from images.

○

E.g., extract edges or contours (to understand shape)

● To enhance the image.

○
○

E.g., to blur to remove noise
to sharpen to “enhance image” a la CSI

7

4.1. Image Filtering

Image  ﬁltering  techniques  are  used  to  preprocess  images  and  enhance  speciﬁc
features.

● Gaussian blur: Smoothes an image by reducing high-frequency noise.
● Edge  detection:  Identiﬁes  and  highlights  the  edges  or  boundaries  between

different objects in an image.

● Noise  reduction  ﬁlters:  Remove  noise  from  images,  improving  clarity  and

quality.

8

4.1. Image Filtering

Neighborhood  ﬁltering  (convolution):  The  image  on  the  left  is  convolved  with  the  ﬁlter  in  the  middle  to
yield  the  image  on  the  right.  The  light  blue  pixels  indicate  the  source  neighborhood  for  the  light  green
destination pixel.

9

4.1. Image Filtering

Linear  ﬁltering  is  a  common  image  processing
technique  that  involves  applying  a  linear  ﬁlter  to
an
to  achieve  various  effects  or
image
enhancements.

Types of Linear Filters:

● Gaussian Filter
● Sobel Filter
● Laplacian Filter
● Box Filter
● Median Filter

10

4.1. Image Filtering

Noise reduction using mean ﬁltering

Replace pixel by mean of neighborhood

Mean ﬁltering, or average ﬁltering or box ﬁltering, is a popular image processing technique
used to reduce noise and blur in images.

It works by replacing each pixel value in an image with the average value of its neighboring
pixels.

11

4.2. Feature Extraction

Feature extraction algorithms detect and extract distinctive features from images.

Examples:

● SIFT  (Scale-Invariant  Feature  Transform):  Extracts  keypoint  features  that  are

invariant to scale, rotation, and lighting changes.

● SURF  (Speeded-Up  Robust  Features):  Detects  and  describes  local  features  in  an

image.

● ORB  (Oriented  FAST  and  Rotated  BRIEF):  Eﬃciently  detects  and  matches  features

using binary descriptors.

12

4.3. Object Recognition

General object recognition falls into two broad categories, namely instance recognition and
class recognition.

To  recognize  one  or  more  instances  of  some  known  objects,  the  recognition  system  ﬁrst
extracts  a  set  of  interest  points  in  each  database  image  and  stores  the  associated
descriptors (and original positions) in an indexing structure such as a search tree.

13

4.4. Image Segmentation

Image  segmentation  techniques  partition
images into meaningful regions or segments.

Segment Anything by Meta AI

● Demo

https://segment-anything.com/demo

● Paper

https://arxiv.org/abs/2304.02643

14

4.5. Tracking

15

4.5. Tracking/Motion Estimation

Tracking and motion estimation are techniques used in computer vision to analyze
the movement of objects in videos or image sequences.

Object Tracking:

● Object tracking involves following the trajectory and movement of a speciﬁc

object over time.

● It aims to locate and track the object of interest as it moves across frames or

in a video stream.

● Object tracking can be achieved through various algorithms, including

feature-based tracking, correlation-based tracking, and optical ﬂow-based
tracking.

16

4.5. Tracking/Motion Estimation

Motion Estimation:

● Motion  estimation  is  the  process  of  estimating  the  motion  vectors  or

displacement between consecutive frames.

● It  aims  to  understand  how  objects  or  pixels  move  within  a  video  or  image

sequence.

● Motion estimation can be classiﬁed into two main categories: global motion

estimation and local motion estimation.

17

4.5. Tracking/Motion Estimation

Global Motion Estimation:

● Global  motion  estimation  models  the  overall  motion  of  a  scene  or  camera,

typically caused by camera motion or large-scale object movement.
● It helps stabilize videos, correct distortions, or align multiple frames.
● Examples  of  global  motion  estimation
transformations and homography estimation.

techniques

include  aﬃne

18

4.5. Tracking/Motion Estimation

Local Motion Estimation:

● Local motion estimation focuses on estimating the motion of individual pixels

or small regions within frames.

● It  helps  identify  object  motion,  track  moving  objects,  and  analyze  pixel-level

motion patterns.

● Techniques  such  as  optical  ﬂow  estimation  and  block  matching  algorithms

are commonly used for local motion estimation.

19

4.5. Tracking/Motion Estimation

Applications of Tracking and Motion Estimation:

● Video surveillance: Tracking objects of interest, detecting abnormal behavior,

and monitoring activities in real-time.

● Augmented reality: Overlaying virtual objects onto the real world by accurately

tracking the camera or user's motion.

● Action recognition: Analyzing and recognizing human actions in videos, such

as gesture recognition or activity monitoring.

● Autonomous vehicles: Estimating the motion of surrounding objects,
predicting their trajectories, and assisting in collision avoidance.

● Robotics: Tracking objects for manipulation, navigation, or interaction in robot

vision systems.

20

4.6. Deep Learning

Deep learning, a subﬁeld of machine learning, has made signiﬁcant advancements
in solving complex computer vision tasks. Convolutional Neural Networks (CNNs)
are a key deep learning architecture that has revolutionized computer vision.

21

4.6. Deep Learning

CNN Architectures:

a. AlexNet:

● AlexNet is a pioneering CNN architecture that won the ImageNet Large-Scale

Visual Recognition Challenge in 2012.

● It consisted of multiple convolutional layers, max-pooling layers, and fully

connected layers.

● AlexNet demonstrated the power of deep learning for image classiﬁcation

tasks and paved the way for subsequent CNN architectures.

22

4.6. Deep Learning

b. VGGNet:

● VGGNet  is  a  deep  network  architecture  known  for  its  simplicity  and

effectiveness in image classiﬁcation.

● It  consists  of  several  convolutional  layers  with  small  ﬁlter  sizes  (3x3)  and

max-pooling layers.

● VGGNet  achieved  competitive  performance  on  various  benchmark  datasets

and provided insights into the importance of network depth.

23

4.6. Deep Learning

c. ResNet:

● ResNet  (Residual  Neural  Network)

introduced  residual  connections  to

address the vanishing gradient problem in deep networks.

● It  allowed  for  the  training  of  extremely  deep  networks  (e.g.,  hundreds  of

layers) by enabling the ﬂow of gradients during backpropagation.

● ResNet  achieved  state-of-the-art  performance  on  image  classiﬁcation  tasks

and inﬂuenced subsequent architectures.

24

4.6. Deep Learning

Applications of Deep Learning in Computer Vision:

● Image Classiﬁcation: Deep learning models can classify images into predeﬁned categories

with high accuracy.

● Object  Detection:  Deep  learning  models  can  detect  and  localize  objects  within  images  or

videos.

● Semantic Segmentation: Deep learning models can assign semantic labels to each pixel in

an image, enabling detailed scene understanding.

● Image Generation: Deep learning models can generate new images with desired attributes

or transfer the style of one image to another.

● Facial Recognition: Deep learning models can identify and verify individuals based on facial

features.

● Video  Analysis:  Deep  learning  models  can  analyze  and  understand  the  content  and

activities in videos.

25

4.6. Deep Learning

Beneﬁts and Challenges of Deep Learning in Computer Vision:

Beneﬁts:

● Higher accuracy: Deep learning models often outperform traditional computer

vision algorithms in various tasks.

● End-to-end  learning:  Deep  learning  enables  learning  directly  from  raw  data,

eliminating the need for handcrafted features.

● Robustness  to  variations:  Deep  learning  models  can  handle  variations  in

lighting, pose, scale, and occlusions.

26

4.6. Deep Learning

Challenges:

● Large amounts of data: Deep learning models require a signiﬁcant amount of

labeled training data to achieve good performance.

● Computational

resources:  Training  deep
computationally intensive and may require powerful hardware.

learning  models  can  be

● Interpretability: Deep learning models can be complex, making it challenging

to interpret their decision-making processes.

27

4.7. 3D Reconstruction

3D  reconstruction  is  the  process  of  capturing  and  modeling  the  three-dimensional
structure of objects or scenes from two-dimensional images or sensor data.

28

4.7. 3D Reconstruction

Techniques for 3D Reconstruction:

a. Stereo Vision:

● Stereo vision involves capturing images of a scene using two or more

cameras with overlapping ﬁelds of view.

● By analyzing the disparities between corresponding image points, depth

information can be estimated, enabling 3D reconstruction.

29

4.7. 3D Reconstruction

b. Structure from Motion (SfM):

● SfM techniques use a sequence of images taken from different viewpoints to

estimate the 3D structure and camera motion.

● By tracking features across images and applying geometric constraints, a

sparse or dense 3D point cloud can be generated.

c. Depth Sensors:

● Depth sensors, such as Time-of-Flight cameras or LiDAR (Light Detection and

Ranging), directly measure the distance to objects in the scene.

● These sensors provide depth information, which can be fused with images to

create detailed 3D representations.

30

4.7. 3D Reconstruction

d. Multi-View Stereo (MVS):

● MVS  algorithms  combine  information  from  multiple  calibrated  images  to

reconstruct a dense 3D point cloud.

● By estimating depth for each pixel across the views, a detailed 3D model can

be created.

31

4.8. Image Synthesis

Image synthesis wit GAN Paper:

https://arxiv.org/pdf/1803.04469.pdf

Demo: https://openai.com/dall-e-2

32

4.9. Video Analysis

Video analysis is a ﬁeld of computer vision that focuses on extracting meaningful
information from videos. It involves understanding and interpreting the content of
videos, enabling machines to analyze and make decisions based on visual motion.

33

5. Challenges in Computer Vision

● Limited  Data:  Training  deep  learning  models  for  computer  vision  tasks  often

requires a large amount of labeled data.

● Variability and Complexity: Real-world visual data exhibits a wide range of variations,
including  variations  in  lighting  conditions,  viewpoints,  occlusions,  and  object
appearances.

● Ambiguity  and  Uncertainty:  Visual  information  can  be  ambiguous,  and  different

interpretations are possible.

● Computational  Complexity:  Many  computer  vision  algorithms  require  signiﬁcant
computational  resources,  especially  when  processing  high-resolution  images  or
videos  in  real-time.  Developing  eﬃcient  algorithms  and  optimizing  computational
performance is an ongoing challenge.

● Generalization:  Computer  vision  algorithms  should  be  able  to  generalize  well  to

unseen data and new environments.

34

5. Challenges in Computer Vision

● Ethical Considerations: Computer vision technologies raise ethical concerns related

to privacy, security, bias, and fairness.

● Real-time Processing: Real-time processing of visual data is essential for
applications such as autonomous vehicles, surveillance, and robotics.

● Interpretability and Explainability: Deep learning models used in computer vision

often act as black boxes, making it diﬃcult to understand the reasoning behind their
predictions.

● Integration with Context and Prior Knowledge: Computer vision algorithms often
beneﬁt from incorporating contextual information and prior knowledge about the
domain.

● Adapting to New Environments: Computer vision algorithms may struggle to adapt
to new environments, especially when faced with signiﬁcant changes in the data
distribution.

35

Homework

- dataset:

https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-s
mall

- use pretrained neural networks such as VGG-16 or VGG-19 to obtain images’

embeddings.

- given a new image, return top 10 products which has very high similarity to

the image.

- VGG16 Example:

https://colab.research.google.com/drive/18vbIrw89raF92q62Nwio1Akn9AN9
mP45?usp=sharing

36

Summary

● Computer  vision  enables  machines  to  perceive  and  understand  visual

information similar to human vision.

● It encompasses the development of algorithms and techniques for image and

video analysis.

● Computer  vision  has  applications

including  robotics,
autonomous  vehicles,  surveillance  systems,  healthcare,  augmented  reality,
and more.

in  various  ﬁelds,

● Key  tasks  in  computer  vision  include  image  classiﬁcation,  object  detection,

segmentation, tracking, 3D reconstruction, and image synthesis.

● Convolutional  Neural  Networks  (CNNs)  have  revolutionized  computer  vision,

particularly in tasks like image classiﬁcation and object recognition.

37

Summary

● Computer  vision  techniques  involve  linear  ﬁltering,  motion  estimation,  feature

extraction, deep learning, and image synthesis.

● Linear  ﬁltering  operations  include  mean  ﬁltering,  Gaussian  ﬁltering,  and  edge

detection.

● Motion estimation involves tracking and analyzing the movement of objects in video

sequences.

● Deep learning, speciﬁcally CNNs, has been highly effective in image analysis tasks.
● Image synthesis involves generating new images based on existing data or patterns.
● Computer  vision  has  signiﬁcant  potential  for  advancing  technology  and  improving
various industries by enabling machines to interpret and interact with visual data.

38

Book

http://cv2.csie.ntu.edu.tw/CV2/2023/textbook.pdf

39

Thanks for your attention!

40


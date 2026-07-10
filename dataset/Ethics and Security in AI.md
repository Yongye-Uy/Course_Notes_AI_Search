Ethics and Security in AI

Sreang Rathanak

AI Ethics

AI ethics is a set of values, principles, and techniques that employ widely
accepted standards of right and wrong to guide moral conduct in the development
and use of AI technologies.

These values, principles, and techniques are intended both to motivate morally
acceptable practices and to prescribe the basic duties and obligations necessary
to produce ethical, fair, and safe AI applications.

2

Why AI ethics?

The ﬁeld of AI ethics has largely emerged as a response to the range of individual
and societal harms that the misuse, abuse, poor design, or negative unintended
consequences of AI systems may cause.

Potential Harms Caused by AI Systems:

● Bias and Discrimination
● Denial of Individual Autonomy, Recourse, and Rights
● Non-transparent, Unexplainable, or Unjustiﬁable Outcomes
● Invasions of Privacy
● Isolation and Disintegration of Social Connection
● Unreliable, Unsafe, or Poor-Quality Outcomes

3

Ethical Considerations in AI

1. Transparency and Explainability:

● AI systems should be transparent, enabling users to understand how decisions are made.
● Explainability is crucial to address concerns about bias, discrimination, and accountability.
● Lack of transparency can undermine trust and hinder the ability to detect and rectify ethical

issues.

2. Fairness and Bias:

● AI algorithms should be designed to ensure fairness and mitigate bias.
● Bias in training data or algorithmic decision-making can lead to discriminatory outcomes.
● Fairness considerations are essential to prevent unfair advantages or disadvantages for

certain groups.

4

Ethical Considerations in AI

3. Privacy and Data Protection:

● AI often relies on vast amounts of personal data.
● Privacy regulations and data protection measures should be implemented to safeguard

user information.

● Proper data anonymization and consent mechanisms should be in place to protect

individual privacy.

4. Safety and Security:

● AI systems should prioritize safety in both physical and cybersecurity domains.
● Robust security measures are necessary to prevent malicious use or attacks on AI systems.
● Ensuring the safety and integrity of AI systems is crucial, especially in critical applications

like autonomous vehicles or healthcare.

5

Ethical Considerations in AI

5. Accountability and Responsibility:

● Clear lines of accountability should be established for AI systems and their

developers.

● Assigning responsibility for AI outcomes is important, particularly in cases of harm

or errors.

● Ethical frameworks should include mechanisms for accountability and recourse.

6. Human-Centric Values:

● AI should align with human values, promoting human well-being and dignity.
● Ethical considerations should prioritize the beneﬁts to individuals and society.
● The potential impact of AI on employment, social equity, and human relationships

should be carefully examined.

6

Ethical Considerations in AI

7. Impact on Jobs and Workforce:

● AI adoption may lead to job displacement and transformation of work.
● Ethical considerations involve addressing the impact on workers, retraining

opportunities, and equitable distribution of beneﬁts.

8. Global Considerations:

● Ethical principles and standards should be considered across borders and

cultures.

● International collaboration and shared values can help address global ethical

challenges in AI development and deployment.

7

★ The Impact of AI on Job Replacement: Concerns and Opportunities

"What are your thoughts on the potential job replacement by AI? Do you see it as a
concern or an opportunity?

Please elaborate on your perspective and any factors that contribute to your
viewpoint."

8

Security for AI

9

Security for AI

Security for AI involves people and practices, to build AI systems by ensuring
conﬁdentiality, integrity and availability.

● AI safety

 “robustness and resiliency of AI systems, as well as the social, political, and
economic systems with which AI interacts”

● AI policy

 “deﬁning procedures that maximize the beneﬁts of AI while minimizing its
potential costs and risks”

10

Security for AI

● AI ethics

“philosophical discussions about the interaction between humans and machines,
and the moral status of AI ethical issues”

● AI governance

”legal framework for ensuring that AI technologies are well researched and
developed to help humanity in its adoption”

11

AI-Security Domains

12

Intended Learning Outcomes

● Deﬁne  standard  notions  of  AI  security  and  use  them  to  evaluate  the  AI

system’s conﬁdentiality, integrity and availability

● Explain standard AI security problems in real world applications
● Use testing and veriﬁcation techniques to reason about the AI system’s safety

and security

13

Motivating Example

● What does the autonomous vehicle see in the traﬃc sign?
● Fake traﬃc sign (Lenticular attack) exploits differences in viewing angle

14

Motivating Example

● Autonomous cars with different camera positions (height) may see different

images. Same for human drivers

● The wrong perception of what information is in the traﬃc sign can cause the

autonomous vehicle to take risky and hazardous decisions in traﬃc

15

Technical AI safety (Speciﬁcation)

Deﬁne the purpose of the system (Speciﬁcation)

● Ensures that an AI System’s behavior meets the operator’s intentions

Ideal speciﬁcation: the hypothetical description of the system

○
○ Design speciﬁcation: the actual speciﬁcation of the system
○

Revealed speciﬁcation: the description of the presented behavior

16

Technical AI safety (Robustness)

Design the system to withstand perturbations

● Ensures  that  an  AI  system  continues  operating  within  safe  limits  upon

perturbations

○ Avoiding risks
○
○

Self-stabilisation
Recovery

17

Technical AI safety (Assurance)

Monitor and control system activity

● Ensures that we can understand and control AI systems during operation

○ Monitoring: inspecting systems, analyse and predict behaviour
○
○

Enforcing: controlling and restricting behaviour
Interpretability and interruptibility

18

Why do attacks exist?

● More to do with limitations of algorithms;
● Less to do with bugs or user mistakes;

○ Algorithms imperfections create opportunities for attacks.
○

Shortcomings of the current state-of-the-art AI methods .

“According to skeptic researchers, like Gary Marcus, author of ‘Deep Learning: A Critical Appraisal’,
deep learning can be seen as greedy, brittle, opaque, and shallow”

19

Why do attacks exist?

Understanding the limitations

● Data dependency

○
They rely solely on data, but good and quality data
○
They (may) demand huge sets of training data
○ Often requires supervision (humans labeling data)

● Brittleness

It cannot contextualize new scenarios (scenarios that were not in training)

○
○ Often break if confronted with “transfer test” (new data)

● Not explainable

Parameters are interpreted in terms of weights within a mathematical geography

○
○ Outputs cannot be explained
○ We know how it works (mathematical formalization) but We don’t know how it works, how it

learns

20

Why do attacks exist?

Understanding the limitations

● Shallowness

○
○
○
○

They are programmed with no innate knowledge innate knowledge
Posses no common sense about the world or humans psychology
Limited knowledge about causal relationships in the world
Limited understanding that wholes are made of parts

21

Why do attacks exist?

Implications of the limitations

 “A self-driving car can drive millions of miles, but it will eventually encounter
something new for which it has no experience”

Pedro Domingos, author of The Master Algorithm

“Or consider robot control: A robot can learn to pick up a bottle, but if it has to pick
up a cup, it starts from scratch”

Pedro Domingos, author of The Master Algorithm

22

Why do attacks exist?

Machine learning algorithms

● Rely solely on data to learn how to

perform tasks

● Patterns learned by current algorithms

are brittle

● Natural or artiﬁcial variations on the

data can disrupt the AI system

23

Why do attacks exist?

Machine learning algorithms

● ML algorithms are black box by nature
● Limited understanding of the learning process
● Limited understanding of what is learned by the algorithms

We can explain the math, but we can’t fully explain why it works (or learns)

24

Summary of AI systems limitations

● ML works by learning patterns that work well but can easily be disrupted (are

brittle)

● High dependency on data offers channel to corrupt the algorithms
● Black box nature of algorithms make them diﬃcult to audit
● Data dependency
● Generalization
● Explainability

25

Attacker goals

Cause Damage

● Attacker wants to cause damage
● Example:

○ Autonomous vehicle ignores a stop signs
○ Outcome: car crashes and physical harm

Hide something

● Attacker wants to evade detection
● Example:

○ Content ﬁlter ignores malicious contents from being detected, e.g., spam, malware and fraud
○ Outcome: People and company are exposed to harmful content and frauds

26

Attacker goals

Degrade faith in the system

● Attacker wants to compromise the credibility in the system performance
● Example:

○ Automated security alarm wrongly classify regular events as security

threats

○ Outcome: System is eventually shutdown

27

Risks facing the machine learning pipeline

28

Training data

Privacy breaches

● Conﬁdential information exposed or recoverable through database

Social network ids, name, nickname, picture

○
○ Data provided by a person can only be used for the purpose it was provided for

Data poisoning: Dataset is altered and manipulated before or during training

29

Training data

Data bias

● unbalanced data

Label leakage

● Occurs when a variable that is not a feature is used to predict the target

Label misclassiﬁcation

● Labels are wrongly assigned to observations

30

Training data

Improper or incomplete training

● Ignoring validation steps and techniques
● Failing to detect over-ﬁtting
● Failing to detect bias
● Insuﬃcient data
● Poor data (lack of variance, no data cleanse)
● Wrong model choice

31

Deployment

System disruption

● AI system becomes inaccessible due to an attack
● AI system unable to recover from an attack
● AI system becomes unresponsive after a malicious input

IT downtime

● Insuﬃcient technical support
● AI system stay down for long periods
● Lack of frequent updates
● Time consuming updates

32

Model

Privacy breaches

● Model becomes exposed to the public
● Unlimited or unrestricted access
● Lack of proper authentication to access the system
● Poor privilege rules set

33

Model and the real world

Adversarial attacks

● Model is exposed to crafted malicious inputs

● Noise added to traﬃc signs
● Wearing physical objects to dismiss facial recognition
● systems
● Adding speciﬁc text to spams so it is wrongly classiﬁed as inoffensive

email

34

Model and the real world

Man creates fake traﬃc jams with 99 smartphones in Berlin

35

Model and the real world

Dataset shift

● Sample selection bias

○

non-uniform population sampling
● Non-Stationary Environments

○

temporal or spatial change between the training and test environments

 “Predicting daily temperature in Sweden with model trained with data collected in
Australia”

36

Results

● Model  stealing:    Company  B  can  reverse  engineer  or  get  a  copy  of  a  model

developed by Company A

● Model  error:  Medical  assistant  system  wrongly  classify  healthy  cell  as  a

cancerous cell for patients bearing a speciﬁc gene mutation

● Misinterpretation:  Model  may  output  its  conﬁdence  in  terms  of  probability
and  users  misinterpret  it  as  percentage  wrongly  believing  0.9  is  0.9  percent
instead of 90 percent

● Job Displacements: Replacing human labor with AI system

37

Types of attacks

● Poisoning attacks (data, algorithm, model)

○ Database poisoning

Label modiﬁcation

■
■ Data injection
■ Data modiﬁcation

● Input attacks (adversarial example)

38

Types of attack

39

Poisoning Attacks

Algorithm and model poisoning

● Logic corruption

○
Is the most dangerous scenario
○
The attacker can change the algorithm and the way it learns
○
The attacker can encode any logic it wants
○ More details in Backdoor and Trojan slides

● Replace a legitimate model by a poisoned model

40

Poisoning Attacks

Backdoor (trojaning) attack

● Hidden patterns that have been trained into a DNN model that produce unexpected

behavior.

● Can be inserted into the model, either at:

○
○

training time,e.g., by a rogue employee at a company responsible for training the model;
or after the initial model training, e.g., by someone modifying and posting online an “improved” version
of a model

● The attack engine takes an existing model and a target prediction output as the

input.

● Then mutates the model and generates a small piece of input data, called the trojan

trigger.

● Inputs stamped with the trojan trigger will cause the mutated model to generate the

given classiﬁcation output.

41

Poisoning Attacks

Trojan attack overview

42

Poisoning Attacks

Backdoor attack: A benign model is augmented with a backdoor trigger resulting
in a poisoned model.

43

Input attacks

● Perceivable vs imperceptible by humans
● Physical vs Digital noise
● Physical vs Digital attacks
● Crafting adversarial inputs
● GANs

44

Crafting input attacks

Digital noises

● Synthetic data
● Patterns that does/may not exist in real world
● Noises that are digitally added to digital or physical objects.

“For digital content like images, these ‘imperceivable’ attacks can be executed by
sprinkling ‘digital dust’ on top of the target.”

45

Crafting input attacks

Digital noises

46

Crafting input attacks

Physical attacks

47

Crafting input attacks

Generative Adversarial Networks (GANs)

48

Crafting input attacks

What are (GANs)?

● Belong to the set of generative models
● They are able to produce/to generate synthetic data
● Grossly, GAN models learn the probability distribution of the input samples;

and

● And output new data within this same probability distribution

49

Evasion (Adversarial Examples)

Conﬁdence reduction

50

Evasion (Adversarial Examples)

Misclassiﬁcation

51

Evasion (Adversarial Examples)

Targeted misclassiﬁcation

52

Evasion (Adversarial Examples)

Source/Targeted misclassiﬁcation

53

Evasion (Adversarial Examples)

Universal misclassiﬁcation

54

Evasion (Adversarial Examples)

Attacker knowledge of the models

● White box: Full knowledge about the network, e.g., weights (parameters) and

train data
● Grey box
● Black box:

Limited knowledge about the network

○
○ Attacker can only send information to the system and observe its output

55

Evasion (Adversarial Examples)

White Box

56

Why do we need to ensure AI security?

AI  systems  must  be  as  robust  and  safe  as  possible,  given  that  even  any  faulty
behavior can lead to catastrophic outcomes, e.g., endangering human lives, public
and private property damage,

● In  2016,  Microsoft  released  an  AI  conversational  bot  that  would  learn  by
interacting with Twitter users. In less than 24 hour Tay was corrupted by the
users and became a racist, hateful, and sexist entity.

● In  2019,  a  Uber  car  hit  and  killed  woman  because  it  did  not  recognize  that

pedestrians jaywalk.

57

References

● Newman, J., Toward AI Security, 2019.

●

●

●

https://cltc.berkeley.edu/wp-content/uploads/2019/02/CLTC_Cussins_Toward_AI_Security.pdf
Finlayson, S.G., et al., “Adversarial Attacks Against Medical Deep Learning Systems” (2019)
https://arxiv.org/abs/1804.05296v3
Security & Privacy Risks of Machine Learning Models
https://sweis.medium.com/security-privacy-risks-of-machine-learning-models-cd0a44ac22b9
Chan-Hon-Tong, A., An Algorithm for Generating Invisible Data Poisoning Using Adversarial Noise That
Breaks Image Classiﬁcation Deep Learning, 2019

● Wang, B., et al.,“Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks” (2019)
●
●
●
●
●
●

Liu, K., et al.,“Trojan attacks on neural networks” (2017)
Gu, T., et al.,“BadNets: Evaluating Backdooring Attacks on Deep Neural Networks” (2019)
Godfellow I., et al., “Explaining and harnessing adversarial example” (2015)
Eykholt, K., et al., “Robust Physical-World Attacks on Deep Learning Visual Classiﬁcation” (2017)
Goodfellow, I., et al. “Generative adversarial nets.”
Tu, C., et al., “AutoZOOM : Autoencoder-based Zeroth Order Optimization Method for Attacking Black-box
Neural Networks” (2019)

58

Thanks for your attention!

59


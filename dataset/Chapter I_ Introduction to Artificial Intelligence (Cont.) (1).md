Chapter 1:
Introduction to Artificial Intelligence (Cont.)
Sreang Rathanak

Outline
1. Rational agents
2. Performance, environment, actuators, sensors
3. Agent programs
4. Reflex agents
5. Planning agents
6. Learning agents
7. Summary
2

Rational agents
| ●   | Informally,  |     | a  rational  |     | agent  | is  | an  | agent  | that  |
| --- | ------------ | --- | ------------ | --- | ------ | --- | --- | ------ | ----- |
does the "right thing".
| ●   | A         | performance  |                  |     | measure  |         | evaluates  |         | a   |
| --- | --------- | ------------ | ---------------- | --- | -------- | ------- | ---------- | ------- | --- |
|     | sequence  |              | of  environment  |     |          | states  |            | caused  | by  |
the agent's behavior.
| ●   | A          | rational  | agent   | is  | an  agent  |            | that  | chooses  |      |
| --- | ---------- | --------- | ------- | --- | ---------- | ---------- | ----- | -------- | ---- |
|     | whichever  |           | action  |     | that       | maximizes  |       |          | the  |
expected value of the performance measure,
given the percept sequence to date.
3

Rational agents
● Rationality ≠ omniscience
○ percepts may not supply all relevant information.
● Rationality ≠ clairvoyance
○ action outcomes may not be as expected.
● Hence, rational ≠ successful.
● However, rationality leads to exploration, learning and autonomy.
4

Performance, environment, actuators, sensors
The characteristics of the performance measure, environment, action space and
percepts dictate techniques for selecting rational actions. These characteristics
are summarized as the task environment.
Example 1: a self-driving car
● performance measure: safety, destination, legality, comfort, ...
● environment: streets, highways, traffic, pedestrians, weather, ...
● actuators: steering, accelerator, brake, horn, speaker, display, ...
● sensors: video, accelerometers, gauges, engine sensors, GPS, …
5

Performance, environment, actuators, sensors
Example 2: an Internet shopping agent
● performance measure: price, quality, appropriateness, efficiency
● environment: current and future WWW sites, vendors, shippers
● actuators: display to user, follow URL, fill in form, ...
● sensors: web pages (text, graphics, scripts)
6

Performance, environment, actuators, sensors
Fully observable vs. partially observable
Whether the agent sensors give access to the complete state of the environment, at each point
in time.
Deterministic vs. stochastic
Whether the next state of the environment is completely determined by the current state and the
action executed by the agent.
Episodic vs. sequential
Whether the agent's experience is divided into atomic independent episodes. time.
7

Performance, environment, actuators, sensors
Static vs. dynamic
Whether the environment can change, or the performance measure can change with time.
Discrete vs. continuous
Whether the state of the environment, the time, the percepts or the actions are continuous.
Single agent vs. multi-agent
Whether the environment include several agents that may interact which each other.
Known vs unknown
Reflects the agent's state of knowledge of the "law of physics" of the environment.
8

Performance, environment, actuators, sensors
Are the following task environments fully observable? deterministic? episodic? static? discrete?
single agents? Known?
● Crossword puzzle ● Taxi driving
● Chess, with a clock ● Medical diagnosis
● Poker ● Image analysis
● Backgammon ● Part-picking robot
● The real world ● Refinery controller
9

Agent programs
The job of AI is to design an agent program that implements the agent function.
Agent programs can be designed and implemented in many ways:
● with tables
● with rules
● with search algorithms
● with learning algorithms
10

Reflex agents
A reflex agent is a type of intelligent agent that selects actions based solely on
the current percept without considering the future consequences of those
actions. Reflex agents are typically used in simple environments where the current
percept provides enough information to make a decision.
Reflex agents:
● choose an action based on current percept (and maybe memory);
● may have memory or model of the world's current state;
● do not consider the future consequences of their actions.
11

Reflex agents
12

Reflex agents
● Simple reflex agents select actions on the basis of the current percept, ignoring
the rest of the percept history.
● They implement condition-action rules that match the current percept to an
action.
○ Rules provide a way to compress the function table.
○ Example (autonomous car): If a car in front of you slow down, you should break. The color
and model of the car, the music on the radio or the weather are all irrelevant.
● They can only work in a Markovian environment, that is if the correct decision
can be made on the basis of only the current percept. In other words, if the
environment is fully observable.
13

Reflex agents
Model-based reflex agents
14

Reflex agents
● Model-based agents handle partial observability of the environment by
keeping track of the part of the world they cannot see now.
● The internal state of model-based agents is updated on the basis of a
model which determines:
○ how the environment evolves independently of the agent;
○ how the agent actions affect the world.
15

Planning agents
| A  planning  |      | agent   |                | is  an       | intelligent  |     |          | agent    |        | that  |
| ------------ | ---- | ------- | -------------- | ------------ | ------------ | --- | -------- | -------- | ------ | ----- |
| can  reason  |      | about   |                | a  sequence  |              |     | of       | actions  |        | to    |
| achieve      | its  | goals.  |                | Unlike       | reflex       |     | agents,  |          | which  |       |
| respond      |      | to      | environmental  |              |              |     | stimuli  |          |        | with  |
pre-programmed actions, planning agents can
| construct  |        | a  plan  |     | of  actions  |     | that     |     | achieve  | their  |      |
| ---------- | ------ | -------- | --- | ------------ | --- | -------- | --- | -------- | ------ | ---- |
| goals      | based  |          | on  | their        |     | current  |     | state    |        | and  |
knowledge of the environment.
16

Planning agents
Planning agents:
● ask "what if?";
● make decisions based on (hypothesized) consequences of actions;
● must have a model of how the world evolves in response to actions;
● must formulate a goal.
17

Goal-based agents
Goal-based agents
18

Goal-based agents
● Decision process:
○ generate possible sequences of actions
○ predict the resulting states
○ assess goals in each.
● A goal-based agent chooses an action that will achieve the goal.
○ More general than rules. Goals are rarely explicit in condition-action rules.
○ Finding action sequences that achieve goals is difficult. Search and planning are two
strategies.
● Example (autonomous car): Has the car arrived to destination?
19

Utility-based agents
Utility-based agents
20

Utility-based agents
● Goals are often not enough to generate high-quality behavior.
○ Example (autonomous car): There are many ways to arrive to destination, but
some are quicker or more reliable.
○ Goals only provide binary assessment of performance.
● A utility function scores any given sequence of environment states.
○ The utility function is an internalization of the performance measure.
● A rational utility-based agent chooses an action that maximizes the
expected utility of its outcomes.
21

Learning agents
22

Learning agents
● Learning agents are capable of self-improvement. They can become more
competent than their initial knowledge alone might allow.
● They can make changes to any of the knowledge components by:
○ learning how the world evolves;
○ learning what are the consequences of actions;
○ learning the utility of actions through rewards.
23

Learning agents
A learning autonomous car
● Performance element:
○ The current system for selecting actions and driving.
● The critic observes the world and passes information to the learning element.
○ E.g., the car makes a quick left turn across three lanes of traffic. The critic observes shocking
language from the other drivers and informs bad action.
○ The learning element tries to modifies the performance element to avoid reproducing this
situation in the future.
● The problem generator identifies certain areas of behavior in need of improvement
and suggest experiments.
○ E.g., trying out the brakes on different surfaces in different weather conditions.
24

Summary
● An agent is an entity that perceives and acts in an environment.
● The performance measure evaluates the agent's behavior. Rational agents act so as
to maximize the expected value of the performance measure.
● Task environments includes performance measure, environment, actuators and
sensors. They can vary along several significant dimensions.
● The agent program effectively implements the agent function. Their designs are
dictated by the task environment.
● Simple reflex agents respond directly to percepts, whereas model-based reflex
agents maintain internal state to track the world. Goal-based agents act to achieve
goals while utility-based agents try to maximize their expected performance.
● All agents can improve their performance through learning.
25

Thanks for your attention!
26
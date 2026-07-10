Introduction to AI Agent
Sreang Rathanak

Introduction to Large Language
Models (LLMs)
2

What is a Large Language Model?
LLM (Large Language Model) - A type of AI model designed to understand and
generate human language.
● Trained on vast amounts of text data
● Learns language patterns, structure, and meaning
● Contains millions or billions of parameters
● Built using the Transformer architecture, which relies on the Attention
mechanism
● Popularized by models like BERT (Google, 2018) and GPT
3

Understanding next token prediction
After tokenizing input text, the model creates a contextual representation
capturing meaning and token positions. The model generates scores predicting
the likelihood of each possible next token.
Decoding strategies select the next token, often:
● Choosing the token with the highest score (greedy decoding)
● Or using more complex methods (e.g., sampling, beam search)
The process repeats until the model generates an End-Of-Sequence (EOS) token.
4

5

Attention Mechanism
A key aspect of the Transformer architecture is Attention. When predicting the
next word, not every word in a sentence is equally important; words like “France”
and “capital” in the sentence “The capital of France is …” carry the most meaning.
6

Messages and Special Tokens in LLMs
LLMs use structured messages to simulate conversation:
messages = [
{"role": "system", "content": "You are a helpful assistant focused on technical
topics."},
{"role": "user", "content": "Can you explain what a chat template is?"},
{"role": "assistant", "content": "A chat template structures conversations between
users and AI models..."},
{"role": "user", "content": "How do I use it ?"}, ]
7

Special Tokens in LLMs
Each LLM has its own special tokens to mark message boundaries:
8

Prompting the LLM
Prompting means providing the LLM with an initial text or question to guide its
response.
The quality and clarity of the prompt greatly affect the output’s relevance and accuracy.
Prompts can be:
● Explicit instructions (e.g., “Summarize this article.”)
● Examples that show the desired output style (few-shot prompting)
Effective prompting helps the model generate more accurate, coherent, and
context-aware results.
Prompt engineering is a growing skill to get the best from LLMs.
9

Prompting Technique
Zero-shot Prompting Few-shot Prompting
Prompt:
Prompt:
Positive This is awesome!
Classify the text into neutral, negative or
positive.
This is bad! Negative
Text: I think the vacation is okay.
Wow that movie was rad! Positive
Sentiment: What a horrible show! --
Output: Output:
Neutral Negative
10

Prompting Technique
Chain-of-Thought (CoT) Prompting is a
technique where a language model is
explicitly guided to reason step by step
before giving a final answer.
It can be combined with few-shot prompting
to get better results on more complex tasks
that require reasoning before responding.
11

Standard Vs CoT Prompting
12

Prompting Technique
Meta Prompting is an advanced prompting technique that focuses on the structural
and syntactic aspects of tasks and problems rather than their specific content details.
This goal with meta prompting is to construct a more abstract, structured way of
interacting with large language models (LLMs), emphasizing the form and pattern of
information over traditional content-centric methods.
Key Characteristics
● Structure-oriented ● Versatile
● Syntax-focused ● Categorical approach
● Abstract examples
13

Prompting Technique - Meta Prompt
Source: Meta Prompting for AI Systems, Yifan Zhang, Yang Yuan, Andrew Chi-Chih Yao
14

Prompting Technique - Generated Knowledge Prompting
Source: Generated Knowledge Prompting for Commonsense Reasoning, Liu et al.
15

AI Tools
An AI Tool is a function exposed to an LLM that fulfills a specific objective the
model can't do well on its own.
Why plain LLMs are not enough
● LLMs are static, they only "know" up to their training cutoff.
● no memory, no live data, no long-term planning
● hallucination
● cannot execute actions directly
Tools provide live data, external actions, or precision functions.
16

17

AI Agents with LLMs
18

What is an AI Agent?
Source: https://huggingface.co/learn/agents-course/unit1/introduction
19

What is an AI Agent?
An AI Agent is a model capable of:
● Reasoning
● Planning
● Interacting with its environment
An Agent is a system that leverages an AI model
External tools
to interact with its environment in order to achieve
a user-defined objective. It combines reasoning,
planning, and action execution (often via
external tools).
20

AI Agent Architecture
21

Memory in AI Agents
| Short-term          | Long-term      | Episodic | Semantic              |
| ------------------- | -------------- | -------- | --------------------- |
| ▸  Rolling context  | ▸  Databases,  |          | ▸  Stores structured  |
▸  Logs specific past
window within a
|     | knowledge graphs &  |     | facts & definitions |
| --- | ------------------- | --- | ------------------- |
events & outcomes
| session | vectors |     | ▸  Generalized  |
| ------- | ------- | --- | --------------- |
▸  Supports
| ▸  Ideal for  | ▸  Enables  |     |     |
| ------------- | ----------- | --- | --- |
knowledge, not
case-based
personalization over
| real-time  |     |     | events |
| ---------- | --- | --- | ------ |
reasoning
time
conversation flow
▸  Foundation for
▸  Key in robotics &
▸  Best implemented
▸  Does not persist
reasoning & logic
autonomous agents
with RAG techniques
across sessions
Source: https://www.ibm.com/think/topics/ai-agent-memory
22

Characteristics of an AI agent
1. Autonomy: Operates independently without constant human oversight.
2. Perception: Gathers and interprets data from the environment using sensors
like cameras or microphones.
3. Reactivity:Responds promptly to environmental changes.
4. Reasoning & Decision-Making: Analyzes data to make informed decisions
using algorithms.
23

Characteristics of an AI agent
5. Learning: Improves performance over time through machine learning
techniques.
6. Communication: Interacts with humans or other agents via natural language or
structured messages.
7. Goal-Oriented Behavior: Designed to achieve specific objectives, either
predefined or learned.
24

Understanding the structure of an AI agent
25

Understanding the structure of an AI agent
1. Environment: The domain where the agent operates that can be physical (e.g., factory)
or digital (e.g., website).
2. Sensors: Devices that collect data from the environment (e.g., cameras, microphones).
3. Actuators: Tools the agent uses to act on the environment (e.g., robotic arms, screen
outputs).
4. Decision-Making Mechanism: The agent’s “brain” that processes input and determines
actions using logic or AI models.
5. Learning System: Enables improvement over time through learning techniques like
supervised, unsupervised, or reinforcement learning
26

How does an AI agent work?
27

The agentic loop - Claude Code
28

How does an AI agent work?
Step 1: Perceiving the Environment
The agent gathers data using sensors or external sources to understand its surroundings.
Step 2: Processing Input Data
Organizes and interprets collected data to create usable internal representations or a knowledge base.
Step 3: Decision-Making
Uses logic, rules, or machine learning to make informed decisions aligned with its goals.
Step 4: Planning & Executing Actions
Develops and executes a plan to achieve goals, considering constraints and feedback from the
environment.
Step 5: Learning & Improvement
Analyzes outcomes and updates its knowledge or strategies to perform better in the future.
29

Key Features of LLM AI Agents
LLM AI Agents are intelligent systems powered by Large Language Models
(such as Claude, OpenAI’s GPT, Google’s PaLM, or Meta’s LLaMA). These agents
are capable of:
● Understanding and processing natural language instructions
● Interacting dynamically with users and their environment
● Performing multi-step reasoning and decision-making
● Utilizing external tools, APIs, and memory
● Executing complex tasks such as data analysis, content generation, or task
automation
30

Key Features of LLM AI Agents
1. Contextual Understanding 3. Autonomous Task Execution
● Maintains context across multiple turns in ● Plans and executes tasks based on goals
a conversation ● Operates with minimal human guidance
● Suitable for handling long, complex, or
4. Multi-Agent Collaboration
evolving tasks
● Supports communication and coordination
2. Tool Integration
between multiple agents
● Can interact with external tools such as: ● Enables distributed problem-solving and
○ APIs & Web services parallel task handling
○ Databases
● Enhances capabilities beyond text
generation
31

Agent Thoughts
Thoughts represent the internal reasoning and planning of an AI Agent.
● This is where the LLM analyzes the current situation based on its prompt.
● It mimics an internal dialogue or stream of consciousness.
● Think: “How should I approach this problem?”
32

Thought: Internal Reasoning and the ReAct Approach
Type of Thought Example
Planning “I need to break this task into three steps: 1)
gather data, 2) analyze trends, 3) generate
report”
Analysis “Based on the error message, the issue appears
to be with the database connection parameters”
Decision Making “Given the user’s budget constraints, I should
recommend the mid-tier option”
Problem Solving “To optimize this code, I should first profile it to
identify bottlenecks”
33

Thought: Internal Reasoning and the ReAct Approach
Type of Thought Example
Memory Integration “The user mentioned their preference for Python
earlier, so I’ll provide examples in Python”
Self-Reflection “My last approach didn’t work well, I should try a
different strategy”
Goal Setting “To complete this task, I need to first establish
the acceptance criteria”
Prioritization “The security vulnerability should be addressed
before adding new features”
34

The ReAct Approach: Reasoning + Acting
The ReAct framework is a prompting method that integrates "reasoning"
(thinking) and "acting" (tool use or environment interaction) in an iterative
loop.
It enables LLM agents to make decisions by:
● Thinking aloud step-by-step
● Calling tools or performing actions
● Reflecting on observations
● Then generating a final answer
35

Actions: Enabling the Agent to Engage with Its Environment
Actions are the concrete steps that agents take to interact with the outside
world—whether it's fetching data, executing code, or calling APIs.
“Think = Plan | Act = Do”
● Turn LLM "thoughts" into real-world outcomes
● Interact with digital or physical environments
● Allow tools to compensate for LLM limitations (e.g., outdated knowledge, math)
Example Use Cases: Web search for live news, Generate an image, Control a device,
Query a company database
36

Types of Agent Actions
Action Type Description
Information Gathering Fetching data from web, DB, or knowledge base
Tool Usage Calling APIs, executing tools (e.g., calculator)
Environment Interaction UI manipulation or device control
Communication Sending messages to users or other agents
37

Agentic Workflows
38

What Are Agentic Workflows?
Agentic workflows are AI-driven, autonomous systems where agents make
decisions, take actions, and coordinate tasks with minimal human input.
Key Traits:
● Reasoning & planning with LLMs
● Tool usage (APIs, web search, scripts)
● Iterative, adaptive processes
● Minimal reliance on static rules
39

Components of agentic workflows
Component Description
AI Agents Autonomous systems that plan and act using reasoning + tool use
LLMs Enable language understanding and decision-making
Tools APIs, scripts, search engines for real-time or domain-specific tasks
Feedback HITL or peer agents to improve decisions
Mechanisms
Prompt Refines reasoning via CoT, self-reflection, zero/one-shot prompts
Engineering
Multiagent Systems Distribute roles/expertise across cooperating agents
Integrations Connect with tools (LangChain, BeeAI), systems (CRM, DB), or orchestration
layers
40

Prompt Engineering in Agentic Workflows
Prompt engineering guides how AI agents interpret tasks and generate
responses. It's essential for enabling agents to reason, plan, and adapt
effectively.
1. Planning
● Agents break down complex tasks into sequential, manageable steps.
● Helps determine optimal task execution order.
● Enables dynamic adjustment in response to unexpected conditions.
Example: Instead of answering immediately, the agent outlines:
1. Understand the user request
2. Retrieve needed data
3. Summarize results
4. Present the response
41

Prompt Engineering in Agentic Workflows
2. Self-Reflection
● Agents assess their own outputs.
● Identifies errors, inconsistencies, or missed information.
● Enables iterative improvement through internal critique.
Example:
“I may have missed a step. Let me reevaluate the logic and verify the output
again.”
42

Workflow: Prompt chaining
Prompt chaining decomposes a task into a sequence of steps, where each
LLM call processes the output of the previous one.
This method supports complex reasoning, modularity, and increased
control over the agent’s behavior.
43

Thanks for your attention!
44
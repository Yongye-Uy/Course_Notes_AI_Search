Chapter II:
Rule-based expert system
Sreang Rathanak

Exercise
# Write a simple python diagnose function base on defined rules below:
rules = {
"fever": { "cough": "respiratory infection", "sore throat": { “tmp above 37”: “COVID”, “tmp between 35-36”: "strep throat" }},
"rash": { "poison ivy": "poison ivy rash" },
"joint pain": { "multiple joints": "rheumatoid arthritis", "single joint": "sprain or strain" },
"abdominal pain": { "upper abdomen": "gastritis or ulcer", "lower abdomen": "appendicitis or irritable bowel syndrome"},
“fever”: {"cough": "COVID"}
}
Ex: Do you have fever? (y/n): y
Do you also have cough? (y/n): y
You may have respiratory infection
2

Outline
1. What is knowledge?
2. Rules as a Knowledge Representation Technique
3. Structure of a rule-based expert system
4. Characteristics of an expert system
5. Can expert systems make mistakes?
6. Forward chaining and backward chaining
7. Conflict resolution
8. Advantages of rule-based expert systems
9. Disadvantages of rule-based expert systems
3

1. What is knowledge?
● Knowledge is a theoretical or practical understanding of a subject or a
domain. Knowledge is also the sum of what is currently known, and
apparently knowledge is power. Those who possess knowledge are called
experts.
● Anyone can be considered a domain expert if he or she has deep
knowledge (of both facts and rules) and strong practical experience in a
particular domain. The area of the domain may be limited. In general, an
expert is a skillful person who can do things other people cannot.
4

1. What is knowledge?
● The human mental process is internal, and it is too complex to be represented
as an algorithm.
● However, most experts are capable of expressing their knowledge in the form
of rules for problem solving.
IF the ‘traffic light’ is ‘green’
THEN the action is go
IF the ‘traffic light’ is ‘red’
THEN the action is stop
5

2. Rules as a Knowledge Representation Technique
● The term rule in AI, which is the most commonly used type of knowledge
representation, can be defined as an IF-THEN structure that relates given
information or facts in the IF part to some action in the THEN part.
● A rule provides some description of how to solve a problem.
● Rule are relatively easy to create and understand
● Any rules consists of two parts: the IF part, called the antecedent (premise or
condition) and the THEN part called the consequent (conclusion or action)
6

2. Rules as a Knowledge Representation Technique
● Any rules consists of two parts: the IF part, called the antecedent (premise or
condition) and the THEN part called the consequent (conclusion or action)
IF <Antecedent>
THEN <Consequent>
7

2. Rules as a Knowledge Representation Technique
A rule can have multiple antecedents joined by the keywords AND (conjunction),
OR (disjunction) or a combination of both.
| IF    | <Antecedent  1> | IF    | <Antecedent 1>    |
| ----- | --------------- | ----- | ----------------- |
| AND   | <Antecedent 2>  | OR    | <Antecedent 2>    |
| AND   | <Antecedent  n> | OR    | <Antecedent n>    |
| THEN  | <Consequent>    | THEN  | <Consequent>      |
8

2. Rules as a Knowledge Representation Technique
● The antecedent of a rule incorporates two parts: an object (linguistic
object) and its value. The object and its value are linked by an operator.
● The operator identifies the object and assigns the value.
● Operators such as is, are, is not, are not are used to assign a symbolic
value to a linguistic object.
9

2. Rules as a Knowledge Representation Technique
● Expert systems can also used mathematical operators to define an object
as numerical and assign it to the numerical value.
IF ‘age of the customer’ < 18 AND ‘cash withdrawal’ > 1000
THEN ‘signature of the parent’ is required
10

2. Rules as a Knowledge Representation Technique
Rules can represent:
● Relation: IF the ‘fuel tank’ is empty THEN the car is dead
● Recommendation: IF the season is autumn AND the sky is cloudy AND
the forecast is drizzle THEN the advice is ‘take an umbrella’
● Directive: IF the car is dead AND the ‘fuel tank’ is empty THEN the action
is ‘refuel the car
11

2. Rules as a Knowledge Representation Technique
● Strategy:
IF the car is dead
THEN the action is ‘check the fuel tank’; step1 complete
IF step1 is complete AND the ‘fuel tank’ is full
THEN the action is ‘check the battery’; step2 is complete
12

2. Rules as a Knowledge Representation Technique
● Heuristic:
IF the spill is liquid AND the ‘spill pH’ < 6 AND the ‘spill smell’ is
vinegar
THEN the ‘spill material’ is ‘acetic acid’
13

2. Rules as a Knowledge Representation Technique
There are five members of the expert system development team:
1. domain expert
2. knowledge engineer
3. programmer
4. project manager
5. end-user
14

2. Rules as a Knowledge Representation Technique
15

2. Rules as a Knowledge Representation Technique
The domain expert is a knowledgeable and skilled person capable of solving
problems in a specific area or domain. This person has the greatest expertise in a
given domain. This expertise is to be captured in the expert system. Therefore, the
expert must be able to communicate his or her knowledge, be willing to participate
in the expert system development and commit a substantial amount of time to the
project. The domain expert is the most important player in the expert system
development team.
16

2. Rules as a Knowledge Representation Technique
The knowledge engineer is someone who is capable of designing, building and
testing an expert system. He or she interviews the domain expert to find out how a
particular problem is solved. The knowledge engineer establishes what reasoning
methods the expert uses to handle facts and rules and decides how to represent
them in the expert system. The knowledge engineer then chooses some
development software or an expert system shell, or looks at programming
languages for encoding the knowledge. And finally, the knowledge engineer is
responsible for testing, revising and integrating the expert system into the
workplace.
17

2. Rules as a Knowledge Representation Technique
The programmer is the person responsible for the actual programming, describing
the domain knowledge in terms that a computer can understand. The programmer
needs to have skills in symbolic programming in such AI languages as LISP, Prolog
and OPS5 and also some experience in the application of different types of expert
system shells.
18

2. Rules as a Knowledge Representation Technique
The project manager is the leader of the expert system development team,
responsible for keeping the project on track. He or she makes sure that all
deliverables and milestones are met, interacts with the expert, knowledge
engineer, programmer and end-user. The end-user, often called just the user, is
a person who uses the expert system when it is developed.
19

2. Rules as a Knowledge Representation Technique
The user must not only be confident in the expert system performance, but
also feel comfortable using it. Therefore, the design of the user interface of
the expert system is also vital for the project’s success; the end-user’s
contribution here can be crucial.
20

3. Structure of a rule-based expert system
● In the early seventies, Newell and Simon from Carnegie-Mellon University
proposed a production system model, the foundation of the modern
rule-based expert systems.
● The production model is based on the idea that humans solve problems by
applying their knowledge (expressed as production rules) to a given problem,
represented by problem-specific information.
● The production rules are stored in the long-term memory and the
problem-specific information or facts in the short-term memory.
21

3. Structure of a rule-based expert system
Production system model
22

3. Structure of a rule-based expert system
Basic structure of a rule-based expert system
23

3. Structure of a rule-based expert system
● The knowledge base contains the domain knowledge useful for problem
solving. In a rule-based expert system, the knowledge is represented as a set
of rules. Each rule specifies a relation, recommendation, directive, strategy or
heuristic and has the IF (condition) THEN (action) structure. When the
condition part of a rule is satisfied, the rule is said to fire and the action part is
executed.
● The database includes a set of facts used to match against the IF (condition)
parts of rules stored in the knowledge base.
24

3. Structure of a rule-based expert system
● The inference engine carries out the reasoning whereby the expert system
reaches a solution. It links the rules given in the knowledge base with the
facts provided in the database.
● The explanation facilities enable the user to ask the expert system how a
particular conclusion is reached and why a specific fact is needed. An expert
system must be able to explain its reasoning and justify its advice, analysis or
conclusion.
● The user interface is the means of communication between a user seeking a
solution to the problem and an expert system.
25

3. Structure of a rule-based expert system
Complete structure of a rule-based expert system
26

5. Characteristics of an expert system
● An expert system is built to perform at a human expert level in a narrow,
specialized domain. Thus, the most important characteristic of an expert
system is its high-quality performance. No matter how fast the system can
solve a problem, the user will not be satisfied if the result is wrong.
● On the other hand, the speed of reaching a solution is very important. Even
the most accurate decision or diagnosis may not be useful if it is too late to
apply, for instance, in an emergency, when a patient dies or a nuclear power
plant explodes.
27

4. Characteristics of an expert system
● Expert systems apply heuristics to guide the reasoning and thus reduce the
search area for a solution.
● A unique feature of an expert system is its explanation capability. It enables
the expert system to review its own reasoning and explain its decisions.
● Expert systems employ symbolic reasoning when solving a problem. Symbols
are used to represent different types of knowledge such as facts, concepts
and rules.
28

5. Can expert systems make mistakes?
● Even a brilliant expert is only a human and thus can make mistakes. This
suggests that an expert system built to perform at a human expert level
also should be allowed to make mistakes. But we still trust experts, even
we recognize that their judgements are sometimes wrong. Likewise, at
least in most cases, we can rely on solutions provided by expert systems,
but mistakes are possible, and we should be aware of this.
29

5. Can expert systems make mistakes?
● In expert systems, knowledge is separated from its processing (the
knowledge base and the inference engine are split up). A conventional
program is a mixture of knowledge and the control structure to process
this knowledge. This mixing leads to difficulties in understanding and
reviewing the program code, as any change to the code affects both the
knowledge and its processing.
● When an expert system shell is used, a knowledge engineer or an expert
simply enters rules in the knowledge base. Each new rule adds some new
knowledge and makes the expert system smarter.
30

Comparison of expert systems with conventional systems and human
experts
31

Comparison of expert systems with conventional systems and human
experts (Cont.)
32

5. Forward chaining and backward chaining
● In a rule-based expert system, the domain knowledge is represented by a set
of IF-THEN production rules and data is represented by a set of facts about
the current situation. The inference engine compares each rule stored in the
knowledge base with facts contained in the database. When the IF (condition)
part of the rule matches a fact, the rule is fired and its THEN (action) part is
executed.
● The matching of the rule IF parts to the facts produces inference chains. The
inference chain indicates how an expert system applies the rules to reach a
conclusion.
33

6. Forward chaining and backward chaining
Inference engine cycles via a
match-fire procedure
34

6. Forward chaining and backward chaining
An example of an inference chain
35

Forward chaining
Forward chaining is the data-driven reasoning. The reasoning starts from
the known data and proceeds forward with that data. Each time, only the
topmost rule is executed. When fired, the rule adds a new fact in the
database. Any rule can be executed only once. The match-fire cycle stops
when no further rules can be fired.
36

Forward chaining
37

Forward chaining
● Forward chaining is a technique for gathering information and then
inferring from it whatever can be inferred.
● However, in forward chaining, many rules may be executed that have
nothing to do with the established goal.
● Therefore, if our goal is to infer only one particular fact, the forward
chaining inference technique would not be efficient.
38

Backward chaining
Backward chaining is the goal-driven reasoning. In backward chaining, an
expert system has the goal (a hypothetical solution) and the inference
engine attempts to find the evidence to prove it. First, the knowledge base
is searched to find rules that might have the desired solution. Such rules
must have the goal in their THEN (action) parts. If such a rule is found and
its IF (condition) part matches data in the database, then the rule is fired
and the goal is proved. However, this is rarely the case.
39

Backward chaining
Thus, the inference engine puts aside the rule it is working with (the rule is
said to stack) and sets up a new goal, a subgoal, to prove the IF part of
this rule. Then the knowledge base is searched again for rules that can
prove the subgoal. The inference engine repeats the process of stacking
the rules until no rules are found in the knowledge base to prove the
current subgoal.
40

Backward chaining
41

How do we choose between forward and backward chaining?
If an expert first needs to gather some information and then tries to infer
from it whatever can be inferred, choose the forward chaining inference
engine.
However, if your expert begins with a hypothetical solution and then
attempts to find facts to prove it, choose the backward chaining inference
engine.
42

7. Conflict resolution
Earlier we considered two simple rules for crossing a road. Let us now
add the third rule:
Rule 1: IF the ‘traffic light’ is green THEN the action is go
Rule 2: IF the ‘traffic light’ is red THEN the action is stop
Rule 3: IF the ‘traffic light’ is red THEN the action is go
43

7. Conflict resolution
We have two rules, Rule 2 and Rule 3, with the same IF part. Thus both of them can
be set to fire when the condition part is satisfied. These rules represent a conflict
set. The inference engine must determine which rule to fire from such a set. A
method for choosing a rule to fire when more than one rule can be fired in a given
cycle is called conflict resolution.
In forward chaining, BOTH rules would be fired. Rule 2 is fired first as the topmost
one, and as a result, its THEN part is executed and linguistic object action obtains
value stop. However, Rule 3 is also fired because the condition part of this rule
matches the fact ‘traffic light’ is red, which is still in the database. As a
consequence, object action takes new value go.
44

Methods used for conflict resolution
● Fire the rule with the highest priority. In simple applications, the priority can be
established by placing the rules in an appropriate order in the knowledge
base. Usually this strategy works well for expert systems with around 100
rules.
● Fire the most specific rule. This method is also known as the longest
matching strategy. It is based on the assumption that a specific rule
processes more information than a general one.
● Fire the rule that uses the data most recently entered in the database. This
method relies on time tags attached to each fact in the database. In the
conflict set, the expert system first fires the rule whose antecedent uses the
data most recently added to the database.
45

Metaknowledge
● Metaknowledge can be simply defined as knowledge about knowledge.
Metaknowledge is knowledge about the use and control of domain
knowledge in an expert system.
● In rule-based expert systems, metaknowledge is represented by metarules. A
metarule determines a strategy for the use of task-specific rules in the expert
system.
46

Metarules
● Metarule 1:
Rules supplied by experts have higher priorities than rules supplied by
novices.
● Metarule 2:
Rules governing the rescue of human lives have higher priorities than rules
concerned with clearing overloads on power system equipment.
47

8. Advantages of rule-based expert systems
Natural knowledge representation. An expert usually explains the
problem-solving procedure with such expressions as this: “In such-and-such
situation, I do so-and-so”. These expressions can be represented quite
naturally as IF-THEN production rules.
Uniform structure. Production rules have the uniform IF-THEN structure. Each
rule is an independent piece of knowledge. The very syntax of production
rules enables them to be self documented.
48

8. Advantages of rule-based expert systems
Separation of knowledge from its processing. The structure of a rule-based
expert system provides an effective separation of the knowledge base from
the inference engine. This makes it possible to develop different applications
using the same expert system shell.
Dealing with incomplete and uncertain knowledge. Most rule-based expert
systems are capable of representing and reasoning with incomplete and
uncertain knowledge.
49

9. Disadvantages of rule-based expert systems
Opaque relations between rules. Although the individual production rules are
relatively simple and self-documented, their logical interactions within the large
set of rules may be opaque. Rule-based systems make it difficult to observe how
individual rules serve the overall strategy.
Ineffective search strategy. The inference engine applies an exhaustive search
through all the production rules during each cycle. Expert systems with a large set
of rules (over 100 rules) can be slow, and thus large rule-based systems can be
unsuitable for real-time applications.
50

9. Disadvantages of rule-based expert systems
Inability to learn. In general, rule-based expert systems do not have an ability to
learn from the experience. Unlike a human expert, who knows when to “break the
rules”, an expert system cannot automatically modify its knowledge base, or
adjust existing rules or add new ones. The knowledge engineer is still responsible
for revising and maintaining the system.
51

Thanks for your attention!
52
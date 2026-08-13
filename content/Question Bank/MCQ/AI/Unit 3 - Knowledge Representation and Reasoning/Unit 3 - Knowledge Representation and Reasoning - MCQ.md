# Unit 3 - Knowledge Representation and Reasoning - MCQ

**Course:** Introduction to Artificial Intelligence
**Title pattern:** `Introduction to Artificial Intelligence - MCQ - U.S.Q`
**Set 1 (questions 1 to 20) is the upload set.** It covers all 11 subtopics of this unit.
**Set 2 (questions 21 to 50) is the reserve bank.**

## Subtopic coverage in the upload set

| Subtopic | Covered by |
| --- | --- |
| `knowledge-based-systems` | 3.1.1, 3.1.19 |
| `knowledge-representation` | 3.1.2 |
| `rule-based-reasoning` | 3.1.3, 3.1.11 |
| `propositional-logic` | 3.1.4, 3.1.12 |
| `first-order-predicate-logic` | 3.1.5, 3.1.13 |
| `logical-inference` | 3.1.6, 3.1.14 |
| `inference-techniques` | 3.1.7, 3.1.15 |
| `semantic-knowledge-models` | 3.1.8, 3.1.16 |
| `reasoning-under-uncertainty` | 3.1.9, 3.1.17 |
| `bayesian-networks` | 3.1.10, 3.1.18 |
| `ai-planning` | 3.1.20 |

---

# Set 1

## Introduction to Artificial Intelligence - MCQ - 3.1.1

**description**
A car dealership's diagnostic system is built so that every fault pattern its senior technician knows sits in one file, while the procedure that matches symptoms to conclusions sits in another and contains no knowledge of cars at all. Which benefit follows most directly from that separation?

- **option1** New fault patterns can be added without the program being rewritten
- **option2** The system runs faster, because the matching procedure can be optimised independently of the knowledge
- **option3** The system needs less memory, because rules are stored once rather than repeated inside the procedure that uses them
- **option4** The technician no longer needs to be consulted once the first version has shipped

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-based-systems

**explanation**
Separating what the system knows from how it reasons means knowledge can change without the program changing, which is the point of the architecture. Three further benefits follow: the domain expert can read the knowledge, the reasoning is reusable across domains, and the system can explain itself from the record of which rules fired.

## Introduction to Artificial Intelligence - MCQ - 3.1.2

**description**
A team writes the eligibility conditions for a scholarship as a function containing a sequence of checks. A reviewer suggests writing them instead as statements that are either true or false. What does the change buy, and what does it cost?

- **option1** It buys speed, at the cost of the conditions no longer being readable by anyone outside the team
- **option2** It buys the ability to change one condition without affecting the others, at the cost of the conditions no longer being able to reference each other in any way
- **option3** It buys both speed and inspectability, with no cost worth recording
- **option4** It buys inspection by a domain expert and reuse by any procedure, at the cost of speed since the use must be derived

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-representation

**explanation**
Declarative knowledge is statements that are true or false, so it can be read and checked by a domain expert and consulted by any procedure. Procedural knowledge is faster because the use is already decided, and it serves only the purpose it was written for. Editing one declarative statement updates every use, which is the change property that makes it worth the speed penalty.

## Introduction to Artificial Intelligence - MCQ - 3.1.3

**description**
A student reorders the rules in a rule base, moving what she considers the most important rule to the top, and is surprised that the conclusions reached are unchanged. Why?

- **option1** Because the engine fires rules in the order written, and her rule was already reachable from the first cycle
- **option2** Because position in the list is not control flow; every rule whose conditions hold is eligible each cycle
- **option3** Because rule bases are compiled into a fixed order before execution
- **option4** Because the conclusions of a rule base are determined by its facts alone, so no arrangement or content of the rules can affect what is ultimately derived

**answer** 2
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** rule-based-reasoning

**explanation**
Each cycle the engine matches every rule against working memory, collects the eligible ones into a conflict set, and resolves which to fire. Order in the list is not control flow, which is exactly what lets knowledge be added without reading the rest of the base. Conflict resolution can depend on ordering, but that is a choice of strategy rather than a property of the list.

## Introduction to Artificial Intelligence - MCQ - 3.1.4

**description**
A student insists that "if the server is down then the alert fires" must be false on a morning when the server was never down and no alert fired. Under the truth table for IMPLIES, is she right?

- **option1** No, since IMPLIES is true whenever the first part is false, regardless of the second
- **option2** No, since IMPLIES is true whenever both parts have the same truth value, which they do on this particular morning
- **option3** Yes, since an implication can only be evaluated on a day when the condition actually occurred
- **option4** Yes, since neither part of the statement was true

**answer** 1
**difficulty** easy
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** propositional-logic

**explanation**
IMPLIES is true exactly when the first part is false or the second is true, so a day on which the server stayed up cannot falsify the rule. This is the operator students find strangest, because ordinary speech treats "if" as suggesting a connection. The answer about both parts sharing a truth value describes IF AND ONLY IF, which is a different operator.

## Introduction to Artificial Intelligence - MCQ - 3.1.5

**description**
Which pair of quantifier and connective is the normal combination, and why?

- **option1** Existential with implication, since the existence of one object implies the property holds
- **option2** Universal with implication, and existential with conjunction
- **option3** Universal with conjunction, since a claim about every object asserts several things at once
- **option4** Either quantifier with either connective, since the choice affects only readability rather than the meaning of the statement

**answer** 2
**difficulty** easy
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** first-order-predicate-logic

**explanation**
A universal statement restricts its claim to a subset, so it reads "for every x, if x is a student then x is enrolled", which needs implication. An existential statement asserts something about at least one object, so it reads "there is an x that is a student and is barred", which needs conjunction. Swapping them produces statements that are trivially true or far stronger than intended.

## Introduction to Artificial Intelligence - MCQ - 3.1.6

**description**
A knowledge base is said to entail a statement. What exactly does that mean?

- **option1** That the statement can be derived by applying the inference rules available to the system
- **option2** That the statement is true in every situation in which everything in the knowledge base is true
- **option3** That the statement appears in the knowledge base, either directly or as part of a larger statement
- **option4** That the statement is true in at least one situation in which everything in the knowledge base is true, which is what makes it consistent with what is already known

**answer** 2
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** logical-inference

**explanation**
Entailment is defined over models, meaning every assignment of truth values consistent with the knowledge base. Derivability is what a procedure achieves, and the two coincide only when the procedure is sound and complete. The answer requiring truth in at least one situation describes satisfiability, which is much weaker than entailment.

## Introduction to Artificial Intelligence - MCQ - 3.1.7

**description**
A diagnostic consultation asks the user five questions and examines three rules before reaching an answer. Running the same knowledge base the other way fires eight rules and needs ten observations. Which technique is which, and what explains the difference?

- **option1** Both are forward chaining, differing only in the order in which the rules were listed
- **option2** Forward chaining asked five questions, since it stops as soon as the goal appears in working memory
- **option3** Backward chaining asked five questions, since it pursues only what bears on the goal, while forward chaining computed everything derivable
- **option4** Backward chaining fired eight rules, since establishing a goal requires proving every rule that mentions it before any conclusion can be drawn

**answer** 3
**difficulty** easy
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** inference-techniques

**explanation**
Backward chaining is goal-driven and touches only what is relevant to the question asked, which is why it needed three rules and five questions. Forward chaining is data-driven and computes everything derivable whether or not anyone wanted it. Neither is better in general: forward chaining suits monitoring a stream, backward chaining suits answering one question.

## Introduction to Artificial Intelligence - MCQ - 3.1.8

**description**
A semantic network records that a sparrow is a bird, and that birds have feathers. Asked whether a sparrow has feathers, the system answers yes, although that fact was never stored. What produced the answer?

- **option1** Inheritance along the is-a link, so the answer came from the shape of the network rather than from a stored fact
- **option2** A default value stored in the sparrow node when it was defined
- **option3** A search of the network for any node containing the word feathers, followed by a check of whether that node is connected to the sparrow node by any path
- **option4** A rule in the inference engine that adds properties to every new node as it is created

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** semantic-knowledge-models

**explanation**
Semantic networks let properties be inherited from general categories down to specific instances, so the organisation itself supports inference. Defaults belong to frames, which are named records of slots. A path search would find a connection without establishing that the connection means the property applies, which is what the is-a link specifically encodes.

## Introduction to Artificial Intelligence - MCQ - 3.1.9

**description**
At a health camp, one percent of those screened have the condition, the test catches 99 percent of real cases, and a positive result gives a 16.7 percent chance of actually being ill. A volunteer hears "99 percent accurate" and tells a patient he is almost certainly ill. What has he done?

- **option1** Confused sensitivity with specificity, which are the two ways a test can be described
- **option2** Committed base rate neglect, by reading the likelihood as if it were the answer and ignoring how rare the condition is
- **option3** Used the prior correctly but applied the wrong likelihood
- **option4** Made no error, since a test that catches 99 percent of cases does make a positive result overwhelmingly likely to be correct whenever the test is applied to a genuine screening population

**answer** 2
**difficulty** easy
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** reasoning-under-uncertainty

**explanation**
The probability of a positive test given the disease is not the probability of the disease given a positive test. With one percent prevalence, most positives come from the far larger healthy group, which is why the posterior is 16.7 percent rather than 99. Ignoring the prior and reading the likelihood as the answer is base rate neglect.

## Introduction to Artificial Intelligence - MCQ - 3.1.10

**description**
A Bayesian network for hostel absences contains no arrow from Illness to Late Night. What does the absence of that arrow assert?

- **option1** That the two variables never occur together in the recorded data
- **option2** That the network is incomplete, since a full model requires an arrow between every pair of variables that could conceivably be related
- **option3** That illness and a late night are equally likely explanations for an absence
- **option4** That there is no direct probabilistic influence between them, which is a claim the network records rather than an omission

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** bayesian-networks

**explanation**
A Bayesian network records the relationships that are not there as deliberately as the ones that are, and those absences are what make it compact. Most variables in any real domain do not directly affect most others. An arrow between every pair would restore the full joint distribution and destroy the saving the network exists to provide.

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 3.1.11

**description**
In a rule-based engine, three rules are eligible on the same cycle. What is the name for that collection, and what happens next?

- **option1** The working memory, which is then updated with all three conclusions at once
- **option2** The conflict set, from which conflict resolution chooses one rule to fire
- **option3** The rule base, which is re-matched against the facts until only one rule remains eligible
- **option4** The match set, which is discarded because a cycle in which more than one rule applies is treated as an inconsistency in the knowledge base

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** rule-based-reasoning

**explanation**
The cycle is match, then resolve, then act. Matching produces the conflict set of all eligible rules, conflict resolution picks one, and acting adds its conclusion to working memory. Working memory holds the facts about the case in hand, and the rule base holds the general domain knowledge that does not change from case to case.

## Introduction to Artificial Intelligence - MCQ - 3.1.12

**description**
A formula involves four propositions. A student proposes to settle whether it is always true by checking every possible situation. How many situations must she check, and what does this method replace?

- **option1** Sixteen situations, replacing argument entirely
- **option2** Eight situations, replacing the need for a formal proof
- **option3** Sixteen situations, replacing only the need to reason about the operators individually, since each operator's meaning must still be established separately before the check can begin
- **option4** Four situations, replacing the need to construct a truth table

**answer** 1
**difficulty** medium
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** propositional-logic

**explanation**
A formula over n propositions has exactly two to the power n possible situations, so four propositions give sixteen. Because every one can be checked mechanically, exhaustive checking replaces argument entirely: there is nothing left to debate once all sixteen rows agree. The method is complete and it is also why the approach stops scaling.

## Introduction to Artificial Intelligence - MCQ - 3.1.13

**description**
Two statements differ only in the order of their quantifiers: "for every student there exists a course they are enrolled in" and "there exists a course such that every student is enrolled in it". Are they equivalent?

- **option1** No, and the first is the stronger claim, since it must hold for every student individually
- **option2** Yes, since both assert a relationship between all students and at least one course
- **option3** No, and the second is the stronger claim, since it requires one single course shared by everyone
- **option4** They cannot be compared, since a statement mixing quantifiers has no fixed meaning until the domain of objects has been specified

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** first-order-predicate-logic

**explanation**
With mixed quantifiers, order changes the meaning. The first allows each student a different course. The second demands one course that every student takes, which implies the first but is not implied by it. Reading these the wrong way round is the commonest source of subtly wrong formalisations.

## Introduction to Artificial Intelligence - MCQ - 3.1.14

**description**
An inference procedure is described as sound but not complete. What does a team using it need to worry about?

- **option1** That some conclusions it draws may be false
- **option2** That its conclusions are correct only for knowledge bases small enough for every model to be enumerated and checked directly
- **option3** That it may loop indefinitely on knowledge bases containing implications
- **option4** That it may fail to draw conclusions that genuinely follow

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** logical-inference

**explanation**
Soundness means everything derived is entailed, so nothing false is produced, and it is non-negotiable because without it the output is untrustworthy. Completeness means everything entailed can be derived, and its absence means missed conclusions rather than false ones. Missing a conclusion is a real risk and a survivable one; asserting a falsehood is not.

## Introduction to Artificial Intelligence - MCQ - 3.1.15

**description**
A factory wants a system that watches a continuous stream of sensor readings and raises alerts as conditions develop. Which inference technique fits, and why?

- **option1** Backward chaining, since each possible alert can be treated as a goal to be tested
- **option2** Backward chaining, since it touches only the rules relevant to the alert currently under consideration
- **option3** Neither, since a continuous stream must be reduced to discrete cases before any rule-based technique can be applied to it
- **option4** Forward chaining, since it is data-driven and its cost scales with change rather than with the size of the knowledge base

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** inference-techniques

**explanation**
Forward chaining suits monitoring, alerting and streams of sensor data, because new facts arrive continuously and the engine derives whatever now follows. Backward chaining becomes wasteful when many goals must be tested against the same facts, which is exactly the situation when every possible alert is a separate goal.

## Introduction to Artificial Intelligence - MCQ - 3.1.16

**description**
Two hospitals want their systems to agree on what terms such as "admission" and "discharge" mean, so records can be exchanged without either side reinterpreting them. Which semantic model is designed for that purpose?

- **option1** Frames
- **option2** Semantic network
- **option3** Ontology
- **option4** Knowledge graph

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** semantic-knowledge-models

**explanation**
An ontology adds formal classes, properties and axioms, which makes consistency checkable and lets systems share meaning, so agreeing vocabulary across organisations is its central use. A knowledge graph is best where scale and multi-hop querying matter, frames describe structured objects with typical values, and a semantic network shows how concepts relate.

## Introduction to Artificial Intelligence - MCQ - 3.1.17

**description**
In Bayes' theorem, what role does the likelihood play?

- **option1** How well a hypothesis predicts the evidence
- **option2** Belief in the hypothesis before this case's evidence
- **option3** Belief in the hypothesis after the evidence has been taken into account
- **option4** The proportion of the population for whom the hypothesis holds, measured before the evidence is gathered and used to weight the result

**answer** 1
**difficulty** medium
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** reasoning-under-uncertainty

**explanation**
The prior is belief before the evidence, the likelihood is how well each hypothesis predicts the evidence, and the posterior is belief afterwards. The answer about the proportion of the population describes the prior in different words. Keeping the three apart is what stops a 99 percent detection rate being misread as a 99 percent chance of illness.

## Introduction to Artificial Intelligence - MCQ - 3.1.18

**description**
A student is absent. Observing a fever raises belief in illness from 10 percent to about 64 percent. Learning separately that the student had a late night then lowers belief in illness again. What is the second effect called?

- **option1** Diagnostic reasoning, since belief is being revised in the light of an observation
- **option2** Base rate neglect, since the prior is being overwritten by the new evidence
- **option3** Explaining away, since a confirmed alternative cause reduces the need to invoke the first one
- **option4** Conditional independence, since the two causes are unrelated in the network

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** bayesian-networks

**explanation**
Explaining away is the effect in which confirming one cause lowers belief in a competing cause of the same observed effect. Diagnostic reasoning is the more general name for inferring causes from effects and describes the first step, from fever to illness. Conditional independence is a structural property of the network rather than a change in belief.

## Introduction to Artificial Intelligence - MCQ - 3.1.19

**description**
Which component of a knowledge-based system makes it possible to answer "why did you conclude that", and what does it hold?

- **option1** The knowledge base, which holds the general facts and rules of the domain
- **option2** The explanation facility, which holds the record of which rules fired and why
- **option3** The working memory, which holds the facts about the case in hand
- **option4** The inference engine, which holds the reasoning procedure and can therefore reconstruct any conclusion on demand

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-based-systems

**explanation**
The explanation facility records the chain of rules that fired, which is the argument a technician can check or challenge. The inference engine carries out the reasoning but holds no domain knowledge and no history of a particular case, so it cannot on its own say why a conclusion was reached for this customer this morning.

## Introduction to Artificial Intelligence - MCQ - 3.1.20

**description**
A planner is given an action specified with a precondition, an add list and a delete list. What does the delete list express, and what is assumed about everything not mentioned?

- **option1** Facts that stop being true, with everything unmentioned assumed unchanged
- **option2** Facts that must not hold before the action, with everything unmentioned assumed false
- **option3** Actions that become unavailable afterwards, with everything unmentioned assumed still available
- **option4** Facts the planner should stop tracking, with everything unmentioned reassessed against the goal at the end of every step in the plan

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** ai-planning

**explanation**
An action states what must hold before it can be taken and what changes when it is taken: the add list becomes true, the delete list stops being true, and everything else carries over untouched. That last assumption is what keeps state descriptions manageable, since otherwise every action would have to restate the entire world.

---

# Set 3

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 3.2.1

**description**
Why is it an advantage that a knowledge-based system's inference engine contains no domain knowledge?

- **option1** Because it reduces the amount of code that has to be tested before release
- **option2** Because the same reasoning machinery can then be reused on a completely different domain
- **option3** Because the engine can then be replaced without consulting anyone
- **option4** Because domain knowledge held inside an engine would have to be recompiled each time an expert corrected a single fact about the domain

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-based-systems

**explanation**
Reusable reasoning is one of the four benefits of the separation, alongside knowledge changing without the program changing, the expert being able to read the knowledge, and the system being able to explain itself. Swap the knowledge base and the same engine diagnoses a different domain.

## Introduction to Artificial Intelligence - MCQ - 3.2.2

**description**
Representational adequacy is one test of a knowledge representation. What does it ask?

- **option1** Whether the representation can be stored efficiently
- **option2** Whether the representation can be translated into any other representation without loss of the information it was originally built to hold
- **option3** Whether the representation can be read by a domain expert
- **option4** Whether the representation can express everything the domain requires

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-representation

**explanation**
Adequacy is about expressive reach: if the domain contains something the notation cannot say, no amount of efficiency rescues it. Storage efficiency and readability are separate and also real criteria, which is why a representation is judged on several axes rather than one.

## Introduction to Artificial Intelligence - MCQ - 3.2.3

**description**
A rule base has grown to several hundred rules maintained by a domain expert with no programming background. Which property of rule-based reasoning makes that arrangement workable?

- **option1** That rules execute in the order written, so the expert can reason about the sequence
- **option2** That knowledge can be added without reading the rest, and the rules are inspectable by their owner
- **option3** That the engine automatically resolves any contradiction between two rules
- **option4** That the number of rules has no effect on the time taken to reach a conclusion, however large the base becomes

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** rule-based-reasoning

**explanation**
Because position is not control flow, a new rule can be written without tracing what the other rules do, and each rule reads as a self-contained statement the expert can check. Contradictions are not resolved automatically, and larger bases do cost more to match, so the last two answers claim guarantees the approach does not offer.

## Introduction to Artificial Intelligence - MCQ - 3.2.4

**description**
Which operator is true exactly when at least one of its two arguments is true, including the case where both are?

- **option1** IF AND ONLY IF
- **option2** OR
- **option3** IMPLIES
- **option4** AND

**answer** 2
**difficulty** easy
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** propositional-logic

**explanation**
OR in logic is inclusive, so both being true still satisfies it, which differs from the exclusive sense of "or" common in speech. AND requires both, IF AND ONLY IF requires the two to agree, and IMPLIES is satisfied whenever the first part is false.

## Introduction to Artificial Intelligence - MCQ - 3.2.5

**description**
What distinguishes a function from a predicate in first-order logic?

- **option1** A function can be quantified over, while a predicate cannot
- **option2** A function takes one argument, while a predicate takes two or more
- **option3** A function maps objects to objects, while a predicate is true or false of the objects it applies to
- **option4** A function names one specific object in the domain, while a predicate describes a property that may be shared by many objects at once

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** first-order-predicate-logic

**explanation**
Instructor of a course returns a person, so it is a function; Student applied to a person returns true or false, so it is a predicate. Argument count is not the distinction, since a relation is simply a predicate over two or more objects. Naming one specific object is what a constant does.

## Introduction to Artificial Intelligence - MCQ - 3.2.6

**description**
Model checking is described as direct and clear but impractical beyond small problems, while deduction scales. What accounts for the difference?

- **option1** Model checking enumerates possible situations, whose number grows explosively, while deduction manipulates the statements themselves
- **option2** Model checking requires a complete knowledge base, whereas deduction tolerates gaps
- **option3** Model checking is unsound on large knowledge bases, whereas deduction remains sound at any scale
- **option4** Model checking must be carried out by hand, whereas deduction can be automated once the inference rules have been programmed into the system

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** logical-inference

**explanation**
Enumerating models means listing every assignment of truth values, and that count doubles with each additional proposition. Deduction applies inference rules to the statements without ever building the space of situations, which is why it scales. Model checking remains perfectly sound; it simply becomes unaffordable.

## Introduction to Artificial Intelligence - MCQ - 3.2.7

**description**
Backward chaining produces a natural explanation of a particular shape. What is it?

- **option1** Here is everything that follows from what you told me
- **option2** Here are the facts I could not derive from the rules available
- **option3** Here is the complete set of rules that were examined, listed in the order the engine considered them during the consultation
- **option4** Here is why I am asking this question, and here is why the answer holds

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** inference-techniques

**explanation**
Because backward chaining works from a goal towards the facts that would establish it, every question it asks has a reason attached, and the chain of rules from goal to evidence is the justification. Forward chaining explains differently, presenting what follows from the data supplied.

## Introduction to Artificial Intelligence - MCQ - 3.2.8

**description**
Which semantic model is best suited to describing structured objects that have typical values, such as a hotel booking with a default check-out time?

- **option1** Semantic network
- **option2** Ontology
- **option3** Knowledge graph
- **option4** Frames

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** semantic-knowledge-models

**explanation**
Frames are named records of slots and add grouping, defaults and attached procedures, which fits an object with a typical value that can be overridden. Ontologies exist to agree vocabulary across systems, knowledge graphs to hold enormous numbers of triples, and semantic networks to show how concepts relate.

## Introduction to Artificial Intelligence - MCQ - 3.2.9

**description**
At the camp, 9,405 of the 9,900 healthy people were correctly cleared. Which quantity does that ratio describe?

- **option1** Sensitivity
- **option2** Prior
- **option3** Specificity
- **option4** Posterior

**answer** 3
**difficulty** medium
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** reasoning-under-uncertainty

**explanation**
Specificity is the probability of a negative result given that the person is well, so it is the rate at which healthy people are cleared. Sensitivity is the mirror image, the rate at which real cases are caught. The remaining 495 healthy people who tested positive are what drags the posterior down to 16.7 percent.

## Introduction to Artificial Intelligence - MCQ - 3.2.10

**description**
Why does a Bayesian network need only a small table at each node rather than one enormous table over all variables?

- **option1** Because each node's probabilities are conditioned only on its parents, and most variables do not directly affect most others
- **option2** Because the tables are compressed and expanded on demand during inference
- **option3** Because variables with more than two possible values are excluded from the network by construction
- **option4** Because the network stores only those combinations of values that were actually observed in the data used to build it

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** bayesian-networks

**explanation**
Conditional independence is the saving: once a node's parents are known, the remaining variables add nothing to its distribution. The full joint distribution is then reconstructed from the small tables when needed. Nothing is discarded, which is why the network can still answer questions about combinations never seen in the data.

---

# Set 4

## Introduction to Artificial Intelligence - MCQ - 3.2.11

**description**
A team stores the working hours of every branch as procedural code inside the booking function. Head office then asks for the same hours to drive an availability display and a reporting tool. What problem does the original choice create?

- **option1** The hours cannot be read by anyone without running the booking function, and they serve only the purpose they were written for
- **option2** The hours will be slower to access than if they had been stored declaratively
- **option3** The hours cannot be changed once the booking function has been deployed
- **option4** The hours will be inconsistent between the three tools, because procedural knowledge is re-evaluated separately each time any one of the tools requests it

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-representation

**explanation**
Procedural knowledge can only be run and observed, and it serves the one purpose it was written for, which is exactly the bind here. Declarative statements can be consulted by any procedure and edited in one place. Procedural representations are typically faster, not slower, since the use is already decided.

## Introduction to Artificial Intelligence - MCQ - 3.2.12

**description**
A rule base contains a rule whose conclusion is also one of its own conditions. What is the practical risk?

- **option1** The engine will refuse to load the rule base, since self-reference is syntactically invalid
- **option2** The rule can never fire, since its conclusion cannot be present before it has fired
- **option3** Nothing, since forward chaining adds each conclusion once and a fact already present changes nothing
- **option4** The rule will fire on every cycle indefinitely, since its conclusion continually re-satisfies its own condition

**answer** 3
**difficulty** hard
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** rule-based-reasoning

**explanation**
Working memory is a set of facts, so adding a fact that is already present has no effect and the cycle reaches a fixed point. The rule can fire, provided its other conditions hold. Endless firing would require the conclusion to change working memory each time, which adding an existing fact does not do.

## Introduction to Artificial Intelligence - MCQ - 3.2.13

**description**
Which situation makes the exhaustive checking of a propositional formula impractical, and what is the underlying reason?

- **option1** Formulas that are false in every situation, since the check cannot terminate early
- **option2** Formulas containing IMPLIES, since implication cannot be evaluated mechanically
- **option3** Formulas over many propositions, since the number of situations doubles with each one added
- **option4** Formulas mixing several different operators, since each operator requires its own separate pass over the table of situations before the result can be combined

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** propositional-logic

**explanation**
Two to the power n grows fast enough that twenty propositions already give over a million rows and fifty is hopeless. Every operator including IMPLIES is defined by a fixed truth table and evaluates mechanically, and a formula false everywhere is detected as readily as any other.

## Introduction to Artificial Intelligence - MCQ - 3.2.14

**description**
Why does propositional logic struggle to express "every student enrolled in CS201 has submitted the assignment", and what does first-order logic add?

- **option1** Propositional logic cannot express negation over a group, and first-order logic adds negated predicates
- **option2** Propositional logic would need one proposition per student, and first-order logic adds predicates over objects together with quantifiers
- **option3** Propositional logic cannot represent time, and first-order logic adds temporal operators
- **option4** Propositional logic has no way to combine two statements into one, and first-order logic adds conjunction so several claims can be asserted together in a single formula

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** first-order-predicate-logic

**explanation**
In propositional logic each student would need a separate atomic proposition, and the general claim could not be stated at all. First-order logic breaks statements into predicates applied to objects and quantifies over those objects, so one formula covers every student including ones not yet enrolled.

## Introduction to Artificial Intelligence - MCQ - 3.2.15

**description**
An entailment check fails. Why is that outcome more useful than a simple report that the statement does not follow?

- **option1** Because the check identifies which statement in the knowledge base is incorrect
- **option2** Because it hands you a concrete counterexample, a situation satisfying the knowledge base in which the statement is false
- **option3** Because it proves the statement's negation is entailed instead
- **option4** Because it establishes that the knowledge base is inconsistent, which is a more serious fault and one worth discovering as early as possible

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** logical-inference

**explanation**
A model satisfying the knowledge base in which the query is false is exactly what refutes entailment, and it can be inspected. Failing to entail a statement does not entail its negation, since both may be undetermined, and it says nothing about the knowledge base being inconsistent.

## Introduction to Artificial Intelligence - MCQ - 3.2.16

**description**
When is forward chaining wasteful?

- **option1** When the facts arrive gradually rather than all at once, since each new arrival forces the entire derivation to be recomputed from the beginning
- **option2** When the knowledge base contains more rules than facts
- **option3** When many separate goals must be tested against the same set of facts
- **option4** When few of the derivable facts matter to the question actually being asked

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** inference-techniques

**explanation**
Forward chaining computes everything derivable, so if only a handful of those conclusions bear on the question, most of the work is discarded. Many goals against the same facts is the case where forward chaining wins and backward chaining becomes wasteful, since one forward pass serves them all.

## Introduction to Artificial Intelligence - MCQ - 3.2.17

**description**
A knowledge graph and a semantic network both store entities joined by labelled relationships. What does the knowledge graph add?

- **option1** Default values on entities, so a property can be assumed unless a specific entity overrides it with a value of its own
- **option2** Inheritance along is-a links, which a semantic network lacks
- **option3** Formal axioms that make the contents consistency-checkable
- **option4** Scale, easy merging, and multi-hop querying across billions of triples

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** semantic-knowledge-models

**explanation**
Knowledge graphs are the industrial-scale form, built from subject-predicate-object triples and used behind search panels, assistants and recommendations. Inheritance is what semantic networks already provide, axioms and consistency checking belong to ontologies, and defaults belong to frames.

## Introduction to Artificial Intelligence - MCQ - 3.2.18

**description**
Why do rules with exceptions push a system towards probabilistic reasoning?

- **option1** Because probability is faster to compute than matching a long list of exception rules
- **option2** Because probabilistic systems do not require a domain expert
- **option3** Because the exceptions cannot all be enumerated in advance, so a rule stated as certain will eventually be wrong
- **option4** Because a rule with exceptions is logically inconsistent, and a knowledge base containing an inconsistency permits any conclusion whatsoever to be derived from it

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** reasoning-under-uncertainty

**explanation**
Birds fly, except penguins, and injured ones, and ones in cages, and the list never closes. Degrees of belief let a system hold a strong expectation that evidence can revise, rather than a certainty that a single counterexample breaks. A rule with unlisted exceptions is incomplete rather than formally inconsistent.

## Introduction to Artificial Intelligence - MCQ - 3.2.19

**description**
In a Bayesian network, what is the difference between causal and diagnostic reasoning?

- **option1** Causal reasoning uses observed data while diagnostic reasoning uses only the prior probabilities
- **option2** Causal reasoning applies to deterministic networks and diagnostic reasoning to probabilistic ones
- **option3** Causal reasoning runs with the arrows, from causes to effects, while diagnostic reasoning runs against them
- **option4** Causal reasoning establishes which arrows belong in the network, while diagnostic reasoning uses the network once its structure has been fixed

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** bayesian-networks

**explanation**
Predicting a fever from a known illness follows the arrows and is causal. Inferring illness from an observed fever runs against them and is diagnostic, which is the direction most applications care about. The same network supports both, which is one of its attractions.

## Introduction to Artificial Intelligence - MCQ - 3.2.20

**description**
A warehouse planner produces a nine-step plan. Achieving the second subgoal undoes the first. What is this called, and what is the standard response?

- **option1** A delete list error, which is repaired by removing the offending fact from the delete list of the action that undid the first subgoal
- **option2** An inconsistent goal specification, which must be resolved by the person who wrote the goal
- **option3** A precondition violation, which is repaired by weakening the precondition of the offending action
- **option4** A subgoal interaction, which is detected and then repaired by reordering or by inserting further actions

**answer** 4
**difficulty** medium
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** ai-planning

**explanation**
Achieving one subgoal can undo another, and the planner's job is to detect the interaction and repair it rather than to treat the goal as impossible. Editing the delete list would misdescribe the world, since the fact really does stop being true when the action is taken.

---

# Set 5

## Introduction to Artificial Intelligence - MCQ - 3.2.21

**description**
A dealership replaces its diagnostic knowledge base with one for washing machines and changes nothing else. The system works. What does this demonstrate?

- **option1** That knowledge bases are interchangeable in general, so any knowledge base may be substituted for any other without adjustment
- **option2** That the two domains happen to share the same fault patterns
- **option3** That the explanation facility is independent of the knowledge base
- **option4** That the inference engine is general-purpose and holds no domain knowledge

**answer** 4
**difficulty** medium
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-based-systems

**explanation**
The reasoning is reusable precisely because the engine contains the procedure and none of the content. The answer claiming knowledge bases are interchangeable in general overgeneralises: the substitution works here because both domains suit the same rule form, not because any knowledge base fits any engine.

## Introduction to Artificial Intelligence - MCQ - 3.2.22

**description**
Which question does the frame problem raise for a knowledge representation?

- **option1** What stays the same when something changes
- **option2** How to decide which representation to use before the domain is fully understood
- **option3** How to store a representation compactly enough to fit in memory
- **option4** How to keep two representations of the same domain synchronised when either of them is edited independently of the other

**answer** 1
**difficulty** hard
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** knowledge-representation

**explanation**
Describing what an action changes is straightforward; describing everything it leaves alone is not, and stating it exhaustively is hopeless. Planning answers it by convention with the delete list, where anything unmentioned is assumed unchanged, which is a design decision rather than a discovered fact.

## Introduction to Artificial Intelligence - MCQ - 3.2.23

**description**
Conflict resolution strategies decide which eligible rule fires. Why does the choice of strategy matter even though the rule base itself is unchanged?

- **option1** Because an unfired rule is removed from the rule base for the remainder of the run
- **option2** Because the strategy determines whether the engine is sound
- **option3** Because firing a rule adds a fact, which can make other rules eligible or ineligible on later cycles
- **option4** Because each strategy interprets the conditions of a rule differently, so the same rule can match under one strategy and fail to match under another

**answer** 3
**difficulty** hard
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** rule-based-reasoning

**explanation**
The order in which conclusions enter working memory changes what is eligible next, so different strategies can reach different fixed points or reach the same one by different routes. Matching is a property of the rule and the facts, identical under every strategy, and rules are never removed from the base.

## Introduction to Artificial Intelligence - MCQ - 3.2.24

**description**
Under what circumstances is "if P then Q" false?

- **option1** Only when P is true and Q is false
- **option2** Only when both P and Q are false, since an implication with a false conclusion cannot be sustained
- **option3** Whenever P and Q differ in truth value
- **option4** Whenever P is false

**answer** 1
**difficulty** easy
**bloomTaxonomy** remember
**topics** knowledge-representation-and-reasoning
**subTopics** propositional-logic

**explanation**
IMPLIES is true when the first part is false or the second is true, so the single falsifying case is a true condition with a false conclusion. A false P makes the implication true regardless of Q, which is the result that surprises people most.

## Introduction to Artificial Intelligence - MCQ - 3.2.25

**description**
A student writes "for all x: Student(x) and Enrolled(x, CS201)" intending "every student is enrolled in CS201". What does the formula actually claim?

- **option1** That every object in the domain is a student and is enrolled in CS201
- **option2** That at least one object is both a student and enrolled in CS201
- **option3** Exactly what the student intended, since conjunction and implication are interchangeable under a universal quantifier
- **option4** That every student is enrolled in CS201, but only for those objects already known to the system to be students

**answer** 1
**difficulty** hard
**bloomTaxonomy** analyze
**topics** knowledge-representation-and-reasoning
**subTopics** first-order-predicate-logic

**explanation**
A universal quantifier ranges over everything in the domain, so pairing it with conjunction claims that every object whatsoever, including buildings and courses, is a student. Implication is what restricts the claim to students, which is why universal statements normally use it.

## Introduction to Artificial Intelligence - MCQ - 3.2.26

**description**
Why is soundness described as non-negotiable while completeness is merely desirable?

- **option1** Because completeness can always be recovered by running the procedure for longer
- **option2** Because soundness is easier to prove than completeness for most inference procedures
- **option3** Because an unsound procedure produces conclusions that are false, whereas an incomplete one only fails to produce some that are true
- **option4** Because an incomplete procedure can be detected at run time and reported, whereas unsoundness leaves no trace in the output that anyone could check against

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** knowledge-representation-and-reasoning
**subTopics** logical-inference

**explanation**
Without soundness the output cannot be trusted at all, which destroys the value of the system. Missing conclusions is a real cost and a survivable one, because what is produced remains reliable. Relative difficulty of proof is a practical matter and not the reason for the priority.

## Introduction to Artificial Intelligence - MCQ - 3.2.27

**description**
On the same rule base, forward chaining fired eight rules and needed ten observations while backward chaining examined three rules and asked five questions. What would reverse that advantage?

- **option1** Adding more rules to the base without changing the number of goals
- **option2** Needing to test many different goals against the same set of observations
- **option3** Reducing the number of observations the user is able to supply
- **option4** Replacing the observations with sensor readings, since automated input removes the cost of asking the user a question at all

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** knowledge-representation-and-reasoning
**subTopics** inference-techniques

**explanation**
Backward chaining wins when one question is asked, because it pursues only what bears on that goal. Once many goals must be tested, each requires its own backward pass while a single forward pass derives everything once. The saving reverses with the number of goals, not with the number of rules.

## Introduction to Artificial Intelligence - MCQ - 3.2.28

**description**
A frame for a delivery van has a slot that runs a procedure whenever its value is read. What capability does that illustrate?

- **option1** Inheritance, since the procedure is shared with every van of that type
- **option2** Slots that trigger procedures, so a value can be computed on demand rather than stored
- **option3** Consistency checking, since the procedure validates the value before returning it
- **option4** Multi-hop querying, since the procedure can follow relationships to other frames in order to assemble the value it returns

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** semantic-knowledge-models

**explanation**
Frames add grouping, defaults and attached procedures, and a slot that triggers a procedure lets a derived value such as remaining range be produced when asked for rather than kept up to date continuously. Consistency checking is what ontologies add, and multi-hop querying is a knowledge graph strength.

## Introduction to Artificial Intelligence - MCQ - 3.2.29

**description**
Two screening programmes use the same test. One screens a population with one percent prevalence and the other a high-risk group with thirty percent prevalence. What happens to the meaning of a positive result?

- **option1** It cannot be compared between the two programmes without recalibrating the test separately for each population being screened
- **option2** It is unchanged, since the test's sensitivity and specificity are properties of the test rather than of the population
- **option3** It becomes less informative in the high-risk group, because more positives are produced overall
- **option4** It becomes far more informative in the high-risk group, because the prior is higher and the posterior rises accordingly

**answer** 4
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** knowledge-representation-and-reasoning
**subTopics** reasoning-under-uncertainty

**explanation**
Sensitivity and specificity do belong to the test, and the posterior does not, because Bayes' theorem combines the likelihood with the prior. The same positive result means 16.7 percent in a one percent population and far more in a thirty percent one, which is why screening decisions depend on who is being screened.

## Introduction to Artificial Intelligence - MCQ - 3.2.30

**description**
Why is it an advantage that planning actions are described once and generally, rather than as a list of specific moves?

- **option1** Because a general description applies to every object it fits, so one action definition covers many concrete steps
- **option2** Because general descriptions are shorter and therefore faster to parse at run time
- **option3** Because a planner cannot accept two actions that differ only in the object they apply to
- **option4** Because a general description removes the need for preconditions, since the conditions are implied by the objects the action is applied to

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** knowledge-representation-and-reasoning
**subTopics** ai-planning

**explanation**
One definition of picking something up covers every object in the warehouse, and relevance then becomes visible because the planner can see which actions could achieve a given fact. Preconditions remain essential, since whether the gripper is empty is exactly what determines if the action is available.

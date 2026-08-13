# Unit 1 - Foundations of Artificial Intelligence - MCQ

**Course:** Introduction to Artificial Intelligence
**Title pattern:** `Introduction to Artificial Intelligence - MCQ - U.S.Q`
**Set 1 (questions 1 to 20) is the upload set.** It covers all 8 subtopics of this unit.
**Set 2 (questions 21 to 50) is the reserve bank.**

## Subtopic coverage in the upload set

| Subtopic | Covered by |
| --- | --- |
| `introduction-to-artificial-intelligence` | 1.1.1, 1.1.2, 1.1.10, 1.1.11 |
| `evolution-of-ai-paradigms` | 1.1.3, 1.1.12 |
| `branches-of-artificial-intelligence` | 1.1.4, 1.1.13 |
| `types-of-artificial-intelligence` | 1.1.5, 1.1.14 |
| `symbolic-ai-vs-learning-based-ai` | 1.1.6, 1.1.15, 1.1.20 |
| `ai-applications` | 1.1.7, 1.1.16 |
| `responsible-ai` | 1.1.8, 1.1.17, 1.1.18 |
| `future-of-ai` | 1.1.9, 1.1.19 |

## Question forms used

This unit has no code, so none of the Python or DBMS archetypes apply. Eleven forms are used instead: diagnose a failure, place a system on a taxonomy, attribute a cause, choose an engineering approach, predict the failure mode, evaluate a claim, judge what evidence supports, distinguish two near neighbours, identify what is missing, reason about a consequence, and decide what must be checked next.

---

# Set 1

## Introduction to Artificial Intelligence - MCQ - 1.1.1

**description**
A hostel fits two corridors with new lighting. Corridor A's lights come on at 6 pm and go off at 6 am on a timer. Corridor B's lights read ambient brightness and movement, staying dim until somebody walks past, and behaving differently on a bright afternoon than on a dark evening. A student insists both are artificial intelligence because neither needs a switch. Which statement best identifies the actual discriminator between them?

- **option1** Corridor A follows a fixed electrical schedule, which makes it a mechanical device rather than a computational one
- **option2** Corridor B runs without human intervention, while Corridor A still requires people
- **option3** Corridor B is the more expensive installation, and AI systems are the costly ones
- **option4** Corridor B changes its behaviour when the situation changes, with nobody rewriting its instructions

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
The test is whether behaviour adapts to a changing situation without a person editing the instructions, which is true of Corridor B and false of Corridor A. The answer about running without human intervention is the tempting one and it is wrong on the facts: both corridors run unattended, so running without a human separates nothing. Cost and the choice of hardware are irrelevant to the distinction.

## Introduction to Artificial Intelligence - MCQ - 1.1.2

**description**
A vendor pitching a warehouse system lists what it can do: it reads barcode scans from the floor, works out which shelf a carton belongs on, gets better at estimating pick times as more orders pass through, and holds eight million records in memory. Which item on that list is not one of the four characteristics an AI system typically shows?

- **option1** Working out which shelf a carton belongs on
- **option2** Improving its pick-time estimates as more orders pass through
- **option3** Reading barcode scans from the floor
- **option4** Holding eight million records in memory

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
The four characteristics are perception, reasoning, learning, and goal-directed action. Storage capacity is not among them, and neither is speed. A system can hold enormous amounts of data and run extremely fast while showing no intelligence at all, which is exactly why a calculator is not called intelligent. The other three items map onto perception, reasoning, and learning in turn.

## Introduction to Artificial Intelligence - MCQ - 1.1.3

**description**
A student writes that Deep Blue beating Kasparov in 1997 and AlphaGo beating Lee Sedol in 2016 were the same kind of achievement, twenty years apart. Her tutor disagrees. What is the substantive difference between the two systems?

- **option1** Grandmasters hand-tuned Deep Blue's scoring function, while AlphaGo learned its judgment of positions from games
- **option2** Deep Blue improved by playing millions of games against itself, whereas AlphaGo relied on an evaluation function that world champions wrote out by hand
- **option3** Both systems learned from data, and only the quantity of data separated them
- **option4** Neither system involved human input at any stage of its construction

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
Deep Blue sits in the symbolic search paradigm: humans encoded the chess knowledge and custom hardware searched roughly 200 million positions per second. AlphaGo learned position judgment from human games and then improved through self-play. The self-play answer states the correct facts about the wrong systems, which is the trap. The knowledge source, not the year or the board, is what separates the paradigms.

## Introduction to Artificial Intelligence - MCQ - 1.1.4

**description**
A toll plaza installs a system that photographs each vehicle as it approaches and extracts the registration number from the image so the account can be charged automatically. Which branch of AI is doing the central work here?

- **option1** Planning
- **option2** Computer Vision
- **option3** Natural Language Processing
- **option4** Knowledge Representation

**answer** 2
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
The branches divide by the kind of problem tackled, and this one is extracting meaning from pixels, which is computer vision. Natural Language Processing is the tempting wrong answer because a registration number is text, but the difficulty here is reading it off an image rather than understanding language. Planning concerns sequences of actions, and knowledge representation concerns storing facts so consequences follow.

## Introduction to Artificial Intelligence - MCQ - 1.1.5

**description**
AlphaGo defeated the strongest human Go player in the world. It cannot play chess, draughts, or any simpler board game, and it has never been asked to want anything. Where does it belong on the capability scale, and why?

- **option1** It resists classification, because the scale describes only systems that operate on language rather than on games
- **option2** ASI, since exceeding the best human in its domain is the definition of superintelligence
- **option3** AGI, since beating the best human at a game of that complexity demonstrates general reasoning
- **option4** ANI, because its capability is superhuman but confined to one task with no transfer to any other

**answer** 4
**difficulty** easy
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
The scale classifies by breadth of capability, not by how impressive the performance is. AlphaGo is narrow: superhuman inside one task and incapable outside it. The ASI answer is the strongest distractor, because ASI does involve exceeding humans, but the definition requires exceeding them in essentially every domain, not one. Every system that exists today is ANI.

## Introduction to Artificial Intelligence - MCQ - 1.1.6

**description**
A university helpdesk bot answers "how do I reset my password" instantly and correctly. A student then types "I've forgotten what I log in with" and gets "Sorry, I did not understand that." She rephrases as "password reset" and the bot returns the same page it had just refused to find. What does this pattern tell you about how the bot was built?

- **option1** It matches messages against a list of phrases, and no phrase in her wording matched a rule
- **option2** The model was trained for too few epochs and needs a longer training run before it will generalise
- **option3** The request was routed to a server that timed out before the intent could be resolved
- **option4** The system overfitted to its validation set, so it now performs well only on the exact examples it was scored against during development

**answer** 1
**difficulty** easy
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
Failing on a paraphrase and then succeeding on the exact keyword is the signature of a rule-based system comparing strings. It did not misunderstand her, because it never attempted to understand her. A learning-based system places a sentence near similar sentences and would have handled the paraphrase, which is why options mentioning training and overfitting point at the wrong family of system entirely.

## Introduction to Artificial Intelligence - MCQ - 1.1.7

**description**
A clinic has three years of handwritten prescriptions in a filing cabinet and wants them turned into searchable text so that a pharmacist can look up what a patient was given last year. Which of the five jobs AI does is being asked for here?

- **option1** Optimisation
- **option2** Personalisation
- **option3** Prediction
- **option4** Perception

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** ai-applications

**explanation**
Perception answers "what is in this image, audio, or text", which is precisely the task of turning a scanned handwritten page into readable characters. Prediction is the common wrong choice because the setting is medical, but nothing here forecasts a future event. Optimisation would arrange or route something, and personalisation would tailor output to one individual.

## Introduction to Artificial Intelligence - MCQ - 1.1.8

**description**
A dermatology screening tool reports 94 percent accuracy in testing. After deployment across several states, clinicians notice it performs noticeably worse on patients with darker skin. An audit finds the training images came overwhelmingly from clinics serving lighter-skinned populations. Which source of bias is this?

- **option1** Deployment bias
- **option2** Historical bias
- **option3** Measurement bias
- **option4** Representation bias

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
Representation bias is about who is in the dataset and who is missing, which is exactly what the audit found. Historical bias would mean the data faithfully recorded a past pattern of discrimination in outcomes. Measurement bias would mean a proxy stood in for the thing that mattered. Deployment bias would mean the tool was used differently from how it was designed. Naming the source correctly matters because each has a different remedy.

## Introduction to Artificial Intelligence - MCQ - 1.1.9

**description**
A crop advisory service serves farmers in districts where mobile data is slow, expensive, and often unavailable in the fields where photographs of diseased leaves are actually taken. The team needs disease identification to work while the phone is offline. Which emerging direction addresses this constraint most directly?

- **option1** Edge AI
- **option2** Agentic AI
- **option3** Multimodal AI
- **option4** Foundation models

**answer** 1
**difficulty** easy
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** future-of-ai

**explanation**
Edge AI moves the model onto the device instead of a data centre, which is what removes the dependence on connectivity. Its own open problem is fitting useful capability into a small model. Multimodal AI concerns reasoning across text, images and audio together, agentic AI concerns turning outputs into multi-step actions, and foundation models concern building once and adapting many times.

## Introduction to Artificial Intelligence - MCQ - 1.1.10

**description**
Optical character recognition, chess playing, and speech transcription were each treated as landmark artificial intelligence problems in their time. Today they are described as ordinary software features and nobody calls them AI. What is this pattern called, and what does it imply about the term?

- **option1** The AI effect, meaning the label attaches to whatever computers cannot yet do comfortably
- **option2** Automation bias, meaning people place more trust in a machine's recommendation than it has earned
- **option3** The knowledge acquisition bottleneck, meaning experts cannot state the rules they are following
- **option4** Combinatorial explosion, meaning the number of possibilities to be searched grows faster than any computer can keep pace with

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
The AI effect is the observation that once a problem is solved and shipped it stops feeling like intelligence, so the meaning of the term keeps shifting ahead of what has been achieved. The three distractors are all real concepts from this unit, which is what makes them useful here: automation bias belongs to human oversight, the acquisition bottleneck to expert systems, and combinatorial explosion to symbolic search.

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 1.1.11

**description**
A team builds a spam filter that reads incoming mail, judges whether each message is junk, and improves as users mark mistakes. A reviewer objects that it cannot be an AI system because it never does anything beyond moving mail into a folder. What is the best response?

- **option1** The reviewer is right, because a system that takes no action in the world fails the definition of AI
- **option2** The reviewer is right, but only until the filter is given permission to delete messages automatically
- **option3** The reviewer is wrong, because not every AI system shows all four characteristics strongly
- **option4** The reviewer is wrong, because sorting mail into a folder is itself a full example of goal-directed action in the physical world

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
The four characteristics describe what AI systems tend to exhibit, not a checklist every system must pass. A spam filter perceives, reasons and learns while acting only weakly, and a chess engine reasons and acts deeply while perceiving almost nothing. The answer calling folder-sorting a full example of goal-directed action gets the verdict right for the wrong reason, which is why the reasoning in an answer matters as much as the verdict.

## Introduction to Artificial Intelligence - MCQ - 1.1.12

**description**
A hospital tries to build a system that flags patients at risk of deterioration by encoding the judgment of its most experienced physician. In interview after interview she cannot state what she is responding to. Pressed, she says only that such patients "look wrong to me". The project stalls. Which known limitation has the team run into?

- **option1** Combinatorial explosion
- **option2** The knowledge acquisition bottleneck
- **option3** Representation bias in the training data
- **option4** The tendency of a learned model to produce a fluent answer that happens to be false

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
The knowledge acquisition bottleneck is the wall expert systems hit: experts frequently cannot articulate what they know, so there is nothing to write into the knowledge base. Combinatorial explosion is a different wall, about the number of possibilities to search. The two remaining options describe problems of learning-based systems, and no model is being trained here at all.

## Introduction to Artificial Intelligence - MCQ - 1.1.13

**description**
A warehouse robot photographs a shelf to confirm which carton is in front of it, works out an order in which to collect six items so the trip is shortest, and then drives and grips without knocking anything over. A student asks which single branch of AI the robot belongs to. Why is the question badly posed?

- **option1** Because the branches describe historical eras, so a system built today belongs to none of them
- **option2** Because one working system routinely combines several branches, here perception, planning, and robotics together
- **option3** Because robotics is not a branch of AI, being a mechanical engineering discipline that merely borrows AI components
- **option4** Because a system can belong to a branch only once it has been formally certified as operating in that domain

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
The branches divide by the kind of problem being tackled, and a real deployment tackles several at once: seeing the shelf is computer vision, ordering the six items is planning, and moving reliably in the physical world is robotics. The branches are a way of naming problems, not exclusive boxes into which whole systems are sorted.

## Introduction to Artificial Intelligence - MCQ - 1.1.14

**description**
A commentator argues that today's large language models are close to artificial general intelligence, citing their breadth across tasks they were never specifically trained for, and capabilities that appeared as the models grew. Which observation is the strongest counterweight to that claim?

- **option1** They pursue no goals of their own, since every objective they act on is supplied from outside
- **option2** They still make occasional factual mistakes, and a general intelligence would be correct every time
- **option3** They cannot beat AlphaGo at Go, which shows their reasoning is shallower than a specialised system's
- **option4** They were trained on text collected from the internet rather than on the kind of curated corpus that a genuinely general system would require in order to reason across domains

**answer** 1
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
Breadth and emergent capability are the real arguments for getting closer, so a counterweight has to address something they do not supply. The absence of self-directed goals is one: the goals remain entirely ours. The answer about occasional factual mistakes sets an unreasonable bar, since humans are also wrong sometimes. The answer about losing to AlphaGo misunderstands the claim, because no one argues AGI must beat every narrow system at its own speciality.

## Introduction to Artificial Intelligence - MCQ - 1.1.15

**description**
A college is designing a hybrid helpdesk assistant. A learned language model will interpret whatever a student types, and a rule layer will enforce institutional policy. One responsibility under discussion is deciding whether the assistant may show a student another student's marks. Where does it belong, and on what grounds?

- **option1** The rule layer, because a decision that is right 99 percent of the time is unacceptable here
- **option2** The learned layer, since the model already interprets the request and splitting the work across two layers would introduce avoidable latency into every single reply
- **option3** The learned layer, because the model can be trained on examples of appropriate and inappropriate disclosure
- **option4** Either layer, provided the assistant logs the decision so it can be reviewed afterwards

**answer** 1
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
The design principle for hybrid systems is to learn the perception and enforce the policy. Disclosure of someone else's marks is a guarantee, not a probability, so it belongs where correctness can be proved. The answer permitting either layer with logging is the subtle trap: logging tells you afterwards that a breach happened, which does not prevent it. Knowing which decisions may never be probabilistic is the core judgment here.

## Introduction to Artificial Intelligence - MCQ - 1.1.16

**description**
Four AI projects are proposed at a company. Which one shows the warning sign most likely to make it fail in deployment?

- **option1** Flagging invoices with unusual totals for a clerk to review, using five years of processed invoices as training data
- **option2** Predicting which of a fixed catalogue of spare parts a depot will need next month, from the depot's own order history
- **option3** Reading meter photographs submitted by field staff, checked against the billing system before any bill is issued
- **option4** Scoring job applicants for a role the company has never hired for, with the score used to reject candidates automatically

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** ai-applications

**explanation**
Deployments that work share four traits: a narrow well-defined task, labelled data that already exists as a by-product of the work, an error cost that is survivable or checked by a human, and a deployment environment resembling the training one. The applicant-scoring project breaks three at once, since there is no history for a role never hired for and nobody checks before rejection. The other three each keep a human or a system check between the model and the consequence.

## Introduction to Artificial Intelligence - MCQ - 1.1.17

**description**
After an audit finds their shortlisting model favours men, a team deletes the gender column from the training data, retrains, and reports that the model can no longer discriminate by gender because it never sees it. What is wrong with that conclusion?

- **option1** Removing any column reduces accuracy, and a less accurate model is by definition a less fair one
- **option2** Nothing is wrong, provided the team also confirms that no column explicitly records gender under a different name
- **option3** The conclusion holds for this model but will fail as soon as the model is retrained on newer data
- **option4** The model can still learn gender from correlated signals, so deleting the column removes the ability to measure the discrimination rather than the discrimination

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
A model that never sees gender can still infer it from a hundred correlated signals: the college attended, sports played, phrasing, a gap in employment. Amazon's hiring tool did exactly this, penalising resumes containing "women's" without any rule about gender. Deleting the column also removes the team's own ability to test for disparate treatment, which makes the situation harder to detect rather than better.

## Introduction to Artificial Intelligence - MCQ - 1.1.18

**description**
A vendor's datasheet reports 96 percent accuracy for a face verification product. A procurement officer asks for the figure broken down by skin tone and gender together. The vendor replies that the overall number already covers everyone. Why is the officer right to insist?

- **option1** Because accuracy is the wrong metric for verification, and only precision and recall are meaningful for this class of system
- **option2** Because an aggregate figure can be dominated by the groups the system handles well, concealing near-total failure on a subgroup
- **option3** Because vendors calculate accuracy differently, so the figure cannot be compared against a competitor's until both are recomputed
- **option4** Because 96 percent is too low for a security application regardless of how the errors are distributed

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
In the 2018 evaluation of commercial gender classification, error rates were under one percent for lighter-skinned men while one system erred on roughly a third of darker-skinned women. Every product could still advertise high overall accuracy, because the aggregate was dominated by the groups handled well. An evaluation that does not disaggregate by the groups the system will affect is not an evaluation.

## Introduction to Artificial Intelligence - MCQ - 1.1.19

**description**
A team demonstrates an agent that books travel end to end: it searches flights, compares fares, holds a seat, fills passenger details, and completes payment. The five-step demonstration works. In production the same agent completes far fewer bookings than expected, though no individual step has been found to be faulty. What best explains the gap?

- **option1** The demonstration was rehearsed, so the true failure must lie in one of the five steps and simply has not been isolated yet
- **option2** Reliability multiplies across a chain, so steps that each usually succeed combine into a task that often does not
- **option3** Production traffic is heavier, and the underlying model becomes less accurate as the number of concurrent requests rises
- **option4** Agents cannot make payments reliably, so any workflow ending in a transaction will always underperform its demonstration

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** future-of-ai

**explanation**
The main open problem for agentic AI is that reliability compounds downward across a chain of steps. Steps that each succeed most of the time combine into a task that frequently does not, with nothing individually broken. This is why the honest remedy is shorter chains, more reliable steps, or a person checking between them, rather than hunting for a single faulty component.

## Introduction to Artificial Intelligence - MCQ - 1.1.20

**description**
A bank must choose between a rule-based engine and a learned model for an internal tool, and the deciding factor is which kind of failure the team can live with. Which pair correctly describes the typical failure of each?

- **option1** Both fail the same way, by producing no output at all when the input falls outside what they were built for
- **option2** The rule engine degrades quietly as inputs drift; the learned model refuses inputs it cannot match
- **option3** The rule engine says it did not understand; the learned model returns a confident, fluent, wrong answer
- **option4** The rule engine returns an answer that is close but imprecise; the learned model returns an answer that is exact whenever it returns one at all

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
This is the most practically useful row of the comparison, because it names the risk being accepted. A symbolic system's failures are loud, visible and therefore safe: it stops and says so. A learned system's failures are quiet and plausible, which makes them far more dangerous wherever nobody checks. The answer about quiet drift and refused inputs states the correct pattern with the two systems swapped.

---

# Set 3

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 1.2.1

**description**
Ananya's map application reroutes her seconds before a junction because hundreds of phones ahead have slowed to walking pace. Match that behaviour to the characteristic it demonstrates: concluding that the slowdown means the road is blocked.

- **option1** Perception
- **option2** Reasoning
- **option3** Learning
- **option4** Goal-directed action

**answer** 2
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
Reasoning is drawing a conclusion that was never explicitly supplied, by combining what is known. Reading the speed signals is perception, improving future travel estimates from past journeys is learning, and issuing the turn instruction to minimise arrival time is goal-directed action. The same short episode contains all four, which is why it is worth separating them.

## Introduction to Artificial Intelligence - MCQ - 1.2.2

**description**
Two camps have historically pulled the field in different directions. One asks whether machines can replicate human thought itself; the other asks whether machines can act correctly in the world, whatever is happening inside them. Which camp does modern AI overwhelmingly follow, and what is the measure of success?

- **option1** The first, with success measured by how closely the internal processing resembles human cognition
- **option2** Neither, since the field abandoned both framings once statistical methods replaced logic
- **option3** The second, with success measured by whether the system chooses an action that sensibly serves its goal
- **option4** The first, since a system that cannot report on its own reasoning process is not accepted as intelligent by current standards

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
Modern AI is concerned with acting rationally: given what the system can perceive, does it choose an action that serves its goal. Ananya's app did not form a mental picture of the lorry or feel relief at finding a way around, and none of that mattered. The behaviour was intelligent even though the internal experience was nothing like a human's.

## Introduction to Artificial Intelligence - MCQ - 1.2.3

**description**
Place these four paradigms in the order they became dominant: deep learning, symbolic AI, machine learning with hand-chosen features, expert systems.

- **option1** Expert systems, symbolic AI, deep learning, machine learning with hand-chosen features
- **option2** Symbolic AI, machine learning with hand-chosen features, expert systems, deep learning
- **option3** Symbolic AI, expert systems, machine learning with hand-chosen features, deep learning
- **option4** Machine learning with hand-chosen features, symbolic AI, expert systems, deep learning

**answer** 3
**difficulty** easy
**bloomTaxonomy** remember
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
The sequence runs from knowledge written by humans towards knowledge extracted from data. Symbolic AI encoded logic directly, expert systems narrowed that ambition to one domain's rules, machine learning learned the patterns while humans still chose the features, and deep learning learned the features as well. Each step moved more of the burden from the human to the data.

## Introduction to Artificial Intelligence - MCQ - 1.2.4

**description**
A paradigm is described in this unit as a shared assumption about where a system's intelligence comes from. Why does that assumption matter so much in practice?

- **option1** Because it predicts how many engineers a project will require
- **option2** Because it determines how such systems are built, what they are good at, and how they fail
- **option3** Because paradigms are enforced by standards bodies, so a system that mixes them cannot be certified for commercial deployment in regulated industries
- **option4** Because it fixes the programming language and hardware that any system in that paradigm must use

**answer** 2
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
The assumption about where intelligence comes from propagates into everything downstream: the build process, the strengths, and the characteristic failure. That is why identifying a system's paradigm tells you so much so quickly. Nothing about paradigms dictates hardware, languages, team size, or certification.

## Introduction to Artificial Intelligence - MCQ - 1.2.5

**description**
A bank wants a system that can answer "why was this loan application declined" with a reason an officer can read, challenge and correct, because a regulator will ask. Which branch of AI is the natural fit for that requirement?

- **option1** Natural Language Processing
- **option2** Computer Vision
- **option3** Expert Systems
- **option4** Deep Learning

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
Expert systems answer the question of how a specialist's decision rules can be captured and audited, and loan eligibility checking is the standard example. The firing rule is the reason, so the explanation is complete by construction. Deep learning would very likely score applications more accurately while leaving nobody able to state why any single application was declined.

## Introduction to Artificial Intelligence - MCQ - 1.2.6

**description**
Which pairing of branch and the question it answers is stated incorrectly?

- **option1** Planning: what sequence of actions reaches the goal
- **option2** Knowledge Representation: how can a system extract meaning from raw pixels
- **option3** Machine Learning: how can a system improve at a task from data instead of instructions
- **option4** Robotics: how can a machine sense and act reliably in the physical world

**answer** 2
**difficulty** easy
**bloomTaxonomy** remember
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
Extracting meaning from pixels is computer vision. Knowledge representation asks how facts should be stored so that consequences can be derived from them, the knowledge panel beside a search result being the everyday example. The other three pairings are stated correctly.

## Introduction to Artificial Intelligence - MCQ - 1.2.7

**description**
A science fiction character converses naturally, reasons about physics, runs an engineering analysis, controls hardware, takes initiative without being asked, and moves between all of these without being retrained for each. Which classification fits, and which single property is doing most of the work in that judgment?

- **option1** ANI, because each of those abilities is individually narrow even when many are combined in one character
- **option2** ASI, because performing several expert tasks at once already exceeds what any human can do
- **option3** AGI, because it transfers between domains without task-specific retraining
- **option4** AGI, because it is able to hold a conversation in natural language about any subject that is raised

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
Transfer between domains without retraining is what separates general from narrow, and it is the property that no system today has. The answer resting on conversational ability names the right class for an insufficient reason, since conversational range alone describes today's language models, which are still narrow. A collection of narrow abilities bolted together does not become general.

## Introduction to Artificial Intelligence - MCQ - 1.2.8

**description**
AGI is described as an open problem whose timeline is genuinely disputed. Beyond the engineering difficulty, what makes the dispute unusually hard to settle?

- **option1** The computing power required cannot be estimated in advance, so no forecast of a date can rest on anything firmer than opinion about future hardware
- **option2** The organisations best placed to build it have agreed not to publish their progress
- **option3** Every proposed test has already been passed by an existing system, so the target has ceased to be meaningful
- **option4** There is no agreed definition of AGI, and therefore no agreed test that would settle whether it had arrived

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
Without an agreed definition there is no agreed test, so people arguing about whether AGI is close are often not disagreeing about evidence at all. They are using different definitions and reaching different conclusions from the same facts, which is why the argument does not resolve.

## Introduction to Artificial Intelligence - MCQ - 1.2.9

**description**
An income tax computation module is being written for a payroll product. The slabs are published law and the output must be exactly correct for every employee. Which approach fits, and why?

- **option1** A learned model trained on several years of correctly computed payslips, which would capture the slabs implicitly along with any exceptions that were applied in practice
- **option2** A hybrid, with a learned model computing the tax and a rule layer checking the result falls in a plausible range
- **option3** A learned model, because tax rules change annually and a model retrains more cheaply than rules are rewritten
- **option4** A rule-based system, because the logic is published, known in advance, and must be exactly obeyed

**answer** 4
**difficulty** easy
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
Rules win when the logic is genuinely known and must be exactly obeyed, and tax is the standard case: a model that computed tax approximately right would be worse than useless. A rule-based calculator is provably correct, whereas a learned model is accurate to some percentage on data resembling its training set. Training on past payslips is superficially attractive and would faithfully reproduce past mistakes.

## Introduction to Artificial Intelligence - MCQ - 1.2.10

**description**
A team lists what their learning-based system gives them: it tolerates spelling mistakes, handles photographs, improves as data accumulates, and has surfaced a fraud pattern nobody had noticed. Their manager asks what they are giving up in exchange. Which answer is accurate?

- **option1** Nothing significant, since a learned system can be converted into an equivalent set of rules once training is complete
- **option2** The ability to state a reason for a single decision, and any guarantee that the answer is correct
- **option3** Only speed, since learned systems respond more slowly than rule-based ones at the moment a decision is requested
- **option4** The ability to handle inputs that differ from the training data, which rule-based systems manage comfortably

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
Learned systems are opaque and come with no guarantees: a model can decline an application with nobody able to state a contestable reason, and its accuracy holds only on data resembling what it was trained on. The answer about handling unfamiliar inputs inverts the truth, since tolerating unfamiliar input is a strength of learning and the weakness of rules.

---

# Set 4

## Introduction to Artificial Intelligence - MCQ - 1.2.11

**description**
A hospital deploys a model that flags scans for a radiologist to review first, rather than reporting on them directly. Which objective of AI does this arrangement illustrate most clearly?

- **option1** Augmenting human capability rather than replacing it
- **option2** Improving from experience rather than from rewrites
- **option3** Handling uncertainty and incomplete information
- **option4** Automating tasks that need judgment rather than repetition

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
The most successful deployed systems pair a person with a machine so that each covers the other's weakness, and the radiologist reviewing flagged scans is the standard example. The other three objectives are real and appear elsewhere in this system, but the defining feature of this arrangement is the pairing rather than the replacement.

## Introduction to Artificial Intelligence - MCQ - 1.2.12

**description**
A three-year-old identifies a dog she has never seen, of a breed she has never encountered, from an angle she has never been shown. A calculator multiplies twelve-digit numbers faster than any human. Which capability separates the child's achievement from the calculator's?

- **option1** Generalising from a few examples to an endless variety of new cases
- **option2** Storing a larger quantity of prior examples for comparison
- **option3** Processing the input in a shorter time
- **option4** Applying an explicit rule that distinguishes dogs from other animals with complete reliability across every case presented

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** introduction-to-artificial-intelligence

**explanation**
Generalisation is the capability calculators lack and the thing the field has spent seventy years chasing. Speed and storage are explicitly not on the list of abilities that constitute intelligence. The answer about an explicit rule describes what a rule-based approach would attempt and is precisely what nobody has managed to write down for recognising a dog.

## Introduction to Artificial Intelligence - MCQ - 1.2.13

**description**
Symbolic AI hit a wall that its own successes made worse: as problems grew, the number of possibilities to search grew faster than any hardware could keep pace with. What is that wall called, and what second problem accompanied it?

- **option1** Data drift, accompanied by the difficulty of keeping a large rule base internally consistent as it grew year after year
- **option2** Overfitting, accompanied by a shortage of labelled training examples
- **option3** The knowledge acquisition bottleneck, accompanied by the cost of specialised hardware
- **option4** Combinatorial explosion, accompanied by the discovery that common sense could not be written down

**answer** 4
**difficulty** medium
**bloomTaxonomy** remember
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
Symbolic AI ran into combinatorial explosion and into the realisation that common sense resists being written down as rules. The knowledge acquisition bottleneck is the wall that expert systems hit, which is a related but distinct failure: there the problem was extracting rules from an expert rather than searching a space of possibilities.

## Introduction to Artificial Intelligence - MCQ - 1.2.14

**description**
The statistical turn is described as a shift towards being usefully right instead of provably right. What was given up, and what was gained?

- **option1** Speed was given up, and interpretability was gained
- **option2** Nothing was given up, and the approach was strictly more capable than what preceded it in every respect that mattered to practitioners at the time
- **option3** The need for data was given up, and mathematical rigour was gained
- **option4** Guarantees of correctness were given up, and the ability to work on messy real problems was gained

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** evolution-of-ai-paradigms

**explanation**
Trading provable correctness for useful accuracy is what let AI move from tidy logical problems onto noisy real ones. Statistical methods need more data, not less, which rules out the answer claiming the need for data went away. The answer claiming nothing was given up is the shape of claim this unit repeatedly warns against, since every paradigm shift in the sequence traded one limitation for another.

## Introduction to Artificial Intelligence - MCQ - 1.2.15

**description**
A single left turn by an autonomous vehicle involves reading the scene from cameras, understanding a spoken instruction from the passenger, deciding a sequence of manoeuvres, and controlling the steering. Which set of branches is engaged?

- **option1** Machine Learning, Natural Language Processing, Knowledge Representation, Planning
- **option2** Computer Vision, Knowledge Representation, Expert Systems, Robotics
- **option3** Computer Vision, Natural Language Processing, Planning, Robotics
- **option4** Deep Learning, Computer Vision, Expert Systems, Planning

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
Reading the scene is computer vision, understanding the spoken instruction is natural language processing, deciding the sequence of manoeuvres is planning, and controlling the steering is robotics. Expert systems and knowledge representation are not the branches at work in this description, which is what makes options 2 and 4 wrong despite each containing genuine branches.

## Introduction to Artificial Intelligence - MCQ - 1.2.16

**description**
Why are machine learning and deep learning grouped together as the learning branches, rather than being placed under perception alongside computer vision?

- **option1** Because they were developed in the same decade, while the perception branches are older
- **option2** Because they are defined by how the system acquires its knowledge, not by the kind of input it handles
- **option3** Because they require more computing power than the perception branches, which is the property the grouping tracks
- **option4** Because computer vision and natural language processing do not use learning techniques at all, having remained rule-based disciplines throughout their history

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** branches-of-artificial-intelligence

**explanation**
The branches divide along different axes: learning branches by how knowledge is acquired, perception branches by the kind of raw input to make sense of, reasoning branches by how facts are stored and consequences derived, and robotics by having to act physically. The answer claiming vision and language remained rule-based is factually wrong, since modern computer vision and language processing are built almost entirely on learning.

## Introduction to Artificial Intelligence - MCQ - 1.2.17

**description**
A product manager writes that his recommendation engine "will grow into general intelligence as we add more product categories". Which observation most directly undermines that plan?

- **option1** General intelligence requires consciousness, which no engineering roadmap can deliver
- **option2** Recommendation is a solved problem, so no further capability can be added to such a system
- **option3** Adding categories widens one narrow task and does not produce transfer between domains
- **option4** General intelligence would require the system to be retrained from scratch every time a new product category was introduced into the catalogue

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
More categories make a narrow system wider inside its own band; they do not create the ability to carry capability into an unrelated domain. The answer raising consciousness introduces something, which the definitions in this unit deliberately avoid, since the scale classifies breadth of capability rather than inner experience.

## Introduction to Artificial Intelligence - MCQ - 1.2.18

**description**
ChatGPT is described in this unit as ANI, but unusually broad. Which limitation is offered as evidence that it remains narrow despite that breadth?

- **option1** It cannot perceive the physical world or learn permanently from a conversation
- **option2** It cannot be used without an internet connection
- **option3** It performs worse than a specialised model on any individual task
- **option4** It handles only text, whereas general intelligence would by definition require the ability to process images and audio in the same system

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** types-of-artificial-intelligence

**explanation**
The stated limitations are the inability to perceive the world, the inability to learn permanently from a conversation, and the inability to reliably know when it is wrong. The text-only answer is outdated rather than principled, since multimodal systems handle images and audio and remain narrow. Connectivity is an engineering detail, not a statement about capability.

## Introduction to Artificial Intelligence - MCQ - 1.2.19

**description**
A rule in a college chatbot fires whenever a message contains both "hostel" and "leave". A student types "the hostel warden is on leave, who signs my form". The bot returns the hostel leave application form. What does this illustrate about rule-based systems?

- **option1** That two rules fired at once and the system resolved the conflict incorrectly
- **option2** That the rule base needs to be retrained on more recent messages
- **option3** That rules match patterns without knowing what they mean
- **option4** That the student's phrasing was ambiguous in a way that no system, rule-based or learned, could have been expected to resolve correctly

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
The rule fires on the presence of two strings and has no representation of what the sentence is about, so a completely different request triggers it. The answer calling the phrasing unresolvable is worth rejecting explicitly: a learned system places the sentence near similar sentences and would likely have distinguished a warden's absence from a leave application. Rule bases are written, not trained, which disposes of the answer about retraining.

## Introduction to Artificial Intelligence - MCQ - 1.2.20

**description**
A bank scores each transaction for suspicion with a learned model, then applies a hard rule that blocks any transaction above a set limit from a new device. Why is the second stage a rule rather than part of the model?

- **option1** Because rules execute faster than models, and fraud decisions are latency-sensitive
- **option2** Because the model would otherwise need to be retrained each time the limit changed
- **option3** Because the block must be a guarantee rather than a probability
- **option4** Because regulators require that no machine learning be involved anywhere in a decision to block a customer's transaction

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** symbolic-ai-vs-learning-based-ai

**explanation**
Learn the perception, enforce the policy. Scoring suspicion is a judgment under uncertainty and suits a model; the block is a commitment the bank must be able to guarantee, so it belongs in a rule. The answer about regulators forbidding machine learning overstates the rules, since the learned scoring stage is itself part of the decision and is permitted.

---

# Set 5

## Introduction to Artificial Intelligence - MCQ - 1.2.21

**description**
A distributor asks for a system that decides how one van should cover thirty shops in a day. Which job is this, and which job would it become if the request changed to forecasting how many cartons each shop will order?

- **option1** Personalisation, becoming optimisation
- **option2** Optimisation, becoming prediction
- **option3** Optimisation, becoming perception
- **option4** Prediction, becoming optimisation

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** foundations-of-artificial-intelligence
**subTopics** ai-applications

**explanation**
Optimisation asks which arrangement or route is best, which is the van covering thirty shops. Prediction asks what is likely to happen next, which is the forecast of cartons. The answer beginning with prediction reverses the two, and separating them matters because they need different data and are evaluated in completely different ways.

## Introduction to Artificial Intelligence - MCQ - 1.2.22

**description**
Two hospitals deploy the same diagnostic model. One sees steady performance for years; the other sees quality drift downward after eighteen months, with no change to the software. Which explanation fits the pattern best?

- **option1** Models degrade with age, since the mathematics inside them loses precision over repeated use
- **option2** The second hospital had fewer patients, so the model had less data to learn from after deployment
- **option3** The second hospital's deployment environment stopped resembling the training environment, and nobody was checking
- **option4** The first hospital retrained the model continuously while the second hospital left the original version in place without applying any of the vendor's periodic updates

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** ai-applications

**explanation**
One of the four conditions for a deployment that works is that the environment continues to resemble the training environment, and that somebody keeps checking that it does. Patient mix, equipment, and referral patterns all shift. The answer about mathematics losing precision invents a mechanism that does not exist, since unchanged software does not lose precision by sitting still.

## Introduction to Artificial Intelligence - MCQ - 1.2.23

**description**
A team wants to predict which patients need extra care and has no direct measure of health need, so it uses past healthcare spending as a stand-in. Which source of bias does this choice risk introducing, and why?

- **option1** Historical bias, because past spending records decisions made by clinicians in the past
- **option2** Deployment bias, because the tool will be used on a population it was not designed for
- **option3** Measurement bias, because spending measures access to healthcare rather than need for it
- **option4** Representation bias, because patients who never sought care are absent from the dataset

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
Measurement bias comes from proxies: you rarely have the thing you care about, so you use a stand-in, and the stand-in measures something subtly different. Spending tracks who could reach and afford care. The representation-bias answer is the closest competitor and describes a real adjacent problem, but the defining fault here is the substitution itself rather than who is missing from the file.

## Introduction to Artificial Intelligence - MCQ - 1.2.24

**description**
A regulator requires that a lending model be "fair". The team finds it can equalise selection rates across groups, or equalise error rates, or keep scores calibrated so a 0.8 means the same thing for everyone, but not all three at once. What should the team conclude?

- **option1** When base rates genuinely differ between groups, these definitions are mathematically incompatible, so somebody must choose and record which one applies
- **option2** The three definitions are equivalent, and the discrepancy indicates a bug in how the team is computing at least one of them
- **option3** Fairness cannot be measured, so the requirement should be treated as aspirational
- **option4** The model has a defect that a better training procedure will remove

**answer** 1
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
This is a property of the arithmetic, not an engineering shortfall, so no better algorithm resolves it. The practical consequence is sharp: "make the model fair" is not a specification. Somebody accountable for the domain must decide which notion this application demands, state it explicitly, accept that another reasonable person could choose differently, and write the decision down.

## Introduction to Artificial Intelligence - MCQ - 1.2.25

**description**
A bank adds a human reviewer to approve or reject every automated credit decision. The reviewer handles roughly two hundred cases an hour, sees no explanation alongside any recommendation, and is measured on throughput. Approvals of the model's recommendation run above 99 percent. What is the most accurate assessment?

- **option1** Oversight is working, since a person signs off on every decision before it takes effect
- **option2** Oversight exists on paper only, because the reviewer lacks the information and time to disagree
- **option3** Oversight is unnecessary here, because the agreement rate shows the model is performing well enough to run unsupervised
- **option4** Oversight is failing because the reviewer has not been trained in the statistical methods used to build the model and therefore cannot evaluate its outputs properly

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
Putting a human in the loop only helps if that person has the information, the time, and the authority to disagree, and none of the three is present. The tendency to defer to an automated recommendation is called automation bias and is well documented. The answer calling oversight unnecessary misreads the agreement rate, which measures deference rather than correctness.

## Introduction to Artificial Intelligence - MCQ - 1.2.26

**description**
An applicant rejected by an automated screening system asks what disqualified him. The team can describe which factors carry the most weight across all applicants but cannot say why his particular application scored as it did. Which distinction does this illustrate?

- **option1** They can supply a global explanation but not a local one
- **option2** They can supply a local explanation but not a global one
- **option3** They have confused explainability with accountability, which are governed by separate requirements
- **option4** They have produced an explanation that is accurate in aggregate and therefore satisfies the applicant's request

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
A global explanation says what the model does in general; a local explanation says why this one decision came out as it did. The local one is what the applicant needs and is usually the harder of the two to produce. Without it there is no contestability, since a decision you cannot see is a decision you cannot appeal.

## Introduction to Artificial Intelligence - MCQ - 1.2.27

**description**
A college anonymises an attendance dataset by removing names and roll numbers before sharing it with a research group. The remaining columns include postcode, date of birth, and gender. Why is this weaker protection than it appears?

- **option1** Because a small number of ordinary attributes are often enough to identify an individual uniquely
- **option2** Because the college failed to obtain consent, which no amount of anonymisation can substitute for
- **option3** Because anonymised data loses so much detail that the research conclusions will be unreliable
- **option4** Because large models trained on the data may reproduce fragments of it later

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
Re-identification defeats naive anonymisation, and postcode with date of birth and gender is the classic combination that singles people out. Options 2 and 4 name genuine privacy issues from this unit, consent and memorisation, but neither is what makes this particular release unsafe. Privacy is a design-time decision and is close to impossible to retrofit.

## Introduction to Artificial Intelligence - MCQ - 1.2.28

**description**
Public debate about self-driving cars concentrates on whom a vehicle should choose to hit when a collision is unavoidable. This unit argues that focus is misplaced. What is the argument?

- **option1** That the dilemma has been solved, and manufacturers already publish the rule their vehicles follow
- **option2** That the vivid dilemma is rare, while duller questions such as how much testing is enough before public deployment arise constantly and matter more
- **option3** That the dilemma is a matter for philosophers rather than engineers, so it falls outside the scope of a technical curriculum
- **option4** That such collisions are already prevented by existing sensor technology, making the question purely theoretical

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** responsible-ai

**explanation**
The ethical questions that actually arise are duller and far more consequential than the trolley-style dilemma, which is vivid and rare. How much testing is enough before deployment on public roads is one of them. The argument is about frequency and consequence, not about whether ethics belongs to engineers.

## Introduction to Artificial Intelligence - MCQ - 1.2.29

**description**
Foundation models are described as changing what is expensive and what is cheap in building an intelligent system. What became cheap, and which open problem does the shift create?

- **option1** Adapting one model to many tasks became cheap, and capability concentrated in a few organisations
- **option2** Running models on small devices became cheap, and accuracy on rare cases suffered
- **option3** Labelling data became cheap, and the resulting labels became less reliable
- **option4** Training a model from scratch became cheap, and the number of competing systems grew faster than any evaluation process could keep pace with

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** foundations-of-artificial-intelligence
**subTopics** future-of-ai

**explanation**
The shift is from one model per task to building once and adapting many times, which makes adaptation cheap and the initial build extremely expensive. That expense is exactly why capability concentrates in a small number of organisations, which is the direction's main open problem. The answer about cheap from-scratch training inverts the economics.

## Introduction to Artificial Intelligence - MCQ - 1.2.30

**description**
A vendor claims its system "will replace your entire customer support department". Applying the three questions this unit recommends for evaluating such predictions, which line of enquiry is most likely to expose an overstatement?

- **option1** Asking which competing vendors were evaluated before this one was selected
- **option2** Asking how many customers the vendor already has in this industry and whether any of them will speak about their experience with the deployment
- **option3** Asking whether the underlying model is a foundation model or trained specifically for support
- **option4** Asking whether a task or a whole job is being automated, and what else must be true for the claim to hold

**answer** 4
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** foundations-of-artificial-intelligence
**subTopics** future-of-ai

**explanation**
The three questions are what exactly is being automated, a task or a job; what has to be true besides the model; and who is making the claim and what they gain if you believe it. A support role is a bundle of tasks, and automating the most common query is not the same as replacing the department. Asking for reference customers is sensible procurement practice and does not test the claim's structure.

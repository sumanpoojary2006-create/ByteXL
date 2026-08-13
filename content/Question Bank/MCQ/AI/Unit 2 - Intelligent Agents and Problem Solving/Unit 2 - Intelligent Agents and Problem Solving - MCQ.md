# Unit 2 - Intelligent Agents and Problem Solving - MCQ

**Course:** Introduction to Artificial Intelligence
**Title pattern:** `Introduction to Artificial Intelligence - MCQ - U.S.Q`
**Set 1 (questions 1 to 20) is the upload set.** It covers all 11 subtopics of this unit.
**Set 2 (questions 21 to 50) is the reserve bank.**

## Subtopic coverage in the upload set

| Subtopic | Covered by |
| --- | --- |
| `intelligent-agents` | 2.1.1, 2.1.12 |
| `agent-architectures` | 2.1.2, 2.1.13 |
| `peas-framework` | 2.1.3, 2.1.20 |
| `ai-environments` | 2.1.4, 2.1.14 |
| `problem-formulation` | 2.1.5 |
| `state-space-representation` | 2.1.6, 2.1.15 |
| `blind-search-algorithms` | 2.1.7, 2.1.16 |
| `heuristic-search-algorithms` | 2.1.8, 2.1.17 |
| `local-search` | 2.1.9, 2.1.18 |
| `adversarial-search` | 2.1.10, 2.1.19 |
| `constraint-satisfaction-problems` | 2.1.11 |

---

# Set 1

## Introduction to Artificial Intelligence - MCQ - 2.1.1

**description**
A robot vacuum bumps into a chair leg it could not see, reverses, and turns. Its owner complains that a smarter machine would have avoided the chair in the first place. Is reversing after the bump a rational action?

- **option1** Yes, but only because the collision caused no damage on this occasion
- **option2** No, because a rational agent by definition avoids collisions altogether
- **option3** No, because the vacuum should have retained a map of the room from previous cleaning runs before it was permitted to move at all
- **option4** Yes, because rationality is judged by the action expected to do best on the evidence available, not by hindsight

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** intelligent-agents

**explanation**
Rationality is not omniscience and it is not perfection. It is choosing the action expected to maximise the performance measure given the percepts so far, and this vacuum had no sensor that could see the chair before touching it. Judging the action by what a better-equipped machine would have done confuses the quality of the agent's sensors with the rationality of its decision.

## Introduction to Artificial Intelligence - MCQ - 2.1.2

**description**
A delivery agent follows condition-action rules such as "stop at red" and "turn right if the road ahead is blocked". It begins circling, repeatedly passing the same junctions, because nothing tells it where it is trying to get to. Which architecture would resolve this, and why?

- **option1** A model-based reflex agent, since remembering junctions already passed is what breaks the loop
- **option2** A learning agent, since the behaviour will correct itself once enough journeys have been recorded and the poorly performing routes have been dropped
- **option3** A utility-based agent, since the agent needs to weigh speed against safety before choosing a road
- **option4** A goal-based agent, since the missing element is an explicit destination to reason towards

**answer** 4
**difficulty** easy
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** agent-architectures

**explanation**
What defeats a model-based reflex agent is having no destination to aim at, which is exactly the symptom here. A goal-based agent holds an explicit goal and reasons about the future to reach it. Memory alone would stop the agent revisiting junctions without giving it anywhere to go, and utility only becomes relevant once several routes all reach the goal but are not equally good.

## Introduction to Artificial Intelligence - MCQ - 2.1.3

**description**
A team specifying an agricultural spraying drone writes its performance measure as "the drone flies smoothly and follows its waypoints accurately". A reviewer objects that this is the wrong kind of statement. What is the objection?

- **option1** The measure is too easy to achieve and should include a difficulty target
- **option2** The measure belongs under Actuators, since flying and following waypoints are things the drone does
- **option3** The measure describes the agent's behaviour rather than a state of the world such as area treated and zero drift onto neighbouring plots
- **option4** The measure omits the sensors the drone will need in order to know whether it has followed its waypoints accurately in the first place

**answer** 3
**difficulty** easy
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** peas-framework

**explanation**
A performance measure must be stated as a property of the world, not of the agent's behaviour, because otherwise an agent can score well while failing at the actual job. A drone that flies beautifully and sprays the wrong field satisfies the written measure. Stating success as infested area treated, chemical per hectare, and zero drift makes the real objective checkable.

## Introduction to Artificial Intelligence - MCQ - 2.1.4

**description**
Two students describe the same self-driving environment. One says it is partially observable because the car cannot see around a parked lorry. The other says that makes it stochastic. Who is right?

- **option1** Both, since anything hidden from the agent produces randomness in the outcome of its actions
- **option2** The second, since an agent that cannot see everything cannot predict anything
- **option3** Neither, since driving is fully observable once the car's sensor suite includes lidar and radar in addition to its cameras
- **option4** The first only, since partial observability concerns what the agent can perceive while stochasticity concerns whether its actions have predictable effects

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** ai-environments

**explanation**
These are separate properties and conflating them is the standard error. Partial observability is about how much of the environment the agent can perceive. Stochasticity is about whether the same action in the same state reliably produces the same result. Driving happens to be both, but the hidden lorry establishes only the first.

## Introduction to Artificial Intelligence - MCQ - 2.1.5

**description**
An engineer formulating a route problem for an inspection vehicle lists the initial state as the depot, the actions as the roads available, the transition model, and the goal test. She sets the path cost to the number of roads taken. The real objective is to finish the round before the depot closes. What is wrong?

- **option1** The goal test should list every acceptable end state rather than describing a property
- **option2** The path cost measures steps when the thing that matters is time
- **option3** The actions should be listed globally instead of per state
- **option4** The initial state is incomplete, because a vehicle leaving a depot has already consumed some portion of the working day before the first road is chosen

**answer** 2
**difficulty** easy
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** problem-formulation

**explanation**
Choosing steps when the thing that matters is time or money is the commonest mistake in setting path cost, and it produces solutions that are short in road count while arriving too late. The other components are stated correctly here: goals may be described by a property, and actions are properly given per state rather than globally.

## Introduction to Artificial Intelligence - MCQ - 2.1.6

**description**
The 8-puzzle has 362,880 possible arrangements of eight tiles and a blank, yet the state space reachable from any particular starting arrangement contains 181,440. What does this tell a student about to write a solver?

- **option1** That the puzzle has two separate reachable regions, so a goal may be unreachable from a given start and this is worth checking before searching
- **option2** That the solver should generate all 362,880 arrangements in advance to guarantee completeness
- **option3** That half the arrangements are illegal configurations which violate the rules of the puzzle
- **option4** That the search will take roughly half as long as a naive estimate would suggest, which is a useful saving but changes nothing about how the solver should be written

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** state-space-representation

**explanation**
Only half the arrangements are reachable from any given start, which means the space splits into two regions with no moves between them. Every arrangement is a legal configuration; the point is that sliding moves cannot carry you between the halves. Asking whether the goal is reachable at all, before searching for it, saves an exhaustive search that was doomed from the first step.

## Introduction to Artificial Intelligence - MCQ - 2.1.7

**description**
A search must return a route with the fewest possible stops, and memory on the device is tight. A colleague suggests depth-first search because it uses far less memory than breadth-first search. What is the flaw in that suggestion?

- **option1** Depth-first search gives no guarantee of the shortest path, which is the stated requirement
- **option2** Depth-first search uses more memory than breadth-first search once the branching factor exceeds two
- **option3** Depth-first search cannot be implemented with a stack on a memory-constrained device
- **option4** Depth-first search will always fail to terminate, because there is no mechanism preventing it from following a branch forever

**answer** 1
**difficulty** easy
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** blind-search-algorithms

**explanation**
The memory claim is true and the recommendation is still wrong, because the requirement is fewest stops and only breadth-first search guarantees that. Depth-first search finds some path if the branch is finite and offers no guarantee it is the shortest. Saying it always fails to terminate overstates the case, since the danger is an endless branch rather than a certainty.

## Introduction to Artificial Intelligence - MCQ - 2.1.8

**description**
On a map with a river, Lake View sits 1.41 km from the hospital in a straight line, but the only road between them runs 20 km around the water. A greedy best-first search using straight-line distance heads confidently for Lake View. What does this expose?

- **option1** That the heuristic is inadmissible, because 1.41 km exceeds the true cost of reaching the goal
- **option2** That greedy search does not account for how far it has already travelled, so a state that looks close can be reached only at great cost
- **option3** That the map has been drawn to an inconsistent scale, which is a data problem rather than a limitation of the search algorithm being used
- **option4** That straight-line distance is unsuitable for road networks and should be replaced by an estimate that ignores geometry

**answer** 2
**difficulty** easy
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** heuristic-search-algorithms

**explanation**
Greedy best-first search orders the frontier by the estimate of what remains and ignores the cost already incurred, so it walks towards whatever looks nearest even when getting there is expensive. Straight-line distance never overestimates the true road distance, so it remains admissible; the fault is in how greedy search uses it, which is precisely what adding the cost so far fixes in A star.

## Introduction to Artificial Intelligence - MCQ - 2.1.9

**description**
Hill climbing on a delivery round reaches 42.1 km and stops after three steps, unable to improve. Random restarts reach 35.4 km, found by 29 of 50 runs. What does the second result reveal about the landscape?

- **option1** That 35.4 km is provably the shortest round, since a majority of independent runs converged on it
- **option2** That hill climbing was implemented incorrectly, since a correct implementation would have reached 35.4 km as well
- **option3** That better solutions exist beyond a local optimum, and the good peak has a basin large enough to be hit from many random starting points
- **option4** That the landscape contains exactly two peaks, one at 42.1 km and one at 35.4 km

**answer** 3
**difficulty** easy
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** local-search

**explanation**
Hill climbing never accepts a worse state, so it halts at the first optimum it reaches, which here was local rather than global. Restarts succeeding in 29 of 50 runs indicates the better peak has a large basin of attraction. Majority agreement is evidence, not proof, so nothing here establishes that 35.4 km is optimal, and nothing fixes the number of peaks at two.

## Introduction to Artificial Intelligence - MCQ - 2.1.10

**description**
A student evaluating a move in a two-player game picks the line that leads to the highest score if the opponent blunders. Her opponent does not blunder and she loses. Which principle did she violate?

- **option1** Alpha-beta pruning would have removed the losing line from consideration before it was ever evaluated
- **option2** A depth limit should have been applied so the search stopped before reaching that position
- **option3** Minimax judges a move by its worst outcome under the opponent's best reply, not by its best outcome under a convenient reply
- **option4** The evaluation function she used must have been inaccurate, since an accurate one would have scored the blunder line lower than the alternative she rejected

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** adversarial-search

**explanation**
Adversarial search assumes the opponent plays their best reply, so every plan is evaluated against the strongest response rather than a convenient one. Alpha-beta prunes branches that cannot change the result and would not have rescued a policy of hoping for blunders, because it returns exactly the same answer as full minimax, only faster.

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 2.1.11

**description**
A Sudoku solver that always fills the next empty cell in reading order makes 4,208 placements. Switching to choosing the variable with the fewest remaining legal values brings that down to 51, with no backtracking at all. What is the reasoning behind the improvement?

- **option1** Cells with few options are usually near the centre of the grid, where constraints are densest
- **option2** A variable with few remaining options is where a wrong assignment will be discovered soonest, so failures surface before work is wasted
- **option3** Filling constrained cells first reduces the total number of variables that need to be assigned
- **option4** Reading order is arbitrary, and any alternative ordering would produce a comparable reduction in the number of placements attempted

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** constraint-satisfaction-problems

**explanation**
Minimum remaining values picks the variable most likely to fail, so a doomed branch is abandoned after a few placements instead of after hundreds. The number of variables is fixed by the puzzle and no ordering changes it. Not every alternative ordering helps, which is why the specific heuristic matters rather than merely departing from reading order.

## Introduction to Artificial Intelligence - MCQ - 2.1.12

**description**
Match the terms to a vacuum that retains nothing between instants. Its rule set is "if bumped, reverse and turn; if dirt, suck; else move forward". Which statement is correct?

- **option1** The rule set is the agent program, and the code implementing it is the agent function
- **option2** The rule set is the agent function, and its percept sequence has length one because nothing is retained
- **option3** The percept sequence is everything the vacuum could in principle perceive, whether or not it has done so
- **option4** The performance measure is a full dust bin, since that is the observable evidence that the machine has been working

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** intelligent-agents

**explanation**
The agent function is the mapping from percept sequences to actions, and the agent program is the code implementing it, so the answer swapping agent program and agent function has them the wrong way round. A percept sequence is everything perceived so far, which for a memoryless vacuum is a single percept. The performance measure is a clean floor, stated as a property of the world, not a full bin.

## Introduction to Artificial Intelligence - MCQ - 2.1.13

**description**
A routing agent already reaches its destination reliably. In heavy rain, management wants it to prefer slower but safer roads, accepting a later arrival. Which architecture does this require, and what makes it hard in practice?

- **option1** A model-based reflex agent, and the difficulty is retaining enough internal state
- **option2** A goal-based agent, and the difficulty is that the destination changes with the weather
- **option3** A learning agent, and the difficulty is obtaining feedback on routes the agent never chose
- **option4** A utility-based agent, and the difficulty is writing a scoring function that honestly trades safety against speed

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** agent-architectures

**explanation**
Two routes that both reach the goal but are not equally good is exactly what defeats a goal-based agent, and it is the situation described. A utility function scores outcomes so competing objectives can be traded off. What defeats a utility-based agent is a scoring function nobody can write honestly, which is the real difficulty when the currencies are minutes and risk of harm.

## Introduction to Artificial Intelligence - MCQ - 2.1.14

**description**
An agent is being designed for an environment that is dynamic with hard real-time deadlines. Which design consequence follows most directly?

- **option1** The agent cannot deliberate without bound, since the world changes while it is thinking
- **option2** The agent cannot be stateless, since it must remember what it has already observed
- **option3** The agent cannot rely on a fixed plan, since its actions may not produce the effects it expects
- **option4** The agent cannot use a discrete representation, since a dynamic environment must be modelled with continuous values throughout

**answer** 1
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** ai-environments

**explanation**
Each structural property rules out a class of technique. Dynamic rules out unbounded deliberation, because an answer that arrives too late is no answer. Being stateless is ruled out by partial observability, and fixed plans are ruled out by stochasticity. Discreteness is a separate axis and a dynamic environment can still be discrete.

## Introduction to Artificial Intelligence - MCQ - 2.1.15

**description**
A student encodes an inspection round so that a state records only the site the vehicle currently occupies. The vehicle must visit every site once. Why will this encoding fail?

- **option1** Because operators cannot be defined without knowing the cost of each road segment in advance
- **option2** Because the state space becomes infinite when the current site is the only variable recorded
- **option3** Because a state must always record the full history of actions taken, including the order in which the earlier sites were reached
- **option4** Because the state must include the set of sites already visited, or the goal test cannot be evaluated

**answer** 4
**difficulty** medium
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** state-space-representation

**explanation**
A state must include everything that affects the future and exclude everything that does not. Whether the round is finished depends on which sites remain, so the visited set belongs in the state. The answer demanding the full history of actions overshoots in the other direction: the order in which earlier sites were reached does not change what remains to be done, so recording it inflates the space for nothing.

## Introduction to Artificial Intelligence - MCQ - 2.1.16

**description**
A logistics team needs the cheapest route, where road segments carry different tolls. Which algorithm fits, and what condition must hold for its guarantee to apply?

- **option1** Breadth-first search, provided every toll is identical
- **option2** Uniform cost search, provided no connection has a negative cost
- **option3** Depth-first search, provided the graph contains no cycles
- **option4** Uniform cost search, provided the number of road segments on any route between two points does not exceed the number of towns in the network

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** blind-search-algorithms

**explanation**
Uniform cost search orders the frontier by cost so far and returns the lowest total cost, and its guarantee holds only when no connection has a negative cost. Breadth-first search would work if every toll were identical, since fewest steps and cheapest coincide in that case, but the premise says tolls differ. The condition about road segments and town counts is invented.

## Introduction to Artificial Intelligence - MCQ - 2.1.17

**description**
On one map, uniform cost search returns a 15 km route after expanding six towns. Greedy best-first returns 35 km after expanding three. A star returns 15 km after expanding three. What does this comparison demonstrate?

- **option1** That A star keeps the optimality of uniform cost search while inheriting the focus of greedy search
- **option2** That greedy search is the correct choice whenever expanding fewer nodes matters more than route length
- **option3** That A star is faster than uniform cost search because it expands fewer nodes, at the price of occasionally returning a longer route
- **option4** That uniform cost search is obsolete, since A star matches its route and beats its node count on every map that has been tested

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** heuristic-search-algorithms

**explanation**
A star orders the frontier by cost so far plus estimated cost remaining, which is why it matches uniform cost search on route length while expanding as few towns as greedy search. Its optimality holds provided the heuristic is admissible. The answer describing A star as faster but occasionally longer names a trade A star does not make here, since it returned the same 15 km route.

## Introduction to Artificial Intelligence - MCQ - 2.1.18

**description**
Simulated annealing reaches the same 35.4 km round as random restarts, but only after accepting 220 moves that made the round worse. Why is accepting worse moves the mechanism rather than a defect?

- **option1** Because accepting worse moves lets the search leave a local optimum, and the probability of doing so falls as the run proceeds
- **option2** Because a worse move is often mislabelled, and re-evaluating it later usually reveals it was an improvement
- **option3** Because the algorithm has no way to compare two states, so it accepts moves at random throughout the run
- **option4** Because accepting worse moves increases the number of states examined, and examining more states is what eventually uncovers the shortest available round

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** local-search

**explanation**
Hill climbing fails on local optima precisely because it never accepts a worse state. Simulated annealing accepts them with a probability that falls over time, so it can escape early and settle later. What defeats it is a badly chosen cooling schedule. It compares states perfectly well, and sheer volume of states examined is not the mechanism.

## Introduction to Artificial Intelligence - MCQ - 2.1.19

**description**
A team adds alpha-beta pruning to a game engine and is surprised that the move it plays is identical to before, though it now searches in a fraction of the time. Is something wrong?

- **option1** Yes, since pruning removes branches and must therefore change which move is selected in at least some positions
- **option2** Yes, since an unchanged move indicates the pruning conditions never triggered and no branches were actually skipped
- **option3** No, but only because this particular position was shallow enough for the full tree to be searched within the time available in both configurations
- **option4** No, since pruning costs nothing in accuracy and only skips branches that could not have changed the result

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** adversarial-search

**explanation**
Alpha-beta returns exactly what full minimax returns, skipping only branches that cannot affect the outcome, so an identical move with a shorter search is the expected result rather than a symptom. How much it saves depends on move ordering. What does change the answer is imposing a depth limit and estimating non-final positions.

## Introduction to Artificial Intelligence - MCQ - 2.1.20

**description**
A warehouse robot is specified with cameras, floor markers, proximity sensors and a weight sensor. Its designers later ask it to avoid a category of obstacle that none of those sensors can detect. Which part of the PEAS specification did they violate, and what does that part constrain?

- **option1** Actuators, which set the ceiling on what the agent can ever achieve
- **option2** Environment, which fixes which situations the agent is accountable for
- **option3** Performance measure, which drives every design trade-off
- **option4** Sensors, which set the ceiling on what the agent can ever know

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** peas-framework

**explanation**
Sensors bound what the agent can know, and no amount of reasoning recovers information the hardware never captured. Actuators bound what it can do, which is a different ceiling. Naming the environment matters too, since an obstacle outside the stated environment is arguably out of scope, but the immediate violation is asking for a decision that the sensor suite cannot support.

---

# Set 3

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 2.2.1

**description**
An agent designer argues that gathering more information before acting is a waste of effort, since a rational agent should simply act on what it already has. Where does this reasoning go wrong?

- **option1** It does not go wrong, because rationality is defined purely over the percepts received so far
- **option2** Rationality does depend on gathering information, since an agent that could have looked and did not has not chosen the best available action
- **option3** It goes wrong only for agents operating in fully observable environments, where all information is available without effort
- **option4** It goes wrong because gathering information is always cheaper than acting on an incomplete picture, whatever the domain and whatever the cost of the sensing involved

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** intelligent-agents

**explanation**
Rationality is not omniscience, but information gathering is itself an action available to the agent, so declining to look when looking would help is not rational. The answer claiming sensing is always cheaper states the right conclusion with an indefensible justification, since sensing has a cost and there are situations where acting immediately is correct.

## Introduction to Artificial Intelligence - MCQ - 2.2.2

**description**
Which situation defeats a simple reflex agent specifically, as opposed to the architectures above it?

- **option1** Two routes that both reach the goal but differ in quality
- **option2** A goal that changes partway through a task
- **option3** Two situations that look identical to its sensors but require different actions
- **option4** A performance measure combining several objectives that cannot all be satisfied at once

**answer** 3
**difficulty** medium
**bloomTaxonomy** remember
**topics** intelligent-agents-and-problem-solving
**subTopics** agent-architectures

**explanation**
A simple reflex agent maps the current percept straight to an action, so two situations that produce the same percept must produce the same action even when they should not. Adding internal state fixes this. Competing objectives defeat goal-based agents and push you towards utility, and a changing goal is a problem for architectures that have no explicit goal at all.

## Introduction to Artificial Intelligence - MCQ - 2.2.3

**description**
When specifying an agent, why is Environment worth writing down explicitly, given that everyone involved already knows roughly what the agent will encounter?

- **option1** Because it fixes the boundary of the problem and therefore which situations the agent is accountable for
- **option2** Because the environment must be simulated before the agent can be tested
- **option3** Because it determines which sensors will be affordable within the project budget
- **option4** Because regulators require a written statement of the operating environment before any autonomous system may be deployed in a public setting

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** peas-framework

**explanation**
Stating the environment fixes what is in scope and what is out of it, which settles later arguments about whether a failure was a bug or a situation the agent was never built for. Simulation and procurement are downstream activities that benefit from the statement without being the reason for it.

## Introduction to Artificial Intelligence - MCQ - 2.2.4

**description**
Classify chess along the four properties used in this unit.

- **option1** Fully observable, deterministic, static or semi-dynamic with a clock, discrete
- **option2** Partially observable, deterministic, static, discrete
- **option3** Fully observable, stochastic, dynamic, discrete
- **option4** Fully observable, deterministic, dynamic, continuous in time though discrete in the positions the pieces may occupy

**answer** 1
**difficulty** medium
**bloomTaxonomy** remember
**topics** intelligent-agents-and-problem-solving
**subTopics** ai-environments

**explanation**
Both players see the whole board, moves have exactly the effect the rules state, the position does not change while a player thinks except through the clock, and states, time and actions are all discrete. Contrast driving, which is partially observable, stochastic, dynamic with hard deadlines, and continuous in position and speed.

## Introduction to Artificial Intelligence - MCQ - 2.2.5

**description**
An abstraction drops the detail of which lane a vehicle occupies from a route-planning problem. What test decides whether that abstraction is valid?

- **option1** Whether the detail was recorded accurately in the source data
- **option2** Whether the abstract problem has fewer states than the original
- **option3** Whether every solution in the abstract problem corresponds to a solution that can actually be carried out in the real world
- **option4** Whether removing the detail leaves the transition model unchanged for every action available anywhere in the state space

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** problem-formulation

**explanation**
An abstraction is valid when every abstract solution can be executed for real. Fewer states is the motive for abstracting, not the test of correctness. Demanding an unchanged transition model sets a bar so high that no useful abstraction would pass, since dropping detail almost always changes the transition model somewhere.

## Introduction to Artificial Intelligence - MCQ - 2.2.6

**description**
What distinguishes a node from a state in a search?

- **option1** A state is a complete description of a situation, while a node is a search record holding a state plus its parent, action and cost
- **option2** A node is a complete description of a situation, while a state additionally records the path taken to reach it
- **option3** They are the same thing, described differently depending on whether the graph or the algorithm is being discussed
- **option4** A node exists only in the frontier, whereas a state exists only once it has been expanded and removed from consideration

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** state-space-representation

**explanation**
The state is the situation itself; the node is the bookkeeping the search wraps around it so a path can be reconstructed. Two different nodes can hold the same state if the search reached it by different routes, which is exactly why the distinction is worth keeping.

## Introduction to Artificial Intelligence - MCQ - 2.2.7

**description**
Which pairing of algorithm and frontier structure is correct?

- **option1** BFS uses a stack, DFS uses a queue, UCS uses a priority queue ordered by cost
- **option2** BFS uses a queue, DFS uses a stack, UCS uses a priority queue ordered by cost
- **option3** All three use a priority queue, differing only in the key used to order it
- **option4** BFS uses a queue, DFS uses a priority queue ordered by depth, UCS uses a stack ordered by insertion time

**answer** 2
**difficulty** easy
**bloomTaxonomy** remember
**topics** intelligent-agents-and-problem-solving
**subTopics** blind-search-algorithms

**explanation**
A queue expands the oldest discovery, which is the shallowest, giving breadth-first behaviour. A stack expands the newest, which is the deepest. Uniform cost search needs the cheapest partial route, which is a priority queue keyed on cost so far.

## Introduction to Artificial Intelligence - MCQ - 2.2.8

**description**
A heuristic used with A star sometimes overestimates the remaining distance to the goal. What is the consequence?

- **option1** The search may return a route that is not the cheapest, because the optimality guarantee requires an admissible heuristic
- **option2** The search will fail to terminate, since the estimate never converges on the true remaining cost
- **option3** The search behaves identically to uniform cost search, since overestimates cancel out across the frontier
- **option4** The search becomes slower but remains optimal, since A star corrects any overestimate once the goal has been reached and the true cost is known

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** heuristic-search-algorithms

**explanation**
A star returns the cheapest route provided the heuristic never overestimates, which is what admissible means. An overestimate can make the search discard a route that was in fact cheaper, so optimality is lost. Termination is unaffected, and there is no mechanism by which reaching the goal repairs a decision already taken.

## Introduction to Artificial Intelligence - MCQ - 2.2.9

**description**
Why are local search methods suitable for problems such as arranging a delivery round, even though they discard the path taken?

- **option1** Because path information is unnecessary in any problem where the cost of each individual step happens to be identical to the cost of every other step
- **option2** Because the state space is small enough to be searched exhaustively once the path is discarded
- **option3** Because discarding the path guarantees that the algorithm cannot revisit a state it has already examined
- **option4** Because the solution is the final configuration itself rather than the sequence of steps that produced it

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** local-search

**explanation**
What the planner wants is the round itself, not a record of how the algorithm arrived at it, which is what makes discarding the path harmless. Local search is used precisely when the space is far too large to search exhaustively, and discarding the path offers no protection against revisiting states.

## Introduction to Artificial Intelligence - MCQ - 2.2.10

**description**
Full minimax is described as impossible for any interesting game. What is the standard response, and what does it cost?

- **option1** Prune with alpha-beta, at the cost of occasionally selecting a weaker move
- **option2** Randomise the order in which moves are examined, at the cost of the engine producing a different move each time it is asked about the same position
- **option3** Search only the moves a human would consider, at the cost of needing an expert to enumerate them
- **option4** Stop at a depth limit and estimate the value of non-final positions, at the cost that the answer is only as good as the estimate

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** adversarial-search

**explanation**
A depth limit plus an evaluation function is what makes game engines practical, and the whole quality of play then rests on how good that estimate is. Alpha-beta also helps and costs nothing in accuracy, which is why it is not the answer to a question asking what the compromise costs.

---

# Set 4

## Introduction to Artificial Intelligence - MCQ - 2.2.11

**description**
A performance measure for a robot vacuum is written as "maximise the weight of dust collected". What behaviour does this invite?

- **option1** The vacuum will clean quickly in order to reach as many rooms as possible within its battery life
- **option2** The vacuum will avoid rooms that appear clean, since they contribute little to the measure
- **option3** The vacuum may deposit dust and collect it again, since the measure rewards collection rather than a clean floor
- **option4** The vacuum will prioritise carpets over hard floors, since carpets hold more dust per square metre than any other surface it encounters

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** intelligent-agents

**explanation**
This is why the measure must be stated as the state of the world you want, a clean floor, rather than as a proxy that is easy to count. Rewarding collection makes recollecting dust a winning strategy. The other behaviours are plausible side effects of various measures but none of them exploits the stated one directly.

## Introduction to Artificial Intelligence - MCQ - 2.2.12

**description**
Which principle should govern the choice of agent architecture?

- **option1** Choose the most capable architecture the project can afford, since capability is never wasted
- **option2** Choose the architecture matching the environment's observability, since that property determines the internal state the agent will need to retain
- **option3** Choose the simplest architecture that produces the required behaviour
- **option4** Choose a learning agent wherever data is available, since learned behaviour outperforms designed behaviour

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** agent-architectures

**explanation**
The useful diagnostic questions are whether the correct action depends on history, whether it depends on a goal that changes, and whether there are competing objectives or uncertain outcomes. Each answered yes moves you one step up. Observability matters and is not the whole test, and reaching for the most capable architecture buys complexity you then have to justify.

## Introduction to Artificial Intelligence - MCQ - 2.2.13

**description**
Two teams specify the same self-driving car. One lists lidar under Sensors; the other lists it under Actuators, reasoning that lidar emits a laser and therefore acts on the world. Who is right, and on what basis?

- **option1** The first, since the classification follows what the component is for, and lidar exists to let the agent know rather than to change the world
- **option2** The second, since anything that emits energy into the environment is by definition an actuator
- **option3** Both, since a component that emits and receives should be listed under each heading
- **option4** Neither, since lidar belongs under Environment as part of the sensing infrastructure the car operates within

**answer** 1
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** peas-framework

**explanation**
Actuators bound how the agent can change the world; sensors bound what it can know. Lidar's laser is a means of measuring, and nothing about the world is altered to the agent's advantage by it. Listing it twice would blur the two ceilings the framework is designed to make explicit.

## Introduction to Artificial Intelligence - MCQ - 2.2.14

**description**
A student says a chess engine faces an adversarial environment and therefore a stochastic one, because it cannot predict the opponent's move. What is the error?

- **option1** There is no error, since an unpredictable opponent is precisely what stochastic means
- **option2** Stochasticity concerns whether the agent's own actions have predictable effects, which they do in chess, and an opponent choosing badly for you is a separate matter
- **option3** Chess is not adversarial, since both players see the same board
- **option4** The error is that stochasticity applies only to environments in which the outcome of an action is determined by a physical process rather than by another player's deliberate choice

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** ai-environments

**explanation**
Moving a rook has exactly the effect the rules state, so the environment is deterministic. Not knowing what the opponent will choose is what makes it adversarial, which is a different property and is handled by searching against a best reply rather than by modelling randomness.

## Introduction to Artificial Intelligence - MCQ - 2.2.15

**description**
When deciding whether a detail belongs in a problem formulation, which set of questions is the right one to ask?

- **option1** Is the detail recorded in the data, is it accurate, and is it available at the time the agent must decide
- **option2** Does it appear in the goal test, does it appear in the initial state, and does it appear in the transition model
- **option3** Does it change which actions are available, does it change the cost meaningfully, and would a solution ignoring it still be carried out successfully
- **option4** Is the detail easy to represent, does it increase the size of the state space, and can it be added later without rewriting the formulation from the beginning

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** problem-formulation

**explanation**
These three questions test whether the detail affects behaviour, cost, or executability, which is exactly what determines whether it belongs. Availability and representational convenience are real engineering concerns and answer a different question, namely whether you can include it, not whether you should.

## Introduction to Artificial Intelligence - MCQ - 2.2.16

**description**
The same problem, encoded two different ways, produces state spaces of very different sizes. What follows for a practitioner?

- **option1** That the two encodings must describe different problems, since a single problem has one state space determined by the rules governing it
- **option2** That the encoding is a design decision with a large effect on whether search is feasible at all
- **option3** That state space size cannot be estimated until the search has been run
- **option4** That the smaller state space is always the better encoding

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** state-space-representation

**explanation**
Include everything that affects the future and exclude everything that does not, and the size of what remains determines whether the problem can be searched. Smaller is usually better but not always, since an encoding can be compact and drop something that mattered, which produces solutions that cannot be executed.

## Introduction to Artificial Intelligence - MCQ - 2.2.17

**description**
Breadth-first search is described as cautious and thorough, yet it is often unusable in practice. What is the reason?

- **option1** It expands the newest discovery first, which sends it down a single branch before the shallower alternatives have been examined
- **option2** It cannot handle graphs containing cycles without an explicit visited set
- **option3** It cannot guarantee the shortest path once step costs differ
- **option4** Its memory requirement grows with each ring of the search, so the frontier becomes too large to hold

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** blind-search-algorithms

**explanation**
Breadth-first search holds an entire ring of the frontier at once and each ring is larger than the last, which is the practical limit on its use. It is true that it guarantees fewest steps rather than lowest cost, and uniform cost search exists for that case, but memory is the reason it is often unusable. Expanding the newest discovery describes depth-first search.

## Introduction to Artificial Intelligence - MCQ - 2.2.18

**description**
A team wants A star to expand fewer nodes and proposes multiplying its admissible heuristic by 1.5. What are they trading?

- **option1** Optimality for speed, since a scaled heuristic may now overestimate and the guarantee requires no overestimate
- **option2** Nothing, since scaling a heuristic changes the order of expansion without affecting which route is returned
- **option3** Memory for speed, since a larger heuristic keeps fewer nodes on the frontier at any moment
- **option4** Completeness for speed, since an inflated heuristic may cause the search to terminate before any route to the goal has been found

**answer** 1
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** heuristic-search-algorithms

**explanation**
Inflating an admissible heuristic can push it above the true remaining cost, and once it overestimates the optimality guarantee no longer holds. The search usually does get faster, which is why the technique is used deliberately when a good-enough route is acceptable. It still finds a route, so completeness is not what is given up.

## Introduction to Artificial Intelligence - MCQ - 2.2.19

**description**
Random restarts and simulated annealing both escaped a local optimum on the same problem. Under what circumstance would random restarts be the weaker choice?

- **option1** When the landscape has only one peak, since restarts would then repeatedly find the same answer
- **option2** When the state space is very large, since restarting requires enumerating it
- **option3** When the best optimum has a very small basin, so few random starting points lead to it
- **option4** When evaluating a state is expensive, since annealing evaluates fewer states in total than a comparable set of restarts would require

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** local-search

**explanation**
Restarts work well precisely when the good peak has a large basin, so they fail when it has a small one and random starts rarely land inside it. A single peak makes hill climbing sufficient and restarts merely redundant rather than weak. Restarting does not require enumerating the space, only sampling a starting point from it.

## Introduction to Artificial Intelligence - MCQ - 2.2.20

**description**
What effect does move ordering have on alpha-beta pruning?

- **option1** It changes the move returned, since different orderings prune different branches
- **option2** It determines whether the search terminates, since a poor ordering can leave the engine examining branches indefinitely
- **option3** It has no effect, since pruning conditions depend only on the values encountered
- **option4** It changes how much of the tree can be skipped, without changing the move returned

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** adversarial-search

**explanation**
Alpha-beta costs nothing in accuracy and returns what full minimax returns whatever the ordering, so the move is unchanged. Examining strong moves first establishes tight bounds early and lets far more of the tree be skipped, which is why engines invest in ordering heuristics.

---

# Set 5

## Introduction to Artificial Intelligence - MCQ - 2.2.21

**description**
A CSP formulation is proposed for exam timetabling: variables are subjects, domains are available slots, and constraints say clashing subjects need different slots. A colleague asks why this is better than writing bespoke scheduling code. What is the strongest argument?

- **option1** That constraints are easier to write than code in every domain where scheduling arises
- **option2** That CSP solvers are faster than any bespoke implementation of the same schedule
- **option3** That the same formulation and the same solving machinery transfer to other problems such as Sudoku and map colouring
- **option4** That a CSP formulation guarantees a solution will be found whenever one exists, which bespoke scheduling code cannot promise without exhaustive enumeration

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** constraint-satisfaction-problems

**explanation**
The reuse is the argument for learning the formulation: variables, domains and constraints describe timetabling, Sudoku and map colouring alike, and the same heuristics such as minimum remaining values apply to all of them. Speed against bespoke code is not guaranteed, and exhaustive bespoke code can also be complete.

## Introduction to Artificial Intelligence - MCQ - 2.2.22

**description**
Forward checking and constraint propagation are described as improvements on plain backtracking. What do they do?

- **option1** They reorder the variables so the most constrained is assigned first
- **option2** They remove values from the domains of unassigned variables once an assignment makes those values impossible
- **option3** They record which assignments have already failed so the same combination is never retried
- **option4** They relax constraints temporarily when no assignment satisfies all of them, then reinstate the constraints once a partial solution has been established

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** constraint-satisfaction-problems

**explanation**
Propagation shrinks the domains of the variables still to be assigned, so a dead end is detected before the search wanders into it. Reordering variables by how constrained they are is minimum remaining values, which is a separate and complementary technique.

## Introduction to Artificial Intelligence - MCQ - 2.2.23

**description**
Sensors and actuators bound what an agent can know and what it can do. Which follows for an agent whose performance measure requires an outcome its actuators cannot produce?

- **option1** The agent will approximate the outcome as closely as its actuators allow
- **option2** The agent will need a richer sensor suite in order to detect how far short it is falling
- **option3** The specification is inconsistent, since the actuators set a ceiling on what can ever be achieved
- **option4** The performance measure will still be satisfied provided the environment is fully observable and the agent deliberates for long enough before committing to an action

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** intelligent-agents-and-problem-solving
**subTopics** peas-framework

**explanation**
Writing PEAS in order exists to catch exactly this. If success requires changing the world in a way the actuators cannot, no amount of sensing or reasoning closes the gap, and the specification has to change. Better sensors would only let the agent observe its own failure more precisely.

## Introduction to Artificial Intelligence - MCQ - 2.2.24

**description**
Which environment property most directly rules out an agent that keeps no internal state?

- **option1** Stochastic
- **option2** Partially observable
- **option3** Continuous
- **option4** Dynamic

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** intelligent-agents-and-problem-solving
**subTopics** ai-environments

**explanation**
If the agent cannot see everything at once, it must remember what it saw earlier, which is what internal state provides. Stochasticity rules out fixed plans, dynamism rules out unbounded deliberation, and continuity affects representation rather than memory.

## Introduction to Artificial Intelligence - MCQ - 2.2.25

**description**
Two students formulate the same problem. One lists the actions available globally; the other lists them per state. Why does this distinction matter?

- **option1** Because which moves are legal generally depends on the current state, and a global list obscures that
- **option2** Because listing actions per state is only possible when the state space is finite
- **option3** Because a global list is longer and therefore slower to read at each step
- **option4** Because the transition model can only be defined once the full set of actions has been enumerated for the problem as a whole

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** problem-formulation

**explanation**
Listing all moves globally rather than per state is one of the commonest formulation mistakes, because legality is state dependent: the blank in an 8-puzzle cannot slide left when it is already on the left edge. The global list then has to be filtered somewhere, and if that filtering is left implicit the formulation is incomplete.

## Introduction to Artificial Intelligence - MCQ - 2.2.26

**description**
A student proposes storing, in each 8-puzzle state, the number of moves made so far, so the search can prefer shorter solutions. What is wrong with putting that in the state?

- **option1** It belongs in the node rather than the state, since it describes how the search arrived rather than the situation itself
- **option2** Nothing, since the number of moves is exactly what the search is trying to minimise
- **option3** It should be stored in the transition model, since each transition increments it
- **option4** It cannot be stored anywhere, because the number of moves is not known until a complete solution has been found and its length can be counted

**answer** 1
**difficulty** hard
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** state-space-representation

**explanation**
A state is a complete description of one situation, and the same tile arrangement is the same situation whether it was reached in four moves or forty. Path length is search bookkeeping and belongs in the node alongside parent, action and cost. Putting it in the state would make identical arrangements look distinct and destroy the search's ability to recognise a repeat.

## Introduction to Artificial Intelligence - MCQ - 2.2.27

**description**
For which problem would depth-first search be a reasonable choice despite its weak guarantees?

- **option1** Finding the cheapest route across a network with varying tolls
- **option2** Finding any complete assignment in a deep tree where solutions are plentiful and memory is scarce
- **option3** Finding the route with the fewest stops in a shallow, wide network
- **option4** Finding the shortest route in a network where every connection has an identical cost and the goal is known to lie a long way from the start

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** intelligent-agents-and-problem-solving
**subTopics** blind-search-algorithms

**explanation**
Depth-first search shines when memory is the binding constraint and any solution will do, because it holds only one branch at a time. The other three ask for optimality of some kind, which needs breadth-first search for fewest steps or uniform cost search for lowest cost.

## Introduction to Artificial Intelligence - MCQ - 2.2.28

**description**
Straight-line distance is the standard heuristic for road navigation. What makes it admissible?

- **option1** That it is computed from coordinates rather than from the road network, so it cannot be distorted by missing roads
- **option2** That it never exceeds the true road distance, since no road can be shorter than the straight line
- **option3** That it is proportional to the true road distance in most networks
- **option4** That it decreases monotonically as the search approaches the goal, which is the property an admissible heuristic is required to have

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** heuristic-search-algorithms

**explanation**
Admissible means never overestimating the remaining cost, and geometry guarantees that a road cannot be shorter than the direct line between two points. Proportionality is neither true in general nor the requirement, and the monotonic property described in one of the distractors is consistency, a related but distinct condition.

## Introduction to Artificial Intelligence - MCQ - 2.2.29

**description**
Hill climbing stops on a plateau, where every neighbouring state has the same value as the current one. Why is this a distinct failure from a local optimum, and what does it change?

- **option1** A plateau occurs only in continuous state spaces, whereas local optima occur only in discrete ones, so the two never arise in the same problem
- **option2** A plateau is a local optimum by another name, and the two require the same remedy
- **option3** On a plateau the algorithm oscillates between two states indefinitely rather than halting
- **option4** On a plateau there is no uphill move and no downhill move either, so the algorithm has no gradient to follow in any direction

**answer** 4
**difficulty** hard
**bloomTaxonomy** analyze
**topics** intelligent-agents-and-problem-solving
**subTopics** local-search

**explanation**
A local optimum is surrounded by worse neighbours, so the rule "take any improving move" has something to reject. A plateau is flat, so there is no signal at all about which way to go, and a strategy of allowing sideways moves for a bounded number of steps is the usual response. Both defeat plain hill climbing and they defeat it differently.

## Introduction to Artificial Intelligence - MCQ - 2.2.30

**description**
In a game tree, why does the agent evaluate a move by passing values up, taking the maximum at its own levels and the minimum at the opponent's?

- **option1** Because the opponent's choices are unknown, so the lowest value is the safest statistical estimate
- **option2** Because minimising at alternate levels keeps the values bounded and prevents the tree from growing exponentially
- **option3** Because the agent no longer picks the whole sequence, so each of its options must be judged by the reply the opponent would actually choose
- **option4** Because the rules of most two-player games award points to one side exactly when they are deducted from the other, which makes minimisation and maximisation interchangeable

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** intelligent-agents-and-problem-solving
**subTopics** adversarial-search

**explanation**
In a single-agent search the agent chooses every step, so it can plan a whole sequence. In a game it chooses only its own moves and the opponent chooses the rest, so a plan is worth what the opponent's best reply leaves it worth. Alternating minimisation does nothing to control the size of the tree, which grows exponentially regardless.

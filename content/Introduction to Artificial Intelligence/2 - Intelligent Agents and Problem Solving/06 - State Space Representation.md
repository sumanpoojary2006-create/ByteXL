## Introduction

Sanjana's eight-year-old cousin hands her a sliding tile puzzle, the plastic kind with eight numbered tiles in a three by three frame and one empty square, and asks her to fix it. She slides tiles around for a while, gets bored, and then does the thing that will matter for the rest of this unit: she asks how many different arrangements the puzzle can possibly be in.

She works it out. Nine positions, nine things to place counting the blank, so nine factorial, which is 362,880. A large number for a toy, but not frightening. A computer could list every one of them in under a second.

Then she asks the better question. Not how many arrangements exist, but how they connect. From any given arrangement, only two, three, or four moves are available, depending on where the blank sits. Each move produces exactly one new arrangement. So the puzzle is not really a pile of 362,880 arrangements; it is a network, where each arrangement is joined to a handful of neighbours, and solving the puzzle means finding a path through that network from where you are to where you want to be.

That network is the **state space**, and once a problem is seen this way, every search algorithm becomes a strategy for walking around it.

**Definition:** The `state space` of a problem is the set of all states reachable from the initial state, together with the transitions between them, forming a graph in which a solution is a path from the initial state to a goal state.

![Opening scene: Sanjana's eight-year-old cousin hands her a sliding tile puzzle, the plastic kind with eight numbered tiles in a three by three frame and one empty square, and asks her to fix it.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_introduction_simple_v2.png)

## What Counts as a State

A `state` is a complete description of the situation at one moment, containing everything that affects what can happen next and nothing else.

Two distinctions keep this precise, and both are routinely blurred.

**A state is not the world.** Sanjana's puzzle sits on a table, has scratched plastic, and belongs to her cousin. The state is only the arrangement of the tiles, because that is the only thing determining which moves are available and whether the puzzle is solved. Everything else has been abstracted away.

**A state is not a node.** This one is subtler and worth getting right early. A state is a configuration, such as tiles in a particular order. A node is a bookkeeping record used during a search, which contains a state but also the parent it came from, the action that produced it, and the cost so far. Two different nodes can hold the same state, reached by different routes, which is exactly what happens when a search rediscovers a position it has seen before. States are facts about the problem; nodes are facts about the search.

![Visual explanation of what counts as a state](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_what_counts_as_a_state_simple_v2.png)

## Operators and Transitions

An `operator` is a rule describing a kind of move, stated once for the whole problem. A `transition` is one specific application of an operator, taking one named state to another.

The 8-puzzle has four operators: slide the blank up, down, left, or right. That is the complete list, and it does not change. What changes is which of them apply. With the blank in a corner, only two are legal; along an edge, three; in the centre, all four.

Written in the usual notation, a transition is a triple of a state, an operator, and the resulting state. Applying "slide blank left" to one arrangement yields exactly one other arrangement. Notice that the 8-puzzle's operators are **reversible**: whatever "slide blank left" does can be undone by "slide blank right". This is why the state space is an undirected graph, and why a search can wander back to where it came from unless something stops it.

Not every problem is like this. Pouring water out of a jug cannot be undone, and a chess pawn cannot move backwards. Those state spaces are directed, and the difference changes what a search can assume.

![Visual explanation of operators and transitions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_operators_and_transitions.png)

## The State Space as a Graph

Put states as nodes and transitions as edges, and the problem becomes a graph. Solving it becomes pathfinding.

An eight-state example makes this concrete, small enough to write out completely. Consider a two-room world with a cleaning robot: the robot is in room A or room B, and each room is independently clean or dirty. That gives two positions times two conditions times two conditions, so eight states in total.

| State | Robot in | Room A | Room B |
| --- | --- | --- | --- |
| S1 | A | dirty | dirty |
| S2 | A | dirty | clean |
| S3 | A | clean | dirty |
| S4 | A | clean | clean |
| S5 | B | dirty | dirty |
| S6 | B | dirty | clean |
| S7 | B | clean | dirty |
| S8 | B | clean | clean |

Three operators are available: move left, move right, and suck. From S1, sucking leads to S3, because the robot cleans room A while standing in it, and moving right leads to S5. The goal states are S4 and S8, the two in which both rooms are clean, and which of them you land in depends only on where the robot finishes standing.

Everything a search algorithm does is visible in this little table. It starts at one row, follows edges to other rows, and stops when it reaches a row satisfying the goal test. The only reason larger problems are harder is that the table cannot be written out.

![Visual explanation of state space graph](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_state_space_graph.png)

## The 8-Puzzle State Space, and a Trap Inside It

Return to Sanjana's puzzle, where the table would have 362,880 rows. Here is the fact that makes it genuinely interesting.

**Only half of those arrangements can be reached from any given starting arrangement.** The reachable state space is 181,440 states, not 362,880. Sliding tiles preserves a mathematical property of the arrangement, so the configurations split into two families, and no sequence of legal moves will ever carry you from one family to the other.

The practical consequence is severe, and it catches people out. If Sanjana's cousin has ever popped a tile out and pushed it back in the wrong slot, the puzzle may now sit in the family that does not contain the solved arrangement. It is not a hard puzzle at that point; it is an impossible one. A search algorithm pointed at it would explore all 181,440 reachable states, find nothing, and only then report failure, having done a great deal of work to discover that the question had no answer.

The lesson generalises well beyond this toy. **Before searching, ask whether the goal is reachable at all.** For many problems, a cheap mathematical check settles it in an instant, where the search would take hours to reach the same conclusion.

![Visual explanation of the 8-puzzle state space, and a trap inside it](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_the_8_puzzle_state_space_and_a_trap_inside_it_simple_v2.png)

## Why State Spaces Explode

Sanjana's puzzle is comfortable. Add one row and one column and it stops being comfortable.

| Problem | Approximate number of states |
| --- | --- |
| Two-room cleaning robot | 8 |
| Tic-tac-toe | About 5,500 legal positions |
| 8-puzzle | 181,440 reachable |
| Rubik's cube | About 4.3 × 10<sup>19</sup> |
| 15-puzzle | About 1.0 × 10<sup>13</sup> reachable |
| Chess | Estimated 10<sup>44</sup> or more legal positions |
| Go on a 19 by 19 board | About 2.1 × 10<sup>170</sup> legal positions |

The step from the 8-puzzle to the 15-puzzle is the one to stare at. The board grew by seven squares and the state space grew by a factor of roughly fifty million. This is `combinatorial explosion`, and it is not a difficulty that faster hardware removes. There are fewer atoms in the observable universe than there are legal positions in Go, so no amount of engineering will let a machine enumerate them.

Everything in the rest of this unit exists because of this table. If state spaces were small, you would list every state, check which are goals, and go home. They are not, so the entire discipline consists of finding goals while visiting as tiny a fraction of the space as possible.

![Visual explanation of why state spaces explode](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_why_state_spaces_explode_simple_v2.png)

## The Representation Decides the Size

Here is the part that separates a student who can define a state space from an engineer who can build one. **The same problem, encoded differently, produces state spaces of wildly different sizes.**

Take a service engineer visiting four sites. One tempting representation is to make the state the full ordered list of places visited so far: depot, then site C, then site A. It works, in the sense that the algorithm will find an answer. But it records the order, and the order does not affect what happens next. Having visited A then C leaves the engineer facing exactly the same remaining problem as having visited C then A, provided the current location is the same. The representation is treating those as different states and searching both.

A better representation is a pair: current location, plus the *set* of sites already visited. Order collapses away, identical situations merge into one state, and the search stops doing the same work twice.

Two rules follow, and they are worth applying to every representation you design.

1. **Include everything that affects the future.** Leave out the set of visited sites and the state is incomplete, so the search will revisit sites and never terminate correctly.
2. **Exclude everything that does not.** Include the order of visits and the state space multiplies for no benefit whatsoever.

Getting rule one wrong produces a program that is wrong. Getting rule two wrong produces a program that is correct and unusably slow, which in practice is often the same thing.

![Visual explanation of the representation decides the size](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_the_representation_decides_the_size.png)

## Tree Search and Graph Search

One final consequence of seeing the state space as a graph rather than a tree.

If a search simply expands states and follows every transition without keeping track, it is performing **tree search**, and it will revisit states endlessly. In the two-room world, the robot could move left, right, left, right forever, generating an infinite sequence of nodes over just two distinct states. In the 8-puzzle, sliding a tile out and back produces the same loop.

Recording which states have already been expanded, and refusing to expand them again, turns this into **graph search**. That record goes by various names, commonly the visited set or the closed list, and it is the reason a search over a finite state space terminates.

The trade is memory for termination. Graph search must hold every state it has seen, which on a large problem is a serious cost, and there are algorithms that deliberately accept repeated work in order to avoid paying it. But for any state space with cycles, and most have them, some form of this bookkeeping is what stands between a search and an infinite loop.

![Visual explanation of tree vs graph search explosion](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_tree_vs_graph_search_explosion.png)

## State Space at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the 8-puzzle</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>State</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A complete description of one situation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One arrangement of the eight tiles and the blank</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Operator</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rule describing a kind of move</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slide the blank up, down, left, or right</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Transition</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One application of an operator, joining two states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">This arrangement, slide blank left, that arrangement</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>State space</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All reachable states plus all transitions, as a graph</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">181,440 reachable arrangements and the moves joining them</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Node</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A search record holding a state plus parent, action, and cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An arrangement together with how the search got there</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Solution</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A path through the graph from initial state to a goal state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The sequence of slides that solves the puzzle</td>
    </tr>
  </tbody>
</table>

![Visual explanation of state space at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_state_space_at_a_glance.png)

## Your Turn

Draw the complete state space of a genuinely tiny problem: a two by two sliding puzzle with three tiles numbered 1, 2, 3 and one blank.

Write out every arrangement, work out which moves connect which, and draw the graph. There are twelve reachable arrangements out of the twenty-four you can write down, so you will meet the reachability trap at a scale where you can verify it by hand rather than taking it on trust. Then pick any two arrangements and count the shortest path between them.

Once the graph is drawn, answer three questions about it. Which arrangement is furthest from the solved one, and how many moves away is it? How many arrangements have only two legal moves available, and what do they have in common? And if you could add one illegal operator, such as lifting a tile out and swapping it with the blank, what would happen to the twelve unreachable arrangements? That last question is the whole reachability idea in miniature, and having drawn the graph yourself you will be able to see the answer rather than deduce it.

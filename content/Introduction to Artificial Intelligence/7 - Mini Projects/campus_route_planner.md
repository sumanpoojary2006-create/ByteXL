## Background

A campus facilities team wants a planner that gives a visitor the shortest walk between any two buildings. That sounds like one problem with one answer, and it is really three questions wearing the same coat: what counts as a state, what counts as a cost, and how much of the map you are willing to look at before committing.

The interesting part is not getting a route. Any of the algorithms in Unit 2 will get a route. The interesting part is that two of them return the cheapest walk and one does not, and the one that does not is the fastest. Seeing that on your own map, with your own numbers, is worth more than reading it in a table.

## What You Will Build

A route planner over a campus map you design, implementing uniform cost search, greedy best-first search, and A star, and a comparison that reports the route, the cost, and how many locations each algorithm examined.

## Learning Objectives

By the end of this project, you will be able to:
- Represent a real place as a state space with weighted transitions
- Implement three search strategies that differ only in how the frontier is ordered
- Explain why an admissible heuristic preserves optimality and an inadmissible one does not
- Demonstrate that expanding fewer nodes and returning a worse answer are different things
- Design a test case that exposes a specific algorithmic weakness on purpose

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Tasks

### Task 1: Build the Map

1. Choose at least twelve campus locations. Give each one a coordinate pair, and give each road a distance. Roads are two-way.

2. Store the coordinates and the roads separately, then build an adjacency structure from them. The coordinates exist only so a heuristic can be computed; the search itself must use the roads.

3. Write a `straight_line(a, b)` function returning the direct distance between two locations from their coordinates.

4. Before searching, assert that no road is shorter than the straight line between its endpoints. If that check fails, your heuristic will overestimate and everything in Task 3 becomes untrue. Fix the map rather than removing the check.

### Task 2: One Search, Three Orderings

1. Write a single `search(start, goal, mode)` function using a priority queue, where `mode` selects what the queue is ordered by:
   - `ucs` orders by the cost so far
   - `greedy` orders by the estimated distance remaining
   - `astar` orders by the sum of the two

2. Return three things: the route, its total cost, and the list of locations expanded in order.

3. Do not write three functions. The point of the exercise is that these three algorithms differ by one line, and writing them separately hides that.

4. Skip a location you have already settled, so the same place is never expanded twice.

### Task 3: Design a Trap, Then Report

1. Add a location that is close to the goal in a straight line but reachable only by a long road. Your reading calls this the river case. Place it so that greedy search walks into it.

2. Add a cluster of locations that are cheap to reach but lie away from the goal. Uniform cost search will expand them because they are cheap; A star should skip them.

3. Print a comparison of all three algorithms giving route, cost, and locations expanded. Then print which locations A star skipped that uniform cost search did not.

4. Your output must show that greedy returns a worse route than the other two. If it does not, your trap is not working and you should move the location or change the road cost until it does.

## Sample Run

```
Planning a route from Main Gate to Sports Ground
Campus has 16 locations and 19 paths

Uniform cost
   route     Main Gate -> Canteen -> Library -> Block A -> Block B -> Sports Ground
   cost      15
   expanded  16 locations

Greedy best-first
   route     Main Gate -> Canteen -> Riverside -> Sports Ground
   cost      23
   expanded  4 locations

A star
   route     Main Gate -> Canteen -> Library -> Block A -> Block B -> Sports Ground
   cost      15
   expanded  11 locations

A star matches the uniform-cost route: True, cost 15
A star expanded 5 fewer locations than uniform cost
Skipped by A star: Guest House, Nursery, Old Block, Pump House, Workshop
Greedy cost 23 against the best 15: NOT optimal
```

Read the greedy row twice. It examined four locations against A star's eleven and returned a walk half again as long. Fewer expansions is not the same as a better answer, and an algorithm that looks efficient can be efficiently wrong.

**Answer these questions after completing all tasks:**
- Greedy search reached Riverside because it was geometrically near the goal. Explain, in terms of what greedy orders its frontier by, why the eight-unit road it took to get there had no influence on that decision.
- Multiply every straight-line estimate in your A star by 1.5 and rerun. Record what happens to the route and to the number of expansions. Which guarantee did you trade, and what did you get for it?
- Uniform cost search expanded every location on your map. Describe the map on which uniform cost search and A star would expand exactly the same number, and say what that tells you about when a heuristic is worth computing.

## Deliverables & Rubric

Submit your `.py` file, the printed comparison, and your written answers to the reflection questions.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Map built with coordinates, roads, and a passing admissibility check | 2 |
| One search function with three frontier orderings, not three functions | 2 |
| All three algorithms return correct routes and expansion counts | 2 |
| Greedy demonstrably returns a worse route than A star on the student's map | 2 |
| Reflection shows the difference between fewer expansions and a better answer | 1 |
| Code readability and organisation | 1 |
| **Total** | **10** |

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)

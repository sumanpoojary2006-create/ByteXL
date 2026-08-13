## Introduction

An ambulance dispatcher in Pune watches the new routing screen take eleven seconds to answer a question she could answer herself in one. The hospital is east. The screen, she can see from the little dots appearing on the map, is patiently costing out roads that run west.

The software is not broken. It is examining those roads with complete seriousness because they happen to be cheap so far, and it has no idea which direction the hospital lies in.

On a map of eight towns this is a minor inefficiency. On the road network of a large city, with hundreds of thousands of junctions, it is fatal. A search that expands outward equally in all directions from the start has to cover an area growing with the square of the distance travelled, so by the time the frontier reaches a destination twenty kilometres away it has examined most of the city.

Yet any person handed the same map solves this instantly. Shown a road heading west when the hospital is east, they do not evaluate it. They know roughly where the hospital is, so they know roughly which way to go, even without knowing the roads. That rough sense of direction, made numerical and handed to the algorithm, is called a **heuristic**, and using one to steer the search is the difference between an algorithm that works on a toy and one that works on a city.

**Definition:** A `heuristic` is a function that estimates the cost of reaching the goal from a given state, and `heuristic search` uses that estimate to decide which part of the frontier to expand next, so the search advances towards the goal instead of spreading out in every direction.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_introduction.png)

## What a Heuristic Actually Is

For any state, a heuristic function returns a number estimating how much further there is to go. It is written `h(n)`, and it is a guess.

For route finding, the standard heuristic is the straight-line distance between a town and the destination. This is easy to compute from coordinates, it requires no knowledge of the roads at all, and it is usually wrong, because no road runs perfectly straight. Being wrong is fine. It only has to be wrong in a useful way.

Contrast it with the other quantity a search already tracks, the cost accumulated so far, written `g(n)`. These two look in opposite directions:

- **`g(n)` looks backwards.** It is the actual, known cost of getting from the start to this state. It is a fact.
- **`h(n)` looks forwards.** It is an estimated cost of getting from this state to the goal. It is a guess.

Everything in this lesson comes from what an algorithm chooses to do with these two numbers.

![Visual explanation of what a heuristic actually is](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_what_a_heuristic_actually_is.png)

## Admissibility: The Property That Makes Heuristics Safe

Not every guess is acceptable. A heuristic is `admissible` when it never overestimates the true remaining cost, meaning `h(n)` is always less than or equal to the real cheapest cost from `n` to the goal.

Straight-line distance is admissible for road travel, and the reason is worth stating properly rather than asserting: no road between two points can be shorter than the straight line between them, because the straight line is the shortest path that exists in the plane. So the estimate is guaranteed to be a lower bound. It may be far too optimistic, as it will be for a town on the far side of a river with one distant bridge, but it will never be too pessimistic.

Admissibility matters because of what it protects. An overestimating heuristic can convince the search that a route is worse than it really is, and the search will then discard the best answer without ever examining it. An underestimating heuristic can only make the search do extra work, never make it wrong. The whole guarantee of the main algorithm in this lesson rests on this one property, and you will break it deliberately at the end of the lesson to watch what happens.

![Visual explanation of heuristic admissibility](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_heuristic_admissibility.png)

## The Map

Eight locations, with straight-line distance to the hospital available from their coordinates, joined by roads of known length.

| Location | Straight-line distance to Hospital (km) |
| --- | --- |
| Depot | 12.65 |
| West End | 15.13 |
| Riverside | 14.14 |
| Market | 8.54 |
| Tech Park | 4.47 |
| North Gate | 5.39 |
| Lake View | 1.41 |
| Hospital | 0.00 |

Two features of this map are deliberate, and they are the whole lesson. **Lake View is only 1.41 km from the hospital in a straight line, but the road between them runs 20 km around a river.** And West End and Riverside sit to the west, in exactly the wrong direction, connected by short cheap roads.

There are two routes to the hospital. Through North Gate and Lake View costs 10 + 5 + 20 = 35 km. Through Market and Tech Park costs 5 + 5 + 5 = 15 km.

![Visual explanation of the map](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_the_map.png)

## Greedy Best-First Search: Trust the Estimate Completely

The simplest way to use a heuristic is to obey it. `Greedy best-first search` orders the frontier by `h(n)` alone, always expanding whichever known state looks closest to the goal.

Reading the code below: `coords` and `roads` are the map, and `straight_line` is the heuristic. The algorithm is `greedy_best_first`, and the thing to watch for is a variable that is deliberately never used.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkbuy" 
 width="100%"
></iframe>

```
Greedy route: Depot -> North Gate -> Lake View -> Hospital
Actual distance: 35 km
Towns expanded: 3
```

Greedy did brilliantly on effort and badly on answer. Three towns expanded, which is as few as anything could manage, and a route more than twice as long as necessary.

The reason is one line, and it is the underscore.

| In the code | What it is | Consequence |
| --- | --- | --- |
| `straight_line(town, goal)` | The heuristic, `h(n)` | The only thing the frontier is sorted by |
| `for neighbour, _distance in roads[town]` | The road length, unpacked and discarded | The leading underscore is Python's convention for "deliberately unused" |
| `heappush(frontier, (straight_line(...), ...))` | Push with the estimate only | Nothing about distance travelled enters the ordering |
| `expanded` | A counter | Lets us compare effort against the next algorithm |

**Greedy best-first search does not know how far it has already walked.** From the depot it saw North Gate at 5.39 km from the hospital and Market at 8.54, chose North Gate, and never registered that reaching North Gate cost 10 km while Market cost 5. It then walked into Lake View, which looks 1.41 km from the hospital and is 20 km from it by road.

Greedy is fast, and it will find a path if one exists in a finite graph, but it offers no guarantee whatsoever about quality. It is the algorithmic version of walking towards a destination by always heading in its general direction, which works until you meet a river.

![Visual explanation of greedy vs astar](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_greedy_vs_astar.png)

## A\* Search: Use Both Numbers

The fix is not to distrust the heuristic but to stop ignoring the cost already paid. `A* search` orders the frontier by the sum of the two:

**f(n) = g(n) + h(n)**

Read that as an estimate of the total cost of the whole journey if it passes through this state: what the journey has cost so far, plus what it is estimated still to cost. Expanding the smallest `f` means always working on the route that currently looks most promising overall, rather than the one that has been cheapest so far or the one that merely looks nearest.

Reading the code below: one function, `best_first`, with a switch. Called with `use_heuristic=True` it is A\*; called with `False` it is uniform cost search. Writing both as one function is the point rather than a shortcut, because it shows they differ by a single term.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkc6g" 
 width="100%"
></iframe>

```
A* route: Depot -> Market -> Tech Park -> Hospital
Distance: 15 km, towns expanded: 3
UCS route: Depot -> Market -> Tech Park -> Hospital
Distance: 15 km, towns expanded: 6
```

That output contains the entire argument for A\*. It matched greedy's effort, three towns expanded, and it matched uniform cost search's answer, the genuinely shortest route at 15 km. Uniform cost search reached the same answer while expanding twice as many towns, because it wasted effort on West End and Riverside, the two locations in the wrong direction.

Notice also that the same function produced both results.

| In the code | What it holds | Set it to zero and you get |
| --- | --- | --- |
| `new_g = g + distance` | Distance actually travelled, `g(n)` | Greedy best-first search |
| `h = straight_line(...)` | Estimated distance remaining, `h(n)` | Uniform cost search |
| `new_g + h` | The frontier's sort key, `f(n)` | The one line that defines A\* |

That table is the whole lesson in three rows. **UCS is A\* with a heuristic that gives up and says zero**, and greedy is A\* that has forgotten `g`. The three algorithms are one algorithm with two terms, and which term you drop decides which one you have.

Following the values makes the mechanism concrete.

| Step | Expanded | g | h | f = g + h | Frontier afterwards, by f |
| --- | --- | --- | --- | --- | --- |
| 1 | Depot | 0 | 12.65 | 12.65 | Market 13.54, North Gate 15.39, West End 19.13 |
| 2 | Market | 5 | 8.54 | 13.54 | Tech Park 14.47, North Gate 15.39, West End 19.13 |
| 3 | Tech Park | 10 | 4.47 | 14.47 | Hospital 15.00, North Gate 15.39, West End 19.13 |
| 4 | Hospital | 15 | 0 | 15.00 | goal reached, 15 km returned |

Look at the last row against the one above it. When the hospital came off the frontier at f = 15.00, North Gate was still sitting there at 15.39. A\* never expanded it, and it was right not to, because 15.39 is a promise that any route through North Gate must cost at least 15.39 km, which is already worse than the completed 15 km route in hand. That is admissibility doing its job: because `h` never overestimates, an `f` value is a genuine lower bound, so anything with a larger `f` than a finished route can be dismissed without being examined.

This is also the proof sketch for the guarantee. **With an admissible heuristic, A\* returns an optimal path.** Since `f` never overstates the true total cost of a route through a state, A\* cannot pull a goal off the frontier while a cheaper route remains unexplored, because that cheaper route would have had a smaller `f` and would have come off first.

![Visual explanation of a\* search: use both numbers](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_a_search_use_both_numbers.png)

## How Route Planners Actually Work

It is tempting to conclude that a navigation app runs A\* over the road network. The truth is more interesting and worth knowing.

A\* is the conceptual foundation, and every serious route planner is a descendant of it. But running plain A\* across a continental road graph for every request would still be far too slow at the scale of millions of queries per minute, so real systems add several things.

- **Precomputation.** The road network changes rarely, so systems spend enormous offline effort building shortcut structures that let a query skip vast numbers of minor roads, which is why a long-distance route returns as fast as a short one.
- **Searching from both ends.** Running two searches, one forward from the start and one backward from the destination, until they meet, explores far less than a single search covering the whole distance.
- **Better cost functions.** The cost of a road is not its length. It is predicted travel time, built from historical patterns for this road at this hour on this day, adjusted by live speed data.
- **Heuristics beyond straight-line distance.** Distance divided by the maximum plausible speed gives an admissible estimate in units of time, which is what the cost function actually uses.

The idea that survives all of this is the one from the table above: keep a lower bound on the total cost of any route through a state, and refuse to examine anything whose lower bound is already worse than a complete answer you hold.

![Visual explanation of how route planners actually work](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_how_route_planners_actually_work.png)

## The Three Strategies at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Algorithm</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Orders frontier by</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">On this map</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Optimal?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Uniform cost</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>g(n)</code>, cost so far</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15 km, 6 towns expanded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, but explores in every direction</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Greedy best-first</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>h(n)</code>, estimate remaining</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">35 km, 3 towns expanded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, and it can be arbitrarily bad</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>A*</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>g(n) + h(n)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15 km, 3 towns expanded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, provided the heuristic is admissible</td>
    </tr>
  </tbody>
</table>

One honest qualification. A\* is optimal in the answer it returns, and it is also efficient in a precise sense, but it is not free. It holds the frontier in memory just as uniform cost search does, and on very large problems that memory is the limiting factor rather than the time.

![Visual explanation of the three strategies at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_the_three_strategies_at_a_glance.png)

## Your Turn

The guarantee in the last column of that table has a condition attached, and conditions are best understood by violating them.

Multiply the heuristic by a weight. With a weight of 1 you have ordinary A\*. With a larger weight, the estimate is deliberately inflated, so it starts claiming that the remaining journey is longer than it really is, which is precisely what admissible means you must not do. Predict what will happen before running it.

Reading the code below: this is the A\* function from above with one character added. `h` becomes `weight * straight_line(...)`, and the loop at the bottom runs the whole search twice with different weights.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkd8k" 
 width="100%"
></iframe>

```
weight 1: 15 km via Depot -> Market -> Tech Park -> Hospital
weight 5: 35 km via Depot -> North Gate -> Lake View -> Hospital
```

The guarantee is gone. At weight 5 the algorithm walks straight into the trap and returns the 35 km route through Lake View, because inflating `h` made Lake View's apparent nearness dominate the sum, and the 20 km of road already committed to stopped weighing enough to correct it. This is exactly the greedy failure arriving through a different door.

Now find the boundary yourself. Add weights of 2, 3, and 4 to the loop and locate the point where the answer flips. You will find that the route survives at 3 and breaks at 4, which is worth pausing over: a heuristic can be somewhat wrong and still produce the right answer, so admissibility is a condition that guarantees optimality rather than a line that destroys it the instant it is crossed.

Then ask the question a practitioner would. Given that weighted A\* expands fewer states and sometimes returns a worse route, when would you deliberately accept it? If your answer involves a deadline and a route that only has to be good rather than perfect, you have found the reason this variant is used in real systems rather than being merely a cautionary tale.

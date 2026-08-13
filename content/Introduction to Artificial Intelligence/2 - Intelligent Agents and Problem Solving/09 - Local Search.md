## Introduction

Latha runs the dispatch desk for a courier branch, and every morning she has the same job: eight stops to cover, one van, and a route to decide before the driver leaves at seven.

She has watched a trainee attempt this with the tools from earlier in this unit, treating it as a path-finding problem, and she has watched it fail in an interesting way. The trainee's program built up routes step by step, holding every partial route it had considered, and ran out of patience long before it finished. The number of possible orderings of seven stops after the warehouse is 5,040, which sounds manageable, but the program was not choosing among 5,040 finished routes. It was exploring a tree of partial routes and keeping the lot in memory.

Latha's reaction cuts to the heart of this lesson. She does not want the sequence of decisions that produced the route. She does not care which orderings were considered along the way. She wants one thing, printed on one sheet of paper: the order of stops. The journey the algorithm took to find it is of no interest whatsoever.

When only the final configuration matters and the route to it is irrelevant, holding paths in memory is pure waste, and a completely different family of algorithms becomes available. They are called **local search**.

**Definition:** `Local search` algorithms keep a single current state and repeatedly move to a neighbouring state, discarding the path taken, which makes them suitable for problems where the solution is the final configuration itself rather than the sequence of steps that reached it.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_introduction.png)

## When the Path Does Not Matter

The distinction is not a technicality. It changes what a solution *is*.

- In **path problems**, the answer is the sequence. Asked how to get from the hostel to the exam hall, "the exam hall" is not an answer. The route is the whole point.
- In **configuration problems**, the answer is the final state. Asked for a clash-free timetable, nobody wants the sequence of edits that produced it. The timetable is the answer, and it is equally good however you arrived at it.

Route ordering, timetabling, seating plans, exam scheduling, and circuit layout are all configuration problems. So is choosing the parameters of a model. In every case the same three consequences follow, and they are what make local search attractive.

1. **Memory is constant.** One current state is held, not a frontier that grows. Latha's problem needs one route in memory, never thousands.
2. **The state space can be unimaginably large.** Since nothing is enumerated, a space too big to search exhaustively is no obstacle in itself.
3. **The algorithm can stop whenever you like.** There is always a current state that is a valid answer, so a deadline produces the best answer found so far rather than nothing at all.

The price is stated plainly at the outset: **local search offers no guarantee of finding the best answer**, and usually cannot even tell you how close it got. Everything after this is about managing that price.

![Visual explanation of when the path does not matter](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_when_the_path_does_not_matter.png)

## The Landscape Metaphor

Picture the state space as a terrain. Every possible route is a point on the ground, and the height at that point is how good the route is. For Latha, a shorter round is better, so it is easier to picture the height as total kilometres and look for the lowest valley rather than the highest peak. The terms `hill climbing` and `local maximum` come from the maximising version, and the ideas are identical either way.

Local search is then a walker on this terrain who can see only the ground immediately around their feet. They cannot see the whole landscape, they have no map, and their entire strategy consists of deciding which neighbouring patch to step onto next.

The `neighbourhood` is the set of states reachable in one small change from the current one. Defining it is a design decision with real consequences. For Latha's route, a natural choice is "swap the positions of any two stops", which for eight stops gives twenty-one neighbours to inspect. A different choice, such as reversing a whole segment of the route, would give a different landscape shape from exactly the same problem.

![Visual explanation of local search landscape](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_local_search_landscape.png)

## Hill Climbing

`Hill climbing` is the simplest possible strategy: look at every neighbour, move to the best one, and repeat until no neighbour is an improvement.

Reading the code below: three small functions and a loop. `tour_length` scores a route, `neighbours` generates the small changes, and the loop repeatedly takes the best one. Watch how little is stored, because that is the whole point of local search.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkgq5" 
 width="100%"
></iframe>

```
Starting round: 62.9 km
  step 1: improved to 52.8 km
  step 2: improved to 47.6 km
  step 3: improved to 42.1 km
Stuck at: 42.1 km
Route: Warehouse -> East Market -> Dairy Circle -> City Mall -> Bus Stand -> Ashok Nagar -> Fort Road -> Green Park
No single swap makes this shorter.
```

Three steps took a 62.9 km round down to 42.1 km, which is a real improvement obtained very cheaply.

| In the code | What it is | Why it matters |
| --- | --- | --- |
| `current` | A single route, overwritten each step | The entire memory. No frontier, no history, constant space |
| `neighbours(tour)` | The 21 routes one swap away | Defines what "nearby" means, and therefore the whole landscape |
| `min(neighbours(...), key=tour_length)` | The best neighbour | Look everywhere adjacent, move to the best |
| `if tour_length(best) >= ...: break` | The stopping rule | Stops when nothing adjacent improves, which is the trap |

The second row is the design decision people overlook. Choosing swaps rather than, say, reversing a segment produces a different set of neighbours from the same problem, and therefore a different set of places the search can get stuck.

Notice also what the last line claims, and that the claim is true. Every one of the twenty-one possible swaps produces a longer round. From where the algorithm stands, every direction is uphill, so it stops.

It has stopped at 42.1 km. The best possible round for these eight stops is 35.4 km. Hill climbing did not fail to look hard enough; it looked at every neighbour it had. It simply cannot see past them.

![Visual explanation of hill climbing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_hill_climbing.png)

## The Three Ways Hill Climbing Fails

The 42.1 km result is not bad luck. It is one of three characteristic failures, and all three come from the same cause: **the algorithm decides using only local information.**

1. **A local optimum.** A state better than all its neighbours but worse than the best state overall, which is exactly where Latha's route stopped. Escaping it requires accepting a worse route first, and hill climbing never does that.

2. **A plateau.** A flat region where many neighbours score exactly the same. The algorithm has no gradient to follow and either stops early or wanders sideways without progress. Timetabling problems are full of these, because moving one class often changes nothing measurable until several move together.

3. **A ridge.** A sequence of states forming a narrow rising path where every individual small step goes down, even though a combination of two steps would go up. Since the neighbourhood only permits one change at a time, the algorithm cannot take the combination and stalls on a slope it could have climbed.

All three have the same remedy in principle. The algorithm must sometimes be willing to move somewhere worse.

![Visual explanation of the three ways hill climbing fails](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_the_three_ways_hill_climbing_fails.png)

## Random Restarts

The bluntest remedy is also surprisingly effective: if one starting point leads to a poor peak, start again somewhere else and keep the best result.

Reading the code below: the scoring and neighbour functions are unchanged, and `hill_climb` is the loop from the previous program wrapped into a function. The new part is the last block, which runs it 50 times from different random starts and tallies where each run ended.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkhg9" 
 width="100%"
></iframe>

```
Where 50 restarts ended up:
   35.4 km  reached by 29 restarts
   39.4 km  reached by 10 restarts
   42.1 km  reached by  7 restarts
   46.8 km  reached by  4 restarts
Best found: 35.4 km
Route: Warehouse -> Green Park -> Fort Road -> East Market -> Dairy Circle -> City Mall -> Bus Stand -> Ashok Nagar
```

That output is a map of the landscape, and it is worth more than the answer. This problem has exactly four local optima reachable by swapping, at 35.4, 39.4, 42.1, and 46.8 kilometres. Latha's single run landed on the third of them. Fifty runs found the best one twenty-nine times.

Two lessons follow. **The number of distinct peaks tells you how rugged the landscape is**, and a landscape with four peaks where the best is reached by more than half of all restarts is a gentle one. **Random restarts work well precisely when the good peak has a large basin**, meaning many starting points flow into it. On a landscape with one narrow deep valley and thousands of shallow ones, restarts would almost never find it, and this is where the method quietly fails.

![Visual explanation of restart and annealing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_restart_and_annealing.png)

## Simulated Annealing

Restarts escape a local optimum by abandoning the search and beginning again. `Simulated annealing` takes a more elegant route: it allows the current search to move to a worse state, with a probability that starts high and falls over time.

The name comes from metallurgy. Cooling a metal slowly lets its atoms settle into a low-energy, well-ordered structure, whereas cooling it suddenly locks in whatever disordered arrangement happened to exist. The algorithm imitates this with a `temperature` that begins high and is reduced on a schedule.

The rule for each proposed move is short.

- **If the move improves things, always take it.**
- **If it makes things worse, take it anyway with probability** that falls as the move gets worse and as the temperature drops.

The behaviour that results is what makes it work. Early, when the temperature is high, the search accepts most proposals and roams widely, which is how it crosses out of a valley it would otherwise be trapped in. Late, when the temperature is low, it accepts almost nothing that is worse, so it settles. The algorithm explores first and refines afterwards, without anyone telling it when to switch.

Reading the code below: two differences from hill climbing. `random_neighbour` proposes one route at random instead of inspecting all 21, and the acceptance test is a single `if` that can say yes to a worse route. The two lines controlling temperature are the whole method.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkhzy" 
 width="100%"
></iframe>

```
Starting round: 62.9 km
Final round:    35.4 km
Worse rounds accepted on the way: 220
Route: Warehouse -> Ashok Nagar -> Bus Stand -> City Mall -> Dairy Circle -> East Market -> Fort Road -> Green Park
```

From the identical starting round that trapped hill climbing at 42.1 km, simulated annealing reached 35.4 km, the best possible. The number that explains it is the second one: it accepted 220 moves that made the route *longer*. Every one of those was a step hill climbing would have refused, and they are collectively the reason it escaped.

Four lines carry the whole method.

| In the code | What it does | Effect of changing it |
| --- | --- | --- |
| `random_neighbour(current)` | Proposes one route instead of all 21 | Far cheaper per step, so many more steps are affordable |
| `change < 0` | Always accept an improvement | Remove it and the search stops descending |
| `math.exp(-change / temperature)` | Chance of accepting a worse route | A slightly worse route is accepted more readily than a much worse one |
| `temperature *= 0.997` | The cooling schedule | The parameter that matters most, and the exercise below breaks it |

Read the third row against the second. Together they are the entire difference from hill climbing: an algorithm that only ever takes the second row is hill climbing, and adding the third is what lets it leave a valley. Cool too fast and the third row switches off early, which is hill climbing with extra steps; cool too slowly and it wanders far longer than necessary.

The route it printed is the same loop the restarts found, travelled in the opposite direction, which for a round trip is the same route.

![Visual explanation of simulated annealing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_simulated_annealing.png)

## Local Search at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Accepts a worse state?</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">On Latha's round</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Fails when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Hill climbing</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Never</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">42.1 km, stuck in 3 steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The landscape has local optima, plateaus, or ridges</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Random restarts</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, it abandons and restarts instead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">35.4 km, found by 29 of 50 runs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The best optimum has a very small basin</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Simulated annealing</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, with falling probability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">35.4 km, after 220 worse moves</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cooling schedule is badly chosen</td>
    </tr>
  </tbody>
</table>

![Visual explanation of local search at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_local_search_at_a_glance.png)

## Your Turn

Take the annealing code and break it deliberately, in two different ways.

First, set the cooling factor to `0.9` instead of `0.997`. The temperature will now collapse within a few dozen iterations. Predict what the result should resemble before you run it, then check whether the number of worse moves accepted drops as sharply as you expected, and explain why the outcome looks like hill climbing again.

Second, set the starting temperature to `0.001` and leave the cooling alone. Work out from the acceptance formula, before running anything, what fraction of worse moves will be accepted at that temperature, and confirm your reasoning against the output.

Then the design question, which is the one that matters at work. Latha's real branch has forty stops, not eight, and she needs an answer within thirty seconds every morning. Restarts and annealing both fit that budget. Which would you choose, and what would you need to measure about her particular problem to decide? If your answer is "run both for thirty seconds on a month of real routes and compare", you have understood the honest truth about local search: these methods come with no guarantees, so the only way to choose between them is to try them on your actual data.

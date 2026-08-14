## Introduction

Ishaan is handed what sounds like a simple task at his internship: work out the best way for the company's service engineer to visit four customer sites in a day and get back to the depot.

He sits with it for twenty minutes and realises he cannot begin, because the sentence he has been given is not a problem a program can accept. What does "best" mean, least distance or least time or least fuel? Is the engineer's lunch break part of the problem? Does the traffic at four in the afternoon matter? Is the depot a place he must return to or merely where he happens to start? Can he visit a site twice? None of this is written anywhere, and every answer changes the task.

What Ishaan is facing is the step that sits between a real situation and any algorithm at all. A search algorithm cannot accept "find the best route". It can accept a precise object with a defined starting point, a defined set of moves, a definition of what counts as finished, and a number attached to each move. Producing that object is called **problem formulation**, and it is where most of the intelligence in a solution actually lives.

**Definition:** `Problem formulation` is the process of restating a real-world situation as a precise search problem, by specifying the initial state, the actions available, the result of each action, a test for the goal, and the cost of each step.

![Opening scene: Ishaan is handed what sounds like a simple task at his internship: work out the best way for the company's service engineer to visit four customer sites in a day and get back to the depot.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_introduction.png)

## From a Real Situation to a Solvable One

The first thing formulation demands is `abstraction`: deciding which details of the real situation to keep and which to discard.

Ishaan's engineer is a person with a scooter, a phone, a lunch preference, and a tendency to chat with customers. The road network has potholes, traffic signals, a market that floods on Tuesdays, and a bypass under construction. None of that can go into the problem, and almost none of it should.

A good abstraction keeps exactly what affects the answer. For a route problem, that is usually the set of locations, which pairs are connected, and the cost of each connection. Everything else is dropped, and dropping it is not laziness but the entire reason the problem becomes tractable.

The risk is dropping something that mattered. If afternoon traffic doubles the travel time on one road, and the abstraction records a single fixed cost per road, the algorithm will confidently return a route that is wrong in practice. **An abstraction is valid when every solution in the abstract problem corresponds to a solution in the real world.** If the answer the program gives cannot actually be carried out by the engineer, the abstraction has removed something it should have kept.

![Visual explanation of from a real situation to a solvable one](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_from_a_real_situation_to_a_solvable_one.png)

## The Five Components

A well-formed search problem has five parts. Four of them are the ones usually named, and the fifth quietly holds them together.

1. **The initial state.** Where the agent begins. For Ishaan, the engineer at the depot with no sites yet visited.

2. **The actions.** For any given state, the set of moves legally available from it. Not all moves in general, but the ones applicable here and now. From the depot, the actions are travelling to any of the four sites.

3. **The transition model.** What each action results in. Applying "travel to site B" to a state produces a new state where the engineer is at site B and B has been added to the visited set. This is the component that gets left out of the usual list of four, and without it the actions are just names.

4. **The goal test.** A check applied to a state that answers whether the job is done. For Ishaan, all four sites visited and the engineer back at the depot.

5. **The path cost.** A number accumulated over the sequence of actions, which the algorithm will try to minimise. Ishaan must choose: kilometres, or minutes, or fuel. They give different answers.

Together these five define the problem completely, and notice what is absent from the list. Nothing here says how to solve it. Formulation states the problem; the algorithm searches it. Keeping those two jobs separate is what allows the same search algorithm to solve a puzzle, a route, and a scheduling task without modification.

![Visual explanation of problem formulation five components](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_problem_formulation_five_components.png)

## Worked Formulation: A Maze

Take a maze on a grid, where a walker starts at one cell and must reach another, moving one cell at a time in four directions and not passing through walls.

| Component | Formulation |
| --- | --- |
| Initial state | The cell the walker starts in, for example (0, 0) |
| Actions | Move up, down, left, or right, restricted to moves that stay in the grid and do not enter a wall |
| Transition model | Moving from (r, c) in a direction results in the adjacent cell in that direction |
| Goal test | Is the current cell the exit cell? |
| Path cost | 1 per move, so total cost equals the number of steps taken |

Two things in that table are worth noticing. The actions are restricted per state rather than listed once globally, because at a corner only two moves are legal, and building the wall check into the action set means the algorithm never has to know what a wall is. And the state is just a pair of coordinates, because in this maze nothing else affects what the walker can do next. A state must capture everything relevant and nothing more.

![Visual explanation of worked formulation: a maze](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_worked_formulation_a_maze.png)

## Worked Formulation: Ishaan's Service Route

Now the harder one, and the difference is instructive.

| Component | Formulation |
| --- | --- |
| Initial state | At the depot, with the set of visited sites empty |
| Actions | Travel to any site not yet visited; travel to the depot if all sites are visited |
| Transition model | Travelling to site X results in being at X with X added to the visited set |
| Goal test | At the depot, with all four sites in the visited set |
| Path cost | Travel minutes between consecutive locations, summed |

The critical difference from the maze is what a state must contain. In the maze, position alone is enough. Here, position alone is useless: being at site C having already covered A and B is a completely different situation from being at site C having covered nothing, because the moves available and the remaining work differ. **The state must include the set of sites already visited**, and getting this wrong is the most common formulation error there is.

The test for whether a state is complete is simple and worth applying every time: given only this state, and nothing about how the agent arrived at it, can you determine which actions are legal and whether the goal is met? If you need to peek at the history, the state is missing something.

![Visual explanation of worked formulation: ishaan's service route](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_worked_formulation_ishaan_s_service_route.png)

## Choosing the Right Level of Abstraction

Formulation is a series of judgment calls about detail, and both directions fail.

Model Ishaan's problem too finely, treating every road segment and every signal as a separate state with time-varying costs, and the state space becomes enormous while the answer barely improves. Model it too coarsely, ignoring that two sites are on opposite sides of a river with a single bridge, and the algorithm returns a route the engineer cannot follow.

Three questions resolve most of these calls.

- **Does this detail change which actions are available?** If yes, it belongs in the state.
- **Does this detail change the cost meaningfully?** If yes, it belongs in the cost function.
- **Would a solution ignoring this detail still be carried out successfully?** If no, the detail cannot be dropped.

Ishaan's afternoon traffic passes the second test, so it belongs in the cost function, probably as a different travel time depending on the time of day. His engineer's chattiness fails all three and gets dropped.

![Visual explanation of abstraction and goal test](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_abstraction_and_goal_test.png)

## Goal Test: Stated Explicitly or by Property

One component deserves a closer look, because it comes in two forms that behave quite differently.

An **explicit** goal test names the target states outright. Reaching the exit cell at (9, 9) is explicit: you compare against a known value.

An **implicit** goal test states a property that a goal state must satisfy, without listing which states those are. "All four sites visited and back at the depot" is implicit, because it describes a condition rather than an address, and there may be many distinct states satisfying it. A Sudoku goal test is implicit too: no repeated digit in any row, column, or box.

The distinction matters because an implicit test is often the only option available. Listing every solved Sudoku grid in advance is not feasible, whereas checking the property takes microseconds. When you cannot enumerate the goals, you can still recognise one when you see it, and that is enough for search to work.

![Visual explanation of goal test: stated explicitly or by property](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_goal_test_stated_explicitly_or_by_property.png)

## Problem Formulation at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Component</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Commonest mistake</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Initial state</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where does the agent begin?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Omitting part of the starting situation, such as what has already been done</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Actions</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What moves are legal from this state?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Listing all moves globally instead of per state</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Transition model</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What state does this action produce?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaving it implicit, so the action is only a label</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Goal test</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is the job finished?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assuming goals must be listed when a property will do</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Path cost</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is being minimised, in what units?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choosing steps when the thing that matters is time or money</td>
    </tr>
  </tbody>
</table>

![Visual explanation of problem formulation at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_problem_formulation_at_a_glance.png)

## Your Turn

Formulate the problem of getting yourself from your room to your first class of the day as a search problem, filling in all five components.

Do it twice, with one change between them. In the first version, path cost is minutes. In the second, path cost is money, and the options include an autorickshaw. Note what changes and what does not: the states and actions may be identical while the answer flips entirely, which is the clearest possible demonstration that the cost function is a design decision rather than a fact about the world.

Then attempt one that will genuinely resist you. Formulate the problem of packing a bag for a three-day trip. Work out what a state is, and how you would write the goal test, and you will quickly find that "everything I need is packed" is not checkable unless you have already listed what you need, while "the bag closes" is checkable but is obviously not the goal. Sitting with that difficulty is the point of the exercise, because real problems very often fail at the goal test long before they fail at the algorithm.

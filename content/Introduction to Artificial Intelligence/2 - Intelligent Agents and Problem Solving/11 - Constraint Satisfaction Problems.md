## Introduction

Every February, the vice principal of Deepa's college locks herself in her office for three days with a whiteboard and builds next semester's timetable by hand. Deepa has seen the whiteboard. It is covered in subject names, arrows, and a great many crossings-out.

The difficulty is not that there are many subjects. It is that everything interferes with everything else. Professor Rao teaches both Maths and Physics, so those two can never share a slot. Physics and Chemistry both need the main laboratory. The second-year batch takes Maths and Chemistry, so those cannot clash either. Fix one collision and two more appear somewhere else on the board.

Notice what the vice principal is not doing. She is not looking for a route, or a sequence of moves, or a plan. There is no journey here. She is trying to give each subject a slot such that a list of rules is not broken, and when she finally succeeds, nobody will ask her how she got there. The finished grid is the entire answer.

Problems shaped like this are so common, and so different from everything else in this unit, that they have their own formulation and their own algorithms. They are **constraint satisfaction problems**.

**Definition:** A `constraint satisfaction problem`, or CSP, is defined by a set of `variables`, a `domain` of possible values for each variable, and a set of `constraints` restricting which combinations of values are permitted; a solution is an assignment of one value to every variable that violates no constraint.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_introduction.png)

## A Different Shape of Problem

Compare the two formulations directly, because the difference determines which algorithms apply.

- In a **search problem**, the state is a black box. The algorithm knows only that a state exists, that operators lead to other states, and that a goal test can be applied. It has no idea what a state is made of.
- In a **CSP**, the state is transparent. It is a set of variables with values, and the algorithm can see inside it. It can ask which variable is causing trouble, which values remain possible for a variable, and which constraint has just been broken.

That visibility is the whole advantage. A search algorithm that hits a dead end can only back up and try something else. A CSP solver that hits a dead end can inspect the assignment, identify the variable responsible, and reason about it. This is why a general CSP solver often beats a general search algorithm on the same problem, despite knowing nothing about timetables or Sudoku specifically.

There is also a practical consequence worth noticing. Because a solution is a complete assignment rather than a path, **the order in which variables are assigned does not affect the answer**, only the effort. Deepa's vice principal could schedule Chemistry first or last and reach an equally valid timetable. The algorithms below exploit exactly this freedom.

![Visual explanation of a different shape of problem](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_a_different_shape_of_problem.png)

## Variables, Domains, and Constraints

Three components define any CSP, and formulating one is a matter of naming all three precisely.

1. **Variables.** The things that need values. For the timetable, one variable per subject. For Sudoku, one variable per blank cell.

2. **Domains.** The values each variable may take. For the timetable, the available time slots. For Sudoku, the digits 1 to 9.

3. **Constraints.** The rules restricting combinations. Constraints are classified by how many variables they involve: a **unary** constraint restricts one variable, such as a professor being unavailable on Tuesdays; a **binary** constraint relates two, such as Maths and Physics needing different slots; and a **global** constraint covers many at once, such as all nine cells in a Sudoku row taking different values.

Most textbook CSPs are expressed with binary constraints, because any constraint over more variables can in principle be rewritten as a collection of binary ones, and algorithms are simpler when only pairs are involved.

![Visual explanation of csp variables domains constraints](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_csp_variables_domains_constraints.png)

## Sudoku as a CSP

Sudoku is the cleanest possible illustration, because all three components fall out immediately.

| Component | Sudoku |
| --- | --- |
| Variables | One per empty cell, up to 81 of them |
| Domains | The digits 1 to 9 |
| Constraints | All cells in a row differ, all cells in a column differ, all cells in a three by three box differ |

That is the entire specification. Nothing in it mentions strategy, technique, or any of the named patterns that puzzle books teach. A solver needs only these three facts.

Before writing any algorithm, look at the size of what is being asked. A puzzle with fifty-one blank cells and nine possible digits each has nine to the power of fifty-one possible assignments, which is a number with forty-nine digits. Checking them one by one is not an option, and once again the whole task is to find the answer while examining almost none of them.

![Visual explanation of sudoku as a csp](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_sudoku_as_a_csp_simple_v2.png)

## Backtracking Search

The core algorithm is `backtracking search`, and it is the obvious idea done carefully.

Pick an unassigned variable. Try a value that does not immediately break a constraint. Move on to the next variable. If you reach a variable with no legal value left, the earlier choice was wrong, so undo it and try the next value there instead.

The word that matters is undo. A naive program that only ever moved forward would fail on the first wrong guess. Backtracking works because every choice is provisional, and the algorithm is willing to walk back.

A four-cell fragment shows the shape of it. Suppose two cells in a row already contain 5 and 3, and two blanks remain with domain restricted to 1, 3, and 7 by the surrounding rows and boxes.

| Step | Action | State of the row | Result |
| --- | --- | --- | --- |
| 1 | Try 1 in the first blank | 5, 3, 1, blank | Legal so far, go deeper |
| 2 | Try 1 in the second blank | 5, 3, 1, 1 | Breaks the row constraint, reject |
| 3 | Try 3 in the second blank | 5, 3, 1, 3 | Breaks the row constraint, reject |
| 4 | Try 7 in the second blank | 5, 3, 1, 7 | Legal, continue |

Had step 4 also failed, the algorithm would have returned to step 1, undone the 1, and tried 3 there instead. That return is the backtrack.

Reading the code below: three short functions. `allowed` is the constraint check, `first_empty` chooses which cell to fill next, and `solve` is backtracking itself, at nine lines. The two lines that matter most are a pair: one writes a digit into the grid, and one takes it back out again.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkdke" 
 width="100%"
></iframe>

```
Blank cells to fill: 51
Solved: True
Digits placed (including ones later undone): 4208
  534678912
  672195348
  198342567
  859761423
  426853791
  713924856
  961537284
  287419635
  345286179
```

The whole solver is three short functions, and one pair of lines is the algorithm.

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `allowed(...)` | The constraints, all three at once | Row, column, and box checked in one call |
| `first_empty(grid)` | Choice of which variable to assign | Arbitrary here, and the next program shows what that costs |
| `grid[row][col] = digit` | **Assign**, provisionally | Every choice is a guess until proven otherwise |
| `if solve(...): return True` | Try to finish from here | Success propagates straight back up the recursion |
| `grid[row][col] = 0` | **Undo**: the backtrack | Without this line the first wrong guess is permanent |

The last two rows are the pair to remember. A program that only ever assigns is a program that fails on its first mistake. Backtracking works because every assignment is provisional and the algorithm is willing to take it back.

Now read the counter. There are 51 blanks to fill, and the solver placed a digit 4,208 times. So roughly 4,157 of those placements were wrong and had to be taken back. The algorithm spent almost all of its effort on choices it later abandoned.

That is enormously better than the forty-nine-digit number of possible assignments, so backtracking is doing real work. It is also enormously worse than it needs to be.

![Visual explanation of backtracking search](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_backtracking_search_simple_v2.png)

## Making Backtracking Smarter

The solver above is wasteful for one specific reason: `first_empty` picks the next blank cell in reading order, which is an arbitrary choice made without looking at the puzzle at all.

Consider what a human solver does instead. Nobody fills a Sudoku top to bottom. They hunt for the cell with only one possible digit, write it in, and repeat. That instinct has a name in CSP work: the **minimum remaining values** heuristic, usually shortened to MRV. Always assign the variable with the fewest legal values left.

The reasoning behind it is worth stating properly, because it sounds backwards at first. You might expect the algorithm to start with easy, unconstrained variables. The opposite is correct. **A variable with few options is where failure will be discovered soonest.** If a cell has one candidate, there is nothing to guess. If a cell has zero candidates, the current assignment is already doomed, and finding that out now costs nothing, whereas finding it out after forty more placements costs all forty of them. MRV is sometimes called the fail-first principle, and failing fast is the entire point.

Reading the code below: `allowed` and the backtracking loop are unchanged. Two things are new: `fewest_candidates`, which is MRV, and a `pick_cell` argument on `solve` so the same search can be run with either choice. The final loop runs both and compares.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzke4h" 
 width="100%"
></iframe>

```
next blank cell in order       ->  4208 digits placed
cell with fewest candidates    ->    51 digits placed
```

Fifty-one. There are exactly fifty-one blank cells, so **MRV solved this puzzle with no backtracking at all.** Every digit it placed was correct and was never undone. A single change in which variable to try next, with the constraint checking and the search structure untouched, removed 4,157 wasted placements.

This is the payoff of the transparency mentioned earlier. A general search algorithm could not do this, because it cannot see inside a state to ask which variable is most constrained. A CSP solver can, and the gain is not marginal.

Three further refinements are standard, and all follow the same instinct of using visible structure.

- **The degree heuristic** breaks ties in MRV by choosing the variable involved in the most constraints on other unassigned variables, on the grounds that it will do the most to narrow the rest.
- **Least constraining value** decides, once a variable is chosen, which value to try first: the one that eliminates the fewest options for its neighbours, leaving the most room to succeed.
- **Forward checking and constraint propagation** go further still, removing values from other variables' domains the moment an assignment is made, so that a dead end is detected before the search ever descends into it.

![Visual explanation of csp backtracking mrv](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_csp_backtracking_mrv.png)

## The Same Machinery on a Timetable

The reason CSPs matter is that the formulation is general. Nothing in the algorithm knew what Sudoku was, so pointing it at Deepa's timetable requires no new algorithm, only a new set of variables, domains, and constraints.

Reading the code below: compare it against the Sudoku solver and you will find the same shape. `allowed` is different, because the constraints are different. `solve` is the same assign, recurse, undo pattern, with MRV built into the line that picks the next subject.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkerk" 
 width="100%"
></iframe>

```
Assignments tried: 5
  Mon 9am  : Biology, Maths
  Mon 11am : English, Physics
  Tue 9am  : Chemistry
```

Five assignments for five subjects, so again no backtracking. Three days of whiteboard work, done correctly, in the time it takes to press a key.

Compare this code with the Sudoku solver line by line and notice how little changed.

| Part | Sudoku | Timetable | Same? |
| --- | --- | --- | --- |
| Variables | Blank cells | Subjects | Different names, same role |
| Domain | Digits 1 to 9 | The available slots | Different values, same role |
| Constraint check | Row, column, box | Clashing pairs | **Different**, and this is the only real change |
| Variable choice | `fewest_candidates` | `min(remaining, key=...)` | The same MRV idea |
| Assign, recurse, undo | Three lines | Three lines | Identical |

**That reuse is the argument for learning the CSP formulation**: get a problem into this shape and a large body of existing technique applies to it immediately, with only the constraint check written fresh.

![Visual explanation of the same machinery on a timetable](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_the_same_machinery_on_a_timetable_simple_v2.png)

## CSPs at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In Sudoku</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the timetable</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Variables</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each empty cell</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each subject</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Domains</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Digits 1 to 9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Available time slots</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Constraints</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rows, columns, and boxes all differ</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clashing subjects get different slots</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Solution</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The completed grid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The completed schedule</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Effect of MRV</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4,208 placements down to 51</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5 assignments, no backtracking</td>
    </tr>
  </tbody>
</table>

![Visual explanation of csps at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_csps_at_a_glance.png)

## Your Turn

Take the timetable code and make it harder in two stages.

First, remove `"Tue 9am"` from `slots`, leaving only two. Before running it, work out by hand whether a clash-free timetable can still exist, using the clash list. Then run it and see whether the program agrees. Getting a definite "no solution exists" from a CSP solver is genuinely useful information, and notice that the solver establishes it by exhausting the possibilities rather than by understanding anything about timetables.

Second, restore the three slots and add a constraint that no slot may hold more than two subjects, because the college has only two rooms. This one is different in kind from the others: it is not a rule about a pair of subjects but a rule about how many share a value, so you will have to change `allowed` to count rather than compare. Work out where the count belongs, and you will have written your first global constraint.

Then answer the design question. Deepa's real college has 60 subjects, 30 slots, and hundreds of clash rules. Plain backtracking on Sudoku wasted 4,157 placements on a 51-variable problem. Reason about what that ratio would look like at ten times the size, and say why MRV stops being a nice optimisation and becomes the only reason the program finishes at all.

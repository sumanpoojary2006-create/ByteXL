## Background

A team inherits a module that calculates hostel mess bills. It works, and no one wants to touch it. A new developer is asked to add one rule, a holiday discount, and spends two days because the logic for a single bill is spread across a very long routine, three copies of the same rounding, and names such as `tmp2` and `flag`. The module is correct and still expensive.

Clean code is judged by the next change. This project asks you to judge a module from a description of it and to propose a review that a colleague could act on.

## What You Will Build

A code review report for the hostel bill module, working from the structural description below: smells found, the reasoning, a prioritised fix list and a set of review comments written kindly and specifically.

## Learning Objectives

By the end of this project, you will be able to:
- Name common smells and the cost each one imposes
- Prioritise fixes by the change they make easier
- Write review comments that are specific, reasoned and respectful
- Decide what not to change

**Difficulty:** Intermediate · **Estimated time:** 2 hours

## Starting Material

A description of the module, as a reviewer would see it:

| Observation | Detail |
|-------------|--------|
| Main routine | One routine of about 400 lines that reads the meter, applies rates, adds fines and prints the bill |
| Names | Variables called `tmp`, `tmp2`, `flag`, `x`; one routine called `doStuff` |
| Rounding | The same rounding rule is written out in five places, and one place rounds differently |
| Rate table | Hard-coded numbers such as 4.5 and 30 inside calculations, with no explanation |
| Comments | A comment says "add GST" above code that does not add GST |
| Tests | None |
| Recent history | Four changes in the last month, all in the main routine |

## Tasks

### Task 1: Find the Smells

1. For each observation, name the smell it shows and the problem it causes for the next developer.
2. Put the results in a table with the columns Observation, Smell, Cost.

### Task 2: Prioritise

1. Rank the problems by how much each one slows the planned holiday-discount change.
2. Choose the two you would fix first and justify the order.
3. Name one smell you would deliberately leave alone for now, and why.

### Task 3: Write the Review

1. Write six review comments. Each must state what you noticed, why it matters and what you suggest.
2. At least one comment must ask a question rather than give an order.
3. At least one must praise something that is done well, if you can find it.

### Task 4: Safety Before Change

1. Describe what you would put in place before touching the main routine, given there are no tests.
2. Explain why the rounding inconsistency must be settled with the finance office, not decided by the developer.

**Answer these questions after completing all tasks:**
- Which of your comments is most likely to be received as an attack, and how did you reword it?
- Why does the recent history in the table matter for deciding what to fix?
- What does "correct but expensive" mean in terms of the next four changes?

## Where to Build This Project

This project needs no software beyond a document editor. Write the report on your own device, or as a Markdown file in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

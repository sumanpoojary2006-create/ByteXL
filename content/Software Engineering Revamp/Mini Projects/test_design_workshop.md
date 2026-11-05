## Background

A scholarship portal accepts an application only if the student's family income is below a limit, the marks are at or above a cut-off, and the form is submitted before the deadline. The team tests it with five applications that all pass. On the last day, a student with marks exactly at the cut-off is rejected, because someone wrote "greater than" where the rule said "at least". The five tests never went near the boundary.

Good testing is the choice of a few cases that expose the most faults. This project gives you a rule set and asks you to choose those cases and defend the choice.

## What You Will Build

A test design for the scholarship eligibility rules: equivalence classes, boundary values, a decision table, and a final set of test cases with expected results.

## Learning Objectives

By the end of this project, you will be able to:
- Divide inputs into equivalence classes
- Choose boundary values on both sides of each limit
- Build a decision table for combined conditions
- Select a small set of cases that covers all rules

**Difficulty:** Intermediate · **Estimated time:** 2 hours

## Starting Material

| Rule | Detail |
|------|--------|
| Income | Family income must be below 300,000 per year |
| Marks | Marks must be at least 75 per cent, out of 100 |
| Deadline | Application must be received by 31 March, inclusive |
| Result | Eligible only if all three conditions are met; otherwise rejected, with the first failing reason shown in the order income, marks, deadline |

## Tasks

### Task 1: Equivalence Classes

1. For each of the three inputs, list the valid and invalid classes, including invalid cases such as negative income and marks above 100.
2. Choose one representative value for each class.

### Task 2: Boundaries

1. For income, marks and date, list the values just below, on, and just above each limit.
2. State which of these a "greater than" mistake would fail.

Expected result: for marks, the values 74, 75 and 76 are among those listed, and 75 is expected to be eligible if the other conditions are met.

### Task 3: Decision Table

1. Build a decision table with the three conditions and every combination of pass and fail.
2. Fill in the expected outcome and the reason shown for each of the eight rows.
3. Identify the row where two conditions fail and confirm which reason is shown.

### Task 4: The Test Set

1. Select the smallest set of test cases that covers every row of the decision table and every boundary.
2. Present them as a table with an ID, inputs, expected result and the technique that produced each.
3. Explain why your set is stronger than the five happy-path applications.

**Answer these questions after completing all tasks:**
- Which of your cases would have caught the "greater than" fault, and why would a typical case not?
- Eight combinations are possible. Which could you have skipped, if any, and what risk would that carry?
- What would you need to know before testing a deadline set in a different time zone?

## Where to Build This Project

This project needs no software beyond a spreadsheet or document editor. Present the final test set as a table on your own device, or in a Markdown file in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

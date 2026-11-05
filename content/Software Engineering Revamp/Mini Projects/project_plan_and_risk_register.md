## Background

A final-year team promises a hospital appointment portal in ten weeks. In week seven, one member falls ill, the payment sandbox turns out to need a business registration nobody has, and the testing that was "obviously going to be quick" has not started. The plan was one line: "ten weeks". Nothing in it said what could go wrong or what the team would do about it.

A plan is a set of beliefs about the future with the uncertainty written down. This project builds one.

## What You Will Build

A project plan for a ten-week appointment portal: work breakdown, three-point estimates, a critical path, and a risk register with responses.

## Learning Objectives

By the end of this project, you will be able to:
- Break a goal into tasks small enough to estimate
- Produce an estimate as a range rather than a single number
- Identify the critical path and the tasks with slack
- Write risks with a probability, an impact and a response

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Starting Material

| ID | Task | Depends on | Optimistic (days) | Likely (days) | Pessimistic (days) |
|----|------|-----------|-------------------|---------------|--------------------|
| A | Gather requirements | none | 3 | 5 | 10 |
| B | Design screens | A | 4 | 6 | 9 |
| C | Design data model | A | 2 | 3 | 6 |
| D | Build booking feature | B, C | 8 | 12 | 20 |
| E | Build payment feature | C | 6 | 10 | 25 |
| F | Integrate and test | D, E | 5 | 8 | 15 |
| G | Fix defects and release | F | 3 | 5 | 10 |

The team has four members and works five days a week.

## Tasks

### Task 1: Expected Durations

1. For each task, compute the expected duration as (optimistic + 4 x likely + pessimistic) divided by 6.
2. Record the results in a table and note which task has the widest gap between optimistic and pessimistic.

Expected result: task E has the widest spread, and its expected duration is higher than its likely value.

### Task 2: Critical Path

1. Draw the dependency network from the Depends on column.
2. Add up the expected durations along each path from A to G.
3. Name the critical path, state its total in working days, and state how many weeks that is.
4. Say which tasks have slack, and by how much.

### Task 3: Risk Register

1. Write at least six risks, including one about people, one about technology, one about the customer and one about the schedule.
2. For each, give a probability (low, medium, high), an impact (low, medium, high) and a one-line response.
3. Sort the register so the highest-exposure risks come first.
4. For the top two risks, name an early warning sign and an owner.

### Task 4: The Verdict

1. State whether ten weeks is realistic and give the range you would promise the customer.
2. List two scope items you would offer to cut first if the range slips.

**Answer these questions after completing all tasks:**
- Why is the sum of the likely durations a poor forecast of the finish date?
- Which risk in your register is also a hidden assumption in the table above?
- If the customer demanded the original ten weeks regardless, what would you change: scope, time, people or quality, and what would you refuse to change?

## Where to Build This Project

This project needs no software beyond a spreadsheet and a document editor. Use any spreadsheet for the estimates and the register, or a Markdown file in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

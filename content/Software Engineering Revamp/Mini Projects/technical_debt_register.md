## Background

A food-delivery team keeps saying "we will clean that up later". After two years, a change to the delivery fee takes three weeks, because the fee rule exists in eight places and nobody is sure which is authoritative. Each shortcut had a reason on the day. None was written down, so none was ever repaid.

Technical debt is manageable only when it is visible. This project asks you to make it visible and to decide which items deserve repayment first.

## What You Will Build

A technical debt register for a delivery app, with each item scored for interest and repayment cost, and a one-quarter repayment plan.

## Learning Objectives

By the end of this project, you will be able to:
- Classify debt as deliberate or accidental, prudent or reckless
- Estimate the interest an item charges on future work
- Rank repayment by return rather than by annoyance
- Present the case for repayment to a non-technical manager

**Difficulty:** Intermediate · **Estimated time:** 2 hours

## Starting Material

| ID | Item | Extra time it adds to each change | Changes per quarter touching it | Cost to fix (days) |
|----|------|-----------------------------------|---------------------------------|--------------------|
| D1 | Delivery fee rule duplicated in 8 places | 2 days | 5 | 12 |
| D2 | No automated tests for the payment flow | 1 day | 8 | 15 |
| D3 | Old library, no longer maintained, has a known weakness | 0 | 0 | 6 |
| D4 | Confusing names in the order module | 0.5 day | 10 | 4 |
| D5 | Screens built before the design system, inconsistent | 0.25 day | 6 | 20 |

## Tasks

### Task 1: Classify

1. Classify each item as deliberate or accidental, and prudent or reckless, with one sentence of reasoning.

### Task 2: Interest and Payback

1. Compute the interest per quarter for each item as extra time multiplied by changes.
2. Compute the payback period in quarters as the fix cost divided by the quarterly interest.
3. Present the results in a table.

Expected result: D1 charges 10 days a quarter and pays back in 1.2 quarters; D2 charges 8 days and pays back in about 1.9 quarters.

### Task 3: The Item the Numbers Miss

1. Explain why D3 shows no interest in the table and still may deserve first place.
2. Describe the kind of cost it carries, and how you would present it.

### Task 4: Plan

1. Choose the items for a quarter in which the team can spare 20 days for repayment.
2. State what you will not repay and why that is acceptable.
3. Write a three-sentence pitch to a manager who wants new features instead.

**Answer these questions after completing all tasks:**
- Which item would you be tempted to pay first because it annoys developers most, and what do the numbers say?
- What stops new debt from arriving as fast as you repay old debt?
- Which of the five was the cheapest to avoid in the first place?

## Where to Build This Project

This project needs no software beyond a spreadsheet and a document editor. Keep the register in a spreadsheet on your own device, or as a table in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

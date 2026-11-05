## Background

A college canteen loses about twenty minutes of every break to queues. A student team proposes a pre-order app. The first meeting with the canteen manager produces a list: "orders, payments, a menu, maybe offers, it should be fast". Six weeks later the team delivers a menu screen the manager never wanted and no way to mark an item as sold out, which is the thing the manager needed most. The words in the first meeting were never turned into requirements anyone could check.

Requirements engineering is the work of turning a wish into a statement that two people read the same way and a tester can verify.

## What You Will Build

A requirements pack for a canteen pre-order app: a stakeholder list, user stories with acceptance criteria, non-functional requirements with measurable limits, and a conflict log.

## Learning Objectives

By the end of this project, you will be able to:
- Identify stakeholders beyond the obvious user
- Write user stories that a tester can turn into a check
- Express a quality need as a number with a way to measure it
- Detect and resolve conflicting requirements

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Starting Material

Notes from the interview with the canteen manager, in the manager's own words:

| # | Statement |
|---|-----------|
| 1 | "Students should order before break and just collect." |
| 2 | "It must be fast." |
| 3 | "I need to switch an item off when it runs out." |
| 4 | "Pay online, but some students only have cash." |
| 5 | "My cook should see the orders in the order they come." |
| 6 | "No student should be able to see another student's order." |
| 7 | "Keep it simple, the cook is not good with phones." |

## Tasks

### Task 1: Stakeholders

1. List at least six stakeholders, including at least two who will never open the app.
2. For each, write one sentence on what they need and one on what they could block.

### Task 2: User Stories

1. Turn statements 1, 3, 4 and 5 into user stories in the form "As a ..., I want ..., so that ...".
2. Give each story at least two acceptance criteria written as a situation and an expected outcome, for example, a given state, an action and a visible result.
3. Mark each story as must, should or could, and justify the marking in a few words.

Expected result: every acceptance criterion could be checked by someone who has never met the manager.

### Task 3: Non-Functional Requirements

1. Rewrite statements 2, 6 and 7 as measurable requirements. "Fast" must become a number, a condition and a way to measure it.
2. Add two requirements the manager did not mention but the app clearly needs, for example, behaviour on the busiest day.

### Task 4: Conflicts and Gaps

1. Find at least two conflicts or tensions among the statements, for example between "pay online" and "cash only students".
2. For each, record both positions, a proposed resolution and the person who must approve it.
3. List three questions you would ask the manager in a second meeting.

**Answer these questions after completing all tasks:**
- Which of your acceptance criteria was hardest to make testable, and what did you change?
- Which stakeholder did you almost forget, and what would have gone wrong without them?
- Which "should" or "could" story would you cut first if the deadline halved, and why?

## Where to Build This Project

This project needs no software beyond a document editor. Build the pack as one document with a section per task, on your own device or as a Markdown file in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

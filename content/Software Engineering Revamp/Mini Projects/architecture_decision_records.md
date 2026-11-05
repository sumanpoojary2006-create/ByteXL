## Background

A start-up builds a ride-sharing app for a campus. In month two, one developer proposes splitting the system into twelve services. Another wants one deployable application. The argument runs for a week, and then someone leaves and the reasoning leaves with them. A year later, new joiners ask why the system is built as it is, and no one can say.

An architecture decision record is a short note that keeps the reason alive. This project asks you to make three decisions and record them in a way that survives the people who made them.

## What You Will Build

Three architecture decision records for a campus ride-sharing app, each comparing at least two options against stated quality goals, plus a one-page context summary.

## Learning Objectives

By the end of this project, you will be able to:
- State the quality goals that drive an architecture
- Compare options by their trade-offs rather than their popularity
- Record a decision with its context, consequences and review trigger
- Distinguish a reversible decision from one that is costly to undo

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Starting Material

| Item | Detail |
|------|--------|
| Users | 3,000 students, peaks at 8:30 and 17:30 |
| Team | 5 developers, no dedicated operations person |
| Budget | Very small, a single modest server to begin with |
| Needs | Live driver location, ride matching, payments, ratings |
| Quality goals, in priority order | Reliable at peak, easy to change, cheap to run, secure payments |

## Tasks

### Task 1: Context Summary

1. In half a page, describe the system, its users and the four quality goals.
2. Mark each quality goal as one the team will protect strongly or accept losing a little of.

### Task 2: Three Decisions

Write one record for each decision below. Each record has a title, status, context, options considered, decision, consequences and a review trigger.

1. One deployable application or several services.
2. How live driver location reaches the rider: the rider's app asks repeatedly, or the server pushes updates.
3. Whether to build payments yourself or use a payment provider.

Expected result: every record compares at least two real options, names at least one cost of the chosen option, and ends with a condition such as "revisit when peak load exceeds ..." that would reopen the decision.

### Task 3: Reversibility

1. For each decision, mark it as easy or hard to reverse and say why.
2. Reorder the three so that the hardest to reverse is decided first, and explain what that implies for how long the team should spend on it.

**Answer these questions after completing all tasks:**
- Which of your records would change if the team had a dedicated operations engineer?
- Which quality goal did you sacrifice most often, and was that intentional?
- A new developer reads only your "consequences" sections. What do they learn that the code alone would not tell them?

## Where to Build This Project

This project needs no software beyond a document editor. Keep the three records as separate sections, or as separate Markdown files in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus), so that the habit of storing them beside the work is practised.

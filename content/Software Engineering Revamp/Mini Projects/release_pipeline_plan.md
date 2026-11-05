## Background

A team ships updates to a student attendance app by copying files to a server on Friday evenings. One Friday, a developer forgets a configuration file, attendance stops saving, and nobody notices until Monday. Two hundred records are lost. The fix is not a more careful developer. It is a release process that makes the careless step impossible.

This project asks you to design that process on paper before anyone builds it.

## What You Will Build

A release pipeline plan for an attendance app: stages, the check at each stage, the branching approach, a rollout strategy and a rollback plan.

## Learning Objectives

By the end of this project, you will be able to:
- Arrange build, test, review and release into stages with clear gates
- Choose a branching approach and defend it for a team of this size
- Select a rollout method that limits the damage of a bad release
- Write a rollback plan that can be followed under stress

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Starting Material

| Item | Detail |
|------|--------|
| Team | 6 developers, 1 tester |
| Users | 4,000 students and 150 staff, heaviest use 9:00 to 10:00 |
| Current release | Manual, weekly, Friday evening |
| Past failures | Missing configuration, a change that broke the staff login, a slow database query |
| Constraint | Attendance must never be lost; a few minutes of read-only downtime is acceptable |

## Tasks

### Task 1: Map the Failures

1. For each past failure, name the earliest stage at which an automated check could have caught it.
2. Write the check in plain words.

### Task 2: Design the Pipeline

1. Draw the stages from a developer's change to production, with at least five stages.
2. For each stage, write what it checks, what happens when it fails and who is told.
3. Mark which stages are automatic and which need a person, and justify each person.

### Task 3: Branching

1. Choose a branching approach for six developers and explain why.
2. State how long a branch may live and what happens to one that lives longer.

### Task 4: Rollout and Rollback

1. Choose a rollout method, such as gradual exposure to a small group first, and state what you will watch during it.
2. Define the signal that stops the rollout and the signal that triggers a rollback.
3. Write the rollback plan as numbered steps that a tired person could follow.
4. Explain how the plan protects attendance data specifically, given that data changes may not roll back as easily as code.

**Answer these questions after completing all tasks:**
- Which stage in your pipeline would the team be most tempted to skip under deadline pressure, and how does your plan resist that?
- Why is Friday evening a poor release time, and what time would you choose?
- What would you change if the team grew to sixty developers?

## Where to Build This Project

This project needs no software beyond a document editor and a drawing tool. Build it as one document on your own device, or in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

## Background

A college library wants students to reserve study seats. The developers draw one large diagram with every class, every screen and every arrow, and nobody can read it. Another team draws nothing, and discovers in week five that the librarian and the system disagree about what happens when a student does not turn up.

Models are valuable when each one answers one question for one audience. This project asks you to choose the right diagram for each question.

## What You Will Build

A small model set for a library seat reservation system: a use case diagram, a class diagram, a sequence diagram and a state diagram, with a caption under each saying what question it answers.

## Learning Objectives

By the end of this project, you will be able to:
- Pick the diagram type that fits a question
- Keep each diagram to one level of detail
- Check diagrams against one another for consistency
- Explain a model to a person who did not draw it

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Starting Material

| Fact | Detail |
|------|--------|
| Actors | Student, Librarian, the college login system |
| Seats | 120, in three rooms, each with a seat number and a power socket flag |
| Reservation rule | A student may hold one reservation at a time, for up to 3 hours |
| No-show rule | If the student has not checked in 15 minutes after the start, the seat is released |
| Check-in | By scanning a code at the desk, handled by the librarian |
| Cancellation | Allowed any time before the start |

## Tasks

### Task 1: Use Cases

1. Draw a use case diagram with the three actors and at least six use cases.
2. Identify one use case that includes another and one that extends another, and write a line explaining each.

### Task 2: Classes

1. Draw a class diagram with at least five classes, their key attributes and the relationships with multiplicities.
2. Check that the one-reservation-at-a-time rule is visible in a multiplicity.

### Task 3: Interaction

1. Draw a sequence diagram for "student reserves a seat", from login to confirmation.
2. Add an alternative path for the case where the seat has just been taken.

### Task 4: Lifecycle

1. Draw a state diagram for a reservation, with the states Reserved, Checked in, Released, Cancelled and Completed.
2. Label every transition with the event and, where needed, a guard such as "15 minutes elapsed".

### Task 5: Consistency Check

1. List every name that appears in more than one diagram and confirm it is spelled identically in each.
2. Find one rule in the starting material that appears in no diagram and decide where it belongs.

**Answer these questions after completing all tasks:**
- Which diagram would you show the librarian, and which would you show a new developer, and why not swap them?
- Which detail did you leave out of the class diagram on purpose, and what made it safe to omit?
- What did the state diagram reveal that the sequence diagram did not?

## Where to Build This Project

Draw by hand and photograph the pages, or use any free diagramming tool. Collect the four diagrams and their captions into one document, on your own device or in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).

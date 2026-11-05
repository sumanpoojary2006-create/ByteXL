## Background

Every hostel has the same quiet failure. A tap leaks on Monday. The student tells the warden on Tuesday, the warden mentions it to the caretaker on Wednesday, the caretaker waits for a plumber who is booked until Friday, and by then the floor below has a damp ceiling and a second complaint. Nobody was lazy. The request simply passed through four people with no record, no owner, no deadline and no way for the student to see what had happened.

CareDesk is a proposed hostel maintenance request system for a residential campus of 2,400 students, 6 hostels and 18 maintenance staff. This capstone asks you to take it from a vague wish to a release-ready engineering package. You will not write a program. You will produce the artefacts that a real team produces before, during and after a programme is written, and you will show that they agree with one another.

The project draws on Units 1 to 15: the nature of software and the choice of process, requirements, planning, modelling, architecture and patterns, clean code, testing, release, maintenance, quality and security, verification and professional practice. Each stage adds a layer on top of the last, and later stages depend on the decisions you recorded earlier.

## Project Workspace

Keep one folder for the whole capstone, with one document per stage and a single file called `decisions.md` that records every important decision with the date, the options considered and the reason. Number every requirement (R1, R2, ...), every risk (K1, K2, ...), every test (T1, T2, ...) and every decision (D1, D2, ...), and refer to them by number in later stages.

The check at the end of the project is traceability: for any requirement, a reader should be able to find the design element that realises it, the test that checks it and the release step that delivers it. Gaps in that chain are the main thing assessed.

## Stages

### Stage 1: Scope and Process

1. Using the Reference Facts below, write a one-page scope statement that says what CareDesk will do in its first release and, just as importantly, what it will not do.
2. Name the stakeholders and the role each person plays in the team that builds it. Use at least the roles of product owner, developer, tester and operations support, and state who holds each in a team of five students.
3. Choose a software process for the project and defend the choice using the facts: customer availability, stability of requirements and the cost of a failure. Record it as decision D1.
4. List three trade-offs the project will have to make between scope, time, cost and quality, and state which one you will protect least.

### Stage 2: Requirements

1. Hold an imaginary interview with each of the four user groups listed below and write the notes you would expect to take.
2. Write at least 12 functional requirements as user stories with acceptance criteria, numbered R1 onwards. Cover reporting a fault, assigning it, updating its status, seeing its history, and closing it.
3. Write at least 6 non-functional requirements with measurable limits, covering response time, availability, privacy of student details, accessibility and the busiest hour.
4. Record at least three conflicts between stakeholders, such as wardens wanting to approve everything and students wanting urgent faults fixed immediately, with a proposed resolution and the person who decides.
5. Classify every requirement as must, should or could, and mark which fit the first release.

### Stage 3: Plan, Estimate and Risk

1. Break the first release into a work breakdown of at least 15 tasks with dependencies.
2. Estimate each task as optimistic, likely and pessimistic durations, compute the expected value, and find the critical path and the earliest finish date.
3. Compare your total with a rough estimate from the number of requirements and explain any difference.
4. Write a risk register of at least 8 risks, covering people, technology, customer, schedule and security. Give each a probability, an impact, an early warning sign, an owner and a response. Mark the two risks you would watch weekly.

### Stage 4: Model the System

1. Draw a use case diagram for the four user groups and the external systems.
2. Draw a class or domain model with at least 7 classes and their multiplicities. A request has exactly one reporter, at most one assigned technician at a time, and any number of status changes.
3. Draw a sequence diagram for "student reports a fault and it reaches a technician", including a path for a request that arrives while no technician is available.
4. Draw a state diagram for a request, with every state, event and guard. Decide what happens when a request is reopened.
5. Check the diagrams against one another and against the requirements, and fix any name or rule that differs between them.

### Stage 5: Architecture and Design

1. State the quality goals in priority order and justify the order.
2. Choose an architectural style for CareDesk and describe the main components and how they communicate. Draw one diagram at the level of components, not classes.
3. Write architecture decision records for at least three decisions: how notifications reach students, where the data is stored and who can see which request, and how the system connects to the existing student login.
4. Identify at least two places where a design pattern fits the problem, such as varying the way a notification is sent or keeping many parts informed when a status changes. Name the pattern, explain the problem it solves, and say what it costs.
5. Identify one place where a pattern would be over-engineering and explain why you will not use it.

### Stage 6: Code Quality Plan

No program is written in this project, so this stage sets the standard that a program would be held to.

1. Write a one-page coding standard covering naming, function size, comments, error handling and configuration.
2. Write a review checklist of at least ten items, and say which items a tool can check and which need a person.
3. Given the following description of an inherited module from the old complaint register, list the smells, rank them by how much they would slow your first change, and propose a refactoring sequence.

   | Observation | Detail |
   |-------------|--------|
   | Routine length | One routine of 600 lines handles saving, notifying and printing |
   | Duplication | The urgency rules appear in four places and disagree in one |
   | Naming | Fields called `st`, `st2` and `flag3` |
   | Tests | None |
   | Change history | Seven changes in two months, all in the 600-line routine |

### Stage 7: Test Strategy

1. Write a test strategy that states what is tested at each level (unit, integration, system and acceptance), by whom, and with what entry and exit conditions.
2. Using the rules below, design test cases with equivalence classes, boundary values and a decision table. Produce at least 20 numbered test cases with inputs, expected results and the requirement each one covers.
3. Plan the automated and the manual parts of testing, and justify which tests you would automate first.
4. Write a test plan for non-functional requirements, covering the busiest hour, accessibility and the privacy of student details.
5. Define what makes a defect a blocker, and write the criteria for declaring the first release ready.

### Stage 8: Build and Release

1. Design the release pipeline from a developer's change to production, with at least six stages, the check at each, and who is told on failure.
2. Choose a branching approach and a versioning rule, and explain both for a team of five.
3. Choose a rollout method for a campus where heavy use starts at 7:30 in the morning, and define the signal that stops it.
4. Write a rollback plan as numbered steps, including what happens to requests created after the release.
5. List the environments you need and what differs between them.

### Stage 9: Operate and Maintain

1. Define what you will monitor, the alert thresholds and who is paged.
2. Using the incident below, write a blameless postmortem with a timeline, causes, what went well and at least five owned actions.

   | Time | Event |
   |------|-------|
   | 07:25 | A release changes how urgent requests are ranked |
   | 07:30 | Morning peak begins; requests arrive at six times the normal rate |
   | 07:40 | Urgent requests stop reaching technicians; no alert fires |
   | 08:10 | A warden phones to say a flooded corridor has not been assigned |
   | 08:30 | The change is rolled back |
   | 09:00 | 41 urgent requests are found to have been left unassigned |

3. Classify five likely future changes as corrective, adaptive, perfective or preventive, and estimate the cost of each category over three years.
4. Create a technical debt register with at least five items, each with the extra time it adds to every change, the changes per quarter and the cost to fix, and compute the payback period for each.

### Stage 10: Quality, Security and Verification

1. Write a quality plan that names at least five quality attributes, how each is measured, and the target.
2. Build a threat model: list the assets, the actors who might attack them, at least eight threats, and a control for each. Include a student viewing another student's request and a technician seeing room numbers they do not need.
3. Write the security requirements as testable statements and add them to the numbered requirement list.
4. Choose three kinds of verification (for example peer review, static analysis and a walkthrough with wardens) and say what each would find that the others would not.
5. Describe how you would measure whether the finished system works, using at least three measures that are not about code.

### Stage 11: Professional Practice

1. Identify two ethical or legal issues in CareDesk, for example the retention of students' personal data and the use of request history to assess individual caretakers. For each, give the options and your recommendation.
2. Write a short data protection note stating what is collected, why, who can see it and how long it is kept.
3. Write the licence and ownership position for the project's documentation and artefacts.
4. Write a one-page handover note that a new maintainer could use on their first day.
5. Write a reflection of about 300 words on the decision you would most like to revisit, and what evidence would make you change it.

## Reference Facts

### Campus

| Fact | Detail |
|------|--------|
| Students | 2,400 across 6 hostels |
| Maintenance staff | 18: electricians, plumbers, carpenters, housekeeping |
| Wardens | 6, one per hostel |
| Existing process | Paper register at each warden's desk and phone calls |
| Existing login | The college login system, which CareDesk must use |
| Busiest period | 07:00 to 08:30 on weekdays, and the first week of each term |
| Budget | Very small; one modest server and free tools |
| Deadline | First release in 14 weeks |

### User Groups

| Group | Main need | Main worry |
|-------|-----------|-----------|
| Students | Report a fault quickly and see what happens to it | Being ignored, or being blamed for the damage |
| Wardens | See all open faults in their hostel | Losing authority to approve work |
| Technicians | Know what to fix, where and how urgent | Being tracked and ranked unfairly |
| Estate office | See costs and recurring faults | Budget overruns |

### Rules for Test Design (Stage 7)

| Rule | Detail |
|------|--------|
| Urgency | A request is urgent if it concerns water leakage, electrical sparks or a blocked exit |
| Response targets | Urgent: assigned within 15 minutes; normal: assigned within 1 working day |
| Escalation | An unassigned urgent request is shown to the warden after 15 minutes and to the estate office after 45 |
| Reopening | A closed request can be reopened by the reporter within 7 days |
| Attachments | At most 3 photos of at most 5 MB each |
| Duplicate reports | A second report for the same room and fault type within 24 hours is linked, not created |

## The Complete Picture

When all eleven stages are finished, you should be able to hand over the following, and every item should refer to the others by number.

| Artefact | Built in stage | Must trace to |
|----------|----------------|---------------|
| Scope statement and process decision | 1 | Decisions D1 onwards |
| Numbered requirements | 2 | Stakeholders, risks |
| Plan and risk register | 3 | Requirements, critical path |
| Models | 4 | Requirements |
| Architecture and decision records | 5 | Quality goals, models |
| Coding standard and review checklist | 6 | Quality plan |
| Test strategy and test cases | 7 | Each requirement |
| Release pipeline and rollback plan | 8 | Environments, test exit criteria |
| Monitoring plan, postmortem, debt register | 9 | Quality goals, risks |
| Quality plan and threat model | 10 | Security requirements |
| Ethics note and handover | 11 | All of the above |

Finish with a traceability table for five requirements of your choice, showing for each the user story, the model element, the design decision, the test cases and the release step. If you cannot fill a cell, you have found a gap. Say what it is and how you would close it.

**Answer these questions after completing all stages:**
- Which early decision turned out to be the most expensive to live with in later stages, and what evidence did you have at the time?
- The incident in Stage 9 should have been preventable at an earlier stage. Which stage would have caught it most cheaply, and which of your artefacts would have needed to change?
- Which requirement was hardest to trace from story to release, and what did that reveal about how it was written?
- If the deadline moved from 14 weeks to 9, what would you cut, and which of your recorded risks would grow?

## Where to Build This Project

This project needs no programming environment. Keep the folder of documents on your own device, or as Markdown files in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus), so that each stage sits beside `decisions.md` and the numbered references can be searched. Diagrams may be drawn by hand and photographed or made with any free diagramming tool.

## Introduction

Scrum is the most widely adopted agile framework. It is deliberately small: a handful of roles, events, and artifacts, with few rules. That simplicity is intended, because Scrum does not tell a team how to build software, only how to organise its work so that problems become visible quickly.

**Definition:** Scrum is a lightweight framework in which a small, cross-functional team delivers a usable product increment in fixed-length iterations called sprints, using defined roles, events, and artifacts to make progress transparent and to inspect and adapt regularly.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_scrum_roles_events_and_artifacts.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A circular sprint loop of one to four weeks with five event markers around it, three artifact icons in the centre, and three role figures outside labelled Product Owner, Scrum Master, Developers.

ON-IMAGE TEXT: show a short bold title "Scrum: Roles, Events and Artifacts" plus only these few labels, large and legible: Sprint, Roles, Artifacts. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Foundation: Empiricism

Scrum rests on **empiricism**: knowledge comes from experience, and decisions are based on what is observed. Three pillars support it.

- **Transparency.** The work and its state are visible to those who care about the outcome.
- **Inspection.** The team checks progress and results frequently to detect problems.
- **Adaptation.** When inspection shows a problem, the team adjusts promptly.

The Scrum Guide, written by Ken Schwaber and Jeff Sutherland, also names five values: commitment, focus, openness, respect, and courage.

## The Scrum Team: Three Accountabilities

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Accountable for</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Not responsible for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product Owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maximising the value of the product; managing and ordering the product backlog; deciding what is built and in what order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deciding how developers build it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scrum Master</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Helping the team and organisation understand and use Scrum; removing obstacles; coaching</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managing people or assigning tasks like a traditional project manager</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creating a usable increment each sprint; planning the sprint; holding one another to the Definition of Done</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Taking orders on how to do the work; they self-manage</td>
    </tr>
  </tbody>
</table>

The Scrum Team is small, usually ten or fewer people, and **cross-functional**: together it has all the skills needed to deliver the increment. "Developers" means everyone who builds the product, including testers and designers, not only programmers.

## The Sprint and the Five Events

The **sprint** is a fixed-length iteration of one month or less, during which a usable increment is created. All other events happen within it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Event</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical timebox</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The container: a short cycle producing a usable increment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One month or less, commonly two weeks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint Planning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide what can be done this sprint and how</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Up to 8 hours for a one-month sprint</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Daily Scrum</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspect progress toward the sprint goal and adjust the plan for the day</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15 minutes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint Review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspect the increment with stakeholders and adapt the product backlog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Up to 4 hours for a one-month sprint</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint Retrospective</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspect how the team worked and plan improvements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Up to 3 hours for a one-month sprint</td>
    </tr>
  </tbody>
</table>

A sprint is not extended when work is unfinished. Its length is fixed so that the team gets a regular rhythm and honest data on how much it can complete.

## The Three Artifacts and Their Commitments

Each artifact has a commitment that increases transparency.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Artifact</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Commitment</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product Backlog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An ordered list of everything known to be needed in the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product Goal: the long-term objective</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint Backlog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The items selected for the sprint plus a plan for delivering them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint Goal: the single purpose of the sprint</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A concrete, usable step toward the Product Goal, which includes all earlier increments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Definition of Done: the shared standard of completeness</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_scrum_framework_loop.png   (16:9 explanatory diagram, place here)

A circular diagram: Product Backlog on the left feeding into Sprint Planning, a loop labelled Sprint with a smaller loop labelled Daily Scrum inside it, leading to Sprint Review and Sprint Retrospective, and an Increment emerging on the right. Roles shown as three figures around the loop.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## How the Pieces Fit Together

The Product Owner orders the backlog. At Sprint Planning the team selects the top items it can complete, forming the Sprint Backlog with a Sprint Goal. During the sprint, the Developers work and use the Daily Scrum to stay aligned. At the Sprint Review, the team shows the Increment and stakeholders give feedback that shapes the backlog. At the Retrospective, the team improves its own way of working. Then the next sprint begins immediately.

## Common Errors in Practice

- The Scrum Master acts as a manager who assigns tasks.
- The Product Owner is a committee or is unavailable, so decisions are delayed.
- Sprints end without a usable increment, and unfinished work is carried over repeatedly.
- The retrospective is skipped when the team is busy, which removes the framework's improvement loop.

## Your Turn: Which Role or Event?

1. Someone decides which feature the team works on first.
2. The team discusses what went well and what to change in how it works.
3. The team shows the finished feature to stakeholders and collects feedback.
4. Someone helps the team resolve a blocker caused by another department.

Item 1 is the Product Owner. Item 2 is the Sprint Retrospective. Item 3 is the Sprint Review. Item 4 is the Scrum Master.

## Conclusion

Scrum is a lightweight framework in which a small, cross-functional team delivers a usable product increment in fixed-length iterations called sprints, using defined roles, events, and artifacts to make progress transparent and to inspect and adapt regularly. Its power comes from the rhythm and honesty it creates, not from its rules.

Having met the structure, the next topic looks more closely at the events themselves: how planning, daily check-ins, and retrospectives are run well.

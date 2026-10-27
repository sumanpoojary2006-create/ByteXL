## Introduction

Work is only useful when it is finished, and teams need a precise shared meaning of "finished." Without one, an item may be reported as complete while testing, integration, or release steps remain, so the work returns later as defects and delay. Agile addresses this with an explicit, shared Definition of Done, and with a firm rule that progress is measured by software that actually works.

**Definition:** The Definition of Done is a shared, written checklist of quality criteria that every item must satisfy before it counts as complete, ensuring that each increment of the product is genuinely usable and potentially releasable.

<!--
IMAGE PROMPT  ->  generate as images/19_intro_definition_of_done_and_working_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A checklist with ticks beside a finished feature card, and a gate labelled Done that only lets fully checked items pass through to a box labelled Releasable.

ON-IMAGE TEXT: show a short bold title "Definition of Done and Working Software" plus only these few labels, large and legible: Checklist, Gate, Releasable. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why "Done" Needs a Definition

Without a shared definition, teams count work as complete when it is only partly complete: the code exists, but it has not been reviewed, tested, integrated, or documented. These unfinished parts, called **undone work**, pile up silently. The team appears to move quickly, but the hidden remainder must be paid later, usually at the worst moment and with interest, since a release then needs a long stabilisation period.

## What a Definition of Done Contains

The content is decided by the team and the organisation, and grows stricter as the team matures. A typical list includes:

- the code is written and has been reviewed by another person
- automated tests were written and pass
- the change is integrated with the main version without breaking the build
- the acceptance criteria of the story are met and confirmed with the Product Owner
- non-functional criteria are met, such as performance or security checks
- documentation affected by the change is updated
- the software is deployed to a test environment and works there

## Definition of Done and Acceptance Criteria

The two ideas are related but distinct.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Acceptance criteria</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Definition of Done</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applies to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One specific story</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every story and the increment as a whole</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What this feature must do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality standards that all work must meet</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Written by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product Owner with the team, per story</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The team, possibly guided by organisational standards</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A user cannot rate the same meal twice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All code reviewed, tests passing, deployed to test environment</td>
    </tr>
  </tbody>
</table>

A story is done only when **both** are satisfied.

## Working Software and the Increment

In Scrum, each sprint must produce an **increment**: a concrete, usable step towards the product goal that meets the Definition of Done. The idea of "potentially releasable" is that the Product Owner could decide to release it immediately, whether or not they choose to. This is the meaning of the agile principle that working software is the primary measure of progress: it is demonstrated, not claimed.

<!--
IMAGE PROMPT  ->  generate as images/02_done_vs_undone_work.png   (16:9 explanatory diagram, place here)

Two side-by-side bars of the same height for Reported progress. On the left, a thin Done portion and a large hatched Undone work portion in orange, on the right a fully solid green Done portion. Labels: Without a Definition of Done, With a Definition of Done.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Relationship to Technical Debt

Each time a team relaxes its Definition of Done to meet a date, it takes on technical debt: quality work is deferred, and the cost shows up later as defects, slow changes, and risky releases. A strong definition protects against this. Teams under pressure should reduce the **scope** of what they deliver, not the **quality** of what counts as done.

## Evolving the Definition

A team starts with what it can achieve and strengthens the definition over time: adding automated testing, then security checks, then automatic deployment. The retrospective is a natural place to decide which criterion to add next.

## Your Turn: Is It Done?

A team's Definition of Done requires code review, passing automated tests, and deployment to a test environment.

1. A developer finishes a feature that works on their own machine and has no tests.
2. A feature is reviewed, tested, and deployed to the test environment, but the Product Owner has found that it does not satisfy one acceptance criterion.
3. A feature meets all criteria, but the team has decided not to release it yet.

Item 1 is not done: review, tests, and deployment are missing. Item 2 is not done: it meets the Definition of Done but fails an acceptance criterion, and both are required. Item 3 is done: it is potentially releasable, and releasing is a separate business decision.

## Conclusion

The Definition of Done is a shared, written checklist of quality criteria that every item must satisfy before it counts as complete, ensuring that each increment of the product is genuinely usable and potentially releasable. It is the main protection against hidden, unfinished work.

Agile practices work comfortably with one team. The next topic looks at what happens when many teams must work together, and what commonly goes wrong.

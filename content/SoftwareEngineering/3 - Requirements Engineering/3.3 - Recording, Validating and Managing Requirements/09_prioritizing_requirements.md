## Introduction

Almost no project can build everything requested. Budgets, deadlines, and team size are finite, and stakeholders always ask for more than can be delivered. Prioritisation is the practice of deciding which requirements matter most, so that limited effort goes to the work with the greatest value, and so that when the schedule tightens, the least important items are the ones that give way.

**Definition:** Requirements prioritisation is the process of ranking requirements by their importance, value, cost, and risk, using explicit criteria agreed with stakeholders, so that the most valuable work is done first and scope can be adjusted rationally.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_prioritizing_requirements.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A pile of requirement cards being sorted onto a rack of shelves labelled Must, Should, Could, Will not, with a small scale weighing Value against Cost.

ON-IMAGE TEXT: show a short bold title "Prioritizing Requirements" plus only these few labels, large and legible: Value, Cost, Order. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why "Everything Is High Priority" Fails

When every requirement is labelled urgent, the label carries no information. Teams then guess, the loudest stakeholder wins, and important work is dropped by accident. Prioritisation forces explicit trade-offs and makes scope decisions visible instead of leaving them to chance.

## Criteria for Prioritising

- **Business value:** how much the requirement contributes to the goals of the project.
- **Cost and effort:** how expensive it is to build.
- **Risk:** the chance that it will be hard, or that building it will reveal problems.
- **Urgency:** whether a date, regulation, or competitor forces timing.
- **Dependencies:** whether other requirements cannot proceed until this one is done.
- **User impact:** how many users and how strongly it affects them.
- **Cost of delay:** what is lost for each week the requirement is not delivered.

## MoSCoW

A simple and widely used scheme sorts requirements into four classes for a given release.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Class</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Test</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must have</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Essential; the release has failed without it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Would the release be illegal, unsafe, or pointless without it?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Should have</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Important, but a workaround exists and the release is still usable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Painful to omit, but possible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Could have</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Desirable; included if time and budget allow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nice to have</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Will not have (this time)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agreed to be out of scope for this release, possibly later</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recorded so that it is not forgotten</td>
    </tr>
  </tbody>
</table>

A common guideline is to limit the Must items to about 60 percent of the planned effort, so that there is room to absorb problems.

## Value Versus Cost

Plot requirements on a simple grid of value against cost. High-value, low-cost items are done first. High-value, high-cost items are planned carefully and may be split. Low-value, low-cost items fill spare capacity. Low-value, high-cost items are usually dropped.

## The Kano Model

Noriaki Kano proposed that features affect satisfaction in different ways.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect if present</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect if absent</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Basic (must-be)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Taken for granted; no extra delight</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong dissatisfaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An order system that correctly records orders</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance (one-dimensional)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More is better; satisfaction grows steadily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Satisfaction falls steadily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Faster response times</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Excitement (delighters)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unexpected pleasure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No complaint, because it was not expected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A prediction of waiting time at the counter</td>
    </tr>
  </tbody>
</table>

The model reminds teams that basics must be right before delighters can matter, and that delighters of today become the basics of tomorrow.

## Minimum Viable Product

A **minimum viable product (MVP)** is the smallest version of a product that delivers real value to users and allows the team to learn from them. Prioritising for an MVP means asking what is the least that must exist to test the central idea. It is a way of reducing the risk of building the wrong thing.

## Doing It Well

- **Agree the criteria first**, with the stakeholders, so the ranking is not a popularity contest.
- **Involve the right people:** business value from users and sponsors, cost from developers.
- **Prioritise a manageable number of items** at a time, grouping small items.
- **Revisit regularly.** Priorities change as knowledge and the world change.
- **Make the result visible**, including what has been left out and why.

<!--
IMAGE PROMPT  ->  generate as images/02_value_cost_grid_and_moscow.png   (16:9 explanatory diagram, place here)

Left: a two-by-two grid with Value on the vertical axis and Cost on the horizontal axis, quadrant labels Do first, Plan carefully, Fill-in, Avoid. Right: four stacked bars Must, Should, Could, Will not with the Must bar around 60 percent of the total.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify and Order

For a food-ordering app's first release, classify each requirement with MoSCoW.

1. Customers can place an order and pay.
2. Customers can rate meals afterwards.
3. The app shows a live map of the delivery rider.
4. Payment data must be handled in line with legal rules.

Requirement 1 is a Must have: without it the product has no purpose. Requirement 4 is also a Must have, because it is a legal obligation. Requirement 2 is a Should have, valuable but not essential for the first release. Requirement 3 is a Could have, or a Will not have this time, since it is costly and not essential to the first release.

## Conclusion

Requirements prioritisation is the process of ranking requirements by their importance, value, cost, and risk, using explicit criteria agreed with stakeholders, so that the most valuable work is done first and scope can be adjusted rationally. Open, criteria-based priorities protect both the product and the relationships around it.

Once the right requirements are chosen, they must be written down in a form that everyone can rely on. The next topic describes the software requirements specification.

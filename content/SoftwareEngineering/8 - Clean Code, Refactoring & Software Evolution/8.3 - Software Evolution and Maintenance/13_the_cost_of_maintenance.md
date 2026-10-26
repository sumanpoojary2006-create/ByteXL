## Introduction

Organisations plan carefully for the cost of building a system and often forget that the largest bill arrives after delivery. Over a system's life, the effort spent changing and supporting it commonly exceeds the effort of the first development by a wide margin. This has large consequences: decisions made during development, about structure, tests, and documentation, have a long tail of cost, and a design that is cheap to build but expensive to change can be a poor bargain.

**Definition:** The cost of maintenance is the total effort and expense of operating, supporting, correcting, adapting, and enhancing software after its first release, and it depends strongly on how maintainable the software is, which is determined by its structure, tests, documentation, and the knowledge of the people who work on it.

<!--
IMAGE PROMPT  ->  generate as images/13_intro_the_cost_of_maintenance.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: An iceberg: a small visible tip above the waterline labelled Initial development, and a very large submerged mass labelled Maintenance, with smaller labels for fixes, adaptation, enhancement, support, and operation.

ON-IMAGE TEXT: show a short bold title "The Cost of Maintenance" plus only these few labels, large and legible: Tip, Bulk, Long tail. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## How Large Is It?

Surveys and studies since the 1970s have repeatedly reported that maintenance takes a large share of the lifetime cost of software. Robert Glass summarises studies suggesting that maintenance consumes **between 40 and 80 percent** of software costs, with most of it spent on enhancements rather than fixes. The exact figure depends on the type of system, its lifetime, and how costs are counted, but the message is stable: **for software that lives for many years, maintenance is the dominant cost.**

Costs also include operation: servers, licences, monitoring, support staff, and security, which together are the **total cost of ownership**.

## What Drives the Cost

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect on cost</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Age of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Older systems accumulate structural decay and obsolete technology</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size and complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More code and more interactions mean more to understand before every change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality of design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tight coupling and poor structure spread the effect of each change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code readability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard-to-understand code slows every task</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test coverage and automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Without tests, each change needs extensive manual checking and carries risk</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing or outdated documentation forces rediscovery</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge and turnover</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When the original authors leave, understanding is lost</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rate of change of requirements and environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More change means more maintenance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies on external systems and platforms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each dependency can force changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The accumulated interest on earlier shortcuts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tooling and process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow builds, manual releases, and weak automation add effort to every change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support demands</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The volume of users and issues to be handled</td>
    </tr>
  </tbody>
</table>

## Measuring Maintainability

Maintainability can be estimated with indicators.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Indicator</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it shows</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity and size measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How hard code is to understand</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many places must change together</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coupling and dependency measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How far a change will spread</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test coverage and test reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How safely changes can be made</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability indices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite scores combining several measures, such as the index proposed by Oman and Hagemeister, to be used as rough guides</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long typical changes take, and how this trend moves</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect rates after change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether changes introduce new problems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time for a newcomer to become productive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well knowledge is captured</td>
    </tr>
  </tbody>
</table>

Direct measures of effort, such as the average time to complete a change of a given size, are often more honest than any computed index, and a rising trend is a clear warning.

## The Cost of Change Curve

For decades it was taught that the cost of changing software rises steeply as development proceeds: cheap in requirements, costlier in design, much costlier after release. Kent Beck argued that modern practices, such as automated tests, continuous integration, refactoring, and small releases, can **flatten the curve**, so that changes remain affordable late. The claim is not that change becomes free, but that investment in these practices keeps the cost of change from growing out of control.

## Reducing the Cost

1. **Design for maintainability from the start,** with modularity, low coupling, and clear structure.
2. **Write readable code** and follow standards.
3. **Maintain automated tests,** the most powerful single contributor to cheap change.
4. **Automate build, test, and release,** removing repeated manual effort.
5. **Document what matters,** and keep it current.
6. **Share knowledge** through reviews, pairing, and rotation, reducing dependence on individuals.
7. **Manage technical debt** continuously.
8. **Keep dependencies and platforms current,** rather than leaving large, risky upgrades.
9. **Reduce what you maintain:** remove unused features and code, and prefer simple solutions.
10. **Track and review** maintenance effort, to decide when to invest in repair or replacement.

## Costs and Decisions

Estimates of lifetime cost support decisions such as:

- **Build or buy:** building creates a permanent maintenance obligation, whereas buying shifts part of it to a supplier but adds licence and integration costs.
- **Repair or replace:** when the cost of continuing to maintain a system exceeds the cost of a replacement over a sensible period, replacement or modernisation is justified.
- **How much to invest in quality now:** extra effort in design and tests is repaid through lower maintenance cost, in proportion to the expected lifetime.
- **Which features to build at all:** every feature adds to the maintenance load for the rest of the system's life.

<!--
IMAGE PROMPT  ->  generate as images/02_lifetime_cost_stack_and_drivers.png   (16:9 explanatory diagram, place here)

Left: a stacked bar of lifetime cost with a thin lower segment Initial development and a much larger upper segment Maintenance and operation. Right: a list of cost drivers with arrows up or down: Test coverage (reduces), Documentation (reduces), Coupling (increases), Turnover (increases), Technical debt (increases).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Cost Driver

1. Every release requires two days of manual checking because there are no automated tests.
2. The only developer who understood the billing module has left the company.
3. A team wants to add a rarely used feature that nobody has asked for, "just in case."

Case 1 shows a cost driver in missing test automation, which makes every change expensive. Case 2 is knowledge loss, which raises the cost of every change to that module. In case 3, the feature would add to maintenance cost for the remaining life of the system with no evident benefit.

## Conclusion

The cost of maintenance is the total effort and expense of operating, supporting, correcting, adapting, and enhancing software after its first release, and it depends strongly on how maintainable the software is, which is determined by its structure, tests, documentation, and the knowledge of the people who work on it. Since maintenance usually dominates lifetime cost, investment in maintainability is among the most economical choices a team can make.

Before any change is made, its effects must be understood. The next topic describes change impact analysis.

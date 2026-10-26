## Introduction

Requirements change. Business conditions shift, users learn what they really need, competitors act, laws are updated, and technology offers new options. A project that treats change as an unusual event is surprised by it constantly. A project that treats change as normal, and manages it, can respond without losing control of scope, cost, and quality.

**Definition:** Requirements change management is the set of practices for proposing, assessing, approving, implementing, and recording changes to requirements, so that the project can respond to genuine needs while keeping scope, schedule, cost, and quality under control.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_managing_changing_requirements.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A gate labelled Change control with incoming change request cards on the left, an analysis step in the centre, and approved changes passing to a baseline on the right while some are held back.

ON-IMAGE TEXT: show a short bold title "Managing Changing Requirements" plus only these few labels, large and legible: Request, Assess, Decide. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Requirements Change

- **Business changes:** new strategy, competitors, markets.
- **Understanding grows:** users see early versions and discover what they need.
- **External changes:** regulation, standards, partner systems.
- **Errors found:** requirements were wrong, missing, or misunderstood.
- **Technology changes:** a new capability or a constraint appears.
- **Stakeholder changes:** new people bring new views.

The rate of change is called **requirements volatility**. High volatility is not necessarily a sign of failure but it needs a process able to absorb it.

## Scope Creep

Scope creep is the uncontrolled growth of a project's scope through many small additions, each seeming reasonable, none formally assessed. It arises when there is no clear baseline, when requests are accepted informally, or when nobody states the cost of a change. The remedy is not to refuse change but to make it **visible and deliberate**: each addition is assessed and traded against schedule, cost, or other scope.

## A Change Control Process

A typical process, which can be lighter or heavier according to the project, has these steps.

1. **Request.** Someone submits a change request describing the change and the reason.
2. **Analyse impact.** Estimate the effects on other requirements, design, code, tests, schedule, cost, and risk.
3. **Decide.** An authority, such as the Product Owner or a change control board, accepts, rejects, defers, or asks for more information.
4. **Implement.** Update the requirements, design, code, and tests.
5. **Record and communicate.** Update the specification and inform everyone affected.
6. **Verify.** Confirm the change was implemented and nothing else broke.

## Impact Analysis

Before approving a change, the team asks what it touches. Traceability makes this possible: following the links from a requirement shows the related designs, code modules, and tests. Questions include:

- Which other requirements depend on or conflict with this one?
- Which components must change?
- Which tests must be written or rerun?
- What is the effort, and what must be dropped or delayed to make room?
- What new risks does the change introduce?

## Baselines and Versioning

A **baseline** is an agreed version of the requirements that serves as the reference point. Changes to a baselined requirement go through change control. Each requirement and document has a **version**, a history of what changed, when, why, and who approved it. This history answers later disputes and supports audit.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unique identifiers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refer to a requirement unambiguously across versions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show what changed, when, and why</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Baseline at milestones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide a stable reference and a point to return to</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Status tracking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record whether each requirement is proposed, approved, implemented, verified, or dropped</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single source of truth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid conflicting copies of the requirements</td>
    </tr>
  </tbody>
</table>

## Change in Agile Projects

Agile methods welcome change but still manage it. The product backlog is the single place where changes appear, the Product Owner decides on priorities, and sprint scope is protected during a sprint so that the team can finish what it started. Changes enter at planning boundaries, which keeps flexibility without chaos. The same questions of impact and trade-off apply: adding an item means something else moves down.

## Reducing the Cost of Change

- **Involve stakeholders early and often**, so misunderstandings surface early.
- **Deliver in small increments** so feedback comes quickly.
- **Design for change** by hiding decisions likely to change behind stable interfaces.
- **Maintain automated tests** so that changes can be made with confidence.
- **Keep requirements and traceability current**, so impact can be judged quickly.

<!--
IMAGE PROMPT  ->  generate as images/02_change_control_flow.png   (16:9 explanatory diagram, place here)

A flow from Change request to Impact analysis to Decision, with three exits: Accept (to Implement and update baseline, green), Defer (to Backlog, orange), Reject (red). A traceability link icon feeds into Impact analysis.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Handle the Request

Midway through a project, a stakeholder asks for a new report that was not in scope.

1. List two questions you would ask before deciding.
2. Name three possible outcomes of the decision.

Useful questions include: what need does the report meet and how important is it, which data and components does it depend on, what effort will it take, and what must be dropped or delayed if it is added. Possible outcomes are to accept it and adjust the plan, to defer it to a later release, or to reject it. A fourth is to accept a simpler version that meets most of the need at lower cost.

## Conclusion

Requirements change management is the set of practices for proposing, assessing, approving, implementing, and recording changes to requirements, so that the project can respond to genuine needs while keeping scope, schedule, cost, and quality under control. Change is not the enemy: uncontrolled change is.

This completes Unit 3. You now know what requirements are, how stakeholders are identified and consulted, how needs are elicited and written as use cases, stories, and statements, how they are analysed, prioritised, specified, validated, and traced, and how change is managed. Unit 4 turns from what to build to how to describe it, beginning with modelling software with UML.

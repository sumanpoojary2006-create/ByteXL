## Introduction

No process is best for every project, and a method that suits a small web product may be unsuitable for flight software. Choosing well is part of engineering judgement: it means looking at the characteristics of the project and its context, then selecting and tailoring an approach to fit, instead of adopting whatever is popular.

**Definition:** Choosing a process is the decision, made from a project's size, risk, uncertainty, regulation, team, and customer involvement, about which activities, ordering, and controls will organise the work, and it should be revisited as the project's circumstances change.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_choosing_a_process_for_a_project.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A decision flowchart with five criteria diamonds, Size, Risk, Uncertainty, Regulation, Customer, leading to three outcomes labelled Plan-driven, Hybrid, Agile.

ON-IMAGE TEXT: show a short bold title "Choosing a Process for a Project" plus only these few labels, large and legible: Criteria, Fit, Tailor. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Factors to Consider

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question to ask</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Points towards plan-driven if...</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Points towards agile if...</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirement stability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How likely are requirements to change?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They are fixed and well understood</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They are unclear or expected to evolve</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost of failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the harm if it goes wrong?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lives, large sums, or legal exposure are at stake</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failures are cheap and quickly fixed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must you prove compliance?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External standards demand documented evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few formal obligations apply</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size and complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many people and parts?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very large, many dependent subsystems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small to medium, one team</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can users take part throughout?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer is distant or contract-bound</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer can give frequent feedback</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team experience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are people skilled in the approach?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team is experienced with structured methods</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team is self-organising and skilled</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technology novelty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well is the technology known?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Well known and stable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Novel, so learning is needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contract type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How is the work paid for?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed scope and price</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexible scope, time and materials, or product budget</td>
    </tr>
  </tbody>
</table>

## From Factors to a Decision

A simple, repeatable approach is to score the project on each factor, look at the overall pattern, and select a starting point.

- If most answers point to stable requirements, high criticality, and regulation, begin with a **plan-driven** model such as V-model, and add feedback loops where possible.
- If most answers point to uncertainty, accessible customers, and low failure cost, begin with an **agile** approach.
- If the signals are mixed, use a **hybrid**: for example, plan the architecture, safety analysis, and compliance evidence up front, then develop features in iterations.

## Tailoring and Hybrids

Real projects rarely match a textbook model. Teams **tailor** a process by choosing which parts to keep, adjust, or drop. Typical hybrids include:

- agile delivery within an overall stage-gated plan, used in many large organisations
- a fixed architecture and compliance phase followed by iterative feature development
- different approaches for different parts of one system, such as agile for the user interface and plan-driven for a safety-critical controller

The test of any tailoring is whether it serves the project's goals, not whether it is faithful to a book.

## Revisiting the Choice

Process decisions are not permanent. A project may start with exploration and prototypes while uncertainty is high, then settle into a more predictable rhythm as the product matures. Regular **retrospectives**, discussed in the agile topics, are a mechanism for noticing that the process no longer fits and adjusting it.

## Common Mistakes

- **Copying what is popular.** Adopting a method because competitors use it, without checking fit.
- **Adopting a label, not the practice.** Calling the work agile while keeping all the old approvals and hand-offs.
- **One size for everything.** Using the same heavy process for a trivial project, or none for a critical one.
- **Never reflecting.** Failing to review whether the process helps.

## Your Turn: Recommend a Starting Point

1. A team of six builds an internal tool for colleagues who are available daily and whose needs change weekly.
2. A company develops software for railway signalling, certified against safety standards.
3. A consultancy builds a customer portal with a fixed legal reporting component and a flexible user interface.

Project 1 starts agile because feedback is available and needs change. Project 2 starts with a plan-driven, V-model-style approach because of safety certification and the cost of failure. Project 3 suits a hybrid: plan and document the fixed reporting component, and develop the interface iteratively.

## Conclusion

Choosing a process is the decision, made from a project's size, risk, uncertainty, regulation, team, and customer involvement, about which activities, ordering, and controls will organise the work, and it should be revisited as the project's circumstances change. Tailoring to fit is a sign of maturity, not of inconsistency.

Organisations also want to improve their processes systematically over time. The next topic introduces process improvement and the maturity models used to measure it.

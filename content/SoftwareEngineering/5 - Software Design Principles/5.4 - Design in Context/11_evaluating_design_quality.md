## Introduction

Teams are often confident about their designs until the first serious change or failure. Evaluating a design before and during construction gives an earlier, cheaper warning. But design quality cannot be read from a single number. It depends on the goals of the system, and on trade-offs that no metric can settle alone. Evaluation combines structured review, evidence from experiments, and a small set of useful measures.

**Definition:** Evaluating design quality is the practice of assessing a design against its requirements and quality goals, using reviews, scenarios, measurements, and experiments, to find weaknesses and trade-offs before they become costly to repair.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_evaluating_design_quality.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A design diagram placed on a table with four inspection tools around it: a checklist, a magnifying glass, a measuring gauge, and a stopwatch, each pointing at part of the diagram.

ON-IMAGE TEXT: show a short bold title "Evaluating Design Quality" plus only these few labels, large and legible: Review, Measure, Test. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Fit for Purpose First

A design is good if it **meets its requirements and quality goals at acceptable cost**. A design for a student project and one for a hospital system should be judged by different standards. Begin evaluation by restating the goals: which functions, which quality attributes, which constraints, and which changes are expected. Without them, there is nothing to judge against.

## Methods of Evaluation

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it involves</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People other than the author examine the design using a checklist and discuss problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finding flaws, misunderstandings, and missing cases early</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scenario-based evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Walk through concrete situations, such as a new feature request or a failure, and see how the design copes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing modifiability, reliability, and security qualities</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture trade-off analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A structured method that links quality goals to design decisions, risks, and trade-offs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Significant architectural decisions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prototype or spike</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a small experiment to test a risky idea or measure performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reducing technical uncertainty</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics and static analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure structural properties of design or code with tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spotting hotspots and trends</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Walkthrough with the requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trace each requirement through the design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checking completeness</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review of change history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspect which parts change most and which change together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finding real coupling in an existing system</td>
    </tr>
  </tbody>
</table>

## What to Look for in a Review

Questions that structure a design review include:

- **Requirements:** Does the design satisfy every functional and quality requirement? Is each requirement traceable to a design element?
- **Structure:** Is it divided sensibly? Are modules cohesive and loosely coupled? Are dependencies one-directional?
- **Interfaces:** Are they minimal, clear, and documented?
- **Change:** How would the likely changes be handled?
- **Failure:** What happens when a component, network, or external service fails?
- **Performance and scale:** Can it meet load targets, and where are the bottlenecks?
- **Security:** Where are the trust boundaries, and how is data protected?
- **Simplicity:** Is any part more complicated than the problem requires?
- **Risks and assumptions:** What is assumed, and what would invalidate the design?

## Measures of Structure

Several measures help to look at structure objectively. They indicate where to look, not what is right.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it indicates</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Caution</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coupling between modules (for example, the number of other modules a module depends on)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How far a change might spread</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High values are warnings, not proof of a defect</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cohesion measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the contents of a module relate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to measure automatically; human judgement is needed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size of modules and functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether units are too large to understand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size alone does not indicate quality</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity of control flow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many paths a function has, and so how hard it is to test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Useful for hot spots, as a later unit explains</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency cycles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether modules cannot be understood or changed separately</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cycles are almost always worth fixing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change frequency and co-change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which parts change often and which change together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows real behaviour of the codebase over time</td>
    </tr>
  </tbody>
</table>

Measures are subject to **Goodhart's law**: when a measure becomes a target, it ceases to be a good measure. Teams that are rewarded for a number will optimise the number. Use measures to start conversations.

## Design Smells

Experienced developers also recognise symptoms of a deteriorating design. Robert C. Martin named four.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rigidity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small change forces many other changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fragility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change breaks things that seem unrelated</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Immobility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Useful parts cannot be reused because they are entangled with the rest</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Viscosity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It is easier to make a quick hack than to do the right thing</td>
    </tr>
  </tbody>
</table>

Other familiar signs are very large modules, circular dependencies, modules that know too much about one another, and the same change being made repeatedly in many places.

## Trade-offs and Documenting Decisions

Because quality attributes compete, evaluation should end with an honest list of trade-offs: what the design favours, what it gives up, and why. Writing these as short **decision records**, stating the context, options considered, decision, and consequences, preserves reasoning for later readers and helps the team revisit decisions when circumstances change.

## Evaluation Is Continuous

Evaluating a design is not a single gate. Early reviews catch large errors cheaply. Prototypes address risk. Reviews of code and structure continue throughout development. Retrospectives and the history of real changes reveal how the design actually behaves, which is more reliable than prediction.

<!--
IMAGE PROMPT  ->  generate as images/02_design_review_checklist_and_smells.png   (16:9 explanatory diagram, place here)

Left: a design review checklist with eight ticked items labelled Requirements, Structure, Interfaces, Change, Failure, Performance, Security, Simplicity. Right: four smell icons labelled Rigidity, Fragility, Immobility, Viscosity as warning signs.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Diagnose the Design

1. Every time the receipt format changes, six modules must be edited.
2. A fix in the payment code unexpectedly breaks the menu screen.
3. A team wants to know how a design copes with a new payment provider being added. Which method suits?

Case 1 shows rigidity and scattered responsibility. Case 2 shows fragility and hidden coupling. For case 3, scenario-based evaluation suits: walk through the scenario of adding a provider and count the modules affected.

## Conclusion

Evaluating design quality is the practice of assessing a design against its requirements and quality goals, using reviews, scenarios, measurements, and experiments, to find weaknesses and trade-offs before they become costly to repair. Judgement, grounded in the goals of the system, matters more than any number.

One aspect of design deals directly with people. The final topic of this unit introduces user interface and user experience design.

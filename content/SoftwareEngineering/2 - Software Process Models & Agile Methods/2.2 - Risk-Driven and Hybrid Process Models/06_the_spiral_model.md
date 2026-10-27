## Introduction

Every project carries uncertainty: requirements may be misunderstood, technology may not perform, schedules may slip, and key people may leave. Earlier models treated these uncertainties as incidental. The spiral model puts them at the centre by asking, in each cycle, what could go wrong and what should be done about it before more is built.

**Definition:** The spiral model is a risk-driven process model in which development proceeds through repeated cycles, each of which sets objectives, identifies and resolves the main risks, builds and tests, and plans the next cycle, so that effort is directed to the greatest uncertainties first.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_the_spiral_model.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A spiral expanding outward from a centre point, divided into four labelled quadrants repeated on each loop: Objectives, Risks, Build and Test, Plan Next.

ON-IMAGE TEXT: show a short bold title "The Spiral Model" plus only these few labels, large and legible: Risk, Cycle, Plan. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

Barry Boehm proposed the spiral model in the mid-1980s, drawing on experience with large, expensive projects where a single bad assumption could waste years. It combines the iterative nature of prototyping with the controlled, systematic aspects of sequential models, and adds explicit risk analysis.

## The Four Quadrants of Each Cycle

Each loop of the spiral passes through four steps. Progress outward represents growing cost and a more complete system.

1. **Determine objectives, alternatives, and constraints.** What must this cycle achieve? What options exist, and what limits apply?
2. **Evaluate alternatives and resolve risks.** Identify the biggest uncertainties and reduce them, using prototypes, simulations, benchmarks, or analysis.
3. **Develop and verify the next level of the product.** Build and test what the cycle was meant to produce.
4. **Plan the next cycle.** Review the results with stakeholders, decide whether to continue, and plan the next loop.

<!--
IMAGE PROMPT  ->  generate as images/02_spiral_four_quadrants.png   (16:9 explanatory diagram, place here)

A spiral with three loops growing outward through four quadrants. Quadrants labelled Objectives (top left), Risk analysis (top right), Develop and test (bottom right), Plan next cycle (bottom left). A small cost arrow grows with each loop.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## What Counts as a Risk?

A risk is an uncertain event that, if it occurs, harms the project. Each risk can be described by its likelihood and its impact.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical risk-reducing action</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users may not actually want the planned feature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a prototype and test it with users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new technology may be too slow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run a small benchmark before committing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dependency on another team may arrive late</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree dates early, plan an alternative</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personnel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single expert holds critical knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share the knowledge, document, pair on the work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A regulation may change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolate the affected part of the design</td>
    </tr>
  </tbody>
</table>

## Risk Decides What Comes Next

The central rule is that the next step should address the biggest risk. If the main uncertainty is whether users will accept the interface, build an interface prototype first. If it is whether the system can handle the expected load, test the architecture under load first. If risks are low, the project can proceed with simpler, more conventional steps. This is why the spiral is sometimes called a **process model generator**: the sequence of activities is chosen from the risks, not fixed in advance.

## Strengths and Limitations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focuses effort on the real uncertainties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs genuine risk-analysis expertise, which is not always available</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allows early, cheap abandonment of doomed projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can feel complex and heavyweight for small projects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combines prototyping and structured control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to use with fixed-price contracts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works well for large, novel, or expensive systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total cost and schedule remain uncertain at the start</td>
    </tr>
  </tbody>
</table>

## Influence on Later Practice

Few teams follow the spiral diagram literally, but its central idea is everywhere. Modern processes ask for risk lists, build the riskiest items early, and review progress at the end of each iteration. The habit of asking "what is our biggest uncertainty right now?" is part of professional practice.

## Your Turn: Which Risk Comes First?

A team plans a navigation application. Rank the first risk to tackle in each case.

1. It is not known whether the position data can be processed fast enough on typical phones.
2. The colour scheme might not match the company brand.
3. Whether people will pay for the product is uncertain, but the design is conventional.

Case 1 is a technical risk that could invalidate the whole product, so it should be addressed first with a quick benchmark. Case 2 is a low-impact risk that can wait. Case 3 is a market risk, best reduced with an early prototype or a minimal release, since building the full product first would waste effort if people will not pay.

## Conclusion

The spiral model is a risk-driven process model in which development proceeds through repeated cycles, each of which sets objectives, identifies and resolves the main risks, builds and tests, and plans the next cycle, so that effort is directed to the greatest uncertainties first. Its lasting contribution is making risk an explicit driver of every decision.

The next topic describes a widely used framework that combines iteration, risk management, and a strong emphasis on architecture and use cases.

## Introduction

The models studied so far lie along a spectrum. At one end work is planned in detail before it begins, and deviation from the plan is treated as a problem. At the other, plans are short and revised constantly, and change is treated as a source of value. Understanding this contrast, and what each side gets right, is the key to choosing a process sensibly instead of by fashion.

**Definition:** Plan-driven approaches prepare detailed plans and documentation in advance and measure progress against them, whereas agile approaches plan in short cycles, deliver working software frequently, and adapt to change as understanding grows.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_plan_driven_vs_agile_approaches.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A balance scale: on the left a long detailed roadmap labelled Predictability, on the right a short loop with arrows labelled Adaptability, with a dial between them.

ON-IMAGE TEXT: show a short bold title "Plan-Driven vs Agile Approaches" plus only these few labels, large and legible: Plan, Adapt, Balance. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Two Philosophies

**Plan-driven** approaches, which include waterfall, the V-model, and heavyweight iterative frameworks, assume that careful up-front analysis and design will reduce risk, that requirements can be understood early, and that success means delivering what was planned within the planned budget and schedule.

**Agile** approaches assume that requirements will change and that people discover what they need by seeing working software. They therefore favour short cycles, close collaboration with users, and responding to change over following a plan.

## A Side-by-Side Comparison

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dimension</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Plan-driven</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Agile</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed and up front</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous, in short horizons</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed early, changed through formal control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expected to evolve, prioritised repeatedly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mainly at the end, or at major milestones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequent, working increments</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comprehensive, a primary record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Just enough, favouring working software</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team organisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialised roles and hand-offs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cross-functional teams, shared responsibility</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer involvement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At the start and end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure of progress</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conformance to the plan and completed phases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working software delivered</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attitude to change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Costly, to be controlled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Welcomed, even late</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strength</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predictability, traceability, formal assurance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsiveness, early value, learning</td>
    </tr>
  </tbody>
</table>

## What Each Gets Right

Neither approach is simply better. **Plan-driven methods** provide predictability, strong documentation, and evidence for regulators, and they suit situations where requirements are stable and the cost of failure is high. **Agile methods** provide early feedback and adaptability, and they suit situations where requirements are uncertain and value is learned through use.

## Common Myths

- **"Agile means no planning."** Agile teams plan constantly, but over short horizons and with frequent revision.
- **"Agile means no documentation."** The manifesto values working software over comprehensive documentation, not instead of any documentation.
- **"Plan-driven means slow and rigid."** Disciplined planning can be efficient when requirements are stable.
- **"Agile is only for small teams."** It is used at scale, though it needs more coordination, as a later topic explains.

## Home Grounds

Barry Boehm and Richard Turner proposed that each style has a "home ground" where it works best, determined by factors such as the criticality of the system, the size of the team, how quickly requirements change, the culture of the organisation, and the availability of skilled people. Projects at the edges of those grounds benefit from a **balanced** approach that borrows from both.

<!--
IMAGE PROMPT  ->  generate as images/02_home_ground_spectrum.png   (16:9 explanatory diagram, place here)

A horizontal spectrum from Plan-driven on the left to Agile on the right, with a sliding marker. Above it, four small factor dials: Criticality, Team size, Rate of change, Culture. A balanced Hybrid zone is highlighted in the middle.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Lean Towards Which Approach?

1. A system that controls a medical device, subject to external regulation, with requirements fixed by a standard.
2. A new consumer mobile app whose features will be decided by user behaviour.
3. A government project with a fixed legal scope, but whose user interface is uncertain.

Case 1 leans plan-driven because of regulation, fixed requirements, and the cost of failure. Case 2 leans agile because uncertainty is high and learning comes from use. Case 3 is best served by a hybrid: planned, documented structure for the fixed legal scope, with iterative development and user feedback for the interface.

## Conclusion

Plan-driven approaches prepare detailed plans and documentation in advance and measure progress against them, whereas agile approaches plan in short cycles, deliver working software frequently, and adapt to change as understanding grows. Each is strong in its own home ground, and many real projects blend them.

The next topic turns this comparison into practical guidance: how to choose a process for a specific project.

## Introduction

The simplest way to organise software work is to do the activities one at a time, in order, and complete each before the next begins. First decide what is needed, then design, then build, then test, then release. This sequential approach is called the waterfall model, and although few teams use it in its pure form, it remains the reference point against which most other models are described.

**Definition:** The waterfall model is a plan-driven process in which software is developed through a fixed sequence of phases, requirements, design, implementation, verification, and maintenance, with each phase completed and approved before the next one starts.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_the_waterfall_model.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Five blocks cascading from upper left to lower right like steps of a waterfall, labelled Requirements, Design, Implementation, Verification, Maintenance, with a small document icon at each step.

ON-IMAGE TEXT: show a short bold title "The Waterfall Model" plus only these few labels, large and legible: Sequence, Phases, Documents. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Phases

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phase</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Document produced and approved</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capture everything the system must do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements specification</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide the structure of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture and detailed design documents</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write and combine the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source code, unit-level results</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check the whole system against the requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test reports</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment and maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release it, then correct and adapt it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release notes, change records</td>
    </tr>
  </tbody>
</table>

Each phase ends with a review. Only when the output is approved, often in a formal sign-off, does the next phase begin. The documents act as the contract between phases: the designers rely on the requirements specification, the programmers on the design, and the testers on both.

## Where the Model Came From

In 1970 Winston Royce described a staged approach to large software projects in an influential paper. Royce himself was critical of a strict single pass, noting that the model is risky because problems found during testing may force a return to design, so he proposed feedback between adjacent stages and early prototyping. The name "waterfall" and the rigid form were applied afterwards.

## Strengths

- **Simple to understand and manage.** Phases, milestones, and responsibilities are clear.
- **Strong documentation.** Useful when a system must be maintained by people who were not involved, or when regulators require a record.
- **Suits stable, well-understood requirements.** If the need will not change, planning everything first is efficient.
- **Straightforward contracts.** Fixed scope, schedule, and price are easy to specify.
- **Early discipline.** Time spent on requirements and design can prevent costly rework.

## Limitations

- **Late feedback.** Users see nothing working until near the end. A misunderstanding made in the first phase may only be discovered at testing, when it is most expensive to fix.
- **Change is costly.** Returning to an earlier phase breaks the planned flow and often requires formal re-approval.
- **Requirements must be right at the start.** In practice customers often do not know exactly what they need until they see something working.
- **Risk is deferred.** Hard technical problems tend to surface late.
- **Idle and rushed phases.** Testers wait while others work, then are squeezed by a schedule that has already been consumed.

<!--
IMAGE PROMPT  ->  generate as images/02_waterfall_cost_of_late_change.png   (16:9 explanatory diagram, place here)

A waterfall of five phases from top left to bottom right. A red upward arrow from Verification back to Requirements is labelled Expensive rework, with a rising cost curve behind it.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## When Waterfall Still Fits

Despite its weaknesses, the sequential approach is sensible when requirements are fixed by law or contract, when the technology is well known, when the system cannot be partly delivered (for example embedded hardware that ships once), or when strict documentation and approval are mandatory. Many safety-critical and government projects still use waterfall-style stages, often with added feedback loops.

## Your Turn: Waterfall or Not?

1. A project to rebuild a payroll calculation exactly as defined by new legislation, with no flexibility in scope.
2. A startup exploring a new idea for a consumer app, unsure what users will want.
3. A team discovers during testing that the whole design misunderstood a key requirement.

Situation 1 suits a waterfall-style approach because the requirements are fixed and well understood. Situation 2 does not, since uncertainty and the need for early feedback make a single long pass risky. Situation 3 illustrates the model's central weakness: a mistake in an early phase surfaced at the end, where fixing it is most expensive.

## Conclusion

The waterfall model is a plan-driven process in which software is developed through a fixed sequence of phases, requirements, design, implementation, verification, and maintenance, with each phase completed and approved before the next one starts. It offers clarity and documentation, at the cost of late feedback and costly change.

One weakness of waterfall is that testing happens at the end. The next topic describes a model that keeps the sequence but plans verification in step with every stage of development.

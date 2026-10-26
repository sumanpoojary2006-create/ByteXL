## Introduction

Two teams with equally talented developers can deliver very different results, and the difference is rarely talent. It is usually how the work is organised: who decides what is built, in what order, how it is checked, and how changes are handled. That organisation is the software process.

This topic explains what a software process is, why even small teams benefit from one, and how a process differs from the product it produces. Every model in this unit is a different answer to the same question: how should the work be arranged?

**Definition:** A software process is a defined set of activities, roles, and rules for turning an idea into delivered software, giving the team a repeatable and predictable way of working instead of improvising each project from nothing.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_why_we_need_a_software_process.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A chaotic tangle of arrows on the left resolving into an ordered pipeline of labelled stages on the right, with a clock and a checklist beside it.

ON-IMAGE TEXT: show a short bold title "Why We Need a Software Process" plus only these few labels, large and legible: Order, Repeat, Predict. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Process and Product

The **product** is what gets delivered: the working software. The **process** is how it is produced. The two are linked, since a weak process tends to produce weak products, but they are not the same thing, and improving one does not automatically improve the other.

A process answers questions that otherwise get settled by accident:

- What must be decided before building starts?
- Who approves a change, and how?
- How and when is the software checked?
- How does the team learn that something has gone wrong?
- When is the work finished?

## What a Process Provides

- **Order.** Everyone knows what happens next, so people do not wait on one another or duplicate work.
- **Repeatability.** What worked on one project can be reused on the next, instead of being rediscovered.
- **Predictability.** With defined steps and measured history, a team can estimate effort and dates more honestly.
- **Visibility.** Managers, customers, and teammates can see progress and problems early.
- **Quality control.** Checks are placed deliberately in the work instead of being left to chance.
- **Shared language.** Terms such as "done", "sprint", or "release candidate" mean the same to everyone.

## What a Process Contains

Every process, however different it looks, is built from the same elements.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Activities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kinds of work that must happen</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements, design, implementation, verification, deployment, maintenance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who is responsible for what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product owner, developer, tester</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Artifacts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Things produced and handed on</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirement specification, design document, test report, release</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules and policies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conditions for moving work forward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change must be reviewed and pass all tests before release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milestones and reviews</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Points where progress is checked</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A design review, an end-of-iteration demonstration</td>
    </tr>
  </tbody>
</table>

## Too Little and Too Much Process

Process has a cost. With none, work depends on individuals' memory and goodwill, so quality, schedule, and knowledge vary wildly and collapse when people leave. With too much, teams spend their effort on forms, approvals, and documents that do not help the customer, and respond slowly to change.

The right amount depends on the project: its size, the cost of failure, the number of people, and how stable the requirements are. A guiding principle is that **process should be as light as the risk allows and as strong as the risk demands**.

## The Spectrum of Process Models

Models differ mainly in three choices.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Choice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">One end</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Other end</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How much is planned up front</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything is planned before work begins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plans are made in small steps as learning occurs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How work is divided over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One long pass through all activities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many short passes, each delivering something usable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How change is treated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a threat to be controlled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a normal event to be welcomed</td>
    </tr>
  </tbody>
</table>

The next topics present the principal models in roughly the order they developed, each solving problems exposed by the one before.

## Your Turn: What Would a Process Provide?

For each situation, name the benefit of a defined process that is missing.

1. Two developers separately build the same feature because neither knew the other was assigned to it.
2. A team cannot say when a release will be ready because nobody has tracked how long similar work took before.
3. A critical bug reaches users because nobody was responsible for checking that area.
4. A new team member spends weeks working out how things are done.

Situation 1 lacks order and visibility. Situation 2 lacks predictability, which depends on recorded history. Situation 3 lacks deliberately placed quality control. Situation 4 lacks a shared language and documented, repeatable ways of working.

## Conclusion

A software process is a defined set of activities, roles, and rules for turning an idea into delivered software, giving the team a repeatable and predictable way of working instead of improvising each project from nothing. It should be sized to the risk of the project.

The earliest and most widely known model arranges the activities in one strict sequence. The next topic examines it, together with its strengths and its limits.

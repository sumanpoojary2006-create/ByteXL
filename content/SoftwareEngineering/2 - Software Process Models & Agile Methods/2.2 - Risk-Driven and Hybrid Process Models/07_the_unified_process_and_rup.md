## Introduction

By the 1990s, projects were large and the industry had accumulated a rich set of techniques: object-oriented design, use cases, visual modelling, iterative planning, and risk management. The Unified Process brought these together in one framework, and its best-known commercial form, the Rational Unified Process (RUP), became a standard in many large organisations.

**Definition:** The Unified Process is an iterative and incremental software development framework that is driven by use cases, centred on architecture, and organised into four phases, inception, elaboration, construction, and transition, each containing several iterations.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_the_unified_process_and_rup.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A horizontal timeline of four phases, Inception, Elaboration, Construction, Transition, with a stack of overlapping coloured bands beneath showing how much effort each discipline takes in each phase.

ON-IMAGE TEXT: show a short bold title "The Unified Process and RUP" plus only these few labels, large and legible: Phases, Use cases, Iterations. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Three Defining Characteristics

- **Use-case driven.** Requirements are expressed as use cases, descriptions of how users interact with the system to achieve goals, and these drive design, implementation, and testing.
- **Architecture-centric.** A sound architecture is established early and used as the backbone for later work.
- **Iterative and incremental.** Each phase contains iterations that deliver a working, tested increment.

## The Four Phases

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phase</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main goal</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical outcome at the end</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inception</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Establish the scope and business case; decide whether the project is worth doing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agreed vision, rough cost and risk estimate, key use cases identified</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elaboration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand most of the requirements and prove a stable architecture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A working architectural baseline and a reduced risk list</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Construction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build the bulk of the system through iterations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A product ready for initial release to users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver to users, fix remaining defects, train and support</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The final product released</td>
    </tr>
  </tbody>
</table>

Each phase ends with a milestone review in which stakeholders decide whether to proceed: the lifecycle objectives, the lifecycle architecture, the initial operational capability, and the product release.

## Disciplines Run Across All Phases

Unlike waterfall, activities do not belong to one phase. The framework defines disciplines, such as business modelling, requirements, analysis and design, implementation, test, deployment, configuration and change management, project management, and environment. Every iteration contains some of each. The emphasis shifts: requirements work dominates early, implementation dominates in construction, and deployment dominates in transition.

## Six Best Practices

RUP summarised its approach in practices that have since become widely accepted:

1. Develop iteratively.
2. Manage requirements.
3. Use component-based architectures.
4. Model software visually, using diagrams.
5. Continuously verify quality.
6. Control changes.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comprehensive guidance for large, complex projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be heavyweight, with many documents and roles</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Addresses risk and architecture early</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs tailoring; teams may follow everything even when unnecessary</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear milestones that suit management and contracts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less natural for small teams and fast-changing products</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Basis for many later iterative approaches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perceived as bureaucratic after the rise of agile methods</td>
    </tr>
  </tbody>
</table>

## Tailoring

The framework was intended to be **customised**: a small project would use a small subset of the artifacts and roles, and a large one more. In practice, many organisations adopted it in a heavy form, and this reputation for ceremony contributed to the move towards lighter agile methods. Understanding it still helps, because many large organisations and public tenders continue to use its vocabulary of phases and milestones.

## Your Turn: Which Phase?

1. The organisation decides the project is viable and approves funding for further work.
2. The architecture is demonstrated with a working baseline that handles the riskiest requirements.
3. Users receive the product, and the team fixes remaining defects and provides training.
4. The team builds most features through successive iterations.

Item 1 is inception. Item 2 is elaboration. Item 3 is transition. Item 4 is construction.

## Conclusion

The Unified Process is an iterative and incremental software development framework that is driven by use cases, centred on architecture, and organised into four phases, inception, elaboration, construction, and transition, each containing several iterations. It showed how iterative development could be made disciplined for large organisations.

Its heaviness led many teams to look for a different philosophy altogether. The next topic compares the plan-driven tradition described so far with the agile approach that challenged it.

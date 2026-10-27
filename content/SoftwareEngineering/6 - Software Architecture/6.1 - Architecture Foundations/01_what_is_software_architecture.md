## Introduction

Design principles guide how individual modules are shaped. A large system also needs a plan for how its major parts fit together, how they communicate, and where they run. This plan is the software architecture. It is the set of decisions that is hardest to change later, and that largely decides whether a system can achieve its goals for performance, reliability, security, and cost.

This topic defines software architecture, explains how it differs from design, and describes the role of the people who make architectural decisions.

**Definition:** Software architecture is the fundamental organisation of a system, consisting of its major elements, the relationships among them, and the principles that govern their design and evolution, and it comprises the significant decisions that are costly to change and that most strongly shape the qualities of the system.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_software_architecture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A city map seen from above: major districts labelled Presentation, Services, Data, Integration, connected by main roads, with a magnifying glass showing a single building as detailed design.

ON-IMAGE TEXT: show a short bold title "What Is Software Architecture" plus only these few labels, large and legible: Structure, Decisions, Qualities. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Defining Architecture

Several well-known definitions emphasise different aspects.

- Len Bass, Paul Clements, and Rick Kazman describe architecture as the **structures** of a system: its software elements, the externally visible properties of those elements, and the relationships among them.
- The international standard ISO/IEC/IEEE 42010 defines it as the fundamental concepts or properties of a system in its environment, embodied in its elements, relationships, and the principles of its design and evolution.
- Martin Fowler offers a practical summary: architecture is about **the important stuff, whatever that is**, meaning the decisions that matter most and are hardest to reverse.

All agree on three points. Architecture is about **structure**, about **important decisions**, and about **qualities** such as performance and modifiability.

## Architecture and Design

The boundary between architecture and design is not sharp, but a useful distinction is one of significance and scope.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Architecture</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detailed design</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The whole system or a major subsystem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module, a class, or a function</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Significant, expensive to reverse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Local, relatively cheap to change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concerns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality attributes, major components, communication, deployment, technology families</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Algorithms, data structures, class responsibilities</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Audience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many stakeholders, including managers and operators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mostly developers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Splitting the system into a mobile client, an interface service, and a database</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choosing how an order total is calculated inside the order module</td>
    </tr>
  </tbody>
</table>

A decision belongs to the architecture if changing it later would require major rework across the system. Choosing between a single deployable application and several independently deployed services is architectural. Choosing a name for a function is not.

## What Architecture Does

- **Enables the required qualities.** Whether a system can serve a million users or recover from failure is largely determined by its structure.
- **Provides a shared vision.** It gives developers and stakeholders a common picture and vocabulary.
- **Guides construction.** It divides the work and suggests an order in which parts can be built.
- **Constrains and permits change.** It makes some changes easy and others hard.
- **Supports reasoning and prediction.** It lets the team estimate performance, cost, and risk before building.
- **Manages complexity.** It shows the system at a level of detail a person can grasp.

## The Elements of an Architecture

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Major units of computation or storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order service, menu service, database</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connectors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The means by which components interact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requests over HTTPS, a message queue, a shared file</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How components and connectors are arranged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The mobile app calls the interface service, which calls the order and menu services</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraints and principles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules that guide design and evolution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All access to data goes through the owning service</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rationale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why the decisions were made</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A message queue is used so that kitchen failures do not block ordering</td>
    </tr>
  </tbody>
</table>

The last item is often missing and is the most valuable to a later reader. Knowing why something was decided tells a team whether the decision still applies.

## Architecture Is Unavoidable

Every system has an architecture, whether or not anyone designed it. Without deliberate decisions, it emerges from many small choices and tends toward a tangle often called a **big ball of mud**. Deliberate architecture means making the important decisions consciously and recording them.

## Who Makes Architectural Decisions

The role of **software architect** is held by a person or, increasingly, shared across the team. Responsibilities usually include understanding the stakeholders and requirements, identifying the significant quality goals, making and recording key decisions, communicating the architecture, guiding the team's design, and reviewing for conformance. Effective architects stay close to the code: an architecture that cannot be built, or that ignores how teams actually work, is a drawing and not a plan.

## Conway's Law

In 1968 Melvin Conway observed that organisations design systems that mirror their own communication structures. If four teams build a compiler, it will have four stages. The consequence is that architecture and team organisation affect one another: boundaries between components tend to follow boundaries between teams. Deliberately shaping teams to match the desired architecture, sometimes called the inverse Conway manoeuvre, is a common tactic.

## Evolution

Architecture is not fixed at the start. It is refined as understanding grows and requirements change. Teams that decide early what is costly to reverse, delay the rest until more is known, and adjust the structure as they learn, usually fare better than those that attempt a perfect plan in advance or those that make no plan at all.

<!--
IMAGE PROMPT  ->  generate as images/02_architecture_vs_design_zoom.png   (16:9 explanatory diagram, place here)

A zoom diagram: the outer ring labelled Architecture shows components, connectors, and quality goals of a meal ordering system; an inner ring labelled Detailed design shows a single component opened to reveal classes. A label shows Costly to change at the outer ring and Cheap to change at the inner ring.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Architecture or Design?

1. Whether the data for the entire system is stored in a single central database or in separate stores for each service.
2. Which sorting method is used inside one report function.
3. Whether two teams will communicate through direct calls or through a message queue.

Decision 1 is architectural: it affects every part of the system and is costly to reverse. Decision 2 is detailed design, local and easy to change. Decision 3 is architectural, since it shapes failure behaviour, performance, and team coupling.

## Conclusion

Software architecture is the fundamental organisation of a system, consisting of its major elements, the relationships among them, and the principles that govern their design and evolution, and it comprises the significant decisions that are costly to change and that most strongly shape the qualities of the system. Every system has one, and it is better to choose it than to discover it.

Architectural decisions are driven by what the system must achieve. The next topic examines the drivers that shape them: the quality attributes.

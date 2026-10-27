## Introduction

Requirements say what a system must do. Code is the working result. Between them lies a stage that is easy to overlook because it often happens in conversations, sketches, and quiet thinking: design. It is the stage in which a team decides how the system will be organised so that the requirements can be met, the software can be built by several people, and the result can be changed in future.

This topic defines software design, separates its levels, and explains why it is best understood as a series of decisions made under constraints.

**Definition:** Software design is the activity of deciding how a system will be structured, what its parts are, how they relate and communicate, and how they will behave, so that the requirements are met and the software remains understandable and changeable.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_software_design.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A blueprint stage between two blocks: on the left a clipboard labelled Requirements, on the right a working system labelled Code, with a drafting table in the middle showing boxes and arrows.

ON-IMAGE TEXT: show a short bold title "What Is Software Design" plus only these few labels, large and legible: Decide, Structure, Build. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Design Is Not Coding

Design and coding overlap, but they are different kinds of work. Coding turns decisions into instructions a computer can run. Design makes the decisions: which parts exist, what each is responsible for, and how they fit. Two programmers can write correct code for the same requirement and produce systems that are very different to maintain, because their design decisions differ.

## Levels of Design

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical decisions</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical output</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architectural (high-level) design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The overall structure of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Major components, how they communicate, technology families, where data lives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture diagrams and decision records</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component (mid-level) design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The structure inside each major part</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modules and their responsibilities, interfaces between them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component and interface descriptions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed (low-level) design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The internals of modules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classes, operations, data structures, algorithms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Class and sequence diagrams, notes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface and user experience design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How people and other systems interact with the software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screens, flows, programming interfaces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wireframes, interface specifications</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is stored and how it is organised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entities, relationships, storage choices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data models</td>
    </tr>
  </tbody>
</table>

The levels are connected. A good architecture makes component design easier, and weak decisions at a higher level are hard to repair at a lower one.

## Design as Decision Making

Almost every design question has several acceptable answers with different consequences. Should two functions live together or apart? Should one part call another directly or send a message? Each choice trades one quality for another: simplicity, speed, flexibility, cost, safety. Design is therefore **a series of trade-offs**, and good designers record the reasons for important choices so that later readers know whether the reasoning still holds.

Horst Rittel and Melvin Webber called problems of this type **wicked**: they cannot be fully specified in advance, every solution changes the problem, and there is no single correct answer, only better and worse ones. Software design shares these properties, which is why it cannot be reduced to a formula.

## Essential and Accidental Complexity

Fred Brooks distinguished **essential complexity**, which comes from the problem itself, from **accidental complexity**, which comes from our tools and solutions. A tax system is complex because tax rules are. A confusing structure for storing those rules adds accidental complexity. Design cannot remove the essential kind, but good design keeps the accidental kind small.

## What Good Design Aims For

- **Correctness:** the design can meet all the requirements.
- **Understandability:** others can learn it without heroic effort.
- **Modifiability:** likely changes can be made locally and safely.
- **Testability:** parts can be checked independently.
- **Reusability:** parts can be used in more than one place where that makes sense.
- **Efficiency:** the design can meet performance and resource needs.
- **Simplicity:** it is no more complicated than the problem requires.

## When Design Happens

Design is not confined to one phase. In sequential processes it occurs mainly between requirements and implementation. In iterative and agile processes it is continuous: a little up-front thinking to choose a direction, then design decisions in every iteration, refined as understanding grows. The question is not whether to design but how much to decide in advance. A sensible approach is to decide early what is expensive to change, and delay everything else until more is known.

<!--
IMAGE PROMPT  ->  generate as images/02_design_levels.png   (16:9 explanatory diagram, place here)

A zoom diagram with four nested levels labelled Architecture, Components, Modules and classes, Details, narrowing from the whole system to a single module. Arrows labelled Decisions flow down and Feedback flows up.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Level?

Name the design level for each decision.

1. Whether the system is split into a mobile client, an interface service, and a database.
2. How the Payment module exposes its operations to the Order module.
3. Which data structure holds the items of one order.

Decision 1 is architectural design. Decision 2 is component or interface design, since it concerns the boundary between modules. Decision 3 is detailed design.

## Conclusion

Software design is the activity of deciding how a system will be structured, what its parts are, how they relate and communicate, and how they will behave, so that the requirements are met and the software remains understandable and changeable. It consists of decisions and trade-offs, not formulas.

Two ideas underlie nearly every design principle. The next topic examines them: abstraction and information hiding.

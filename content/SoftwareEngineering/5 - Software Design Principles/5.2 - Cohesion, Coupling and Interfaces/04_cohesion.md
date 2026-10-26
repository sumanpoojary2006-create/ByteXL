## Introduction

Two properties decide how good a division into modules is. One concerns what is inside each module, and the other concerns how modules relate to each other. Cohesion is the first. It asks whether the contents of a module belong together. A module whose parts all serve a single purpose is easy to name, understand, and change. A module that holds unrelated items is a place where bugs and confusion collect.

**Definition:** Cohesion is the degree to which the elements inside a module belong together because they contribute to a single, well-defined purpose, and high cohesion, where everything in a module serves one purpose, is a mark of good design.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_cohesion.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two containers side by side: the left holds items all of the same kind neatly sorted and is labelled High cohesion, the right holds a jumble of unrelated objects labelled Low cohesion.

ON-IMAGE TEXT: show a short bold title "Cohesion" plus only these few labels, large and legible: Together, Purpose, Focus. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Idea

Imagine a drawer labelled "kitchen knives" containing only knives, and another labelled "miscellaneous" holding batteries, string, and a screwdriver. The first is easy to use: you know what is inside. The second invites loss and confusion. A highly cohesive module is the knife drawer.

A simple test is to try to describe the module's purpose in one short sentence without using the word "and" or "or". If that is difficult, the module probably does more than one thing.

## Levels of Cohesion

Studies of structured design, beginning with work by Larry Constantine and Edward Yourdon, identify a scale from the worst to the best.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Elements are together because...</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coincidental</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">There is no real relationship; they were put together by chance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A utilities module with unrelated functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Worst</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They are in the same logical category but do different things</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module for all input handling, covering files, keyboard, and network</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Temporal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They run at the same time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A start-up module that does many unrelated initialisations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Procedural</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They follow a fixed order of steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module doing validation, then logging, then saving in sequence for unrelated reasons</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communicational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They work on the same data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations that all read and update one order record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequential</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The output of one is the input of the next</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read an order, calculate its total, then format the invoice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functional</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">They all contribute to one well-defined task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module that only calculates delivery fees</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Best</td>
    </tr>
  </tbody>
</table>

The aim is not to classify every module but to recognise the direction: toward **functional** cohesion, where everything in a module serves one purpose.

## Cohesion in Object-Oriented Design

A class is cohesive when its attributes and operations are closely related and when most operations use most of the attributes. If a class has two groups of operations that use two separate sets of attributes, it is probably two classes that have been merged. This is the thinking behind the **single responsibility principle**, described later in this unit.

## Why High Cohesion Helps

- **Understandability:** a focused module is easier to read, name, and explain.
- **Maintainability:** changes concentrate in one place.
- **Reusability:** a module with one clear purpose can be reused elsewhere.
- **Testability:** fewer behaviours mean simpler tests.
- **Reliability:** fewer unrelated interactions inside means fewer surprising defects.

## Symptoms of Low Cohesion

- A module with a vague name such as Manager, Helper, Utils, or Processor
- A module that keeps growing because everything "related" ends up there
- Operations in the same module that share nothing: no data, no purpose
- Frequent merge conflicts because many people edit the same module for unrelated reasons
- A change for one reason forces testing of many unrelated features

## Improving Cohesion

1. **Identify the responsibilities** present in the module by listing what it does.
2. **Group** the elements that serve the same purpose.
3. **Split** the module along those lines, giving each part a clear name.
4. **Move** misplaced elements to the module they belong to.
5. **Resist merging** modules for convenience when their purposes differ.

Cohesion can be overdone. Splitting a module into pieces that have no meaning alone, or that always change together, adds overhead without benefit. If two things always change together and are used together, they probably belong together.

<!--
IMAGE PROMPT  ->  generate as images/02_cohesion_spectrum.png   (16:9 explanatory diagram, place here)

A horizontal spectrum from Coincidental through Logical, Temporal, Procedural, Communicational, Sequential to Functional, shown as seven stacked drawers going from a jumble of mixed objects on the left to a single neatly sorted set on the right. An arrow labelled Aim higher points right.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify the Cohesion

1. A module contains: calculate delivery fee, calculate tax, convert currency, validate email address.
2. A module contains only operations for adding, removing, and totalling the items of an order.
3. A module runs "at start-up": open log file, load settings, connect to cache, check licence.

Module 1 is coincidental or logical, since only loosely related items share a module; it should be split. Module 2 has functional or communicational cohesion: all operations concern order items, so it is well focused. Module 3 has temporal cohesion: the items are together only because they run at the same time, which is acceptable for a start-up routine that merely calls separate modules, but poor if it contains their logic.

## Conclusion

Cohesion is the degree to which the elements inside a module belong together because they contribute to a single, well-defined purpose, and high cohesion, where everything in a module serves one purpose, is a mark of good design. A short purpose statement without "and" is a practical test.

Cohesion looks inside modules. The next topic looks at the connections between them: coupling.

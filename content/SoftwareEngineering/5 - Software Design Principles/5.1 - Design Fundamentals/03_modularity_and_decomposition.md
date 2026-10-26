## Introduction

Large problems are solved by dividing them into smaller ones. This is true in engineering generally, and in software it is the basic strategy for coping with size. A well-divided system can be built by several people at once, understood piece by piece, tested part by part, and changed with limited risk. A poorly divided one is a tangle in which every change touches everything.

This topic describes modularity, how a system is decomposed into modules, and the ways in which decomposition can succeed or fail.

**Definition:** Modularity is the degree to which a system is divided into separate, interchangeable parts, called modules, each with a clear responsibility and interface, and decomposition is the process of breaking a larger problem or system into such parts.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_modularity_and_decomposition.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A large block being divided into smaller labelled blocks, Menu, Orders, Payments, Notifications, each with one visible connector socket, and fitted together like building bricks.

ON-IMAGE TEXT: show a short bold title "Modularity and Decomposition" plus only these few labels, large and legible: Divide, Own, Connect. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What a Module Is

A module is a unit of software with a defined responsibility and an interface through which others use it. Depending on the setting, it may be a function, a class, a package, a library, a service, or a whole subsystem. What makes it a module is not its size but its **boundary**: it can be understood, replaced, tested, and assigned to a person or team on its own.

## Why Decompose

- **Managing complexity.** Each part is small enough to understand.
- **Division of labour.** Different people or teams can work in parallel.
- **Localised change.** A change affects one module, not everything.
- **Independent testing.** Each part can be checked alone.
- **Reuse.** A well-defined module can serve several purposes.
- **Replaceability.** A module can be rewritten or swapped without disturbing the rest.

## Separation of Concerns

Edsger Dijkstra named the idea of **separation of concerns**: dealing with one aspect of a problem at a time. In design it means that each module addresses a distinct concern, such as presentation, business rules, data storage, or communication, and that concerns are not mixed together. When a module handles several concerns, a change to one risks the others.

## Ways to Decompose

There is no single correct way to divide a system. Common strategies are:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By function (processing steps)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module per step in a process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read input, validate, calculate, format, write</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By feature or business capability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module per thing the business does</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordering, Payments, Delivery, Reporting</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By layer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module per level of abstraction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presentation, business logic, data access</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By hidden design decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module per decision likely to change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module that hides the storage format</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By data (object-oriented)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module per important kind of thing, with its operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer, Order, Dish</td>
    </tr>
  </tbody>
</table>

Parnas showed that dividing by steps of processing tends to produce modules that all depend on the same decisions, so a change ripples across them. Dividing by hidden decisions limits that effect. In practice, designers combine strategies: layers within a business capability, and objects within a layer.

## Hierarchical Decomposition

Decomposition is usually applied repeatedly. The whole system is divided into major parts, each of those is divided into smaller parts, and so on until the pieces are small enough to build and understand. This produces a hierarchy that can be drawn as a tree, and it is the same top-down thinking used in work breakdown for planning. It is worth remembering that the structure should be revisited, because a decomposition that looked right early may prove wrong as understanding grows.

## What Makes a Decomposition Good

A good decomposition has modules that are **cohesive**, each focused on one purpose, and **loosely coupled**, each depending on others as little as possible. The next two topics examine those ideas in detail. Other signs of a good decomposition:

- the modules have names that describe their purpose clearly
- the responsibilities of each are easy to state in one sentence
- a typical change affects one or two modules
- dependencies run in a consistent direction, without cycles
- a new team member can find where something belongs

## Signs of Poor Decomposition

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symptom</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Likely cause</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single change requires edits in many modules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Related behaviour scattered across modules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module that nobody dares touch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too large, mixing many concerns</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modules that cannot be tested without all the others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden or tangled dependencies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams constantly waiting for each other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Boundaries do not match how work is divided</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Circular dependencies between modules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsibilities poorly allocated</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many tiny modules that merely pass requests along</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-decomposition, with no real responsibility</td>
    </tr>
  </tbody>
</table>

Too much decomposition is also a problem: excessive layers and fragments add indirection and make the system harder to follow.

<!--
IMAGE PROMPT  ->  generate as images/02_decomposition_tree_and_strategies.png   (16:9 explanatory diagram, place here)

Left: a tree with Ordering System at the top, branching to Menu, Orders, Payments, Notifications, and then to smaller modules. Right: a small table of three strategies by step, by capability, by hidden decision, with a ripple-of-change icon showing less spread for the last.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Good or Poor Division?

1. A system has one module called Utilities that holds payment rules, date formatting, email sending, and menu search.
2. Changing the format of a receipt requires edits in the Order, Payment, Menu, and Notification modules.
3. A module is described as responsible for creating and storing orders.

Division 1 is poor: Utilities mixes unrelated concerns and will grow without limit. Division 2 shows scattered responsibility: receipt formatting should live in one place. Division 3 is borderline: creating an order and storing it are two concerns, which many designs would separate, though for a small system one module may be acceptable.

## Conclusion

Modularity is the degree to which a system is divided into separate, interchangeable parts, called modules, each with a clear responsibility and interface, and decomposition is the process of breaking a larger problem or system into such parts. Good division follows the grain of the problem and the likely changes.

How well a division works depends on two measurable-in-spirit properties. The next chapter begins with the first: cohesion.

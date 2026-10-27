## Introduction

Before designing how a system works inside, it helps to be clear about who uses it and what they use it for. A use case diagram gives that overview on a single page. It does not show detailed steps. It shows the boundary of the system, the people and other systems around it, and the goals each can pursue. It is therefore a natural link between requirements work, which Unit 3 covered, and design.

**Definition:** A use case diagram is a UML behaviour diagram that shows the actors who interact with a system, the use cases that represent the goals they can achieve with it, and the relationships among them, drawn inside and outside a boundary that marks the scope of the system.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_use_case_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A rectangle boundary box labelled Meal Ordering System containing four ovals, with a stick-figure Customer on the left connected to two of them and a Payment Service box on the right connected to one.

ON-IMAGE TEXT: show a short bold title "Use Case Diagrams" plus only these few labels, large and legible: Actor, Use case, Boundary. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Elements

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it is drawn</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stick figure (or a box labelled with a stereotype for systems)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A role played by a person or an external system that interacts with the system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An oval containing a verb phrase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A goal the actor wants to achieve with the system</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">System boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rectangle around the use cases, labelled with the system name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separates what is inside the system from what is outside</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Association</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A line between an actor and a use case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The actor takes part in the use case</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Include</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dashed arrow from the base use case to the included one, labelled include</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The base use case always uses the behaviour of the other</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extend</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dashed arrow from the extending use case to the base, labelled extend</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The extending use case optionally adds behaviour at a defined point</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generalisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A solid line with a hollow triangle toward the parent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A specialised actor or use case inherits from a more general one</td>
    </tr>
  </tbody>
</table>

## Actors Are Roles, Not People

An actor represents a **role**. One person can play several roles, and many people can play the same role. A cook who also pays for lunch is a Staff Member in one use case and a Customer in another. Actors can also be external systems, such as a payment service or an email gateway. Naming actors by role avoids confusion and keeps the diagram stable as people change.

A **primary actor** starts a use case to achieve a goal, usually drawn on the left. A **secondary actor** supports it, such as a bank, usually drawn on the right.

## Writing Good Use Case Names

Use cases are named with an active verb and a goal from the user's viewpoint: "Place order," "Cancel booking," "View weekly report." Names that describe system internals, such as "Update database," or tiny steps, such as "Click button," are at the wrong level. Each use case should deliver something of value to an actor.

## Include and Extend

These two relationships are often confused.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Include</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Extend</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse common behaviour that is always needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add optional or exceptional behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is the added behaviour always executed?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only under some condition</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which use case depends on the other?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The base depends on the included one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The extension depends on the base, which does not know about it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place order includes Pay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place order is extended by Apply discount code</td>
    </tr>
  </tbody>
</table>

A rule of thumb: if removing the second use case would make the first one incomplete, it is an include. If the base use case still works fully without it, it is an extension.

## Scope and Level

A single diagram should show a manageable number of use cases, often between five and fifteen. For large systems, diagrams are grouped by subsystem or actor. The details of each use case are not drawn but written in a use case description with a main flow and alternatives, as the Unit 3 topic on use cases explained. The diagram is a **table of contents** for the written use cases.

## Strengths and Limits

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limits</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple enough for non-technical stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows nothing about the order of steps or data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows scope at a glance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to create too many tiny use cases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Helps check that every actor has needed goals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Says little about quality requirements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connects naturally to testing and stories</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detail lives in text, which must be kept in step</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_use_case_diagram_meal_ordering.png   (16:9 explanatory diagram, place here)

A use case diagram for a meal ordering system. Actors Customer and Kitchen Staff on the left, Payment Service on the right. Inside the boundary: Browse menu, Place order, Pay (included by Place order with a dashed include arrow), Apply discount code (dashed extend arrow to Place order), Update order status (Kitchen Staff).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Read the Diagram Description

A diagram shows actors Student and Cashier, and use cases Order meal, Pay, and Apply loyalty discount. Order meal includes Pay. Apply loyalty discount extends Order meal.

1. Which use case is always performed as part of Order meal?
2. Which is optional?
3. Is a payment gateway an actor or a use case?

Pay is always performed, because it is included. Apply loyalty discount is optional, since it is an extension. A payment gateway is an actor, specifically a secondary actor, because it is an external system that takes part in the interaction but is outside the boundary.

## Conclusion

A use case diagram is a UML behaviour diagram that shows the actors who interact with a system, the use cases that represent the goals they can achieve with it, and the relationships among them, drawn inside and outside a boundary that marks the scope of the system. It gives scope at a glance and points to the written detail.

Use cases describe behaviour from outside. The next topic turns to the inside and introduces the most widely used UML diagram: the class diagram.

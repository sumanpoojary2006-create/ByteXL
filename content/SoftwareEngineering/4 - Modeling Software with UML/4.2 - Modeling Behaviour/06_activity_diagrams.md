## Introduction

Many things worth modeling are processes: a sequence of actions with decisions, loops, and sometimes steps that happen at the same time. Examples include how an order is fulfilled, how a loan application is approved, or how a feature moves from request to release. The activity diagram is UML's flowchart-like notation for such workflows. It is used to describe business processes, the flow of a use case, and the logic of complex operations.

**Definition:** An activity diagram is a UML behaviour diagram that shows the flow of actions in a process, including decisions, parallel paths, and the points where the process begins and ends, optionally grouped by the participants responsible for each action.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_activity_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A flow starting at a filled circle, passing through rounded action boxes, a diamond decision with two branches, a thick bar splitting into two parallel paths and rejoining, and ending at a circle with a dot.

ON-IMAGE TEXT: show a short bold title "Activity Diagrams" plus only these few labels, large and legible: Flow, Decide, Parallel. Keep text minimal, no sentences.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Initial node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A filled circle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where the activity starts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rounded rectangle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single step of work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control flow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An arrow between nodes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order in which steps happen</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A diamond with several outgoing arrows labelled by conditions in square brackets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A choice: exactly one path is taken</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A diamond where paths rejoin</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternative paths come together again</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fork</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A thick bar with one incoming and several outgoing arrows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start of parallel (concurrent) paths</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Join</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A thick bar with several incoming and one outgoing arrow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Waiting for all parallel paths to finish</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Activity final node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A circle containing a smaller filled circle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The end of the whole activity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flow final node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A circle containing an X</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The end of one path only, without ending the activity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rectangle holding a thing, such as an order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data passed between actions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Swimlane (partition)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A vertical or horizontal band labelled with a role</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which participant performs the actions within it</td>
    </tr>
  </tbody>
</table>

## Decisions and Parallelism

**Decisions** and **forks** are often mixed up. A decision chooses **one** of several paths, depending on a condition: after payment, either the order is confirmed or it is rejected. A fork starts **all** the outgoing paths at once: after confirmation, the kitchen prepares the meal while the system sends a receipt. A join then waits for **every** incoming path before continuing, whereas a merge simply continues when any path arrives.

## Swimlanes

Dividing the diagram into labelled lanes, one for each person, team, or system, shows **who** does each action as well as what is done. A lane for the Customer, one for the Ordering System, and one for the Kitchen makes handoffs between participants visible. Many problems in processes occur at handoffs, so swimlanes are useful for finding delays and missing responsibilities.

## An Example: Fulfilling an Order

The activity begins when an order is submitted. The system checks stock. If an item is unavailable, the customer is asked to choose again and the flow returns to stock checking. If all items are available, the customer pays. If payment fails, the order is cancelled and the activity ends. If it succeeds, the flow forks: the Kitchen prepares the meal while the system emails a receipt. When both are complete, they join, the order is marked ready, and the activity ends.

This one paragraph uses initial and final nodes, a loop through a decision and merge, a fork and join, and two swimlanes, and it can be read by non-programmers.

## Activity Diagrams, Flowcharts, and Use Cases

An activity diagram resembles a traditional flowchart but adds support for parallel flow, swimlanes, and object flow. Compared with use case text, the diagram shows the sequence and branching of a process visually, making complex logic easier to check. Compared with a sequence diagram, it describes the flow of work, without focusing on messages between specific objects.

## Good Practice

- Give the diagram a clear scope, one process or one use case.
- Label decision branches with clear conditions, and make sure all cases are covered.
- Keep the level of detail consistent: do not mix high-level steps with fine-grained operations.
- Limit size. A diagram that does not fit on a page should be split.
- Use swimlanes only if responsibility is relevant.

<!--
IMAGE PROMPT  ->  generate as images/02_activity_fulfil_order_swimlanes.png   (16:9 explanatory diagram, place here)

An activity diagram with three swimlanes Customer, Ordering System, Kitchen. Flow: submit order, check stock decision (loop back if unavailable), pay, payment decision (cancel path ends), fork to Prepare meal (Kitchen) and Send receipt (System), join, mark ready, final node.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Decision or Fork?

1. After an order is accepted, the kitchen prepares food while the system sends a receipt.
2. After payment, the process either confirms the order or cancels it.
3. The process must not continue until both food preparation and packaging are finished.

Item 1 is a fork, since both paths run at the same time. Item 2 is a decision, since only one path is taken. Item 3 is a join, since it waits for all incoming paths to finish.

## Conclusion

An activity diagram is a UML behaviour diagram that shows the flow of actions in a process, including decisions, parallel paths, and the points where the process begins and ends, optionally grouped by the participants responsible for each action. It is the clearest UML view of how work flows.

Activity diagrams describe a process as a whole. The next topic looks at behaviour from the point of view of a single object, whose responses depend on its state.

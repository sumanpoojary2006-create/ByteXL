## Introduction

One of the oldest ideas in building complex systems is to arrange them in layers, each built on the one beneath and hiding its details from the one above. Computer networks are described this way, operating systems are structured this way, and most business applications still follow the same pattern. The layered style is often a team's first architecture, and it is a good place to learn the trade-offs that every style involves.

**Definition:** Layered architecture is a style in which a system is divided into horizontal layers, each providing services to the layer above and using services from the layer below, so that each layer has a distinct responsibility and depends only on the layers beneath it.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_layered_architecture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four horizontal slabs stacked like a cake: Presentation at the top, Application, Domain or Business, and Data at the bottom, with downward arrows between adjacent slabs.

ON-IMAGE TEXT: show a short bold title "Layered Architecture" plus only these few labels, large and legible: Presentation, Business, Data. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Idea

Each layer has a particular role and relates only to its neighbours. Requests generally travel downward, from the user towards the data, and responses travel back up. The key rule is a **dependency rule**: a layer may use the layer below, but a lower layer must not depend on a higher one. This keeps changes in upper layers, such as interface redesigns, from breaking lower ones.

## A Typical Business Application

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Layer</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples in an ordering system</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presentation (user interface)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show information and accept user input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mobile screens, web pages, interface endpoints</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application (service)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coordinate use cases and workflows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place order, cancel order; calls the domain layer in the right order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Domain (business logic)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implement the rules and concepts of the business</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pricing rules, order validation, discount policy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data access (persistence)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Store and retrieve data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reading and writing orders and menus in the database</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrastructure (cross-cutting)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support services used by several layers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logging, security checks, configuration</td>
    </tr>
  </tbody>
</table>

Not every system needs all layers. Small ones may combine application and domain. The point is that **responsibilities are separated**, and that dependencies point in one direction.

## Strict and Relaxed Layering

- In **strict layering**, a layer may only use the layer immediately below it. This maximises isolation but can force layers to pass requests along even when they add nothing.
- In **relaxed layering**, a layer may use any lower layer. This is more efficient, but couples upper layers to the details of lower ones.

Some designs mark certain layers as **open**, meaning they may be bypassed, such as a layer of shared utilities.

## Benefits

- **Separation of concerns:** each layer has a clear job.
- **Replaceability:** a layer can be changed with little effect on others, such as swapping the database or redesigning the interface.
- **Testability:** layers can be tested separately, for example the domain logic without a database.
- **Understandability:** the structure is familiar to most developers, so new team members find their way quickly.
- **Division of labour:** teams can specialise by layer.

## Drawbacks

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance overhead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each request passes through several layers, and each crossing adds cost</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change often cuts across layers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new feature usually needs changes in every layer, so layers do not isolate feature changes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sinkhole pattern</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many requests merely pass through layers without any processing, adding code but no value</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monolithic deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All layers are often released together, so a small change requires a full release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk of technical, not business, structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code is organised by technical role instead of by what the business does, which hides the domain</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaky layers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower-level details creep upward, such as database structure shaping the interface</td>
    </tr>
  </tbody>
</table>

## Layers and Business Capabilities

Because features cut across layers, many modern systems organise **vertically** by business capability, such as ordering, payments, and delivery, with a layered structure inside each. This combines the clarity of layers with the locality of change that features need.

## Layers Elsewhere

The layered idea appears throughout computing: the layers of a network protocol stack, the layers of an operating system, and the stack from application to hardware. In each, the benefit is the same, that each layer relies on a simple, defined interface of the one below. Edsger Dijkstra's THE operating system in the 1960s was an early well-known layered design.

## When to Use It

Layered architecture is a sound default for applications with moderate complexity, a single team, and requirements that favour simplicity and familiarity. It is less suitable where parts must be scaled or deployed independently, or where very high performance requires minimal indirection.

<!--
IMAGE PROMPT  ->  generate as images/02_layers_strict_vs_relaxed.png   (16:9 explanatory diagram, place here)

Two stacks side by side. Left, Strict layering: each layer connects only to the next one down. Right, Relaxed layering: arrows skip layers. Beside them a vertical arrow labelled A feature change cuts across all layers in orange.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Layer?

1. A rule that orders above 1,000 currency units receive a discount.
2. The code that runs the database query for a customer's orders.
3. A screen that displays the order history.
4. A function that writes a record of every request to a log.

Item 1 belongs in the domain layer, since it is a business rule. Item 2 belongs to the data access layer. Item 3 belongs to the presentation layer. Item 4 is infrastructure or cross-cutting, because several layers use logging.

## Conclusion

Layered architecture is a style in which a system is divided into horizontal layers, each providing services to the layer above and using services from the layer below, so that each layer has a distinct responsibility and depends only on the layers beneath it. It is simple, familiar, and effective for many applications, at the cost of overhead and cross-layer changes.

Layers organise the code inside an application. The next topic describes how an application is divided across machines: the client-server style.

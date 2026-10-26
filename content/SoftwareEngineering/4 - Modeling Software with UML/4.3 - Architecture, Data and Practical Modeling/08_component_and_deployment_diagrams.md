## Introduction

Class diagrams work at the level of individual classes, which is too fine-grained to explain a large system. At a higher level, the questions are different. What are the major parts, and what does each offer to the others? And once built, where do those parts run? Component diagrams answer the first question and deployment diagrams answer the second. Together they describe the physical and logical organisation of a system.

**Definition:** A component diagram shows the major replaceable parts of a system and the interfaces through which they connect, while a deployment diagram shows the hardware and execution environments on which software artifacts run and how those environments communicate.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_component_and_deployment_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: several rectangular component boxes joined by lollipop and socket connectors. Right: three server boxes labelled Phone, Application server, Database server containing small artifact icons and linked by labelled communication lines.

ON-IMAGE TEXT: show a short bold title "Component and Deployment Diagrams" plus only these few labels, large and legible: Parts, Interfaces, Nodes. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Components

A **component** is a modular part of a system that encapsulates its content and can be replaced by another that offers the same interfaces. It might be a service, a library, a module, or a subsystem. Examples in a meal-ordering system are the Menu component, the Order component, the Payment component, and the Notification component.

Components are drawn as rectangles labelled with the name and a component symbol or stereotype.

## Interfaces: Provided and Required

The key idea of a component diagram is that components connect only through **interfaces**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A circle on a short line (lollipop)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provided interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Services the component offers to others</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A half circle on a short line (socket)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Services the component needs from others</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A lollipop fitting into a socket</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assembly connector</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One component uses the service provided by another</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small square on the component edge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Port</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A named interaction point of the component</td>
    </tr>
  </tbody>
</table>

For example, the Order component requires a Payment interface, and the Payment component provides it. The Order component does not know how payment is implemented, so a different payment provider can be substituted if it provides the same interface. This is the basis of loose coupling, a principle covered in the design principles unit.

## What Component Diagrams Show and Do Not Show

They show the **major building blocks**, their dependencies, and where interfaces lie. They do not show internal classes or the order of calls. A good diagram has a small number of components, often five to twelve, with clear names and meaningful interfaces. Too many components produce a tangle, which is itself a warning sign about the design.

## Deployment Diagrams

A deployment diagram describes the **runtime** environment.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A three-dimensional box</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A physical or virtual computing resource where software runs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Device</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A node labelled as a device</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physical hardware, such as a phone or server</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Execution environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A node inside another node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software that hosts other software, such as an operating system or web server</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Artifact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rectangle with an artifact symbol, placed inside a node</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A deployable file or package, such as an application or a configuration file</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communication path</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A line between nodes, labelled with the protocol</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How nodes talk to each other, such as HTTPS or a database connection</td>
    </tr>
  </tbody>
</table>

A typical deployment diagram for the ordering system shows: a customer's phone running the mobile application, connected over HTTPS to an application server hosting the order and menu services, which connect to a database server holding the data and to an external payment service.

## Why Deployment Matters

- **Performance and capacity**: where components run determines network traffic and delay.
- **Reliability**: it shows where there are single points of failure and where redundancy is needed.
- **Security**: it shows boundaries between zones, such as public network, application, and data.
- **Operations**: teams use it to plan installation, monitoring, and scaling.
- **Cost**: the number and type of nodes determine infrastructure cost.

## Logical and Physical Views Together

Components are a **logical** organisation: what the parts are. Deployment is a **physical** one: where they run. The same logical component might run on one server in a small installation and on many servers in a large one. The two diagrams are linked by showing which artifacts, such as the packaged Order component, are placed on which nodes.

## Modern Variations

Cloud and container technology changes the picture without changing the idea. Nodes may be containers, virtual machines, or managed cloud services, and many components are independently deployed services. The questions remain: what are the parts, what do they offer each other, where do they run, and how do they communicate?

<!--
IMAGE PROMPT  ->  generate as images/02_component_and_deployment_views.png   (16:9 explanatory diagram, place here)

Top: a component diagram with Menu, Order, Payment, Notification components joined by lollipop and socket connectors; Order requires Payment interface. Bottom: a deployment diagram with Phone, Application server, Database server nodes, artifacts inside nodes, and HTTPS and database connection labels. Dotted lines show which component is deployed on which node.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Component or Deployment?

1. Which diagram shows that the Order part needs a Payment interface?
2. Which diagram shows that the database runs on a separate server from the application?
3. Why does connecting through interfaces make a component replaceable?

The first is a component diagram, which shows required and provided interfaces. The second is a deployment diagram, which shows nodes and their communication. Connecting through interfaces means that other parts depend only on the promised services, not on the internal implementation, so any component offering the same interface can replace it.

## Conclusion

A component diagram shows the major replaceable parts of a system and the interfaces through which they connect, while a deployment diagram shows the hardware and execution environments on which software artifacts run and how those environments communicate. Together they give the large-scale logical and physical view.

Software almost always stores data. The next topic describes how the data itself is modeled, using entity-relationship diagrams.

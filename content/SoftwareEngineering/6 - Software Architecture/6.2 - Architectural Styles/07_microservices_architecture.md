## Introduction

As systems and organisations grew, the limitations of large monoliths pushed companies to divide applications into many small services that can be built, deployed, and scaled independently. This approach, called microservices, was popularised in the early 2010s by large internet companies and described in a widely read 2014 article by James Lewis and Martin Fowler. It has delivered real benefits at scale, and has also caused many failures where it was adopted without need. The central lesson is that microservices trade one kind of complexity for another.

**Definition:** Microservices architecture is a style in which an application is built as a collection of small, independently deployable services, each organised around a business capability, owning its own data, and communicating with others over a network through well-defined interfaces.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_microservices_architecture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Several small independent boxes labelled Menu, Orders, Payments, Notifications, each with its own small database cylinder, connected by thin message lines, with a gateway box in front receiving client requests.

ON-IMAGE TEXT: show a short bold title "Microservices Architecture" plus only these few labels, large and legible: Small, Independent, Networked. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Characteristics

Lewis and Fowler described common characteristics of the style.

- **Componentisation through services:** the unit of replacement is a service running in its own process.
- **Organised around business capabilities:** services align with what the business does, such as ordering or payments, not with technical layers.
- **Products, not projects:** a team owns a service through its whole life, building and running it.
- **Smart endpoints and simple communication:** logic lives in the services, and the connections between them are simple, such as requests and messages.
- **Decentralised governance:** teams can choose suitable tools for each service within agreed guidelines.
- **Decentralised data management:** each service owns its data and others access it only through the service.
- **Infrastructure automation:** automated building, testing, deployment, and monitoring are essential.
- **Design for failure:** any call may fail, so services must tolerate the failure of others.
- **Evolutionary design:** services are replaced and rewritten as understanding changes.

## Defining Service Boundaries

The hardest decision is where to draw lines. Poor boundaries produce services that must change together and call each other constantly. The guidance from domain-driven design is to align services with **bounded contexts**: areas of the business with a consistent vocabulary and rules. Ordering and delivery may both use the word "address" with different meanings, and each service owns its own meaning. Good services are **cohesive**, with a single business purpose, and **loosely coupled**, with few and stable interactions.

## Benefits

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Benefit</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change to one service can be released without redeploying the others, enabling frequent small releases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Targeted scaling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only the busy services are replicated</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fault isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failure can be contained to one service if others are designed to cope</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technology freedom</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different services can use different languages or storage as appropriate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team autonomy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small teams own services end to end and work with little coordination</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easier replacement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small service can be rewritten without touching the rest</td>
    </tr>
  </tbody>
</table>

## Costs and Challenges

Splitting a system into services converts internal method calls into network calls and brings the problems of distributed systems, the subject of a later topic.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Challenge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributed complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Network delay, partial failure, and retries must be handled everywhere</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction spanning several services cannot use a single database transaction; systems use patterns such as sagas and accept eventual consistency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operational burden</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many services need deployment pipelines, monitoring, logging, and orchestration</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing difficulty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End-to-end behaviour depends on many services; contract testing is needed to keep interfaces compatible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A request crosses many services, requiring distributed tracing to follow</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Versioning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Services change at different times, so interfaces must stay backward compatible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organisational demand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requires mature automation, skills, and team structures</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplication and drift</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared concerns can be repeated or become inconsistent across services</td>
    </tr>
  </tbody>
</table>

## The Distributed Monolith

The worst outcome is a **distributed monolith**: services that are separately deployed but so tightly coupled that they must change and release together, or that share one database. It has all the costs of microservices and none of the benefits. Warning signs are releases that always involve several services, and services that cannot run without many others.

## When to Use Microservices

They suit large systems and organisations where independent teams and scaling really matter, where the domain is well understood so that boundaries can be drawn confidently, and where the organisation has strong automation and operations skills. For small teams and uncertain domains, a modular monolith is usually a better start, with extraction of services later where justified.

<!--
IMAGE PROMPT  ->  generate as images/02_microservices_gateway_and_own_data.png   (16:9 explanatory diagram, place here)

An API gateway receiving requests from clients and routing to Menu, Orders, Payments, and Notification services, each with its own database. A broken line to a single shared database is crossed out in red and labelled Distributed monolith.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Healthy or Not?

1. Two services share one database and either can change any table.
2. The Payments team releases its service on its own several times a week.
3. A single customer request passes through fifteen tiny services, and one slow service delays everything.

Situation 1 is a warning sign of coupling: services should own their data. Situation 2 is a healthy outcome and a main benefit. Situation 3 shows over-fragmentation and the cost of network calls; some services may be better combined.

## Conclusion

Microservices architecture is a style in which an application is built as a collection of small, independently deployable services, each organised around a business capability, owning its own data, and communicating with others over a network through well-defined interfaces. It offers independence and scale in exchange for significant distributed complexity.

Services need ways to talk to one another, and the style of communication shapes the whole system. The next topic describes event-driven and message-based architecture.

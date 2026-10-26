## Introduction

Architects do not choose structures because they are fashionable. They choose them because of what the system must achieve and under what conditions. A system serving a few dozen users on a single site, and a system serving millions across continents, need different architectures even if their features are identical. The factors that push an architecture in one direction or another are called architectural drivers, and the most influential are the quality attributes.

**Definition:** Architectural drivers are the requirements, constraints, and business goals that most strongly influence the architecture, and quality attributes are the measurable properties of a system, such as performance, availability, security, and modifiability, whose required levels determine which structures are suitable.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_architectural_drivers_and_quality_attributes.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four input funnels labelled Functions, Quality attributes, Constraints, Business goals feeding into a central architecture shape, with a dial panel of attributes beside it.

ON-IMAGE TEXT: show a short bold title "Architectural Drivers and Quality Attributes" plus only these few labels, large and legible: Drivers, Qualities, Shape. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Main Drivers

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Driver</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Significant functional requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features that shape the structure, not every feature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real-time order tracking, which requires pushing updates to many users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well the system must perform its functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Respond within 2 seconds at the lunch peak</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed conditions that limit choices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must use the organisation cloud provider, must comply with data-protection law</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business goals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why the organisation is building the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enter new markets within six months, keep operating cost low</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context and environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users, other systems, and organisational factors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration with an existing accounting system; a small team with limited operations experience</td>
    </tr>
  </tbody>
</table>

Requirements that have a profound effect on the architecture are called **architecturally significant requirements**. Only a small fraction of all requirements are significant. Finding them early, and testing the design against them, is a core architectural activity.

## Quality Attributes

Quality attributes describe how well the system performs. The ones most often driving architecture are:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical architectural responses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response time and throughput</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Caching, concurrency, efficient data access, placing resources close to users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handling growth in load or data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statelessness, horizontal scaling, partitioning data, load balancing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of time the system works</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundancy, failover, health monitoring, avoiding single points of failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correct operation over time; behaviour under faults</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retries, timeouts, redundancy, graceful degradation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protection of data and operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authentication and authorisation, encryption, isolation of sensitive parts, least privilege</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modifiability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of changing the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information hiding, loose coupling, clear interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of verifying the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modular parts, replaceable dependencies, observable behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interoperability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working with other systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standard protocols, well-defined interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of use for the intended people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsive design, fast feedback; affects the interface architecture</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operability and deployability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of running and releasing the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automation, monitoring, small independently releasable parts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Development and running cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple structure, managed services, right-sized infrastructure</td>
    </tr>
  </tbody>
</table>

## Tactics

Architectural **tactics** are design decisions that influence a particular quality attribute. They are a catalogue of proven responses.

- **For availability:** redundant components, heartbeat monitoring, automatic failover, retries.
- **For performance:** caching, load balancing, reducing the work per request, processing in parallel.
- **For security:** authenticating users, encrypting data, limiting access, detecting attacks, auditing.
- **For modifiability:** encapsulating likely changes, using intermediaries, deferring decisions to configuration.
- **For testability:** isolating components, providing test hooks and observability.

## Stating Quality Attributes Precisely

As in the requirements unit, vague goals cannot drive design. A **quality attribute scenario** states a goal in six parts.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example for performance</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who or what triggers it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers using the mobile app</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stimulus</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The event or request</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Submit an order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Artifact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The part of the system affected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The lunch peak, 2,000 simultaneous users</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the system does</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirms the order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well, measurable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Within 2 seconds for 95 percent of requests</td>
    </tr>
  </tbody>
</table>

## Prioritising and Trade-offs

Qualities conflict. Greater security can reduce usability, higher availability costs more, and flexibility can reduce performance. An architecture cannot maximise everything, so the key task is to **rank the qualities** with stakeholders. A common tool is the **utility tree**: list the quality attributes, break each into concrete scenarios, and rate each scenario for importance to the business and for difficulty of achieving. Scenarios rated high on both most strongly drive the architecture.

## Constraints and Business Goals

Constraints are not negotiable in the way preferences are. A requirement to use a particular platform or to keep data in a specific country excludes some options. Business goals, such as speed to market or minimising cost, sometimes outweigh technical elegance. A startup racing to validate an idea needs a different architecture from a bank protecting transactions. Being explicit about these goals prevents building the wrong kind of excellence.

<!--
IMAGE PROMPT  ->  generate as images/02_utility_tree.png   (16:9 explanatory diagram, place here)

A utility tree: root Quality at the top, branches Performance, Availability, Modifiability, Security, each with one concrete scenario leaf rated with importance and difficulty badges (High/Medium/Low). The leaves rated High-High are highlighted as architecturally significant.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Identify the Driver

1. The service must remain available during a meal rush even if one server fails.
2. The system must store personal data only in a specific country.
3. The company wants to add new payment methods quickly each quarter.

Item 1 is an availability quality attribute, answered with redundancy and failover. Item 2 is a constraint that limits where data may be stored. Item 3 is a modifiability quality attribute, linked to the business goal of fast change, and answered by hiding payment providers behind an interface.

## Conclusion

Architectural drivers are the requirements, constraints, and business goals that most strongly influence the architecture, and quality attributes are the measurable properties of a system, such as performance, availability, security, and modifiability, whose required levels determine which structures are suitable. Stating them as measurable scenarios and ranking them is the starting point of architecture.

With the drivers understood, the rest of this unit presents common architectural styles. The first and most widely used is the layered style.

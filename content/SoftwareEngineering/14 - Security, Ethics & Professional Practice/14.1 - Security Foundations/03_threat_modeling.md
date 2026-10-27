## Introduction

Defending a system requires knowing what it must be defended against. Threat modelling is a structured way of thinking about a system as an attacker would: what is valuable, how the system is put together, where it can be attacked, what could go wrong, and what to do about it. It is done on paper or on a whiteboard, before anything is built or while changes are still cheap, and it turns the broad worry of "is it secure?" into a concrete list of threats, each with a decision.

This topic explains the questions threat modelling answers, how to describe a system with data-flow diagrams and trust boundaries, the STRIDE classification of threats, how to rate and respond to them, and how to make the practice routine.

**Definition:** Threat modelling is a structured analysis of a system's assets, structure, and attack surfaces to identify the ways in which it could be attacked or misused, to assess the importance of those threats, and to decide on controls that reduce the resulting risk.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_threat_modeling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A data-flow diagram with an external user box, a process circle, and a data store, a dashed boundary line separating the outside from the inside, and six small icon tags around it for the STRIDE categories.

ON-IMAGE TEXT: show a short bold title "Threat Modeling" plus only these few labels, large and legible: Draw It, Break It, Fix It. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Four Questions

A widely used summary, from Adam Shostack, frames threat modelling as four questions.

1. **What are we building?** Describe the system.
2. **What can go wrong?** Identify threats.
3. **What are we going to do about it?** Choose controls and decisions.
4. **Did we do a good job?** Check the analysis and the result.

## Step 1: Understand What Is Being Protected and Who Might Attack

- **List the assets:** data (personal, financial, credentials), functions (payment, administration), and services.
- **Identify attackers:** who would want it, with what skill and access (see the previous topics).
- **State assumptions** and the scope of what is being analysed.

## Step 2: Model the System

A **data-flow diagram (DFD)** shows how information moves. Its elements are few.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External entity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A person or system outside the control of the design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer, payment provider, administrator</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Something that transforms data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web application, order service, background job</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data store</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where data rests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database, file storage, cache, log</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data flow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Movement of data between elements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Request, response, message, file transfer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trust boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A line across which the level of trust changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internet to server, web tier to database, one organisation to another, user to administrator</td>
    </tr>
  </tbody>
</table>

**Trust boundaries** are the most valuable part of the model. Whenever data crosses a boundary, it must be treated with suspicion: it may have been tampered with, it may be from someone who is not who they claim, and the receiver should check what it accepts. Most threats concentrate at these crossings.

Diagrams can be drawn at several levels, starting with an overview and adding detail for the sensitive parts. They should be simple enough to read in a meeting. Other views are also useful, such as sequence diagrams for authentication flows and deployment diagrams for where components run.

## Step 3: Find Threats with STRIDE

STRIDE, devised by Loren Kohnfelder and Praerit Garg at Microsoft in 1999, is a mnemonic for six categories of threat. Each violates a security property.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Letter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Threat</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property violated</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question to ask</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical controls</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spoofing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authentication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can someone pretend to be another user or system?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using a stolen password; forged service request</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong authentication, mutual authentication of services</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">T</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tampering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can data or code be changed without permission?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Altering a price in a request; modifying a stored record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Input validation, integrity checks, signatures, access control</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repudiation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-repudiation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can someone deny having done something, with no evidence either way?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A user denies a transaction; an administrator changes a record untraceably</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secure audit logs, timestamps, signing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information disclosure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can data be seen by those who should not see it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verbose error message; unprotected backup; open storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encryption, access control, minimising data, careful errors</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">D</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Denial of service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can the service be made unavailable?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flooding; expensive request repeated; resource exhaustion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rate limiting, quotas, scaling, timeouts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">E</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elevation of privilege</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authorisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can someone gain rights they should not have?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A normal user reaching an administrator function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Least privilege, authorisation checks on every request, isolation</td>
    </tr>
  </tbody>
</table>

The usual method is to take each element of the diagram, especially each element and flow that crosses a trust boundary, and ask the six questions. Different elements are subject to different threats: external entities can be spoofed or repudiate; processes face all six; data stores are exposed to tampering, disclosure, and denial; data flows to tampering, disclosure, and denial.

### Other Approaches

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attack trees</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The goal of the attacker is the root; branches show alternative ways of achieving it, each broken down into sub-steps. Introduced by Bruce Schneier</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PASTA (Process for Attack Simulation and Threat Analysis)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A risk-centred seven-stage process linking business objectives to technical threats</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">LINDDUN</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A framework for privacy threats: linking, identifying, non-repudiation, detecting, data disclosure, unawareness, non-compliance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kill chain and MITRE ATT&amp;CK</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Catalogues of how real attackers proceed, step by step, useful for defence planning</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misuse cases and abuse stories</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scenario-based thinking in the language of requirements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Card games and workshops</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Games such as Elevation of Privilege structure brainstorming for teams</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checklists</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lists of known weaknesses, such as the OWASP Top 10, applied to each component</td>
    </tr>
  </tbody>
</table>

## Attack Surfaces

The **attack surface** is every place where an attacker can interact with the system: user interfaces, programming interfaces, network ports, file uploads, administrative consoles, message queues, third-party integrations, mobile app internals, and even people and processes (support staff, deployment pipelines). Mapping it shows where to concentrate defences, and reducing it is among the most effective measures: remove features, close ports, disable default accounts, and expose only what is needed.

## Step 4: Rate and Prioritise Threats

Not all threats warrant equal attention. Common aids:

- **Likelihood and impact** ratings (high, medium, low) placed on a matrix, as in risk management (Unit 13).
- **DREAD,** an older scheme scoring damage, reproducibility, exploitability, affected users, and discoverability. It is now regarded as inconsistent and less used.
- **CVSS** for known vulnerabilities.
- **Business context:** which assets matter most and what the regulators require.

## Step 5: Decide What to Do

For each significant threat, choose one of the standard responses (see risk management in Unit 13).

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Response</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mitigate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add or strengthen a control to reduce likelihood or impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Require multi-factor authentication for administrators</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eliminate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the feature or data that creates the threat</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop storing card numbers; delegate to a payment provider</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transfer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pass the risk to another party</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a certified payment service; insurance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consciously decide to live with a residual risk, recorded with an owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A low-impact threat where the control is too costly</td>
    </tr>
  </tbody>
</table>

Controls follow from secure design principles: authentication, authorisation, input validation, encryption, logging, rate limiting, isolation, and so on, all described in the next topics. Each decision is recorded, becoming a requirement or a task in the backlog and, later, a test.

## Step 6: Validate and Maintain

- **Review** the model with people who know the system, and with a security specialist where the risk is high.
- **Turn threats into tests** and review items.
- **Update the model** whenever the architecture, data, or integrations change; a threat model that is out of date gives false comfort.
- **Keep it lightweight.** For a small change, a half-hour conversation around a whiteboard sketch may suffice. A diagram, a list of threats, the decisions taken, and the open items is a complete record.

## Worked Idea: A Food-Ordering System

Consider the meal-ordering system used throughout this course. The overview diagram has the customer's phone, a web API, an order service, a payment provider, and a database, with trust boundaries between the phone and the API, the API and the internal services, and the system and the payment provider.

- **Spoofing:** can someone place an order as another customer? Control: authentication on every request.
- **Tampering:** can the customer change the price field in the order request? Control: the server calculates prices from its own data and ignores any price sent by the client.
- **Repudiation:** can a customer deny placing an order, or staff deny a refund? Control: audit records of orders and refunds.
- **Information disclosure:** can one customer read another's order by changing the order number? Control: check ownership on every access; use hard-to-guess identifiers.
- **Denial of service:** can a script submit thousands of orders and block the kitchen? Control: rate limits and order validation.
- **Elevation of privilege:** can a customer reach the staff dashboard? Control: role checks on every administrative function.

Each is a design question answered before coding, and each becomes a test.

## Common Mistakes

- Doing it once and never again.
- Modelling only the technology and forgetting people and processes.
- Skipping trust boundaries.
- Listing threats but making no decisions or assigning no owners.
- Making it so heavy that teams avoid it.
- Treating it as a specialist activity done to the team, rather than by the team.

<!--
IMAGE PROMPT  ->  generate as images/03_data_flow_diagram_and_stride.png   (16:9 explanatory diagram, place here)

Left: a simple data-flow diagram of customer, web API, order service, database and payment provider with two dashed trust boundaries and red lightning marks where flows cross them. Right: six STRIDE tiles (S, T, R, I, D, E) each with a one-word property label below.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Think Like an Attacker

1. A mobile app sends the price of an item to the server with each order. Which STRIDE category applies, and what is the remedy?
2. Why are trust boundaries the most important part of a data-flow diagram?
3. When should a threat model be updated?

For case 1, tampering: the server should never trust a client-supplied price and should compute it from its own data. For case 2, because data crossing a boundary moves between different levels of trust, and most attacks happen at those crossings. For case 3, whenever the architecture, data handled, integrations, or deployment change significantly, and periodically in any case.

## Conclusion

Threat modelling is a structured analysis of a system's assets, structure, and attack surfaces to identify the ways in which it could be attacked or misused, to assess the importance of those threats, and to decide on controls that reduce the resulting risk. Describing the system, applying STRIDE at the trust boundaries, and recording decisions produce a plan that engineers can act on.

Many threats follow familiar patterns that appear again and again in real software. The next chapter turns to these common weaknesses and the defences against them, beginning with the OWASP Top 10.

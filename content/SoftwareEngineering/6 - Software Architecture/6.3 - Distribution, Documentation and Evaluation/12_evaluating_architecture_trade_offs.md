## Introduction

Architectural decisions are expensive to reverse, so it is valuable to test them before committing: will this structure achieve the performance, security, and flexibility the system needs, and what does it sacrifice? Evaluation cannot give certainty, but it can expose risks early, make trade-offs explicit, and prevent a team from discovering a fatal weakness after the system is built.

**Definition:** Architecture evaluation is the practice of examining a proposed or existing architecture against its quality goals, using scenarios, analysis, and experiments, to identify risks, trade-offs, and sensitivities, so that decisions are made with their consequences understood.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_evaluating_architecture_trade_offs.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A balance scale with quality attribute weights on both pans labelled Performance, Security, Modifiability, Cost, and an inspector with a clipboard noting risks beside an architecture diagram.

ON-IMAGE TEXT: show a short bold title "Evaluating Architecture Trade-offs" plus only these few labels, large and legible: Scenarios, Risks, Trade-offs. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Is Being Evaluated

Evaluation asks whether the architecture:

- **meets the quality attribute goals** that were identified as drivers
- **handles the most important scenarios,** including failure and change
- **has acceptable risks,** and what they are
- **balances competing qualities** in a way stakeholders accept
- **is feasible** within the budget, schedule, and skills available
- **is consistent** with its documented principles

## Quality Attribute Scenarios as Test Cases

The scenarios introduced earlier in the unit give evaluation its substance. Each one states a source, stimulus, artifact, environment, response, and measurable response. The evaluators walk through the architecture and ask whether it can deliver the response.

Example scenarios:

- **Performance:** at the lunch peak, 2,000 users submit orders, and the system confirms 95 percent of them within 2 seconds.
- **Availability:** a database server fails during peak hours, and the service resumes within 60 seconds with no confirmed order lost.
- **Modifiability:** a developer adds a new payment method in no more than three days, changing only the payment module.
- **Security:** an attacker attempts to read another customer's order, and the system refuses and records the attempt.

## ATAM: A Structured Method

The **Architecture Tradeoff Analysis Method (ATAM)**, developed at the Software Engineering Institute, is a well-known approach. It brings together the architects and stakeholders for a structured review.

1. **Present** the business drivers and the architecture.
2. **Identify the architectural approaches** used, such as layering, queues, or replication.
3. **Generate a utility tree** of quality attributes and refine them into prioritised scenarios.
4. **Analyse the approaches against the scenarios,** identifying how each is satisfied.
5. **Record the findings** using the following terms.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sensitivity point</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A property of the design that is critical to achieving a quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response time depends heavily on how many calls the order service makes to the menu service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trade-off point</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A decision that affects more than one quality, in opposing directions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encrypting all internal traffic improves security but increases latency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A decision that may lead to an undesirable outcome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only one database server, which would mean total outage if it fails</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A decision judged safe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using a well-proven web framework for the interface</td>
    </tr>
  </tbody>
</table>

6. **Report** the risks, trade-offs, and recommendations, and agree follow-up actions.

Full ATAM takes several days and suits large, high-stakes systems. Lighter versions, such as a half-day workshop on the top five scenarios, give much of the benefit for ordinary projects.

## Other Evaluation Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture review with checklists</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structured questions on structure, qualities, risk, and consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick and broad</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prototype or spike</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a thin, risky slice of the system and measure it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evidence for performance and feasibility questions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Load and failure testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simulate heavy load and component failure on the real design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reveals bottlenecks and fragile points</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost-benefit analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate the cost and expected benefit of each option</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Links decisions to business value</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fitness functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated checks that an architectural property still holds, such as response times or allowed dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevents gradual erosion; used in evolutionary architecture</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review of decision records</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examine whether each decision still matches the context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps decisions current</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysis of change history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Study which parts change together in practice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows real coupling</td>
    </tr>
  </tbody>
</table>

## Making Trade-off Decisions

Trade-offs are not defects: every architecture gives something up. A useful discipline for each significant decision is to:

1. State the **options** being considered, including doing nothing.
2. List the **qualities** each option affects and how.
3. Weigh them against the **prioritised drivers**: which matter most here?
4. Consider **reversibility**: how costly would it be to change this decision later? Prefer to delay hard-to-reverse choices until evidence is available, and to make easily reversed choices quickly.
5. Consider **risk and cost** over the whole life of the system, not only the initial build.
6. **Record** the decision and its rationale.

## Common Mistakes

- **Optimising a single quality** while ignoring the others.
- **Choosing technology first,** because it is fashionable, and justifying it afterwards.
- **Evaluating too late,** when the cost of change is high.
- **Treating estimates as facts,** such as expected load.
- **Ignoring operations and cost,** which often decide the real viability.
- **Never revisiting:** the context changes, and a once-good decision can become poor.

## Evaluation Throughout the Life of the System

Evaluate early on paper, to choose a direction. Evaluate during construction with prototypes and tests, to check assumptions. Evaluate in production with monitoring, to see how the system actually behaves. Finally, evaluate on a regular schedule or when major changes occur, so that the architecture evolves deliberately and remains fit for purpose.

<!--
IMAGE PROMPT  ->  generate as images/02_atam_outputs.png   (16:9 explanatory diagram, place here)

An architecture diagram of a meal ordering system with four coloured callout markers: a blue Sensitivity point on the order-to-menu call, an orange Trade-off point on internal encryption, a red Risk on a single database, and a green Non-risk on the web framework. A prioritised scenario list is on the side.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify the Finding

1. Reducing response time depends critically on caching menu data.
2. Adding redundant database servers improves availability but increases cost and complexity.
3. All order data is stored on a single server with no backup.

Finding 1 is a sensitivity point: a property that is critical for a quality. Finding 2 is a trade-off point, since one decision moves two qualities in opposite directions. Finding 3 is a risk, because failure of that server would cause loss of data and service.

## Conclusion

Architecture evaluation is the practice of examining a proposed or existing architecture against its quality goals, using scenarios, analysis, and experiments, to identify risks, trade-offs, and sensitivities, so that decisions are made with their consequences understood. The aim is not a perfect architecture but one whose compromises are chosen knowingly.

This completes Unit 6. You can now explain what architecture is and how quality attributes drive it, compare layered, client-server, MVC, monolithic, microservice, event-driven, and pipe-and-filter styles, describe the central problems of distributed systems, document an architecture with views and decision records, and evaluate trade-offs. Unit 7 moves from the structure of whole systems to the techniques of object-oriented design and design patterns.

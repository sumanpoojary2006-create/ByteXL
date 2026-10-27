## Introduction

The word "software" covers everything from a small phone game to the control system of a power station. These systems share a discipline but not a level of risk, so applying the same process to all of them would be wasteful for some and dangerous for others.

This topic surveys the main families of software systems and introduces three questions that help an engineer decide how much rigour a system deserves: **who uses it, what does a failure cost, and how fast does it have to change?**

**Definition:** A software system is a collection of programs, data, and configuration that work together to provide some service, and its type is determined by the environment it runs in, the people who depend on it, and the consequences of its failure.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_types_of_software_systems.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A set of icons arranged around a central software symbol: phone app, bank building, heart monitor, game controller, server rack, and satellite.

ON-IMAGE TEXT: show a short bold title "Types of Software Systems" plus only these few labels, large and legible: Web, Embedded, Enterprise. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Major Kinds of Software Systems

- **Web and mobile applications.** Used by many people through a browser or phone and updated often, such as food ordering or social platforms.
- **Enterprise and business systems.** Run an organisation's operations: payroll, inventory, banking, hospital records. They are large, long-lived, and tied to business rules.
- **Embedded and real-time systems.** Run inside devices such as cars, appliances, and medical equipment, with limited memory and strict timing requirements.
- **Data-intensive and analytics systems.** Collect, store, and process large volumes of data, including recommendation engines and machine learning pipelines.
- **System software and infrastructure.** Operating systems, compilers, databases, and cloud platforms that other software is built on.
- **Games and entertainment software.** Heavy on performance and user experience, often released in one big launch and then patched.
- **Scientific and engineering software.** Simulations and calculations where numerical correctness matters more than a polished interface.

## Product Software and Custom Software

Another useful split is by who the customer is.

- **Generic (product) software** is built to be sold to many customers, such as a word processor. The developer decides what to build based on a guess about what many people want.
- **Custom (bespoke) software** is built for one customer, who decides what it should do, such as a government tax portal.

Many real products sit between the two, sold to many customers but customised for each.

## Systems of Systems

Many services are not a single program. A digital payment passes through the payer's app, two banks, a national payment network, and a messaging service. No single team owns the whole chain. A **system of systems** is made of independently built and operated systems that cooperate. These are hard to engineer because nobody controls all the parts, and a fault in one can spread to the others.

## Why the Type Matters: Rigour Should Match Risk

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">System</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who is affected by a failure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost of failure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How fast it changes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Appropriate rigour</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Food-ordering web app</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users who miss an order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low, easily corrected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weekly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Light reviews, automated tests, fast releases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overnight bank settlement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Millions of account holders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High, financial and legal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slowly, with approvals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heavy testing, audits, careful change control</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medical device firmware</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A patient</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Potentially fatal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rarely, after certification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extensive verification, formal methods, regulatory approval</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mobile game</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Players</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low to moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequent patches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Playtesting, fast fixes, performance tuning</td>
    </tr>
  </tbody>
</table>

Applying surgical-level caution to a menu screen would waste months, and applying menu-screen casualness to a medical device would be dangerous. Good engineers learn to **scale the process to the risk**.

## Your Turn: Classify the System

Name the most fitting family for each system and say whether its failure cost is low, moderate, or severe.

1. The software controlling the airbags in a car.
2. A food delivery app's restaurant search screen.
3. A weather forecasting model run on a supercomputer.

System 1 is an embedded, real-time, safety-critical system, and its failure cost is severe: it must act within milliseconds and cannot be patched casually. System 2 is a web or mobile application with a low failure cost, since a poor search result is annoying but not harmful. System 3 is scientific software with a moderate failure cost: wrong forecasts matter, but the main requirement is numerical correctness, checked by experts.

## Conclusion

A software system is a collection of programs, data, and configuration that work together to provide some service, and its type is determined by the environment it runs in, the people who depend on it, and the consequences of its failure. The type tells you how much rigour to apply.

With the nature of the discipline, its history, its failure modes, and the kinds of systems established, the next chapter turns to how the work itself is organised, beginning with the stages every system passes through.

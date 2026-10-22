## Introduction

Three messages arrived in Ananya's inbox in the same week. A former classmate invited her to join a team writing firmware for a heart monitor. A bank recruiter asked if she would consider a role maintaining the system that settles card transactions overnight. And her own team at CampusConnect wanted a decision about how carefully to review a change to the mess menu screen.

All three are "software jobs." Ananya wondered how the same word could cover work that feels so different. Vikram suggested a way to compare them: ask three questions of any system. **Who uses it? What does a failure cost? How fast does it have to change?**

**Definition:** A software system is a collection of programs, data, and configuration that work together to provide some service, and its type is determined by the environment it runs in, the people who depend on it, and the consequences of its failure.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_types_of_software_systems.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya stands at a crossroads with three glowing paths: a phone showing a mess-menu app, a heart monitor, and a bank building, with Vikram holding a signpost reading Who, Cost, Change.

ON-IMAGE TEXT: show a short bold title "Types of Software Systems" plus only these few labels, large and legible: Web, Embedded, Batch. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Major Kinds of Software Systems

Software comes in many families. These are the ones a beginner is most likely to meet.

- **Web and mobile applications.** Used by many people through a browser or phone, updated often. The CampusConnect app belongs here.
- **Enterprise and business systems.** Run an organisation's operations: payroll, inventory, banking, hospital records. They are large, long-lived, and tied to business rules.
- **Embedded and real-time systems.** Run inside devices such as cars, washing machines, and medical equipment. They have limited memory and must respond within strict time limits.
- **Data-intensive and analytics systems.** Collect, store, and process huge volumes of data, including recommendation systems and machine learning pipelines.
- **System software and infrastructure.** Operating systems, compilers, databases, and cloud platforms that other software is built on.
- **Games and entertainment software.** Heavy on performance and user experience, often released in a big launch and then patched.
- **Scientific and engineering software.** Simulations and calculations where correctness of numbers matters more than a polished interface.

## Product Software and Custom Software

Another useful split is by who the customer is.

- **Generic (product) software** is built to be sold to many customers: a word processor, a messaging app. The developer decides what to build, based on a guess about what many people want.
- **Custom (bespoke) software** is built for one customer, who decides what it should do: a hospital's patient system, a government tax portal.

CampusConnect sits in between. It sells one product to twelve colleges, but each college asks for its own changes.

## Systems of Systems

Many real services are not a single program. When you pay with UPI, your phone app talks to your bank, the receiver's bank, a national payment network, and a messaging system. No single team owns the whole chain. A **system of systems** is made of independently built and operated systems that cooperate. These are hard to engineer because nobody controls all the parts, and a fault in one can spread to others.

<!--
IMAGE PROMPT  ->  generate as images/05_system_of_systems_payment.png   (16:9 explanatory diagram, place here)

A phone on the left connected through arrows to a bank, a payment network, a second bank, and an SMS service, each in its own coloured box, showing independent systems cooperating to complete one payment.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Why the Type Matters: Rigour Should Match Risk

The type of system determines how much engineering effort is appropriate.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mess-menu web app</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Students who miss one meal choice</td>
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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heart monitor firmware</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A patient</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Potentially fatal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rarely, after certification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formal methods, extensive verification, regulatory approval</td>
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

Applying surgical-level caution to a mess-menu screen would waste months. Applying mess-menu-level casualness to a heart monitor would be dangerous. Good engineers learn to **scale the process to the risk**.

## Your Turn: Classify the System

Name the most fitting family for each system and say whether its failure cost is low, moderate, or severe.

1. The software controlling the airbags in a car.
2. A food delivery app's restaurant search screen.
3. A weather forecasting model run on a supercomputer.

System 1 is an embedded, real-time, safety-critical system, and its failure cost is severe: it must fire within milliseconds and cannot be patched casually. System 2 is a web or mobile application with a low failure cost, because a poor search result is annoying but not harmful. System 3 is scientific software, and its failure cost is moderate: wrong forecasts matter, but the main requirement is numerical correctness and the results are reviewed by experts.

## Conclusion

A software system is a collection of programs, data, and configuration that work together to provide some service, and its type is determined by the environment it runs in, the people who depend on it, and the consequences of its failure. The type tells you how much rigour to apply.

Ananya has now seen what software engineering is, where it came from, how projects fail, and what kinds of systems exist. The next chapter looks at how the work itself is organised: the stages every system moves through, and the people who carry them out.

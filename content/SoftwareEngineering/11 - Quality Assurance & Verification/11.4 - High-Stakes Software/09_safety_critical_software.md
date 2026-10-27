## Introduction

Most software failures cost time, money, or reputation. A few kinds of software can cost lives. The programs that fly aircraft, control railway signals, regulate insulin pumps, steer vehicles, run nuclear plants, and guide radiation machines belong to a category in which an error can injure or kill. Societies expect such software to be built with a different standard of care, and regulators in each industry enforce it. Unit 1 observed that rigour should be matched to risk. This topic explains what that means at the high end: how hazards are analysed, how safety is argued, and how the engineering practices change.

**Definition:** Safety-critical software is software whose failure or incorrect behaviour could cause death, injury, serious damage to health or the environment, or catastrophic loss, and safety engineering is the discipline of identifying hazards, assessing and reducing risk, and demonstrating with evidence that the system is acceptably safe.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_safety_critical_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four domain icons around a central software chip: an aircraft, a train, a medical pump, a car, with layered shield rings labelled Hazard analysis, Redundancy, Verification, Certification.

ON-IMAGE TEXT: show a short bold title "Safety-Critical Software" plus only these few labels, large and legible: Hazard, Defence, Evidence. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Safety, Reliability, and Security

The three are related but different.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the system do what is required, continuously?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A reliable system can still be unsafe if its requirements are wrong or if reliable behaviour is itself hazardous</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can the system cause harm?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concerned with avoiding accidents, including those caused by correct operation in unexpected situations</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can the system be attacked or misused?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A security breach can create safety hazards, as when attackers alter controls, so the two increasingly overlap</td>
    </tr>
  </tbody>
</table>

Nancy Leveson, a leading figure in the field, argues that **safety is a property of the whole system**, including hardware, software, people, and organisation, and not of the software alone. Software on its own is neither safe nor unsafe; it becomes so in the context of what it controls.

## Domains and Their Standards

Each industry has its own regulatory framework, and most standards share ideas.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Domain</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Standards and bodies (examples)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Levels used</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">General electrical and programmable systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">IEC 61508</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety integrity levels SIL 1 to 4</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aviation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DO-178C for airborne software, with regulators such as the FAA and EASA</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software levels A (catastrophic failure effect) to E (no effect)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automotive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO 26262</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automotive safety integrity levels ASIL A to D</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medical devices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">IEC 62304, with regulators such as the FDA</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software safety classes A, B, C</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Railways</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EN 50128 and related standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety integrity levels</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nuclear</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">IEC 60880 and national regimes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Categories by safety function</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Space</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agency standards (NASA, ESA)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Criticality categories</td>
    </tr>
  </tbody>
</table>

The higher the level, the **more rigorous the required evidence**: for example, at the highest aviation level, DO-178C requires modified condition/decision coverage in testing, independent verification, and detailed traceability from requirements to code and tests.

## Hazard and Risk Analysis

Safety engineering begins before design, by asking what can go wrong and how bad it would be.

- A **hazard** is a condition that could lead to harm, such as "the infusion pump delivers too much drug."
- **Risk** combines the **likelihood** of the hazard leading to an accident and the **severity** of the harm.
- The aim is to reduce risk to a level that is acceptable, often described as **as low as reasonably practicable.**

### Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preliminary hazard analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">List potential hazards early, from the purpose and environment of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FMEA (failure modes and effects analysis)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For each component, list the ways it can fail, the effects on the system, and the severity, likelihood, and detectability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bottom-up analysis of components</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fault tree analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start from a hazardous event and work backwards through the combinations of faults that could cause it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Top-down analysis of causes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">HAZOP (hazard and operability study)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A team applies guide words such as "no," "more," "less," "late" to each part of a process or design to find deviations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systematic exploration</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">STPA (systems-theoretic process analysis)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developed by Leveson; models the system as control loops and finds unsafe control actions, including ones from design flaws and interactions with no component failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex software-intensive systems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event tree analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follows the consequences of an initiating event through the success or failure of safeguards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consequence analysis</td>
    </tr>
  </tbody>
</table>

The outputs are **safety requirements:** specific, testable requirements for the system to prevent or mitigate each hazard, which then flow into design and verification, with traceability in both directions, as Unit 3 described.

## Design for Safety

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplicity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity breeds faults; keep safety functions simple and small</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fail-safe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When something fails, the system moves to a safe state, such as stopping a train or closing a valve</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fail-operational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For functions that cannot simply stop, such as flight control, continue to operate despite failure, using redundancy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defence in depth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Multiple independent layers of protection, so that no single failure causes an accident, as in the Swiss cheese model of Unit 1</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundancy and diversity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate components, and where possible use different designs, hardware, or software, so a common fault does not defeat both</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independence of safety functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep safety monitoring separate from the control it protects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hardware interlocks and independent protection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not rely on software alone for the most dangerous hazards, a lesson of the Therac-25 in Unit 1</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Watchdogs and self-checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detect stuck or faulty behaviour and take safe action</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit and bound</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restrict values, rates, and ranges to safe limits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Human factors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design interfaces and procedures that prevent operator error and resist automation surprise</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deterministic, analysable behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predictable timing and memory use; avoid dynamic features that cannot be bounded</td>
    </tr>
  </tbody>
</table>

## Coding and Process Practices

- **Restricted coding standards** limit the use of risky language features. MISRA C is a well-known example for the automotive and other industries.
- **Strong static analysis** and in some cases formal verification, as in the previous topics.
- **Rigorous testing** to coverage criteria such as MC/DC, plus testing of failure and recovery behaviour.
- **Independent verification and validation (IV&V):** people independent of the developers check the work.
- **Traceability** from hazards through requirements, design, code, and tests, so that every safety requirement is shown to be implemented and verified.
- **Tight configuration and change control,** as in Unit 8; any change is analysed for safety impact.
- **Qualification of tools** such as compilers and test tools whose faults could hide or introduce defects.
- **Document-driven processes** with reviews and inspections at each stage, in the manner of the V-model of Unit 2.

## The Safety Case

Regulators and customers need to be convinced that the system is safe. A **safety case** (or assurance case) is a structured, documented argument, supported by evidence, that the system is acceptably safe for its intended use in its environment.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Claim</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A statement to be shown, such as "the system does not deliver an overdose"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Argument</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The reasoning that supports the claim, often by breaking it into sub-claims</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analyses, test results, proofs, reviews, field experience that support the sub-claims</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context and assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The conditions under which the case holds</td>
    </tr>
  </tbody>
</table>

Notations such as Goal Structuring Notation draw the argument as a tree. A strong safety case also considers **what could undermine it** and states the limits of the evidence. It is a living document, updated as the system changes and as experience accumulates.

## Certification and Regulation

Many safety-critical systems must be **certified** or **approved** by a regulator before use, on the basis of evidence of conformance to standards and of the safety case. Regulators may audit the development, review the evidence, and require monitoring in service, reporting of incidents, and updates. Certification adds time and cost, and changes to certified software must be controlled and, often, re-approved.

## Culture

Standards and techniques are necessary but not sufficient. Industries with strong records, such as commercial aviation, combine them with a **safety culture**:

- open reporting of incidents and near misses, with protection for those who report
- learning from failures across the whole industry
- questioning attitudes, and authority to stop work on safety grounds
- resistance to the **normalisation of deviance**, described by the sociologist Diane Vaughan in her study of the Challenger shuttle accident: the gradual acceptance of warning signs as normal until disaster strikes
- management that does not trade safety for schedule

## Agile and Safety-Critical Work

Safety-critical development has been seen as the home ground of plan-driven methods, as Unit 2 noted, but many organisations now combine iterative practices with the documentation, traceability, and analysis that standards demand. The key is to keep **safety analysis and evidence continuously up to date** in each iteration, not to postpone it.

## Proportion

Not all software needs this rigour, and applying it everywhere would be wasteful. The art is to **recognise which parts of a system are safety-relevant,** isolate them, and apply the highest rigour to them, while treating the rest at a lower level. A well-chosen architecture limits the amount of software that needs the most expensive assurance.

<!--
IMAGE PROMPT  ->  generate as images/02_hazard_to_safety_case_flow.png   (16:9 explanatory diagram, place here)

A flow: Hazard analysis (FMEA and fault tree icons), Safety requirements, Design with defence in depth layers, Verification (tests, proofs, inspection), Safety case (claim, argument, evidence tree), Certification stamp. A traceability line runs under the whole flow.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Apply Safety Thinking

1. A hazard analysis for an infusion pump lists "pump delivers too much drug." What should follow?
2. A control system has a single sensor and no cross-check. What principle is violated?
3. When a train control system detects an internal fault, it brings the train to a stop. What design principle is this?

After identifying the hazard, assess the risk by likelihood and severity, derive safety requirements and protections, such as limits, independent monitoring, and alarms, and trace them through design and verification. A single sensor violates redundancy and independence: a fault in one sensor can lead to a hazardous action, and cross-checking against a second is needed. Stopping on a detected fault is fail-safe behaviour.

## Conclusion

Safety-critical software is software whose failure or incorrect behaviour could cause death, injury, serious damage to health or the environment, or catastrophic loss, and safety engineering is the discipline of identifying hazards, assessing and reducing risk, and demonstrating with evidence that the system is acceptably safe. It combines systematic hazard analysis, defence in depth, rigorous verification, a reasoned safety case, and above all a culture of learning from failure.

The last topic of this unit draws on that culture. It examines failures that have already happened and asks what they teach.

## Introduction

Every piece of software contains mistakes. They come from misunderstood requirements, overlooked cases, wrong assumptions, and ordinary human error, and they occur in the work of the most experienced engineers. The question is not whether defects exist but whether they are found before users find them. Testing is the activity that looks for them. It is also the main source of the confidence that lets a team change software without fear, which makes it central to everything in the previous units, from continuous delivery to refactoring.

**Definition:** Software testing is the process of executing a program, or examining its work products, with the intention of finding defects, evaluating its quality, and gaining justified confidence that it behaves as intended, so that decisions about releasing it are based on evidence.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_why_test_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A magnifying glass inspecting a block of software, finding small bug icons, with a scale on the side weighing Risk of defects against Cost of testing, and a green confidence meter rising.

ON-IMAGE TEXT: show a short bold title "Why Test Software" plus only these few labels, large and legible: Find, Trust, Decide. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Testing Is For

Testing has several purposes, and a good team holds all of them in mind.

- **Finding defects** so that they can be fixed before release, when they are cheaper to repair and cannot harm users.
- **Building confidence** that the software meets its requirements and works in realistic conditions.
- **Preventing defects.** Writing tests early exposes unclear requirements and weak designs, and a test suite prevents old defects from returning.
- **Providing information** to stakeholders about quality and risk, so they can decide whether to release.
- **Reducing risk** to users, the organisation, and sometimes to safety.
- **Enabling change.** A reliable set of tests is the safety net that makes refactoring and frequent release possible.
- **Verifying compliance** with contracts, standards, and regulation.

## The Cost of Defects

The previous units made the point that defects are cheaper to fix when found early. A misunderstanding caught while writing a requirement costs a conversation. The same defect found in production costs diagnosis, a fix, a new release, and the damage to users in the meantime. In safety-critical or financial systems, as the failures studied in Unit 1 showed, the cost can be enormous. Testing early and often is therefore an economic decision as well as a technical one.

## A Brief History of "Bugs"

Engineers had used the word "bug" for faults in machinery for a long time, and it was used by Thomas Edison in the nineteenth century. A famous entry in 1947 on the logbook of the Harvard Mark II computer records an actual moth found in a relay, taped into the book with the note "first actual case of bug being found," a remark attributed to the team that included Grace Hopper. The word has stayed, though most software defects are of course not insects but human mistakes.

## Seven Principles of Testing

Decades of experience have been condensed into a short list of principles, popularised by the International Software Testing Qualifications Board.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing shows the presence of defects, not their absence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests can reveal bugs but can never prove that none remain. Edsger Dijkstra made the point in a famous remark</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exhaustive testing is impossible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Even a small program has more input combinations than could be tried. Effort must be focused by risk and priority</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early testing saves time and money</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starting test activities in requirements and design finds problems when they are cheapest to fix</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects cluster together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small number of modules usually contain most of the defects, so effort should follow the evidence</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The pesticide paradox</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running the same tests repeatedly stops finding new bugs; tests must be reviewed and varied</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing is context dependent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A medical device and a game call for different kinds and amounts of testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absence of errors is a fallacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software with no known bugs is still a failure if it does not meet the needs of users</td>
    </tr>
  </tbody>
</table>

## What Testing Cannot Do

- It **cannot prove correctness.** A passing suite means only that these cases passed.
- It **cannot compensate for poor design** or unclear requirements. Testing a system built to the wrong specification confirms only that it was built wrongly.
- It **is not the same as quality.** Quality is built in through good practice at every stage, a topic of the next unit.
- It **cannot be done fully by one person at the end.** Quality is the responsibility of the whole team.

## Testing, Verification, Validation, and Debugging

These ideas are related but distinct.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question or purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are we building the product right? Does it meet its specification?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Validation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are we building the right product? Does it meet the real needs of users?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running or examining the software to find defects and gather evidence for both</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finding the cause of a failure and fixing it; testing detects the failure, and debugging diagnoses it</td>
    </tr>
  </tbody>
</table>

## Who Tests

In the past, testing was a separate phase carried out by a separate team after development. Modern practice spreads it across the whole life cycle.

- **Developers** write unit and integration tests as they work.
- **Testers (quality engineers)** bring a specialist's skills in test design, exploration, and automation, and an independent viewpoint.
- **Product owners and users** take part in acceptance.
- **Operations staff** contribute through monitoring and production checks.

Independence still has value: fresh eyes find what the author cannot see.

## Testing as Risk Management

Since everything cannot be tested, the central skill is deciding **what matters most**. A useful approach is to consider, for each area, the **likelihood** of failure and the **impact** if it happens. Complex, new, frequently changed, or poorly understood code is likely to fail. Payments, personal data, and safety functions have high impact. Effort goes first to high-likelihood, high-impact areas.

<!--
IMAGE PROMPT  ->  generate as images/02_risk_matrix_for_testing_effort.png   (16:9 explanatory diagram, place here)

A two-by-two grid with Likelihood of failure on one axis and Impact of failure on the other. Quadrants: Test most (high-high, highlighted), Test carefully, Test lightly, Test minimally. Examples placed: payment processing, new pricing rules, a rarely used admin report, a static help page.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Principle or Purpose?

1. A team runs the same set of tests for two years and no longer finds any new defects, though customers report bugs.
2. A product passes all its tests but users find it confusing and stop using it.
3. A team wants to know which modules deserve the most testing time.

Case 1 is the pesticide paradox: the tests need to be reviewed and extended. Case 2 is the absence-of-errors fallacy: the software was verified but not validated against real needs. For case 3, use risk: focus on modules that are complex, changing often, and where failure would hurt most, noting that defects cluster.

## Conclusion

Software testing is the process of executing a program, or examining its work products, with the intention of finding defects, evaluating its quality, and gaining justified confidence that it behaves as intended, so that decisions about releasing it are based on evidence. It cannot prove the absence of defects, so it must be guided by risk and begun early.

To discuss testing precisely, a team needs a shared vocabulary and a picture of how different kinds of tests fit together. The next topic provides both.

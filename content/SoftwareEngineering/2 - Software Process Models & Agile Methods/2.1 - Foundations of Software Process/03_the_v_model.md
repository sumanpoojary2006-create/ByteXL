## Introduction

In a strict waterfall, testing is a single phase near the end, which means that test planning is often left late and defects in early work are found late. The V-model keeps the sequential flow but changes one important thing: every development stage is paired with a matching level of testing that is planned at the same time.

**Definition:** The V-model is a sequential process model in which each development phase on the way down is paired with a corresponding verification or validation phase on the way up, so that test planning begins as soon as the related requirements or design are written.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_the_v_model.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A V-shaped diagram: development stages descending on the left, coding at the bottom, and four matching test levels ascending on the right, joined by horizontal dotted lines.

ON-IMAGE TEXT: show a short bold title "The V-Model" plus only these few labels, large and legible: Left, Right, Pairs. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Shape of the V

The left arm descends through development, the point of the V is implementation, and the right arm ascends through testing. Horizontal links connect each stage to the test level that checks it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Development stage (left)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Matching test level (right)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What the test checks</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business and user requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the system meet the real needs of its users?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">System requirements and specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">System testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the complete system behave as specified?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture and high-level design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do the major parts work correctly together?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed design of each component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component (unit) testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does each small part behave as designed?</td>
    </tr>
  </tbody>
</table>

## Verification and Validation

The V-model makes a useful distinction that applies to all software.

- **Verification** asks: "Are we building the product right?" It checks that work meets its specification, for example that code matches the design.
- **Validation** asks: "Are we building the right product?" It checks that the finished software meets the real needs of its users.

Lower levels of the V are mostly verification, and the top level, acceptance testing, is validation.

## Test Planning Starts Early

The main benefit of the V is that **tests are designed alongside the requirement or design they check**. Writing an acceptance test while writing a requirement exposes vagueness immediately: a requirement that cannot be turned into a test is probably unclear. By the time the code exists, the test plans for every level are already prepared.

## Strengths and Limitations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing is planned from the start instead of squeezed in at the end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Still sequential, so late feedback from real users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each stage has a clear, checkable output</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes to requirements force rework of designs and test plans</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disciplined and easy to audit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No working software until the right arm of the V is reached</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fits regulated and safety-related domains</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Little room for learning and adjusting along the way</td>
    </tr>
  </tbody>
</table>

## Where the V-Model Is Used

The model is common in domains where documentation, traceability, and formal verification are required: automotive, aerospace, medical devices, and government systems. Standards in these domains often expect evidence that every requirement is linked to at least one test, which the V structure produces naturally.

## Your Turn: Match the Test to the Stage

Match each description to the level of the V-model.

1. A tester checks that two separately built subsystems exchange data correctly.
2. Representatives of the customer confirm that the finished system supports their daily work.
3. A developer checks that one small module handles invalid input as its design says.
4. The full system is tested against the written specification in a realistic environment.

Description 1 is integration testing, paired with architecture design. Description 2 is acceptance testing, paired with user requirements, and is validation. Description 3 is component testing, paired with detailed design. Description 4 is system testing, paired with the system specification.

## Conclusion

The V-model is a sequential process model in which each development phase on the way down is paired with a corresponding verification or validation phase on the way up, so that test planning begins as soon as the related requirements or design are written. It improves on waterfall by planning quality early, but it remains a single long pass.

The next topic introduces the idea that fixes the single-pass weakness directly: building the system in repeated cycles that each deliver something usable.

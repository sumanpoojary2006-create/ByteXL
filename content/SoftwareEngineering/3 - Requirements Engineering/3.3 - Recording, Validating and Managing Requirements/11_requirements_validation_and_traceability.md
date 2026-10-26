## Introduction

A requirements document can be well formatted, carefully written, and still describe the wrong system. Validation is the activity of checking that the requirements truly reflect what stakeholders need. Traceability is the discipline of linking each requirement to its origin and to the design, code, and tests that satisfy it, so that nothing is lost, nothing is built without reason, and the effects of change can be seen.

**Definition:** Requirements validation is the process of checking that requirements are correct, complete, consistent, and truly what stakeholders want, and traceability is the ability to follow each requirement forwards to its design, implementation, and tests, and backwards to its source.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_requirements_validation_and_traceability.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A chain of linked blocks from Need to Requirement to Design to Code to Test, with forward and backward arrows, and a magnifying glass checking the Requirement block.

ON-IMAGE TEXT: show a short bold title "Requirements Validation and Traceability" plus only these few labels, large and legible: Check, Link, Trace. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Validation Versus Verification

These words are often confused.

- **Validation** asks: "Are these the right requirements?" It checks the requirements against real stakeholder needs.
- **Verification** asks: "Does the product meet the requirements?" It checks the product against the specification.

Validating requirements early is valuable because a defect found at this stage is far cheaper to remove than one found in a finished system.

## What Validation Checks

- **Validity:** does each requirement meet a real need of some stakeholder?
- **Consistency:** do any requirements conflict?
- **Completeness:** are all needed functions and constraints included?
- **Realism:** can the requirements be implemented within budget, time, and technology?
- **Verifiability:** can each be tested?
- **Comprehensibility:** can the intended readers understand them?

## Validation Techniques

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements reviews and inspections</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A group reads the specification systematically, often with a checklist, and records defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finds many problems cheaply; spreads understanding</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Walkthroughs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The author presents the document to stakeholders who comment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick, informal feedback</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prototyping</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholders try a mock-up or early version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reveals misunderstandings that text hides</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test-case generation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writing tests for each requirement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exposes requirements that cannot be tested</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modelling and simulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysing diagrams or models for gaps and conflicts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finds structural problems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance criteria workshops</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholders agree concrete examples of success</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aligns understanding in concrete terms</td>
    </tr>
  </tbody>
</table>

A review checklist might ask, for each requirement: Is it clear? Is it testable? Does it have a source? Does it conflict with another? Is anything assumed but not written?

## Ambiguity

Ambiguity is the most common defect. Detecting it is helped by having several people independently interpret each requirement and compare their readings. If two readers understand a statement differently, it needs rewriting. Concrete examples and test cases help: if a team cannot agree on the expected output for a given input, the requirement is not yet clear.

## Traceability

Traceability links related items through the project.

- **Backward traceability** links a requirement to its source: a need, a stakeholder, a regulation.
- **Forward traceability** links a requirement to the design elements, code, and tests that implement and verify it.
- **Bidirectional traceability** supports both, so that one can ask "why does this exist?" and "what implements this?"

A simple tool is a **traceability matrix**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Requirement</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Design element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Test case</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FR-01 Place order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need N-1, business goal B-1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">T-01, T-02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implemented, tested</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FR-02 Cancel order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need N-2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">T-03</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implemented</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FR-03 Refund on cancel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need N-2, finance policy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment module</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None yet</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gap: no test</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">NFR-01 Menu within 2 s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business goal B-2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Menu cache</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Load test L-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tested</td>
    </tr>
  </tbody>
</table>

Even this small matrix reveals problems: FR-03 has no test, so it is not verified.

## Benefits of Traceability

- **Completeness:** every requirement is implemented and tested, and gaps are visible.
- **No gold plating:** code or features with no linked requirement are questioned.
- **Impact analysis:** when a requirement changes, the linked design, code, and tests are known.
- **Compliance:** regulated industries must demonstrate that every requirement is verified.
- **Progress tracking:** the proportion of requirements implemented and tested is measurable.

The cost is effort to maintain the links. Teams balance this by tracing at a sensible level of detail, using tools that keep links with the work items, and tracing more strictly where risk or regulation demands it.

<!--
IMAGE PROMPT  ->  generate as images/02_traceability_matrix.png   (16:9 explanatory diagram, place here)

A matrix with requirements as rows and columns for Source, Design, Code, Test. Cells connected by lines, most filled green, one cell empty and highlighted red labelled Gap: no test. Forward and backward arrows on the side.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Find the Gap

Using the traceability idea, identify the problem in each situation.

1. A feature exists in the code that no requirement mentions.
2. A requirement has no linked test.
3. A regulation changes, and nobody knows which requirements it affects.

Situation 1 suggests gold plating or a missing requirement, and should be questioned. Situation 2 means the requirement is unverified, so a test must be written or the requirement is not testable. Situation 3 shows missing backward traceability, since requirements were not linked to their sources.

## Conclusion

Requirements validation is the process of checking that requirements are correct, complete, consistent, and truly what stakeholders want, and traceability is the ability to follow each requirement forwards to its design, implementation, and tests, and backwards to its source. Together they keep the project connected to real needs.

Requirements will still change after they are validated. The final topic of this unit covers how to manage that change.

## Introduction

Agreed requirements need a durable, shared record. When a team grows, when contractors join, when a system must be tested against its specification, or when a dispute arises years later, people turn to the written document. The Software Requirements Specification (SRS) is the traditional form of that record. Even in agile projects, where it may be lighter or take other forms such as a backlog and product documentation, the questions an SRS answers must still be answered.

**Definition:** A software requirements specification is a document that describes completely and precisely what a software system must do and the constraints on it, serving as an agreement among stakeholders and as the basis for design, testing, and acceptance.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_writing_a_software_requirements_specification.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A neatly structured document with three labelled sections, Introduction, Overall description, Specific requirements, with readers around it: customer, designer, tester.

ON-IMAGE TEXT: show a short bold title "Writing a Software Requirements Specification" plus only these few labels, large and legible: Document, Agree, Test. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Purposes and Readers

An SRS serves several readers.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reader</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Uses the SRS to</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers and users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm that the right system will be built</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan, estimate, and control the project</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designers and developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand what to design and build</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Derive tests and decide what counts as correct</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand intended behaviour when changing the system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contract and legal staff</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Establish what was agreed</td>
    </tr>
  </tbody>
</table>

## Standard Structure

Standards such as IEEE 830-1998, later replaced by ISO/IEC/IEEE 29148, suggest outlines. A typical structure is below.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Section</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Contents</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Introduction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose, scope, definitions and abbreviations, references, overview of the document</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Overall description</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product perspective (how it fits with other systems), main functions, user characteristics, constraints, assumptions and dependencies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Specific requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External interfaces (user, hardware, software, communication); functional requirements; performance requirements; design constraints; software quality attributes; other requirements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Appendices and index</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supporting material such as data models, sample layouts, and a glossary</td>
    </tr>
  </tbody>
</table>

The outline is a checklist, not a template to fill blindly. Sections that do not apply are omitted, and sections that matter get more space.

## Qualities of a Good SRS

A good specification as a whole is:

- **Correct:** every requirement states something the system really must do.
- **Unambiguous:** each statement has one interpretation.
- **Complete:** all significant requirements, responses to all inputs, and definitions of terms are included.
- **Consistent:** no requirement contradicts another.
- **Ranked:** importance or stability of each requirement is indicated.
- **Verifiable:** each requirement can be checked by a finite, practical process.
- **Modifiable:** changes can be made easily and consistently, with limited duplication.
- **Traceable:** each requirement has an identifier and a link to its origin and to later work.

## Practical Writing Advice

- **Use a glossary** and keep terms consistent. If "customer" and "user" mean different things, define them.
- **Give every requirement a unique identifier**, so it can be referenced in discussion, design, and tests.
- **State the rationale** for non-obvious requirements, since it prevents later removal of something important.
- **Separate what from how.** The SRS says what the system must do, leaving design choices to designers unless a design constraint is truly required.
- **Use diagrams** for processes, data, and interfaces, and use tables for rules with many conditions.
- **Include what is out of scope.**
- **Keep it readable.** A specification nobody reads is useless, so write for the reader and use structure.

## Specification in Agile Settings

Agile teams usually avoid a large up-front document, but they still record requirements: a product backlog with stories and acceptance criteria, a shared description of the product and its quality requirements, and living documentation that is updated as the system changes. The principle is the same, to hold a shared understanding that can be checked, and the level of formality is matched to the risk, so that regulated or safety-related projects keep more.

<!--
IMAGE PROMPT  ->  generate as images/02_srs_outline.png   (16:9 explanatory diagram, place here)

A document page with an indented outline: 1 Introduction (purpose, scope, glossary), 2 Overall description (product perspective, user classes, constraints), 3 Specific requirements (interfaces, functions, quality), Appendices. Callout arrows show each reader group using specific sections.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Where Does It Go?

In which section of an SRS would each item normally appear?

1. A definition of the term "active customer."
2. A statement that the system must run on a particular government-approved platform.
3. A requirement that the system shall send a confirmation within 5 seconds.
4. A description of how the new system relates to the existing accounting system.

Item 1 belongs in the introduction, under definitions. Item 2 is a design constraint, in the specific requirements or in the constraints under the overall description. Item 3 is a requirement for the functional or performance parts of the specific requirements. Item 4 belongs in the overall description, under product perspective.

## Conclusion

A software requirements specification is a document that describes completely and precisely what a software system must do and the constraints on it, serving as an agreement among stakeholders and as the basis for design, testing, and acceptance. Its value comes from clarity, structure, and being kept current.

A written specification can still be wrong, vague, or inconsistent. The next topic covers how requirements are checked and how each can be traced through the project.

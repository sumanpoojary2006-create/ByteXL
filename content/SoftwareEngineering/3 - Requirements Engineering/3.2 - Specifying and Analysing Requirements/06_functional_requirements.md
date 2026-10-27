## Introduction

Functional requirements are the heart of a specification: they say what the system must do. They are also where much of the ambiguity and omission in projects originates, because natural language is flexible, and what is obvious to the writer may be missing from the page. This topic describes what functional requirements cover and the qualities that make a single requirement statement good.

**Definition:** A functional requirement states a behaviour or function that the system must perform, including how it responds to inputs, what it produces as outputs, and which business rules it enforces, written so that it is clear, complete, and verifiable.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_functional_requirements.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A system box with arrows entering labelled Inputs, arrows leaving labelled Outputs, a rule book inside labelled Rules, and a magnifying glass checking the statement text.

ON-IMAGE TEXT: show a short bold title "Functional Requirements" plus only these few labels, large and legible: Inputs, Rules, Outputs. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Functional Requirements Cover

- **Inputs and how the system responds** to them, including invalid or unexpected input
- **Outputs and results**: reports, messages, stored records
- **Processing and calculations**, and the business rules that govern them
- **Data**: what must be stored, retrieved, and kept consistent
- **Interactions with other systems**, such as exchanging data with a payment service
- **User management and access**: who may do what
- **Error handling and recovery behaviour** at the level of what users and other systems experience

## Writing a Good Requirement Statement

Individual requirements should have the following qualities, which are taken from standards such as ISO/IEC/IEEE 29148.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Poor example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Better example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Necessary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traces to a real need; removing it would leave a gap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall use a blue theme (no one asked for it)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall use the organisation colour palette defined in its brand guidelines</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unambiguous</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be understood in only one way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall handle large orders quickly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall accept orders of up to 100 items</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contains all needed information</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall calculate a discount</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall deduct 10 percent from the total of orders above 1,000 currency units</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does not conflict with other requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders can be cancelled at any time / Orders cannot be cancelled once paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders can be cancelled until preparation starts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Singular (atomic)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Says one thing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall send an email and update the record and print a label</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Three separate requirements, one for each</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verifiable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A test can show whether it is met</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall be user-friendly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A first-time user shall complete an order within 2 minutes in a usability test</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feasible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be achieved with available time, budget, technology</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Zero delay in all situations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response within a stated time under stated load</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traceable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Has an identifier and a link to its source and tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No identifier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">FR-12, derived from need N-4, tested by T-31</td>
    </tr>
  </tbody>
</table>

## Words to Treat with Suspicion

Certain words signal vagueness or hide missing detail.

- **Vague quality words:** fast, user-friendly, easy, flexible, robust, modern, adequate
- **Open-ended phrases:** "and so on," "etc.," "including but not limited to"
- **Escape clauses:** "if possible," "as appropriate," "where necessary"
- **Unmeasured comparatives:** better, faster, more efficient (than what?)
- **Pronouns without clear reference:** "it shall update it"
- **Universal claims:** always, never, all (these are rarely true and hard to verify)

## Modal Verbs

Many organisations use fixed meanings for modal verbs so that obligation is clear.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Word</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">shall</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A mandatory requirement</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">should</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A recommended feature that may be omitted for good reason</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">may</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optional</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">will</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A statement of fact or intention, not a requirement on the system</td>
    </tr>
  </tbody>
</table>

Using "shall" consistently, and nothing else, for mandatory statements removes a common source of dispute.

## Organising Functional Requirements

Long lists are hard to read. Teams group requirements by feature, by user type, by subsystem, or by use case, and give each a unique identifier. The grouping should help a reader answer: is everything covered, and is anything missing? Cross-checking requirements against use cases, data, and external interfaces is a reliable way to find gaps.

<!--
IMAGE PROMPT  ->  generate as images/02_requirement_quality_checklist.png   (16:9 explanatory diagram, place here)

A single requirement statement card in the centre surrounded by eight small tick-badges: Necessary, Unambiguous, Complete, Consistent, Singular, Verifiable, Feasible, Traceable, with one red cross on a vague word highlighted in the statement.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Requirement

1. "The system shall quickly show recent orders."
2. "The system shall let users log in and reset passwords and view their profile."
3. "The system shall be flexible."

Statement 1 needs measurable terms: "The system shall display a user's ten most recent orders within 2 seconds of opening the orders page." Statement 2 is not singular and should be split into three requirements, one each for logging in, resetting a password, and viewing the profile. Statement 3 is not verifiable; it needs to be replaced by concrete requirements, such as which kinds of change the system must allow without redesign.

## Conclusion

A functional requirement states a behaviour or function that the system must perform, including how it responds to inputs, what it produces as outputs, and which business rules it enforces, written so that it is clear, complete, and verifiable. Quality is a property of each statement and of the set as a whole.

Functional requirements describe what the system does. The next topic covers how well it must do it.

## Introduction

Every software project starts with a gap between a situation people are unhappy with and one they would like to reach. Requirements are the statements that describe how the software should close that gap. They are the foundation for design, testing, planning, and contracts, so errors in them spread to everything built afterwards.

This topic defines what a requirement is, separates a need from a requirement, distinguishes levels of requirements, and outlines the activities of requirements engineering.

**Definition:** A requirement is a statement of a capability that a system must provide or a quality it must have in order to satisfy a stakeholder's need, and requirements engineering is the set of activities used to discover, analyse, document, check, and manage such statements.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_are_requirements.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A bridge being built across a gap between a left bank labelled Current situation and a right bank labelled Desired situation, with planks labelled Requirements.

ON-IMAGE TEXT: show a short bold title "What Are Requirements" plus only these few labels, large and legible: Need, Requirement, Gap. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Needs and Requirements

A **need** is a problem or goal in the world of the stakeholder: "students waste time queuing to order food." A **requirement** is a statement about the system that, if satisfied, helps meet that need: "the system shall let a student order and pay for a meal from a phone before arriving."

The distinction matters. A need is discovered by studying people and their situation. A requirement is a decision about what the system will do about it. The same need can often be met by different requirements, and a requirement that does not trace back to a real need is a candidate for removal.

## Levels of Requirements

Requirements are written at several levels of detail for different readers.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Describes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical reader</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why the project exists and what the organisation wants to achieve</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sponsors and managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduce queuing time at meal counters by half within a year</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User (stakeholder) requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What users need to be able to do, in their language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users, analysts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A student can order a meal before arriving</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">System requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed behaviour and constraints of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designers, developers, testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall confirm an order within 3 seconds of payment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restrictions on the solution from outside</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system must comply with data-protection law</td>
    </tr>
  </tbody>
</table>

Going from business down to system requirements is a refinement: each lower level should be traceable to the one above.

## Kinds of Requirements

- **Functional requirements** describe behaviour: what the system does.
- **Non-functional requirements** describe qualities such as performance, security, and usability.
- **Constraints** limit how the system may be built or run, for example required technology, budget, or regulation.
- **Domain requirements** come from the field of use, such as accounting rules or medical safety standards.

Later topics treat these in detail.

## The Requirements Engineering Process

Requirements engineering is a set of related activities that overlap and repeat.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elicitation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What do stakeholders need? How do we find out?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are the requirements clear, consistent, feasible? Do any conflict?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do we record them so everyone understands the same thing?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Validation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do the written requirements really describe what stakeholders want?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do we handle change and keep track of requirements throughout the project?</td>
    </tr>
  </tbody>
</table>

## Why Requirements Are Hard

- **Stakeholders do not fully know what they want** until they see something.
- **Knowledge is tacit.** People forget to mention things they take for granted.
- **Language is ambiguous.** Two readers can honestly understand the same sentence differently.
- **Stakeholders disagree.** Different groups have different goals.
- **Context changes.** Needs shift during the project as business, technology, and regulation change.

Studies of project failure often put unclear or changing requirements near the top of the list of causes, and the cost of fixing a requirements error rises sharply the later it is found.

<!--
IMAGE PROMPT  ->  generate as images/02_requirements_levels_and_activities.png   (16:9 explanatory diagram, place here)

A stepped pyramid with three levels from top to bottom: Business requirements, User requirements, System requirements, each narrowing into more detail. To the right, a circular loop of five activities: Elicitation, Analysis, Specification, Validation, Management.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Need or Requirement? Which Level?

1. "Customers abandon the checkout page because it takes too long."
2. "The system shall let a customer save a payment method for later purchases."
3. "The company wants to increase repeat purchases by 15 percent this year."

Statement 1 is a need, a problem in the stakeholder's world. Statement 2 is a requirement, specifically a system-level or user-level statement of capability. Statement 3 is a business requirement, a goal that explains why the project exists.

## Conclusion

A requirement is a statement of a capability that a system must provide or a quality it must have in order to satisfy a stakeholder's need, and requirements engineering is the set of activities used to discover, analyse, document, check, and manage such statements. Good requirements always trace back to a real need.

Before needs can be discovered, we must know whose needs count. The next topic examines how to identify and analyse stakeholders.

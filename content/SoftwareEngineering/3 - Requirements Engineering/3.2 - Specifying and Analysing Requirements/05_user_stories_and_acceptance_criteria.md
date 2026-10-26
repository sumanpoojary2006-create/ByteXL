## Introduction

Use cases describe interaction in detail, which suits large, carefully specified systems. Many teams instead need a lighter way to record needs that invites conversation and can be reshaped as understanding grows. The user story fills that role. This topic looks at stories as a requirements technique, concentrating on how to write them well and how to attach criteria that make them testable. The Unit 2 topic on the product backlog covers how stories are ordered and managed.

**Definition:** A user story is a short statement of a need written from the viewpoint of a user, in the form of a role, a goal, and a benefit, and acceptance criteria are the specific, testable conditions that must be met for the story to be considered complete.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_user_stories_and_acceptance_criteria.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A story card on the left with three lines labelled Role, Goal, Benefit, and a checklist on the right labelled Acceptance criteria, joined by a bracket showing they belong together.

ON-IMAGE TEXT: show a short bold title "User Stories and Acceptance Criteria" plus only these few labels, large and legible: Role, Goal, Check. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Structure of a Story

A widely used template is:

**As a** (role), **I want** (goal or capability), **so that** (benefit).

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Role</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who needs it, so the team can think about a real person</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">a student</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What they want to be able to do, without prescribing how</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">to see which dishes are vegetarian</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why it matters, so alternatives can be judged against the real aim</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">so that I can choose a meal quickly</td>
    </tr>
  </tbody>
</table>

The benefit is the part most often omitted and the most valuable, because it lets the team challenge a costly solution and find a cheaper one that achieves the same purpose.

## Good Stories and Bad Stories

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weak story</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Better</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall have a database</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No user, no benefit, prescribes a solution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a manager, I want orders to be stored, so that I can see the sales of the day later</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a user, I want a better interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vague, not testable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a first-time user, I want to order in three taps, so that I do not hold up the queue</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As an admin, I want to manage everything</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Far too large</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split into: add a dish, change a price, remove a dish</td>
    </tr>
  </tbody>
</table>

Stories should follow the **INVEST** qualities introduced in Unit 2: independent, negotiable, valuable, estimable, small, and testable.

## Acceptance Criteria

A story is deliberately short, so the details of "done" are captured as acceptance criteria. They turn a vague wish into a verifiable requirement. They should be:

- **Specific**, naming concrete behaviour and values
- **Testable**, so that someone can say clearly pass or fail
- **Independent of design**, describing outcomes rather than screens or technology
- **Agreed before work starts**, with the people who will build and accept it

## Given, When, Then

A common format borrowed from behaviour-driven development describes each criterion as a small scenario.

- **Given** a starting situation
- **When** an action or event occurs
- **Then** an observable outcome is expected

For the story "As a student, I want to cancel an order, so that I am not charged for a meal I will not collect", the criteria could be:

1. Given an order that has not yet been prepared, when the student cancels, then the order is removed and the full amount is refunded.
2. Given an order that is already being prepared, when the student tries to cancel, then the system refuses and explains that preparation has started.
3. Given a cancellation, when it completes, then the student receives a confirmation.

Each example makes a requirement concrete and gives a tester a ready-made case. Writing examples also exposes questions, such as whether a partial refund is allowed, that would otherwise appear late.

## Where Stories Are Weak

- Stories alone do not capture non-functional requirements, constraints, or the overall system picture. Teams add quality criteria and constraints separately.
- Large systems with strict regulation may need more formal specification.
- A collection of stories can lose coherence without a map showing how they fit together, which is why teams use story maps and overall product descriptions.

<!--
IMAGE PROMPT  ->  generate as images/02_story_card_with_criteria.png   (16:9 explanatory diagram, place here)

A story card reading As a student, I want to cancel an order, so that I am not charged, with three Given-When-Then criteria cards fanned beneath it, each with a small tick icon, and a Definition of Done gate to the right.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Repair the Story

1. "As a user, I want the system to be fast." What is wrong, and how could it be repaired?
2. Write two Given-When-Then criteria for the story "As a customer, I want to apply a coupon, so that I pay less."

Statement 1 is vague and untestable, with no clear benefit. A repair is a story with a measurable criterion, such as: "As a customer, I want the menu to appear quickly, so that I can order while queuing," with the criterion "Given a normal load, when I open the menu, then it appears within 2 seconds." For item 2, one criterion is: given a valid coupon, when the customer applies it, then the discount is shown and the total is reduced. Another is: given an expired coupon, when the customer applies it, then the system rejects it and explains why.

## Conclusion

A user story is a short statement of a need written from the viewpoint of a user, in the form of a role, a goal, and a benefit, and acceptance criteria are the specific, testable conditions that must be met for the story to be considered complete. Stories begin the conversation, and criteria make it precise.

Stories and use cases both describe what the system does. The next topic looks at functional requirements as a category and how to state them well.

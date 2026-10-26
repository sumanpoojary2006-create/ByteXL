## Introduction

Lists of "shall" statements can describe what a system does without showing how people use it. A use case adds this missing view: it describes a goal that a user wants to achieve and the sequence of interactions between the user and the system to reach it, including what happens when things go wrong. Telling a story about use is often the fastest way to find forgotten requirements.

**Definition:** A use case is a description of how an actor interacts with a system to achieve a specific goal, consisting of a main sequence of steps, alternative and exception paths, and the conditions that hold before and after, while a scenario is one concrete path through such a use case.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_use_cases_and_scenarios.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A stick-figure actor on the left, a system boundary box on the right containing a flow of numbered steps, with a green main path and two orange branching alternative paths.

ON-IMAGE TEXT: show a short bold title "Use Cases and Scenarios" plus only these few labels, large and legible: Actor, Goal, Flow. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Key Terms

- **Actor:** a person or external system that interacts with the system. A **primary actor** has the goal, and a **secondary actor** provides support, such as a payment service.
- **Goal:** what the actor wants to accomplish, expressed as a verb phrase, for example "Place an order."
- **System boundary:** the line between what is part of the system and what is outside it.
- **Precondition:** what must be true before the use case can start.
- **Postcondition (guarantee):** what is true when it finishes, on success and sometimes on failure.
- **Main success scenario (basic flow):** the most typical sequence in which everything works.
- **Extensions (alternate and exception flows):** variations and failures at particular steps.

## Structure of a Use Case

A well-formed use case, in the style popularised by Ivar Jacobson and refined by Alistair Cockburn, contains the following parts.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content for the use case "Place an order"</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Name and goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place an order: a customer buys a meal from a menu</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primary actor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secondary actors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preconditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The customer is logged in and the menu for the day is available</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Main success scenario</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Customer selects dishes. 2. System shows total. 3. Customer confirms and pays. 4. Payment service approves. 5. System confirms the order and shows pickup time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extensions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3a. Customer cancels, so no order is created. 4a. Payment is declined, so the system explains and offers another method. 1a. A selected dish is sold out, so the system offers alternatives</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Postconditions (success)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order is recorded, payment is taken, and the kitchen is notified</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Postconditions (failure)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No payment is taken, and no order exists</td>
    </tr>
  </tbody>
</table>

## Why Use Cases Are Useful

- **They focus on goals**, keeping features connected to real user value.
- **They expose exceptions.** Asking "what can go wrong at each step?" finds requirements that lists miss.
- **They are readable by non-technical stakeholders**, since they use ordinary language.
- **They support design and testing.** Each path is a natural test case and a guide to the interactions the system must support.

## Scenarios

A **scenario** is one specific story of use, often written with a named person and concrete detail: "A student orders lunch at 12:50 with a card that is declined and then pays with a different one." Scenarios are valuable early in elicitation because stakeholders can react to them directly, and each use case contains many scenarios, one for each distinct path.

## Use Case Diagrams

A use case diagram gives an overview: actors drawn outside a boundary, use cases as ovals inside, and lines showing who takes part in which. Two relationships are common. **Include** means one use case always uses another, such as "Place an order" including "Pay." **Extend** means a use case optionally adds behaviour at a defined point, such as "Apply a discount." Diagrams show scope at a glance, but the detail is in the written descriptions.

<!--
IMAGE PROMPT  ->  generate as images/02_use_case_diagram_and_flow.png   (16:9 explanatory diagram, place here)

Left half: a use case diagram with actors Customer and Payment service outside a boundary box and ovals Place order, Pay, Apply discount inside connected by include and extend arrows. Right half: a numbered step flow of the main success scenario with two branching extension steps.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Writing Tips

- Name use cases with an active verb and a goal: "Cancel a booking."
- Write steps as simple sentences showing who does what: the actor or the system.
- Keep each use case focused on one goal, at a level a user would recognise.
- Describe what the user wants, not how the interface works, so the design stays open.
- Always ask what can go wrong at every step.

## Your Turn: Find the Extensions

For the use case "Withdraw cash from a cash machine", the main success scenario is: insert card, enter code, choose amount, take cash and card.

1. Name two extension paths for step "enter code."
2. Name one precondition.
3. Name one postcondition for a failed withdrawal.

Extensions for entering the code include: the code is wrong, so the system asks again, and after repeated wrong attempts the card is retained. The user may also cancel. A precondition is that the machine has cash and is working, and the card is valid. A failure postcondition is that no money has been dispensed and the account balance is unchanged.

## Conclusion

A use case is a description of how an actor interacts with a system to achieve a specific goal, consisting of a main sequence of steps, alternative and exception paths, and the conditions that hold before and after, while a scenario is one concrete path through such a use case. Their strength is exposing the exceptions that simple lists of requirements overlook.

Agile teams often capture needs in an even lighter form. The next chapter begins with user stories and acceptance criteria and shows how needs are turned into precise, testable requirements.

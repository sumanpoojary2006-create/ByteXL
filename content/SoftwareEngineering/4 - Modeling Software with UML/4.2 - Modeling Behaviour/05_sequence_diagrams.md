## Introduction

A class diagram shows which parts exist, but not how they cooperate to do something. Most useful behaviour involves several objects exchanging messages in a particular order: a customer submits an order, the order checks stock, the payment service is asked to charge a card, and a confirmation returns. A sequence diagram shows exactly this: who talks to whom, in what order, for one scenario.

**Definition:** A sequence diagram is a UML interaction diagram that shows how a set of participants exchange messages over time to carry out a scenario, with time running from top to bottom and participants arranged across the top.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_sequence_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four vertical dashed lifelines with participant boxes at the top labelled Customer, Order Service, Payment Service, Kitchen, and horizontal arrows between them numbered in order from top to bottom.

ON-IMAGE TEXT: show a short bold title "Sequence Diagrams" plus only these few labels, large and legible: Who, Message, Order. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Elements

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it is drawn</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Participant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A box at the top, labelled with a name and optionally a class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An object, component, or actor in the interaction</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lifeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dashed vertical line below the participant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The existence of the participant over time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Activation bar</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A thin rectangle on the lifeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The period during which the participant is busy handling a message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Synchronous message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line with a filled arrowhead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The sender waits for the receiver to finish</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Asynchronous message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line with an open arrowhead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The sender continues without waiting</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashed line with an open arrowhead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The reply to an earlier message</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Self message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An arrow looping back to the same lifeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A participant calls its own operation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creation and destruction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrow to a participant box lower in the diagram; an X at the end of a lifeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An object is created or ceases to exist during the scenario</td>
    </tr>
  </tbody>
</table>

Time flows downward. The vertical distance between messages has no scale: only the order matters.

## Reading an Example

Consider a scenario "Place an order". The messages, in order, are:

1. The Customer asks the Order Service to place an order for chosen dishes.
2. The Order Service asks the Menu to check that the dishes are available.
3. The Menu returns availability.
4. The Order Service asks the Payment Service to charge the customer.
5. The Payment Service returns an approval.
6. The Order Service tells the Kitchen, asynchronously, to prepare the order.
7. The Order Service returns a confirmation to the Customer.

Reading from top to bottom tells the story of the scenario. The diagram also reveals design facts: the Order Service coordinates everything, and the Kitchen is notified without being waited on.

## Combined Fragments: Choices, Loops, Options

Real behaviour includes decisions and repetition. UML draws a box around part of the diagram, with a label in the corner, to show this.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Label</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">alt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternatives: exactly one of several parts runs, according to conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">If payment is approved, confirm the order; otherwise, report the failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">opt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optional: runs only if a condition is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">If a discount code was entered, apply it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">loop</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeats while a condition holds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For each dish in the order, check availability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">par</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parts run in parallel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Send notifications to the kitchen and the customer at the same time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ref</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refers to another diagram</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The detailed payment interaction is shown elsewhere</td>
    </tr>
  </tbody>
</table>

## What Sequence Diagrams Are Good For

- **Working out responsibilities.** Deciding who sends each message forces decisions about which participant is responsible for what.
- **Checking a use case.** A sequence diagram can show how a use case scenario is realised by the parts of the system.
- **Finding missing operations.** Every message must be something the receiver can do, and so each one suggests an operation on a class.
- **Explaining complicated interactions**, such as protocols and integrations with external systems.
- **Designing tests.** The sequence defines expected interactions.

## Limits and Good Practice

- A sequence diagram shows **one scenario**, or a small number of variations. Showing every possibility makes it unreadable.
- Keep the number of participants small, usually five or fewer, and the number of messages manageable.
- Show the main success path first, then separate diagrams for important failure paths.
- Use meaningful message names that match operations, not vague words like "process".
- Draw only what supports the point: omit trivial or internal calls.

<!--
IMAGE PROMPT  ->  generate as images/02_sequence_place_order.png   (16:9 explanatory diagram, place here)

A sequence diagram with lifelines Customer, Order Service, Menu, Payment Service, Kitchen. Numbered messages for placing an order, with an alt fragment around payment approved versus declined, and the message to Kitchen drawn as an asynchronous open-headed arrow.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Read the Sequence

1. In a sequence diagram, how do you tell the order of two messages?
2. What does a dashed arrow with an open head represent?
3. How would you show that sending an email is optional, depending on a customer's preference?

Messages higher on the page occur earlier, so order is read from top to bottom. A dashed arrow with an open head is a return message, the reply to an earlier call. The optional email is shown using an opt fragment around the message with the condition that the customer asked for email.

## Conclusion

A sequence diagram is a UML interaction diagram that shows how a set of participants exchange messages over time to carry out a scenario, with time running from top to bottom and participants arranged across the top. It is the standard way to show how objects cooperate.

Sequence diagrams focus on messages between objects. The next topic describes activity diagrams, which show workflows and flows of control from a broader viewpoint.

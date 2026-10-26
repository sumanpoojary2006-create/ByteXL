## Introduction

Some objects behave differently depending on what has already happened to them. An order that has been paid can be prepared, but one that has not been paid cannot. A user account that is locked cannot log in, whatever password is entered. The same event produces different results according to the **state** the object is in. A state machine diagram describes this: the states, the events that cause changes, and the rules for moving between them.

**Definition:** A state machine diagram is a UML behaviour diagram that shows the states an object can be in during its life, the events that cause it to move from one state to another, and the conditions and actions that accompany each transition.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_state_machine_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Rounded boxes labelled Created, Paid, Preparing, Ready, Collected, with arrows between them labelled by events, a Cancelled state reachable from Created and Paid, and filled start and end circles.

ON-IMAGE TEXT: show a short bold title "State Machine Diagrams" plus only these few labels, large and legible: State, Event, Transition. Keep text minimal, no sentences.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rounded rectangle with a name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A condition in which the object waits for events and behaves in a particular way</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Initial pseudostate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A filled circle with an arrow to the first state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where the object starts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Final state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A circle containing a smaller filled circle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The end of the object life</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An arrow from one state to another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change of state</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A label on a transition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What triggers the change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guard</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A condition in square brackets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The transition occurs only if this is true</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Action (effect)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text after a slash on a transition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Something done during the transition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entry and exit actions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text inside a state, prefixed with entry or exit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Done every time the state is entered or left</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A state containing nested states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Groups related states and simplifies the diagram</td>
    </tr>
  </tbody>
</table>

A transition label has the general form **event [guard] / action**. For example: "pay [amount is correct] / send receipt."

## An Example: The Life of an Order

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">From state</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Event [guard]</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">To state</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">(start)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">submit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record the order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">pay [payment approved]</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Send receipt</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">cancel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancelled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release reserved stock</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">start cooking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notify the customer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">cancel [preparation not started]</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancelled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refund the customer</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">finish</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ready</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alert the customer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ready</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">collect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Close the order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">(end)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">(final)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"></td>
    </tr>
  </tbody>
</table>

This table is the same information as the diagram in another form. It makes rules explicit: an order cannot be collected before it is ready, and cancelling after preparation starts is not allowed, because no such transition exists.

## Why State Machines Help

- **They make rules about order and timing explicit.** Many defects come from an object handling an event in a state where it should not.
- **They reveal missing cases.** For each state, ask what happens for every event; unspecified combinations are either impossible or forgotten.
- **They suit objects with a life cycle**: orders, accounts, documents, tickets, devices, connections.
- **They support testing.** Each transition is a test case, and unreachable states or dead ends are found by inspection.
- **They are valuable in embedded and protocol software**, where behaviour is largely a response to events.

## Checking a State Machine

A quick review asks:

1. Is every state reachable from the start?
2. Can the object always leave a state, unless it is final? A state with no exit is a trap.
3. For each state, is every relevant event handled or deliberately ignored?
4. Are guards on different transitions from the same state and event mutually exclusive and complete?
5. Does every transition have a clear trigger?

## State, Not Flow

A state machine describes **one object over its life**, reacting to events, whereas an activity diagram describes **a process**, a flow of work. The two are related but answer different questions: "What can happen to an order, and when?" versus "What steps do we follow to fulfil orders?"

<!--
IMAGE PROMPT  ->  generate as images/02_order_state_machine.png   (16:9 explanatory diagram, place here)

A state machine for an Order: start circle, Created, Paid, Preparing, Ready, Collected, end circle, plus Cancelled reached from Created and from Paid. Transitions labelled with events and a guard, for example cancel [preparation not started] / refund customer.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Problem

Using the order example:

1. Can an order go from Created directly to Collected?
2. What would happen if the Cancelled state had no incoming transitions from Paid?
3. Name an object in a library system that has a life cycle suited to a state machine.

No: there is no transition from Created to Collected, so the rules do not allow it. If Paid had no transition to Cancelled, customers could not cancel after paying, which would be a design decision to confirm with stakeholders, not an accident. A library book is a good example, with states such as Available, On loan, Reserved, and Lost.

## Conclusion

A state machine diagram is a UML behaviour diagram that shows the states an object can be in during its life, the events that cause it to move from one state to another, and the conditions and actions that accompany each transition. It makes the rules about what can happen, and when, explicit and checkable.

With structure and behaviour covered, the final chapter addresses larger-scale structure, data, and the practical question of how much modeling is enough, starting with component and deployment diagrams.

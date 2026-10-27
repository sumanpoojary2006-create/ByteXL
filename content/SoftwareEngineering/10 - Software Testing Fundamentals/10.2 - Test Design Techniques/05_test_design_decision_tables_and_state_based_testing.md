## Introduction

Input ranges are only one source of complexity. Many business rules depend on **combinations** of conditions: a discount applies if the customer is a member and the order is large and it is not a holiday. Other behaviour depends on **history**: whether an order can be cancelled depends on what has already happened to it. Ranges and boundaries do not capture these. Two further techniques do: decision tables, which organise combinations of conditions, and state-based testing, which examines sequences of events.

**Definition:** A decision table is a systematic way of listing every combination of conditions in a business rule together with the resulting actions, from which tests are derived, and state-based testing designs tests from a model of states and transitions to check that an object responds correctly to sequences of events.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_test_design_decision_tables_and_state_based_testing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a grid with condition rows and rule columns of Yes and No entries leading to an action row. Right: a small state diagram of an order with arrows labelled by events and a highlighted path being walked.

ON-IMAGE TEXT: show a short bold title "Decision Tables and State-Based Testing" plus only these few labels, large and legible: Combinations, Sequences. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Decision Tables

### Structure

A decision table has four parts.

- **Conditions:** the inputs or circumstances that matter (each true or false).
- **Actions:** the outcomes that may result.
- **Rules:** each column is one combination of condition values.
- **Entries:** which actions each rule triggers.

### Example: Discount Rules

The business rule: a member receives a discount of five percent. An order over 1,000 receives ten percent. If both apply, the larger applies (ten percent). Otherwise there is no discount.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Condition or action</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule 1</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule 2</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule 3</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule 4</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer is a member</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order over 1,000</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discount applied</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10 percent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5 percent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10 percent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None</td>
    </tr>
  </tbody>
</table>

With two conditions there are four combinations, and the table lists them all. Each column becomes **one test case**: Rule 2, for instance, is a member with an order of 500, expected to get five percent.

### Benefits

- **Completeness:** it forces consideration of every combination, which often exposes rules the specification forgot. If a combination has no defined outcome, the requirement is incomplete.
- **Clarity:** business people can read and check the table.
- **Efficient test derivation:** each rule is a test.
- **Consistency checks:** contradictory or duplicate rules show up.

### Controlling the Size

With n conditions there are 2 to the power n combinations: three conditions give eight, five give thirty-two, ten give over a thousand. To keep tables manageable:

- **Collapse** rules where a condition does not matter (shown as a dash) because the outcome is the same either way.
- **Split** large rules into several tables by topic.
- Use **risk** to select the most important combinations.
- For many independent conditions, use **pairwise testing**.

Decision tables work well with **cause-effect** thinking: what causes lead to which effects.

## State-Based Testing

### Why State Matters

Many objects behave differently depending on their **state**, as Unit 4 explained with state machine diagrams. The same event may be accepted in one state and rejected in another. Bugs often hide in unusual sequences: an order that is paid twice, a cancellation after the food is ready, an action that works the first time and fails the second.

### The Model

The tests are derived from a model of:

- **States:** for example Created, Paid, Preparing, Ready, Collected, Cancelled.
- **Events:** pay, cancel, start preparing, finish, collect.
- **Transitions:** which events move the object from which state to which, with any conditions (guards).
- **Actions:** what happens on a transition.

### A State Table

A table lists, for every state and every event, the result. It is more complete than the diagram, because it forces a decision about **every** combination, including the invalid ones.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Current state</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pay</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cancel</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Start preparing</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Finish</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Collect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancelled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed (already paid)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancelled (with refund)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ready</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ready</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collected</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancelled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not allowed</td>
    </tr>
  </tbody>
</table>

### Coverage Levels

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Coverage criterion</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Requirement</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every state is visited at least once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All transitions (valid)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every allowed transition is exercised at least once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common minimum</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All invalid transitions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every disallowed event in every state is tried, and shown to be rejected correctly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Important for robustness</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequences of transitions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chains of two or more transitions, where defects depend on history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More thorough, with a rapidly growing number of paths</td>
    </tr>
  </tbody>
</table>

### Designing the Tests

1. Build the state model, with the stakeholders, if one does not exist.
2. Choose the **coverage level** appropriate to the risk.
3. Derive **paths** through the model, starting from the initial state, that visit every required transition. A single long path can cover many transitions, but shorter, separate tests are easier to diagnose.
4. For each step define the **expected state** and any output.
5. Add **invalid event** tests: try to pay a collected order, cancel a ready order, and confirm that the system refuses and the state is unchanged.
6. Add **sequence** tests for risky histories.

An example valid path: Created, pay, Paid, start preparing, Preparing, finish, Ready, collect, Collected. An example invalid test: from Preparing, attempt to cancel; the system must refuse, and the order must remain in Preparing.

### Where It Applies

State-based testing suits workflows (orders, applications, tickets), user interfaces with modes and dialogs, protocols, device behaviour, and sessions with login states.

## Choosing Between Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single input with a range or set of values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Equivalence partitioning and boundary value analysis</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several conditions combine to determine an outcome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decision table</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour depends on the history or current mode of an object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State transition testing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many inputs with few interactions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pairwise testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experience suggests specific risks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error guessing and exploratory testing</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_discount_decision_table_and_order_state_table.png   (16:9 explanatory diagram, place here)

Left: a decision table for the discount rule with conditions Member and Over 1000 across four rule columns and a Discount row, each column marked as test case 1 to 4. Right: a state transition table for an order with a valid path highlighted in green and one invalid cell highlighted in red labelled Must be rejected.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Derive the Tests

1. A shipping rule: free shipping if the order is over 500 or the customer has a premium subscription. Build the decision table and state how many tests are needed.
2. Using the order state table, name one invalid transition test.

For the shipping rule, there are two conditions and so four combinations: over 500 and premium (free), over 500 and not premium (free), not over 500 and premium (free), neither (not free). That gives four tests. A valid invalid-transition test is to attempt to collect an order that is still in Created and confirm that it is rejected and that the state does not change.

## Conclusion

A decision table is a systematic way of listing every combination of conditions in a business rule together with the resulting actions, from which tests are derived, and state-based testing designs tests from a model of states and transitions to check that an object responds correctly to sequences of events. They reveal missing rules and unusual histories that simple input testing misses.

Black-box techniques work from the specification. The next topic looks inside the code, with white-box testing and code coverage.

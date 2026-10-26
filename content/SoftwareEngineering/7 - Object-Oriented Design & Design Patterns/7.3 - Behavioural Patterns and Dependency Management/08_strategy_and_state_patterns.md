## Introduction

Behavioural patterns concern how objects distribute responsibility and cooperate. Two of the most useful deal with a similar-looking problem: an object must behave differently in different circumstances. In one case the circumstance is a choice of method, such as how to calculate a fee. In the other it is the object's own condition, such as the stage an order has reached. The Strategy and State patterns both replace conditionals with polymorphism, but their purposes differ, and the difference is a good test of understanding.

**Definition:** The Strategy pattern defines a family of interchangeable algorithms, encapsulates each one, and lets the client choose among them, while the State pattern lets an object change its behaviour when its internal state changes, by delegating to a separate object that represents each state.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_strategy_and_state_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a context box with a swappable plug-in slot receiving one of three algorithm blocks labelled Standard fee, Express fee, Free delivery. Right: a state diagram of an order moving from Created to Paid to Preparing to Ready, with each state box holding its own behaviour.

ON-IMAGE TEXT: show a short bold title "Strategy and State Patterns" plus only these few labels, large and legible: Swap algorithm, Change state. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Strategy

**The problem.** A system must calculate delivery fees in several ways: a flat fee, a fee by distance, free delivery above a threshold, and special rules for festival days. If all variants live inside one operation, it becomes a long chain of conditions, edited every time a rule changes, and hard to test.

**The solution.** Define a **strategy interface** for calculating a fee. Write a separate class for each method of calculation. The object that needs a fee, called the **context**, holds a reference to a strategy and delegates the calculation to it. The strategy can be chosen when the context is created or swapped later.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strategy interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common operation for all algorithms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fee Calculator: calculate fee for an order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete strategies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each implements one algorithm</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flat Fee, Distance Fee, Free Above Threshold</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses a strategy through the interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order, which asks its Fee Calculator for the fee</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selects the strategy to use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checkout logic, or configuration</td>
    </tr>
  </tbody>
</table>

**Benefits**

- Removes long conditionals and isolates each algorithm in its own class.
- Follows the **open-closed principle**: a new rule is a new class.
- Strategies are easy to **test alone** and to **reuse** in other contexts.
- The algorithm can be changed **at run time**.
- It is a direct example of **composition over inheritance**.

**Costs**

- More classes and objects.
- The client must know the strategies in order to choose among them.
- If the algorithms are trivial or never change, the pattern is excessive.
- In languages where functions can be passed as values, a strategy can be a simple function without a class, which is lighter.

## State

**The problem.** An order behaves differently depending on its stage. A paid order can be prepared, but cannot be paid again. An order being prepared can no longer be cancelled. A naive design has an attribute for the status and every operation checks it with a conditional: "if created, do this; else if paid, do that; else if preparing, refuse." The same checks are repeated in every operation, and adding a new status touches all of them.

**The solution.** Represent each state as its own class, implementing a common interface of all the operations the order supports. The order, the **context**, holds a reference to its current state object and delegates every request to it. A state object decides how to respond and, when appropriate, **replaces the context's current state** with the next one. The rules of each state live in one place.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declares all operations whose behaviour depends on state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order State: pay, cancel, start preparing, collect</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implement behaviour for one state and trigger transitions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created, Paid, Preparing, Ready, Collected, Cancelled</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds the current state and delegates to it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order</td>
    </tr>
  </tbody>
</table>

The state diagram from Unit 4 is the natural plan for this design: each box becomes a class and each transition a point where one state hands over to another.

**Benefits**

- State-specific behaviour is **localised**, so each state is simple.
- **Conditionals disappear** from the context.
- Transitions are **explicit**, making illegal ones easier to prevent.
- New states are added with little change to existing ones.

**Costs**

- Many small classes for a simple state machine.
- Knowledge of transitions is spread across states, so the overall flow is harder to see in one place.
- For a handful of states with simple behaviour, a table of transitions or a few conditionals may be clearer.

## Strategy Versus State

The two patterns have almost the same structure: a context delegating to an object behind an interface. The difference is in intent and in who decides.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">State</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose **how** to do a task from a family of interchangeable algorithms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change **what the object does** according to its condition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who changes the object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The client, usually from outside</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The state objects, from inside, as events occur</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do the variants know each other?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, strategies are independent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, states know which states may follow</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lifetime of the choice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often fixed for a context, changeable if needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes throughout the life of the context</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which delivery fee method applies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which stage the order has reached</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_strategy_vs_state.png   (16:9 explanatory diagram, place here)

Left: an Order context holding a Fee Calculator slot with three interchangeable strategies; an arrow from the Client chooses one. Right: an Order context holding a current State object, with arrows from Created to Paid to Preparing, labelled State objects change the state themselves.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Strategy or State?

1. A discount can be calculated by percentage, by fixed amount, or by buy-two-get-one, and the checkout picks one.
2. A library book acts differently when it is available, on loan, reserved, or lost, and moves between these by itself as events occur.
3. A route planner offers fastest, shortest, and scenic routes, selected by the user.

Case 1 is Strategy. Case 2 is State, since the behaviour depends on the object's own condition and transitions occur internally. Case 3 is Strategy, with the user as the client choosing an algorithm.

## Conclusion

The Strategy pattern defines a family of interchangeable algorithms, encapsulates each one, and lets the client choose among them, while the State pattern lets an object change its behaviour when its internal state changes, by delegating to a separate object that represents each state. Both turn conditionals into polymorphism, and they are distinguished by who decides and why.

Another common need is for objects to be told when something they care about changes. The next topic describes the Observer pattern.

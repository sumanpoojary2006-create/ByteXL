## Introduction

Three more behavioural patterns are used so frequently that most developers meet them without noticing. Command turns a request into an object, which makes it possible to queue, log, and undo it. Template Method fixes the skeleton of an algorithm and lets variations fill in the steps. Iterator lets code walk through a collection without knowing how it is stored. Each is simple to describe and shows a different way of separating what is requested from how and when it is carried out.

**Definition:** The Command pattern encapsulates a request as an object, the Template Method pattern defines the skeleton of an algorithm in a base class while deferring some steps to subclasses, and the Iterator pattern provides a way to access the elements of a collection sequentially without exposing its underlying representation.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_command_template_method_and_iterator_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three panels: a request slip being placed into a queue tray with an undo arrow, a recipe card with fixed steps and two blank steps to fill in, and a hand moving a pointer along items in a list.

ON-IMAGE TEXT: show a short bold title "Command, Template Method and Iterator" plus only these few labels, large and legible: Request as object, Skeleton, Walk. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Command

**The problem.** A user interface has buttons, menu items, and keyboard shortcuts that all trigger operations. Tying each control directly to the code that performs the action makes the control depend on the action, prevents reuse, and gives no way to undo, delay, or record the operation.

**The solution.** Represent each request as a **command object** that contains everything needed to carry it out: the receiver of the request, the operation, and its inputs. A command offers a simple interface, typically "execute", and often "undo".

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Command interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declares execute (and undo)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order Action</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete command</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Binds a receiver to an action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add Item Command, Cancel Order Command</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Receiver</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The object that knows how to perform the work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invoker</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Triggers commands without knowing what they do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A button, a menu, a scheduler, a queue worker</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creates commands and hands them to the invoker</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The screen controller</td>
    </tr>
  </tbody>
</table>

**What commands make possible**

- **Undo and redo:** each command stores what is needed to reverse itself, and a history list of executed commands is kept.
- **Queuing and scheduling:** commands can be stored and executed later or in order, by a worker.
- **Logging and recovery:** a record of commands can be replayed after a failure.
- **Macros:** several commands combined into a composite command.
- **Decoupling:** the invoker does not depend on the receiver, so the same command can be triggered from several places.
- **Transactions:** a group of commands can be completed or rolled back together.

**Costs.** One class per kind of action, and care to implement undo correctly, which may need storing prior state.

## Template Method

**The problem.** Several processes follow the same sequence of steps but differ in details. Processing an order might always involve validating, calculating a price, taking payment, and notifying, but the price calculation and notification differ between dine-in and delivery orders. Copying the whole sequence into each class duplicates it, and a change to the sequence must be repeated everywhere.

**The solution.** Put the **skeleton** of the algorithm in a base class, in an operation that calls the steps in a fixed order. Steps that vary are declared as overridable operations, and subclasses supply them. Some steps may be **hooks**: optional points with a default that does nothing, which subclasses may override if they wish.

The pattern embodies the **Hollywood principle**: "do not call us, we will call you." The base class is in control and calls into the subclass at defined points, instead of the subclass calling the base.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Assessment</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common structure is written once; variants are small and focused</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order of steps is enforced and cannot be changed by subclasses</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relies on inheritance, so it inherits the weaknesses of tight coupling discussed earlier in this unit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternative</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Strategy pattern, by composition, lets the steps be supplied as objects, giving more flexibility at the cost of more objects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subclasses must know which steps they are meant to override and what the base expects</td>
    </tr>
  </tbody>
</table>

## Iterator

**The problem.** Code needs to go through all the elements of a collection, such as the items of an order, the nodes of a tree, or the rows of a result. If the code depends on how the collection is stored, whether as a list, a tree, or a set, it breaks when the representation changes, and each kind of collection needs its own looping code.

**The solution.** The collection supplies an **iterator**: an object that remembers a position and offers two basic operations, "is there another element?" and "give me the next one." Clients use the same interface for any collection. Different iterators can offer different orders, such as forward, backward, or filtered, and several can traverse the same collection at once, each with its own position.

**Benefits**

- The collection's **internal structure stays hidden**, which protects encapsulation.
- **Uniform traversal** across different collections.
- **Multiple simultaneous traversals.**
- Support for **lazy** evaluation: elements produced one at a time, even from an endless or very large source.

**Costs and cautions**

- Changing a collection while it is being traversed can produce errors or skipped elements.
- For simple cases, direct access may be simpler.

Most modern languages build iteration into the language through loops that work over any iterable collection, so the pattern is largely invisible, but understanding it explains how those features work and how to design custom collections.

## Patterns at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem solved</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Key idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Command</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requests must be queued, logged, undone, or decoupled from their senders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make the request an object</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Template Method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several processes share a sequence but differ in some steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix the skeleton, vary the steps</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Iterator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code must traverse collections regardless of their structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide a separate object that walks through the elements</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_command_undo_history.png   (16:9 explanatory diagram, place here)

A row of three buttons labelled Add item, Cancel order, Undo each linked to a command object, and a history stack of executed command cards beneath; an Undo arrow pops the top command, which reverses its action on the Order receiver.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Pattern?

1. A text editor must support undo and redo of every user action.
2. Dine-in and delivery orders follow the same four processing steps, but calculate the price and notify differently.
3. A report needs to print every item in a menu without knowing whether items are stored in a list or a tree.

Case 1 uses Command, with a history of executed commands. Case 2 uses Template Method, with the sequence fixed and two steps varying. Case 3 uses Iterator.

## Conclusion

The Command pattern encapsulates a request as an object, the Template Method pattern defines the skeleton of an algorithm in a base class while deferring some steps to subclasses, and the Iterator pattern provides a way to access the elements of a collection sequentially without exposing its underlying representation. Each separates what is wanted from how, when, or in what structure it is done.

Many patterns depend on objects receiving their collaborators from outside. The next topic describes the technique that makes this practical across a whole application: dependency injection.

## Introduction

Nobody can hold a large program entirely in mind. People manage by working with simplified views: using a part without knowing how it works inside, and thinking about a system at the level of detail that matters for the task. Abstraction is the mental tool for this. Information hiding is the design discipline that makes abstraction safe, by deciding deliberately what a part reveals and what it keeps private.

**Definition:** Abstraction is the practice of focusing on the essential characteristics of something while ignoring irrelevant detail, and information hiding is the design principle of concealing the internal decisions of a module, especially those likely to change, behind a stable interface.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_abstraction_and_information_hiding.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A sealed box with a small labelled interface panel on the outside, while its internal gears and wiring are visible only as a faded cut-away, and a user pressing a button on the panel.

ON-IMAGE TEXT: show a short bold title "Abstraction and Information Hiding" plus only these few labels, large and legible: Interface, Hidden, Stable. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Abstraction

Every familiar object is used through an abstraction. A driver uses a steering wheel and pedals without understanding the engine. A person sends an email without knowing how data crosses the network. In software, a function name, a class, or a service is an abstraction: it offers **what** something does and conceals **how**.

Abstraction works at several levels, and each one builds on the one below. A "place order" operation is composed of smaller operations such as checking stock and taking payment, each of which hides further detail. Because the reader of the upper level need not know the lower levels, the system can be understood in layers.

### Kinds of Abstraction

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it hides</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Procedural</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The steps of a computation behind an operation name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calculate delivery fee</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The representation of data behind a defined set of operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order that can add items and report its total, however it stores them</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The implementation behind a promise of behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Payment Method that can charge an amount, whether by card, wallet, or bank transfer</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layer or service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A whole subsystem behind a boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A notification service that sends messages by email or text</td>
    </tr>
  </tbody>
</table>

## Information Hiding

David Parnas proposed in 1972 that the best way to divide a system into modules is not by the steps of processing, but by **the design decisions that are likely to change**. Each module hides one such decision, so that when the decision changes only that module is affected. The module's interface reveals only what other modules need, and everything else is private.

Examples of decisions worth hiding:

- how data is stored, in a file, a database, or memory
- the format of messages exchanged with an external system
- the algorithm used to calculate a price
- which supplier or service provider is used
- the choice of data structure for a collection

A change to any of these should affect one module, not the whole system.

## Abstraction Versus Information Hiding

The two ideas are related but distinct.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Abstraction</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Information hiding</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A way of thinking: focus on what matters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A design rule: make internal decisions inaccessible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduce what a reader must understand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit the effects of change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Question asked</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the essence of this thing?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What might change, and how do I protect the rest from it?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A simple, useful concept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A boundary that others cannot cross</td>
    </tr>
  </tbody>
</table>

Abstraction describes the view offered. Information hiding enforces that the hidden parts really are hidden, so the abstraction cannot be bypassed.

## Leaky Abstractions

An abstraction **leaks** when users must know about its internals to use it correctly. A storage layer that hides the database but requires callers to understand how it orders results, or an operation whose speed depends in surprising ways on hidden detail, has leaked. Leaks cannot be avoided completely, since every abstraction simplifies, but a design should aim to make them rare and documented.

## Benefits and Costs

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Benefits</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Costs</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parts can be understood and changed separately</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra layers add indirection and can hurt performance or clarity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementations can be replaced without affecting users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A badly chosen abstraction can be harder to change than none</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work can be divided among people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-abstraction creates concepts that serve no real purpose</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing is easier, since parts can be replaced by simple stand-ins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden detail can make debugging harder</td>
    </tr>
  </tbody>
</table>

The right amount of abstraction is the amount that protects against **real, likely** change. Abstraction added for imagined future needs is wasted effort, a point the heuristics topic returns to.

<!--
IMAGE PROMPT  ->  generate as images/02_hidden_decisions_behind_interface.png   (16:9 explanatory diagram, place here)

Three modules drawn as boxes, each with a visible slim interface on the surface and a hidden decision inside labelled Storage format, Price algorithm, Payment provider. A green arrow shows that changing a hidden decision leaves other modules unaffected.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: What Should Be Hidden?

1. A reporting module calls a Storage module. Should it need to know whether data is kept in a file or a database?
2. A team exposes the internal list that holds order items so that any module may add items directly. What risk does this create?
3. Which is the abstraction: the name "Send notification" or the code that connects to the email server?

The reporting module should not need to know, because where data is stored is a likely-to-change decision that Storage should hide. Exposing the internal list means any module can change it in ways the Order does not expect, breaking its rules, and a later change of representation would break all of them. "Send notification" is the abstraction, and the connection code is the hidden implementation.

## Conclusion

Abstraction is the practice of focusing on the essential characteristics of something while ignoring irrelevant detail, and information hiding is the design principle of concealing the internal decisions of a module, especially those likely to change, behind a stable interface. Together they let people understand large systems and change them safely.

Hiding is done by dividing a system into modules. The next topic looks at modularity and how a system is decomposed.

## Introduction

Experienced designers repeatedly find the same kinds of structure succeed and the same kinds fail. Over decades they distilled these findings into named principles that can be applied when designing and reviewing. The five collected under the name SOLID are the best known guidance for object-oriented design. They are heuristics, not laws: they describe tendencies that usually lead to software that is easier to change, and they must be applied with judgement.

**Definition:** SOLID is a set of five design principles, single responsibility, open-closed, Liskov substitution, interface segregation, and dependency inversion, which together guide the creation of modules and classes that are easy to understand, extend, and maintain.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_the_solid_principles.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Five tall labelled building blocks standing side by side, each with a letter S, O, L, I, D and a small icon: one tool, an open door, interchangeable parts, a slim plug, and an upside-down arrow.

ON-IMAGE TEXT: show a short bold title "The SOLID Principles" plus only these few labels, large and legible: S, O, L, I, D. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

The principles were collected and popularised by Robert C. Martin in the early 2000s, building on earlier ideas of others: the open-closed idea comes from Bertrand Meyer in the late 1980s, and the substitution principle from Barbara Liskov. The acronym SOLID was proposed by Michael Feathers. They describe how classes and modules should relate, but the thinking applies to modules and services of any size.

## S: Single Responsibility Principle

**A module should have one, and only one, reason to change.**

A responsibility is a reason for change, usually tied to one group of people who ask for it. A class that both calculates an invoice and decides how it is printed has two reasons to change: finance changes the calculation and marketing changes the layout. A change for one risks the other. Separating them lets each change on its own.

This links closely to cohesion: a module with one responsibility has high cohesion. It does not mean a module has only one operation, but that everything in it changes for the same reason.

## O: Open-Closed Principle

**A module should be open for extension but closed for modification.**

New behaviour should be possible by adding code, not by editing code that already works. For example, if a system calculates delivery fees with a long series of conditions for each type of delivery, each new type forces an edit to that tested code. If instead each delivery type is a separate piece behind a common interface, a new type is added without changing existing ones. The mechanism is usually abstraction: depend on an interface and supply new implementations.

The principle should be applied where change is **likely**. Making everything extensible in advance leads to needless complexity.

## L: Liskov Substitution Principle

**Objects of a subtype must be usable wherever objects of the parent type are expected, without surprising the user.**

If code works with a Payment Method, it must work with every kind of Payment Method. A subtype that breaks the expectations of its parent violates the principle. The classic example is a Square defined as a kind of Rectangle: code that expects to set width and height independently will be surprised when changing one changes the other.

Substitutability requires that a subtype does not demand more than its parent (stronger preconditions) and does not deliver less (weaker postconditions). It is a test for whether inheritance is truly an is-a relationship in behaviour, not merely in name.

## I: Interface Segregation Principle

**Clients should not be forced to depend on operations they do not use.**

A large interface serving many different users means each user is exposed to, and affected by, operations irrelevant to it. A Machine interface with operations for printing, scanning, and faxing forces a simple printer to implement scanning and faxing. It is better to provide several small interfaces, each focused on one role, so that a class implements only the ones it needs.

This reduces coupling and keeps changes from reaching users who never needed the changed operations.

## D: Dependency Inversion Principle

**High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.**

Normally, a high-level policy such as "place an order" would call a low-level detail such as a particular payment provider directly, so the policy depends on the detail. Dependency inversion reverses this: the policy defines the abstraction it needs, a Payment Method interface, and the provider-specific code implements that interface. Now the provider can be changed without touching the policy, and the policy can be tested with a simple stand-in.

The related technique of **dependency injection** supplies a module with its collaborators from outside, instead of having it create them, which makes this practical.

## The Principles at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question to ask</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Violation signal</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single responsibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many reasons does this module have to change?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class changed by several unrelated requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split by responsibility</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open-closed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can I add behaviour without editing tested code?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long chains of conditions for types, edited for every new case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract the varying part behind an interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Liskov substitution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can every subtype stand in for its parent?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Callers check the exact type, or subtypes refuse operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revise the hierarchy; prefer composition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface segregation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does each client use everything in the interface?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Empty or error-throwing implementations of unused operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split into role-specific interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency inversion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does policy depend on detail?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-level code directly names a specific low-level component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depend on an interface owned by the high-level code</td>
    </tr>
  </tbody>
</table>

## Using SOLID Wisely

The principles reduce the cost of change when change really happens, but they also add interfaces, classes, and indirection. A small, stable program does not need them all. Treat them as questions to ask during design and review: Is this class doing too much? Will adding the next case force edits here? Does this subtype behave as its parent promises? Apply them in proportion to the volatility and size of the system, and in tension with simplicity, as the next topic discusses.

<!--
IMAGE PROMPT  ->  generate as images/02_solid_five_cards.png   (16:9 explanatory diagram, place here)

Five cards in a row, one per letter. S: a class with one toolbox. O: a plug-in slot with a new plug being added without opening the core. L: a parent interface with three interchangeable children. I: a big remote control split into small role-specific remotes. D: policy box pointing to an interface, with a provider box pointing to the same interface.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Principle Is Broken?

1. A class both calculates sales tax and formats receipts for printing.
2. Adding a new discount type requires editing a long set of conditions inside a tested function.
3. A class must implement an operation called "fax" although it is a simple printer.
4. The order logic directly creates and uses one specific payment provider.

Case 1 breaks single responsibility. Case 2 breaks open-closed. Case 3 breaks interface segregation. Case 4 breaks dependency inversion.

## Conclusion

SOLID is a set of five design principles, single responsibility, open-closed, Liskov substitution, interface segregation, and dependency inversion, which together guide the creation of modules and classes that are easy to understand, extend, and maintain. They are tools for judgement, and are most valuable where change is likely.

SOLID is one set of guidelines. The next topic covers shorter, more general rules of thumb that every designer meets.

## Introduction

A module is useful because others can rely on it without knowing what is inside. What they rely on is its interface: the operations it offers, what they accept and return, and the promises they make. Encapsulation is the practice of keeping the contents of a module behind that interface, so that the interface becomes the only way in. Together they determine how stable, safe, and pleasant a module is to use.

**Definition:** Encapsulation is the bundling of data with the operations that act on it while restricting direct access to the internals, and interface design is the practice of defining the minimal, clear, and stable set of operations through which other parts of a system use a module.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_encapsulation_and_interface_design.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A capsule-shaped module with a closed protective shell, three small labelled access ports on its surface, and its internal data shown only as a faint outline inside.

ON-IMAGE TEXT: show a short bold title "Encapsulation and Interface Design" plus only these few labels, large and legible: Shell, Ports, Contract. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Encapsulation

An encapsulated module keeps its data private and exposes behaviour. Instead of letting outsiders change an order total directly, an Order offers operations such as adding an item, and the Order itself keeps the total correct. This protects the module's **invariants**, the conditions that must always hold, such as a total that equals the sum of its items, because only the module's own code can change its state.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Without encapsulation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">With encapsulation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any code can change internal data in any way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes pass through operations that enforce the rules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules are repeated, or forgotten, at each place of use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules are implemented once, inside the module</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change to the internal representation breaks all users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The representation can change freely behind the interface</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bugs can originate anywhere</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bugs in the module state can only come from the module</td>
    </tr>
  </tbody>
</table>

Encapsulation is the practical mechanism of information hiding, which was introduced earlier in this unit.

## What an Interface Is

An interface is the contract between a module and its users. It specifies:

- the **operations** offered, with their names
- the **inputs** each accepts and the **outputs** each returns
- the **errors** that can occur and how they are signalled
- the **behaviour** promised, including conditions that must hold before and after
- any **non-functional** expectations, such as the time an operation may take

Interfaces exist at every scale: between two classes, between components, and between whole services, where they are often called application programming interfaces (APIs).

## Qualities of a Good Interface

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Offers only what users need; every operation earns its place</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide "add item" and "remove item" instead of exposing the internal list</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear and consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names and behaviour are obvious and follow the same conventions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always "get" for reading and "create" for adding, in the same style throughout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to misuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Makes correct use easy and incorrect use difficult or impossible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requires an amount and currency together, instead of two separate calls that could be mismatched</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes rarely, so users are not repeatedly broken</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add new operations without altering existing ones</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expressed at the right level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reflects the purpose, not the implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Charge the customer," not "write row to payments table"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">States the contract, including errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describes what each operation requires and guarantees</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete enough</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lets users do everything they legitimately need</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does not force callers to work around gaps</td>
    </tr>
  </tbody>
</table>

## Guidelines for Interface Design

1. **Design from the user viewpoint.** Imagine writing the calling code. Does it read naturally?
2. **Keep it small.** An interface is easy to add to and hard to remove from. Resist exposing something until it is needed.
3. **Hide implementation detail,** including data structures and the order of internal steps.
4. **Fail clearly.** Report errors in a consistent way that tells the caller what went wrong.
5. **Be consistent** in naming, parameter order, and conventions.
6. **Make invalid states unrepresentable** where practical, for example by using a specific type for an amount instead of a bare number.
7. **Plan for evolution.** Interfaces used by many parties need a way to change without breaking them, such as adding optional features and keeping old versions for a time.
8. **Document the contract,** especially what is not guaranteed.

## Common Mistakes

- Exposing internal data structures and then being unable to change them
- Interfaces with many operations and many flags, which are hard to use correctly
- Operations that must be called in a hidden order
- Leaking implementation details in names, such as those mentioning a particular database
- Inconsistent conventions that force users to look everything up
- Changing an interface without warning

## Interfaces Between Teams and Systems

When interfaces cross team or organisation boundaries, they become contracts that are costly to change. Designing them carefully, publishing clear documentation, versioning them, and treating changes as deliberate decisions are essential. A later unit covers programming interfaces for web services in more depth.

<!--
IMAGE PROMPT  ->  generate as images/02_good_vs_poor_interface.png   (16:9 explanatory diagram, place here)

Two modules side by side. Left, Poor interface: a box with its internals exposed, many sprawling cables and switches, a warning label. Right, Good interface: a closed box with three clearly labelled ports (Add item, Remove item, Get total) and a short contract card beside it.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Interface

1. An Order exposes its list of items for anyone to edit directly. What is the risk, and what is a better interface?
2. An operation takes four true or false parameters that change its behaviour. What is the concern?
3. Why is it easier to add an operation to an interface than to remove one?

Exposing the list lets any code break the Order rules, such as the total matching the items. A better interface offers operations such as add item and remove item that maintain the rules. Several flags make the operation hard to understand and easy to misuse, since callers must remember what each combination means; separate operations are clearer. Adding an operation does not disturb existing users, whereas removing one breaks every caller that uses it.

## Conclusion

Encapsulation is the bundling of data with the operations that act on it while restricting direct access to the internals, and interface design is the practice of defining the minimal, clear, and stable set of operations through which other parts of a system use a module. A narrow, well-documented interface is the most effective protection against the spread of change.

The principles so far describe qualities of a good structure. The next chapter turns to named, widely used principles and heuristics, beginning with the five collectively known as SOLID.

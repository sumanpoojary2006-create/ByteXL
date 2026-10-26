## Introduction

Software is rarely built from nothing. Teams integrate libraries, external services, and older systems whose interfaces they cannot change, and these seldom match what the new code expects. At the same time, many subsystems have grown complicated, with numerous parts that must be called in the right order, and users of the subsystem need only a simple view. The Adapter and Facade patterns address these two situations. They look similar, but their purposes differ.

**Definition:** The Adapter pattern converts the interface of an existing class into the interface that clients expect, so that classes with incompatible interfaces can work together, while the Facade pattern provides a single, simplified interface to a complex subsystem, making it easier to use.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_adapter_and_facade_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a travel power adapter converting a foreign plug shape into the local socket shape, labelled Adapter. Right: a simple front desk panel with three buttons standing in front of a tangle of machinery, labelled Facade.

ON-IMAGE TEXT: show a short bold title "Adapter and Facade Patterns" plus only these few labels, large and legible: Convert, Simplify, Hide. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Adapter

**The problem.** The ordering system expects every payment provider to offer a standard operation, "charge an amount." A new provider's library offers a different operation with different inputs, such as "create transaction" with an amount in the smallest currency unit and a reference. The library cannot be modified, and the ordering code should not be filled with special cases for it.

**The solution.** Write an **adapter**: a small class that implements the interface the ordering code expects, and internally translates each request into calls on the provider library. The ordering code sees only the familiar interface.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Target</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The interface the client expects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment Method, with "charge"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adaptee</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The existing class with an incompatible interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The provider library</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adapter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implements the target by delegating to the adaptee, converting inputs and outputs as needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provider Payment Adapter</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses the target interface, unaware of the adaptee</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order logic</td>
    </tr>
  </tbody>
</table>

**Object and class adapters.** Most adapters work by holding the adaptee and delegating to it (the **object adapter**, which uses composition). In languages with multiple inheritance, an adapter can inherit from both interfaces (the **class adapter**). The object form is more flexible and more common.

**Typical uses**

- Integrating a third-party library or service behind a stable interface of one's own
- Wrapping legacy code so that new code does not depend on its design
- Allowing several providers to be used interchangeably
- Protecting the system from changes in an external interface, by confining them to one adapter

This is an application of **dependency inversion**: the system depends on its own abstraction, and the adapter is the only place that knows the outside details.

## Facade

**The problem.** To place an order, a client must check the menu, reserve stock, calculate prices and tax, take payment, notify the kitchen, and send a receipt, calling several subsystems in the correct order and handling their failures. Every client would have to repeat this knowledge, and any change in the subsystems would break all of them.

**The solution.** Provide a **facade**: a single class with a simple operation, such as "place order," that carries out the sequence of calls on behalf of the client. The subsystems remain available for those who need them, but most clients use only the facade.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplicity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clients deal with one simple interface instead of many complicated parts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduced coupling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clients no longer depend on the details of the subsystem</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A facade can be the entry point to a layer or subsystem</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Freedom to change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The subsystem can be restructured without affecting clients, provided the facade still works</td>
    </tr>
  </tbody>
</table>

**Risks.** A facade can grow into a large class that does too much, a "god object", if every function is added to it. It also may hide capabilities some clients need, in which case they should be allowed to use the subsystem directly. A facade should simplify, not forbid.

## Adapter Versus Facade

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Adapter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Facade</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make an existing interface match an expected one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make a complicated subsystem easier to use</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of classes involved</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usually wraps one class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usually coordinates several classes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The target interface is fixed in advance by the client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new, simpler interface is designed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Translation between two interfaces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplification of many into one</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Question it answers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can I use this thing that does not fit?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can I avoid dealing with all of this?</td>
    </tr>
  </tbody>
</table>

They can be combined: a facade may use adapters for the external services it coordinates.

## Related Patterns

- **Proxy** also stands in front of an object, with the **same** interface, to control access: delaying creation, checking permission, or crossing a network.
- **Bridge** separates an abstraction from its implementation so that both can vary independently, and is planned in advance, whereas an adapter is applied to fit existing parts.
- **Gateway** in enterprise design is an adapter specifically for an external system.

<!--
IMAGE PROMPT  ->  generate as images/02_adapter_vs_facade.png   (16:9 explanatory diagram, place here)

Left: Order logic expecting a Payment Method socket, an Adapter box converting it to the Provider library's different socket. Right: a client calling one Place order button on a Facade box that fans out to Menu, Stock, Payment, Kitchen, Receipt subsystems.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Adapter or Facade?

1. A team must use a legacy accounting library whose operations do not match the interface the new code expects.
2. A mobile app currently makes six separate calls to subsystems to complete a checkout, and every screen repeats the sequence.
3. Three different delivery companies each offer a different programming interface, and the system must treat them alike.

Case 1 is an Adapter. Case 2 is a Facade, giving one "complete checkout" operation. Case 3 uses an Adapter for each company, all implementing the one interface the system expects.

## Conclusion

The Adapter pattern converts the interface of an existing class into the interface that clients expect, so that classes with incompatible interfaces can work together, while the Facade pattern provides a single, simplified interface to a complex subsystem, making it easier to use. Both reduce coupling to things that cannot or should not be changed.

Two more structural patterns let objects be combined to add behaviour and to form trees. The next topic describes Decorator and Composite.

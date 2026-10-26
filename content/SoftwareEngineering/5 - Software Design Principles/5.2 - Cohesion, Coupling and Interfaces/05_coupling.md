## Introduction

Cohesion concerns the inside of a module, and coupling concerns its relationships with others. Every useful system has connections between its parts, since they must cooperate. The question is how strong and how visible those connections are. Tightly coupled modules cannot be understood, tested, or changed alone, because each depends on the details of the other. Loosely coupled modules interact only through small, stable interfaces.

**Definition:** Coupling is the degree of interdependence between modules, the extent to which one module relies on the internal details of another, and low coupling, where modules interact only through narrow, stable interfaces, is a mark of good design.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_coupling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two pairs of boxes: on the left two boxes fused together by many thick tangled cables labelled Tight coupling, on the right two boxes connected by one thin clean plug labelled Loose coupling.

ON-IMAGE TEXT: show a short bold title "Coupling" plus only these few labels, large and legible: Tight, Loose, Interface. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Coupling Matters

When module A depends heavily on module B, a change to B may break A. If many modules depend on one another in this way, a small change causes a chain of failures, and nobody can safely change anything. Coupling therefore determines **how far a change spreads**. It also determines whether a module can be tested in isolation and whether it can be reused.

## Forms of Coupling

Work by Glenford Myers and Meilir Page-Jones classifies coupling from the tightest to the loosest.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How A depends on B</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A uses or changes the internal workings of B</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module directly alters another module private data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Worst</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common (global)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both share the same global data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several modules read and write one shared global record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both depend on an external format, device, or protocol</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two modules that both assume the same file layout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tells B what to do by passing a flag that controls its logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A caller passes a switch that changes how B behaves</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stamp (data structure)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A passes a whole data structure when B needs only part</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passing an entire customer record when only a name is needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A passes only the data B needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passing an amount and a currency code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A and B communicate only through messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A request sent through a defined interface or queue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Best</td>
    </tr>
  </tbody>
</table>

## Sources of Coupling in Practice

- **Direct access to internals:** reaching into another module data instead of asking it.
- **Shared global state:** variables or resources that anyone can change.
- **Knowledge of concrete types:** depending on a specific implementation, not on an interface.
- **Temporal coupling:** operations that must be called in a particular order that is not enforced.
- **Inheritance:** a subclass depends on the details of its parent.
- **Shared data stores:** several modules or services reading and writing the same tables.
- **Chains of calls:** an object that navigates through many others to get something.

## Reducing Coupling

1. **Communicate through interfaces,** so that a module depends on a promise, not on an implementation.
2. **Pass only what is needed,** avoiding whole structures or objects when a simple value will do.
3. **Avoid shared mutable state,** or encapsulate it behind a module that controls access.
4. **Depend on abstractions,** a point made precise by the dependency inversion principle.
5. **Use events or messages** where modules should not know about each other directly.
6. **Follow the Law of Demeter,** sometimes stated as "talk only to your immediate friends": a module should use the operations of the modules it holds directly and not reach through them to others.
7. **Keep dependencies one-directional,** avoiding cycles.

## The Cost of Loose Coupling

Decoupling is not free. Indirection through interfaces, messages, and layers adds code, concepts, and sometimes delay, and makes the flow of control harder to follow. Distributed systems that are loosely coupled through messages must also handle failure and consistency. The design question is how much decoupling is worthwhile for the changes likely to occur. Some coupling is natural: modules inside the same cohesive unit may reasonably know each other well.

## Coupling and Cohesion Together

The two measures work as a pair.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cohesion</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Coupling</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The goal: focused modules with few dependencies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focused modules that depend heavily on one another; may need rethinking of boundaries</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modules that are independent but unfocused, hard to understand</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The worst: unfocused modules, entangled with one another</td>
    </tr>
  </tbody>
</table>

Increasing cohesion usually reduces coupling, because behaviour that belongs together is kept together and does not need to cross boundaries.

<!--
IMAGE PROMPT  ->  generate as images/02_coupling_spectrum.png   (16:9 explanatory diagram, place here)

A horizontal spectrum from Content coupling (modules fused, one reaching into the other) through Common, Control, Stamp, Data to Message coupling (two modules exchanging envelopes). A ripple icon shows a change spreading widely at the tight end and staying contained at the loose end.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Coupling

1. A reporting module reads the internal list of an Order object directly.
2. A module passes a true or false flag to another that switches its behaviour.
3. Two services both read and write the same database tables.
4. A module passes an order total and a currency code to a calculator.

Case 1 is content-style coupling to internals, which is poor. Case 2 is control coupling. Case 3 is shared data store coupling: changing a table breaks both services, and each can alter data the other relies on. Case 4 is data coupling, which is good.

## Conclusion

Coupling is the degree of interdependence between modules, the extent to which one module relies on the internal details of another, and low coupling, where modules interact only through narrow, stable interfaces, is a mark of good design. Together with high cohesion it is the main measure of how well a system is divided.

The place where coupling is controlled is the boundary between modules. The next topic looks at encapsulation and the design of interfaces.

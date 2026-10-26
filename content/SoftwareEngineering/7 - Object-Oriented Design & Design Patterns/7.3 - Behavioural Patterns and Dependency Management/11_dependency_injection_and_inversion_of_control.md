## Introduction

A class that creates the objects it depends on, by naming specific classes and building them itself, is welded to those choices. It cannot be tested without them, and it cannot be given different ones without editing it. The SOLID dependency inversion principle states the ideal: depend on abstractions. Dependency injection is the practical technique that achieves it, and inversion of control is the broader idea behind it. Together they are among the most influential practices in modern application design.

**Definition:** Dependency injection is a technique in which an object receives the other objects it depends on from the outside, instead of creating them itself, and inversion of control is the principle that a framework or external mechanism, not the application code, decides when and how components are created and called.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_dependency_injection_and_inversion_of_control.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a class building its own dependency inside itself, tightly bolted, labelled Creates its own. Right: the same class with an empty socket, and a separate assembler hand supplying a part from outside, labelled Injected.

ON-IMAGE TEXT: show a short bold title "Dependency Injection and Inversion of Control" plus only these few labels, large and legible: Receive, Not create, Assemble. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Problem

Imagine an Order Service that needs to take payment. If the service itself creates a particular payment provider object, three problems follow.

- **It is bound to one provider.** Using another means editing the service.
- **It is hard to test.** Every test would contact the real provider unless the code is changed.
- **It hides dependencies.** Reading the service from the outside does not reveal what it needs to work.

## The Idea

Instead, the Order Service **declares** what it needs, as an abstraction such as a Payment Method interface, and **receives** an object that implements it. Somebody else decides which implementation to provide. The service now depends only on the interface, and the same service can run with a real provider in production, a different provider elsewhere, and a simple fake in tests.

## Ways to Inject

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Form</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How the dependency arrives</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constructor injection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supplied when the object is created, as a required input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object is always fully ready; dependencies are explicit; can be made unchangeable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A large number of inputs, which signals a design problem</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Setter (property) injection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supplied after creation through a setting operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good for optional dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object may be used before the dependency is set</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface or method injection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supplied as an input to the operation that needs it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency can vary per call</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clutters operation inputs</td>
    </tr>
  </tbody>
</table>

Constructor injection is generally preferred, because it makes the dependencies of a class visible and ensures none is missing.

## Inversion of Control

The term **inversion of control** describes a reversal in who is in charge. In traditional code, the application calls libraries. In an inverted design, a **framework** calls the application code at the right moments, and the application supplies pieces for it to use. The Template Method pattern's Hollywood principle, "do not call us, we will call you," is a small instance. Dependency injection is a form of inversion of control in which the framework or assembler controls how dependencies are created and wired.

Martin Fowler's 2004 article on inversion of control containers helped to popularise the terminology and the technique.

## Containers and the Composition Root

An application with many classes needs someone to create objects and supply their dependencies. This may be done by hand or by a **dependency injection container**, a framework that is told which implementation to use for each interface and builds the whole object graph automatically, including managing lifetimes.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Lifetime</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Singleton (one per application)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single instance is shared by everything</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration, caches, stateless services</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scoped (one per request or unit of work)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new instance for each request, shared within it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database sessions, per-request data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transient (new every time)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fresh instance whenever one is requested</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Light, stateful helpers</td>
    </tr>
  </tbody>
</table>

Notice that a container gives the "only one instance" property of a Singleton without global access, which is the preferable way to achieve it.

Good practice is to assemble the object graph in one place, close to the entry point of the application, called the **composition root**. The rest of the code receives its dependencies and never calls the container itself.

## Benefits

- **Loose coupling:** classes depend on interfaces.
- **Testability:** real dependencies are replaced by simple fakes or stand-ins.
- **Flexibility:** implementations can be changed through configuration.
- **Explicit dependencies:** a class declares what it needs.
- **Support for the open-closed principle:** behaviour is changed by supplying different parts.
- **Consistent management of lifetimes and shared resources.**

## Pitfalls

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service locator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class asks a global registry for what it needs, hiding dependencies and creating a global dependency on the registry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer injecting dependencies explicitly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A constructor with a long list of inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">This signals a class with too many responsibilities; split it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Container magic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heavy reliance on automatic wiring makes it hard to see how objects are connected, and errors appear at run time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep configuration simple and visible; wire by hand in small applications</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interfaces for everything</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An interface for every class even where there is only one implementation and no need for another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduce an interface where there is a real reason, such as testing or variation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Circular dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two classes each need the other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redesign the responsibilities, or introduce an intermediary</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_dependency_injection_before_after.png   (16:9 explanatory diagram, place here)

Top: Order Service creating a specific Provider inside itself, no way to swap, tests need the real provider (red). Bottom: a Composition Root assembling Order Service with a Payment Method interface and plugging in either Real Provider (production) or Fake Payment (tests), both green.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Dependency Problem

1. A class creates its own connection to a specific database inside its operations. What makes testing hard?
2. A constructor requires twelve different collaborators. What does this suggest?
3. Where should the wiring of all components be done?

In case 1, the class cannot be tested without a real database, because it chooses the connection itself; it should receive an abstraction. Case 2 suggests the class has too many responsibilities and should be divided. The wiring should be done in a single composition root near the start of the application.

## Conclusion

Dependency injection is a technique in which an object receives the other objects it depends on from the outside, instead of creating them itself, and inversion of control is the principle that a framework or external mechanism, not the application code, decides when and how components are created and called. It makes designs flexible and testable, and is the practical form of depending on abstractions.

The patterns of this unit are tools for good design, but misapplied or neglected design has its own recurring failures. The last topic of the unit describes them.

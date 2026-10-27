## Introduction

Most modern business software is built using the object-oriented approach, in which a program is a community of objects that hold data and cooperate by sending each other messages. Object-oriented thinking is a way of organising a design around the things in the problem, giving each a clear responsibility. The design patterns studied in this unit are all expressed in this vocabulary, so a firm grasp of the underlying concepts is the starting point.

This topic revisits the core ideas of object orientation from a design viewpoint, concentrating on how they help or hinder good structure.

**Definition:** Object-oriented design is an approach in which a system is structured as a set of collaborating objects, each combining state and behaviour and communicating through well-defined interfaces, using encapsulation, abstraction, inheritance, and polymorphism to manage complexity and change.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_object_oriented_concepts_revisited.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A group of labelled object boxes, Order, Dish, Customer, Payment, each holding a small data compartment and a behaviour compartment, with message arrows passing between them.

ON-IMAGE TEXT: show a short bold title "Object-Oriented Concepts Revisited" plus only these few labels, large and legible: Objects, Messages, Roles. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Objects and Classes

An **object** combines three things:

- **State:** the data it holds at a moment in time, such as the items and status of an order.
- **Behaviour:** what it can do, expressed as operations, such as adding an item.
- **Identity:** what makes it a particular object, distinct from others with the same data.

A **class** is a template that describes a kind of object: the state its objects carry and the behaviour they offer. A running program creates many objects from each class, and they interact by **sending messages**, asking one another to perform operations.

The object-oriented idea has a long history: the Simula language of the 1960s introduced classes and objects, and Smalltalk, developed by Alan Kay and colleagues, built a whole environment around objects exchanging messages. Languages in wide use today support the idea in varying degrees.

## The Four Core Ideas

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Design benefit</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encapsulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data and the operations on it are bundled together, and the internals are hidden behind an interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protects rules and permits changing the inside freely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order guards its own total and offers "add item"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstraction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focus on essential characteristics, ignoring detail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lets people think at a useful level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Payment Method that can charge an amount, however it does so</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inheritance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class takes on the characteristics of another and may extend or change them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shares common behaviour and expresses specialisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Card Payment and Cash Payment are kinds of Payment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Polymorphism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different objects respond to the same message in their own way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Callers need not know the exact kind of object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Asking any Payment to "charge" works whether it is by card or cash</td>
    </tr>
  </tbody>
</table>

## Polymorphism in More Detail

Polymorphism, literally "many forms", is the idea that makes object-oriented designs flexible. When code sends a message to an object, the operation that runs is chosen according to the **actual kind** of the receiving object, at the time the program runs. This is called **dynamic dispatch** or late binding.

Its effect on design is large. Instead of writing code that checks the type of something and acts differently for each type, a designer lets each type supply its own behaviour. A long chain of "if the delivery is standard, do this; if express, do that; if scheduled, do the other" is replaced by asking a Delivery object for its fee and letting each kind of delivery answer. Adding a new kind of delivery then means adding a new class, not editing the chain.

There are several forms:

- **Subtype polymorphism:** objects of different classes sharing a common interface, as above.
- **Parametric polymorphism (generics):** one piece of code works for many types, such as a list of any item type.
- **Ad hoc polymorphism (overloading):** the same name used for different operations distinguished by their inputs.

## Responsibilities and Collaborations

The most useful way to design with objects is to think of each as having **responsibilities**: things it knows and things it does, and **collaborators**, the other objects it works with to fulfil them. Kent Beck and Ward Cunningham introduced **CRC cards** (class, responsibility, collaborator) in 1989 as a simple tool: a card for each class, listing what it is responsible for and with whom it cooperates. Role-playing a scenario with the cards reveals which objects are overloaded or missing.

Craig Larman collected guidance on assigning responsibilities under the name **GRASP**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">GRASP principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information expert</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assign a responsibility to the object that has the information needed to fulfil it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Order, which holds the items, calculates its own total</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Let the object that contains or closely uses another create it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order creates its Order Lines</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controller</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give a non-interface object the job of handling a system event</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Checkout Controller receives "place order" and coordinates</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low coupling and high cohesion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer assignments that keep dependencies few and responsibilities focused</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As in the design principles unit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Polymorphism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handle variation in behaviour by type with polymorphic operations, not conditionals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each Delivery kind calculates its own fee</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pure fabrication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invent a class that does not represent a domain concept to keep cohesion high</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A repository that stores orders</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Indirection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add an intermediary to decouple two things</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A gateway between the order logic and a payment provider</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protected variations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shield the system from points of likely change with a stable interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hide payment providers behind a Payment Method interface</td>
    </tr>
  </tbody>
</table>

## Tell, Do Not Ask

A guideline that follows from encapsulation is **tell, do not ask**: instead of asking an object for its data and then making decisions on its behalf, tell it what to do and let it decide. Code that repeatedly extracts data from objects to calculate something elsewhere is a sign of misplaced behaviour, often producing the **anaemic domain model**, where objects are bare containers of data and all the logic sits in separate procedures. Such designs lose the main benefit of the object-oriented approach.

## Where Object Orientation Strains

The approach is not a universal fit. Very large inheritance hierarchies become rigid. Data that is processed in bulk, in pipelines or with mathematical operations, is sometimes better served by other styles. Many modern designs blend object-oriented structure with functional ideas, such as immutable data and functions as values. The aim is not purity, but using each idea where it clarifies the design.

<!--
IMAGE PROMPT  ->  generate as images/02_polymorphism_replaces_conditionals.png   (16:9 explanatory diagram, place here)

Left: a caller with a long branching conditional box checking Delivery type (red, labelled Edit for every new type). Right: the caller sending one message calculate fee to a Delivery interface with three implementing boxes Standard, Express, Scheduled (green, labelled Add a class for a new type).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Assign the Responsibility

1. Which object should calculate the total of an order: the Order, or a separate Total Calculator that reads every item from the Order?
2. A system checks the kind of payment in many places with conditionals. Which core idea would remove them?
3. What is wrong with a class that contains only data and no behaviour, while all rules live in other places?

The Order should calculate its own total, since it holds the items: it is the information expert. Polymorphism removes the conditionals: each kind of payment supplies its own behaviour. A class that is only data with logic elsewhere is the anaemic domain model, which weakens encapsulation and scatters rules.

## Conclusion

Object-oriented design is an approach in which a system is structured as a set of collaborating objects, each combining state and behaviour and communicating through well-defined interfaces, using encapsulation, abstraction, inheritance, and polymorphism to manage complexity and change. Thinking in responsibilities and collaborations is the key to using it well.

Of the four core ideas, inheritance is the most easily overused. The next topic examines when to prefer a different tool: composition.

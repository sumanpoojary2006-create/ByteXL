## Introduction

Object-oriented software is built from classes: descriptions of kinds of things, with the data they hold and the operations they can perform. A class diagram is a picture of those classes and the relationships among them. It is the most commonly drawn UML diagram, because it shows the static structure of a system: what exists, and how the parts connect, independent of any particular moment in time.

**Definition:** A class diagram is a UML structure diagram that shows a system's classes, their attributes and operations, and the relationships between them, giving a static view of how the parts of the system are organised.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_class_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three rectangle boxes divided into compartments labelled Customer, Order, Dish, joined by labelled lines with small numbers at the ends.

ON-IMAGE TEXT: show a short bold title "Class Diagrams" plus only these few labels, large and legible: Class, Attribute, Operation. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## A Class

A class is drawn as a rectangle with up to three compartments.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Compartment</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Contents</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example for Order</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Top</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The class name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Middle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attributes: the data each object holds, with types</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">date : Date; status : OrderStatus; total : Money</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bottom</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations: what objects of the class can do, with parameters and return types</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">addItem(dish, quantity); cancel(); calculateTotal() : Money</td>
    </tr>
  </tbody>
</table>

An **object** is one particular instance of a class, such as one specific order. A class diagram describes classes, and an object diagram shows instances at a moment in time.

## Visibility

Each attribute or operation can carry a symbol showing who may use it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symbol</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Visibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">+</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Public</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessible from anywhere</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">-</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Private</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessible only inside the class</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">#</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessible inside the class and its subclasses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">~</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Package</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessible within the same package</td>
    </tr>
  </tbody>
</table>

Good design usually keeps attributes private and exposes behaviour through a small set of public operations. This is the idea of encapsulation, which a later unit on design principles examines.

## Other Notation

- An **underlined** member belongs to the class as a whole, not to individual objects (static).
- An **italic** class name or operation means abstract: it is incomplete and must be specialised.
- A class marked with the label interface specifies a set of operations without implementing them.
- A class marked with the label enumeration lists a fixed set of values, such as the possible order statuses.
- A **note** is a small box with a folded corner attaching a comment to an element.

## Multiplicity

At each end of a relationship, a **multiplicity** says how many objects take part.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exactly one</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0..1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Zero or one (optional)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">*  or  0..*</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Zero or more</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1..*</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One or more</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2..5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A specific range</td>
    </tr>
  </tbody>
</table>

For example, a Customer places zero or more Orders, and each Order is placed by exactly one Customer. Multiplicity captures business rules directly: an Order must contain at least one Order Item, so the multiplicity there is one or more.

## Levels of Detail

A class diagram can be drawn at different levels, and the level should match the purpose.

- **Conceptual (domain) level:** classes represent real-world concepts, with few attributes and no operations. It is used to understand the problem.
- **Specification (design) level:** classes represent software elements with key attributes and operations. It is used to plan the solution.
- **Implementation level:** includes every attribute, type, and visibility, close to the code. It is rarely drawn by hand, and is often produced by tools.

Drawing every attribute of every class in a large system produces diagrams nobody can read. Draw only what supports the point being made.

## Finding Classes

Candidate classes can be found by reading requirements and use cases for important nouns, then checking each: Does it have identity and data? Does the system need to remember or act on it? Is it more than a simple value? Verbs suggest operations. The result is refined by discussion, since a first list always contains duplicates, vague terms, and attributes mistaken for classes.

<!--
IMAGE PROMPT  ->  generate as images/02_class_anatomy_and_multiplicity.png   (16:9 explanatory diagram, place here)

Left: a class box for Order with three compartments (name, attributes with types, operations) and visibility symbols. Right: Customer and Order boxes joined by a line labelled places, with multiplicity 1 near Customer and 0..* near Order.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Read and Fix

1. In a class box, what does a minus sign before an attribute mean?
2. A diagram says an Order is linked to Customer with multiplicity 1 at the Customer end and 0..* at the Order end. State this in words.
3. A student draws a class called "Calculate Total." What is wrong?

A minus sign means the attribute is private. The relationship says that each order belongs to exactly one customer, and a customer may have any number of orders, including none. "Calculate Total" is an action, not a thing: it should be an operation of a class such as Order, not a class of its own.

## Conclusion

A class diagram is a UML structure diagram that shows a system's classes, their attributes and operations, and the relationships between them, giving a static view of how the parts of the system are organised. It is most useful when drawn at the level of detail needed for the question at hand.

The lines between classes carry much of a class diagram's meaning. The next topic explains the main kinds of relationship.

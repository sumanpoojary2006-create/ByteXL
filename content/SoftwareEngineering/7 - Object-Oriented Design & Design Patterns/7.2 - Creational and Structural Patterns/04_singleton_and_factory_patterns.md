## Introduction

Every object must be created somewhere, and the way creation is arranged affects how flexible a design is. If code creates concrete objects directly, it becomes bound to those exact kinds: adding a new kind means editing every place that creates one. Creational patterns manage this. This topic presents two of the best known: the Singleton, which controls how many instances exist, and the family of Factory patterns, which decide which kind of object to create.

**Definition:** The Singleton pattern ensures that a class has only one instance and provides a single point of access to it, while the Factory patterns delegate the decision about which concrete class to instantiate to a dedicated creator, so that client code depends on an interface and not on specific classes.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_singleton_and_factory_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a single glowing object with a lock icon and a signpost labelled One instance. Right: a factory machine receiving an order slip and outputting different product shapes behind a common wrapper labelled Payment Method.

ON-IMAGE TEXT: show a short bold title "Singleton and Factory Patterns" plus only these few labels, large and legible: One, Create, Choose. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Singleton

**Intent:** guarantee that exactly one instance of a class exists and give everyone a way to reach it.

**Typical uses:** a configuration holder, a logger, a connection pool, a cache. Things for which several independent copies would be wasteful or wrong.

**How it works:** the class prevents others from creating instances freely, holds the single instance itself, and offers an operation that returns it.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controlled access to a unique resource; avoids repeated creation of something expensive</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any code can reach the instance from anywhere, so dependencies are not visible in interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Global state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It is effectively a global variable, with all the risks of shared mutable state</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to replace with a simple stand-in, and state can leak from one test to the next</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creating the instance safely when several threads ask at once needs care</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coupling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many classes become tied to one specific class</td>
    </tr>
  </tbody>
</table>

Because of these costs, the Singleton is among the most criticised of the classic patterns and is often called an anti-pattern when overused. A better modern approach is usually to **make one instance and pass it to those who need it**, with a dependency injection mechanism controlling its lifetime, as a later topic explains. This gives the "only one" property without global access. A Singleton is justified only where a single instance is truly required by the problem, not merely convenient.

## Factory Patterns

**The problem:** code that decides which concrete class to create is scattered through the system. For example, wherever a payment is processed, code checks the chosen method and creates a Card Payment, Wallet Payment, or Cash Payment. Adding a new method forces edits everywhere.

### Simple Factory

A single place, often an operation, takes a description such as "card" or "wallet" and returns the right kind of object. It is not one of the Gang of Four patterns but is a common first step. The decision is centralised, and clients receive the object through a common interface. Adding a kind changes the factory, though not the clients.

### Factory Method

**Intent:** define an interface for creating an object, but let subclasses decide which class to create.

A base class contains an operation that needs a product, and calls an abstract creation operation to obtain one. Each subclass overrides the creation operation to supply a different product. For example, a Notification Sender base class defines how a notification is sent and calls "create channel"; an Email Sender supplies an email channel and a Text Message Sender supplies a text message channel. The general algorithm is reused and only the created object varies.

### Abstract Factory

**Intent:** provide an interface for creating **families** of related objects without specifying their concrete classes.

When several objects must be used together and must match, one factory makes the whole consistent set. For example, an interface toolkit might offer a Light Theme Factory and a Dark Theme Factory, each producing buttons, menus, and dialogs in matching styles. Client code asks the factory for a button and a menu and gets compatible ones, whichever factory was chosen. The cost is that adding a new kind of product to the family changes every factory.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Creates</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Varies by</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical signal</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple factory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One kind of object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A parameter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A conditional that chooses classes in several places</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Factory Method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One kind of object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A subclass</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A framework that needs to create objects whose type its users define</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract Factory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A family of related objects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A choice of factory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Objects that must be used together and kept consistent</td>
    </tr>
  </tbody>
</table>

## Benefits of Factories

- **Decoupling:** client code depends on an interface, not on concrete classes.
- **Open for extension:** new kinds are added without editing client code, in line with the open-closed principle.
- **Centralised creation logic:** rules about how objects are built live in one place.
- **Easier testing:** a factory can supply test stand-ins.

## Costs

Factories add classes and a level of indirection. If there is only one concrete type and no realistic prospect of another, a factory is unnecessary and the plain creation of the object is clearer.

<!--
IMAGE PROMPT  ->  generate as images/02_factory_variants.png   (16:9 explanatory diagram, place here)

Three panels. Simple factory: one factory box picking among Card, Wallet, Cash products by a parameter. Factory Method: a base creator with an overridable create step and two subclass creators each making a different product. Abstract Factory: Light and Dark factories each producing a matching Button and Menu.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Pattern?

1. A system must ensure there is only one connection pool shared by all code.
2. Payment code checks the method name in six places to create the right payment object, and a new method is about to be added.
3. A user interface library must produce a matching set of controls for each of several themes.

Case 1 suggests a Singleton, or better, a single instance supplied by dependency injection. Case 2 suggests a simple factory or Factory Method, to centralise the choice. Case 3 suggests an Abstract Factory, since a family of related objects must stay consistent.

## Conclusion

The Singleton pattern ensures that a class has only one instance and provides a single point of access to it, while the Factory patterns delegate the decision about which concrete class to instantiate to a dedicated creator, so that client code depends on an interface and not on specific classes. Factories are a staple of flexible design, while the Singleton should be used with caution.

Some objects are difficult to create for a different reason: they are complex, with many parts and options. The next topic describes the Builder and Prototype patterns.

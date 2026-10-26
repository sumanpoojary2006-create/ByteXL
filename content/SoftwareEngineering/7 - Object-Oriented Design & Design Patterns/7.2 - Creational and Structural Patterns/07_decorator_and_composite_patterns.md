## Introduction

Two common design problems concern combining objects. The first is adding features to an object in many different combinations, such as a dish with extra cheese, a spicy sauce, and a gift wrap, without a class for every possible combination. The second is working with structures that contain parts which may themselves contain parts, such as menus with submenus, or folders with folders, and treating a single item and a whole group in the same way. The Decorator and Composite patterns solve these respectively, and both rely on the same device: objects that wrap or contain others while sharing their interface.

**Definition:** The Decorator pattern attaches additional responsibilities to an object dynamically by wrapping it in another object with the same interface, while the Composite pattern arranges objects into tree structures so that individual objects and groups of objects can be treated uniformly.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_decorator_and_composite_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a plain dish being wrapped in successive transparent layers labelled Extra cheese, Spicy sauce, Gift wrap, each layer adding to the price tag. Right: a tree of menu nodes where branches are submenus and leaves are dishes.

ON-IMAGE TEXT: show a short bold title "Decorator and Composite Patterns" plus only these few labels, large and legible: Wrap, Tree, Same interface. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Decorator

**The problem.** A dish can have optional extras. If each combination is a subclass, with extra cheese, with spice, with both, and so on, the number of classes grows explosively, and a customer cannot add an extra after the object has been made.

**The solution.** Define a common interface for anything that has a description and a price. The plain dish implements it. Each extra is a **decorator**: a class that also implements the interface, holds another object of that interface, and delegates to it while adding its own contribution. A decorator for extra cheese asks the object it wraps for its price and adds the price of the cheese. Because decorators have the same interface as what they wrap, they can be **stacked** in any order and any number.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The common interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priced Item: description and price</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The basic object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plain Dish</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decorator (base)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds a component and implements the same interface by delegating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra Decorator</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete decorators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add specific behaviour before or after delegating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra Cheese, Spicy Sauce, Gift Wrap</td>
    </tr>
  </tbody>
</table>

A dish with extra cheese and spicy sauce is a Spicy Sauce decorator wrapping an Extra Cheese decorator wrapping a Plain Dish. Asking it for the price passes the request down the chain, and each layer adds its amount on the way back.

**Familiar examples** include input and output streams in many languages, where a basic stream can be wrapped by one that buffers, one that compresses, and one that encrypts, in whatever combination is needed. Middleware chains in web applications follow the same idea.

**Benefits**

- Behaviour is added **at run time** and in any combination, without subclass explosion.
- Each decorator has a **single responsibility**, in line with the single responsibility principle.
- It follows the **open-closed principle**: new decorators extend behaviour without changing existing classes.

**Costs**

- Many small objects, which can make the design harder to follow and debug.
- The order of wrapping may matter, and mistakes are easy to make.
- A decorator is not the same object as what it wraps, so tests of identity can fail.
- Not suited when the component interface is large, since every decorator must forward all operations.

## Composite

**The problem.** A menu contains dishes and also submenus, which contain dishes and further submenus. Code that works with the structure, such as calculating the total price of a set menu or displaying everything, would need to ask at every step whether it has a dish or a group and handle each differently.

**The solution.** Define a common interface for both individual items and groups. A **leaf** (a dish) implements it directly. A **composite** (a menu) implements it by holding a collection of children, which may be leaves or other composites, and forwarding requests to each. The client treats everything the same way.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations common to leaves and groups</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Menu Element: show, get price</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaf</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An end object with no children</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dish</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds children and carries out operations by delegating to them and combining the results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Menu, which asks each child for its price and adds them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works with the component interface only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The display or checkout code</td>
    </tr>
  </tbody>
</table>

Asking the top-level menu for its price causes the request to travel down the whole tree, each composite combining the answers of its children. The code that asks does not need to know how deep the tree is.

**Familiar examples** include file systems (folders contain files and other folders), graphical interfaces (a window contains panels that contain buttons), organisation charts, and documents containing sections containing paragraphs.

**Benefits**

- **Uniform treatment** of single items and groups simplifies client code.
- **Recursive structure** is expressed naturally.
- **Easy extension:** new kinds of leaves or groups can be added.

**Costs**

- It can make the design overly general, allowing combinations that make no sense, such as a dish containing a menu. The interface for children management must be designed with care.
- Operations meaningful only for groups, such as "add child", are awkward to put in the shared interface.

## Using Them Together

The two patterns share the idea of a common interface with wrapping or containment, and can be combined: a decorated dish can be a leaf of a composite menu, so a set menu may contain a plain pizza and a pizza with extra cheese. Both patterns turn what would be conditionals and many classes into **objects that combine through one interface**.

<!--
IMAGE PROMPT  ->  generate as images/02_decorator_chain_and_composite_tree.png   (16:9 explanatory diagram, place here)

Left: Plain Dish wrapped by Extra Cheese then Spicy Sauce, with a price request arrow entering the outer layer and amounts adding on the way back, base price plus cheese plus sauce. Right: a Set Menu tree with a Starters submenu and Mains submenu, leaves are dishes, a total price arrow collecting from leaves up to the root.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Decorator or Composite?

1. A text message must optionally be encrypted, compressed, and logged, in any combination.
2. A menu is made of dishes and of submenus, and the total price must be calculated across the whole structure.
3. A plain dish costs 100, extra cheese adds 20, and spicy sauce adds 10. What is the total for a dish with both extras, and what pattern produced it?

Case 1 uses Decorator, stacking each optional behaviour. Case 2 uses Composite, so the same operation works on dishes and menus. In case 3, the total is 100 plus 20 plus 10, which is 130, produced by the Decorator pattern, each layer adding its own price.

## Conclusion

The Decorator pattern attaches additional responsibilities to an object dynamically by wrapping it in another object with the same interface, while the Composite pattern arranges objects into tree structures so that individual objects and groups of objects can be treated uniformly. Both rely on a common interface to let objects be combined freely.

Creational and structural patterns concern how objects are made and arranged. The next chapter turns to patterns about behaviour: how objects interact and how responsibility is divided.

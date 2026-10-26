## Introduction

Factories decide which kind of object to make. Two other creational patterns address different difficulties. Some objects are complicated, with many optional parts, and creating them through a single call with a long list of arguments is error-prone. Others are expensive to create from scratch, or are best made by copying an existing, configured one. The Builder and Prototype patterns solve these problems respectively.

**Definition:** The Builder pattern separates the step-by-step construction of a complex object from its final representation, so the same process can create different results, while the Prototype pattern creates new objects by copying an existing instance instead of building them from scratch.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_builder_and_prototype_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a builder placing labelled blocks, base, toppings, drink, side, one by one onto a meal tray, ending in a finished combo. Right: an original object being photocopied into two identical copies, one slightly altered.

ON-IMAGE TEXT: show a short bold title "Builder and Prototype Patterns" plus only these few labels, large and legible: Step by step, Copy, Customise. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Builder

**The problem.** Consider creating a custom meal order with a base dish, optional extras, a spice level, a delivery time, a note to the kitchen, and a coupon. A single operation that accepts all of these as separate inputs is hard to read ("what does the fourth argument mean?"), forces callers to supply values they do not care about, and needs many variations for different combinations. This difficulty is known as the **telescoping constructor** problem.

**The solution.** Provide a separate **builder** object with a method for each part. The client calls only the ones it needs, in readable steps, and then asks the builder for the finished product. A well-designed builder checks that the combination is valid before producing the object.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meal order example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The complex object being built</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A finished Order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Builder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Offers steps to set each part and a final step to produce the result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order Builder with "add dish", "set spice level", "set delivery time", "apply coupon", and "build"</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Director (optional)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knows a fixed recipe for using the builder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A "standard lunch combo" routine that adds a fixed set of items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses the builder to obtain the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The checkout code</td>
    </tr>
  </tbody>
</table>

**Benefits**

- Readable construction: each step is named.
- Optional parts can be skipped without a profusion of variations.
- Validation can be applied before the object exists, so that invalid or half-built objects are never seen.
- The finished product can be made **immutable**, because all values are set before it is created.
- The same process can produce different products, by using different builders.

**Costs.** An extra class for each product, and some duplication of the product's fields. For simple objects with few parts, a builder is more ceremony than benefit.

## Prototype

**The problem.** Creating an object may be costly, for example when it needs a slow load of data, or complicated set-up. Sometimes a program must create many objects that are nearly the same, with small differences, or must create objects whose exact class is not known in advance.

**The solution.** Keep a configured object as a **prototype**. To make a new one, ask the prototype to produce a copy of itself, then adjust the copy. The object that requests the copy need not know the prototype's concrete class, only that it can be copied.

**Shallow and deep copies.** A critical point in this pattern is how thoroughly the copy is made.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What is copied</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shallow copy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The object itself, but any other objects it refers to are shared between the original and the copy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing a shared part through one affects the other</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deep copy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The object and everything it refers to, recursively</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More expensive; must handle circular references</td>
    </tr>
  </tbody>
</table>

For example, copying an order template with a shallow copy would give two orders that share one list of items, so adding an item to one adds it to the other. Deciding what must be copied and what may be shared is the main design effort.

**Typical uses**

- Starting new documents or orders from a saved template
- Creating many similar objects, such as characters in a game, from a configured model
- Avoiding a large set of factory classes parallel to a hierarchy of products
- Storing a library of preconfigured objects chosen at run time

**Costs.** Copying objects with complex internal links is difficult, and cloning can bypass the normal rules of construction. Some languages provide built-in copying support, which reduces the effort.

## Choosing Among Creational Patterns

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only one instance may exist</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Singleton (with caution)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which class to create depends on a condition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Factory Method or simple factory</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A family of related objects must match</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract Factory</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An object has many parts and options</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Builder</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New objects are best made by copying a configured one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prototype</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_builder_steps_and_deep_copy.png   (16:9 explanatory diagram, place here)

Left: an Order Builder with numbered steps add dish, set spice, set delivery time, apply coupon, then a build arrow producing a finished Order. Right: a shallow copy sharing one item list between two orders (red, labelled Shared) versus a deep copy with two separate lists (green, labelled Independent).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Builder or Prototype?

1. An order has a dozen optional settings, and callers are confused by a long list of inputs.
2. A restaurant wants to create a new weekly menu by taking last week's menu, which is fully configured, and changing a few dishes.
3. After copying a template order, adding an item to the copy also adds it to the original. What went wrong?

Case 1 calls for a Builder. Case 2 calls for a Prototype: copy the existing menu and adjust. Case 3 is a shallow copy problem: the item list is shared and a deep copy of the list is needed.

## Conclusion

The Builder pattern separates the step-by-step construction of a complex object from its final representation, so the same process can create different results, while the Prototype pattern creates new objects by copying an existing instance instead of building them from scratch. Both solve difficulties of creation that a plain constructor handles poorly.

Creational patterns concern making objects. The next topics move to structural patterns, which concern arranging them. The first pair deals with making incompatible parts work together and hiding complexity: Adapter and Facade.

## Introduction

Inheritance looks like a convenient way to reuse code: take an existing class and extend it. Early object-oriented practice leaned on it heavily, and large hierarchies of classes became common. Experience then showed a pattern of trouble: hierarchies that were hard to change, subclasses that broke when their parents were modified, and designs that did not match how the problem varied. One of the most widely quoted pieces of advice in the Design Patterns book is to **favour object composition over class inheritance**.

**Definition:** Composition is a design technique in which an object obtains behaviour by holding and delegating to other objects, rather than inheriting it from a parent class, and the principle of favouring composition over inheritance advises using inheritance only where a true specialisation relationship exists.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_composition_over_inheritance.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a tall rigid class hierarchy tree with many levels and red cracks. Right: a central object with removable component blocks plugged into slots labelled Payment, Delivery, Notification, shown flexible and green.

ON-IMAGE TEXT: show a short bold title "Composition Over Inheritance" plus only these few labels, large and legible: Is-a, Has-a, Swap. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Two Ways to Reuse

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Inheritance</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Composition</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Is a kind of"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Has a" or "uses a"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse style</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">White-box: the subclass sees and depends on the internals of the parent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Black-box: the object uses another only through its interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When it is decided</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed when the class is written</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be chosen or changed while the program runs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coupling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tight: a subclass is bound to its parent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loose: depends on an interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing the hierarchy affects every subclass</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parts can be swapped independently</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Express Delivery extends Delivery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order holds a Delivery Method and asks it for the fee</td>
    </tr>
  </tbody>
</table>

**Delegation** is how composition works: an object that receives a request passes it to another object that does the work. The outer object remains in control and the inner one is replaceable.

## Problems With Inheritance

1. **The fragile base class.** A change to a parent class can break subclasses in ways the author of the parent never imagined, because the subclasses depend on its internal behaviour. The deeper the hierarchy, the greater the risk.
2. **Tight coupling.** A subclass is bound to its parent and cannot easily be reused elsewhere.
3. **Inflexible variation.** A class can inherit from a parent in a fixed way. If objects need to change kind during their life, such as an employee who becomes a manager, inheritance cannot express it without rebuilding the object.
4. **Explosion of classes.** When several independent dimensions of variation are modelled by subclassing, the number of classes multiplies. With three kinds of delivery and three kinds of payment, subclassing for every combination needs nine classes, and each new kind adds more.
5. **Misuse of is-a.** Inheritance is sometimes used merely to borrow code, even when the child is not truly a kind of the parent. Such a design violates the Liskov substitution principle, as the design principles unit explained.
6. **Multiple inheritance complications.** Inheriting from several parents can create ambiguity, known as the diamond problem, when two parents share a common ancestor.

## How Composition Helps

Using the delivery and payment example, composition models each dimension as a separate component. An Order holds one Delivery Method and one Payment Method, chosen independently. Three kinds of each need only six small classes, and combinations are formed at run time. Adding a fourth delivery kind adds one class, not three or more. The pieces can be tested alone and reused elsewhere.

## When Inheritance Is Appropriate

Inheritance remains a valid tool when:

- there is a **genuine is-a relationship** that honours substitutability: wherever the parent is expected, the child behaves correctly
- the hierarchy is **shallow and stable**
- the **parent is designed for extension**, with clear points where subclasses may change behaviour, and is documented for it
- the aim is to **share an interface** (inheriting from an abstract type or an interface, which carries no implementation) rather than implementation

A useful distinction is between **interface inheritance**, which declares what an object can do, and **implementation inheritance**, which borrows how it does it. The first is safe and central to polymorphism. The second is the source of most of the trouble.

## A Test

Before using inheritance, ask:

1. Is the child **truly a special kind** of the parent in every situation, not just a convenient one?
2. Will the child **always** be that kind, for its whole life?
3. Can the child be used **anywhere** the parent is expected without surprises?
4. Is the child reusing the parent **interface**, or merely its code?

If any answer is no, composition is likely the better choice.

## Related Techniques

Some languages offer alternatives that lie between inheritance and composition, such as **mixins** and **traits**, which let behaviour be added to a class from separate reusable units. They address the same need to share behaviour without a rigid chain of parents, and are another reminder that the question is how to share behaviour with the least coupling.

<!--
IMAGE PROMPT  ->  generate as images/02_class_explosion_vs_composition.png   (16:9 explanatory diagram, place here)

Left: a grid of nine subclasses labelled with every combination of Standard, Express, Scheduled delivery and Card, Wallet, Cash payment, marked Class explosion. Right: an Order box holding one Delivery Method slot and one Payment Method slot, with three interchangeable parts available for each, marked Six small classes.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Inherit or Compose?

1. A Stack class is built by inheriting from a List class to reuse its storage. Is this wise?
2. A Card Payment and a Cash Payment both need to be usable wherever a Payment is expected. Which technique fits?
3. A game character must change from a walking to a flying mode during play. Which fits better?

Case 1 is unwise: a stack is not a kind of list and would inherit many operations that break its rules. A stack should hold a list and use it internally. Case 2 fits inheritance of an interface, since both are genuinely kinds of Payment. Case 3 fits composition: the character holds a movement behaviour object that can be swapped at run time.

## Conclusion

Composition is a design technique in which an object obtains behaviour by holding and delegating to other objects, rather than inheriting it from a parent class, and the principle of favouring composition over inheritance advises using inheritance only where a true specialisation relationship exists. Composition keeps coupling low and variation flexible.

Many of the best-known solutions to recurring design problems apply exactly this advice. The next topic introduces them: design patterns.

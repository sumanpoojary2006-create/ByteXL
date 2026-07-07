## Introduction

Dev is adding an inventory management feature. He wonders whether `Inventory` should *be* a `LibraryItem` (inheritance) or *have* a list of `LibraryItem` objects (composition). He reaches for inheritance instinctively, but his tech lead stops him. "Does an inventory *is-a* library item?" she asks. He realizes it is not. An inventory *has* library items. He is reaching for the wrong tool.

This lesson covers the most common design decision in object-oriented programming: whether two concepts should be connected by inheritance or by composition. Getting this choice right produces code that is easy to extend; getting it wrong produces class hierarchies that become rigid and fragile.

![](images/06_composition_vs_inheritance.png)

## The Two Relationships

**Inheritance** models the "is-a" relationship. A `Book` *is a* `LibraryItem`. An `EBook` *is a* `LibraryItem`. These relationships mean `Book` should share and extend the interface of `LibraryItem`, and code that works with `LibraryItem` objects should also work with `Book` objects.

**Composition** models the "has-a" relationship. A `Library` *has* `LibraryItem` objects. An `Inventory` *has* a list of items. A `Checkout` *has* a patron and a book. These relationships mean one object holds a reference to another as an attribute, delegating behavior to it without claiming to be that thing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-06-composition-vs-inheritance-001-adbad2a1c7.html"
 width="100%"
></iframe>

## The Liskov Substitution Principle

A useful rule of thumb: if you inherit, anywhere the parent class is used, the child should be usable as a drop-in replacement. If that is not true, inheritance is the wrong relationship.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-06-composition-vs-inheritance-002-30503ad004.html"
 width="100%"
></iframe>

An `Inventory` cannot replace a `LibraryItem` in `print_checkout_policy`. An inventory is not a library item. If a subclass does not actually substitute for its parent in the way callers expect, it is a sign that inheritance was chosen for the wrong reason.

## When Inheritance Goes Wrong: "Fragile Base Class"

A class hierarchy that is too deep or too broad becomes brittle. When the parent class changes an internal detail, all children that depend on that detail break, sometimes in surprising ways. Composition avoids this: if `Inventory` holds items as a list rather than inheriting from a catalog class, the catalog class can change its internals without affecting `Inventory` at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-06-composition-vs-inheritance-003-a86a45ea47.html"
 width="100%"
></iframe>

The composed version is simpler, easier to test (you can create an `Inventory` with mock items), and unaffected by changes to `LibraryItem`.

## Composition and Delegation

Composition often pairs with delegation: the outer object passes method calls through to an inner object it holds, rather than inheriting those methods.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-06-composition-vs-inheritance-004-2ea01f619c.html"
 width="100%"
></iframe>

`ReservationManager` does not inherit from `NotificationService`. It holds one as an attribute and delegates notification calls to it. This also makes it easy to swap the notifier (email vs SMS) without changing `ReservationManager` at all, as seen in Unit 2.

## Composition vs. Inheritance at a Glance

| Question | Suggests |
|---|---|
| "Is A a subtype of B?" (`isinstance` should return True) | Inheritance |
| "Does A contain or use B?" | Composition |
| "Does the child substitute for the parent everywhere?" | Inheritance if yes; composition if no |
| "Could the inner object change without breaking the outer?" | Composition (independence) |
| "Are you inheriting to reuse code but not the interface?" | Composition (avoid this use of inheritance) |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-06-composition-vs-inheritance-005-6edeab4088.html"
 width="100%"
></iframe>

`Car` uses composition: it *has* an `Engine`. Consider what would happen if you had written `class Car(Engine):` instead: would `isinstance(my_car, Engine)` make semantic sense? What would callers be allowed to do to a `Car` object that they should not be able to do? Use this analysis to articulate in one sentence why composition is the right choice here.

## Conclusion

Inheritance models "is-a" relationships, where the child genuinely substitutes for the parent. Composition models "has-a" relationships, where one object holds and uses another without claiming to be that thing. The test is whether the child class should be a drop-in replacement for the parent anywhere the parent is used; if not, composition is almost always cleaner and more maintainable. The next lesson focuses on the dunder methods that make your objects integrate naturally into Python's syntax, building directly on the data-model introduction from Unit 1.

## Introduction

Three months into the project, Priya has four different notifier classes: `EmailNotifier`, `SMSNotifier`, `PushNotifier`, and a `SlackNotifier` a colleague added last week. The `SlackNotifier` works perfectly in isolation. It crashes in production because the colleague named the method `notify` instead of `send`. The bug was not caught until a patron tried to make a reservation.

Priya wants Python to tell her at class-definition time if a notifier is missing the method the rest of the system expects. She does not want to wait until runtime to discover the omission. Python's `abc` module (Abstract Base Classes) exists precisely for this situation.

![](images/06_abstract_base_classes.png)

## What an Abstract Base Class Is

An **Abstract Base Class** (ABC) is a class that defines an interface without providing implementations for all of it. It declares which methods every concrete subclass *must* define, and Python raises a `TypeError` if you try to instantiate a subclass that forgot one.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-001-38b4c256fe.html"
 width="100%"
></iframe>

`ABC` is a convenience base class from Python's `abc` module. `@abstractmethod` marks a method that every subclass must implement. The docstring in the abstract method acts as a specification: it tells future developers what any implementation must do.

## Concrete Subclasses Must Implement Every Abstract Method

A class that inherits from `Notifier` and fails to implement `send` cannot be instantiated. Python catches this at instantiation time, not at call time, which is a major improvement over duck typing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-002-ff0d5e2813.html"
 width="100%"
></iframe>

The error message names the missing method explicitly. Priya would have caught the `SlackNotifier` bug the moment it was first instantiated in a test, not in production.

## Abstract Classes Can Have Concrete Methods Too

Abstract base classes are not required to be purely abstract. They can include concrete methods that all subclasses inherit, providing default behavior alongside the required interface.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-003-e084ccef79.html"
 width="100%"
></iframe>

`send_batch` is a concrete method defined on the abstract class. It works correctly for every concrete subclass, regardless of how `send` is implemented, because it delegates to `self.send()`. This is the **template method pattern**: the abstract class defines the structure, concrete subclasses fill in the variable part.

## Abstract Properties

You can also mark properties as abstract, requiring subclasses to provide a value or computation for an attribute:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-004-2eeaf53721.html"
 width="100%"
></iframe>

## isinstance() With Abstract Classes

A useful side effect of ABCs: `isinstance()` works correctly across the whole hierarchy, regardless of which concrete class you are holding.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-005-ea7094aaf3.html"
 width="100%"
></iframe>

The ABC becomes a single, authoritative check: anything that claims to be a `Notifier` must have implemented `send`.

## Abstract Base Classes at a Glance

| Concept | What it does |
|---|---|
| `class X(ABC)` | Declares X as an abstract base class |
| `@abstractmethod` | Marks a method that every subclass must implement |
| Concrete subclass | A subclass that implements all abstract methods |
| Instantiation error | Python raises `TypeError` if a required method is missing |
| Concrete methods on ABC | Inherited by all subclasses; can call abstract methods via `self` |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-06-abstract-base-classes-006-4cb8745a05.html"
 width="100%"
></iframe>

Write a `CSVExporter` and a `JSONExporter` that both inherit from `Exporter` and implement `export`. Then try to instantiate `Exporter` directly and observe the `TypeError`. Finally, write an `IncompleteExporter(Exporter): pass` and confirm Python refuses to let you create one.

## Conclusion

Abstract Base Classes define a formal interface that concrete subclasses are required to implement, with Python raising a `TypeError` at instantiation time rather than at call time if a method is missing. They can include concrete methods that delegate to the abstract ones, and `isinstance()` checks work cleanly across the entire hierarchy. The final lesson of this unit brings encapsulation and abstraction together into a practical design exercise, showing how clean interfaces are designed for a real system.

## Introduction

Priya is ready to put everything in this unit together. She has encapsulated state with properties, defined a formal interface with an ABC, and written concrete classes that implement it. But there is a final, practical question her tech lead poses: "How do you know if the interface you designed is actually clean?" He means: what is the difference between an interface that makes code easier to write and one that just adds boilerplate?

This lesson synthesizes the unit into concrete design principles, shows the full shape of a well-designed component, and highlights the most common mistakes that make interfaces harder rather than easier to use.

![](images/07_designing_clean_interfaces.png)

## Principle 1: Expose What Callers Need, Nothing More

A clean interface has no public methods or properties that callers are not supposed to use. Every public name is a commitment: once published, callers will depend on it, and changing or removing it becomes a breaking change.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-07-designing-clean-interfaces-001-c171940714.html"
 width="100%"
></iframe>

The public interface is two methods: `send` and `send_batch`. The validation helper is prefixed with `_` to signal it is internal. Callers never need to call `_validate` directly; the class calls it as needed inside `send`.

## Principle 2: Make It Hard to Use Incorrectly

A well-designed interface should be harder to misuse than to use correctly. This is achieved through type checking in setters, sensible defaults, and validation at the entry point.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-07-designing-clean-interfaces-002-3ff6ff4c2f.html"
 width="100%"
></iframe>

Validation in `__init__` and the setter means an invalid `Book` object simply cannot exist. Callers do not need to remember to validate; the class takes care of it for them.

## Principle 3: Keep Interfaces Narrow and Focused

An interface that declares 12 abstract methods is a burden: every concrete subclass must implement all 12, even if it only needs 3. Good interface design splits a large interface into smaller, more focused ones.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-07-designing-clean-interfaces-003-b62bc8ed33.html"
 width="100%"
></iframe>

A class that needs to send notifications and export data can inherit from both `Notifier` and `Exporter` without being forced to implement payment handling it will never use.

## Putting It Together: A Complete Component

Here is what the full `Book`-and-`Notifier` design looks like when all the lessons of this unit are applied together:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-07-designing-clean-interfaces-004-c1e010d7f1.html"
 width="100%"
></iframe>

## Clean Interfaces at a Glance

| Principle | What it looks like in code |
|---|---|
| Expose only what callers need | Keep helpers and internals prefixed with `_` |
| Make misuse hard | Validate in `__init__` and setters, raise on invalid input |
| Keep interfaces narrow | One ABC per responsibility, not one ABC for everything |
| Separate interface from implementation | ABCs define what; concrete classes define how |
| Document the contract | Abstract method docstrings describe what callers can expect |

## Your Turn

Design a clean `PaymentProcessor` ABC and two concrete implementations: `CreditCardProcessor` and `UPIProcessor`. The interface should have one abstract method: `charge(amount, account_id)` that returns `True` on success and `False` on failure. Add a concrete `charge_with_retry(amount, account_id, attempts=3)` method on the ABC that calls `charge` in a loop up to `attempts` times, returning `True` on first success or `False` if all attempts fail. Test both implementations and confirm the retry logic works without modification to either concrete class.

## Conclusion

A clean interface exposes exactly what callers need and nothing more, validates input at every entry point so invalid objects cannot exist, and splits responsibilities into narrow, focused ABCs rather than one sprawling contract. This unit covered the full arc: from the raw `Book` class with an open attribute that anyone could set to a validated, property-controlled object, and from informal duck typing to a formal ABC that catches missing implementations at instantiation time. Unit 3 builds on this foundation by exploring what happens when one class inherits from another: how constructor chains work, how methods override each other, and how multiple classes can share and extend behavior through inheritance.

## Introduction

Dev's `LibraryItem` base class has a `checkout_policy()` method that returns a standard 21-day loan period. Physical books follow this rule. Ebooks do not need it at all since they are always available. Reference books can only be used in the library and cannot be checked out. Dev needs each item type to answer the question "what is the checkout policy for this item?" differently, but the calling code should not have to know which type it is talking to.

This is **method overriding**: a child class provides its own implementation of a method that already exists in the parent. It is the mechanism that makes the same method call behave differently depending on which class the object actually belongs to.

![](images/03_method_overriding.png)

## Overriding a Method

When a child class defines a method with the same name as one in the parent, the child's version takes precedence. Python always calls the most specific version it can find, starting with the object's own class.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-001-d8a27eeeec.html"
 width="100%"
></iframe>

`Book` does not define `checkout_policy()`, so it inherits the parent's 21-day version. `EBook` and `ReferenceBook` each override it with their own behavior.

## When to Override vs. When to Call super()

There are two distinct situations when a child needs to change a parent method. The first is when the child's behavior *completely replaces* the parent's: the parent's version is not needed at all, so the child simply defines a new body.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-002-f25fea15b3.html"
 width="100%"
></iframe>

The second is when the child *extends* the parent's behavior: the parent's version still does useful work, so the child calls `super()` to run it and then adds more.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-003-af2e3628f3.html"
 width="100%"
></iframe>

The rule of thumb: if the parent's behavior is *wrong* for this child, replace it entirely. If it is *incomplete* for this child, extend it with `super()`.

## Overriding __init__ Without Forgetting super()

The most common mistake with overriding is forgetting `super().__init__()` when overriding `__init__`. Without it, the parent's initialization does not run, and attributes the parent sets are missing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-004-891fc3481d.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-005-fe1fc8d7e2.html"
 width="100%"
></iframe>

## A Complete Override Example With checkout_policy

Here is the full pattern applied consistently across all item types:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-006-e1460d9a6b.html"
 width="100%"
></iframe>

The loop calls `checkout_policy()` on each item without knowing or caring what type each one is. Each type's own version of the method runs. This is the beginning of polymorphism, covered formally in the next lesson.

## Method Overriding at a Glance

| Situation | What to do |
|---|---|
| Parent behavior is completely wrong for child | Override entirely; do not call `super()` |
| Parent behavior is useful but incomplete | Override and call `super()` to extend |
| Child does not need to change it | Do nothing; inherited version runs automatically |
| Overriding `__init__` | Always call `super().__init__()` first |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-03-method-overriding-007-7b560287d1.html"
 width="100%"
></iframe>

Create a `Circle` and a `Rectangle` and call `describe()` on each. Notice that `describe()` is defined only in `Shape`, but it calls `self.area()`, which executes the correct version for each child. Then add a `Square(Rectangle)` that accepts only `side` in its `__init__` and passes `side, side` to `Rectangle.__init__`. Confirm that `describe()` still works on a `Square` without any changes to `Shape` or `Rectangle`.

## Conclusion

Method overriding lets a child class replace or extend a parent method. When the parent's behavior is completely wrong for the child, the child defines a new body with no call to `super()`. When the parent's behavior is useful but incomplete, the child calls `super().method()` and adds to the result. Always call `super().__init__()` when overriding `__init__`, or the parent's attributes will be missing. The next lesson builds on this to introduce polymorphism: what it means that the same method call behaves differently depending on the actual type of the object at runtime.

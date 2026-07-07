## Introduction

Dev needs an `AudioBook` that is simultaneously a `LibraryItem` (with a title and ISBN) and also a `DigitalMedia` object (with a file size and download capability). It is naturally both things at once. Python allows a class to inherit from more than one parent, and this is called **multiple inheritance**.

Multiple inheritance is powerful but introduces a question that simpler inheritance does not have: if both parent classes define the same method, which version does Python use? The answer depends on a rule called the **Method Resolution Order** (MRO), and understanding it prevents a whole category of subtle bugs.

![](images/05_multiple_inheritance_mro.png)

## Multiple Inheritance Syntax

The syntax is straightforward: list both parent classes in the parentheses.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-05-multiple-inheritance-and-the-001-48b02809d5.html"
 width="100%"
></iframe>

Here the two parents have no methods in common, so there is no conflict. The real complexity appears when both parents define the same method name.

## The Diamond Problem and the MRO

The classic conflict in multiple inheritance is called the **diamond problem**. Imagine this hierarchy:

```
     Base
    /    \
  Left   Right
    \    /
     Child
```

Both `Left` and `Right` inherit from `Base` and override a method. When `Child` calls that method, which version runs: `Left`'s or `Right`'s?

Python's answer is the **Method Resolution Order** (MRO): a deterministic, linearized ordering of the class hierarchy calculated using the **C3 linearization algorithm**. In simple terms, Python checks classes in the order: the class itself, then left-to-right through parents, following a rule that ensures no class appears before another class it inherits from.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-05-multiple-inheritance-and-the-002-c3c2fb1445.html"
 width="100%"
></iframe>

Python found `describe` in `Left` and used it. The MRO tells you the exact order Python searches. You can inspect it any time with `ClassName.__mro__` or `ClassName.mro()`.

## super() Follows the MRO

When you use `super()` in multiple inheritance, Python does not call the direct parent. It calls the *next class in the MRO*. This is how `super()` stays correct in complex hierarchies: each class calls `super()`, Python picks the right next class, and every `__init__` in the chain runs exactly once.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-05-multiple-inheritance-and-the-003-5dbd3118cc.html"
 width="100%"
></iframe>

Every `__init__` ran exactly once, in MRO order, because each one calls `super()`. If any level skipped `super().__init__()`, everything after it in the MRO would be silently skipped.

## When to Use Multiple Inheritance

Multiple inheritance is appropriate when an object genuinely has two independent, orthogonal roles: a `SearchableMixin`, a `LoggableMixin`, or a `SerializableMixin` that adds behavior orthogonally to a domain class. Mixins, classes that add specific capabilities without being primary base classes, are the most common and well-justified use of multiple inheritance.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-05-multiple-inheritance-and-the-004-f9c4689be8.html"
 width="100%"
></iframe>

## Multiple Inheritance and MRO at a Glance

| Concept | What it means |
|---|---|
| Multiple inheritance | `class Child(A, B):` inherits from both |
| Diamond problem | Same method in two parents; which version runs? |
| MRO | Python's linearized search order; always deterministic |
| `__mro__` | Inspect the resolution order of any class |
| `super()` in MI | Follows the MRO, not just the direct parent |
| Mixins | Common, safe use of multiple inheritance for orthogonal capabilities |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-05-multiple-inheritance-and-the-005-af27f7ac7c.html"
 width="100%"
></iframe>

Create an `Article`, add two tags, and print `created_at_label()`, `tag_list()`, and `Article.__mro__`. Then explain in your own words why calling `super().__init__()` in `Article` rather than `TaggableMixin.__init__(self)` directly is the correct approach when using mixins.

## Conclusion

Multiple inheritance lets a class inherit from two or more parents. When method names collide, Python resolves the conflict using the Method Resolution Order (MRO), a deterministic linearization visible via `ClassName.__mro__`. Using `super()` at every level of a multiple-inheritance hierarchy ensures all `__init__` methods run exactly once. The cleanest and most common use of multiple inheritance is mixin classes, which add specific capabilities orthogonally to a main domain class. The next lesson asks a harder design question: when is inheritance the wrong tool, and when should you use composition instead?

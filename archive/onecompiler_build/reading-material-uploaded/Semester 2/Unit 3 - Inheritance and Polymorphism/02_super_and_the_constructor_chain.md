## Introduction

Dev noticed the problem from the last lesson immediately: every subclass (`Book`, `EBook`, `Audiobook`) is copying `self.title = title` and `self.isbn = isbn` from the parent class. If he ever needs to add a `language` attribute to every library item, he has to add it in `LibraryItem.__init__` and then add it to three other `__init__` methods as well. The duplication is back.

The solution is `super()`, which lets a child class delegate part of its `__init__` to the parent's `__init__`. This is one of the most important patterns in object-oriented Python, and understanding it correctly removes a large class of common bugs.

![](images/02_super_constructor_chain.png)

## super() Calls the Parent's Method

`super()` returns a proxy object that delegates method calls to the parent class. The most common use is in `__init__`, where the child calls `super().__init__()` to run the parent's initialization logic before adding its own.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-02-super-and-the-constructor-ch-001-cb3a9bbf31.html"
 width="100%"
></iframe>

`super().__init__(title, isbn)` runs `LibraryItem.__init__` with `title` and `isbn`. After that returns, `self.copies = copies` adds the attribute unique to `Book`. Now `self.title` is set in exactly one place.

## All Three Subclasses, Fixed

With `super()`, each subclass delegates the common work upward:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-02-super-and-the-constructor-ch-002-728e64d91a.html"
 width="100%"
></iframe>

Now if Dev adds `self.language = "English"` to `LibraryItem.__init__`, all three subclasses automatically inherit it with no changes required. The parent is the single source of truth for shared initialization.

## super() Is Not Just for __init__

`super()` works for any method, not only `__init__`. A child class can override a method and still call the parent's version to extend rather than completely replace it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-02-super-and-the-constructor-ch-003-e1a1918af5.html"
 width="100%"
></iframe>

The child's `display_info` starts with the parent's output and appends its own extra detail. This pattern, calling `super().method()` and extending the result, is how you build on existing behavior rather than duplicating it.

## The Constructor Chain in Multi-Level Inheritance

Inheritance can be more than one level deep. When `super()` is called, Python follows the Method Resolution Order (MRO) to find the next class in the chain, even when there are three or more levels.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-02-super-and-the-constructor-ch-004-140728f037.html"
 width="100%"
></iframe>

Each level delegates upward with `super()`. The chain runs from the most-specific class to the most-general, ensuring every `__init__` along the way gets called exactly once.

## super() at a Glance

| Pattern | Code | What it does |
|---|---|---|
| Delegate initialization | `super().__init__(args)` | Runs parent's `__init__`, sets shared attributes |
| Extend a method | `result = super().method(); return result + extra` | Builds on parent's behavior |
| Multi-level chain | `super().__init__()` at each level | Each parent's init runs once, in order |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-02-super-and-the-constructor-ch-005-b91749f4e8.html"
 width="100%"
></iframe>

Create a `TrainedPet` and call `describe()` on it. Trace through which `describe()` calls which, and in what order, to produce the final string. Then add a `language` attribute to `Animal.__init__` and confirm `TrainedPet` automatically inherits it without any changes to `Pet` or `TrainedPet`.

## Conclusion

`super()` delegates to the parent class's method without hardcoding the parent's name, making inheritance chains clean and maintainable. In `__init__`, it runs the parent's initialization before the child adds its own attributes. In other methods, it calls the parent's version and lets the child extend the result. The next lesson takes this further: what happens when a child class defines a method that already exists in the parent, replacing rather than extending it.

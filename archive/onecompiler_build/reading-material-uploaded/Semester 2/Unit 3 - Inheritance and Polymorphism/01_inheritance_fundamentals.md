## Introduction

Dev is building the library catalog system and has written three classes: `Book`, `EBook`, and `Audiobook`. All three have a `title`, an `isbn`, and a method called `display_info()`. All three implement `is_available()` with identical logic. He is copying and pasting the same code into each class, and every time he finds a bug in `display_info()`, he has to fix it in three places.

There is a better way. If all three share common structure and behavior, that structure should live in one place and the three classes should share it. The mechanism is **inheritance**, and this lesson covers how it works and why it exists.

![](images/01_inheritance_fundamentals.png)

## What Inheritance Is

Inheritance is a relationship between two classes: a **parent class** (also called a base class or superclass) defines shared attributes and methods, and a **child class** (subclass) inherits all of them, adding or changing only what is specific to the child.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-01-inheritance-fundamentals-001-7157e42374.html"
 width="100%"
></iframe>

`LibraryItem` defines what all library items have in common. It deliberately does not implement `is_available()` because the right behavior differs per item type (a physical book tracks copies; an ebook may always be available).

## Defining a Subclass

The syntax for inheritance is the parent class name in parentheses after the class name:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-01-inheritance-fundamentals-002-f074f550a8.html"
 width="100%"
></iframe>

`Book` inherits `display_info()` from `LibraryItem` without re-defining it. Any change to `display_info()` in the parent automatically applies to `Book`, `EBook`, and `Audiobook` simultaneously. The bug-in-three-places problem is solved.

## What Gets Inherited

A child class inherits everything that is not explicitly private (not name-mangled with `__`): all methods, all class attributes, and the `__init__` method if the child does not define its own. This includes dunder methods like `__repr__` and `__str__`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-01-inheritance-fundamentals-003-3471570f0f.html"
 width="100%"
></iframe>

Both classes share `display_info()` from `LibraryItem`. Neither had to write it.

## The "Is-A" Relationship

Inheritance models the "is-a" relationship: a `Book` *is a* `LibraryItem`. A `Dog` *is an* `Animal`. An `EBook` *is a* `LibraryItem`. When this relationship holds naturally in your problem domain, inheritance is the right tool. When it does not (a library has books, but a library is not a book), then composition (covered in lesson 6) is more appropriate.

You can check this relationship at runtime with `isinstance()`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-01-inheritance-fundamentals-004-7e0ba6cb9b.html"
 width="100%"
></iframe>

`isinstance` checks the full inheritance chain, so a `Book` is both a `Book` and a `LibraryItem` at the same time.

## Inheritance Fundamentals at a Glance

| Concept | What it means |
|---|---|
| Parent class | Defines shared attributes and methods |
| Child class | Inherits everything from parent; adds or changes its own specifics |
| Syntax | `class Child(Parent):` |
| Inherited members | All non-name-mangled methods and attributes |
| `isinstance(obj, Parent)` | True for both the child's direct type and all parent types |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-01-inheritance-fundamentals-005-11222c0e71.html"
 width="100%"
></iframe>

Create a `Car` and a `Truck` and call `describe()` on each to confirm inheritance works. Then notice a problem: both subclasses repeat `self.make = make`, `self.model = model`, and `self.year = year` even though `Vehicle.__init__` already sets them. The next lesson solves this with `super()`.

## Conclusion

Inheritance lets a child class share the attributes and methods of a parent class, so common behavior is written once and maintained in one place. The "is-a" test helps decide whether inheritance is the right relationship. The next lesson covers the key tool for using inheritance without repeating initialization code: `super()`, which lets a child class call the parent's `__init__` and add only the pieces unique to the child.

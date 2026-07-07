## Introduction

Dev is building the library catalog system and has written three classes: `Book`, `EBook`, and `Audiobook`. All three have a `title`, an `isbn`, and a method called `display_info()`. All three implement `is_available()` with identical logic. He is copying and pasting the same code into each class, and every time he finds a bug in `display_info()`, he has to fix it in three places.

There is a better way. If all three share common structure and behavior, that structure should live in one place and the three classes should share it. The mechanism is **inheritance**, and this lesson covers how it works and why it exists.

![](images/01_inheritance_fundamentals.png)

## What Inheritance Is

Inheritance is a relationship between two classes: a **parent class** (also called a base class or superclass) defines shared attributes and methods, and a **child class** (subclass) inherits all of them, adding or changing only what is specific to the child.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2luaGVyaXRhbmNlX2Z1bmRhbWVudGFscyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY2xhc3MgTGlicmFyeUl0ZW06XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cblxuICAgIGRlZiBkaXNwbGF5X2luZm8oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJ7c2VsZi50aXRsZX0gKElTQk46IHtzZWxmLmlzYm59KVwiXG5cbiAgICBkZWYgaXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByYWlzZSBOb3RJbXBsZW1lbnRlZEVycm9yKFwiU3ViY2xhc3NlcyBtdXN0IGltcGxlbWVudCBpc19hdmFpbGFibGUoKVwiKSJ9"
 width="100%"
></iframe>

`LibraryItem` defines what all library items have in common. It deliberately does not implement `is_available()` because the right behavior differs per item type (a physical book tracks copies; an ebook may always be available).

## Defining a Subclass

The syntax for inheritance is the parent class name in parentheses after the class name:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2luaGVyaXRhbmNlX2Z1bmRhbWVudGFscyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgQm9vayhMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuICAgICAgICBzZWxmLmNvcGllcyA9IGNvcGllc1xuXG4gICAgZGVmIGlzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuY29waWVzID4gMFxuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiLCAzKVxucHJpbnQoYi5kaXNwbGF5X2luZm8oKSkgICAgIyBEdW5lIChJU0JOOiA5NzgtMDQ0MTAxMzU5MykgLS0gaW5oZXJpdGVkIGZyb20gTGlicmFyeUl0ZW1cbnByaW50KGIuaXNfYXZhaWxhYmxlKCkpICAgICMgVHJ1ZSAtLSBkZWZpbmVkIG9uIEJvb2sifQ"
 width="100%"
></iframe>

`Book` inherits `display_info()` from `LibraryItem` without re-defining it. Any change to `display_info()` in the parent automatically applies to `Book`, `EBook`, and `Audiobook` simultaneously. The bug-in-three-places problem is solved.

## What Gets Inherited

A child class inherits everything that is not explicitly private (not name-mangled with `__`): all methods, all class attributes, and the `__init__` method if the child does not define its own. This includes dunder methods like `__repr__` and `__str__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2luaGVyaXRhbmNlX2Z1bmRhbWVudGFscyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiY2xhc3MgRUJvb2soTGlicmFyeUl0ZW0pOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgZmlsZV9zaXplX21iKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5maWxlX3NpemVfbWIgPSBmaWxlX3NpemVfbWJcblxuICAgIGRlZiBpc19hdmFpbGFibGUoc2VsZik6XG4gICAgICAgIHJldHVybiBUcnVlICAgICMgZWJvb2tzIGFyZSBhbHdheXMgYXZhaWxhYmxlOyBubyBwaHlzaWNhbCBjb3BpZXNcblxuY2xhc3MgQXVkaW9ib29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGR1cmF0aW9uX2hvdXJzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5kdXJhdGlvbl9ob3VycyA9IGR1cmF0aW9uX2hvdXJzXG5cbiAgICBkZWYgaXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByZXR1cm4gVHJ1ZVxuXG5lYiA9IEVCb29rKFwiRm91bmRhdGlvblwiLCBcIjk3OC0wNTUzMjkzMzU3XCIsIDIuMSlcbmFiID0gQXVkaW9ib29rKFwiU2hvZ3VuXCIsIFwiOTc4LTAzODUyOTE2NzVcIiwgMjIpXG5cbnByaW50KGViLmRpc3BsYXlfaW5mbygpKSAgICMgRm91bmRhdGlvbiAoSVNCTjogOTc4LTA1NTMyOTMzNTcpIC0tIGluaGVyaXRlZFxucHJpbnQoYWIuZGlzcGxheV9pbmZvKCkpICAgIyBTaG9ndW4gKElTQk46IDk3OC0wMzg1MjkxNjc1KSAtLSBpbmhlcml0ZWQifQ"
 width="100%"
></iframe>

Both classes share `display_info()` from `LibraryItem`. Neither had to write it.

## The "Is-A" Relationship

Inheritance models the "is-a" relationship: a `Book` *is a* `LibraryItem`. A `Dog` *is an* `Animal`. An `EBook` *is a* `LibraryItem`. When this relationship holds naturally in your problem domain, inheritance is the right tool. When it does not (a library has books, but a library is not a book), then composition (covered in lesson 6) is more appropriate.

You can check this relationship at runtime with `isinstance()`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2luaGVyaXRhbmNlX2Z1bmRhbWVudGFscyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50KGlzaW5zdGFuY2UoYiwgQm9vaykpICAgICAgICAgICMgVHJ1ZSAtLSBiIGlzIGEgQm9va1xucHJpbnQoaXNpbnN0YW5jZShiLCBMaWJyYXJ5SXRlbSkpICAgIyBUcnVlIC0tIGIgaXMgYWxzbyBhIExpYnJhcnlJdGVtXG5wcmludChpc2luc3RhbmNlKGIsIEVCb29rKSkgICAgICAgICAjIEZhbHNlIC0tIGIgaXMgbm90IGFuIEVCb29rIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2luaGVyaXRhbmNlX2Z1bmRhbWVudGFscyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY2xhc3MgVmVoaWNsZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbWFrZSwgbW9kZWwsIHllYXIpOlxuICAgICAgICBzZWxmLm1ha2UgPSBtYWtlXG4gICAgICAgIHNlbGYubW9kZWwgPSBtb2RlbFxuICAgICAgICBzZWxmLnllYXIgPSB5ZWFyXG5cbiAgICBkZWYgZGVzY3JpYmUoc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJ7c2VsZi55ZWFyfSB7c2VsZi5tYWtlfSB7c2VsZi5tb2RlbH1cIlxuXG5jbGFzcyBDYXIoVmVoaWNsZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG1ha2UsIG1vZGVsLCB5ZWFyLCBkb29ycyk6XG4gICAgICAgIHNlbGYubWFrZSA9IG1ha2VcbiAgICAgICAgc2VsZi5tb2RlbCA9IG1vZGVsXG4gICAgICAgIHNlbGYueWVhciA9IHllYXJcbiAgICAgICAgc2VsZi5kb29ycyA9IGRvb3JzXG5cbmNsYXNzIFRydWNrKFZlaGljbGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBtYWtlLCBtb2RlbCwgeWVhciwgcGF5bG9hZF90b25zKTpcbiAgICAgICAgc2VsZi5tYWtlID0gbWFrZVxuICAgICAgICBzZWxmLm1vZGVsID0gbW9kZWxcbiAgICAgICAgc2VsZi55ZWFyID0geWVhclxuICAgICAgICBzZWxmLnBheWxvYWRfdG9ucyA9IHBheWxvYWRfdG9ucyJ9"
 width="100%"
></iframe>

Create a `Car` and a `Truck` and call `describe()` on each to confirm inheritance works. Then notice a problem: both subclasses repeat `self.make = make`, `self.model = model`, and `self.year = year` even though `Vehicle.__init__` already sets them. The next lesson solves this with `super()`.

## Conclusion

Inheritance lets a child class share the attributes and methods of a parent class, so common behavior is written once and maintained in one place. The "is-a" test helps decide whether inheritance is the right relationship. The next lesson covers the key tool for using inheritance without repeating initialization code: `super()`, which lets a child class call the parent's `__init__` and add only the pieces unique to the child.

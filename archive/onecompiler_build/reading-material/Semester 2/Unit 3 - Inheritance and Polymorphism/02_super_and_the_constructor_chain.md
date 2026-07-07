## Introduction

Dev noticed the problem from the last lesson immediately: every subclass (`Book`, `EBook`, `Audiobook`) is copying `self.title = title` and `self.isbn = isbn` from the parent class. If he ever needs to add a `language` attribute to every library item, he has to add it in `LibraryItem.__init__` and then add it to three other `__init__` methods as well. The duplication is back.

The solution is `super()`, which lets a child class delegate part of its `__init__` to the parent's `__init__`. This is one of the most important patterns in object-oriented Python, and understanding it correctly removes a large class of common bugs.

![](images/02_super_constructor_chain.png)

## super() Calls the Parent's Method

`super()` returns a proxy object that delegates method calls to the parent class. The most common use is in `__init__`, where the child calls `super().__init__()` to run the parent's initialization logic before adding its own.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N1cGVyX2FuZF90aGVfY29uc3RydWN0b3JfY2hhaW4gY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNsYXNzIExpYnJhcnlJdGVtOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibik6XG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG5cbiAgICBkZWYgZGlzcGxheV9pbmZvKHNlbGYpOlxuICAgICAgICByZXR1cm4gZlwie3NlbGYudGl0bGV9IChJU0JOOiB7c2VsZi5pc2JufSlcIlxuXG5jbGFzcyBCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGNvcGllcyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18odGl0bGUsIGlzYm4pICAgIyBkZWxlZ2F0ZXMgdG8gTGlicmFyeUl0ZW0uX19pbml0X19cbiAgICAgICAgc2VsZi5jb3BpZXMgPSBjb3BpZXMgICAgICAgICAgICAjIGFkZHMgb25seSB3aGF0IEJvb2sgbmVlZHNcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50KGIudGl0bGUpICAgICAgICAgICMgRHVuZSAtLSBzZXQgYnkgTGlicmFyeUl0ZW0uX19pbml0X19cbnByaW50KGIuY29waWVzKSAgICAgICAgICMgMyAtLSBzZXQgYnkgQm9vay5fX2luaXRfX1xucHJpbnQoYi5kaXNwbGF5X2luZm8oKSkgIyBEdW5lIChJU0JOOiA5NzgtMDQ0MTAxMzU5MykifQ"
 width="100%"
></iframe>

`super().__init__(title, isbn)` runs `LibraryItem.__init__` with `title` and `isbn`. After that returns, `self.copies = copies` adds the attribute unique to `Book`. Now `self.title` is set in exactly one place.

## All Three Subclasses, Fixed

With `super()`, each subclass delegates the common work upward:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N1cGVyX2FuZF90aGVfY29uc3RydWN0b3JfY2hhaW4gY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNsYXNzIEVCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGZpbGVfc2l6ZV9tYik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18odGl0bGUsIGlzYm4pXG4gICAgICAgIHNlbGYuZmlsZV9zaXplX21iID0gZmlsZV9zaXplX21iXG5cbiAgICBkZWYgaXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByZXR1cm4gVHJ1ZVxuXG5jbGFzcyBBdWRpb2Jvb2soTGlicmFyeUl0ZW0pOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgZHVyYXRpb25faG91cnMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKVxuICAgICAgICBzZWxmLmR1cmF0aW9uX2hvdXJzID0gZHVyYXRpb25faG91cnNcblxuICAgIGRlZiBpc19hdmFpbGFibGUoc2VsZik6XG4gICAgICAgIHJldHVybiBUcnVlIn0"
 width="100%"
></iframe>

Now if Dev adds `self.language = "English"` to `LibraryItem.__init__`, all three subclasses automatically inherit it with no changes required. The parent is the single source of truth for shared initialization.

## super() Is Not Just for __init__

`super()` works for any method, not only `__init__`. A child class can override a method and still call the parent's version to extend rather than completely replace it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N1cGVyX2FuZF90aGVfY29uc3RydWN0b3JfY2hhaW4gY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImNsYXNzIExpYnJhcnlJdGVtOlxuICAgIGRlZiBkaXNwbGF5X2luZm8oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJ7c2VsZi50aXRsZX0gKElTQk46IHtzZWxmLmlzYm59KVwiXG5cbmNsYXNzIEJvb2soTGlicmFyeUl0ZW0pOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0aXRsZSwgaXNibilcbiAgICAgICAgc2VsZi5jb3BpZXMgPSBjb3BpZXNcblxuICAgIGRlZiBkaXNwbGF5X2luZm8oc2VsZik6XG4gICAgICAgIGJhc2UgPSBzdXBlcigpLmRpc3BsYXlfaW5mbygpICAgICAgIyBnZXQgdGhlIHBhcmVudCdzIHZlcnNpb25cbiAgICAgICAgcmV0dXJuIGZcIntiYXNlfSB8IHtzZWxmLmNvcGllc30gY29waWVzXCJcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50KGIuZGlzcGxheV9pbmZvKCkpICAgIyBEdW5lIChJU0JOOiA5NzgtMDQ0MTAxMzU5MykgfCAzIGNvcGllcyJ9"
 width="100%"
></iframe>

The child's `display_info` starts with the parent's output and appends its own extra detail. This pattern, calling `super().method()` and extending the result, is how you build on existing behavior rather than duplicating it.

## The Constructor Chain in Multi-Level Inheritance

Inheritance can be more than one level deep. When `super()` is called, Python follows the Method Resolution Order (MRO) to find the next class in the chain, even when there are three or more levels.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N1cGVyX2FuZF90aGVfY29uc3RydWN0b3JfY2hhaW4gY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImNsYXNzIENvbGxlY3RpYmxlKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGVkaXRpb24pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKVxuICAgICAgICBzZWxmLmVkaXRpb24gPSBlZGl0aW9uXG5cbmNsYXNzIFNpZ25lZEVkaXRpb24oQ29sbGVjdGlibGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgZWRpdGlvbiwgc2lnbmVyKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0aXRsZSwgaXNibiwgZWRpdGlvbikgICAjIGdvZXMgdG8gQ29sbGVjdGlibGUuX19pbml0X19cbiAgICAgICAgc2VsZi5zaWduZXIgPSBzaWduZXJcblxucyA9IFNpZ25lZEVkaXRpb24oXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgXCJGaXJzdCBFZGl0aW9uXCIsIFwiRnJhbmsgSGVyYmVydFwiKVxucHJpbnQocy50aXRsZSkgICAgICAjIER1bmUgLS0gc2V0IGJ5IExpYnJhcnlJdGVtLl9faW5pdF9fXG5wcmludChzLmVkaXRpb24pICAgICMgRmlyc3QgRWRpdGlvbiAtLSBzZXQgYnkgQ29sbGVjdGlibGUuX19pbml0X19cbnByaW50KHMuc2lnbmVyKSAgICAgIyBGcmFuayBIZXJiZXJ0IC0tIHNldCBieSBTaWduZWRFZGl0aW9uLl9faW5pdF9fIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N1cGVyX2FuZF90aGVfY29uc3RydWN0b3JfY2hhaW4gY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIEFuaW1hbDpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbmFtZSwgc3BlY2llcyk6XG4gICAgICAgIHNlbGYubmFtZSA9IG5hbWVcbiAgICAgICAgc2VsZi5zcGVjaWVzID0gc3BlY2llc1xuXG4gICAgZGVmIGRlc2NyaWJlKHNlbGYpOlxuICAgICAgICByZXR1cm4gZlwie3NlbGYubmFtZX0gaXMgYSB7c2VsZi5zcGVjaWVzfVwiXG5cbmNsYXNzIFBldChBbmltYWwpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCBzcGVjaWVzLCBvd25lcik6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18obmFtZSwgc3BlY2llcylcbiAgICAgICAgc2VsZi5vd25lciA9IG93bmVyXG5cbiAgICBkZWYgZGVzY3JpYmUoc2VsZik6XG4gICAgICAgIGJhc2UgPSBzdXBlcigpLmRlc2NyaWJlKClcbiAgICAgICAgcmV0dXJuIGZcIntiYXNlfSwgb3duZWQgYnkge3NlbGYub3duZXJ9XCJcblxuY2xhc3MgVHJhaW5lZFBldChQZXQpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCBzcGVjaWVzLCBvd25lciwgdHJpY2tzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyhuYW1lLCBzcGVjaWVzLCBvd25lcilcbiAgICAgICAgc2VsZi50cmlja3MgPSB0cmlja3NcblxuICAgIGRlZiBkZXNjcmliZShzZWxmKTpcbiAgICAgICAgYmFzZSA9IHN1cGVyKCkuZGVzY3JpYmUoKVxuICAgICAgICByZXR1cm4gZlwie2Jhc2V9LCBrbm93cyB7bGVuKHNlbGYudHJpY2tzKX0gdHJpY2socylcIiJ9"
 width="100%"
></iframe>

Create a `TrainedPet` and call `describe()` on it. Trace through which `describe()` calls which, and in what order, to produce the final string. Then add a `language` attribute to `Animal.__init__` and confirm `TrainedPet` automatically inherits it without any changes to `Pet` or `TrainedPet`.

## Conclusion

`super()` delegates to the parent class's method without hardcoding the parent's name, making inheritance chains clean and maintainable. In `__init__`, it runs the parent's initialization before the child adds its own attributes. In other methods, it calls the parent's version and lets the child extend the result. The next lesson takes this further: what happens when a child class defines a method that already exists in the parent, replacing rather than extending it.

## Introduction

Dev's `LibraryItem` base class has a `checkout_policy()` method that returns a standard 21-day loan period. Physical books follow this rule. Ebooks do not need it at all since they are always available. Reference books can only be used in the library and cannot be checked out. Dev needs each item type to answer the question "what is the checkout policy for this item?" differently, but the calling code should not have to know which type it is talking to.

This is **method overriding**: a child class provides its own implementation of a method that already exists in the parent. It is the mechanism that makes the same method call behave differently depending on which class the object actually belongs to.

![](images/03_method_overriding.png)

## Overriding a Method

When a child class defines a method with the same name as one in the parent, the child's version takes precedence. Python always calls the most specific version it can find, starting with the object's own class.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBMaWJyYXJ5SXRlbTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4pOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuXG4gICAgZGVmIGNoZWNrb3V0X3BvbGljeShzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiMjEtZGF5IGxvYW5cIlxuXG5jbGFzcyBCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGNvcGllcyk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18odGl0bGUsIGlzYm4pXG4gICAgICAgIHNlbGYuY29waWVzID0gY29waWVzXG5cbmNsYXNzIEVCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKVxuXG4gICAgZGVmIGNoZWNrb3V0X3BvbGljeShzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiTm8gbG9hbiBuZWVkZWQ6IGFsd2F5cyBhdmFpbGFibGVcIlxuXG5jbGFzcyBSZWZlcmVuY2VCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4pOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKVxuXG4gICAgZGVmIGNoZWNrb3V0X3BvbGljeShzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiSW4tbGlicmFyeSB1c2Ugb25seTogY2Fubm90IGJlIGNoZWNrZWQgb3V0XCJcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbmViID0gRUJvb2soXCJGb3VuZGF0aW9uXCIsIFwiOTc4LTA1NTMyOTMzNTdcIilcbnJiID0gUmVmZXJlbmNlQm9vayhcIk94Zm9yZCBFbmdsaXNoIERpY3Rpb25hcnlcIiwgXCI5NzgtMDE5OTU3MTEyM1wiKVxuXG5wcmludChiLmNoZWNrb3V0X3BvbGljeSgpKSAgICAjIDIxLWRheSBsb2FuIC0tIHVzZXMgcGFyZW50J3MgdmVyc2lvblxucHJpbnQoZWIuY2hlY2tvdXRfcG9saWN5KCkpICAgIyBObyBsb2FuIG5lZWRlZDogYWx3YXlzIGF2YWlsYWJsZSAtLSBvdmVycmlkZGVuXG5wcmludChyYi5jaGVja291dF9wb2xpY3koKSkgICAjIEluLWxpYnJhcnkgdXNlIG9ubHk6IGNhbm5vdCBiZSBjaGVja2VkIG91dCAtLSBvdmVycmlkZGVuIn0"
 width="100%"
></iframe>

`Book` does not define `checkout_policy()`, so it inherits the parent's 21-day version. `EBook` and `ReferenceBook` each override it with their own behavior.

## When to Override vs. When to Call super()

There are two distinct situations when a child needs to change a parent method. The first is when the child's behavior *completely replaces* the parent's: the parent's version is not needed at all, so the child simply defines a new body.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBSZWZlcmVuY2VCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgY2hlY2tvdXRfcG9saWN5KHNlbGYpOlxuICAgICAgICByZXR1cm4gXCJJbi1saWJyYXJ5IHVzZSBvbmx5OiBjYW5ub3QgYmUgY2hlY2tlZCBvdXRcIlxuICAgICMgcGFyZW50IHZlcnNpb24gZGlzY2FyZGVkOyB3ZSBkbyBub3QgY2FsbCBzdXBlcigpIGhlcmUifQ"
 width="100%"
></iframe>

The second is when the child *extends* the parent's behavior: the parent's version still does useful work, so the child calls `super()` to run it and then adds more.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJjbGFzcyBCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgZGlzcGxheV9pbmZvKHNlbGYpOlxuICAgICAgICBiYXNlID0gc3VwZXIoKS5kaXNwbGF5X2luZm8oKSAgICAgICAgIyBydW4gcGFyZW50J3MgdmVyc2lvbiBmaXJzdFxuICAgICAgICByZXR1cm4gZlwie2Jhc2V9IHwge3NlbGYuY29waWVzfSBjb3BpZXMgYXZhaWxhYmxlXCIifQ"
 width="100%"
></iframe>

The rule of thumb: if the parent's behavior is *wrong* for this child, replace it entirely. If it is *incomplete* for this child, extend it with `super()`.

## Overriding __init__ Without Forgetting super()

The most common mistake with overriding is forgetting `super().__init__()` when overriding `__init__`. Without it, the parent's initialization does not run, and attributes the parent sets are missing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBNYWdhemluZShMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBpc3N1ZV9udW1iZXIpOlxuICAgICAgICAjIFdST05HOiBmb3Jnb3Qgc3VwZXIoKS5fX2luaXRfX1xuICAgICAgICAjIHNlbGYudGl0bGUgYW5kIHNlbGYuaXNibiBuZXZlciBnZXQgc2V0XG4gICAgICAgIHNlbGYuaXNzdWVfbnVtYmVyID0gaXNzdWVfbnVtYmVyXG5cbm0gPSBNYWdhemluZShcIk5hdHVyZVwiLCBcIjAwMjgtMDgzNlwiLCA1MilcbnByaW50KG0uaXNzdWVfbnVtYmVyKSAgICAjIDUyIC0tIGZpbmVcbnByaW50KG0udGl0bGUpICAgICAgICAgICAjIEF0dHJpYnV0ZUVycm9yOiAnTWFnYXppbmUnIG9iamVjdCBoYXMgbm8gYXR0cmlidXRlICd0aXRsZScifQ"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBNYWdhemluZShMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBpc3N1ZV9udW1iZXIpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKSAgICAjIGNvcnJlY3Q6IHBhcmVudCBzZXRzIHRpdGxlIGFuZCBpc2JuXG4gICAgICAgIHNlbGYuaXNzdWVfbnVtYmVyID0gaXNzdWVfbnVtYmVyXG5cbm0gPSBNYWdhemluZShcIk5hdHVyZVwiLCBcIjAwMjgtMDgzNlwiLCA1MilcbnByaW50KG0udGl0bGUpICAgICAgICAgICMgTmF0dXJlIC0tIG5vdyBjb3JyZWN0XG5wcmludChtLmlzc3VlX251bWJlcikgICAjIDUyIn0"
 width="100%"
></iframe>

## A Complete Override Example With checkout_policy

Here is the full pattern applied consistently across all item types:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpdGVtcyA9IFtcbiAgICBCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDMpLFxuICAgIEVCb29rKFwiRm91bmRhdGlvblwiLCBcIjk3OC0wNTUzMjkzMzU3XCIpLFxuICAgIFJlZmVyZW5jZUJvb2soXCJPeGZvcmQgRGljdGlvbmFyeVwiLCBcIjk3OC0wMTk5NTcxMTIzXCIpLFxuICAgIE1hZ2F6aW5lKFwiTmF0dXJlXCIsIFwiMDAyOC0wODM2XCIsIDUyKSxcbl1cblxuZm9yIGl0ZW0gaW4gaXRlbXM6XG4gICAgcHJpbnQoZlwie2l0ZW0udGl0bGV9OiB7aXRlbS5jaGVja291dF9wb2xpY3koKX1cIilcblxuIyBEdW5lOiAyMS1kYXkgbG9hblxuIyBGb3VuZGF0aW9uOiBObyBsb2FuIG5lZWRlZDogYWx3YXlzIGF2YWlsYWJsZVxuIyBJbi1saWJyYXJ5IHVzZSBvbmx5OiBjYW5ub3QgYmUgY2hlY2tlZCBvdXRcbiMgT3hmb3JkIERpY3Rpb25hcnk6IDIxLWRheSBsb2FuICA8LSBNYWdhemluZSBpbmhlcml0cyB0aGUgZGVmYXVsdCJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX21ldGhvZF9vdmVycmlkaW5nIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJjbGFzcyBTaGFwZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY29sb3IpOlxuICAgICAgICBzZWxmLmNvbG9yID0gY29sb3JcblxuICAgIGRlZiBhcmVhKHNlbGYpOlxuICAgICAgICByYWlzZSBOb3RJbXBsZW1lbnRlZEVycm9yKFwiU3ViY2xhc3NlcyBtdXN0IGltcGxlbWVudCBhcmVhKClcIilcblxuICAgIGRlZiBkZXNjcmliZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIkEge3NlbGYuY29sb3J9IHNoYXBlIHdpdGggYXJlYSB7c2VsZi5hcmVhKCk6LjJmfVwiXG5cbmNsYXNzIENpcmNsZShTaGFwZSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNvbG9yLCByYWRpdXMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKGNvbG9yKVxuICAgICAgICBzZWxmLnJhZGl1cyA9IHJhZGl1c1xuXG4gICAgZGVmIGFyZWEoc2VsZik6XG4gICAgICAgIHJldHVybiAzLjE0MTU5ICogc2VsZi5yYWRpdXMgKiogMlxuXG5jbGFzcyBSZWN0YW5nbGUoU2hhcGUpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjb2xvciwgd2lkdGgsIGhlaWdodCk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oY29sb3IpXG4gICAgICAgIHNlbGYud2lkdGggPSB3aWR0aFxuICAgICAgICBzZWxmLmhlaWdodCA9IGhlaWdodFxuXG4gICAgZGVmIGFyZWEoc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLndpZHRoICogc2VsZi5oZWlnaHQifQ"
 width="100%"
></iframe>

Create a `Circle` and a `Rectangle` and call `describe()` on each. Notice that `describe()` is defined only in `Shape`, but it calls `self.area()`, which executes the correct version for each child. Then add a `Square(Rectangle)` that accepts only `side` in its `__init__` and passes `side, side` to `Rectangle.__init__`. Confirm that `describe()` still works on a `Square` without any changes to `Shape` or `Rectangle`.

## Conclusion

Method overriding lets a child class replace or extend a parent method. When the parent's behavior is completely wrong for the child, the child defines a new body with no call to `super()`. When the parent's behavior is useful but incomplete, the child calls `super().method()` and adds to the result. Always call `super().__init__()` when overriding `__init__`, or the parent's attributes will be missing. The next lesson builds on this to introduce polymorphism: what it means that the same method call behaves differently depending on the actual type of the object at runtime.

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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBvc2l0aW9uX3ZzX2luaGVyaXRhbmNlIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIEluaGVyaXRhbmNlOiBCb29rIElTLUEgTGlicmFyeUl0ZW1cbmNsYXNzIEJvb2soTGlicmFyeUl0ZW0pOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0aXRsZSwgaXNibilcbiAgICAgICAgc2VsZi5jb3BpZXMgPSBjb3BpZXNcblxuIyBDb21wb3NpdGlvbjogSW52ZW50b3J5IEhBUy1BIGxpc3Qgb2YgTGlicmFyeUl0ZW1zXG5jbGFzcyBJbnZlbnRvcnk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLl9pdGVtcyA9IFtdICAgICAjIGNvbnRhaW5zIExpYnJhcnlJdGVtIG9iamVjdHMsIGlzIG5vdCBvbmVcblxuICAgIGRlZiBhZGQoc2VsZiwgaXRlbSk6XG4gICAgICAgIHNlbGYuX2l0ZW1zLmFwcGVuZChpdGVtKVxuXG4gICAgZGVmIGNvdW50KHNlbGYpOlxuICAgICAgICByZXR1cm4gbGVuKHNlbGYuX2l0ZW1zKVxuXG4gICAgZGVmIGF2YWlsYWJsZV9pdGVtcyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIFtpdGVtIGZvciBpdGVtIGluIHNlbGYuX2l0ZW1zIGlmIGl0ZW0uaXNfYXZhaWxhYmxlKCldIn0"
 width="100%"
></iframe>

## The Liskov Substitution Principle

A useful rule of thumb: if you inherit, anywhere the parent class is used, the child should be usable as a drop-in replacement. If that is not true, inheritance is the wrong relationship.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBvc2l0aW9uX3ZzX2luaGVyaXRhbmNlIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJkZWYgcHJpbnRfY2hlY2tvdXRfcG9saWN5KGl0ZW0pOiAgICMgd29ya3Mgb24gYW55IExpYnJhcnlJdGVtXG4gICAgcHJpbnQoaXRlbS5jaGVja291dF9wb2xpY3koKSlcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50X2NoZWNrb3V0X3BvbGljeShiKSAgICAjIHdvcmtzIC0tIEJvb2sgaXMgYSBMaWJyYXJ5SXRlbSJ9"
 width="100%"
></iframe>

An `Inventory` cannot replace a `LibraryItem` in `print_checkout_policy`. An inventory is not a library item. If a subclass does not actually substitute for its parent in the way callers expect, it is a sign that inheritance was chosen for the wrong reason.

## When Inheritance Goes Wrong: "Fragile Base Class"

A class hierarchy that is too deep or too broad becomes brittle. When the parent class changes an internal detail, all children that depend on that detail break, sometimes in surprising ways. Composition avoids this: if `Inventory` holds items as a list rather than inheriting from a catalog class, the catalog class can change its internals without affecting `Inventory` at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBvc2l0aW9uX3ZzX2luaGVyaXRhbmNlIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIEZyYWdpbGUgaGllcmFyY2h5IC0tIEludmVudG9yeSBpbmhlcml0cyBmcm9tIExpYnJhcnlJdGVtIGZvciBubyBnb29kIHJlYXNvblxuY2xhc3MgSW52ZW50b3J5KExpYnJhcnlJdGVtKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGl0ZW1zKTpcbiAgICAgICAgc3VwZXIoKS5fX2luaXRfXyh0aXRsZSwgaXNibikgICAjIEludmVudG9yeSBpcyBub3QgYSBsaWJyYXJ5IGl0ZW1cbiAgICAgICAgc2VsZi5faXRlbXMgPSBpdGVtc1xuICAgICMgSW5oZXJpdHMgY2hlY2tvdXRfcG9saWN5KCkgYW5kIGRpc3BsYXlfaW5mbygpIHdoaWNoIG1ha2Ugbm8gc2Vuc2UgZm9yIGludmVudG9yeVxuXG4jIENsZWFuZXI6IGNvbXBvc2l0aW9uXG5jbGFzcyBJbnZlbnRvcnk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLl9pdGVtcyA9IFtdXG5cbiAgICBkZWYgYWRkKHNlbGYsIGl0ZW0pOlxuICAgICAgICBzZWxmLl9pdGVtcy5hcHBlbmQoaXRlbSlcblxuICAgIGRlZiB0b3RhbF9hdmFpbGFibGUoc2VsZik6XG4gICAgICAgIHJldHVybiBzdW0oMSBmb3IgaXRlbSBpbiBzZWxmLl9pdGVtcyBpZiBpdGVtLmlzX2F2YWlsYWJsZSgpKSJ9"
 width="100%"
></iframe>

The composed version is simpler, easier to test (you can create an `Inventory` with mock items), and unaffected by changes to `LibraryItem`.

## Composition and Delegation

Composition often pairs with delegation: the outer object passes method calls through to an inner object it holds, rather than inheriting those methods.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBvc2l0aW9uX3ZzX2luaGVyaXRhbmNlIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBOb3RpZmljYXRpb25TZXJ2aWNlOlxuICAgIGRlZiBzZW5kKHNlbGYsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgICAgICBwcmludChmXCJbTk9USUZZXSB7Y29udGFjdH06IHttZXNzYWdlfVwiKVxuXG5jbGFzcyBSZXNlcnZhdGlvbk1hbmFnZXI6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5vdGlmaWVyKTpcbiAgICAgICAgc2VsZi5fbm90aWZpZXIgPSBub3RpZmllciAgICAjIEhBUy1BIE5vdGlmaWNhdGlvblNlcnZpY2VcblxuICAgIGRlZiBub3RpZnlfcGF0cm9uKHNlbGYsIHBhdHJvbl9jb250YWN0LCBib29rX3RpdGxlKTpcbiAgICAgICAgc2VsZi5fbm90aWZpZXIuc2VuZChwYXRyb25fY29udGFjdCwgZlwiJ3tib29rX3RpdGxlfScgaXMgbm93IGF2YWlsYWJsZS5cIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBvc2l0aW9uX3ZzX2luaGVyaXRhbmNlIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBFbmdpbmU6XG4gICAgZGVmIHN0YXJ0KHNlbGYpOlxuICAgICAgICByZXR1cm4gXCJFbmdpbmUgc3RhcnRlZFwiXG5cbiAgICBkZWYgc3RvcChzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiRW5naW5lIHN0b3BwZWRcIlxuXG5jbGFzcyBDYXI6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG1ha2UsIG1vZGVsKTpcbiAgICAgICAgc2VsZi5tYWtlID0gbWFrZVxuICAgICAgICBzZWxmLm1vZGVsID0gbW9kZWxcbiAgICAgICAgc2VsZi5fZW5naW5lID0gRW5naW5lKClcblxuICAgIGRlZiBkcml2ZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2VuZ2luZS5zdGFydCgpICsgXCIgLS0gZHJpdmluZ1wiXG5cbiAgICBkZWYgcGFyayhzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2VuZ2luZS5zdG9wKCkgKyBcIiAtLSBwYXJrZWRcIiJ9"
 width="100%"
></iframe>

`Car` uses composition: it *has* an `Engine`. Consider what would happen if you had written `class Car(Engine):` instead: would `isinstance(my_car, Engine)` make semantic sense? What would callers be allowed to do to a `Car` object that they should not be able to do? Use this analysis to articulate in one sentence why composition is the right choice here.

## Conclusion

Inheritance models "is-a" relationships, where the child genuinely substitutes for the parent. Composition models "has-a" relationships, where one object holds and uses another without claiming to be that thing. The test is whether the child class should be a drop-in replacement for the parent anywhere the parent is used; if not, composition is almost always cleaner and more maintainable. The next lesson focuses on the dunder methods that make your objects integrate naturally into Python's syntax, building directly on the data-model introduction from Unit 1.

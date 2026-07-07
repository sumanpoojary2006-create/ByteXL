## Introduction

Dev's `Book` class needs a factory function that creates a `Book` from a dictionary (like the kind that comes back from a JSON API). He writes it as a regular function outside the class, but it feels disconnected: someone reading the code later has to guess that `book_from_dict()` is related to `Book`. He wants it to live inside the class, but it does not operate on an instance (`self`) because it creates new instances. He needs something between a method and a standalone function.

Python provides three kinds of callable objects you can define inside a class body. Understanding when to use each one is what separates well-organized class code from code that technically works but is confusing to read.

![](images/09_class_static_instance_methods.png)

## Instance Methods: The Default

An **instance method** receives `self` as its first argument, giving it access to the specific object it was called on. Everything you have written so far in this unit falls into this category. Instance methods can read and modify the instance's attributes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NsYXNzX3N0YXRpY19hbmRfaW5zdGFuY2VfbWV0aG9kcyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGNvcGllcyk6XG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgZGVmIGNoZWNrX291dChzZWxmKTogICAgICAgICMgaW5zdGFuY2UgbWV0aG9kOiBvcGVyYXRlcyBvbiBzZWxmXG4gICAgICAgIGlmIHNlbGYuX2NvcGllcyA8IDE6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIk5vIGNvcGllcyBvZiAne3NlbGYudGl0bGV9JyBhdmFpbGFibGVcIilcbiAgICAgICAgc2VsZi5fY29waWVzIC09IDFcblxuICAgIGRlZiBjb3BpZXNfYXZhaWxhYmxlKHNlbGYpOiAgIyBpbnN0YW5jZSBtZXRob2Q6IHJlYWRzIHNlbGZcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllc1xuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiLCAzKVxuYi5jaGVja19vdXQoKVxucHJpbnQoYi5jb3BpZXNfYXZhaWxhYmxlKCkpICAgIyAyIn0"
 width="100%"
></iframe>

When you call `b.check_out()`, Python passes `b` as `self` automatically.

## Class Methods: Receiving the Class, Not an Instance

A **class method** receives `cls` (the class itself) as its first argument rather than `self`. It is defined with the `@classmethod` decorator. Class methods have access to the class and all its class attributes, but not to any specific instance.

The most common use is as an **alternative constructor**: a factory method that creates instances from a different input format.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NsYXNzX3N0YXRpY19hbmRfaW5zdGFuY2VfbWV0aG9kcyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGNvcGllcyk6XG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgQGNsYXNzbWV0aG9kXG4gICAgZGVmIGZyb21fZGljdChjbHMsIGRhdGEpOlxuICAgICAgICByZXR1cm4gY2xzKFxuICAgICAgICAgICAgdGl0bGU9ZGF0YVtcInRpdGxlXCJdLFxuICAgICAgICAgICAgaXNibj1kYXRhW1wiaXNiblwiXSxcbiAgICAgICAgICAgIGNvcGllcz1kYXRhLmdldChcImNvcGllc1wiLCAxKVxuICAgICAgICApXG5cbiAgICBAY2xhc3NtZXRob2RcbiAgICBkZWYgZnJvbV9pc2JuKGNscywgaXNibik6XG4gICAgICAgIHJldHVybiBjbHModGl0bGU9XCJVbmtub3duXCIsIGlzYm49aXNibiwgY29waWVzPTApXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHtzZWxmLnRpdGxlIXJ9LCB7c2VsZi5pc2JuIXJ9LCBjb3BpZXM9e3NlbGYuX2NvcGllc30pXCJcblxuYXBpX3Jlc3BvbnNlID0ge1widGl0bGVcIjogXCJEdW5lXCIsIFwiaXNiblwiOiBcIjk3OC0wNDQxMDEzNTkzXCIsIFwiY29waWVzXCI6IDN9XG5iID0gQm9vay5mcm9tX2RpY3QoYXBpX3Jlc3BvbnNlKVxucHJpbnQoYikgICAjIEJvb2soJ0R1bmUnLCAnOTc4LTA0NDEwMTM1OTMnLCBjb3BpZXM9MylcblxuYjIgPSBCb29rLmZyb21faXNibihcIjk3OC0wNTUzMjkzMzU3XCIpXG5wcmludChiMikgICMgQm9vaygnVW5rbm93bicsICc5NzgtMDU1MzI5MzM1NycsIGNvcGllcz0wKSJ9"
 width="100%"
></iframe>

Using `cls(...)` rather than `Book(...)` inside the class method is important: it means the method works correctly if a subclass calls it, creating the correct subclass instance rather than always creating a `Book`.

## Static Methods: Utilities That Belong to the Class

A **static method** receives neither `self` nor `cls`. It has no access to the instance or the class at all. It is defined with `@staticmethod` and is essentially a regular function that lives inside the class namespace because it is conceptually related to the class.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NsYXNzX3N0YXRpY19hbmRfaW5zdGFuY2VfbWV0aG9kcyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGNvcGllcyk6XG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgQHN0YXRpY21ldGhvZFxuICAgIGRlZiBpc192YWxpZF9pc2JuKGlzYm4pOlxuICAgICAgICByZXR1cm4gaXNpbnN0YW5jZShpc2JuLCBzdHIpIGFuZCBpc2JuLnN0YXJ0c3dpdGgoXCI5NzhcIilcblxuICAgIEBjbGFzc21ldGhvZFxuICAgIGRlZiBmcm9tX2RpY3QoY2xzLCBkYXRhKTpcbiAgICAgICAgaWYgbm90IGNscy5pc192YWxpZF9pc2JuKGRhdGEuZ2V0KFwiaXNiblwiLCBcIlwiKSk6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIkludmFsaWQgSVNCTjoge2RhdGEuZ2V0KCdpc2JuJyl9XCIpXG4gICAgICAgIHJldHVybiBjbHMoZGF0YVtcInRpdGxlXCJdLCBkYXRhW1wiaXNiblwiXSwgZGF0YS5nZXQoXCJjb3BpZXNcIiwgMSkpXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHtzZWxmLnRpdGxlIXJ9KVwiXG5cbnByaW50KEJvb2suaXNfdmFsaWRfaXNibihcIjk3OC0wNDQxMDEzNTkzXCIpKSAgICMgVHJ1ZVxucHJpbnQoQm9vay5pc192YWxpZF9pc2JuKFwiYWJjXCIpKSAgICAgICAgICAgICAjIEZhbHNlIn0"
 width="100%"
></iframe>

The rule for static methods: use one when the function is logically associated with the class, but it does not need to know what class it is called on or what object it was called from. If it needs neither `self` nor `cls`, it is a static method (or possibly just a module-level function).

## When to Use Each Kind

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NsYXNzX3N0YXRpY19hbmRfaW5zdGFuY2VfbWV0aG9kcyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiIyBJbnN0YW5jZSBtZXRob2Q6IHRoZSBmdW5jdGlvbiBuZWVkcyB0byByZWFkIG9yIG1vZGlmeSBhIHNwZWNpZmljIG9iamVjdCdzIHN0YXRlXG5kZWYgY2hlY2tfb3V0KHNlbGYpOlxuICAgIHNlbGYuX2NvcGllcyAtPSAxXG5cbiMgQ2xhc3MgbWV0aG9kOiB0aGUgZnVuY3Rpb24gY3JlYXRlcyBpbnN0YW5jZXMsIGNvdW50cyBpbnN0YW5jZXMsIG9yXG4jIHdvcmtzIHdpdGggY2xhc3MtbGV2ZWwgc3RhdGVcbkBjbGFzc21ldGhvZFxuZGVmIGZyb21fZGljdChjbHMsIGRhdGEpOlxuICAgIHJldHVybiBjbHMoZGF0YVtcInRpdGxlXCJdLCBkYXRhW1wiaXNiblwiXSwgZGF0YS5nZXQoXCJjb3BpZXNcIiwgMSkpXG5cbiMgU3RhdGljIG1ldGhvZDogdGhlIGZ1bmN0aW9uIGlzIHJlbGF0ZWQgdG8gdGhlIGNsYXNzIGNvbmNlcHR1YWxseVxuIyBidXQgZG9lcyBub3QgbmVlZCBzZWxmIG9yIGNsc1xuQHN0YXRpY21ldGhvZFxuZGVmIGlzX3ZhbGlkX2lzYm4oaXNibik6XG4gICAgcmV0dXJuIGlzYm4uc3RhcnRzd2l0aChcIjk3OFwiKSJ9"
 width="100%"
></iframe>

## Class, Static, and Instance Methods at a Glance

| Kind | Decorator | First argument | Has access to |
|---|---|---|---|
| Instance method | (none) | `self` | Instance attributes and class |
| Class method | `@classmethod` | `cls` | Class and class attributes only |
| Static method | `@staticmethod` | (none) | Neither instance nor class |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NsYXNzX3N0YXRpY19hbmRfaW5zdGFuY2VfbWV0aG9kcyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZnJvbSBkYXRhY2xhc3NlcyBpbXBvcnQgZGF0YWNsYXNzLCBmaWVsZFxuZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZVxuXG5AZGF0YWNsYXNzXG5jbGFzcyBMb2FuOlxuICAgIHBhdHJvbl9uYW1lOiBzdHJcbiAgICBib29rX2lzYm46IHN0clxuICAgIGR1ZV9kYXRlOiBkYXRlXG4gICAgcmV0dXJuZWQ6IGJvb2wgPSBGYWxzZVxuXG4gICAgQGNsYXNzbWV0aG9kXG4gICAgZGVmIGZvcl90b2RheShjbHMsIHBhdHJvbl9uYW1lLCBib29rX2lzYm4sIGRheXM9MjEpOlxuICAgICAgICBmcm9tIGRhdGV0aW1lIGltcG9ydCB0aW1lZGVsdGFcbiAgICAgICAgZHVlID0gZGF0ZS50b2RheSgpICsgdGltZWRlbHRhKGRheXM9ZGF5cylcbiAgICAgICAgcmV0dXJuIGNscyhwYXRyb25fbmFtZSwgYm9va19pc2JuLCBkdWUpXG5cbiAgICBAc3RhdGljbWV0aG9kXG4gICAgZGVmIGlzX292ZXJkdWVfYnkoZHVlX2RhdGUsIHRvZGF5KTpcbiAgICAgICAgcmV0dXJuIHRvZGF5ID4gZHVlX2RhdGVcblxuICAgIGRlZiBtYXJrX3JldHVybmVkKHNlbGYpOlxuICAgICAgICBzZWxmLnJldHVybmVkID0gVHJ1ZSJ9"
 width="100%"
></iframe>

Create a `Loan` using `Loan.for_today("Priya", "978-0441013593")`. Then use `Loan.is_overdue_by` with a date in the past to confirm the static method works as a standalone check. Finally, call `mark_returned()` on the loan and confirm `loan.returned` is `True`. Explain why `is_overdue_by` is a better fit for `@staticmethod` than `@classmethod`.

## Conclusion

Instance methods operate on a specific object via `self`. Class methods operate on the class itself via `cls` and are most useful as alternative constructors. Static methods are utility functions logically associated with the class but needing neither `self` nor `cls`. Choosing the right kind of method makes a class's intent clearer: instance methods change or inspect state, class methods create or configure at the class level, and static methods group related logic without coupling it to state. This completes Unit 3's coverage of inheritance, polymorphism, dunder methods, dataclasses, and method types. Unit 4 moves from class design to a different kind of elegance: making objects that Python can iterate over lazily, processing items one at a time without loading everything into memory at once.

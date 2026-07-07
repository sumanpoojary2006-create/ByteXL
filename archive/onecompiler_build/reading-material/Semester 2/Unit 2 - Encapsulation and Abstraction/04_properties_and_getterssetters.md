## Introduction

Priya's team has a dilemma. Half the codebase already accesses `book.copies` as a plain attribute. Renaming it to `_copies` and adding a `copies_available()` method would fix the design, but it would break every line of code that already uses `book.copies`. She needs a way to add validation logic to an attribute without changing how callers interact with it, so that `book.copies` still looks like a plain attribute from the outside but secretly runs validation code when read or written.

Python's `@property` decorator solves this exactly. It is one of the most useful tools in Python's object-oriented toolkit, and it is the reason you will almost never see explicit "getter" and "setter" methods in well-designed Python code.

![](images/04_properties_getters_setters.png)

## The Simplest Property: A Computed Read-Only Value

The most basic use of `@property` is turning a method into something that reads like an attribute. Rather than calling `book.is_available()`, callers can read `book.is_available` with no parentheses, and Python calls the method invisibly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3Byb3BlcnRpZXNfYW5kX2dldHRlcnNzZXR0ZXJzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgQHByb3BlcnR5XG4gICAgZGVmIGlzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllcyA-IDBcblxuYiA9IEJvb2soXCJEdW5lXCIsIDMpXG5wcmludChiLmlzX2F2YWlsYWJsZSkgICAgIyBUcnVlIC0tIGNhbGxlZCBsaWtlIGFuIGF0dHJpYnV0ZSwgbm8gcGFyZW50aGVzZXNcbmIuX2NvcGllcyA9IDBcbnByaW50KGIuaXNfYXZhaWxhYmxlKSAgICAjIEZhbHNlIn0"
 width="100%"
></iframe>

The `@property` decorator tells Python: "when someone reads `obj.is_available`, call this function." The result is a cleaner, more natural interface: `if book.is_available:` reads like English rather than `if book.is_available():`.

## Adding a Setter: Validation on Write

The real power of properties appears when you add a **setter**. A setter runs code whenever someone writes to the attribute, which is exactly where Priya needs to add her validation.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3Byb3BlcnRpZXNfYW5kX2dldHRlcnNzZXR0ZXJzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuY29waWVzID0gY29waWVzICAgICMgdGhpcyBjYWxscyB0aGUgc2V0dGVyIGltbWVkaWF0ZWx5XG5cbiAgICBAcHJvcGVydHlcbiAgICBkZWYgY29waWVzKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5fY29waWVzXG5cbiAgICBAY29waWVzLnNldHRlclxuICAgIGRlZiBjb3BpZXMoc2VsZiwgdmFsdWUpOlxuICAgICAgICBpZiBub3QgaXNpbnN0YW5jZSh2YWx1ZSwgaW50KTpcbiAgICAgICAgICAgIHJhaXNlIFR5cGVFcnJvcihmXCJjb3BpZXMgbXVzdCBiZSBhbiBpbnQsIGdvdCB7dHlwZSh2YWx1ZSkuX19uYW1lX199XCIpXG4gICAgICAgIGlmIHZhbHVlIDwgMDpcbiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiY29waWVzIGNhbm5vdCBiZSBuZWdhdGl2ZSwgZ290IHt2YWx1ZX1cIilcbiAgICAgICAgc2VsZi5fY29waWVzID0gdmFsdWVcblxuYiA9IEJvb2soXCJEdW5lXCIsIDMpXG5wcmludChiLmNvcGllcykgICAgICMgMyAtLSBnZXR0ZXIgY2FsbGVkXG5iLmNvcGllcyA9IDIgICAgICAgICMgc2V0dGVyIGNhbGxlZCwgdmFsaWRhdGlvbiBwYXNzZXNcbmIuY29waWVzID0gLTEgICAgICAgIyBlcnJvciEgVmFsdWVFcnJvclxuYi5jb3BpZXMgPSBcInRocmVlXCIgICMgZXJyb3IhIFR5cGVFcnJvciJ9"
 width="100%"
></iframe>

Notice a detail in `__init__`: `self.copies = copies` rather than `self._copies = copies`. This is intentional: by routing through the setter from the very start, validation applies even at object creation time. Any invalid initial value is caught immediately.

## Adding a Deleter (Rarely Needed)

A third decorator, `@name.deleter`, runs code when someone calls `del obj.name`. This is rarely needed but occasionally useful, for example when deletion should trigger cleanup.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3Byb3BlcnRpZXNfYW5kX2dldHRlcnNzZXR0ZXJzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgQHByb3BlcnR5XG4gICAgZGVmIGNvcGllcyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllc1xuXG4gICAgQGNvcGllcy5zZXR0ZXJcbiAgICBkZWYgY29waWVzKHNlbGYsIHZhbHVlKTpcbiAgICAgICAgaWYgdmFsdWUgPCAwOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcImNvcGllcyBjYW5ub3QgYmUgbmVnYXRpdmVcIilcbiAgICAgICAgc2VsZi5fY29waWVzID0gdmFsdWVcblxuICAgIEBjb3BpZXMuZGVsZXRlclxuICAgIGRlZiBjb3BpZXMoc2VsZik6XG4gICAgICAgIHByaW50KGZcIlJlbW92aW5nIGNvcHkgY291bnQgZm9yICd7c2VsZi50aXRsZX0nXCIpXG4gICAgICAgIGRlbCBzZWxmLl9jb3BpZXNcblxuYiA9IEJvb2soXCJEdW5lXCIsIDMpXG5kZWwgYi5jb3BpZXMgICAjIHByaW50cyB0aGUgbWVzc2FnZSJ9"
 width="100%"
></iframe>

## Why Python Does Not Use get_x() and set_x() Methods

In Java and C++, the standard pattern is to write `getCopies()` and `setCopies()` methods explicitly. Python's `@property` makes this unnecessary: you can start with a plain attribute and add a property later without changing any code that uses the object. This is the Pythonic approach: start simple, add complexity only when you need it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3Byb3BlcnRpZXNfYW5kX2dldHRlcnNzZXR0ZXJzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIFN0YWdlIDE6IHNpbXBsZSBhdHRyaWJ1dGUgLS0gdG90YWxseSBmaW5lIGZvciBhIHByb3RvdHlwZVxuY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGNvcGllcyk6XG4gICAgICAgIHNlbGYuY29waWVzID0gY29waWVzICAgIyBwbGFpbiBhdHRyaWJ1dGVcblxuIyBTdGFnZSAyOiBhZGQgdmFsaWRhdGlvbiB3aXRob3V0IGJyZWFraW5nIGNhbGxlcnNcbmNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLmNvcGllcyA9IGNvcGllcyAgICMgc3RpbGwgbG9va3MgdGhlIHNhbWUgZnJvbSBvdXRzaWRlXG5cbiAgICBAcHJvcGVydHlcbiAgICBkZWYgY29waWVzKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5fY29waWVzXG5cbiAgICBAY29waWVzLnNldHRlclxuICAgIGRlZiBjb3BpZXMoc2VsZiwgdmFsdWUpOlxuICAgICAgICBpZiB2YWx1ZSA8IDA6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKFwiY29waWVzIGNhbm5vdCBiZSBuZWdhdGl2ZVwiKVxuICAgICAgICBzZWxmLl9jb3BpZXMgPSB2YWx1ZSJ9"
 width="100%"
></iframe>

Every caller that used `book.copies = 2` before the refactor still uses `book.copies = 2` after. Nothing broke. The validation just appeared silently behind the same interface.

## Properties at a Glance

| Decorator | What it defines | When it runs |
|---|---|---|
| `@property` | The getter | When `obj.name` is read |
| `@name.setter` | The setter | When `obj.name = value` is written |
| `@name.deleter` | The deleter | When `del obj.name` is called |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3Byb3BlcnRpZXNfYW5kX2dldHRlcnNzZXR0ZXJzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBUZW1wZXJhdHVyZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgY2Vsc2l1cyk6XG4gICAgICAgIHNlbGYuY2Vsc2l1cyA9IGNlbHNpdXMgICAjIHJvdXRlcyB0aHJvdWdoIHNldHRlclxuXG4gICAgQHByb3BlcnR5XG4gICAgZGVmIGNlbHNpdXMoc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLl9jZWxzaXVzXG5cbiAgICBAY2Vsc2l1cy5zZXR0ZXJcbiAgICBkZWYgY2Vsc2l1cyhzZWxmLCB2YWx1ZSk6XG4gICAgICAgIGlmIHZhbHVlIDwgLTI3My4xNTpcbiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiVGVtcGVyYXR1cmUgYmVsb3cgYWJzb2x1dGUgemVybzoge3ZhbHVlfVwiKVxuICAgICAgICBzZWxmLl9jZWxzaXVzID0gdmFsdWVcblxuICAgIEBwcm9wZXJ0eVxuICAgIGRlZiBmYWhyZW5oZWl0KHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5fY2Vsc2l1cyAqIDkgLyA1ICsgMzIifQ"
 width="100%"
></iframe>

Test this class by reading both `celsius` and `fahrenheit` (note: `fahrenheit` is read-only since it has no setter). Try to set `celsius` to `-300` and confirm the error. Then add a `fahrenheit` setter that converts the value back to Celsius and stores it, so that setting `t.fahrenheit = 32` results in `t.celsius == 0`.

## Conclusion

The `@property` decorator transforms method calls into attribute-like access, letting you add validation, computation, and cleanup behind a clean interface without changing any code that uses the object. The getter runs on read, the setter on write, and you can start with a plain attribute and add a property later without breaking anything. The next lesson moves from attribute access to a larger question: how do you design a class that hides not just its data, but the complexity of its entire implementation, presenting only what callers need to know?

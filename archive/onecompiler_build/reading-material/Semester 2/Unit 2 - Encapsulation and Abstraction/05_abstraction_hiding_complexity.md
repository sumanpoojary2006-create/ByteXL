## Introduction

Priya's library system needs to notify patrons when a reserved book becomes available. The notification can arrive as an email, an SMS, or a push notification, depending on the patron's preferences. She starts writing the notification code and realizes she is facing a different kind of design problem from the one encapsulation solved. Encapsulation was about protecting state. This problem is about defining a consistent behavior that multiple different systems need to provide, without the calling code caring which system it is talking to.

She needs a reservation manager that can trigger a notification without knowing whether it is sending an email or an SMS. She needs to hide the complexity of each notification method behind a single, consistent interface. This idea has a name: **abstraction**.

![](images/05_abstraction_hiding_complexity.png)

## What Abstraction Means

Abstraction means exposing what something *does* while hiding how it does it. A calling function should be able to say "send a notification" without knowing or caring what sending involves: opening a socket, formatting HTML, calling a third-party API, or something else entirely.

This is not the same as encapsulation, though the two work together. Encapsulation hides internal state inside a single class. Abstraction defines a shared interface that multiple unrelated classes can implement, allowing calling code to treat them interchangeably.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFRoZSBjYWxsaW5nIGNvZGUgc2hvdWxkIGxvb2sgbGlrZSB0aGlzIC0tIGl0IGFza3MgZm9yIGEgbm90aWZpY2F0aW9uXG4jIHdpdGhvdXQga25vd2luZyBvciBjYXJpbmcgd2hpY2ggc3lzdGVtIGRlbGl2ZXJzIGl0OlxuZGVmIG5vdGlmeV9wYXRyb24obm90aWZpZXIsIHBhdHJvbiwgYm9va190aXRsZSk6XG4gICAgbm90aWZpZXIuc2VuZChwYXRyb24uY29udGFjdCwgZlwiJ3tib29rX3RpdGxlfScgaXMgbm93IGF2YWlsYWJsZS5cIikifQ"
 width="100%"
></iframe>

For this to work, every `notifier` object must guarantee it has a `send` method that accepts a contact address and a message. Abstraction is the design pattern; the next lesson shows the Python mechanism for enforcing it.

## Designing for Abstraction: Concrete vs. Abstract

The idea of a "notifier" is abstract: it represents a category of things that can send messages, without specifying which particular channel is used. Specific implementations (email, SMS) are concrete.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBFbWFpbE5vdGlmaWVyOlxuICAgIGRlZiBzZW5kKHNlbGYsIGFkZHJlc3MsIG1lc3NhZ2UpOlxuICAgICAgICBwcmludChmXCJFbWFpbCB0byB7YWRkcmVzc306IHttZXNzYWdlfVwiKVxuXG5jbGFzcyBTTVNOb3RpZmllcjpcbiAgICBkZWYgc2VuZChzZWxmLCBwaG9uZSwgbWVzc2FnZSk6XG4gICAgICAgIHByaW50KGZcIlNNUyB0byB7cGhvbmV9OiB7bWVzc2FnZX1cIilcblxuY2xhc3MgUHVzaE5vdGlmaWVyOlxuICAgIGRlZiBzZW5kKHNlbGYsIGRldmljZV9pZCwgbWVzc2FnZSk6XG4gICAgICAgIHByaW50KGZcIlB1c2ggdG8ge2RldmljZV9pZH06IHttZXNzYWdlfVwiKSJ9"
 width="100%"
></iframe>

Each class has a `send` method. Python duck typing means `notify_patron` works with any of them without modification: if an object has a `send` method with the right signature, it qualifies as a notifier.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWYgbm90aWZ5X3BhdHJvbihub3RpZmllciwgY29udGFjdCwgYm9va190aXRsZSk6XG4gICAgbm90aWZpZXIuc2VuZChjb250YWN0LCBmXCIne2Jvb2tfdGl0bGV9JyBpcyBub3cgYXZhaWxhYmxlLlwiKVxuXG5lbWFpbCA9IEVtYWlsTm90aWZpZXIoKVxuc21zID0gU01TTm90aWZpZXIoKVxuXG5ub3RpZnlfcGF0cm9uKGVtYWlsLCBcInBhdHJvbkBlbWFpbC5jb21cIiwgXCJEdW5lXCIpXG5ub3RpZnlfcGF0cm9uKHNtcywgXCIrOTEtOTk5OS0wMDAwMDBcIiwgXCJTaG9ndW5cIikifQ"
 width="100%"
></iframe>

This works perfectly, but there is a gap: Python does not enforce that every notifier *actually* has a `send` method. If Priya adds a `SlackNotifier` that accidentally names the method `notify` instead of `send`, no error appears until `notify_patron` tries to call `send` at runtime.

## Duck Typing and the "Trust the Contract" Model

Python's approach to abstraction relies on **duck typing**: if an object behaves like the thing you need (has the right methods and attributes), you can use it as that thing, regardless of its actual type. The name comes from "if it walks like a duck and quacks like a duck, it is a duck."

This gives Python great flexibility: any class can implement a `send` method and immediately work with `notify_patron`. There is no registration, no declaration, no import. The cost is that contracts are invisible: a developer reading the code has to infer what interface `notifier` must provide.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIFRoZSBpbnRlcmZhY2UgdGhhdCBhbnkgbm90aWZpZXIgbXVzdCBmdWxmaWxsOlxuIyAtIHNlbmQoY29udGFjdDogc3RyLCBtZXNzYWdlOiBzdHIpIC0-IE5vbmVcbiMgUHl0aG9uIGRvZXMgbm90IHdyaXRlIHRoaXMgZG93biBhbnl3aGVyZSB1bmxlc3MgeW91IHVzZSBhbiBBQkMgKG5leHQgbGVzc29uKSJ9"
 width="100%"
></iframe>

Abstract Base Classes, covered in the next lesson, bridge this gap by making the required interface explicit and enforced.

## Hiding Complexity Behind a Simple Interface

Abstraction is not only about polymorphism. It is also about hiding internal complexity that callers do not need to know about. A well-designed class exposes simple methods even when the implementation is complex.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBSZXNlcnZhdGlvbk1hbmFnZXI6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNhdGFsb2csIG5vdGlmaWVyKTpcbiAgICAgICAgc2VsZi5fY2F0YWxvZyA9IGNhdGFsb2dcbiAgICAgICAgc2VsZi5fbm90aWZpZXIgPSBub3RpZmllclxuICAgICAgICBzZWxmLl9xdWV1ZSA9IHt9ICAgICMgaXNibiAtPiBsaXN0IG9mIChwYXRyb24sIGNvbnRhY3QpXG5cbiAgICBkZWYgcmVzZXJ2ZShzZWxmLCBwYXRyb24sIGlzYm4sIGNvbnRhY3QpOlxuICAgICAgICBzZWxmLl9xdWV1ZS5zZXRkZWZhdWx0KGlzYm4sIFtdKS5hcHBlbmQoKHBhdHJvbiwgY29udGFjdCkpXG4gICAgICAgIHByaW50KGZcIlJlc2VydmVkICd7aXNibn0nIGZvciB7cGF0cm9ufVwiKVxuXG4gICAgZGVmIGZ1bGZpbGwoc2VsZiwgaXNibik6XG4gICAgICAgIGJvb2sgPSBzZWxmLl9jYXRhbG9nLmZpbmQoaXNibilcbiAgICAgICAgaWYgbm90IHNlbGYuX3F1ZXVlLmdldChpc2JuKTpcbiAgICAgICAgICAgIHJldHVyblxuICAgICAgICBwYXRyb24sIGNvbnRhY3QgPSBzZWxmLl9xdWV1ZVtpc2JuXS5wb3AoMClcbiAgICAgICAgc2VsZi5fbm90aWZpZXIuc2VuZChjb250YWN0LCBmXCIne2Jvb2sudGl0bGV9JyBpcyBhdmFpbGFibGUuXCIpXG4gICAgICAgIHByaW50KGZcIk5vdGlmaWVkIHtwYXRyb259XCIpIn0"
 width="100%"
></iframe>

The calling code only sees `reserve()` and `fulfill()`. The queue, the catalog lookup, the notification routing, all of that is hidden inside `ReservationManager`. Callers do not know it exists.

## Abstraction at a Glance

| Concept | What it means |
|---|---|
| Abstraction | Expose what an object does; hide how it does it |
| Concrete class | A specific implementation (EmailNotifier, SMSNotifier) |
| Abstract interface | The set of methods a category of objects must provide |
| Duck typing | Python accepts any object that has the required methods |
| The gap | Duck typing does not enforce the interface at class-definition time |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Fic3RyYWN0aW9uX2hpZGluZ19jb21wbGV4aXR5IGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJjbGFzcyBDU1ZFeHBvcnRlcjpcbiAgICBkZWYgZXhwb3J0KHNlbGYsIGRhdGEsIGZpbGVuYW1lKTpcbiAgICAgICAgd2l0aCBvcGVuKGZpbGVuYW1lLCBcIndcIikgYXMgZjpcbiAgICAgICAgICAgIGZvciByb3cgaW4gZGF0YTpcbiAgICAgICAgICAgICAgICBmLndyaXRlKFwiLFwiLmpvaW4oc3RyKHYpIGZvciB2IGluIHJvdykgKyBcIlxcblwiKVxuICAgICAgICBwcmludChmXCJFeHBvcnRlZCB0byB7ZmlsZW5hbWV9XCIpXG5cbmNsYXNzIEpTT05FeHBvcnRlcjpcbiAgICBkZWYgZXhwb3J0KHNlbGYsIGRhdGEsIGZpbGVuYW1lKTpcbiAgICAgICAgaW1wb3J0IGpzb25cbiAgICAgICAgd2l0aCBvcGVuKGZpbGVuYW1lLCBcIndcIikgYXMgZjpcbiAgICAgICAgICAgIGpzb24uZHVtcChkYXRhLCBmLCBpbmRlbnQ9MilcbiAgICAgICAgcHJpbnQoZlwiRXhwb3J0ZWQgdG8ge2ZpbGVuYW1lfVwiKVxuXG5kZWYgZXhwb3J0X3JlcG9ydChleHBvcnRlciwgcm93cywgcGF0aCk6XG4gICAgZXhwb3J0ZXIuZXhwb3J0KHJvd3MsIHBhdGgpIn0"
 width="100%"
></iframe>

Call `export_report` once with a `CSVExporter` and once with a `JSONExporter` using a small data set. Then write a `PrintExporter` that implements `export` by printing data to the console instead of writing a file. Confirm `export_report` works with it without any changes to `export_report` itself.

## Conclusion

Abstraction means designing objects so that callers interact with a simple, stable interface without knowing or caring about the internal implementation. Python's duck typing supports this naturally: any object with the right methods qualifies, regardless of its class. The practical limitation is that the interface is informal and not enforced. The next lesson introduces Abstract Base Classes, which make the interface formal, document it clearly, and cause Python to raise an error at class-definition time if a required method is missing.

## Introduction

Three months into the project, Priya has four different notifier classes: `EmailNotifier`, `SMSNotifier`, `PushNotifier`, and a `SlackNotifier` a colleague added last week. The `SlackNotifier` works perfectly in isolation. It crashes in production because the colleague named the method `notify` instead of `send`. The bug was not caught until a patron tried to make a reservation.

Priya wants Python to tell her at class-definition time if a notifier is missing the method the rest of the system expects. She does not want to wait until runtime to discover the omission. Python's `abc` module (Abstract Base Classes) exists precisely for this situation.

![](images/06_abstract_base_classes.png)

## What an Abstract Base Class Is

An **Abstract Base Class** (ABC) is a class that defines an interface without providing implementations for all of it. It declares which methods every concrete subclass *must* define, and Python raises a `TypeError` if you try to instantiate a subclass that forgot one.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZnJvbSBhYmMgaW1wb3J0IEFCQywgYWJzdHJhY3RtZXRob2RcblxuY2xhc3MgTm90aWZpZXIoQUJDKTpcbiAgICBAYWJzdHJhY3RtZXRob2RcbiAgICBkZWYgc2VuZChzZWxmLCBjb250YWN0LCBtZXNzYWdlKTpcbiAgICAgICAgXCJcIlwiU2VuZCBhIG5vdGlmaWNhdGlvbiB0byB0aGUgZ2l2ZW4gY29udGFjdCB3aXRoIHRoZSBnaXZlbiBtZXNzYWdlLlwiXCJcIiJ9"
 width="100%"
></iframe>

`ABC` is a convenience base class from Python's `abc` module. `@abstractmethod` marks a method that every subclass must implement. The docstring in the abstract method acts as a specification: it tells future developers what any implementation must do.

## Concrete Subclasses Must Implement Every Abstract Method

A class that inherits from `Notifier` and fails to implement `send` cannot be instantiated. Python catches this at instantiation time, not at call time, which is a major improvement over duck typing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgRW1haWxOb3RpZmllcihOb3RpZmllcik6XG4gICAgZGVmIHNlbmQoc2VsZiwgY29udGFjdCwgbWVzc2FnZSk6XG4gICAgICAgIHByaW50KGZcIkVtYWlsIHRvIHtjb250YWN0fToge21lc3NhZ2V9XCIpXG5cbmNsYXNzIEJyb2tlbk5vdGlmaWVyKE5vdGlmaWVyKTpcbiAgICBwYXNzICAgICMgZm9yZ290IHRvIGltcGxlbWVudCBzZW5kXG5cbmVtYWlsID0gRW1haWxOb3RpZmllcigpICAgICMgZmluZVxuZW1haWwuc2VuZChcImFAYi5jb21cIiwgXCJCb29rIGF2YWlsYWJsZVwiKSAgICMgRW1haWwgdG8gYUBiLmNvbTogQm9vayBhdmFpbGFibGVcblxuYnJva2VuID0gQnJva2VuTm90aWZpZXIoKSAgIyBlcnJvciEgVHlwZUVycm9yOiBDYW4ndCBpbnN0YW50aWF0ZSBhYnN0cmFjdCBjbGFzcyBCcm9rZW5Ob3RpZmllclxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgd2l0aG91dCBhbiBpbXBsZW1lbnRhdGlvbiBmb3IgYWJzdHJhY3QgbWV0aG9kICdzZW5kJyJ9"
 width="100%"
></iframe>

The error message names the missing method explicitly. Priya would have caught the `SlackNotifier` bug the moment it was first instantiated in a test, not in production.

## Abstract Classes Can Have Concrete Methods Too

Abstract base classes are not required to be purely abstract. They can include concrete methods that all subclasses inherit, providing default behavior alongside the required interface.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZnJvbSBhYmMgaW1wb3J0IEFCQywgYWJzdHJhY3RtZXRob2RcblxuY2xhc3MgTm90aWZpZXIoQUJDKTpcbiAgICBkZWYgc2VuZF9iYXRjaChzZWxmLCBjb250YWN0cywgbWVzc2FnZSk6XG4gICAgICAgIGZvciBjb250YWN0IGluIGNvbnRhY3RzOlxuICAgICAgICAgICAgc2VsZi5zZW5kKGNvbnRhY3QsIG1lc3NhZ2UpICAgICMgZGVsZWdhdGVzIHRvIHRoZSBhYnN0cmFjdCBtZXRob2RcblxuICAgIEBhYnN0cmFjdG1ldGhvZFxuICAgIGRlZiBzZW5kKHNlbGYsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgICAgICBcIlwiXCJTZW5kIGEgc2luZ2xlIG5vdGlmaWNhdGlvbi5cIlwiXCJcblxuY2xhc3MgU01TTm90aWZpZXIoTm90aWZpZXIpOlxuICAgIGRlZiBzZW5kKHNlbGYsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgICAgICBwcmludChmXCJTTVMgdG8ge2NvbnRhY3R9OiB7bWVzc2FnZX1cIilcblxuc21zID0gU01TTm90aWZpZXIoKVxuc21zLnNlbmRfYmF0Y2goW1wiKzkxLTk5OVwiLCBcIis5MS04ODhcIl0sIFwiQm9vayBhdmFpbGFibGVcIilcbiMgU01TIHRvICs5MS05OTk6IEJvb2sgYXZhaWxhYmxlXG4jIFNNUyB0byArOTEtODg4OiBCb29rIGF2YWlsYWJsZSJ9"
 width="100%"
></iframe>

`send_batch` is a concrete method defined on the abstract class. It works correctly for every concrete subclass, regardless of how `send` is implemented, because it delegates to `self.send()`. This is the **template method pattern**: the abstract class defines the structure, concrete subclasses fill in the variable part.

## Abstract Properties

You can also mark properties as abstract, requiring subclasses to provide a value or computation for an attribute:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZnJvbSBhYmMgaW1wb3J0IEFCQywgYWJzdHJhY3RtZXRob2RcblxuY2xhc3MgTGlicmFyeUl0ZW0oQUJDKTpcbiAgICBAcHJvcGVydHlcbiAgICBAYWJzdHJhY3RtZXRob2RcbiAgICBkZWYgZGlzcGxheV90aXRsZShzZWxmKTpcbiAgICAgICAgXCJcIlwiVGhlIHRpdGxlIGFzIGl0IHNob3VsZCBhcHBlYXIgaW4gdGhlIGNhdGFsb2cuXCJcIlwiXG5cbmNsYXNzIFBoeXNpY2FsQm9vayhMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBlZGl0aW9uKTpcbiAgICAgICAgc2VsZi5fdGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmVkaXRpb24gPSBlZGl0aW9uXG5cbiAgICBAcHJvcGVydHlcbiAgICBkZWYgZGlzcGxheV90aXRsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIntzZWxmLl90aXRsZX0gKEVkLiB7c2VsZi5lZGl0aW9ufSlcIlxuXG5iID0gUGh5c2ljYWxCb29rKFwiRHVuZVwiLCAzKVxucHJpbnQoYi5kaXNwbGF5X3RpdGxlKSAgICMgRHVuZSAoRWQuIDMpIn0"
 width="100%"
></iframe>

## isinstance() With Abstract Classes

A useful side effect of ABCs: `isinstance()` works correctly across the whole hierarchy, regardless of which concrete class you are holding.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZW1haWwgPSBFbWFpbE5vdGlmaWVyKClcbnNtcyA9IFNNU05vdGlmaWVyKClcblxucHJpbnQoaXNpbnN0YW5jZShlbWFpbCwgTm90aWZpZXIpKSAgICMgVHJ1ZVxucHJpbnQoaXNpbnN0YW5jZShzbXMsIE5vdGlmaWVyKSkgICAgICMgVHJ1ZVxuXG5kZWYgbm90aWZ5X2FsbChub3RpZmllcnMsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgIGZvciBuIGluIG5vdGlmaWVyczpcbiAgICAgICAgaWYgbm90IGlzaW5zdGFuY2UobiwgTm90aWZpZXIpOlxuICAgICAgICAgICAgcmFpc2UgVHlwZUVycm9yKGZcIkV4cGVjdGVkIGEgTm90aWZpZXIsIGdvdCB7dHlwZShuKS5fX25hbWVfX31cIilcbiAgICAgICAgbi5zZW5kKGNvbnRhY3QsIG1lc3NhZ2UpIn0"
 width="100%"
></iframe>

The ABC becomes a single, authoritative check: anything that claims to be a `Notifier` must have implemented `send`.

## Abstract Base Classes at a Glance

| Concept | What it does |
|---|---|
| `class X(ABC)` | Declares X as an abstract base class |
| `@abstractmethod` | Marks a method that every subclass must implement |
| Concrete subclass | A subclass that implements all abstract methods |
| Instantiation error | Python raises `TypeError` if a required method is missing |
| Concrete methods on ABC | Inherited by all subclasses; can call abstract methods via `self` |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2Fic3RyYWN0X2Jhc2VfY2xhc3NlcyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZnJvbSBhYmMgaW1wb3J0IEFCQywgYWJzdHJhY3RtZXRob2RcblxuY2xhc3MgRXhwb3J0ZXIoQUJDKTpcbiAgICBAYWJzdHJhY3RtZXRob2RcbiAgICBkZWYgZXhwb3J0KHNlbGYsIGRhdGEsIGZpbGVuYW1lKTpcbiAgICAgICAgXCJcIlwiV3JpdGUgZGF0YSB0byBmaWxlbmFtZSBpbiB0aGUgYXBwcm9wcmlhdGUgZm9ybWF0LlwiXCJcIlxuXG4gICAgZGVmIGV4cG9ydF93aXRoX2hlYWRlcihzZWxmLCBoZWFkZXIsIGRhdGEsIGZpbGVuYW1lKTpcbiAgICAgICAgc2VsZi5leHBvcnQoW2hlYWRlcl0gKyBkYXRhLCBmaWxlbmFtZSkifQ"
 width="100%"
></iframe>

Write a `CSVExporter` and a `JSONExporter` that both inherit from `Exporter` and implement `export`. Then try to instantiate `Exporter` directly and observe the `TypeError`. Finally, write an `IncompleteExporter(Exporter): pass` and confirm Python refuses to let you create one.

## Conclusion

Abstract Base Classes define a formal interface that concrete subclasses are required to implement, with Python raising a `TypeError` at instantiation time rather than at call time if a method is missing. They can include concrete methods that delegate to the abstract ones, and `isinstance()` checks work cleanly across the entire hierarchy. The final lesson of this unit brings encapsulation and abstraction together into a practical design exercise, showing how clean interfaces are designed for a real system.

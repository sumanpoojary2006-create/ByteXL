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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-001-a2277ab9e7.html"
 width="100%"
></iframe>

For this to work, every `notifier` object must guarantee it has a `send` method that accepts a contact address and a message. Abstraction is the design pattern; the next lesson shows the Python mechanism for enforcing it.

## Designing for Abstraction: Concrete vs. Abstract

The idea of a "notifier" is abstract: it represents a category of things that can send messages, without specifying which particular channel is used. Specific implementations (email, SMS) are concrete.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-002-00e30765ce.html"
 width="100%"
></iframe>

Each class has a `send` method. Python duck typing means `notify_patron` works with any of them without modification: if an object has a `send` method with the right signature, it qualifies as a notifier.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-003-87cc47536a.html"
 width="100%"
></iframe>

This works perfectly, but there is a gap: Python does not enforce that every notifier *actually* has a `send` method. If Priya adds a `SlackNotifier` that accidentally names the method `notify` instead of `send`, no error appears until `notify_patron` tries to call `send` at runtime.

## Duck Typing and the "Trust the Contract" Model

Python's approach to abstraction relies on **duck typing**: if an object behaves like the thing you need (has the right methods and attributes), you can use it as that thing, regardless of its actual type. The name comes from "if it walks like a duck and quacks like a duck, it is a duck."

This gives Python great flexibility: any class can implement a `send` method and immediately work with `notify_patron`. There is no registration, no declaration, no import. The cost is that contracts are invisible: a developer reading the code has to infer what interface `notifier` must provide.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-004-988b8062ff.html"
 width="100%"
></iframe>

Abstract Base Classes, covered in the next lesson, bridge this gap by making the required interface explicit and enforced.

## Hiding Complexity Behind a Simple Interface

Abstraction is not only about polymorphism. It is also about hiding internal complexity that callers do not need to know about. A well-designed class exposes simple methods even when the implementation is complex.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-005-b8ea9e7587.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-05-abstraction-hiding-complexi-006-a2017a9048.html"
 width="100%"
></iframe>

Call `export_report` once with a `CSVExporter` and once with a `JSONExporter` using a small data set. Then write a `PrintExporter` that implements `export` by printing data to the console instead of writing a file. Confirm `export_report` works with it without any changes to `export_report` itself.

## Conclusion

Abstraction means designing objects so that callers interact with a simple, stable interface without knowing or caring about the internal implementation. Python's duck typing supports this naturally: any object with the right methods qualifies, regardless of its class. The practical limitation is that the interface is informal and not enforced. The next lesson introduces Abstract Base Classes, which make the interface formal, document it clearly, and cause Python to raise an error at class-definition time if a required method is missing.

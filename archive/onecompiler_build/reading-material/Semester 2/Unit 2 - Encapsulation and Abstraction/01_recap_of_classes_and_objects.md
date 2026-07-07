## Introduction

Priya is proud of the `Book` class she wrote last semester. It stores a title, an ISBN, and a copy count. It even has a `__repr__`. But two weeks after she joined the library management team, a colleague edits a book's `copies` attribute directly and sets it to `-5`. There is no error. The system merrily reports that there are negative copies of a book on the shelf, and a reservation made against that "stock" sends an automated email to a patron telling them a book is available when it is not.

The class works. The objects are wrong. Priya realizes the problem: her class is a container with no guard on the door. This unit is about building the guard. Before doing that, a brief review of what you already know about classes is worth taking, because everything in this unit grows directly from that foundation.

![](images/01_classes_and_objects_recap.png)

## A Class Is a Blueprint; an Object Is a Built Thing

A class definition describes what data an object will hold (attributes) and what operations it supports (methods). Every time you call the class like a function, Python creates a new independent object from that blueprint.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlY2FwX29mX2NsYXNzZXNfYW5kX29iamVjdHMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuICAgICAgICBzZWxmLmNvcGllcyA9IGNvcGllc1xuXG4gICAgZGVmIGlzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuY29waWVzID4gMFxuXG4gICAgZGVmIF9fcmVwcl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gZlwiQm9vayh7c2VsZi50aXRsZSFyfSwgY29waWVzPXtzZWxmLmNvcGllc30pXCJcblxuYjEgPSBCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDMpXG5iMiA9IEJvb2soXCJTaG9ndW5cIiwgXCI5NzgtMDM4NTI5MTY3NVwiLCAxKVxuXG5wcmludChiMS5pc19hdmFpbGFibGUoKSkgICAjIFRydWVcbnByaW50KGIyKSAgICAgICAgICAgICAgICAgICMgQm9vaygnU2hvZ3VuJywgY29waWVzPTEpIn0"
 width="100%"
></iframe>

`b1` and `b2` are independent objects. Changing `b1.copies` does not affect `b2`. Each holds its own data, and both share the same method definitions.

## Instance Attributes, Class Attributes, and the Difference

Attributes set on `self` in `__init__` are **instance attributes**: each object gets its own copy. Attributes set directly on the class body are **class attributes**: all instances share one copy.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlY2FwX29mX2NsYXNzZXNfYW5kX29iamVjdHMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgbGlicmFyeV9uYW1lID0gXCJDaXR5IENlbnRyYWwgTGlicmFyeVwiICAgIyBjbGFzcyBhdHRyaWJ1dGU6IHNoYXJlZFxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGUgICAgICAgIyBpbnN0YW5jZSBhdHRyaWJ1dGU6IHBlci1vYmplY3RcbiAgICAgICAgc2VsZi5jb3BpZXMgPSBjb3BpZXMgICAgICMgaW5zdGFuY2UgYXR0cmlidXRlOiBwZXItb2JqZWN0XG5cbmIgPSBCb29rKFwiRHVuZVwiLCAzKVxucHJpbnQoYi5saWJyYXJ5X25hbWUpICAgICAgICAgICMgQ2l0eSBDZW50cmFsIExpYnJhcnkgKHJlYWQgZnJvbSB0aGUgY2xhc3MpXG5wcmludChCb29rLmxpYnJhcnlfbmFtZSkgICAgICAgIyBDaXR5IENlbnRyYWwgTGlicmFyeSAoZGlyZWN0IGNsYXNzIGFjY2VzcylcblxuQm9vay5saWJyYXJ5X25hbWUgPSBcIldlc3RzaWRlIEJyYW5jaFwiICAgIyBjaGFuZ2UgYWZmZWN0cyBhbGwgaW5zdGFuY2VzXG5wcmludChiLmxpYnJhcnlfbmFtZSkgICAgICAgICAgIyBXZXN0c2lkZSBCcmFuY2gifQ"
 width="100%"
></iframe>

Class attributes are useful for constants and counters shared across all instances, but be careful: mutating a class attribute changes it for every object, which is either exactly what you want or a very confusing bug.

## Methods Are Just Functions That Receive the Object

Every method receives `self` as its first argument, which is the instance the method was called on. Python passes it automatically; you never provide it when calling.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlY2FwX29mX2NsYXNzZXNfYW5kX29iamVjdHMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5jb3BpZXMgPSBjb3BpZXNcblxuICAgIGRlZiBjaGVja19vdXQoc2VsZik6XG4gICAgICAgIGlmIHNlbGYuY29waWVzIDwgMTpcbiAgICAgICAgICAgIHByaW50KFwiTm8gY29waWVzIGF2YWlsYWJsZVwiKVxuICAgICAgICAgICAgcmV0dXJuXG4gICAgICAgIHNlbGYuY29waWVzIC09IDFcbiAgICAgICAgcHJpbnQoZlwiQ2hlY2tlZCBvdXQgJ3tzZWxmLnRpdGxlfScuIFJlbWFpbmluZzoge3NlbGYuY29waWVzfVwiKVxuXG5iID0gQm9vayhcIkR1bmVcIiwgMilcbmIuY2hlY2tfb3V0KCkgICAjIENoZWNrZWQgb3V0ICdEdW5lJy4gUmVtYWluaW5nOiAxXG5iLmNoZWNrX291dCgpICAgIyBDaGVja2VkIG91dCAnRHVuZScuIFJlbWFpbmluZzogMFxuYi5jaGVja19vdXQoKSAgICMgTm8gY29waWVzIGF2YWlsYWJsZSJ9"
 width="100%"
></iframe>

`check_out` modifies `self.copies`, so each call on the same object sees the updated state. This is the core of what makes objects useful: state that persists between calls.

## The Problem with Open State

The `Book` class above has a subtle weakness: nothing prevents code outside the class from writing directly to `self.copies`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlY2FwX29mX2NsYXNzZXNfYW5kX29iamVjdHMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImIgPSBCb29rKFwiRHVuZVwiLCAyKVxuYi5jaGVja19vdXQoKVxuYi5jb3BpZXMgPSAtNSAgICMgbm8gZXJyb3IsIG5vIHdhcm5pbmdcbnByaW50KGIuY29waWVzKSAjIC01In0"
 width="100%"
></iframe>

The `check_out` method has logic to prevent negative copies, but that logic can be bypassed completely by anyone who knows the attribute name. In a small codebase with one developer, this is manageable. In a team or a system with thousands of calls, it is a ticking bug.

## Classes and Objects at a Glance

| Concept | Syntax | What it does |
|---|---|---|
| Class attribute | Defined in class body, outside `__init__` | Shared across all instances |
| Instance attribute | Set on `self` in `__init__` | Unique to each object |
| Method | Function defined in class body, takes `self` | Operates on the instance's data |
| `__init__` | Called automatically by Python when you create an object | Sets up initial state |
| `__repr__` | Called by `repr()` and the REPL | Returns a developer-readable string |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlY2FwX29mX2NsYXNzZXNfYW5kX29iamVjdHMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIExpYnJhcnlDYXJkOlxuICAgIHRvdGFsX2lzc3VlZCA9IDAgICAjIHRyYWNrIGFjcm9zcyBhbGwgY2FyZHNcblxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBob2xkZXJfbmFtZSk6XG4gICAgICAgIHNlbGYuaG9sZGVyX25hbWUgPSBob2xkZXJfbmFtZVxuICAgICAgICBzZWxmLmJvb2tzX2JvcnJvd2VkID0gW11cbiAgICAgICAgTGlicmFyeUNhcmQudG90YWxfaXNzdWVkICs9IDFcblxuICAgIGRlZiBib3Jyb3coc2VsZiwgYm9va190aXRsZSk6XG4gICAgICAgIHNlbGYuYm9va3NfYm9ycm93ZWQuYXBwZW5kKGJvb2tfdGl0bGUpXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJMaWJyYXJ5Q2FyZCh7c2VsZi5ob2xkZXJfbmFtZSFyfSwgYm9ycm93ZWQ9e2xlbihzZWxmLmJvb2tzX2JvcnJvd2VkKX0pXCIifQ"
 width="100%"
></iframe>

Create two `LibraryCard` objects, borrow one book on each, then print `LibraryCard.total_issued`. Confirm it is `2`. Now explain why `total_issued` counts correctly across both instances even though neither instance sets it on `self`.

## Conclusion

A class defines attributes and methods; an object holds its own copy of the instance attributes and shares method definitions with all other instances of the same class. The `check_out` method illustrated a real problem: an object's internal state can be modified from outside the class, bypassing any logic the class has in place to keep it valid. The next lesson gives this problem a name, **encapsulation**, and shows the techniques Python provides to address it.

## Introduction

Priya keeps writing the same little calculation by hand outside her `Student` objects: comparing `marks` to 40 to decide pass or fail, for every single student, every time. A real student does not just passively hold a mark; in a sense, a student "knows" whether they have passed, and Priya would like to simply ask the object that question directly, the way you would ask a real person, rather than recomputing it herself from outside every time.

A **method** is a function defined inside a class, an action that belongs to its objects and can use their attributes directly. This lesson introduces methods, and the special first parameter, `self`, that every method needs in order to know exactly which object it is working on.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/05_method_asks_object_directly.png)

## Defining a Method Inside a Class

A method is written exactly like a function, with `def`, indented one level inside the class body.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY2xhc3MgU3R1ZGVudDpcbiAgICBkZWYgZ3JlZXQoc2VsZik6XG4gICAgICAgIHByaW50KFwiSGVsbG8sIEkgYW0gYSBzdHVkZW50LlwiKVxuXG5hc2hhID0gU3R1ZGVudCgpXG5hc2hhLmdyZWV0KCkgICAgIyBIZWxsbywgSSBhbSBhIHN0dWRlbnQuIn0"
 width="100%"
></iframe>

Calling `asha.greet()` looks just like calling any method you have used before, `"text".upper()` or `my_list.append(...)`, because that is exactly what a method call always was: dot notation reaching an action that belongs to the object on the left of the dot.

## The self Parameter: Which Object Is This?

Every method needs a first parameter, conventionally named `self`, which automatically refers to the specific object the method was called on. You never pass it yourself; Python supplies it automatically the moment you write `asha.greet()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgU3R1ZGVudDpcbiAgICBkZWYgZ3JlZXQoc2VsZik6XG4gICAgICAgIHByaW50KGZcIkhlbGxvLCBJIGFtIHtzZWxmLm5hbWV9LlwiKVxuXG5hc2hhID0gU3R1ZGVudCgpXG5hc2hhLm5hbWUgPSBcIkFzaGFcIlxuYXNoYS5ncmVldCgpICAgICMgSGVsbG8sIEkgYW0gQXNoYS5cblxucmF2aSA9IFN0dWRlbnQoKVxucmF2aS5uYW1lID0gXCJSYXZpXCJcbnJhdmkuZ3JlZXQoKSAgICAjIEhlbGxvLCBJIGFtIFJhdmkuIn0"
 width="100%"
></iframe>

The very same method, written once, prints a different name depending on which object called it, because `self` inside `greet` automatically refers to whichever object sits before the dot at the call site: `asha` in the first call, `ravi` in the second.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/05_self_routes_to_object.png)


## What Happens If You Forget self

Leaving `self` out of a method's definition causes a confusing error the moment that method is actually called on an object, because Python always supplies the calling object as the first argument, whether the method asked for it or not.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiY2xhc3MgU3R1ZGVudDpcbiAgICBkZWYgZ3JlZXQoKTogICAgICAgICAgICAgICAjIG1pc3Npbmcgc2VsZiFcbiAgICAgICAgcHJpbnQoXCJIZWxsbyFcIilcblxuYXNoYSA9IFN0dWRlbnQoKVxuYXNoYS5ncmVldCgpICAgICMgZXJyb3IhIn0"
 width="100%"
></iframe>

This raises a `TypeError` complaining that `greet()` takes 0 positional arguments but 1 was given, because Python quietly passed `asha` itself as an argument, and `greet` had no parameter ready to receive it. Every method you write needs `self` as its first parameter, with no exceptions, even if that particular method never ends up using it.

## A Method Using self to Read and Reason

Now Priya can finally write the "have I passed" logic directly on the object, using `self` to reach its own attributes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiY2xhc3MgU3R1ZGVudDpcbiAgICBkZWYgaGFzX3Bhc3NlZChzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYubWFya3MgPj0gNDBcblxuYXNoYSA9IFN0dWRlbnQoKVxuYXNoYS5tYXJrcyA9IDcyXG5wcmludChhc2hhLmhhc19wYXNzZWQoKSkgICAgIyBUcnVlXG5cbnJhdmkgPSBTdHVkZW50KClcbnJhdmkubWFya3MgPSAzMFxucHJpbnQocmF2aS5oYXNfcGFzc2VkKCkpICAgICMgRmFsc2UifQ"
 width="100%"
></iframe>

`self.marks` reaches whichever object's `marks` attribute is relevant to that particular call, exactly the same way `self.name` did in the `greet` example. The method's logic is written once, on the class, and it correctly judges every object built from that class using that object's own data.

## Calling One Method From Another

Methods on the same object can call each other through `self`, exactly the way ordinary functions can call each other.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY2xhc3MgU3R1ZGVudDpcbiAgICBkZWYgaGFzX3Bhc3NlZChzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYubWFya3MgPj0gNDBcblxuICAgIGRlZiByZXBvcnQoc2VsZik6XG4gICAgICAgIHJlc3VsdCA9IFwiUGFzc1wiIGlmIHNlbGYuaGFzX3Bhc3NlZCgpIGVsc2UgXCJGYWlsXCJcbiAgICAgICAgcHJpbnQoZlwie3NlbGYubmFtZX06IHtyZXN1bHR9XCIpXG5cbmFzaGEgPSBTdHVkZW50KClcbmFzaGEubmFtZSA9IFwiQXNoYVwiXG5hc2hhLm1hcmtzID0gNzJcbmFzaGEucmVwb3J0KCkgICAgIyBBc2hhOiBQYXNzIn0"
 width="100%"
></iframe>

`report` reaches `has_passed` through `self.has_passed()`, exactly the dot-notation pattern used everywhere else, because one method calling another belonging to the same object is still just calling a method on `self`.

## Methods and self at a Glance

| Idea | Detail |
|---|---|
| A method | A function defined inside a class, indented in its body |
| The first parameter | Always `self`, supplied automatically by Python |
| What `self` refers to | Whichever object the method was actually called on |
| Calling it | `object.method()`, never passing `self` manually |

## Your Turn: A Method That Reasons About the Object

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21ldGhvZHNfYW5kX3RoZV9zZWxmX3BhcmFtZXRlciBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiY2xhc3MgQmFua0FjY291bnQ6XG4gICAgZGVmIGNhbl93aXRoZHJhdyhzZWxmLCBhbW91bnQpOlxuICAgICAgICByZXR1cm4gYW1vdW50IDw9IHNlbGYuYmFsYW5jZVxuXG5hY2MgPSBCYW5rQWNjb3VudCgpXG5hY2MuYmFsYW5jZSA9IDMwMDBcblxucHJpbnQoYWNjLmNhbl93aXRoZHJhdygyMDAwKSkgICAgIyBUcnVlXG5wcmludChhY2MuY2FuX3dpdGhkcmF3KDUwMDApKSAgICAjIEZhbHNlIn0"
 width="100%"
></iframe>

Notice `can_withdraw` takes a second parameter, `amount`, alongside the required `self`, exactly the way an ordinary function can take more than one parameter; `self` simply always comes first.

## Conclusion

A method is a function defined inside a class, and its first parameter, always named `self` by convention, automatically refers to whichever object the method was called on, letting the same method's logic correctly use each object's own attributes. Forgetting `self` causes a `TypeError` the moment the method is actually called, because Python always supplies the calling object as an argument regardless. With data and behaviour finally living together on the same object, the next lesson removes the last fragile part of this picture: setting up an object's attributes by hand, one at a time, after it is created.

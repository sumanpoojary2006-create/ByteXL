## Introduction

Priya has been creating a `Student` object and then immediately writing three or four separate lines to attach a name, a roll number, and marks, every single time, for every single student. Forget one of those lines, even once, and that student object is left with a missing attribute, ready to raise an `AttributeError` the moment anything tries to read it. She wants every `Student` to arrive already complete, with all of its required attributes set the instant it is created, with no separate setup step she might forget.

Python's answer is the **`__init__` constructor**, a special method that runs automatically the moment an object is instantiated, exactly the right place to guarantee every object starts out fully formed.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_builds_complete_object.png)

## The __init__ Method Runs Automatically

Define a method named `__init__` inside a class, and Python calls it automatically every time that class is instantiated, immediately after the object is created.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBTdHVkZW50OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgcHJpbnQoXCJBIG5ldyBzdHVkZW50IG9iamVjdCB3YXMganVzdCBjcmVhdGVkLlwiKVxuXG5hc2hhID0gU3R1ZGVudCgpICAgICMgQSBuZXcgc3R1ZGVudCBvYmplY3Qgd2FzIGp1c3QgY3JlYXRlZC4ifQ"
 width="100%"
></iframe>

Notice nobody explicitly called `__init__`; writing `Student()` triggered it on its own. The double underscores on either side of the name are Python's signal that this method has a special, built-in role, rather than being an ordinary method you invented yourself.

## Accepting Values and Setting Attributes

`__init__` can take parameters beyond `self`, exactly like any other method, and the values passed in when the object is created flow straight into it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBTdHVkZW50OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCByb2xsX251bWJlciwgbWFya3MpOlxuICAgICAgICBzZWxmLm5hbWUgPSBuYW1lXG4gICAgICAgIHNlbGYucm9sbF9udW1iZXIgPSByb2xsX251bWJlclxuICAgICAgICBzZWxmLm1hcmtzID0gbWFya3NcblxuYXNoYSA9IFN0dWRlbnQoXCJBc2hhXCIsIDEwMSwgNzIpXG5wcmludChhc2hhLm5hbWUsIGFzaGEucm9sbF9udW1iZXIsIGFzaGEubWFya3MpICAgICMgQXNoYSAxMDEgNzIifQ"
 width="100%"
></iframe>

Read each line inside `__init__` carefully: `self.name = name` takes the `name` argument that was just passed in, and stores it as an attribute on this specific object. Now every `Student` is guaranteed to have a `name`, a `roll_number`, and `marks` the instant it exists, because there is no way to call `Student(...)` without supplying all three.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_auto_setup.png)


## Required Arguments at Creation Time

Leave out a required argument, and Python refuses to create the object at all, exactly the protection Priya was missing before.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJyYXZpID0gU3R1ZGVudChcIlJhdmlcIiwgMTAyKSAgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

This raises a `TypeError` complaining that `__init__` is missing the required `marks` argument, caught immediately at creation time rather than silently producing a broken object that fails later, possibly far away from where the mistake actually happened.

## Combining __init__ With Other Methods

`__init__` sets attributes up once; your other methods, exactly as in the previous lesson, can then use `self` to read and reason about them.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBTdHVkZW50OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCByb2xsX251bWJlciwgbWFya3MpOlxuICAgICAgICBzZWxmLm5hbWUgPSBuYW1lXG4gICAgICAgIHNlbGYucm9sbF9udW1iZXIgPSByb2xsX251bWJlclxuICAgICAgICBzZWxmLm1hcmtzID0gbWFya3NcblxuICAgIGRlZiBoYXNfcGFzc2VkKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5tYXJrcyA-PSA0MFxuXG4gICAgZGVmIHJlcG9ydChzZWxmKTpcbiAgICAgICAgcmVzdWx0ID0gXCJQYXNzXCIgaWYgc2VsZi5oYXNfcGFzc2VkKCkgZWxzZSBcIkZhaWxcIlxuICAgICAgICBwcmludChmXCJ7c2VsZi5uYW1lfSAoUm9sbCB7c2VsZi5yb2xsX251bWJlcn0pOiB7cmVzdWx0fVwiKVxuXG5hc2hhID0gU3R1ZGVudChcIkFzaGFcIiwgMTAxLCA3MilcbnJhdmkgPSBTdHVkZW50KFwiUmF2aVwiLCAxMDIsIDMwKVxuXG5hc2hhLnJlcG9ydCgpICAgICMgQXNoYSAoUm9sbCAxMDEpOiBQYXNzXG5yYXZpLnJlcG9ydCgpICAgICMgUmF2aSAoUm9sbCAxMDIpOiBGYWlsIn0"
 width="100%"
></iframe>

Both objects were complete and ready to use the moment they were created, with no separate setup lines anywhere, and `report` works correctly on each, exactly because `__init__` guaranteed every attribute it needs was already there.

## Default Values Inside __init__

A constructor's parameters can carry default values too, exactly like any function parameter from the functions unit, making some setup details optional.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBTdHVkZW50OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCByb2xsX251bWJlciwgbWFya3M9MCk6XG4gICAgICAgIHNlbGYubmFtZSA9IG5hbWVcbiAgICAgICAgc2VsZi5yb2xsX251bWJlciA9IHJvbGxfbnVtYmVyXG4gICAgICAgIHNlbGYubWFya3MgPSBtYXJrc1xuXG5uZXdfYWRtaXNzaW9uID0gU3R1ZGVudChcIk1lZXJhXCIsIDEwMylcbnByaW50KG5ld19hZG1pc3Npb24ubWFya3MpICAgICMgMCwgbm8gbWFya3MgZW50ZXJlZCB5ZXQifQ"
 width="100%"
></iframe>

## __init__ at a Glance

| Idea | Detail |
|---|---|
| What it is | A special method named `__init__`, with double underscores on each side |
| When it runs | Automatically, the moment an object is instantiated |
| What it is for | Setting up an object's attributes so it starts complete |
| Required arguments | Missing one raises a `TypeError` immediately, at creation |

## Your Turn: A Complete BankAccount From the Start

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3RoZV9pbml0X2NvbnN0cnVjdG9yIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJjbGFzcyBCYW5rQWNjb3VudDpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgaG9sZGVyLCBiYWxhbmNlPTApOlxuICAgICAgICBzZWxmLmhvbGRlciA9IGhvbGRlclxuICAgICAgICBzZWxmLmJhbGFuY2UgPSBiYWxhbmNlXG5cbiAgICBkZWYgZGVwb3NpdChzZWxmLCBhbW91bnQpOlxuICAgICAgICBzZWxmLmJhbGFuY2UgPSBzZWxmLmJhbGFuY2UgKyBhbW91bnRcblxuICAgIGRlZiBjYW5fd2l0aGRyYXcoc2VsZiwgYW1vdW50KTpcbiAgICAgICAgcmV0dXJuIGFtb3VudCA8PSBzZWxmLmJhbGFuY2VcblxuYWNjID0gQmFua0FjY291bnQoXCJBc2hhXCIsIDEwMDApXG5hY2MuZGVwb3NpdCg1MDApXG5wcmludChhY2MuaG9sZGVyLCBhY2MuYmFsYW5jZSkgICAgICAgICAjIEFzaGEgMTUwMFxucHJpbnQoYWNjLmNhbl93aXRoZHJhdygyMDAwKSkgICAgICAgICAgICMgRmFsc2UifQ"
 width="100%"
></iframe>

Every account this class produces starts complete, with a holder and a balance guaranteed from the very first line after creation.

## Conclusion

`__init__` is a special method that Python calls automatically the moment an object is instantiated, and setting attributes inside it, using `self.attribute = value`, guarantees every object starts fully formed, with required arguments enforced immediately rather than discovered later as a missing-attribute crash. Default values inside `__init__` work exactly like default parameters on any function. With objects now arriving complete and capable, the next lesson walks through two full, realistic classes from start to finish: a Student and a BankAccount.

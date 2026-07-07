## Introduction

At the end of Asel's first week, Rahul shows her something that surprises her. He writes a custom class, and then uses `len()` on it, adds two instances together with `+`, and loops over it with `for`. None of these behaviors are methods she wrote; they just work. When she asks how, he says: "Because everything in Python follows a contract. Your class tells Python how to behave in each situation by defining special methods. The `for` loop does not care what your object is; it just calls a specific method on it."

That contract is called the **Python data model**, and the special methods that implement it are called **dunder methods** (short for double-underscore). This lesson introduces the model; Units 2 and 3 go much deeper.

![](images/08_python_data_model_contract.png)

## Everything in Python Is an Object

The first principle of the data model: every value in Python, including integers, strings, functions, and classes themselves, is an instance of some class, and every class participates in the data model.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2ludHJvZHVjdGlvbl90b190aGVfcHl0aG9uX2RhdGFfbW9kZWwgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InByaW50KHR5cGUoNDIpKSAgICAgICAgICAjIDxjbGFzcyAnaW50Jz5cbnByaW50KHR5cGUoXCJoZWxsb1wiKSkgICAgICMgPGNsYXNzICdzdHInPlxucHJpbnQodHlwZShsZW4pKSAgICAgICAgICMgPGNsYXNzICdidWlsdGluX2Z1bmN0aW9uX29yX21ldGhvZCc-XG5wcmludCh0eXBlKHR5cGUpKSAgICAgICAgIyA8Y2xhc3MgJ3R5cGUnPiJ9"
 width="100%"
></iframe>

`int` has a `+` operator because `int` defines `__add__`. `str` supports `len()` because `str` defines `__len__`. When you write your own class, you opt into these behaviors by defining the same methods.

## len(), +, and [] Are Just Method Calls

Python's built-in functions and operators are thin wrappers around dunder method calls. `len(x)` calls `x.__len__()`. `a + b` calls `a.__add__(b)`. `x[0]` calls `x.__getitem__(0)`. This uniformity means any object can participate in any Python feature once it defines the corresponding method.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2ludHJvZHVjdGlvbl90b190aGVfcHl0aG9uX2RhdGFfbW9kZWwgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNsYXNzIFBsYXlsaXN0OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBzb25ncyk6XG4gICAgICAgIHNlbGYuc29uZ3MgPSBzb25nc1xuXG4gICAgZGVmIF9fbGVuX18oc2VsZik6XG4gICAgICAgIHJldHVybiBsZW4oc2VsZi5zb25ncylcblxuICAgIGRlZiBfX2dldGl0ZW1fXyhzZWxmLCBpbmRleCk6XG4gICAgICAgIHJldHVybiBzZWxmLnNvbmdzW2luZGV4XVxuXG4gICAgZGVmIF9fcmVwcl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gZlwiUGxheWxpc3Qoe3NlbGYuc29uZ3N9KVwiXG5cbnAgPSBQbGF5bGlzdChbXCJTb25nIEFcIiwgXCJTb25nIEJcIiwgXCJTb25nIENcIl0pXG5wcmludChsZW4ocCkpICAgICAgIyAzICAtLSBjYWxscyBfX2xlbl9fXG5wcmludChwWzFdKSAgICAgICAgIyBTb25nIEIgIC0tIGNhbGxzIF9fZ2V0aXRlbV9fXG5cbmZvciBzb25nIGluIHA6ICAgICAjIGNhbGxzIF9fZ2V0aXRlbV9fIHdpdGggMCwgMSwgMi4uLiB1bnRpbCBJbmRleEVycm9yXG4gICAgcHJpbnQoc29uZykifQ"
 width="100%"
></iframe>

Notice that `for` works without a dedicated `__iter__` because Python falls back to calling `__getitem__` with increasing indices until it raises `IndexError`. This is the data model being flexible: define one method, get several behaviors for free.

## __str__ vs __repr__: Two Different Audiences

Two of the most immediately useful dunder methods are `__str__` and `__repr__`. They both return a string representation of your object, but they serve different audiences.

`__repr__` is for developers: it should be unambiguous and, ideally, a valid Python expression that recreates the object. It is what you see in the REPL and in `repr()`.

`__str__` is for end users: it should be readable and pleasant. It is what `print()` and `str()` use. If `__str__` is not defined, Python falls back to `__repr__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2ludHJvZHVjdGlvbl90b190aGVfcHl0aG9uX2RhdGFfbW9kZWwgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cblxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIkJvb2sodGl0bGU9e3NlbGYudGl0bGUhcn0sIGlzYm49e3NlbGYuaXNibiFyfSlcIlxuXG4gICAgZGVmIF9fc3RyX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJ7c2VsZi50aXRsZX0gKElTQk46IHtzZWxmLmlzYm59KVwiXG5cbmIgPSBCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIpXG5wcmludChyZXByKGIpKSAgICMgQm9vayh0aXRsZT0nRHVuZScsIGlzYm49Jzk3OC0wNDQxMDEzNTkzJylcbnByaW50KHN0cihiKSkgICAgIyBEdW5lIChJU0JOOiA5NzgtMDQ0MTAxMzU5MylcbnByaW50KGIpICAgICAgICAgIyBEdW5lIChJU0JOOiA5NzgtMDQ0MTAxMzU5MykgIC0tIHByaW50IHVzZXMgX19zdHJfXyJ9"
 width="100%"
></iframe>

Defining both is good practice for any class you will use for more than a few minutes. You will write `__repr__` constantly in Units 2 and 3.

## __eq__ and Why Comparisons Work

By default, `==` compares object identity (the same as `is`). If you want two different objects with the same data to be considered equal, you must define `__eq__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2ludHJvZHVjdGlvbl90b190aGVfcHl0aG9uX2RhdGFfbW9kZWwgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGlzYm4pOlxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG5cbiAgICBkZWYgX19lcV9fKHNlbGYsIG90aGVyKTpcbiAgICAgICAgaWYgbm90IGlzaW5zdGFuY2Uob3RoZXIsIEJvb2spOlxuICAgICAgICAgICAgcmV0dXJuIE5vdEltcGxlbWVudGVkXG4gICAgICAgIHJldHVybiBzZWxmLmlzYm4gPT0gb3RoZXIuaXNiblxuXG5iMSA9IEJvb2soXCI5NzgtMDQ0MTAxMzU5M1wiKVxuYjIgPSBCb29rKFwiOTc4LTA0NDEwMTM1OTNcIilcbnByaW50KGIxID09IGIyKSAgICAjIFRydWUgIC0tIHdpdGhvdXQgX19lcV9fIHRoaXMgd291bGQgYmUgRmFsc2UifQ"
 width="100%"
></iframe>

Returning `NotImplemented` (not `False`) when the types do not match lets Python try the comparison from the other side, which is the correct behavior when working with mixed types.

## The Python Data Model at a Glance

| Dunder method | What it enables |
|---|---|
| `__repr__` | `repr(obj)` and display in the REPL |
| `__str__` | `str(obj)` and `print(obj)` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[index]` and iteration fallback |
| `__eq__` | `obj1 == obj2` |
| `__add__` | `obj1 + obj2` |
| `__iter__` | `for item in obj:` (preferred over `__getitem__`) |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2ludHJvZHVjdGlvbl90b190aGVfcHl0aG9uX2RhdGFfbW9kZWwgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIFNoZWxmOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBib29rcyk6XG4gICAgICAgIHNlbGYuYm9va3MgPSBib29rc1xuXG4gICAgZGVmIF9fbGVuX18oc2VsZik6XG4gICAgICAgIHJldHVybiBsZW4oc2VsZi5ib29rcylcblxuICAgIGRlZiBfX2NvbnRhaW5zX18oc2VsZiwgdGl0bGUpOlxuICAgICAgICByZXR1cm4gYW55KGIudGl0bGUgPT0gdGl0bGUgZm9yIGIgaW4gc2VsZi5ib29rcylcblxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIlNoZWxmKHtsZW4oc2VsZi5ib29rcyl9IGJvb2tzKVwiIn0"
 width="100%"
></iframe>

Add a `Book` class with a `title` attribute, build a `Shelf` with a few books, and then test: `len(shelf)`, `"Dune" in shelf`, and `repr(shelf)`. Then add `__iter__` to `Shelf` so that `for book in shelf: print(book)` works. You will need `__str__` on `Book` as well for a readable output.

## Conclusion

The Python data model is a uniform contract that every object participates in by defining dunder methods. Built-in functions and operators like `len()`, `+`, `[]`, and `for` are all implemented as calls to these methods, which means any class can integrate naturally with Python's syntax once it defines the relevant ones. Units 2 and 3 build on this foundation by exploring how dunder methods combine with encapsulation, access control, inheritance, and polymorphism to produce the kind of clean, expressive APIs that well-designed Python libraries use.

## Introduction

Priya has been using single underscores consistently, and her team has been respecting them. But a new developer joins and, not knowing the convention, reads `_copies` directly and builds a feature that caches the value in another part of the system. When Priya later refactors `_copies` to `_copies_by_branch`, his feature breaks silently. The convention worked until it did not.

She wonders: is there a stronger mechanism? There is, and it uses a double underscore. But it comes with a twist that surprises almost every developer the first time they see it. This lesson explains the difference between one underscore and two, and what name mangling actually does.

![](images/03_access_control_name_mangling.png)

## One Underscore: Convention, Not Enforcement

A single leading underscore (`_copies`) is purely a social signal. Python never prevents you from reading or writing it from outside the class. It communicates "this is an internal detail; use the provided methods instead," and it relies entirely on the caller understanding and respecting that message.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FjY2Vzc19jb250cm9sX3Byb3RlY3RlZF9wcml2YXRlX25hbWVtYW5nbGluZyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGNvcGllcyk6XG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllcyAgICMgc29jaWFsIGNvbnZlbnRpb25cblxuYiA9IEJvb2soXCJEdW5lXCIsIDMpXG5iLl9jb3BpZXMgPSAtOTkgICAjIFB5dGhvbiBhbGxvd3MgdGhpcyBjb21wbGV0ZWx5XG5wcmludChiLl9jb3BpZXMpICAjIC05OSAtLSBjb252ZW50aW9uIGJyb2tlbiwgYnV0IG5vIGVycm9yIn0"
 width="100%"
></iframe>

This is actually intentional in Python's design philosophy. Python prefers clarity and explicit agreements among developers over rigid technical barriers. The single underscore is that agreement. Most of the time, it is enough.

## Two Underscores: Name Mangling

A double leading underscore (`__copies`) triggers a Python feature called **name mangling**. When Python compiles a class that contains an attribute or method starting with `__`, it renames it to `_ClassName__attributename` before the class body runs. This makes it genuinely harder to access from outside the class, because the attribute's name has changed.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FjY2Vzc19jb250cm9sX3Byb3RlY3RlZF9wcml2YXRlX25hbWVtYW5nbGluZyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGNvcGllcyk6XG4gICAgICAgIHNlbGYuX19jb3BpZXMgPSBjb3BpZXMgICAjIHN0b3JlZCBhcyBfQm9va19fY29waWVzXG5cbiAgICBkZWYgY29waWVzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX19jb3BpZXMgICAgIyBzdGlsbCB3b3JrcyBpbnNpZGUgdGhlIGNsYXNzXG5cbmIgPSBCb29rKFwiRHVuZVwiLCAzKVxucHJpbnQoYi5jb3BpZXNfYXZhaWxhYmxlKCkpICAgICMgMyAtLSB3b3Jrc1xuXG5wcmludChiLl9fY29waWVzKSAgICAgICAgICAgICAgIyBlcnJvciEgQXR0cmlidXRlRXJyb3I6IG5vIGF0dHJpYnV0ZSBfX2NvcGllc1xucHJpbnQoYi5fQm9va19fY29waWVzKSAgICAgICAgICMgMyAtLSBuYW1lIG1hbmdsaW5nIGV4cG9zZWQ7IGFjY2Vzc2libGUgYnV0IGRpc2NvdXJhZ2VkIn0"
 width="100%"
></iframe>

The last line is the important one: name mangling is not true privacy. Anyone who knows the mangled name can still access it. The barrier is technical, not cryptographic. Its real purpose is **preventing accidental name clashes in subclasses**, not providing security.

## Why Name Mangling Exists: Subclass Safety

The original motivation for `__` name mangling was not "make attributes private." It was "make sure a subclass cannot accidentally override an important attribute by using the same name."

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FjY2Vzc19jb250cm9sX3Byb3RlY3RlZF9wcml2YXRlX25hbWVtYW5nbGluZyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiY2xhc3MgTGlicmFyeUl0ZW06XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNvcGllcyk6XG4gICAgICAgIHNlbGYuX19jb3BpZXMgPSBjb3BpZXMgICAjIHN0b3JlZCBhcyBfTGlicmFyeUl0ZW1fX2NvcGllc1xuXG5jbGFzcyBFQm9vayhMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGNvcGllcywgZmlsZV9mb3JtYXQpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKGNvcGllcylcbiAgICAgICAgc2VsZi5fX2NvcGllcyA9IGNvcGllcyAgICMgc3RvcmVkIGFzIF9FQm9va19fY29waWVzIC0tIGRpZmZlcmVudCBhdHRyaWJ1dGUhXG5cbml0ZW0gPSBFQm9vayg1LCBcInBkZlwiKVxucHJpbnQoaXRlbS5fTGlicmFyeUl0ZW1fX2NvcGllcykgICAjIDUgLS0gdGhlIHBhcmVudCdzIGNvcGllc1xucHJpbnQoaXRlbS5fRUJvb2tfX2NvcGllcykgICAgICAgICAjIDUgLS0gdGhlIGNoaWxkJ3MgY29waWVzIn0"
 width="100%"
></iframe>

Without name mangling, the subclass's `self.__copies` would overwrite the parent's, causing subtle bugs. With mangling, each class's `__` attribute lives under a unique mangled name. This is the real reason the feature exists.

## When to Use One vs. Two Underscores

In practice, most experienced Python developers use single underscores almost exclusively and reserve double underscores for specific situations.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FjY2Vzc19jb250cm9sX3Byb3RlY3RlZF9wcml2YXRlX25hbWVtYW5nbGluZyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiIyBVc2UgXyB3aGVuOlxuIyAtIFlvdSB3YW50IHRvIHNpZ25hbCBcImludGVybmFsIGRldGFpbCwgcGxlYXNlIHVzZSB0aGUgbWV0aG9kc1wiXG4jIC0gVGhlIGF0dHJpYnV0ZSBjb3VsZCByZWFzb25hYmx5IGJlIG92ZXJyaWRkZW4gaW4gYSBzdWJjbGFzcyAoaWYgYXBwcm9wcmlhdGUpXG5zZWxmLl9jb3BpZXMgPSBjb3BpZXNcblxuIyBVc2UgX18gd2hlbjpcbiMgLSBZb3UgaGF2ZSBhIHNwZWNpZmljIGNvbmNlcm4gdGhhdCBhIHN1YmNsYXNzIG1pZ2h0IGFjY2lkZW50YWxseSBzaGFkb3cgdGhpcyBuYW1lXG4jIC0gVGhlIGF0dHJpYnV0ZSBpcyBzbyBmdW5kYW1lbnRhbCB0byB0aGUgY2xhc3MncyBpbnRlZ3JpdHkgdGhhdCBhY2NpZGVudGFsIGNvbGxpc2lvblxuIyAgIGluIGluaGVyaXRhbmNlIGNvdWxkIGNhdXNlIGhhcmQtdG8tZGVidWcgYmVoYXZpb3JcbnNlbGYuX190cmFuc2FjdGlvbl9pZCA9IGdlbmVyYXRlX2lkKCkifQ"
 width="100%"
></iframe>

Using `__` everywhere is actually a minor anti-pattern: it makes introspection and testing harder, and it communicates the wrong intent (collision avoidance) rather than the intended one (internal detail).

## No Trailing Double Underscore: Dunder Methods Are Different

It is easy to confuse `__name__` (double underscore on both sides) with `__name` (double underscore only at the start). They are completely different:

- `__copies`: name mangling applies, attribute renamed to `_Book__copies`
- `__repr__`: a **dunder method** (double on both sides), recognized by Python as part of the data model, no mangling

Never create your own attributes or methods with the `__name__` double-double-underscore pattern. Those names are reserved for Python's own protocols.

## Access Control at a Glance

| Convention | Example | What Python does | Who can access it |
|---|---|---|---|
| Public | `self.copies` | Nothing | Anyone |
| Protected | `self._copies` | Nothing (social only) | Anyone, but "please don't" |
| Name-mangled | `self.__copies` | Renamed to `_ClassName__copies` | Still accessible, just harder |
| Dunder method | `__repr__` | Recognized by the data model | Called by Python itself |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FjY2Vzc19jb250cm9sX3Byb3RlY3RlZF9wcml2YXRlX25hbWVtYW5nbGluZyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY2xhc3MgU2VjdXJlQWNjb3VudDpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgb3duZXIsIHBpbik6XG4gICAgICAgIHNlbGYub3duZXIgPSBvd25lclxuICAgICAgICBzZWxmLl9fcGluID0gcGluICAgICAgICMgbmFtZS1tYW5nbGVkXG5cbiAgICBkZWYgdmVyaWZ5X3BpbihzZWxmLCBhdHRlbXB0KTpcbiAgICAgICAgcmV0dXJuIGF0dGVtcHQgPT0gc2VsZi5fX3BpblxuXG5hID0gU2VjdXJlQWNjb3VudChcIlByaXlhXCIsIFwiMTIzNFwiKVxucHJpbnQoYS52ZXJpZnlfcGluKFwiMTIzNFwiKSkgICAgIyBUcnVlXG5wcmludChhLnZlcmlmeV9waW4oXCIwMDAwXCIpKSAgICAjIEZhbHNlIn0"
 width="100%"
></iframe>

Try to print `a.__pin` and observe the `AttributeError`. Then use Python's `dir(a)` to find the mangled name, and print it directly. Finally explain: does name mangling actually prevent someone determined from reading the pin? What does it actually prevent?

## Conclusion

A single leading underscore is a social convention signaling "internal detail." A double leading underscore triggers name mangling, which renames the attribute to prevent accidental subclass collisions, but does not create true privacy. Most Python code uses single underscores, reserving double underscores for specific inheritance-safety concerns. The next lesson introduces a more elegant solution to the "callers are setting attributes directly" problem: properties, which look like attribute access but secretly run a method.

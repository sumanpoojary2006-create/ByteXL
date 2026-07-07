## Introduction

Dev notices something tedious about his `Book` and `LibraryItem` classes: almost every new attribute he adds requires touching three places: the `__init__` signature, the body of `__init__`, and `__repr__`. When the class holds five or six attributes, this boilerplate becomes oppressive. He finds himself writing the same `__init__` pattern for every new data class he creates.

Python 3.7 introduced `dataclasses` to solve exactly this problem. A `dataclass` is an ordinary Python class with `__init__`, `__repr__`, and `__eq__` generated automatically from field declarations. It does not add new behavior to Python; it removes repetitive boilerplate while keeping the class model completely familiar.

![](images/08_dataclasses.png)

## The Basic dataclass

The `@dataclass` decorator reads your class's annotated attributes and generates `__init__`, `__repr__`, and `__eq__` for you.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcblxuQGRhdGFjbGFzc1xuY2xhc3MgQm9vazpcbiAgICB0aXRsZTogc3RyXG4gICAgaXNibjogc3RyXG4gICAgY29waWVzOiBpbnRcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50KGIpICAgICAgICAgICAjIEJvb2sodGl0bGU9J0R1bmUnLCBpc2JuPSc5NzgtMDQ0MTAxMzU5MycsIGNvcGllcz0zKVxucHJpbnQocmVwcihiKSkgICAgICMgQm9vayh0aXRsZT0nRHVuZScsIGlzYm49Jzk3OC0wNDQxMDEzNTkzJywgY29waWVzPTMpXG5cbmIyID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiLCAzKVxucHJpbnQoYiA9PSBiMikgICAgICMgVHJ1ZSAtLSBfX2VxX18gY29tcGFyZXMgYWxsIGZpZWxkcyJ9"
 width="100%"
></iframe>

The type annotations (`title: str`) are used by the dataclass decorator to know which fields to include. Python does not enforce these types at runtime unless you use a separate tool like `mypy`; the annotations are metadata that `@dataclass` reads to generate code.

## Default Values and Default Factories

Fields can have defaults, just as in a normal `__init__`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3MsIGZpZWxkXG5cbkBkYXRhY2xhc3NcbmNsYXNzIEJvb2s6XG4gICAgdGl0bGU6IHN0clxuICAgIGlzYm46IHN0clxuICAgIGNvcGllczogaW50ID0gMVxuICAgIHRhZ3M6IGxpc3QgPSBmaWVsZChkZWZhdWx0X2ZhY3Rvcnk9bGlzdCkgICAjIG11dGFibGUgZGVmYXVsdDogbXVzdCB1c2UgZmllbGQoKVxuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiKVxucHJpbnQoYi5jb3BpZXMpICAgIyAxIC0tIGRlZmF1bHQgdXNlZFxucHJpbnQoYi50YWdzKSAgICAgIyBbXVxuXG5iLnRhZ3MuYXBwZW5kKFwic2NpLWZpXCIpXG5iMiA9IEJvb2soXCJGb3VuZGF0aW9uXCIsIFwiOTc4LTA1NTMyOTMzNTdcIilcbnByaW50KGIyLnRhZ3MpICAgICMgW10gLS0gZWFjaCBpbnN0YW5jZSBnZXRzIGl0cyBvd24gbGlzdCJ9"
 width="100%"
></iframe>

The `field(default_factory=list)` is important: you cannot write `tags: list = []` directly in a dataclass (or any Python class) because the same list object would be shared across all instances. `default_factory` creates a fresh list for each new instance.

## Adding Methods to Dataclasses

A `@dataclass` is a normal class. You can add methods exactly as you would in any class:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcblxuQGRhdGFjbGFzc1xuY2xhc3MgQm9vazpcbiAgICB0aXRsZTogc3RyXG4gICAgaXNibjogc3RyXG4gICAgY29waWVzOiBpbnQgPSAxXG5cbiAgICBkZWYgaXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5jb3BpZXMgPiAwXG5cbiAgICBkZWYgY2hlY2tfb3V0KHNlbGYpOlxuICAgICAgICBpZiBzZWxmLmNvcGllcyA8IDE6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIk5vIGNvcGllcyBvZiAne3NlbGYudGl0bGV9JyBhdmFpbGFibGVcIilcbiAgICAgICAgc2VsZi5jb3BpZXMgLT0gMVxuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiLCAyKVxucHJpbnQoYi5pc19hdmFpbGFibGUoKSkgICAjIFRydWVcbmIuY2hlY2tfb3V0KClcbmIuY2hlY2tfb3V0KClcbnByaW50KGIuaXNfYXZhaWxhYmxlKCkpICAgIyBGYWxzZSJ9"
 width="100%"
></iframe>

## Frozen Dataclasses: Immutable by Default

Adding `frozen=True` makes a dataclass immutable: its fields cannot be reassigned after creation, and Python generates `__hash__`, making instances usable as dictionary keys or set members.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcblxuQGRhdGFjbGFzcyhmcm96ZW49VHJ1ZSlcbmNsYXNzIElTQk46XG4gICAgdmFsdWU6IHN0clxuXG4gICAgZGVmIF9fcG9zdF9pbml0X18oc2VsZik6XG4gICAgICAgIGlmIG5vdCBzZWxmLnZhbHVlLnN0YXJ0c3dpdGgoXCI5NzhcIik6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKFwiSVNCTiBtdXN0IHN0YXJ0IHdpdGggOTc4XCIpXG5cbmkgPSBJU0JOKFwiOTc4LTA0NDEwMTM1OTNcIilcbnByaW50KGkudmFsdWUpICAgICAgIyA5NzgtMDQ0MTAxMzU5M1xuaS52YWx1ZSA9IFwib3RoZXJcIiAgICMgZXJyb3IhIEZyb3plbkluc3RhbmNlRXJyb3I6IGNhbm5vdCBhc3NpZ24gdG8gZmllbGQgJ3ZhbHVlJ1xuXG4jIFVzYWJsZSBpbiBhIHNldCBiZWNhdXNlIGZyb3plbiBkYXRhY2xhc3NlcyBhcmUgaGFzaGFibGVcbnNlZW4gPSB7SVNCTihcIjk3OC0wNDQxMDEzNTkzXCIpLCBJU0JOKFwiOTc4LTA1NTMyOTMzNTdcIil9In0"
 width="100%"
></iframe>

Frozen dataclasses are excellent for value objects: things that represent a value rather than an entity with changing state, like an ISBN, a coordinate, a date range, or a configuration snapshot.

## __post_init__: Running Code After auto-generated __init__

If you need to run validation or derived computation after all fields are set, `__post_init__` runs automatically at the end of the generated `__init__`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3NcblxuQGRhdGFjbGFzc1xuY2xhc3MgQm9vazpcbiAgICB0aXRsZTogc3RyXG4gICAgaXNibjogc3RyXG4gICAgY29waWVzOiBpbnQgPSAxXG5cbiAgICBkZWYgX19wb3N0X2luaXRfXyhzZWxmKTpcbiAgICAgICAgaWYgc2VsZi5jb3BpZXMgPCAwOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmXCJjb3BpZXMgY2Fubm90IGJlIG5lZ2F0aXZlLCBnb3Qge3NlbGYuY29waWVzfVwiKVxuICAgICAgICBzZWxmLnRpdGxlID0gc2VsZi50aXRsZS5zdHJpcCgpICAgIyBub3JtYWxpemUgd2hpdGVzcGFjZVxuXG5iID0gQm9vayhcIiAgRHVuZSAgXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMylcbnByaW50KGIudGl0bGUpICAgIyBEdW5lIC0tIHN0cmlwcGVkIGJ5IF9fcG9zdF9pbml0X18ifQ"
 width="100%"
></iframe>

## Dataclasses at a Glance

| Feature | How to use it |
|---|---|
| Auto `__init__`, `__repr__`, `__eq__` | `@dataclass` decorator |
| Default values | `field: type = value` |
| Mutable defaults (list, dict) | `field(default_factory=list)` |
| Immutable instances | `@dataclass(frozen=True)` |
| Post-creation logic | `def __post_init__(self):` |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2RhdGFjbGFzc2VzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJmcm9tIGRhdGFjbGFzc2VzIGltcG9ydCBkYXRhY2xhc3MsIGZpZWxkXG5cbkBkYXRhY2xhc3NcbmNsYXNzIFBhdHJvbjpcbiAgICBuYW1lOiBzdHJcbiAgICBjYXJkX251bWJlcjogc3RyXG4gICAgYm9ycm93ZWQ6IGxpc3QgPSBmaWVsZChkZWZhdWx0X2ZhY3Rvcnk9bGlzdClcblxuICAgIGRlZiBib3Jyb3coc2VsZiwgYm9va190aXRsZSk6XG4gICAgICAgIHNlbGYuYm9ycm93ZWQuYXBwZW5kKGJvb2tfdGl0bGUpXG5cbiAgICBkZWYgcmV0dXJuX2Jvb2soc2VsZiwgYm9va190aXRsZSk6XG4gICAgICAgIGlmIGJvb2tfdGl0bGUgbm90IGluIHNlbGYuYm9ycm93ZWQ6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIid7Ym9va190aXRsZX0nIG5vdCBib3Jyb3dlZCBieSB7c2VsZi5uYW1lfVwiKVxuICAgICAgICBzZWxmLmJvcnJvd2VkLnJlbW92ZShib29rX3RpdGxlKSJ9"
 width="100%"
></iframe>

Create two `Patron` objects, have each borrow different books, and confirm their `borrowed` lists are independent. Then print `repr()` of each patron. Finally convert `Patron` to `frozen=True`, observe what breaks, and explain why a patron needs to be mutable (state changes over time) while an `ISBN` is a better candidate for frozen.

## Conclusion

The `@dataclass` decorator generates `__init__`, `__repr__`, and `__eq__` from field annotations, removing the most repetitive boilerplate in data-holding classes while leaving you free to add methods, override generated methods, and add `__post_init__` validation. Frozen dataclasses add immutability and hashability, making them ideal for value objects. The final lesson of this unit covers three method varieties that Python supports on classes: instance methods (which you have been writing all along), class methods, and static methods.

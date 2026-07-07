## Introduction

Dev notices something tedious about his `Book` and `LibraryItem` classes: almost every new attribute he adds requires touching three places: the `__init__` signature, the body of `__init__`, and `__repr__`. When the class holds five or six attributes, this boilerplate becomes oppressive. He finds himself writing the same `__init__` pattern for every new data class he creates.

Python 3.7 introduced `dataclasses` to solve exactly this problem. A `dataclass` is an ordinary Python class with `__init__`, `__repr__`, and `__eq__` generated automatically from field declarations. It does not add new behavior to Python; it removes repetitive boilerplate while keeping the class model completely familiar.

![](images/08_dataclasses.png)

## The Basic dataclass

The `@dataclass` decorator reads your class's annotated attributes and generates `__init__`, `__repr__`, and `__eq__` for you.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-001-fc90959cb9.html"
 width="100%"
></iframe>

The type annotations (`title: str`) are used by the dataclass decorator to know which fields to include. Python does not enforce these types at runtime unless you use a separate tool like `mypy`; the annotations are metadata that `@dataclass` reads to generate code.

## Default Values and Default Factories

Fields can have defaults, just as in a normal `__init__`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-002-47181d6e59.html"
 width="100%"
></iframe>

The `field(default_factory=list)` is important: you cannot write `tags: list = []` directly in a dataclass (or any Python class) because the same list object would be shared across all instances. `default_factory` creates a fresh list for each new instance.

## Adding Methods to Dataclasses

A `@dataclass` is a normal class. You can add methods exactly as you would in any class:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-003-035d219364.html"
 width="100%"
></iframe>

## Frozen Dataclasses: Immutable by Default

Adding `frozen=True` makes a dataclass immutable: its fields cannot be reassigned after creation, and Python generates `__hash__`, making instances usable as dictionary keys or set members.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-004-ca0e8ee82b.html"
 width="100%"
></iframe>

Frozen dataclasses are excellent for value objects: things that represent a value rather than an entity with changing state, like an ISBN, a coordinate, a date range, or a configuration snapshot.

## __post_init__: Running Code After auto-generated __init__

If you need to run validation or derived computation after all fields are set, `__post_init__` runs automatically at the end of the generated `__init__`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-005-dbb0ba03ba.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-08-dataclasses-006-fd5150ed35.html"
 width="100%"
></iframe>

Create two `Patron` objects, have each borrow different books, and confirm their `borrowed` lists are independent. Then print `repr()` of each patron. Finally convert `Patron` to `frozen=True`, observe what breaks, and explain why a patron needs to be mutable (state changes over time) while an `ISBN` is a better candidate for frozen.

## Conclusion

The `@dataclass` decorator generates `__init__`, `__repr__`, and `__eq__` from field annotations, removing the most repetitive boilerplate in data-holding classes while leaving you free to add methods, override generated methods, and add `__post_init__` validation. Frozen dataclasses add immutability and hashability, making them ideal for value objects. The final lesson of this unit covers three method varieties that Python supports on classes: instance methods (which you have been writing all along), class methods, and static methods.

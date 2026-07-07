## Introduction

Priya has been creating a `Student` object and then immediately writing three or four separate lines to attach a name, a roll number, and marks, every single time, for every single student. Forget one of those lines, even once, and that student object is left with a missing attribute, ready to raise an `AttributeError` the moment anything tries to read it. She wants every `Student` to arrive already complete, with all of its required attributes set the instant it is created, with no separate setup step she might forget.

Python's answer is the **`__init__` constructor**, a special method that runs automatically the moment an object is instantiated, exactly the right place to guarantee every object starts out fully formed.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_builds_complete_object.png)

## The __init__ Method Runs Automatically

Define a method named `__init__` inside a class, and Python calls it automatically every time that class is instantiated, immediately after the object is created.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-001-0aa75ab16d.html"
 width="100%"
></iframe>

Notice nobody explicitly called `__init__`; writing `Student()` triggered it on its own. The double underscores on either side of the name are Python's signal that this method has a special, built-in role, rather than being an ordinary method you invented yourself.

## Accepting Values and Setting Attributes

`__init__` can take parameters beyond `self`, exactly like any other method, and the values passed in when the object is created flow straight into it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-002-cb1155f6a8.html"
 width="100%"
></iframe>

Read each line inside `__init__` carefully: `self.name = name` takes the `name` argument that was just passed in, and stores it as an attribute on this specific object. Now every `Student` is guaranteed to have a `name`, a `roll_number`, and `marks` the instant it exists, because there is no way to call `Student(...)` without supplying all three.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_auto_setup.png)


## Required Arguments at Creation Time

Leave out a required argument, and Python refuses to create the object at all, exactly the protection Priya was missing before.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-003-242fcb3649.html"
 width="100%"
></iframe>

This raises a `TypeError` complaining that `__init__` is missing the required `marks` argument, caught immediately at creation time rather than silently producing a broken object that fails later, possibly far away from where the mistake actually happened.

## Combining __init__ With Other Methods

`__init__` sets attributes up once; your other methods, exactly as in the previous lesson, can then use `self` to read and reason about them.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-004-c590355431.html"
 width="100%"
></iframe>

Both objects were complete and ready to use the moment they were created, with no separate setup lines anywhere, and `report` works correctly on each, exactly because `__init__` guaranteed every attribute it needs was already there.

## Default Values Inside __init__

A constructor's parameters can carry default values too, exactly like any function parameter from the functions unit, making some setup details optional.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-005-abd9e62004.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-06-the-init-constructor-006-1d42bb68b2.html"
 width="100%"
></iframe>

Every account this class produces starts complete, with a holder and a balance guaranteed from the very first line after creation.

## Conclusion

`__init__` is a special method that Python calls automatically the moment an object is instantiated, and setting attributes inside it, using `self.attribute = value`, guarantees every object starts fully formed, with required arguments enforced immediately rather than discovered later as a missing-attribute crash. Default values inside `__init__` work exactly like default parameters on any function. With objects now arriving complete and capable, the next lesson walks through two full, realistic classes from start to finish: a Student and a BankAccount.

## Introduction

Priya now has the vocabulary, class and object, but she still cannot write either one in actual Python. She wants to create a `Student` blueprint, and then build a separate, independent object from it for Asha, another for Ravi, and another for Meera, exactly the way the cookie cutter analogy described. This lesson gives her the precise syntax for both halves of that idea: the `class` keyword to define the blueprint, and a function-call-like syntax to actually build an object from it.

This is the moment OOP stops being an analogy and starts being code you can run.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/03_class_definition_three_objects.png)

## Defining a Class

A class is defined with the keyword `class`, followed by a name, and a colon, with its body indented underneath, the same shape you already trust from functions and `if` blocks. The simplest possible class needs a body of some kind, so an empty one uses the placeholder keyword `pass`.

```python
class Student:
    pass

# Demo:
obj = Student()
print(obj)
```

By strong convention, class names are written in CapitalisedWords, sometimes called PascalCase, which is exactly why this is `Student` and not `student`, the opposite convention from the snake_case you use for variables and functions. That capital letter is a small but real signal to anyone reading your code: "this name refers to a class."

## Creating an Object: Instantiation

To build an actual object from a class, write the class name followed by parentheses, exactly the way you call a function.

```python
class Student:
    pass

asha = Student()
print(asha)             # <__main__.Student object at 0x...>
print(type(asha))       # <class '__main__.Student'>
```

This process is called **instantiation**, and `asha` is now an **instance** of the `Student` class, a real object built from that blueprint. The exact text after `object at` will differ every time you run this, since it is a memory address Python assigned, but the important part, `<__main__.Student object`, confirms `asha` really is a `Student`.

## Many Independent Objects From One Class

Call the class again, and you get a brand new, separate object, exactly as pressing a cookie cutter twice gives you two separate cookies.

```python
class Student:
    pass

asha = Student()
ravi = Student()
meera = Student()

print(asha is ravi)    # False, two separate objects
```

The `is` operator checks whether two names refer to the very same object in memory, not just equal-looking ones, and here it confirms `asha` and `ravi` are genuinely two distinct students, even though both came from the identical `Student` blueprint.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/03_instantiation_factory.png)


## An Empty Class Holds Nothing Useful Yet

Right now, `Student()` produces an object with no name, no roll number, nothing at all attached to it. That is expected at this stage; an empty class is simply a blueprint with no described shape yet. The next two lessons fill that gap, first by attaching data directly to an object, and then by giving the class a proper way to set that data up automatically the moment an object is created.

## Defining and Instantiating at a Glance

| Step | Syntax | What It Produces |
|---|---|---|
| Define the class | `class Student:` then an indented body | A blueprint, no objects yet |
| Instantiate an object | `asha = Student()` | One real, independent object |
| Instantiate another | `ravi = Student()` | A second, completely separate object |
| Check the type | `type(asha)` | Confirms which class an object was built from |

## Your Turn: Build Three Objects

```python
class BankAccount:
    pass

acc1 = BankAccount()
acc2 = BankAccount()
acc3 = BankAccount()

print(acc1 is acc2)    # False
print(acc2 is acc3)    # False
print(type(acc1))      # <class '__main__.BankAccount'>
```

Run this and confirm for yourself that all three accounts, though built from the exact same blueprint, are genuinely separate objects, none of them secretly sharing identity with another.

## Conclusion

A class is defined with `class Name:` and an indented body, following the CapitalisedWords naming convention, and an object is created from it by calling the class name with parentheses, a process called instantiation. Each call produces a brand new, independent object, confirmed distinct from any other with the `is` operator, even when built from the same class. An empty class like this holds no actual data yet; the next lesson attaches real values, called attributes, to each individual object.

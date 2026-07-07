## Introduction

Priya has been creating a `Student` object and then immediately writing three or four separate lines to attach a name, a roll number, and marks, every single time, for every single student. Forget one of those lines, even once, and that student object is left with a missing attribute, ready to raise an `AttributeError` the moment anything tries to read it. She wants every `Student` to arrive already complete, with all of its required attributes set the instant it is created, with no separate setup step she might forget.

Python's answer is the **`__init__` constructor**, a special method that runs automatically the moment an object is instantiated, exactly the right place to guarantee every object starts out fully formed.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_builds_complete_object.png)

## The __init__ Method Runs Automatically

Define a method named `__init__` inside a class, and Python calls it automatically every time that class is instantiated, immediately after the object is created.

```python
class Student:
    def __init__(self):
        print("A new student object was just created.")

asha = Student()    # A new student object was just created.
```

Notice nobody explicitly called `__init__`; writing `Student()` triggered it on its own. The double underscores on either side of the name are Python's signal that this method has a special, built-in role, rather than being an ordinary method you invented yourself.

## Accepting Values and Setting Attributes

`__init__` can take parameters beyond `self`, exactly like any other method, and the values passed in when the object is created flow straight into it.

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

asha = Student("Asha", 101, 72)
print(asha.name, asha.roll_number, asha.marks)    # Asha 101 72
```

Read each line inside `__init__` carefully: `self.name = name` takes the `name` argument that was just passed in, and stores it as an attribute on this specific object. Now every `Student` is guaranteed to have a `name`, a `roll_number`, and `marks` the instant it exists, because there is no way to call `Student(...)` without supplying all three.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/06_init_auto_setup.png)


## Required Arguments at Creation Time

Leave out a required argument, and Python refuses to create the object at all, exactly the protection Priya was missing before.

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

try:
    ravi = Student("Ravi", 102)    # error! marks is missing
except TypeError as e:
    print(f"TypeError: {e}")
    print("Python refused to build the object because a required argument was missing.")
```

This raises a `TypeError` complaining that `__init__` is missing the required `marks` argument, caught immediately at creation time rather than silently producing a broken object that fails later, possibly far away from where the mistake actually happened.

## Combining __init__ With Other Methods

`__init__` sets attributes up once; your other methods, exactly as in the previous lesson, can then use `self` to read and reason about them.

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

    def report(self):
        result = "Pass" if self.has_passed() else "Fail"
        print(f"{self.name} (Roll {self.roll_number}): {result}")

asha = Student("Asha", 101, 72)
ravi = Student("Ravi", 102, 30)

asha.report()    # Asha (Roll 101): Pass
ravi.report()    # Ravi (Roll 102): Fail
```

Both objects were complete and ready to use the moment they were created, with no separate setup lines anywhere, and `report` works correctly on each, exactly because `__init__` guaranteed every attribute it needs was already there.

## Default Values Inside __init__

A constructor's parameters can carry default values too, exactly like any function parameter from the functions unit, making some setup details optional.

```python
class Student:
    def __init__(self, name, roll_number, marks=0):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

new_admission = Student("Meera", 103)
print(new_admission.marks)    # 0, no marks entered yet
```

## __init__ at a Glance

| Idea | Detail |
|---|---|
| What it is | A special method named `__init__`, with double underscores on each side |
| When it runs | Automatically, the moment an object is instantiated |
| What it is for | Setting up an object's attributes so it starts complete |
| Required arguments | Missing one raises a `TypeError` immediately, at creation |

## Your Turn: A Complete BankAccount From the Start

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def can_withdraw(self, amount):
        return amount <= self.balance

acc = BankAccount("Asha", 1000)
acc.deposit(500)
print(acc.holder, acc.balance)         # Asha 1500
print(acc.can_withdraw(2000))           # False
```

Every account this class produces starts complete, with a holder and a balance guaranteed from the very first line after creation.

## Conclusion

`__init__` is a special method that Python calls automatically the moment an object is instantiated, and setting attributes inside it, using `self.attribute = value`, guarantees every object starts fully formed, with required arguments enforced immediately rather than discovered later as a missing-attribute crash. Default values inside `__init__` work exactly like default parameters on any function. With objects now arriving complete and capable, the next lesson walks through two full, realistic classes from start to finish: a Student and a BankAccount.

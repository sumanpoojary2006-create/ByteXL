## Introduction

Priya has all the pieces now: a class is a blueprint, an object is a specific instance, attributes hold an object's own data, methods are actions that belong to it, and `__init__` guarantees every object starts complete. What she has not yet done is build one genuinely complete, realistic class from a blank file, watch it work end to end, and then do it again for a second, differently shaped real-world thing.

This lesson walks through two full classes from scratch: a `Student`, finishing the example this unit has been building all along, and a `BankAccount`, modeling something that changes meaningfully over time rather than just sitting there.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/07_two_complete_classes_walkthrough.png)

## Building the Student Class, Start to Finish

Begin with what a student needs to carry, and what a student needs to be able to do.

```text
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def report(self):
        status = "Pass" if self.has_passed() else "Fail"
        print(f"{self.name} (Roll {self.roll_number}): {status}, Grade {self.grade()}")
```

Notice how naturally each piece fits the role it was given in earlier lessons. `__init__` makes sure every student starts complete. `has_passed` and `grade` each reason about the object's own `marks` through `self`. `report` ties the others together, calling both `self.has_passed()` and `self.grade()` to build one final message.

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def report(self):
        status = "Pass" if self.has_passed() else "Fail"
        print(f"{self.name} (Roll {self.roll_number}): {status}, Grade {self.grade()}")

asha = Student("Asha", 101, 92)
ravi = Student("Ravi", 102, 55)
meera = Student("Meera", 103, 30)

for student in [asha, ravi, meera]:
    student.report()
```

Output:

```
Asha (Roll 101): Pass, Grade A
Ravi (Roll 102): Pass, Grade C
Meera (Roll 103): Fail, Grade F
```

That last block is worth pausing on: a plain `for` loop, from two units ago, walks through a list of `Student` objects exactly as comfortably as it would walk through a list of numbers or strings, calling the same method on each one in turn.

## Building the BankAccount Class, Start to Finish

A bank account is a different shape of problem. A student's marks rarely change once entered, but an account's balance is expected to change constantly, through deposits and withdrawals, and it must never be allowed to go below zero by mistake.

```text
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
```

`withdraw` is doing real work here, not just reporting a value: it checks a condition with `self.balance` before changing anything, exactly the guard-clause habit from the control flow unit, now protecting an object's own data instead of a plain variable.

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

acc = BankAccount("Asha", 1000)
acc.deposit(500)      # Deposited 500. New balance: 1500
acc.withdraw(2000)    # Insufficient balance.
acc.withdraw(800)     # Withdrew 800. New balance: 700
```

Each call changes `acc.balance` in place, on that one object, and the next call always sees the latest, correct value, because the balance genuinely lives on the object itself, not in a separate variable that something else might forget to update.

## Student vs BankAccount at a Glance

| | Student | BankAccount |
|---|---|---|
| What rarely changes | Name, roll number | The account holder's name |
| What changes over time | Marks, occasionally | Balance, constantly |
| A method that reasons about state | `has_passed()`, reads marks | `can_withdraw`-style checks before acting |
| A method that changes state | Rare; marks are usually set once | `deposit()` and `withdraw()`, every call |

Both are built from the exact same four ingredients, `__init__`, attributes, methods, and `self`, simply describing two different real-world things, one mostly static, one constantly changing.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/07_object_lifecycle_walkthrough.png)


## Your Turn: Extend the BankAccount

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount

    def summary(self):
        print(f"{self.holder}'s balance: {self.balance}")

acc = BankAccount("Ravi", 2000)
acc.deposit(300)
acc.withdraw(500)
acc.summary()    # Ravi's balance: 1800
```

A new method, `summary`, was added with no changes needed anywhere else in the class, exactly the kind of clean extension a well-built class allows.

## Conclusion

A complete class combines `__init__` to guarantee every object starts fully formed, attributes to hold its own data, and methods, always taking `self` first, to read, reason about, and change that data. The `Student` class modeled something mostly static, judged by its own data, while the `BankAccount` class modeled something that changes constantly, protected by a condition before any change is allowed. Both came from the exact same four ingredients. The final lesson of this unit asks the practical question every one of these examples has been building toward: when does a real piece of data actually deserve a class, instead of a plain dictionary or tuple?

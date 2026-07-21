# Unit 9: Basic Object-Oriented Programming - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 9 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led modelling, object-state tracing, implementation comparison, failure diagnosis, minimal repair, and design judgment
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option

---

## Questions

### 1. A transferred student exposes a record-keeping weakness

**Difficulty:** Foundational

An office stores student names and roll numbers in separate lists whose positions must always match. After one name is moved without its roll number, reports pair the wrong details. Which redesign addresses the underlying modelling problem?

A. Sort both lists independently before every report  
B. Add more comments explaining that the positions must match  
C. Represent each student as one object carrying its related data  
D. Convert the roll-number list into a tuple and keep the name list unchanged

### 2. Identifying the central things in a service application

**Difficulty:** Intermediate

A repair service tracks customers who raise tickets, technicians who accept them, and tickets that change status. Which first step best reflects object-oriented modelling?

A. Identify `Customer`, `Technician`, and `Ticket` as candidate program entities  
B. Put every value into one long list, then document the position assigned to each field and entity  
C. Create one function for each individual customer by name  
D. Store all statuses in variables unrelated to their tickets

### 3. Related facts are together, but their rule is still scattered

**Difficulty:** Intermediate

Each order is already stored as a dictionary containing `total` and `paid`. Five screens separately repeat the rule that decides whether an order can ship. Which improvement takes the next OOP step?

A. Rename the dictionaries differently on the five screens  
B. Store `total` and `paid` in separate lists again  
C. Copy the shipping condition into every current and future screen that displays an order  
D. Model an order with its data and a reusable shipping-decision method

### 4. Two implementations face a policy change

**Difficulty:** Advanced

Version A stores account balances in dictionaries and lets each screen implement withdrawals. Version B gives every account object one `withdraw` method that rejects overdrafts. A new fee rule is introduced. Which comparison is strongest?

A. Version A guarantees consistency because dictionaries prevent screens from using different rules  
B. Version B has one method to update, so every account follows the revised withdrawal rule  
C. Both versions necessarily require changes in exactly one location  
D. Version B is unsuitable because an object's balance cannot change after creation

### 5. Distinguishing a blueprint from one real item

**Difficulty:** Foundational

A library system includes a general description, "Every book has a title and author," and a record for the specific copy of *Wings of Fire* on shelf 3. How should these be classified?

A. Both descriptions are classes because both refer to books  
B. The general description is an object; the shelf copy is a class  
C. Both descriptions are objects with different amounts of data  
D. The general description is a class; the shelf copy is an object

### 6. One blueprint serves three registrations

**Difficulty:** Intermediate

`asha`, `ravi`, and `meera` are created separately from the same `Student` class. Which statement correctly describes their relationship?

A. The first object is the class, while the remaining two are copies of it  
B. They are three independent objects built from one shared blueprint  
C. They must all hold identical attribute values because their class matches  
D. Creating the third object automatically deletes the first one

### 7. Choosing the object from a set of descriptions

**Difficulty:** Intermediate

Which description refers to an object rather than a class?

A. An invoice has a number, date, and amount  
B. A vehicle can start, stop, and report its speed  
C. Neha's invoice `INV-204`, dated 12 July, for ₹850  
D. A support ticket has an owner and can be closed

### 8. Testing independence rather than shared origin

**Difficulty:** Advanced

Two student objects come from the same class. After `asha.marks` is changed from 70 to 95, `ravi.marks` remains 70. Which conclusion follows?

A. Objects can share a class while retaining separate attribute values  
B. Changing an object automatically creates a new class for that object  
C. The two names must refer to one object because their original marks matched  
D. Classes prevent attributes from being reassigned after instantiation

### 9. Creating the smallest usable blueprint

**Difficulty:** Foundational

A developer wants an intentionally empty `Sensor` class before adding details later. Which definition is valid Python?

A. `def Sensor(): pass`  
B. `class Sensor: pass`  
C. `Sensor = class()`  
D. `class Sensor()`

### 10. Producing one instance from an existing class

**Difficulty:** Intermediate

The class `Sensor` has already been defined and currently needs no arguments. Which statement instantiates one object and stores it in `lab_sensor`?

A. `class lab_sensor = Sensor`  
B. `lab_sensor.Sensor()`  
C. `def lab_sensor(Sensor)`  
D. `lab_sensor = Sensor()`

### 11. Two calls use the same empty class

**Difficulty:** Intermediate

```python
class PassCard:
    pass

card_a = PassCard()
card_b = PassCard()
same = card_a is card_b
```

Which value is assigned to `same`?

A. `False`, because the two calls create distinct objects  
B. `True`, because both objects have no attributes  
C. `None`, because `is` works only with numbers and strings  
D. The comparison fails because empty classes cannot be instantiated twice

### 12. Making a class name readable as a class name

**Difficulty:** Intermediate

A code review finds a class written as `class bank_account:`. Which revision follows the naming convention taught in this unit?

A. `class bank-account:`  
B. `class BANK_ACCOUNT:`  
C. `class BankAccount:`  
D. `class bankAccount:`

### 13. An alias is confused with a fresh instance

**Difficulty:** Advanced

```python
class Student:
    pass

first = Student()
second = first
third = Student()
first.name = "Asha"
```

Which observation correctly distinguishes assignment from instantiation?

A. `second.name` is `"Asha"`, while reading `third.name` raises `AttributeError`  
B. Both `second.name` and `third.name` are automatically `"Asha"`  
C. Reading either name raises `AttributeError` because attributes cannot be added later  
D. `third.name` is `"Asha"`, while `second` remains without a name

### 14. Attaching data to one existing object

**Difficulty:** Foundational

An empty `Student` object is stored in `asha`. Which statement attaches roll number 101 to that particular object?

A. `Student.roll_number(101)`  
B. `roll_number.asha = 101`  
C. `asha.roll_number = 101`  
D. `asha = roll_number(101)`

### 15. Updating one account without disturbing another

**Difficulty:** Intermediate

```python
acc1.balance = 1000
acc2.balance = 1000
acc1.balance = acc1.balance - 250
```

Which pair of balances remains after the update?

A. `acc1` has 750 and `acc2` has 750  
B. `acc1` has 750 and `acc2` has 1000  
C. `acc1` has 1000 and `acc2` has 750  
D. Both balances become undefined after reassignment

### 16. A partially prepared object reaches a report

**Difficulty:** Intermediate

```python
class Student:
    pass

meera = Student()
meera.roll_number = 103
print(meera.name)
```

Which incident classification matches the last line?

A. `KeyError`, because `name` was not used as a dictionary key  
B. It displays an empty string because Python automatically supplies defaults for every missing object attribute  
C. `NameError`, because `meera` stops existing after assignment  
D. `AttributeError`, because this object was never given a `name` attribute

### 17. Replacing an existing attribute value

**Difficulty:** Intermediate

An object begins with `ticket.status = "Open"`. After the issue is resolved, which statement changes only that object's existing status?

A. `Ticket("Closed")`  
B. `ticket.status = "Closed"`  
C. `status.ticket("Closed")`  
D. `class ticket.status = "Closed"`

### 18. Preventing incomplete objects rather than detecting them later

**Difficulty:** Advanced

A program creates fifty student objects and then manually assigns `name`, `roll_number`, and `marks` in three separate lines for each one. Missing one line causes a delayed `AttributeError`. Which structural repair addresses the source of the defect?

A. Require those values in `__init__` and assign them to `self` during creation  
B. Catch every later `AttributeError` and continue with a blank report  
C. Add a fourth parallel list recording which assignments were forgotten  
D. Sort the objects before reading their attributes

### 19. Placing behaviour on the blueprint

**Difficulty:** Foundational

A `Student` object should answer whether its own marks meet the pass boundary. Which class member has the correct basic method shape?

A. `has_passed(self) = self.marks >= 40`  
B. `method has_passed(): return marks >= 40`  
C. `def has_passed(): return self.marks >= 40  # self is available automatically`  
D. `def has_passed(self): return self.marks >= 40`

### 20. The same method serves different objects

**Difficulty:** Intermediate

```python
class Student:
    def result(self):
        return self.marks >= 40

asha.marks = 78
ravi.marks = 32
```

Which pair follows from `asha.result()` and `ravi.result()`?

A. Both calls return `True` because the method is shared  
B. Both calls return `False` because `marks` is outside the method  
C. The calls return `True` and `False`, using each calling object's marks  
D. The first call permanently changes the shared method, forcing the second call to use Asha's marks

### 21. A method definition leaves no place for the object argument

**Difficulty:** Intermediate

```python
class Greeter:
    def welcome():
        return "Welcome"

guest = Greeter()
message = guest.welcome()
```

Which explanation matches the failed call?

A. Python supplies `guest` automatically, but `welcome` has no parameter to receive it  
B. Methods are required to print a message rather than return one  
C. The class must contain an attribute before it may contain a method  
D. `welcome` can only be called by writing `Greeter.welcome()` because methods never receive an object automatically

### 22. Supplying a method's ordinary argument

**Difficulty:** Intermediate

```python
class Account:
    def can_withdraw(self, amount):
        return amount <= self.balance

acc.balance = 500
allowed = acc.can_withdraw(450)
```

How are the two parameters supplied during the call?

A. `450` becomes `self`, and `amount` remains missing  
B. Both `self` and `amount` receive the value `450`  
C. The caller must pass `acc` again after `450`, because Python supplies neither method parameter automatically  
D. Python supplies `acc` as `self`, and `450` becomes `amount`

### 23. One method reuses another method's decision

**Difficulty:** Intermediate

```python
class Student:
    def has_passed(self):
        return self.marks >= 40

    def report(self):
        return "Pass" if self.has_passed() else "Fail"
```

Which detail makes `report` evaluate the same student's marks?

A. `has_passed` becomes a global function when `report` begins  
B. Python copies `marks` into every local variable named `self`  
C. `self.has_passed()` calls the method on the current object  
D. The conditional expression ignores the result of `has_passed`

### 24. A rename method updates a temporary name

**Difficulty:** Advanced

```python
class Student:
    def rename(self, new_name):
        name = new_name
```

Calling `asha.rename("Asha Rao")` leaves `asha.name` unchanged. Which smallest repair makes the method update the object's attribute?

A. Replace the body with `new_name = name`  
B. Replace the body with `self.name = new_name`  
C. Call the method as `asha.rename(self, "Asha Rao")`  
D. Move `name = new_name` outside the class

### 25. Setup occurs without a separate method call

**Difficulty:** Foundational

```python
class Device:
    def __init__(self):
        self.status = "offline"

router = Device()
```

Which statement describes the state immediately after the last line?

A. `router.status` is missing until `router.__init__()` is called manually  
B. The class stores `"offline"`, but the object does not  
C. `router.status` is `"offline"` because `__init__` ran automatically  
D. `router` contains only a method and cannot hold data

### 26. Constructor arguments are stored on the correct instance

**Difficulty:** Intermediate

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

learner = Student("Kabir", 84)
```

Which state belongs to `learner`?

A. `name` is 84 and `marks` is `"Kabir"`  
B. `name` is `"Kabir"` and `marks` is 84  
C. Both attributes contain the complete argument tuple  
D. The arguments disappear because the constructor returns nothing

### 27. Creation is blocked when required data is absent

**Difficulty:** Intermediate

```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

record = Student("Leela", 108)
```

Which result protects the program from receiving an incomplete object?

A. The object is created with `marks` equal to zero  
B. Python stores `None` for the missing attribute  
C. The constructor skips all assignments and returns an empty object  
D. A `TypeError` reports the missing required `marks` argument

### 28. A new account uses the standard opening balance

**Difficulty:** Intermediate

```python
class Account:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
```

Which call creates Neha's account with the declared default balance?

A. `neha = Account("Neha")`  
B. `neha = Account(balance="Neha")`  
C. `neha = Account()`  
D. `neha = Account(0, "Neha")`

### 29. A constructor reads an attribute before creating it

**Difficulty:** Advanced

```python
class Student:
    def __init__(self, name):
        self.name = self.name
```

Instantiation fails because the right side requests an attribute that does not yet exist. Which minimal repair stores the supplied argument?

A. Change the body to `name = self.name`  
B. Remove the `name` parameter and keep the body  
C. Change the body to `self = name`  
D. Change the body to `self.name = name`

### 30. A nearly correct special-method name is never recognised

**Difficulty:** Advanced

```python
class Product:
    def _init_(self, price):
        self.price = price

item = Product(250)
```

Which repair restores automatic constructor behaviour?

A. Rename the class to `_Product_`  
B. Call `_init_` manually before creating `item`, then pass the unfinished object into `Product`  
C. Rename `_init_` to `__init__`, using two underscores on each side  
D. Replace `self.price` with a global variable

### 31. The exact pass boundary is tested

**Difficulty:** Foundational

```python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

student = Student(40)
```

Which decision does `student.has_passed()` return?

A. `True`, because the boundary includes 40  
B. `False`, because passing begins at 41  
C. `None`, because methods cannot return Boolean values  
D. The comparison fails because marks is an attribute

### 32. An accepted deposit is followed by a rejected withdrawal

**Difficulty:** Foundational

An account begins with 500. Its `deposit` method adds 200. Its `withdraw` method changes the balance only when the requested amount does not exceed the current balance. A withdrawal of 800 is then attempted. Which balance remains?

A. `-100`  
B. `700`  
C. `500`  
D. `1500`

### 33. Transactions stay with the account that receives them

**Difficulty:** Intermediate

`primary` and `savings` are separate `BankAccount` objects, each starting at 1000. The program calls `primary.withdraw(300)` and then `savings.deposit(50)`. Which state is consistent with independent objects?

A. Both balances become 750 because they share the class  
B. `primary` becomes 1050 and `savings` becomes 700  
C. `primary` becomes 700 and `savings` becomes 1050  
D. Both balances remain 1000 because methods cannot change attributes

### 34. A report coordinates two existing decisions

**Difficulty:** Intermediate

A `Student.report()` method needs the results already provided by `has_passed()` and `grade()`. Which implementation avoids duplicating both rules?

A. Call `self.has_passed()` and `self.grade()` while constructing the report  
B. Recalculate every grade boundary inside `report` and stop using the other methods  
C. Create a new `Student` object inside `report` to obtain fresh values  
D. Read global variables named `has_passed` and `grade`

### 35. Withdrawing the full balance is rejected by one character

**Difficulty:** Advanced

```python
def withdraw(self, amount):
    if amount >= self.balance:
        return "Insufficient"
    self.balance -= amount
    return "Accepted"
```

The policy allows an account to withdraw exactly its current balance. Which smallest repair implements that boundary correctly?

A. Change the condition to `amount < self.balance`  
B. Change the condition to `amount > self.balance`  
C. Change the subtraction to `self.balance += amount`  
D. Remove the condition and accept every request

### 36. A deposit method changes the wrong account

**Difficulty:** Advanced

```python
class Account:
    def deposit(self, amount):
        main_account.balance += amount

main_account = Account()
savings = Account()
main_account.balance = 100
savings.balance = 400
savings.deposit(50)
```

The call is intended to update whichever account receives it. Which repair achieves that behaviour?

A. Replace the body with `amount += main_account.balance`  
B. Pass `main_account` manually whenever `savings.deposit` is called  
C. Move both balances into one global variable shared by the objects  
D. Replace the body with `self.balance += amount`

### 37. A single daily count needs no personal behaviour

**Difficulty:** Foundational

The help desk only needs to store today's visitor count, `47`, and perform ordinary arithmetic with it. Which representation is most appropriate?

A. A plain numeric variable  
B. A `VisitorCount` class with a constructor and four methods  
C. One object per visitor even though no visitor details are stored  
D. Two parallel lists containing the same count

### 38. Fixed coordinates carry facts but no actions

**Difficulty:** Foundational

A map marker is represented only by latitude and longitude. The pair has no custom behaviour or rule to enforce. Which structure is a proportionate choice?

A. A class whose only method returns the same two values  
B. A dictionary of methods with no coordinate values  
C. A tuple such as `(17.3850, 78.4867)`  
D. Separate classes for latitude and longitude

### 39. Registration must protect an event's capacity

**Difficulty:** Intermediate

An event has a title, capacity, and current registrations. Every registration must be rejected once capacity is reached, and hundreds of events follow the same rule independently. Which model best fits?

A. Store only all event titles in one tuple  
B. Use unrelated variables and repeat the capacity condition at every registration call site in the application  
C. Keep a dictionary of capacities but omit registration behaviour  
D. Use an `Event` class with state and a registration method that enforces the limit

### 40. Choosing the point where a class earns its place

**Difficulty:** Advanced

Version A represents each student as a dictionary, while several screens independently implement pass, grade, and report rules. Version B uses `Student` objects with those operations as methods. The system will manage thousands of students and revise grading rules annually. Which judgment is most defensible?

A. Version A is preferable because repeated rules become safer as the number of screens grows  
B. Version B better centralises shared behaviour while each object retains its own student data  
C. Both designs are equivalent because a dictionary automatically supplies the same methods as a class  
D. Neither design can represent more than one student at a time

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | An object keeps one student's related facts together, removing dependence on synchronised positions. |
| 2 | A | Intermediate | OOP begins by identifying the meaningful entities whose data and behaviour belong together. |
| 3 | D | Intermediate | A class can keep the order's state and its shipping rule together instead of repeating behaviour across screens. |
| 4 | B | Advanced | A shared method gives the withdrawal policy one implementation point used by every account object. |
| 5 | D | Foundational | The general shape is a class, while the identified physical copy is one specific object. |
| 6 | B | Intermediate | One class can instantiate any number of separate objects, each with its own state. |
| 7 | C | Intermediate | The invoice number, date, and amount identify one concrete invoice rather than a general blueprint. |
| 8 | A | Advanced | Objects share their blueprint and methods, but instance attributes belong independently to each object. |
| 9 | B | Foundational | `class Sensor:` defines the class, and `pass` supplies a valid placeholder body. |
| 10 | D | Intermediate | Calling the class name constructs a new instance, which the assignment stores in `lab_sensor`. |
| 11 | A | Intermediate | Each class call creates a new object, so identity comparison with `is` returns `False`. |
| 12 | C | Intermediate | Python class names conventionally use CapitalisedWords, represented here by `BankAccount`. |
| 13 | A | Advanced | `second = first` creates an alias to the same object, while `third = Student()` creates a new object with no `name`. |
| 14 | C | Foundational | Dot assignment creates `roll_number` on the specific object referenced by `asha`. |
| 15 | B | Intermediate | Reassigning `acc1.balance` changes that object only; `acc2` retains its separate value. |
| 16 | D | Intermediate | Dot lookup raises `AttributeError` when the requested attribute was never attached to that object. |
| 17 | B | Intermediate | Assigning through `ticket.status` replaces the value on that particular ticket object. |
| 18 | A | Advanced | A constructor makes the required setup part of creation, preventing partially prepared objects. |
| 19 | D | Foundational | A method is a `def` inside the class and needs `self` first to access the calling object's attributes. |
| 20 | C | Intermediate | In each call, `self` refers to the object before the dot, so the two marks produce different Boolean results. |
| 21 | A | Intermediate | An object method call automatically passes the object, causing a `TypeError` when no first parameter exists. |
| 22 | D | Intermediate | Python supplies the calling object as `self`; the explicitly supplied 450 fills `amount`. |
| 23 | C | Intermediate | Calling through `self` keeps the delegated method on the current student object. |
| 24 | B | Advanced | The original assignment creates a local variable; dot assignment is needed to replace the instance attribute. |
| 25 | C | Foundational | Python invokes `__init__` during `Device()`, so the new object starts with the assigned status. |
| 26 | B | Intermediate | Constructor arguments bind by position and are stored by the two `self.attribute` assignments. |
| 27 | D | Intermediate | Omitting the required `marks` argument raises `TypeError` during construction instead of creating an incomplete object. |
| 28 | A | Intermediate | The holder is supplied and the omitted balance uses its declared default of zero. |
| 29 | D | Advanced | The right side must use the parameter `name`; the left side creates the object's `name` attribute. |
| 30 | C | Advanced | Python recognises the constructor only with the exact special name `__init__`. |
| 31 | A | Foundational | The `>=` operator includes 40 in the passing range. |
| 32 | B | Foundational | The deposit raises the balance to 700, and the excessive withdrawal leaves it unchanged. |
| 33 | C | Intermediate | Each method updates only its receiving object, leaving balances of 700 and 1050. |
| 34 | A | Intermediate | Calling the existing methods through `self` reuses their decisions for the same student. |
| 35 | B | Advanced | Only amounts greater than the balance should be rejected; an equal amount must reach the subtraction. |
| 36 | D | Advanced | `self` refers to the object that received the call, so the deposit updates `savings` in this scenario. |
| 37 | A | Foundational | A standalone number with no attached behaviour needs only a normal variable. |
| 38 | C | Foundational | A tuple is sufficient for a fixed group of related values with no custom behaviour. |
| 39 | D | Intermediate | A class lets every event retain independent state while reusing one capacity-enforcing registration method. |
| 40 | B | Advanced | The class centralises recurring rules for reuse while keeping every student's attribute values independent. |

---

## Topic coverage

| Unit 9 topic | Questions |
|---|---|
| Why OOP? Modeling Real-World Things | 1-4 |
| What is a Class? What is an Object? | 5-8 |
| Creating a Class and Instantiating Objects | 9-13 |
| Attributes (Instance Variables) | 14-18 |
| Methods and the `self` Parameter | 19-24 |
| The `__init__` Constructor | 25-30 |
| A Simple Class Walkthrough | 31-36 |
| Objects vs Plain Data: When to Use a Class | 37-40 |

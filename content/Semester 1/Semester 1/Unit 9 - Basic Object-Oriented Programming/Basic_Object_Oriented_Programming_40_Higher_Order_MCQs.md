# Unit 9: Basic Object-Oriented Programming - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 9 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led modelling, object-state tracing, implementation comparison, failure diagnosis, minimal repair, and design judgment
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option
- Opening coverage: Questions 1-10 collectively assess all five official Unit 9 taxonomy subtopics
- Metadata: every question identifies its taxonomy subtopic and assessment type

---

## Questions

### 1. One edit silently changes the identity of three records

**Difficulty:** Foundational

**Taxonomy:** python → object-oriented-programming-intro → object-oriented-programming  
**Is Curriculum Based:** No  
**Assessment type:** Applying a concept in a realistic situation

An office stores names, roll numbers, and attendance in three parallel lists. A transfer operation moves one name but not the matching values in the other lists. The program still runs, yet the next report combines facts from different students. Which redesign removes the dependency that caused the silent corruption?

A. Sort both lists independently before every report  
B. Add more comments explaining that the positions must match  
C. Represent each student as one object carrying its related data  
D. Convert the roll-number list into a tuple and keep the name list unchanged

### 2. Finding the boundaries before writing classes

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate programming structure

A repair service must remember who raised a ticket, which technician accepted it, and how each ticket's status changes. Before choosing attributes or methods, which proposed model identifies the most defensible object boundaries?

A. Identify `Customer`, `Technician`, and `Ticket` as candidate program entities  
B. Put every value into one long list, then document the position assigned to each field and entity  
C. Create one function for each individual customer by name  
D. Store all statuses in variables unrelated to their tickets

### 3. Two names may represent either one object or two

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the final value of a variable

Consider the following incident-reproduction code:

```python
class Parcel:
    pass

first = Parcel()
second = first
third = Parcel()
same_first_second = first is second
same_first_third = first is third
```

Which pair is stored in `same_first_second` and `same_first_third`?

A. `False, False`  
B. `True, True`  
C. `False, True`  
D. `True, False`

### 4. A method updates a temporary value instead of the object

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

An inventory test expects `item.reserve(3)` to reduce `item.stock` from 10 to 7, but the object remains unchanged:

```python
class Item:
    def reserve(self, amount):
        stock = self.stock - amount

item = Item()
item.stock = 10
item.reserve(3)
```

Which one-line replacement repairs the method without changing its interface?

A. `amount = self.stock - amount`  
B. `self.stock -= amount`  
C. `Item.stock = amount`  
D. `return stock - amount`

### 5. Construction succeeds only after a manual setup call

**Difficulty:** Foundational

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing code

A developer intends every new badge to receive its owner during creation, but the setup method is not recognised automatically:

```python
class Badge:
    def ______(self, owner):
        self.owner = owner

staff_badge = Badge("Meera")
```

Which exact method name completes the class so that the final line succeeds?

A. `_init_`  
B. `init`  
C. `__create__`  
D. `__init__`

### 6. A shared blueprint does not imply shared state

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

Two registrations are created from the same class:

```python
class Registration:
    pass

morning = Registration()
evening = Registration()
morning.seats = 20
evening.seats = 35
morning.seats -= 4
print(morning.seats, evening.seats)
```

Which console record should the tester expect?

A. `16 31`  
B. `16 35`  
C. `20 35`  
D. `31 31`

### 7. Choosing a model that owns both state and a rule

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct validation approach

A parking application manages hundreds of lots. Each lot has its own capacity and occupied count, and every entry attempt must be rejected when that particular lot is full. Which design places the validation where it can be reused without mixing the lots' state?

A. Keep all capacities in one list and let each screen edit occupancy directly  
B. Store each lot in a tuple and repeat the capacity check wherever an entry is recorded  
C. Give each `ParkingLot` object its own state and an `admit` method that enforces capacity  
D. Create one global Boolean named `has_space` and reuse it for every lot

### 8. A method accidentally consults the wrong student

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes a defect

A method is supposed to judge the object receiving the call, but it uses `asha.marks` instead of `self.marks`:

```python
class Student:
    def has_passed(self):
        return asha.marks >= 40
```

Which test data most clearly exposes the defect when the program evaluates `ravi.has_passed()`?

A. `asha.marks = 80` and `ravi.marks = 20`  
B. `asha.marks = 80` and `ravi.marks = 80`  
C. `asha.marks = 20` and `ravi.marks = 20`  
D. `asha.marks = 40` and `ravi.marks = 40`

### 9. Completing a blueprint without inventing behaviour

**Difficulty:** Foundational

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing code

A hardware team wants an intentionally empty `Sensor` blueprint so integration code can already create `Sensor()` objects. Which completion produces a valid class while adding no premature data or behaviour?

```python
class Sensor:
    ______
```

A. `Sensor = None`  
B. `pass`  
C. `def read(self): return None`  
D. `status = "unknown"`

### 10. A default constructor value is overridden once

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple object states

A dashboard creates two counters:

```python
class Counter:
    def __init__(self, value=0):
        self.value = value

left = Counter()
right = Counter(5)
left.value += 2
```

Which state is present after the final assignment?

A. `left.value == 0` and `right.value == 7`  
B. `left.value == 7` and `right.value == 7`  
C. `left.value == 5` and `right.value == 2`  
D. `left.value == 2` and `right.value == 5`

### 11. Two calls use the same empty class

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the final value of a variable

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

### 12. A valid declaration fails the team's class-name check

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

A valid declaration, `class bank_account:`, runs successfully but fails the project's class-naming check. The public name should remain the two words "bank account." Which header is the smallest convention-compliant repair?

A. `class Bank_Account:`  
B. `class BANKAccount:`  
C. `class BankAccount:`  
D. `class bankAccount:`

### 13. An alias is confused with a fresh instance

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → classes-and-objects  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected program behaviour

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing code

An empty `Student` object is stored in `asha`. Which statement attaches roll number 101 to that particular object?

A. `Student.roll_number = 101`  
B. `roll_number = 101`  
C. `asha.roll_number = 101`  
D. `asha = 101`

### 15. Updating one account without disturbing another

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple object states

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Handling a runtime failure

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Completing a state update

An object begins with `ticket.status = "Open"`. After the issue is resolved, which statement changes only that object's existing status?

A. `Ticket.status = "Closed"`  
B. `ticket.status = "Closed"`  
C. `status = "Closed"`  
D. `ticket = "Closed"`

### 18. Preventing incomplete objects rather than detecting them later

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct validation approach

A program creates fifty student objects and then manually assigns `name`, `roll_number`, and `marks` in three separate lines for each one. Missing one line causes a delayed `AttributeError`. Which structural repair addresses the source of the defect?

A. Require those values in `__init__` and assign them to `self` during creation  
B. Catch every later `AttributeError` and continue with a blank report  
C. Add a fourth parallel list recording which assignments were forgotten  
D. Sort the objects before reading their attributes

### 19. Placing behaviour on the blueprint

**Difficulty:** Foundational

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing method code

A `Student` object should answer whether its own marks meet the pass boundary. Which class member has the correct basic method shape?

A. `def has_passed(marks): return marks >= 40`  
B. `def has_passed(self): return marks >= 40`  
C. `def has_passed(self): result = self.marks >= 40`  
D. `def has_passed(self): return self.marks >= 40`

### 20. The same method serves different objects

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Handling a method-call failure

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Tracing argument binding

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Tracing delegated method calls

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the final value of an attribute

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Tracing constructor argument binding

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Handling a construction failure

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about default arguments

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

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

**Taxonomy:** python → object-oriented-programming-intro → constructors  
**Is Curriculum Based:** No  
**Assessment type:** Handling an unexpected construction failure

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

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an incorrect boundary condition

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

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Tracing successive method calls

An account begins with 500. Its `deposit` method adds 200. Its `withdraw` method changes the balance only when the requested amount does not exceed the current balance. A withdrawal of 800 is then attempted. Which balance remains?

A. `-100`  
B. `700`  
C. `500`  
D. `1500`

### 33. Transactions stay with the account that receives them

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple object states

`primary` and `savings` are separate `BankAccount` objects, each starting at 1000. The program calls `primary.withdraw(300)` and then `savings.deposit(50)`. Which state is consistent with independent objects?

A. Both balances become 750 because they share the class  
B. `primary` becomes 1050 and `savings` becomes 700  
C. `primary` becomes 700 and `savings` becomes 1050  
D. Both balances remain 1000 because methods cannot change attributes

### 34. Two reports agree today but age differently

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Deciding whether two implementations are equivalent

A class already provides `has_passed()` and `grade()`. Version A of `report()` calls those methods. Version B repeats their current conditions exactly inside `report()`. Tests over every integer mark from 0 through 100 currently produce identical reports. Which review conclusion is accurate?

A. Equivalent now; Version A is less likely to drift after a rule change  
B. They cannot be equivalent because one method is not allowed to call another method on the same object  
C. Version B is necessarily safer because copying a rule creates a second independent source of truth  
D. Version A evaluates another student's state whenever it calls through `self`

### 35. Withdrawing the full balance is rejected by one character

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an incorrect boundary condition

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

**Taxonomy:** python → object-oriented-programming-intro → attributes-and-methods  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a state-management defect

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

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate programming structure

The help desk only needs to store today's visitor count, `47`, and perform ordinary arithmetic with it. Which representation is most appropriate?

A. A plain numeric variable  
B. A `VisitorCount` class with a constructor and four methods  
C. One object per visitor even though no visitor details are stored  
D. Two parallel lists containing the same count

### 38. Fixed coordinates carry facts but no actions

**Difficulty:** Foundational

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate programming structure

A map marker is represented only by latitude and longitude. The pair has no custom behaviour or rule to enforce. Which structure is a proportionate choice?

A. A class whose only method returns the same two values  
B. A dictionary of methods with no coordinate values  
C. A tuple such as `(17.3850, 78.4867)`  
D. Separate classes for latitude and longitude

### 39. Registration must protect an event's capacity

**Difficulty:** Intermediate

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct validation approach

An event has a title, capacity, and current registrations. Every registration must be rejected once capacity is reached, and hundreds of events follow the same rule independently. Which model best fits?

A. Store only all event titles in one tuple  
B. Use unrelated variables and repeat the capacity condition at every registration call site in the application  
C. Keep a dictionary of capacities but omit registration behaviour  
D. Use an `Event` class with state and a registration method that enforces the limit

### 40. Choosing the point where a class earns its place

**Difficulty:** Advanced

**Taxonomy:** python → object-oriented-programming-intro → modeling-with-classes  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two code implementations

Version A represents each student as a dictionary, while several screens independently implement pass, grade, and report rules. Version B uses `Student` objects with those operations as methods. The system will manage thousands of students and revise grading rules annually. Which judgment is most defensible?

A. Version A is preferable because repeated rules become safer as the number of screens grows  
B. Version B better centralises shared behaviour while each object retains its own student data  
C. Both designs are equivalent because a dictionary automatically supplies the same methods as a class  
D. Neither design can represent more than one student at a time

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | Bundling each student's related state in one object removes the positional dependency that allowed the parallel collections to drift. |
| 2 | A | Intermediate | `Customer`, `Technician`, and `Ticket` are the meaningful entities whose separate state and behaviour the service must model. |
| 3 | D | Intermediate | Assignment makes `second` an alias of `first`, while the second call to `Parcel()` creates the distinct object referenced by `third`. |
| 4 | B | Advanced | Assigning through `self.stock` changes the attribute of the object that received the method call; the original line only created a local variable. |
| 5 | D | Foundational | Python invokes only the exact special method name `__init__` automatically while processing `Badge("Meera")`. |
| 6 | B | Intermediate | The subtraction changes only `morning.seats`; the independent `evening` object retains 35. |
| 7 | C | Intermediate | Each object keeps one lot's state, while one shared method consistently checks that lot's capacity before changing occupancy. |
| 8 | A | Advanced | Ravi should fail with 20, but the defective method reads Asha's 80 and returns `True`; equal-side test values would conceal the wrong reference. |
| 9 | B | Foundational | `pass` is a valid placeholder statement in a class body and adds no data or behaviour. |
| 10 | D | Intermediate | The omitted argument gives `left` zero before its increment to two, while `right` keeps its explicitly supplied value of five. |
| 11 | A | Intermediate | Each class call creates a new object, so identity comparison with `is` returns `False`. |
| 12 | C | Intermediate | Python class names conventionally use CapitalisedWords, represented here by `BankAccount`. |
| 13 | A | Advanced | `second = first` creates an alias to the same object, while `third = Student()` creates a new object with no `name`. |
| 14 | C | Foundational | Dot assignment creates `roll_number` on the specific object referenced by `asha`; the alternatives modify another namespace or replace the reference. |
| 15 | B | Intermediate | Reassigning `acc1.balance` changes that object only; `acc2` retains its separate value. |
| 16 | D | Intermediate | Dot lookup raises `AttributeError` when the requested attribute was never attached to that object. |
| 17 | B | Intermediate | Assigning through `ticket.status` replaces that object's value; a class attribute, standalone variable, or replaced reference does not perform the requested update. |
| 18 | A | Advanced | A constructor makes the required setup part of creation, preventing partially prepared objects. |
| 19 | D | Foundational | The correct method receives the object as `self`, reads its attribute, and explicitly returns the Boolean result. |
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
| 34 | A | Intermediate | Matching conditions make the versions equivalent over the stated marks today, but delegation avoids a duplicate rule that can diverge after a policy change. |
| 35 | B | Advanced | Only amounts greater than the balance should be rejected; an equal amount must reach the subtraction. |
| 36 | D | Advanced | `self` refers to the object that received the call, so the deposit updates `savings` in this scenario. |
| 37 | A | Foundational | A standalone number with no attached behaviour needs only a normal variable. |
| 38 | C | Foundational | A tuple is sufficient for a fixed group of related values with no custom behaviour. |
| 39 | D | Intermediate | A class lets every event retain independent state while reusing one capacity-enforcing registration method. |
| 40 | B | Advanced | The class centralises recurring rules for reuse while keeping every student's attribute values independent. |

---

## Taxonomy coverage

| Subject | Topic | Subtopic | Questions | Is Curriculum Based |
|---|---|---|---|:---:|
| python | object-oriented-programming-intro | object-oriented-programming | 1 | No |
| python | object-oriented-programming-intro | classes-and-objects | 3, 6, 9, 11-13 | No |
| python | object-oriented-programming-intro | attributes-and-methods | 4, 8, 14-17, 19-24, 36 | No |
| python | object-oriented-programming-intro | constructors | 5, 10, 18, 25-30 | No |
| python | object-oriented-programming-intro | modeling-with-classes | 2, 7, 31-35, 37-40 | No |

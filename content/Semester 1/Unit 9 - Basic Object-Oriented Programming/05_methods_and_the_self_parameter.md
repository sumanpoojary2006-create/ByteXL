## Introduction

Priya keeps writing the same little calculation by hand outside her `Student` objects: comparing `marks` to 40 to decide pass or fail, for every single student, every time. A real student does not just passively hold a mark; in a sense, a student "knows" whether they have passed, and Priya would like to simply ask the object that question directly, the way you would ask a real person, rather than recomputing it herself from outside every time.

A **method** is a function defined inside a class, an action that belongs to its objects and can use their attributes directly. This lesson introduces methods, and the special first parameter, `self`, that every method needs in order to know exactly which object it is working on.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/05_method_asks_object_directly.png)

## Defining a Method Inside a Class

A method is written exactly like a function, with `def`, indented one level inside the class body.

```python
class Student:
    def greet(self):
        print("Hello, I am a student.")

asha = Student()
asha.greet()    # Hello, I am a student.
```

Calling `asha.greet()` looks just like calling any method you have used before, `"text".upper()` or `my_list.append(...)`, because that is exactly what a method call always was: dot notation reaching an action that belongs to the object on the left of the dot.

## The self Parameter: Which Object Is This?

Every method needs a first parameter, conventionally named `self`, which automatically refers to the specific object the method was called on. You never pass it yourself; Python supplies it automatically the moment you write `asha.greet()`.

```python
class Student:
    def greet(self):
        print(f"Hello, I am {self.name}.")

asha = Student()
asha.name = "Asha"
asha.greet()    # Hello, I am Asha.

ravi = Student()
ravi.name = "Ravi"
ravi.greet()    # Hello, I am Ravi.
```

The very same method, written once, prints a different name depending on which object called it, because `self` inside `greet` automatically refers to whichever object sits before the dot at the call site: `asha` in the first call, `ravi` in the second.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/05_self_routes_to_object.png)


## What Happens If You Forget self

Leaving `self` out of a method's definition causes a confusing error the moment that method is actually called on an object, because Python always supplies the calling object as the first argument, whether the method asked for it or not.

```python
class Student:
    def greet():               # missing self!
        print("Hello!")

asha = Student()
try:
    asha.greet()    # error!
except TypeError as e:
    print(f"TypeError: {e}")
    print("Python passed asha as the first argument, but greet() had no self to receive it.")
```

This raises a `TypeError` complaining that `greet()` takes 0 positional arguments but 1 was given, because Python quietly passed `asha` itself as an argument, and `greet` had no parameter ready to receive it. Every method you write needs `self` as its first parameter, with no exceptions, even if that particular method never ends up using it.

## A Method Using self to Read and Reason

Now Priya can finally write the "have I passed" logic directly on the object, using `self` to reach its own attributes.

```python
class Student:
    def has_passed(self):
        return self.marks >= 40

asha = Student()
asha.marks = 72
print(asha.has_passed())    # True

ravi = Student()
ravi.marks = 30
print(ravi.has_passed())    # False
```

`self.marks` reaches whichever object's `marks` attribute is relevant to that particular call, exactly the same way `self.name` did in the `greet` example. The method's logic is written once, on the class, and it correctly judges every object built from that class using that object's own data.

## Calling One Method From Another

Methods on the same object can call each other through `self`, exactly the way ordinary functions can call each other.

```python
class Student:
    def has_passed(self):
        return self.marks >= 40

    def report(self):
        result = "Pass" if self.has_passed() else "Fail"
        print(f"{self.name}: {result}")

asha = Student()
asha.name = "Asha"
asha.marks = 72
asha.report()    # Asha: Pass
```

`report` reaches `has_passed` through `self.has_passed()`, exactly the dot-notation pattern used everywhere else, because one method calling another belonging to the same object is still just calling a method on `self`.

## Methods and self at a Glance

| Idea | Detail |
|---|---|
| A method | A function defined inside a class, indented in its body |
| The first parameter | Always `self`, supplied automatically by Python |
| What `self` refers to | Whichever object the method was actually called on |
| Calling it | `object.method()`, never passing `self` manually |

## Your Turn: A Method That Reasons About the Object

```python
class BankAccount:
    def can_withdraw(self, amount):
        return amount <= self.balance

acc = BankAccount()
acc.balance = 3000

print(acc.can_withdraw(2000))    # True
print(acc.can_withdraw(5000))    # False
```

Notice `can_withdraw` takes a second parameter, `amount`, alongside the required `self`, exactly the way an ordinary function can take more than one parameter; `self` simply always comes first.

## Conclusion

A method is a function defined inside a class, and its first parameter, always named `self` by convention, automatically refers to whichever object the method was called on, letting the same method's logic correctly use each object's own attributes. Forgetting `self` causes a `TypeError` the moment the method is actually called, because Python always supplies the calling object as an argument regardless. With data and behaviour finally living together on the same object, the next lesson removes the last fragile part of this picture: setting up an object's attributes by hand, one at a time, after it is created.

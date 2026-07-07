## Introduction

Priya's office has a printed registration form template: blank lines for a name, a roll number, a department. The blank template itself is not any particular student; nobody named "Name: ___________" ever walked through the door. The moment Priya fills one in with "Asha, 101, Computer Science," it becomes a real, specific record. The same template gets photocopied and filled in differently for Ravi, for Meera, and for every student who registers.

That blank template and its many filled-in copies are exactly the relationship between Python's two central OOP ideas: the **class**, a blueprint describing what a kind of thing looks like, and the **object**, one specific, filled-in instance built from that blueprint.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/02_class_blueprint_object_copies.png)

## A Class Is a Blueprint

A class describes the shape of a thing: what data it will carry, and what it will be able to do, without referring to any one specific example of it. "A student has a name, a roll number, and an attendance record" is a description of the blueprint, not a description of Asha specifically. You will see the exact Python syntax for writing one in the very next lesson; for now, hold onto the idea itself.

## An Object Is One Specific Instance

An object, also called an instance, is one particular thing built from a class's blueprint, with its own actual values filled in. Asha is an object built from the Student blueprint, with her own specific name, roll number, and attendance. Ravi is a different object, built from the very same blueprint, with his own different values.

## The Cookie Cutter Analogy

If a class is a cookie cutter, an object is one actual cookie. The cutter defines the shape every cookie made from it will share, round, with a star pattern, a certain size, but the cutter itself is not edible and cannot be eaten. Each cookie pressed out from it is a separate, real thing, and you can press out as many cookies as you like from the same cutter, each one independent of the others, even though they all share the same shape.

## One Blueprint, Many Independent Objects

This is the relationship worth sitting with before any syntax arrives: many different objects can come from the very same class, and changing one object never affects another, even though they were built from an identical blueprint.

| Concept | Cookie Cutter Analogy | Priya's Office |
|---|---|---|
| Class | The cutter itself, defining the shape | "Student": has a name, roll number, attendance |
| Object | One actual cookie pressed from the cutter | Asha, a specific student with her own values |
| Many objects, one class | Dozens of cookies from one cutter | Asha, Ravi, and Meera, all built from "Student" |
| Independence | Eating one cookie does not affect another | Changing Asha's attendance never touches Ravi's |

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/02_blueprint_instance_independence.png)


## Class vs Object at a Glance

| | Class | Object |
|---|---|---|
| What it is | A blueprint or template | A specific instance built from a blueprint |
| How many exist | Usually one, written once | As many as you create |
| Holds actual values? | No, it describes what values will look like | Yes, its own specific values |
| Example | `Student` | `asha`, `ravi`, `meera` |

## Your Turn: Class or Object?

Before any code, just decide which word fits each description:

1. "A bank account has a balance and an account holder's name." Is this describing a class or an object?
2. "Ravi's savings account, with a balance of 5000." Is this describing a class or an object?
3. "A book has a title, an author, and a number of pages." Class or object?
4. "The copy of *Wings of Fire* on Priya's desk, written by Abdul Kalam." Class or object?

The odd-numbered descriptions describe a shape with no specific values filled in, which makes them classes. The even-numbered ones name one actual, specific thing with real values, which makes them objects.

## Conclusion

A class is a blueprint describing the shape of a kind of thing, what data and behaviour it will have, without referring to any specific example, while an object is one actual instance built from that blueprint, carrying its own real values. Many independent objects can be created from the very same class, exactly the way many cookies come from one cutter, and changing one object never touches another. With the vocabulary settled, the next lesson finally writes the Python syntax for defining a class and creating objects from it.

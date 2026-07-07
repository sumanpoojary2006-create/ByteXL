## Introduction

Priya's three empty `Student` objects from the last lesson are, right now, just as blank as her photocopied registration forms before anyone fills them in. She needs to actually write Asha's name onto Asha's object, Ravi's name onto Ravi's object, and have each one remember its own details independently, the same way a filled-in form holds one specific student's information without affecting any other form.

The pieces of data that belong to a specific object are called its **attributes**, also known as **instance variables**, and this lesson covers how to attach them, read them, and trust that each object keeps its own separate copy.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/04_each_object_own_attributes.png)

## Attaching an Attribute to an Object

You attach an attribute to an object with dot notation: the object's name, a dot, the attribute's name, and an assignment.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-04-attributes-001-0f44233e3c.html"
 width="100%"
></iframe>

Reading `asha.name` afterward is exactly the dot notation you already used for string and list methods, except here the dot is reaching an attached piece of data rather than calling a method.

## Each Object Keeps Its Own Attributes

This is the single most important idea in this lesson. Attributes belong to one specific object, not to the class itself, so two objects of the same class can hold entirely different values without ever interfering with each other.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-04-attributes-002-8cc3acfd49.html"
 width="100%"
></iframe>

Changing `ravi.name` never touched `asha.name`, exactly the independence the cookie cutter analogy promised. This is precisely the bug Priya kept risking with parallel lists, one record accidentally drifting onto another, and an attribute attached directly to its own object simply cannot drift like that.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/04_attribute_name_value_slots.png)


## Attributes Set Outside the Class Are Fragile

Notice something slightly uncomfortable about the code so far: nothing forces every `Student` object to actually have a `name` or `roll_number`. Forget to set one, and reading it raises an error rather than showing a sensible default.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-04-attributes-003-45efa03508.html"
 width="100%"
></iframe>

This raises an `AttributeError`, because `meera` was never given a `name` attribute at all; unlike a dictionary's `.get()`, there is no safe fallback here by default. This fragility, that an object's shape depends entirely on remembering to set every attribute by hand, is exactly the gap the next-but-one lesson's constructor closes.

## Reading and Changing an Attribute

Once an attribute exists, you can read it freely, and reassign it exactly like any other variable, with the new value simply replacing the old one on that specific object.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-04-attributes-004-0d33d40f19.html"
 width="100%"
></iframe>

## Attributes at a Glance

| Action | Syntax | Notes |
|---|---|---|
| Attach an attribute | `obj.attribute = value` | Creates it if it does not exist yet |
| Read an attribute | `obj.attribute` | Raises `AttributeError` if never set |
| Change an attribute | `obj.attribute = new_value` | Overwrites the previous value on that object |
| Independence | Each object's attributes are separate | Changing one object never affects another |

## Your Turn: Two Independent Accounts

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-9-basic-object-oriented-programming-04-attributes-005-9296d11cb9.html"
 width="100%"
></iframe>

Confirm for yourself that withdrawing from `acc1` never disturbed `acc2`'s balance at all, exactly the separation attributes are designed to guarantee.

## Conclusion

An attribute is a piece of data attached to one specific object using dot notation, `obj.attribute = value`, and every object of a class keeps its own independent set of attributes, so changing one never affects another. Setting attributes by hand after creating an object works, but it is fragile, since nothing guarantees every object actually gets every attribute it needs, and reading a missing one raises an `AttributeError`. Before fixing that fragility, the next lesson introduces methods, the functions that belong to a class and act on an object's attributes directly.

## Introduction

Naveen writes a function that calculates a `total` inside it, and right after calling that function, he tries to print `total` at the top level of his script, expecting to see the number the function just worked out. Python tells him `total` does not exist at all. He is certain he saw it being calculated; the function printed it just fine from inside. So why does the very same name vanish the moment the function finishes?

The answer is **scope**: the region of a program where a particular variable name is actually visible. A variable created inside a function belongs to that function alone, and Python decides what a name refers to by checking a small, fixed sequence of places, known as the **LEGB rule**.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/10_local_scope_boundary.png)

## Local Scope: Variables Belong to Their Function

A variable assigned inside a function is **local** to that function. It is created when the function runs and disappears the moment the function finishes.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-001-3768cc96ad.html"
 width="100%"
></iframe>

The function's own `print` works fine, because `total` exists while the function is running. The line after the call fails with a `NameError`, because that same `total` was local, and it was gone the instant `calculate_total` returned.

## Global Scope: Variables Belong to the Whole File

A variable assigned at the top level of your script, outside any function, is **global**, and it is visible everywhere, including inside every function that comes after it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-002-92e0a5e1ed.html"
 width="100%"
></iframe>

`add_tax` never received `tax_rate` as a parameter, yet it can read it directly, because a function can always read a global variable. Reading a global is fine and common; the trouble starts the moment a function tries to change one.

## Trying to Change a Global From Inside a Function

Assigning to a name inside a function, even one that shares its name with a global variable, creates a brand new local variable instead of changing the global one.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-003-fb7178eab1.html"
 width="100%"
></iframe>

This actually raises an error, because Python sees the assignment to `counter` anywhere in the function and decides, before the function even runs, that `counter` is local to that function. That makes the right-hand side, `counter + 1`, try to read a local `counter` that has not been given a value yet.

## The global Keyword: Asking to Change It Anyway

If a function genuinely needs to modify a global variable, the `global` keyword tells Python to use the outer variable instead of creating a new local one.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-004-f15db03a0b.html"
 width="100%"
></iframe>

This works now, but treat `global` as a tool to reach for rarely and deliberately. A function that quietly changes variables outside itself is harder to reason about than one that simply takes input and returns output, which is exactly the pattern this whole unit has been building toward.

## The LEGB Rule: How Python Finds a Name

When your code refers to a name, Python searches four scopes, in this exact order, and stops at the first match: **L**ocal (inside the current function), **E**nclosing (an outer function, if this one is nested inside it), **G**lobal (the top level of the file), and **B**uilt-in (names Python itself provides, like `len` or `print`).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-005-f93c4942e5.html"
 width="100%"
></iframe>

Each `print(value)` finds the nearest matching `value` to where it is written, exactly following the L-E-G-B order, never looking further out than it has to.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/10_legb_lookup_path.png)


## Scope at a Glance

| Scope | Where It Lives | Visible From |
|---|---|---|
| Local | Inside one function | Only that function |
| Enclosing | An outer function, for a nested function | The nested function and the outer one |
| Global | The top level of the script | Everywhere, including inside functions |
| Built-in | Python itself | Everywhere, unless shadowed by a closer name |

## Your Turn: Watch Scope in Action

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-006-8c16b748e6.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-10-variable-scope-and-the-legb-rule-007-d5b2705ee3.html"
 width="100%"
></iframe>

The second block confirms what the first one quietly relied on: `charge_member` read the global `fee` freely, but its own local `total` never escaped back out. Catching this `NameError` gracefully with `try`/`except` is a tool for a later unit; for now, simply recognizing why it happens is the point.

## Conclusion

A variable assigned inside a function is local and disappears once the function finishes; a variable assigned at the top level is global and readable from anywhere, though changing a global from inside a function needs the explicit `global` keyword, a tool to use sparingly. Python resolves every name by the LEGB rule, checking Local, then Enclosing, then Global, then Built-in scope, stopping at the first match. Understanding scope explains exactly why functions are such reliable, self-contained building blocks. The next lesson puts that reliability to a real test: a function that calls itself.

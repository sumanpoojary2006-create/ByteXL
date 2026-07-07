## Introduction

Naveen is ready to stop copy-pasting and actually write his bill-splitting logic as a proper, reusable function, the way the last lesson previewed. Before he can do that comfortably, he needs the exact rules: what keyword starts a function, what makes Python treat a block as belonging to that function, and how do you actually run it once it exists. None of this is new machinery. It is the same `def`-a-block, indent-the-body pattern you already trust from `if` statements and loops, just with a new keyword at the front.

This lesson is entirely about those rules: **defining** a function once, and **calling** it as many times as you like afterward.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/02_define_once_call_many.png)

## Defining a Function

A function definition starts with the keyword `def`, followed by a name, parentheses, and a colon, with the function's body indented underneath, exactly like an `if` block.

```text
def greet_member():
    print("Welcome to the hostel committee!")
```

Reading this line by line: `def` announces "a function is being defined here." `greet_member` is the name Naveen chose, following the same snake_case naming rules you already know for variables. The empty parentheses mean this particular function takes no input for now. The colon and the indentation mark everything that belongs to the function, exactly as they marked everything belonging to an `if`.

## Defining Does Not Run It

Here is the detail that catches every beginner once. Running the block above prints nothing at all.

```python
def greet_member():
    print("Welcome to the hostel committee!")

print("Script finished.")
```

Output:

```
Script finished.
```

The `print` inside `greet_member` never ran, because defining a function only teaches Python the recipe; it does not follow the recipe. A function's body only executes when the function is actually called.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/02_define_does_not_run_call_button.png)


## Calling a Function

To run a function's body, write its name followed by parentheses, exactly the way you have been calling `print()` and `len()` all course.

```python
def greet_member():
    print("Welcome to the hostel committee!")

greet_member()
```

Output:

```
Welcome to the hostel committee!
```

Now the body runs, because `greet_member()`, with the parentheses, is an instruction to actually execute the function, not just refer to it.

## Calling It as Many Times as You Like

The entire point of defining a function once is that you can call it from many places, as many times as you like, without retyping its body.

```python
def greet_member():
    print("Welcome to the hostel committee!")

greet_member()
greet_member()
greet_member()
```

Three calls, three identical greetings, and the body itself was only ever written once. This is precisely the reuse the last lesson promised: one definition, unlimited calls.

## A Function Must Be Defined Before It Is Called

Python reads your file from top to bottom, so a function must be defined before the line that calls it, or Python will not yet know the name.

```python
try:
    say_hello()        # error! say_hello is not defined yet
except NameError as e:
    print(f"NameError: {e}")
    print("Python had not reached the def yet when it hit the call.")

def say_hello():
    print("Hello!")
```

This raises a `NameError`, complaining that `say_hello` does not exist, because Python had not reached its definition yet when it hit the call. Swapping the two blocks, definition first, then call, fixes it immediately.

## Defining vs Calling at a Glance

| Action | Syntax | What Happens |
|---|---|---|
| Define | `def name():` then an indented body | Teaches Python the recipe; nothing runs yet |
| Call | `name()` | Actually runs the body, right now |
| Call again | `name()` a second time | Runs the same body again, from the same definition |

## Your Turn: Define and Call

```python
def print_separator():
    print("--------------------")

print_separator()
print("Mess Bill Report")
print_separator()
print("Total: 1200")
print_separator()
```

Run this and watch the same small function dividing up a tidy report, called three times from three different points, with its body written only once.

## Conclusion

A function is defined with `def name():` and an indented body, but that body only runs once the function is actually called by writing its name followed by parentheses: `name()`. Defining a function teaches Python the recipe; calling it follows the recipe, and you can call the same recipe as many times as you need. Every function you have called so far has taken no input and given nothing back; the next lesson opens up both directions, letting you hand information in and get a result out.

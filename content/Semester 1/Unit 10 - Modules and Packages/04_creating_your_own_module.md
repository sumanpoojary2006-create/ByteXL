## Introduction

Naveen is finally ready to do what the first lesson of this unit only previewed: actually pull his bill-splitting functions out of his giant script and into their own proper module, then import them from somewhere else. There is no special command to "create a module." There is no new syntax at all, in fact. The entire trick is simply saving a `.py` file in the right place and importing it by its filename, without the `.py` extension.

This lesson walks through that, file by file, exactly the way Naveen would do it on his own laptop.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/04_two_files_same_folder.png)

## Step One: Write the Module File

Naveen creates a new file named `billing.py`, in the same folder as his main script, containing only the functions that belong together.

```python
# billing.py
def split_cost(total, people, service_charge=0):
    """Split a total cost evenly among people, with an optional service charge."""
    return (total + service_charge) / people

def add_late_fee(amount, rate=0.05):
    """Apply a late fee, expressed as a decimal rate, to an amount."""
    return amount * (1 + rate)

# Demo:
result = split_cost(1200, 4, service_charge=100)
print(f"split_cost(1200, 4, service_charge=100) -> {result}")
result = add_late_fee(500, rate=0.05)
print(f"add_late_fee(500, rate=0.05) -> {result}")
```

This file does nothing on its own when it is run directly; it simply defines two functions and stops. That is exactly the point. A module's job is to be imported, not to be the main script itself.

## Step Two: Import It From Another File

In a second file, `main.py`, saved in that very same folder, Naveen imports `billing` exactly the way he would import `math` or `random`.

```python
# First we save billing.py (Step One) so this main.py example can run.
billing_code = '''
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people

def add_late_fee(amount, rate=0.05):
    return amount * (1 + rate)
'''
with open("billing.py", "w") as f:
    f.write(billing_code)

# main.py, in the same folder as billing.py
import billing

mess_share = billing.split_cost(1200, 4)
print("Each person owes:", mess_share)

late_amount = billing.add_late_fee(300)
print("With late fee:", late_amount)
```

Notice the module name used in `import billing` is just `billing`, the filename with the `.py` removed, and every function inside it is reached through `billing.` exactly as `math.sqrt` reached a function inside `math`.

## The Folder Layout That Makes This Work

```
my_project/
    billing.py
    main.py
```

Python looks for a module being imported in the same folder as the script doing the importing, among a few other places. As long as `billing.py` and `main.py` sit side by side like this, `import billing` inside `main.py` finds it without any extra configuration.

## A Module Can Be Run Directly, Too

Because a module is just a `.py` file, nothing stops you from running it on its own as well, separately from importing it.

```python
# billing.py
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people

print(split_cost(1000, 5))    # runs immediately if billing.py itself is executed
```

The catch is that this `print` line would also run every single time `billing` is imported from anywhere else, which is rarely what you actually want from a module meant to be reused quietly. The next lesson on packages, and good practice generally, favours keeping a module's top level limited to definitions, saving any "run this directly" code for the script that does the importing.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/04_name_main_guard.png)


## Naming Your Module File

A module's name follows the exact same snake_case convention as a variable or function: lower case words, separated by underscores, descriptive of what it contains. `billing.py`, `trip_planner.py`, and `receipt_formatter.py` are all reasonable; a module named `stuff.py` documents nothing about what it actually holds.

## Creating a Module at a Glance

| Step | What Happens |
|---|---|
| Save functions in a `.py` file | That file is now a module, automatically |
| Place it beside the importing script | Python can find it with a plain `import module_name` |
| Import it | `import billing` |
| Use its contents | `billing.function_name(...)`, exactly like `math.sqrt` |

## Your Turn: Picture Your Own Module

```python
# Save this as greetings.py, so the import below can find it:
greetings_code = '''
def welcome(name):
    return f"Welcome, {name}!"

def farewell(name):
    return f"Goodbye, {name}, see you soon!"
'''
with open("greetings.py", "w") as f:
    f.write(greetings_code)

# And this is main.py, in the same folder:
import greetings

print(greetings.welcome("Asha"))
print(greetings.farewell("Asha"))
```

If you have a real project folder to try this in, save the two halves as two actual files exactly as commented above, and run `main.py` to see the import work for real.

## Conclusion

Creating your own module takes no special syntax at all: save a `.py` file containing functions (or other definitions), place it in the same folder as the script that needs it, and import it by its filename, without the `.py` extension, exactly the way you import any standard library module. Keep a module's top level limited mostly to definitions, since any other code runs every time the module is imported, not just when you intend it to. With one module under control, the next lesson covers organising several related modules together into a single package.

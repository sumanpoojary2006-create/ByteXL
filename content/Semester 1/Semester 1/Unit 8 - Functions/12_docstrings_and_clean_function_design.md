## Introduction

Naveen is finally handing his collection of scripts over to next year's committee, and he opens `split_cost` for the first time in months to check it still does what he remembers. The parameters are named `a`, `b`, and `c`. There is no note anywhere explaining what they mean, whether `c` is a percentage or a flat amount, whether it even expects a whole number or a decimal, or what the function actually hands back. He wrote this code, and even he has to guess.

This final lesson of the unit is not about a new piece of syntax alone. It is about the habits, `docstrings` that explain what a function does and `type hints` that state what kind of values it expects and returns, that turn a function from something that merely works into something a stranger, or you in six months, can trust and use without re-reading every line.

**Definition:** A `docstring` is a string, almost always triple-quoted, placed as the very first line inside a function's body, describing what the function does.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/12_docstring_explains_the_function.png)

## The Docstring: Documentation Built Into the Function

A `docstring` is a string, almost always triple-quoted, placed as the very first line inside a function's body, describing what the function does.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwegtz" 
 width="100%"
></iframe>

Unlike an ordinary comment, a docstring is a real, accessible part of the function. Python attaches it to the function itself, retrievable with the built-in `help()`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrweh4t" 
 width="100%"
></iframe>

This prints the function's signature alongside the docstring, the exact information Naveen needed and did not have. A good editor or IDE will also show this docstring automatically the moment someone starts typing a call to the function, which is precisely why it is worth writing well.

## What a Good Docstring Covers

For a simple function, one clear sentence describing what it does and what it returns is often enough, exactly like the `split_cost` example above. For anything less obvious, a slightly longer docstring naming each parameter helps far more than a clever one-liner.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwehe8" 
 width="100%"
></iframe>

The goal is always the same question, answered without making the reader trace through the function's body: what does this need, and what do I get back?

## Type Hints: Stating What Kind of Value, Not Just What It Means

A docstring can say "total: the amount to be split," but it cannot say, in a way Python or an editor actually checks, whether that amount has to be an `int`, a `float`, or something else entirely. `Type hints` fill exactly that gap: written directly in the function's signature, they name the expected type of each parameter and, after an arrow, the type of whatever the function returns.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwehq8" 
 width="100%"
></iframe>

`total: float` means "this parameter is meant to hold a float," and the `-> float` after the closing parenthesis means "this function is meant to return a float." Read the whole signature left to right and it almost speaks for itself: give `split_cost` a float, an int, and optionally another float, and it hands back a float.

## Type Hints Are a Promise, Not a Lock

Unlike some languages, Python does not actually stop you from breaking a type hint; it runs the function anyway and only complains, if at all, through a separate checking tool.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwej35" 
 width="100%"
></iframe>

```text
300.0
TypeError: can only concatenate str (not "int") to str
```

The second call passes a string where `total: float` asked for a float, and Python still runs it, hint or no hint. It gets as far as `total + service_charge`, `"1200" + 0`, before it actually fails, because Python's `+` refuses to combine a string with an integer, and only then does the `TypeError` surface. Type hints document intent clearly enough that tools like `mypy`, and most modern editors, can flag a mismatch like this one before you ever run the code at all; Python itself simply trusts you to keep the promise, and only fails, if it fails, wherever the mismatched value first collides with an operation it cannot support.

## Naming: The Cheapest Documentation There Is

Before a docstring is even read, a function's own name and parameter names are already documenting it, for free. Compare these two identical functions.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwejc8" 
 width="100%"
></iframe>

Both compute exactly the same thing. Only one of them tells you what it computes without a single extra word of explanation. Naveen's `a`, `b`, `c` function from the introduction is exactly this trap: working code that nobody, including its own author, can trust on sight.

## One Function, One Job

A function that does one clearly nameable thing is easier to test, easier to reuse, and easier to trust than a function that quietly does three things at once. If you find yourself struggling to summarise a function in one short sentence for its docstring, that struggle is often a sign the function is trying to do too much, and would read more clearly split into two.

```text
def process_member(name, dues):
    print(f"Processing {name}")
    total = dues * 1.05
    print(f"{name} owes {total}")
    return total
```

This function prints a status message, computes a late fee, prints another message, and returns a result, all at once. Splitting it makes each piece nameable and testable on its own.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/12_one_job_function_design.png)


```text
def apply_late_fee(dues):
    """Apply a flat 5 percent late fee to a due amount."""
    return dues * 1.05

def report_due(name, amount):
    """Print a one-line status report for a member's due amount."""
    print(f"{name} owes {amount}")
```

## Clean Function Design at a Glance

| Habit | Why It Matters |
|---|---|
| A clear docstring as the first line | Lets `help()` and editors explain the function instantly |
| Type hints in the signature | States what type each parameter and the return value are meant to be |
| Descriptive parameter and function names | Documents intent before anyone reads the body |
| One function, one clearly nameable job | Easier to test, trust, reuse, and explain in one sentence |
| Defaults for the genuinely optional details | Keeps the common call simple, the rare call still possible |

## Your Turn: Document Your Own Function

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwejnb" 
 width="100%"
></iframe>

Run both lines and compare what `help()` shows you against the docstring and the type-hinted signature you wrote, confirming `help()` surfaces both the parameter types and the explanation together, exactly as a stranger opening this function for the first time would want to see them.

## Conclusion

A docstring, written as the first line inside a function's body, documents what a function does in a way `help()` and editors can surface automatically, and a type hint, written directly in the signature, states what kind of value each parameter and the return are meant to be, checked by external tools even though Python itself does not enforce it. Clear names for the function and its parameters document intent before anyone even reads that docstring or those hints. A function that does one clearly nameable job is easier to trust, reuse, and explain than one that quietly does several things at once. Across this entire unit, you have learned to define, call, parameterise, default, gather, shorten, transform, scope, and recurse with functions; writing them clearly, documented and type-hinted, the way this final lesson asked, is what makes every one of those tools actually pay off in code other people, including future you, can rely on.

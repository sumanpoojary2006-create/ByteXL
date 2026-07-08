## Introduction

Meera is about to post a photo, but the caption she drafted is a mess: half of it is in lowercase, there are stray spaces at both ends, and it still has the old name of her page in it that she has since changed. Rather than retyping the whole thing, she fixes it in a few quick taps, one to set the capitalisation right, one to trim the stray spaces, one to swap the old name for the new one. Strings come with exactly this kind of built-in toolbox of actions, called methods, for transforming text. Want everything in capitals? There is a method. Need to trim stray spaces from an entry? There is a method. Want to swap one word for another? There is a method. Because strings are immutable, every one of these methods leaves the original alone and hands you a brand new string instead, just as Meera's corrected username from the last lesson was always a freshly built replacement, never an edit to the old one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/04_string_methods_toolbox.png)

## Calling a Method With the Dot

A method is an action that belongs to the string, and you call it by writing the string, a dot, the method name, and parentheses.

```python
name = "asha"
print(name.upper())    # ASHA
```

Read `name.upper()` as "ask name for its upper-case version". The dot is the key: it says "this action belongs to this value." Most string methods need no extra information and take empty parentheses, while a few take arguments, as you will see.

## Changing Case

Several methods adjust capitalisation, which is endlessly useful.

```python
text = "hello world"
print(text.upper())        # HELLO WORLD
print(text.lower())        # hello world
print(text.title())        # Hello World
print(text.capitalize())   # Hello world
```

A common real use is making comparisons fair. If a user logs in as "ASHA" but the stored name is "asha", comparing them directly fails. Lower-casing both first, with `.lower()`, lets you compare them as equal regardless of how they were typed.

## Trimming Whitespace

Text from forms and files often arrives with unwanted spaces at the ends. The `strip` method removes them.

```python
messy = "   asha@email.com   "
print(messy.strip())       # asha@email.com
```

There are also `lstrip` and `rstrip` for trimming only the left or only the right side. Cleaning input with `strip` is one of the first things experienced programmers do, because a hidden trailing space causes mysterious mismatches, exactly the kind of stray space Meera spotted creeping into both ends of her messy caption.

## Replacing Text

The `replace` method swaps every occurrence of one piece of text for another. It takes two arguments: what to find, and what to put in its place.

```python
sentence = "I like tea"
print(sentence.replace("tea", "coffee"))    # I like coffee
```

## Asking a String What It Contains

Some methods do not change a string at all. Instead, they check what kind of characters it holds and hand back a boolean, `True` or `False`. The one you will lean on most is `.isdigit()`, which tells you whether every character in the string is a digit.

```python
print("123".isdigit())     # True
print("12a".isdigit())     # False
print("".isdigit())        # False
```

This is exactly the check you need before converting text from `input()` into a number. Recall from the control flow unit that `int("abc")` crashes the program; `.isdigit()` lets you test first and avoid that crash entirely.

```python
entry = input("Enter your age: ")
if entry.isdigit():
    age = int(entry)
    print("Age accepted:", age)
else:
    print("Please enter digits only.")
```

A related method, `.isalpha()`, works the same way but checks for letters instead of digits, useful when a field, such as a name, should contain no numbers at all.

## The Catch Everyone Hits Once

Here is the mistake that trips up nearly every beginner. Methods return a new string; they do not change the original. So what is wrong with this code?

```python
name = "asha"
name.upper()
print(name)    # still "asha"
```

The `upper()` did produce "ASHA", but nobody stored it, so it was thrown away, and `name` is unchanged. The fix is to capture the result: `name = name.upper()`. Remember, with immutable strings you must always reassign.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/04_methods_return_new_string.png)


## String Methods at a Glance

| Method | Effect | Example |
|---|---|---|
| `.upper()` | All capitals | `"hi".upper()` is `"HI"` |
| `.lower()` | All lowercase | `"HI".lower()` is `"hi"` |
| `.title()` | Capitalises each word | `"hi there".title()` is `"Hi There"` |
| `.capitalize()` | Capitalises just the first letter | `"hi there".capitalize()` is `"Hi there"` |
| `.strip()` | Removes whitespace from both ends | `"  hi  ".strip()` is `"hi"` |
| `.replace(old, new)` | Swaps every occurrence | `"tea".replace("t", "c")` is `"cea"` |
| `.isdigit()` | `True` if every character is a digit | `"123".isdigit()` is `True` |
| `.isalpha()` | `True` if every character is a letter | `"abc".isalpha()` is `True` |

## Your Turn: Clean Up an Entry

```python
raw = input("Enter your email: ")
clean = raw.strip().lower()
print("Stored as:", clean)
```

Type your email with some extra spaces and in mixed case. The program trims it and lower-cases it in one tidy line, because methods can be chained: the result of `.strip()` is itself a string, so you can immediately call `.lower()` on it.

## Conclusion

String methods are built-in actions called with a dot, such as `upper`, `lower`, `title`, `strip`, and `replace`, and because strings are immutable they always return a new string rather than changing the original. Checking methods like `.isdigit()` and `.isalpha()` are the exception, since they hand back a boolean instead of a new string, which is exactly what makes them so useful for validating input before you trust it. The single most common beginner bug with the text-transforming methods is forgetting to store the result, so make `text = text.method()` a habit. With case-changing, trimming, replacing, and now checking in your toolkit, you can clean, normalise, and validate almost any text a user throws at you. These methods all transform or inspect a string you already have whole; the next lesson tackles a different pair of jobs, breaking one string apart into many and fusing many back into one.

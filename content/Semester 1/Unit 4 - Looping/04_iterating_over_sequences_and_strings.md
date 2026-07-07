## Introduction

Kabir is going down the member list of the class WhatsApp group on his phone, reading each name in turn, Aisha, Ravi, Meera, one after another, rather than thinking about positions 0, 1, 2. A moment later he is checking a fest hashtag he made up, and his eye moves over it one letter at a time in just the same way, no numbers involved at all.

So far your `for` loops have walked through numbers made by `range()`. But the `for` loop is far more general than that. It can step through any sequence of items, one at a time: every character in a piece of text, every name in a list, every item in a collection. The natural way to read a `for` loop is "for each item in this group, do something." Kabir never once converted the member list into position numbers in his head; he simply moved from name to name, and his hashtag in the same way letter to letter. This lesson shows that wider power.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5m6t8/04_iterating_letters.png)
## Looping Straight Through a String

A string is really a sequence of characters, so a `for` loop can visit each character in turn, with no `range()` required.

```python
for letter in "Python":
    print(letter)
```

This prints each letter on its own line: P, then y, then t, and so on. The loop variable `letter` holds one character per pass. You will explore strings in depth in the next unit, but already you can see them as something a loop can walk through, character by character.

## Looping Through a List of Items

Often you want to process a group of values: a set of names, a row of scores, a basket of prices. Python stores such groups in a list, written with square brackets. You will study lists fully in a later unit, but they are intuitive enough to loop over right now.

```python
names = ["Asha", "Ravi", "Meera"]
for name in names:
    print("Hello,", name)
```

The loop runs once for each name, greeting all three. Notice how natural this reads: "for each name in names." There is no index to manage and no length to count; the loop simply hands you each item in order, the same effortless scroll down the class group Kabir does without ever thinking in positions.

## When You Also Need the Position

Sometimes you want both the item and its position number. So how do you get the index without going back to `range()`? Python offers `enumerate`, which gives you both at once.

```python
names = ["Asha", "Ravi", "Meera"]
for position, name in enumerate(names, start=1):
    print(position, name)
```

This prints "1 Asha", "2 Ravi", "3 Meera". The `start=1` simply makes the numbering begin at 1 instead of 0, which is friendlier for people reading a list.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5m6t8/04_enumerate_position_and_item.png)

## What a for Loop Can Step Through

| You're Looping Over | Loop Variable Holds | Example |
|---|---|---|
| A string | One character per pass | `for letter in "Python":` |
| A list | One item per pass | `for name in names:` |
| `enumerate(a_list)` | Position and item together | `for position, name in enumerate(names):` |

## Your Turn: Count the Vowels

```python
word = input("Enter a word: ")
vowels = 0
for letter in word:
    if letter in "aeiouAEIOU":
        vowels = vowels + 1
print(f"'{word}' has {vowels} vowels.")
```

Type your own name and watch it count the vowels. The loop visits each letter, the `if` checks whether that letter is a vowel, and a counter keeps the running total. This is your first taste of combining a loop with a decision, which is where loops become genuinely useful.

## Conclusion

A `for` loop can step through any sequence, not just numbers, visiting each character of a string or each item in a list with the readable shape "for each item in the group." When you need the position as well as the value, `enumerate` hands you both. Iterating directly over the things you care about, rather than over index numbers, is the natural Python way, and it makes your loops read almost like plain English. Not every pass through a sequence needs to run all the way to the end, though, and the next lesson gives you the tools to cut one short the moment it has done its job.

## Introduction

Meera has typed all her tags into one box as a single line, "handmade,gifts,pune", crammed together with commas, but the app needs them as three separate tags. She splits the line apart at each comma to get them. A moment later she has the opposite problem: a few separate words she wants to fuse into one neat hashtag with no spaces, so she joins them back together into a single piece of text. Real-world text rarely comes in the exact shape you need, and these two opposite jobs, breaking apart and joining together, are handled by two partner methods: `split` and `join`. The single comma-separated line Meera typed her tags into looked like one piece of text to her, but the app needed it treated as three separate pieces, which is precisely the gap these two methods close.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/05_split_join.png)

## Meera's Tags, Split Apart

The line Meera typed, all her tags crammed into one box separated by commas, is the exact shape `split` exists to handle.

```python
tags_line = "handmade,gifts,pune"
tags = tags_line.split(",")
print(tags)    # ['handmade', 'gifts', 'pune']
```

What looked like one piece of text to Meera was always, structurally, three separate tags waiting to be pulled apart, and `split(",")` does exactly that in a single call, with no manual scanning for comma positions required.

## split: Break One String Into Many

The `split` method chops a string into pieces wherever it finds a separator you choose, handing back a list of the pieces. (You will study lists fully in the next unit; for now, think of a list as several values in order.)

```python
data = "Asha,20,Pune"
parts = data.split(",")
print(parts)    # ['Asha', '20', 'Pune']
```

Each comma marks a cut, and the pieces between the cuts become the items. If you call `split` with no separator at all, it splits on spaces, which is the easy way to break a sentence into words:

```python
sentence = "Python is fun"
print(sentence.split())    # ['Python', 'is', 'fun']
```

## join: Combine Many Into One

The `join` method does the reverse: it glues a collection of strings together, placing a chosen separator between each. The separator is the string you call `join` on, which reads a little oddly at first but quickly makes sense.

```python
words = ["Python", "is", "fun"]
print(" ".join(words))     # Python is fun
print("-".join(words))     # Python-is-fun
```

Read `" ".join(words)` as "join these words with a space between each". One caution worth remembering: `join` only works on pieces that are already strings. This is exactly the move Meera makes in reverse, fusing a handful of separate words back into one clean hashtag with no stray spaces left between them.

```python
hashtag_words = ["handmade", "gifts", "pune"]
hashtag = "#" + "".join(word.title() for word in hashtag_words)
print(hashtag)    # #HandmadeGiftsPune
```

Joining with an empty string, `"".join(...)`, glues every piece together with nothing at all between them, exactly the no-spaces hashtag Meera wanted, and `.title()` on each word along the way keeps it readable despite having no spaces left to separate the words visually.

## A Round Trip

Splitting and joining are natural partners. You often split a line apart, do something to the pieces, then join them back together.

```python
name = "sachin tendulkar"
words = name.split()
joined = " ".join(words)
print(joined.title())      # Sachin Tendulkar
```

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/05_split_join_round_trip.png)


## split and join at a Glance

| Method | Direction | Example |
|---|---|---|
| `text.split(",")` | One string into a list, cut at each comma | `"a,b,c".split(",")` is `['a', 'b', 'c']` |
| `text.split()` | One string into a list, cut at spaces | `"a b c".split()` is `['a', 'b', 'c']` |
| `" ".join(words)` | A list into one string, joined with a space | `" ".join(['a', 'b'])` is `"a b"` |
| `"".join(words)` | A list into one string, joined with nothing | `"".join(['a', 'b'])` is `"ab"` |

## Your Turn: Count the Words

```python
sentence = input("Type a sentence: ")
words = sentence.split()
print(f"Your sentence has {len(words)} words.")
```

Type any sentence and the program splits it into words and counts them with `len()`. Splitting on spaces turned a single string into separate words, and counting them became trivial. This split-then-process idea is one of the most useful habits in all of text handling.

## Conclusion

The `split` method breaks a string into a list of pieces at a chosen separator, defaulting to spaces so it neatly produces words, while `join` combines a collection of strings into one, placing a separator between each. They are exact opposites and frequent partners: split text apart to work on the pieces, then join them back together. Mastering this pair is the foundation of reading data files and parsing almost any structured text. Splitting hands you the pieces; the next lesson shows how to search within a string directly, without first having to break it apart at all.

## Introduction

Nadia is three months into her data analyst role at the library consortium. She has written a random book recommender, a CSV importer, a date-formatting utility, a counter for overdue records, and a folder-walker that finds all catalog files. Each one took her an afternoon to write and debug. When she shows the code to her mentor, he asks one question: "Did you check if stdlib already has this?"

It does. Every single one of them. Python ships with a standard library of more than 200 modules that cover randomness, cryptography, dates, data structures, file-system operations, serialization, testing, and much more. Learning the stdlib means knowing which tools already exist before writing your own.

![A toolbox labeled "Python Standard Library" with drawers: random, datetime, collections, pathlib, json, csv, hashlib, os, and itertools](images/01_why_stdlib_matters.png)

## What the Standard Library Is

The standard library is the collection of modules that ship with every Python installation. They require no `pip install`. They are maintained by the core Python team, documented at docs.python.org, and stable across platforms.

```python
# These are all part of the standard library -- no pip install needed
import random, datetime, collections, pathlib
import json, csv, hashlib, os, itertools, re, logging, unittest, functools

stdlib_modules = [
    "random", "datetime", "collections", "pathlib",
    "json", "csv", "hashlib", "os", "itertools",
    "re", "logging", "unittest", "functools",
]
print(f"Imported {len(stdlib_modules)} stdlib modules:")
for name in stdlib_modules:
    print(f"  import {name}  -- no pip install needed")
```

When you run `python`, you have access to all of these immediately.

## The Cost of Not Knowing It

Writing your own version of a stdlib function has a hidden cost beyond development time:

- Your implementation has bugs the stdlib version has already fixed.
- Your implementation is not documented, tested, or reviewed by peers.
- New team members must read your code to understand what a standard function does.
- Your implementation may not handle edge cases correctly (leap years, Unicode, thread safety).

Nadia's date formatter silently produced wrong output for dates in early January because she did not handle ISO week numbers correctly. `datetime.strftime` handles it correctly by default.

## The Import Is the Documentation

Looking up a module in the standard library is also a way to discover what Python considers to be a "standard" solution to a problem. When you see that `collections.Counter` exists, you learn that "count occurrences in a sequence" is a common enough problem to deserve a dedicated data structure.

```python
from collections import Counter

overdue_records = [
    {"patron_id": "P001", "isbn": "978-001"},
    {"patron_id": "P002", "isbn": "978-002"},
    {"patron_id": "P001", "isbn": "978-003"},
    {"patron_id": "P003", "isbn": "978-001"},
    {"patron_id": "P001", "isbn": "978-004"},
]

# Nadia's original solution:
overdue_count = {}
for record in overdue_records:
    patron = record["patron_id"]
    overdue_count[patron] = overdue_count.get(patron, 0) + 1
print(f"Manual counter: {overdue_count}")

# The stdlib already solved this:
overdue_count = Counter(record["patron_id"] for record in overdue_records)
print(f"Counter:        {dict(overdue_count)}")
print(f"Most overdue:   {overdue_count.most_common(1)}")
```

The stdlib version is not just shorter. It is readable to anyone who knows Python, handles edge cases (like an empty sequence), and gives extra methods like `most_common()` for free.

## How to Explore the Standard Library

Three approaches work well:

1. **Python documentation**: docs.python.org/3/library/ has every module with examples.
2. **`help()` in the REPL**: `help(random)` prints the module's documentation inline.
3. **`dir()` in the REPL**: `dir(collections)` lists everything in the module.

```python
import random

# help() shows the docstring and signature inline
help(random.choice)

# dir() lists all names in the module
names = [n for n in dir(random) if not n.startswith("_")]
print(f"\nPublic names in random ({len(names)} total):")
print(", ".join(names[:10]), "...")
```

## The Standard Library at a Glance

| Module | What it solves |
|---|---|
| `random` | Randomness, sampling, shuffling |
| `hashlib`, `secrets` | Cryptographic hashing, secure tokens |
| `datetime` | Dates, times, durations |
| `collections` | Named tuple, counter, ordered dict, deque |
| `itertools` | Iteration patterns: chain, groupby, islice |
| `os`, `pathlib` | File system operations |
| `json`, `csv` | Serialization and deserialization |
| `re` | Regular expressions |
| `logging` | Structured, leveled application logging |
| `unittest` | Built-in test framework |

## Your Turn

Open a Python REPL and explore at least two of the modules listed above. For each one, run `dir(module)` to see the available names, then pick one function and call `help(function)` to read its signature and description.

```python
import random
import collections

# What's available in each module?
random_names = [n for n in dir(random) if not n.startswith("_")]
collections_names = [n for n in dir(collections) if not n.startswith("_")]
print(f"random has {len(random_names)} public names: {random_names[:5]}...")
print(f"collections has {len(collections_names)} public names: {collections_names[:5]}...")

# Quick demo of a function you'd otherwise write yourself
books = ["Dune", "Foundation", "Neuromancer", "Shogun"]
sample = random.sample(books, 2)    # choose 2 without replacement
print(f"\nRandom 2-book recommendation: {sample}")

Point = collections.namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"namedtuple Point: {p}, x={p.x}, y={p.y}")
```

Write down one function or class from each module that solves something you have previously written by hand.

## Conclusion

The Python standard library ships with every Python installation and covers the most common utility problems in software development. Using it instead of hand-writing solutions means fewer bugs, more readable code, and shared vocabulary with other Python developers. The following lessons explore the most useful stdlib modules in depth, starting with the one Nadia needed first: `random`.

## Introduction

Leila's import pipeline is shipping. But Arjun, watching it go live, asks the question she has been expecting: "Should I use generators everywhere now? Every function that returns a list, should I convert it?" Leila pauses. She knows generators are powerful and memory-efficient, but she also knows her pipeline has two places where she had to call `list()` explicitly because she needed to count items and iterate twice. Generators are not always better. They are a specific tool for a specific situation.

This final lesson of the unit draws a practical line: when generators are clearly the right choice, when lists are, and how to recognize which situation you are in.

![A decision tree showing large stream or single-pass on one branch leading to generator, and small data or multiple passes on the other leading to list](images/08_when_to_use_generators.png)

## When Generators Are the Right Choice

Generators excel in four situations:

**Processing large or unbounded data**: when your data source is a file, a network stream, a database cursor, or anything that might be too large to hold in memory, a generator is always correct. A `for line in file:` loop is a generator-based pattern that works for a 100-byte file and a 100-gigabyte file identically.

**Early termination**: when you expect to stop before reaching the end, a lazy generator is efficient regardless of how much data exists after the stopping point. `next(gen for gen in huge_dataset if condition)` reads nothing after the first match.

**Pipelining**: chaining a series of transformations and filters through multiple generators, as Leila did, avoids all intermediate collections. Data flows through the entire pipeline one item at a time.

**Infinite sequences**: generators can represent sequences that have no end: counting integers, generating Fibonacci numbers, producing heartbeat timestamps. Lists cannot hold an infinite sequence; generators can represent one trivially.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-08-when-to-use-generators-001-f773e97fce.html"
 width="100%"
></iframe>

## When Lists Are the Right Choice

Lists are better when:

**You need to iterate more than once.** A list supports multiple `for` loops, index access, and length queries. A generator is exhausted after one pass.

**You need to know the length.** `len()` requires a sequence that knows its size. Generators do not.

**You need random access.** `items[42]` requires indexing. Generators can only move forward.

**You need to modify the sequence.** Appending, removing, or sorting requires a mutable sequence.

**The dataset is small.** For a list of twenty items, the overhead of thinking about laziness is not justified. Clarity and simplicity matter more.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-08-when-to-use-generators-002-d5aa383bdd.html"
 width="100%"
></iframe>

## Converting Between Generators and Lists

The conversion between a generator and a list is always explicit and intentional: `list(gen)` materializes everything, and the `list()` call makes that trade-off visible in the code.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-08-when-to-use-generators-003-18edf95bcb.html"
 width="100%"
></iframe>

## Generators in the Complete Library System

In the context of the semester project, generators are the right tool for the data ingestion layer:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-08-when-to-use-generators-004-dfb455f96d.html"
 width="100%"
></iframe>

`read_csv` and `validated` are both generators. The `for` loop inside `imported_count` drives the pipeline, pulling records one at a time from disk through validation to the database call. At no point is more than one record in memory.

## When to Use Generators at a Glance

| Situation | Generator | List |
|---|---|---|
| Large or unbounded data | Correct | Risky (memory) |
| Single pass only | Correct | Also works, less efficient |
| Multiple passes | Must re-call the function | Correct |
| Random access (`seq[i]`) | Not supported | Correct |
| `len()` | Not supported | Correct |
| Early termination expected | Efficient (stops on first match) | Processes everything first |
| Sorting the results | Not directly supported | Correct |

## Your Turn

Consider this function:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-08-when-to-use-generators-005-fcdbb22469.html"
 width="100%"
></iframe>

A database with 50,000 patrons returns 50,000 rows at once. Rewrite `load_all_patrons` as a generator that uses `fetchone()` in a loop to retrieve rows one at a time. Then explain in which scenario a caller would need `list(load_all_patrons(cursor))` even with your generator version, and why that is an acceptable and explicit trade-off rather than a bug.

## Conclusion

Generators are the right tool when data is large or unbounded, when you expect early termination, when you are building a pipeline of transformations, or when the sequence is infinite. Lists are the right tool when you need multiple passes, random access, length queries, or sorted output. The two are not in competition: a well-designed system uses generators where data flows and lists where data is examined, sorted, or revisited. Unit 5 moves from lazy iteration to a different kind of code reuse: decorators, which wrap functions to add behavior without modifying them.

## Introduction

Leila's `CatalogReader` class works correctly, but writing eighteen lines to do what feels like a simple "give me approved records one at a time" operation seems excessive. She shows it to Nadia, who reads it and says: "That's correct, but Python gives you a much shorter way to write the same thing." She writes a generator function in five lines that does exactly what `CatalogReader` does, and Leila's first reaction is: "That looks like a bug. How does the function return more than once?"

The answer is `yield`, and understanding what it does transforms the way you think about functions that produce sequences.

![](images/04_generators_yield.png)

## A Regular Function Returns Once

A normal function runs from top to bottom, returns a value, and then its local state is gone. Calling it again starts from scratch.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJkZWYgZ2V0X2FwcHJvdmVkKHJlY29yZHMpOlxuICAgIHJlc3VsdHMgPSBbXVxuICAgIGZvciByIGluIHJlY29yZHM6XG4gICAgICAgIGlmIHJbXCJhcHByb3ZlZFwiXTpcbiAgICAgICAgICAgIHJlc3VsdHMuYXBwZW5kKHIpXG4gICAgcmV0dXJuIHJlc3VsdHMgICAgIyByZXR1cm5zIG9uY2UsIGRpc2NhcmRzIHN0YXRlIn0"
 width="100%"
></iframe>

This builds the entire list before the caller receives anything. For a million records, that is a million records in memory simultaneously.

## A Generator Function Yields Many Times

A **generator function** looks like a regular function but uses `yield` instead of `return`. When called, it does not run immediately. It returns a **generator object**. Advancing that generator (via `next()` or a `for` loop) resumes the function from where it last `yield`-ed, runs until the next `yield`, and pauses again with its local state fully preserved.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJkZWYgYXBwcm92ZWRfcmVjb3JkcyhyZWNvcmRzKTpcbiAgICBmb3IgcmVjb3JkIGluIHJlY29yZHM6XG4gICAgICAgIGlmIHJlY29yZFtcImFwcHJvdmVkXCJdOlxuICAgICAgICAgICAgeWllbGQgcmVjb3JkICAgIyBwYXVzZSBoZXJlLCByZXR1cm4gdGhpcyB2YWx1ZSwgcmVzdW1lIGxhdGVyXG5cbnJlY29yZHMgPSBbXG4gICAge1widGl0bGVcIjogXCJEdW5lXCIsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG4gICAge1widGl0bGVcIjogXCJSb3VnaCBEcmFmdFwiLCBcImFwcHJvdmVkXCI6IEZhbHNlfSxcbiAgICB7XCJ0aXRsZVwiOiBcIkZvdW5kYXRpb25cIiwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbl1cblxuZ2VuID0gYXBwcm92ZWRfcmVjb3JkcyhyZWNvcmRzKVxucHJpbnQodHlwZShnZW4pKSAgICAgICAjIDxjbGFzcyAnZ2VuZXJhdG9yJz5cbnByaW50KG5leHQoZ2VuKSkgICAgICAgIyB7XCJ0aXRsZVwiOiBcIkR1bmVcIiwgXCJhcHByb3ZlZFwiOiBUcnVlfVxucHJpbnQobmV4dChnZW4pKSAgICAgICAjIHtcInRpdGxlXCI6IFwiRm91bmRhdGlvblwiLCBcImFwcHJvdmVkXCI6IFRydWV9XG5wcmludChuZXh0KGdlbikpICAgICAgICMgU3RvcEl0ZXJhdGlvbiAtLSBubyBtb3JlIGFwcHJvdmVkIHJlY29yZHMifQ"
 width="100%"
></iframe>

The function body ran in three pieces: up to the first `yield`, from there to the second `yield`, then to the end of the loop where it fell off the end and raised `StopIteration`. Between each piece, all local variables (`records`, `record`) were preserved exactly.

## Using a Generator in a for Loop

Because generators implement the iterator protocol (`__iter__` and `__next__`), they work seamlessly in `for` loops:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJyZWNvcmRzID0gW1xuICAgIHtcInRpdGxlXCI6IFwiRHVuZVwiLCBcImFwcHJvdmVkXCI6IFRydWV9LFxuICAgIHtcInRpdGxlXCI6IFwiUm91Z2ggRHJhZnRcIiwgXCJhcHByb3ZlZFwiOiBGYWxzZX0sXG4gICAge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG4gICAge1widGl0bGVcIjogXCJTaG9ndW5cIiwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbl1cblxuZm9yIGJvb2sgaW4gYXBwcm92ZWRfcmVjb3JkcyhyZWNvcmRzKTpcbiAgICBwcmludChib29rW1widGl0bGVcIl0pXG4jIER1bmVcbiMgRm91bmRhdGlvblxuIyBTaG9ndW4ifQ"
 width="100%"
></iframe>

The `for` loop calls `iter()` on the generator (which returns the generator itself) and then calls `next()` repeatedly. The function's execution is interleaved with the loop: one `yield` per iteration.

## Generators Are One-Pass Iterators

Like the custom iterator class from the previous lesson, a generator object is exhausted after one pass. Calling the generator *function* again produces a fresh generator.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJnZW4xID0gYXBwcm92ZWRfcmVjb3JkcyhyZWNvcmRzKVxuZ2VuMiA9IGFwcHJvdmVkX3JlY29yZHMocmVjb3JkcykgICAjIGZyZXNoIGdlbmVyYXRvciwgaW5kZXBlbmRlbnQgc3RhdGVcblxucHJpbnQobmV4dChnZW4xKSkgICAjIER1bmVcbnByaW50KG5leHQoZ2VuMikpICAgIyBEdW5lXG5wcmludChuZXh0KGdlbjEpKSAgICMgRm91bmRhdGlvbiAtLSBnZW4xIGFkdmFuY2VzIGluZGVwZW5kZW50bHkifQ"
 width="100%"
></iframe>

## yield vs return in the Same Function

A function can have both `yield` and `return`, but in a generator function `return` ends iteration immediately by raising `StopIteration`. The value after `return` is stored in the exception but not usually visible to the caller.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgZmlyc3Rfbl9hcHByb3ZlZChyZWNvcmRzLCBuKTpcbiAgICBjb3VudCA9IDBcbiAgICBmb3IgcmVjb3JkIGluIHJlY29yZHM6XG4gICAgICAgIGlmIHJlY29yZFtcImFwcHJvdmVkXCJdOlxuICAgICAgICAgICAgeWllbGQgcmVjb3JkXG4gICAgICAgICAgICBjb3VudCArPSAxXG4gICAgICAgICAgICBpZiBjb3VudCA-PSBuOlxuICAgICAgICAgICAgICAgIHJldHVybiAgICMgc3RvcHMgaXRlcmF0aW9uIGVhcmx5In0"
 width="100%"
></iframe>

## Generators at a Glance

| Concept | What it means |
|---|---|
| Generator function | A function with at least one `yield` statement |
| Generator object | The iterator returned when a generator function is called |
| `yield value` | Pauses the function; returns `value`; resumes later |
| `return` in a generator | Ends the generator; raises `StopIteration` |
| One-pass | A generator object is exhausted after one traversal |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2dlbmVyYXRvcnNfYW5kX3RoZV95aWVsZF9rZXl3b3JkIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJkZWYgZmlib25hY2NpKCk6XG4gICAgYSwgYiA9IDAsIDFcbiAgICB3aGlsZSBUcnVlOiAgICAgICAgICMgaW5maW5pdGUgZ2VuZXJhdG9yIVxuICAgICAgICB5aWVsZCBhXG4gICAgICAgIGEsIGIgPSBiLCBhICsgYiJ9"
 width="100%"
></iframe>

This generator produces Fibonacci numbers indefinitely. Write a `for` loop that collects only the first 10 values into a list (use `enumerate` or a counter with `break`). Then explain why an infinite generator does not crash Python: the function is paused at `yield` between calls, so only one value is computed at a time.

## Conclusion

A generator function uses `yield` to pause execution and return a value, then resumes from where it left off when the next item is requested. The function's local state is fully preserved between yields. Generators implement the iterator protocol automatically, making them usable wherever an iterator is expected. They produce values on demand rather than all at once, which is exactly what Leila needs for her million-record catalog import. The next lesson introduces a concise syntax for producing generator objects in a single expression: generator expressions.

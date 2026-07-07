## Introduction

Nadia's book recommendation feature picks a random title from the catalog every morning and displays it on the library portal. Her original implementation used `random.random()` multiplied by the list length, rounded to an integer, used as an index. It worked most of the time but occasionally crashed with an index-out-of-range error when the float rounding was off by one.

Her mentor points her to `random.choice()`, which does this correctly in one line. The `random` module is the right place for all randomness in Python that does not involve security.

![A diagram showing the random module's main functions: choice (picks one), sample (picks k unique), shuffle (reorders in place), and randint (picks an integer in a range)](images/02_random_module.png)

## Basic Random Choices

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCByYW5kb21cblxuY2F0YWxvZyA9IFtcIkR1bmVcIiwgXCJGb3VuZGF0aW9uXCIsIFwiTmV1cm9tYW5jZXJcIiwgXCJUaGUgTGVmdCBIYW5kIG9mIERhcmtuZXNzXCIsIFwiRW5kZXIncyBHYW1lXCJdXG5cbiMgUGljayBvbmUgYXQgcmFuZG9tXG5yZWNvbW1lbmRhdGlvbiA9IHJhbmRvbS5jaG9pY2UoY2F0YWxvZylcbnByaW50KGZcIlRvZGF5J3MgcmVjb21tZW5kYXRpb246IHtyZWNvbW1lbmRhdGlvbn1cIilcblxuIyBQaWNrIGsgdW5pcXVlIGl0ZW1zIChubyByZXBlYXRzKVxudG9wX3RocmVlID0gcmFuZG9tLnNhbXBsZShjYXRhbG9nLCBrPTMpXG5wcmludChmXCJUb3AgdGhyZWU6IHt0b3BfdGhyZWV9XCIpXG5cbiMgU2h1ZmZsZSBhIGxpc3QgaW4gcGxhY2VcbnJhbmRvbS5zaHVmZmxlKGNhdGFsb2cpXG5wcmludChmXCJTaHVmZmxlZDoge2NhdGFsb2d9XCIpIn0"
 width="100%"
></iframe>

`random.choice` picks exactly one element. `random.sample` picks `k` elements without replacement -- the same item cannot appear twice. `random.shuffle` rearranges the list in place and returns `None`.

## Random Numbers

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCByYW5kb21cblxuIyBJbnRlZ2VyIGluIGFuIGluY2x1c2l2ZSByYW5nZSBbYSwgYl1cbmRpY2UgPSByYW5kb20ucmFuZGludCgxLCA2KVxucHJpbnQoZlwiRGljZToge2RpY2V9XCIpXG5cbiMgRmxvYXQgaW4gdGhlIHJhbmdlIFswLjAsIDEuMClcbnByb2JhYmlsaXR5ID0gcmFuZG9tLnJhbmRvbSgpXG5wcmludChmXCJQcm9iYWJpbGl0eToge3Byb2JhYmlsaXR5Oi40Zn1cIilcblxuIyBGbG9hdCBpbiBhIGN1c3RvbSByYW5nZSBbYSwgYilcbnJhdGluZyA9IHJhbmRvbS51bmlmb3JtKDEuMCwgNS4wKVxucHJpbnQoZlwiUmFuZG9tIHJhdGluZzoge3JhdGluZzouMmZ9XCIpIn0"
 width="100%"
></iframe>

`random.randint(a, b)` is inclusive on both ends, which is different from Python's `range(a, b)` (exclusive end). This follows the natural language meaning of "a number between 1 and 6."

## Weighted Selection

Sometimes items should not have equal probability. `random.choices` (with an `s`) accepts a `weights` list:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCByYW5kb21cblxuZ2VucmVzID0gW1wiRmljdGlvblwiLCBcIk5vbi1GaWN0aW9uXCIsIFwiU2NpZW5jZSBGaWN0aW9uXCIsIFwiQmlvZ3JhcGh5XCJdXG53ZWlnaHRzID0gWzQwLCAzMCwgMjAsIDEwXSAgICMgRmljdGlvbiBpcyA0MCUgbGlrZWx5LCBCaW9ncmFwaHkgaXMgMTAlXG5cbnBpY2tlZCA9IHJhbmRvbS5jaG9pY2VzKGdlbnJlcywgd2VpZ2h0cz13ZWlnaHRzLCBrPTEpWzBdXG5wcmludChmXCJXZWlnaHRlZCBwaWNrOiB7cGlja2VkfVwiKVxuXG4jIE92ZXIgbWFueSB0cmlhbHMsIGRpc3RyaWJ1dGlvbiBzaG91bGQgbWF0Y2ggdGhlIHdlaWdodHM6XG5jb3VudHMgPSB7ZzogMCBmb3IgZyBpbiBnZW5yZXN9XG5mb3IgXyBpbiByYW5nZSgxMF8wMDApOlxuICAgIGNvdW50c1tyYW5kb20uY2hvaWNlcyhnZW5yZXMsIHdlaWdodHM9d2VpZ2h0cylbMF1dICs9IDFcbnByaW50KGNvdW50cykifQ"
 width="100%"
></iframe>

Note: `random.choices` (plural, with weights) allows repeats; `random.sample` (without weights) does not allow repeats.

## Reproducibility with Seeds

The `random` module uses a pseudo-random number generator. The same seed always produces the same sequence. This is critical for reproducible tests, demos, and experiments:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCByYW5kb21cblxucmFuZG9tLnNlZWQoNDIpXG5wcmludChyYW5kb20uY2hvaWNlKFtcIkFcIiwgXCJCXCIsIFwiQ1wiLCBcIkRcIl0pKSAgICMgYWx3YXlzIHRoZSBzYW1lIHJlc3VsdFxucHJpbnQocmFuZG9tLnJhbmRpbnQoMSwgMTAwKSkgICAgICAgICAgICAgICAgICAjIGFsd2F5cyB0aGUgc2FtZSByZXN1bHRcblxuIyBXaXRob3V0IHNlZWQ6IGRpZmZlcmVudCByZXN1bHQgZWFjaCBydW5cbnJhbmRvbS5zZWVkKE5vbmUpICAgIyByZXN0b3JlcyBub24tZGV0ZXJtaW5pc3RpYyBiZWhhdmlvclxucHJpbnQocmFuZG9tLmNob2ljZShbXCJBXCIsIFwiQlwiLCBcIkNcIiwgXCJEXCJdKSkgICAjIHVucHJlZGljdGFibGUifQ"
 width="100%"
></iframe>

## Important: random Is Not Cryptographically Secure

`random` uses a predictable algorithm (Mersenne Twister). For security-sensitive uses -- generating passwords, tokens, session IDs -- use `secrets` instead (covered in the next lesson).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgV1JPTkcgZm9yIHNlY3VyaXR5OiBwcmVkaWN0YWJsZVxuaW1wb3J0IHJhbmRvbVxudG9rZW4gPSBzdHIocmFuZG9tLnJhbmRpbnQoMTAwMDAwLCA5OTk5OTkpKVxuXG4jIENPUlJFQ1QgZm9yIHNlY3VyaXR5OiB1bnByZWRpY3RhYmxlXG5pbXBvcnQgc2VjcmV0c1xudG9rZW4gPSBzZWNyZXRzLnRva2VuX2hleCgxNikifQ"
 width="100%"
></iframe>

## The random Module at a Glance

| Function | What it does |
|---|---|
| `random.choice(seq)` | Pick one element at random |
| `random.sample(seq, k)` | Pick k unique elements (no repeats) |
| `random.shuffle(lst)` | Shuffle a list in place |
| `random.choices(seq, weights, k)` | Pick k elements with optional weights |
| `random.randint(a, b)` | Random integer in [a, b] (inclusive) |
| `random.random()` | Random float in [0.0, 1.0) |
| `random.uniform(a, b)` | Random float in [a, b) |
| `random.seed(n)` | Set seed for reproducibility |

## Your Turn

Write a function `morning_picks(catalog, n)` that returns `n` unique book recommendations for the day, in a random order. If the catalog has fewer than `n` books, return all books shuffled.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3JhbmRvbV9tb2R1bGUgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImltcG9ydCByYW5kb21cblxuZGVmIG1vcm5pbmdfcGlja3MoY2F0YWxvZywgbik6XG4gICAgaWYgbGVuKGNhdGFsb2cpIDw9IG46XG4gICAgICAgIHJlc3VsdCA9IGxpc3QoY2F0YWxvZylcbiAgICAgICAgcmFuZG9tLnNodWZmbGUocmVzdWx0KVxuICAgICAgICByZXR1cm4gcmVzdWx0XG4gICAgcmV0dXJuIHJhbmRvbS5zYW1wbGUoY2F0YWxvZywgaz1uKVxuXG5ib29rcyA9IFtcIkR1bmVcIiwgXCJGb3VuZGF0aW9uXCIsIFwiTmV1cm9tYW5jZXJcIiwgXCIxOTg0XCIsIFwiQnJhdmUgTmV3IFdvcmxkXCJdXG5wcmludChtb3JuaW5nX3BpY2tzKGJvb2tzLCAzKSlcbnByaW50KG1vcm5pbmdfcGlja3MoYm9va3MsIDEwKSkgICAjIGZld2VyIHRoYW4gMTAgYm9va3MgLS0gcmV0dXJucyBhbGwgNSJ9"
 width="100%"
></iframe>

Then add a `seed` parameter so the function can produce the same output for testing.

## Conclusion

The `random` module covers all everyday randomness: picking, sampling, shuffling, and weighting. It is simple, well-tested, and built in. The critical caveat is that it is not secure: for tokens, passwords, and session IDs, the next lesson introduces `hashlib` and `secrets`, which provide cryptographic-strength randomness and hashing.

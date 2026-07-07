## Introduction

Nadia's book recommendation feature picks a random title from the catalog every morning and displays it on the library portal. Her original implementation used `random.random()` multiplied by the list length, rounded to an integer, used as an index. It worked most of the time but occasionally crashed with an index-out-of-range error when the float rounding was off by one.

Her mentor points her to `random.choice()`, which does this correctly in one line. The `random` module is the right place for all randomness in Python that does not involve security.

![A diagram showing the random module's main functions: choice (picks one), sample (picks k unique), shuffle (reorders in place), and randint (picks an integer in a range)](images/02_random_module.png)

## Basic Random Choices

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-001-483de89fe1.html"
 width="100%"
></iframe>

`random.choice` picks exactly one element. `random.sample` picks `k` elements without replacement -- the same item cannot appear twice. `random.shuffle` rearranges the list in place and returns `None`.

## Random Numbers

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-002-b51e95f4c6.html"
 width="100%"
></iframe>

`random.randint(a, b)` is inclusive on both ends, which is different from Python's `range(a, b)` (exclusive end). This follows the natural language meaning of "a number between 1 and 6."

## Weighted Selection

Sometimes items should not have equal probability. `random.choices` (with an `s`) accepts a `weights` list:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-003-26b22c6581.html"
 width="100%"
></iframe>

Note: `random.choices` (plural, with weights) allows repeats; `random.sample` (without weights) does not allow repeats.

## Reproducibility with Seeds

The `random` module uses a pseudo-random number generator. The same seed always produces the same sequence. This is critical for reproducible tests, demos, and experiments:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-004-f9ec1d9761.html"
 width="100%"
></iframe>

## Important: random Is Not Cryptographically Secure

`random` uses a predictable algorithm (Mersenne Twister). For security-sensitive uses -- generating passwords, tokens, session IDs -- use `secrets` instead (covered in the next lesson).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-005-4b2fcee2a4.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-02-random-module-006-f781ca4084.html"
 width="100%"
></iframe>

Then add a `seed` parameter so the function can produce the same output for testing.

## Conclusion

The `random` module covers all everyday randomness: picking, sampling, shuffling, and weighting. It is simple, well-tested, and built in. The critical caveat is that it is not secure: for tokens, passwords, and session IDs, the next lesson introduces `hashlib` and `secrets`, which provide cryptographic-strength randomness and hashing.

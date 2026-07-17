# Semester 1 Final Coding Assessment: Python Fundamentals

## About This Assessment

This assessment is meant to be attempted after completing all 14 units of Semester 1. It contains 10 full-length coding questions. Each one is a standalone, real-world problem, and each draws on a different combination of topics from across the semester, so solving all 10 is a genuine test of everything covered so far.

Unlike the short OneCompiler practice questions in the Question Bank, these are meant to take 30-45 minutes each. Read the whole problem before writing any code, work through the Approach section on paper or in comments first, and only then start typing. No solutions are provided; the Approach and Examples in each question are enough to get you to a correct, working program if you follow them step by step.

| # | Question | Primary Topics |
|---|----------|-----------------|
| 1 | Movie Ticket Pricing Engine | Data Types, Operators, Control Flow |
| 2 | Password Strength Analyzer | Looping, Strings |
| 3 | Marathon Race Results Analyzer | Lists and Tuples |
| 4 | People You May Know | Sets and Dictionaries |
| 5 | Tile Runner (Staircase Ways) | Functions, Recursion |
| 6 | Zoo Enclosure Manager | Basic Object-Oriented Programming |
| 7 | Unit Conversion Toolkit | Modules and Packages |
| 8 | Server Log Analyzer | File Handling |
| 9 | ATM Withdrawal Simulator | Exception Handling |
| 10 | Contact Book: Debug and Extend | Debugging, integration of all units |

---

## Question 1: Movie Ticket Pricing Engine

**Primary Topics:** Data Types, Operators, Control Flow (Unit 2, Unit 3)
**Difficulty:** Easy

### Background

A single-screen theatre still calculates ticket prices by hand at the counter, and the counter staff keep making small arithmetic mistakes during busy weekend shows. You have been asked to write a program that calculates the final price for a group booking, given the base rules the theatre already follows on paper.

### Problem Statement

Write a program that calculates the total price for `n` tickets, given a customer's `age`, the `seat_type` (`"standard"` or `"premium"`), and the `day` of the week, using these rules, applied in order:

1. The base price of a standard ticket is ₹150. A premium (recliner) seat adds a flat ₹100 to the base price, making it ₹250.
2. Age-based discount, applied to the seat price from step 1:
   - Age under 12: 40% off.
   - Age 60 or above: 30% off.
   - Otherwise: no discount.
3. Wednesday special: if the day is `"Wednesday"` (compare case-insensitively) **and** the seat type is `"standard"`, subtract a further flat ₹20. This special does not apply to premium seats.
4. Multiply the per-ticket price from steps 1-3 by `n` to get the subtotal.
5. Group discount: if `n` is greater than 4, apply an additional 5% off the subtotal.
6. Round the final total to the nearest whole rupee.

### Input Format

Four values: `age` (int), `seat_type` (str), `day` (str), `n` (int, number of tickets, all for the same age and seat type).

### Output Format

A single line: `Final Total: Rs. <amount>`

### Constraints

- `0 <= age <= 100`
- `seat_type` is exactly `"standard"` or `"premium"` (but a user might type it in any mix of upper/lower case)
- `n >= 1`

### Example 1

Input: `age=8, seat_type="standard", day="Wednesday", n=5`

Walkthrough: base = 150 (standard). Child discount 40% -> 150 * 0.6 = 90. Wednesday + standard -> 90 - 20 = 70. Subtotal = 70 * 5 = 350. Since n=5 > 4, group discount 5% -> 350 * 0.95 = 332.5, which rounds to 332.

Output: `Final Total: Rs. 332`

### Example 2

Input: `age=65, seat_type="premium", day="Monday", n=2`

Walkthrough: base = 150 + 100 = 250 (premium). Senior discount 30% -> 250 * 0.7 = 175. Not Wednesday, and premium is excluded from the Wednesday special anyway, so no further change. Subtotal = 175 * 2 = 350. n=2 is not greater than 4, so no group discount.

Output: `Final Total: Rs. 350`

### Approach: How to Solve This

1. Start with `price = 150`, then add ₹100 if `seat_type` is `"premium"`. Normalize the input with `.lower()` before comparing.
2. Apply the age discount using `if`/`elif`/`else` on `age`. Multiply `price` by `0.6` or `0.7` as appropriate; leave it unchanged otherwise.
3. Check the Wednesday condition with `and` — both the day and the seat type must match before you subtract ₹20.
4. Multiply by `n` to get the subtotal, then check if `n > 4` before applying the group discount.
5. Use `round()` on the final value, and print it using an f-string.

### Things to Watch Out For

- Apply the discounts in the exact order given. Applying the group discount before the age discount, or the Wednesday special before rounding, will change the final number.
- `"wednesday" == "Wednesday"` is `False` in Python — you must normalize case before comparing strings.
- Test with `n` exactly equal to 4 (no group discount) and `n = 5` (group discount applies) to make sure your boundary condition uses `>` and not `>=`.

---

## Question 2: Password Strength Analyzer

**Primary Topics:** Looping, Strings (Unit 4, Unit 5)
**Difficulty:** Easy-Medium

### Background

A college's internal portal team wants a strength check on the signup form, but without pulling in any external libraries or regular expressions — just plain loops and string operations, since that is all the junior dev team currently knows.

### Problem Statement

Write a function `check_strength(username, password)` that scores a password out of 5, one point for each rule it satisfies:

1. Length is at least 8 characters.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Contains at least one digit.
5. Contains at least one special character from this set: `!@#$%^&*`

You must check rules 2-5 by looping over the characters of the password yourself (do not use a regular expression). After scoring, apply one override: if the password contains the username as a substring, case-insensitively, the score is forced to 0 regardless of how many rules it passed, and the report should say why.

Report the score and a rating:
- 0-1 points: `Weak`
- 2-3 points: `Moderate`
- 4-5 points: `Strong`

Also list which of the 5 rules failed, so the user knows what to fix.

### Input Format

Two strings: `username`, `password`.

### Output Format

The score, the rating, and a list of failed rules (or a note that the username was found inside the password).

### Constraints

- `1 <= len(username) <= 30`
- `0 <= len(password) <= 50`

### Example 1

Input: `username="rahul"`, `password="Rahul@2024"`

Walkthrough: on its own, this password would score 5 (length 10, has uppercase `R`, lowercase, digits, and `@`). But `"rahul"` (lowercased) is a substring of `"rahul@2024"` (the password lowercased), so the override applies.

Output:
```
Score: 0/5
Rating: Weak
Reason: Password must not contain your username.
```

### Example 2

Input: `username="asha"`, `password="Coding#Rocks9"`

Walkthrough: length 13 (>= 8, pass). Has uppercase (`C`, `R`). Has lowercase. Has digit `9`. Has special character `#`. All 5 rules pass. `"asha"` does not appear anywhere in `"coding#rocks9"`.

Output:
```
Score: 5/5
Rating: Strong
Failed rules: None
```

### Approach: How to Solve This

1. First check the username-substring rule. If it is a hit, skip straight to reporting a score of 0 — do not bother computing the rest.
2. Otherwise, set up five boolean flags, one per rule, all starting `False` (except the length check, which you can compute directly with `len()`).
3. Loop over the password once with a `for` character loop. Inside the loop, use `.isupper()`, `.islower()`, `.isdigit()`, and a membership check (`char in "!@#$%^&*"`) to flip the relevant flags to `True`.
4. After the loop, sum the flags (plus the length check) to get the score out of 5.
5. Use the score to pick the rating band, and build the "failed rules" list from whichever flags stayed `False`.

### Things to Watch Out For

- `"".isupper()` and similar checks behave oddly on an empty string — test with `password=""` and make sure your program doesn't crash, and correctly reports 0/5.
- The username check must be case-insensitive on both sides: lowercase both `username` and `password` before checking `in`.
- Do not just use `any(c.isupper() for c in password)` if the instructions ask you to loop explicitly — write the `for` loop yourself first, then, as a bonus, rewrite it as a one-liner and compare the two.

---

## Question 3: Marathon Race Results Analyzer

**Primary Topics:** Lists and Tuples (Unit 6)
**Difficulty:** Medium

### Background

A city marathon has just finished, and the organizers have a raw list of results as `(bib_number, name, finish_time_in_minutes)` tuples. They need a leaderboard, and they use competition-style ranking: runners who tie get the same rank, and the next rank after a tie skips ahead by the number of tied runners (so two runners tied for 1st are both "1st", and the next runner is "3rd", not "2nd").

### Problem Statement

Given a list of `(bib_number, name, finish_time_minutes)` tuples, write a program that:

1. Sorts runners by finish time, fastest first.
2. Assigns competition-style ranks, so tied finish times get the same rank.
3. Formats each finish time as `HH:MM` (e.g. 255 minutes -> `04:15`).
4. Reports the name of the fastest and the slowest runner.
5. Computes the average finish time across all runners, rounded to the nearest minute, also formatted as `HH:MM`.
6. Returns the top 3 finishers (by rank) as a list of `(rank, name, formatted_time)` tuples.
7. Tags each runner as `"Elite"` if their finish time is under 240 minutes (4 hours), otherwise `"Finisher"`.

### Input Format

A list of tuples: `[(bib_number, name, finish_time_minutes), ...]`

### Output Format

The full ranked leaderboard (rank, name, time, tag), the fastest and slowest runner's names, the average time, and the top 3 as a separate list.

### Constraints

- At least 1 runner in the list, at most 5,000.
- `finish_time_minutes` is a positive integer.

### Example

Input:
```python
runners = [
    (101, "Meera", 255),
    (102, "Kabir", 235),
    (103, "Wei", 235),
    (104, "Ana", 300),
]
```

Walkthrough: sorted by time -> Kabir (235), Wei (235), Meera (255), Ana (300). Kabir and Wei tie for finish time 235, so both get rank 1. Meera is next, but since two runners already took rank 1, Meera gets rank 3 (not rank 2). Ana gets rank 4.

Average = (255 + 235 + 235 + 300) / 4 = 256.25, rounds to 256 minutes = `04:16`.

Output:
```
Rank 1: Kabir  - 03:55 (Elite)
Rank 1: Wei    - 03:55 (Elite)
Rank 3: Meera  - 04:15 (Finisher)
Rank 4: Ana    - 05:00 (Finisher)

Fastest: Kabir
Slowest: Ana
Average finish time: 04:16

Top 3: [(1, 'Kabir', '03:55'), (1, 'Wei', '03:55'), (3, 'Meera', '04:15')]
```

### Approach: How to Solve This

1. Use `sorted()` with a `key` function (e.g. `key=lambda r: r[2]`) to sort the list of tuples by finish time without modifying the original list.
2. Walk through the sorted list with a loop, keeping track of the current rank and the finish time you last assigned a rank to. Only advance the rank counter to `position + 1` when you hit a finish time different from the previous one — that is what makes tied runners share a rank and the rank number correctly skip afterwards.
3. Write a small helper function `format_time(minutes)` that returns a zero-padded `"HH:MM"` string using integer division and the modulo operator.
4. The fastest and slowest runners are simply the first and last elements of your sorted list.
5. Compute the average with `sum(...) / len(...)`, round it, and reuse your `format_time` helper on the rounded value.
6. Build the top-3 list by slicing your ranked results: `ranked[:3]`.

### Things to Watch Out For

- Do not sort the original list in place with `.sort()` if you still need the original bib-number order elsewhere — prefer `sorted()`, which returns a new list.
- The tie-handling logic is the trickiest part. Test it by hand with a small list of 4-5 runners that includes one tie, before trusting it on a bigger dataset.
- `round(256.25)` and manually rounding "256.25 rounds to 256" match here, but Python's `round()` uses round-half-to-even for `.5` cases — worth checking with `round(2.5)` and `round(3.5)` to see the behavior for yourself.

---

## Question 4: People You May Know

**Primary Topics:** Sets and Dictionaries (Unit 7)
**Difficulty:** Medium

### Background

A small campus social app wants a "People You May Know" feature. The friendship data is stored as a dictionary mapping each username to the set of usernames they are directly friends with.

### Problem Statement

Given a friendship dictionary and a `target` username, write a function `suggest_friends(friends, target)` that:

1. Looks at every friend of `target` (the target's "direct friends").
2. Collects everyone who is a friend of at least one of those direct friends — these are the candidate suggestions.
3. Removes from the candidates: the target themself, and anyone who is already a direct friend of the target.
4. For each remaining candidate, counts how many of the target's direct friends they have in common (the "mutual friends").
5. Returns the candidates sorted by mutual friend count, highest first; ties broken alphabetically by name.

### Input Format

A dictionary `{username: set_of_friend_usernames, ...}`, and a `target` username string.

### Output Format

A list of `(candidate_name, mutual_count, sorted_list_of_mutual_friend_names)` tuples.

### Constraints

- The friendship dictionary is symmetric: if `"a"` is in `friends["b"]`, then `"b"` is in `friends["a"]`.
- `target` is guaranteed to exist as a key in the dictionary.

### Example

Input:
```python
friends = {
    "amit": {"neha", "raj"},
    "neha": {"amit", "priya", "raj"},
    "raj": {"amit", "neha", "priya", "zara"},
    "priya": {"neha", "raj", "zara"},
    "zara": {"raj", "priya"},
}
target = "amit"
```

Walkthrough: `amit`'s direct friends are `{neha, raj}`. Friends of `neha` are `{amit, priya, raj}`; friends of `raj` are `{amit, neha, priya, zara}`. Union of those, minus `amit`'s own friends and `amit` himself, leaves candidates `{priya, zara}`. `priya` is a mutual friend through both `neha` and `raj` (count 2). `zara` is a mutual friend only through `raj` (count 1).

Output:
```python
[('priya', 2, ['neha', 'raj']), ('zara', 1, ['raj'])]
```

### Approach: How to Solve This

1. Get `direct = friends[target]`.
2. Build an empty set `candidates = set()`, and for every friend `f` in `direct`, union in `friends[f]` using `|=`.
3. Remove the noise: `candidates -= direct` (drops anyone already a direct friend), then `candidates.discard(target)` (drops the target if they somehow appear).
4. For each remaining candidate `c`, build the mutual-friends list with a list comprehension: everyone `f` in `direct` such that `c` is in `friends[f]`.
5. Sort the final list with `sorted(..., key=lambda x: (-x[1], x[0]))` — negating the count sorts it descending while the name still sorts ascending.

### Things to Watch Out For

- `discard()` versus `remove()` on sets: `remove()` raises a `KeyError` if the item is not present, `discard()` does not. Since the target should never actually appear in the candidate set if your union logic is right, using `discard()` here is a safety net, not a workaround for a bug.
- A user with zero friends (`friends["someone"] = set()`) should not crash your function — it should simply return an empty list, since there are no friends-of-friends to look at.
- Building the mutual list requires checking membership in a set (`c in friends[f]`), which is fast; doing the equivalent check against a list would be needlessly slower and is worth noting even at this scale.

---

## Question 5: Tile Runner (Counting Staircase Ways)

**Primary Topics:** Functions, Recursion (Unit 8)
**Difficulty:** Medium

### Background

In the mobile game "Tile Runner," a character climbs a staircase of `n` tiles, and on each move can advance by any of a fixed set of step sizes (for example, 1, 2, or 3 tiles at a time). The game designers want to know, for level-balancing purposes, exactly how many distinct paths (distinct orderings of moves) exist to reach the top of a staircase of a given height.

### Problem Statement

Write a function `count_ways(n, steps=(1, 2, 3))` that returns the number of distinct ordered sequences of moves (each move taken from `steps`) that sum to exactly `n`. Two sequences that use the same moves in a different order count as different paths (e.g. `1+2` and `2+1` are two separate ways to reach 3).

Use recursion: the number of ways to reach `n` is the sum, over every step size `s` in `steps`, of the number of ways to reach `n - s`. The base case is that there is exactly 1 way to reach 0 (take no more moves), and 0 ways to reach a negative number.

Because the naive recursion recomputes the same sub-values many times, add memoization: cache the result for each value of `n` you have already solved, so it is only computed once.

Also write a second version, `count_ways_args(n, *steps)`, with the same behavior but where the allowed step sizes are passed as separate arguments instead of a tuple, e.g. `count_ways_args(4, 1, 2)`.

### Input Format

An integer `n`, and either a tuple of allowed step sizes or, for the second version, the step sizes as separate arguments.

### Output Format

A single integer: the number of distinct paths.

### Constraints

- `0 <= n <= 40`
- All step sizes are distinct positive integers, at most `n`.

### Example 1

Input: `count_ways(4, steps=(1, 2))`

Walkthrough: the ways to make 4 using steps of 1 and 2 are: `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`.

Output: `5`

### Example 2

Input: `count_ways(3)` (using the default `steps=(1, 2, 3)`)

Walkthrough: `1+1+1`, `1+2`, `2+1`, `3`.

Output: `4`

### Approach: How to Solve This

1. Write the plain recursive version first, without memoization, and confirm it gives the right answer on Example 2 even if it is slow.
2. Add a cache. The simplest approach for a student-written cache is a dictionary declared outside the recursive helper (or passed through the recursion), storing `n -> number_of_ways` once computed.
3. Before you reach for a mutable default argument like `def count_ways(n, steps=(1,2,3), cache={})`, think through what happens on the *second* call to this function with a different `n` — does the cache from the first call leak into the second? This is a well-known Python pitfall: mutable default arguments are created once, when the function is defined, and reused across every call. Design your cache so it does not carry stale state between independent calls (for example, create a fresh cache inside the function body on every call, or use a nested helper function that closes over a fresh cache each time).
4. For `count_ways_args`, notice that `*steps` collects the extra positional arguments into a tuple automatically — the body of the function can reuse the exact same logic as `count_ways` once you have that tuple.

### Things to Watch Out For

- Test `n=0` directly: the answer should be 1 (there is exactly one way to "climb" zero tiles — do nothing), not 0.
- Test with a step size larger than `n` (e.g. `count_ways(2, steps=(1, 5))`) to make sure your negative-base-case handles it instead of crashing or looping.
- Time your memoized version against the plain recursive version for `n=30` — the difference should be dramatic, and is worth seeing for yourself rather than taking on faith.

---

## Question 6: Zoo Enclosure Manager

**Primary Topics:** Basic Object-Oriented Programming (Unit 9)
**Difficulty:** Medium

### Background

A small city zoo wants a simple digital system to track the animals across its enclosures — how much food each animal needs per day, and a quick way to hear what sound each animal makes for the zoo's new interactive kiosk.

### Problem Statement

1. Define a base class `Animal` with attributes `name`, `age`, and `daily_food_kg`, set in `__init__`. Give it a method `make_sound()` that raises `NotImplementedError` — every real animal subclass must override it.
2. Define at least two subclasses of `Animal`:
   - `Lion`, which overrides `make_sound()` to return `"Roar"`.
   - `Elephant`, which overrides `make_sound()` to return `"Trumpet"`.

   Each subclass should also set a `diet` attribute (`"meat"` for `Lion`, `"plants"` for `Elephant`) in its own `__init__`, in addition to calling the parent `__init__` for the shared attributes.
3. Define a class `ZooEnclosure` that manages a collection of `Animal` objects, with methods:
   - `add_animal(animal)` — adds an animal to the enclosure.
   - `total_daily_food()` — returns the sum of `daily_food_kg` across all animals.
   - `oldest_animal()` — returns the `Animal` object with the highest `age` (assume no ties for this method).
   - `animals_needing_checkup()` — returns a list of animals aged 10 or older, since the zoo's policy is that older animals get a mandatory annual checkup.

### Input Format

Construct `Animal` subclass instances directly with `(name, age, daily_food_kg)`, then add them to a `ZooEnclosure`.

### Output Format

Whatever each method above is documented to return, printed or inspected directly.

### Constraints

- An enclosure holds at least 1 and at most 200 animals.
- `age >= 0`, `daily_food_kg > 0`.

### Example

```python
zoo = ZooEnclosure()
zoo.add_animal(Lion("Leo", 5, 8))
zoo.add_animal(Elephant("Ellie", 12, 150))

zoo.total_daily_food()          # 158
zoo.oldest_animal().name        # "Ellie"
zoo.animals_needing_checkup()   # [<Elephant Ellie>]

for animal in zoo.animals:
    print(animal.name, "says", animal.make_sound())
# Leo says Roar
# Ellie says Trumpet
```

### Approach: How to Solve This

1. Start with the `Animal` base class. Its `__init__` should accept and store `name`, `age`, `daily_food_kg`. Its `make_sound()` should be exactly `raise NotImplementedError`.
2. Write `Lion` and `Elephant` as `class Lion(Animal):`. In each subclass `__init__`, call `super().__init__(name, age, daily_food_kg)` before setting the subclass-specific `diet` attribute — this avoids repeating the same three lines of assignment in every subclass.
3. Override `make_sound()` in each subclass to simply `return` the right string. This is polymorphism: calling `.make_sound()` on any `Animal` reference runs the correct subclass's version automatically.
4. `ZooEnclosure` just needs a list attribute (e.g. `self.animals = []`) that `add_animal` appends to. `total_daily_food`, `oldest_animal`, and `animals_needing_checkup` are then straightforward loops or comprehensions over that list.
5. Test `oldest_animal()` and `total_daily_food()` on an enclosure with just one animal before testing with several, to isolate bugs in the aggregation logic from bugs in the loop itself.

### Things to Watch Out For

- If you forget to call `super().__init__(...)` inside a subclass, `name`, `age`, and `daily_food_kg` will simply not exist on that object, and you'll get an `AttributeError` the first time you try to use them — not at object-creation time.
- Calling `make_sound()` directly on a plain `Animal` object (not a subclass) should raise `NotImplementedError` — this is intentional, and confirms your base class is correctly forcing subclasses to override it.
- Decide what `oldest_animal()` should do on an empty enclosure before you're asked — even though the constraint guarantees at least 1 animal, thinking through this now is good practice for Question 9, where every edge case matters.

---

## Question 7: Unit Conversion Toolkit

**Primary Topics:** Modules and Packages (Unit 10)
**Difficulty:** Easy-Medium

### Background

A study-abroad prep app needs a small, reusable set of unit conversion functions (distance, weight, and temperature) that can be imported cleanly into any script, rather than copy-pasted everywhere the app needs a conversion.

### Problem Statement

Build a Python package named `converters` with this structure:

```
converters/
    __init__.py
    length.py
    weight.py
    temperature.py
main.py
```

1. `length.py` should define `km_to_miles(km)`, returning `km * 0.621371`, rounded to 2 decimal places.
2. `weight.py` should define `kg_to_lb(kg)`, returning `kg * 2.20462`, rounded to 2 decimal places.
3. `temperature.py` should define `celsius_to_fahrenheit(c)`, returning `c * 9 / 5 + 32`.
4. In `converters/__init__.py`, import the three functions so that they can also be accessed directly as `converters.km_to_miles`, `converters.kg_to_lb`, and `converters.celsius_to_fahrenheit`, without the caller needing to know which submodule each one lives in.
5. In `main.py`, demonstrate all three of these import styles, each used at least once:
   - `import converters` then calling `converters.km_to_miles(...)`
   - `from converters import weight` then calling `weight.kg_to_lb(...)`
   - `from converters.temperature import celsius_to_fahrenheit as c_to_f` then calling `c_to_f(...)`

### Input Format

Direct function calls with numeric arguments, as shown in the examples.

### Output Format

The converted numeric value from each function call.

### Constraints

- All inputs are valid numbers (int or float); no need to validate input types for this question.

### Example

```python
km_to_miles(10)              # 6.21
kg_to_lb(5)                  # 11.02
celsius_to_fahrenheit(0)     # 32.0
celsius_to_fahrenheit(100)   # 212.0
```

### Approach: How to Solve This

1. Create the folder structure first, exactly as shown, with an empty `converters/__init__.py` to begin with — an `__init__.py` file (even empty) is what tells Python that `converters/` is a package, not just a folder.
2. Write each conversion function in its own file. Keep them simple, pure functions: given an input number, return the converted number. No printing inside these functions.
3. Edit `__init__.py` to add three import lines, e.g. `from .length import km_to_miles`. The leading dot means "from a module inside this same package."
4. In `main.py`, work through the three import styles one at a time, printing a result after each, so you can confirm each style resolves to the same underlying function.
5. Run `main.py` from the directory that contains both `converters/` and `main.py` — package imports are relative to where Python resolves the package from, not from inside the package folder itself.

### Things to Watch Out For

- A very common mistake: running `main.py` from inside the `converters/` folder itself, which breaks the import. Always run it from the parent folder.
- If `celsius_to_fahrenheit(0)` prints `32` instead of `32.0`, check whether you accidentally used integer division (`//`) instead of true division (`/`) somewhere in the formula.
- Once all three functions are importable via `converters.<name>`, try `import converters; print(dir(converters))` to see for yourself what your `__init__.py` exposed at the package level.

---

## Question 8: Server Log Analyzer

**Primary Topics:** File Handling (Unit 11)
**Difficulty:** Medium

### Background

A small college project's web server writes every incoming request to a plain text log file. The team wants a quick script that reads that log and flags IP addresses that look like they might be scanning for vulnerabilities (a burst of failed requests), instead of scrolling through thousands of lines by hand.

### Problem Statement

You are given a log file `access.log`, where each line has this space-separated format:

```
<date> <time> <ip_address> <method> <path> <status_code>
```

Write a program that:

1. Reads `access.log` line by line using a `with open(...)` block.
2. Parses each line into its six fields using `.split()`.
3. Counts how many requests fall under each distinct status code.
4. For each IP address, counts how many of its requests had a status code of 400 or above (a "failed" request).
5. Flags any IP address with 3 or more failed requests as suspicious.
6. Writes a formatted summary to a new file, `summary.txt`, in the exact format shown in the example below.

### Input Format

A text file, `access.log`, with one request per line.

### Output Format

A new file, `summary.txt`, containing the total request count, a breakdown by status code, and the list of suspicious IPs.

### Constraints

- The log file has at least 1 line and at most 100,000 lines.
- Status codes are standard 3-digit HTTP codes (e.g. 200, 404, 500).

### Example

Input file `access.log`:
```
2026-07-15 09:12:33 192.168.1.5 GET /home 200
2026-07-15 09:13:01 192.168.1.9 GET /login 404
2026-07-15 09:13:47 192.168.1.5 GET /profile 200
2026-07-15 09:14:02 192.168.1.9 GET /login 404
2026-07-15 09:15:10 192.168.1.9 GET /login 500
2026-07-15 09:16:20 192.168.1.2 GET /home 200
```

Walkthrough: 6 total requests. Status breakdown: 200 appears 3 times, 404 appears 2 times, 500 appears once. IP `192.168.1.9` has 3 failed requests (two 404s and one 500), which meets the suspicious threshold of 3.

Output file `summary.txt`:
```
LOG SUMMARY
===========
Total requests: 6

Status code breakdown:
  200: 3
  404: 2
  500: 1

Suspicious IPs (3+ failed requests):
  192.168.1.9 - 3 failed requests
```

### Approach: How to Solve This

1. Open and read the log file with `with open("access.log") as f:`, then loop over `f` directly — this reads it one line at a time, which matters once the file has thousands of lines.
2. For each line, call `.strip()` to remove the trailing newline, then `.split()` to break it into the 6 fields. Unpack them into named variables so the rest of your code is readable (e.g. `date, time, ip, method, path, status = line.split()`).
3. Use two dictionaries: one mapping `status_code -> count`, and one mapping `ip -> failed_count`. Update both inside the same loop, using `dict.get(key, 0) + 1` (or a `collections.Counter`, if you have looked ahead to it) so you don't need a separate check for "have I seen this key before."
4. After the loop, decide which IPs are suspicious by filtering your `ip -> failed_count` dictionary for values `>= 3`.
5. Open a second file, `summary.txt`, with `with open("summary.txt", "w") as f:`, and use `f.write(...)` with f-strings to produce the exact formatting shown, including the blank lines.

### Things to Watch Out For

- Status codes come out of `.split()` as strings, not integers — comparing `status >= "400"` against a string works by accident for 3-digit codes but is fragile; convert to `int(status)` before comparing.
- If `access.log` has a trailing blank line at the end of the file, an unguarded `.split()` on it will produce an empty list and crash your unpacking. Skip empty lines with a quick `if not line.strip(): continue`.
- Open files with the `with` statement rather than a bare `open()`/`close()` pair, so the file is guaranteed to close even if something in your loop raises an exception partway through.

---

## Question 9: ATM Withdrawal Simulator

**Primary Topics:** Exception Handling (Unit 12)
**Difficulty:** Medium-Hard

### Background

An ATM has stricter validation rules than a simple bank transfer: notes only come in multiples of ₹100, there's a hard daily withdrawal cap regulators require, and every single validation failure needs a distinct, specific error message so the physical machine can show the right instruction to the customer.

### Problem Statement

Design a small exception hierarchy:

```
ATMError(Exception)              # base class for all ATM-related errors
    InvalidAmountError(ATMError)
    InsufficientFundsError(ATMError)
    DailyLimitExceededError(ATMError)
```

Write a class `ATM` with a `balance`, a `daily_limit` (default ₹25,000), and a running `daily_used` total (starts at 0). It should have a method `withdraw(amount)` that:

1. Raises `InvalidAmountError` if `amount` is not a positive multiple of 100.
2. Raises `InsufficientFundsError` if `amount` is more than the current `balance`.
3. Raises `DailyLimitExceededError` if `daily_used + amount` would exceed `daily_limit`.
4. Otherwise, deducts `amount` from `balance`, adds it to `daily_used`, and returns the new balance.

Checks must run in the order listed above — an invalid amount should be reported as invalid even if it would also have exceeded the balance.

Write a driver loop that attempts a list of withdrawal amounts against one `ATM` instance, catches each exception type separately with its own user-facing message, and uses a `finally` block that always prints the current balance and daily-used total after every attempt, whether it succeeded or failed.

### Input Format

An `ATM` starting balance and daily limit, and a list of withdrawal amounts to attempt in sequence.

### Output Format

For each attempted withdrawal: either a success message with the new balance, or the specific error message for whichever exception was raised — followed, in both cases, by the balance/daily-used line from `finally`.

### Constraints

- `balance >= 0`
- Withdrawal amounts attempted may be any integer, including negative numbers and non-multiples of 100 — your validation must handle all of them.

### Example

Setup: `ATM(balance=5000, daily_limit=25000)`, attempting withdrawals `[4700, 5300, 4800, 21000]` in order.

Walkthrough:
- `4700`: not a multiple of 100 -> `InvalidAmountError`.
- `5300`: a valid multiple of 100, but greater than the balance of 5000 -> `InsufficientFundsError`.
- `4800`: valid, within balance, within daily limit (0 used so far) -> succeeds. Balance becomes 200, daily_used becomes 4800.
- `21000`: valid on its own, but `4800 + 21000 = 25800`, which exceeds the daily limit of 25000 -> `DailyLimitExceededError`. (It would also fail on insufficient balance, since only 200 remains, but the daily limit check is not reached before the balance check in the required order — check your own ordering against this case carefully.)

Output:
```
Attempt: Rs. 4700 -> Invalid amount: must be a positive multiple of 100.
  [Balance: Rs. 5000, Daily used: Rs. 0]
Attempt: Rs. 5300 -> Insufficient funds: balance is Rs. 5000.
  [Balance: Rs. 5000, Daily used: Rs. 0]
Attempt: Rs. 4800 -> Success. New balance: Rs. 200.
  [Balance: Rs. 200, Daily used: Rs. 4800]
Attempt: Rs. 21000 -> Insufficient funds: balance is Rs. 200.
  [Balance: Rs. 200, Daily used: Rs. 4800]
```

### Approach: How to Solve This

1. Define the four exception classes first. Each is just `class InvalidAmountError(ATMError): pass` — the value is in having distinct types to catch separately, not in adding custom behavior to them.
2. Write `withdraw()` with three `if` checks in sequence, each doing `raise SomeError("message")` and returning immediately (a `raise` exits the function, so you don't need `elif` here — each check only runs if the previous ones didn't already raise).
3. In the driver loop, use one `try` block per withdrawal attempt, with separate `except InvalidAmountError as e:`, `except InsufficientFundsError as e:`, `except DailyLimitExceededError as e:` blocks — order them from most specific to most general if any of them shared a parent-child relationship with each other (here they don't, so order between them doesn't matter, but all three must come before a bare `except ATMError` if you add one as a catch-all).
4. Add a `finally` block after the `except` blocks. Code in `finally` runs whether the `try` succeeded or an exception was caught — use it for the balance/daily-used line that must appear after every attempt.
5. Walk through the worked example above by hand, step by step, before running your code, so you know exactly what output to expect and can catch a logic bug immediately rather than guessing.

### Things to Watch Out For

- `amount % 100 == 0` is `True` for `amount = 0` and for negative multiples of 100 like `-200` — make sure your "positive multiple of 100" check actually requires `amount > 0` as well.
- Catching `Exception` (or your base `ATMError`) before your specific exception classes in the same `try` will silently swallow all of them into one generic handler — always catch the most specific exceptions first.
- Confirm for yourself that the `finally` block runs even when a `raise` happens inside the `try` and is caught by an `except` — add a `print("in finally")` temporarily if you want to see the order of execution directly.

---

## Question 10: Contact Book — Debug and Extend

**Primary Topics:** Debugging, and integration of Functions, File Handling, and Exception Handling (Unit 13, closing question)
**Difficulty:** Hard

### Background

A junior developer on your team wrote a simple JSON-backed contact book, but it's shipped with three bugs that only show up once you actually use the app for more than a single call. Your job is to find them the way you would on a real team: by running the code, watching what it actually does versus what it should do, and fixing the root cause rather than papering over the symptom.

### Problem Statement

Here is the contact book as it currently exists:

```python
import json

def add_contact(name, phone, contacts=[]):
    contacts.append({"name": name, "phone": phone})
    return contacts

def search_contact(name, contacts):
    for c in contacts:
        if c["name"] == name:
            return c
    return None

def load_contacts(filepath="contacts.json"):
    file = open(filepath, "r")
    data = json.load(file)
    file.close()
    return data

def save_contacts(contacts, filepath="contacts.json"):
    with open(filepath, "w") as f:
        json.dump(contacts, f)
```

**Bug 1:** Call `add_contact("Asha", "9876500001")` and then, in a completely separate part of the program, call `add_contact("Vikram", "9876500002")` without passing a `contacts` list to either call. Inspect what the second call actually returns. It is not just Vikram's contact — explain why, in terms of how Python evaluates default arguments, and fix `add_contact` so each call that doesn't receive an explicit list starts from a clean one.

**Bug 2:** Delete `contacts.json` (or run this on a machine where it has never been created) and call `load_contacts()`. It crashes instead of giving a new user an empty contact list to start from. Fix `load_contacts` so a missing file results in an empty list, while other problems (like a corrupted file) still surface as clear errors rather than being silently hidden.

**Bug 3:** Add a contact with `add_contact("Raj Mehta", "9876500003", contacts)`, then call `search_contact("raj mehta", contacts)`. It returns `None` even though the contact clearly exists. Fix the search so it is case-insensitive.

**New feature:** After fixing all three bugs, add a custom exception `DuplicateContactError(Exception)`. Modify `add_contact` to raise it if the phone number being added already belongs to another contact in the list — compare phone numbers by digits only, ignoring any spaces or hyphens (so `"98765-00001"` and `"9876500001"` should be treated as the same number). Write a small driver that attempts to add a duplicate and shows the exception being caught with a clear message.

### Input Format

Direct function calls, as described in each bug above.

### Output Format

For each bug: what you observed before the fix, and the corrected function. For the new feature: a short demonstration of `DuplicateContactError` being raised and caught.

### Constraints

- Treat the three bugs as independent — fixing one should not require you to have already fixed another.
- The new `DuplicateContactError` check should not reject a contact for having the same name as an existing one, only the same phone number.

### Example

Before the fix, Bug 1 in a Python shell:
```python
>>> add_contact("Asha", "9876500001")
[{'name': 'Asha', 'phone': '9876500001'}]
>>> add_contact("Vikram", "9876500002")
[{'name': 'Asha', 'phone': '9876500001'}, {'name': 'Vikram', 'phone': '9876500002'}]
```
Vikram's call was supposed to start a brand-new one-contact list, since no `contacts` argument was passed in, but Asha is still there from the earlier call.

After the fix, the same two calls should each return a list containing only the one contact just added, unless the caller deliberately passes an existing list in.

New feature demonstration:
```python
contacts = []
add_contact("Priya", "98765-00004", contacts)
add_contact("Neha", "9876500004", contacts)
# raises DuplicateContactError: "9876500004 is already registered to Priya"
```

### Approach: How to Solve This

1. For Bug 1, read up on when Python evaluates a default argument value like `contacts=[]` — it happens once, when the `def` statement runs, not on every call. That single list object is then reused as the default on every call that doesn't supply its own. The standard fix is `def add_contact(name, phone, contacts=None):` followed by `if contacts is None: contacts = []` as the first line of the function body.
2. For Bug 2, wrap the `open()` and `json.load()` calls in a `try/except FileNotFoundError:` that returns `[]`. Leave other exceptions (like `json.JSONDecodeError` from a corrupted file) unhandled for now, or handled separately with their own message — don't let a blanket `except:` hide a real data-corruption problem behind the same "starting fresh" message a missing file gets.
3. For Bug 3, lowercase both sides of the comparison in `search_contact`: `if c["name"].lower() == name.lower():`.
4. For the new feature, write a small helper that strips out any character that isn't a digit from a phone string (e.g. loop over the string and keep only characters where `.isdigit()` is `True`, or use `"".join(...)`). Compare the cleaned version of the incoming phone number against the cleaned version of every existing contact's phone number before appending.
5. Fix and test the bugs one at a time, in the order given, re-running each specific reproduction scenario after your fix to confirm the bug is actually gone before moving to the next one.

### Things to Watch Out For

- Bug 1 and Bug 3 are both "silent" bugs — the program does not crash, it just quietly returns the wrong thing. These are more dangerous in real systems than a crash, because nobody notices until the wrong data has already been relied on somewhere else. Get in the habit of checking return values against what you expect, not just checking that a program "ran without errors."
- After fixing Bug 2, make sure you did not accidentally catch `FileNotFoundError` so broadly that it also swallows a genuine `PermissionError` on a file that exists but can't be read — catch the specific exception type you intend to handle.
- For the duplicate-phone check, decide what should happen if `contacts` is empty — your loop should simply find no match and allow the add, without a special case.

---

## Wrapping Up

If you were able to complete all 10 questions without looking at the Approach section until after your first attempt, you have a solid grip on Semester 1. If you needed the Approach steps for several of them, that's normal too — go back afterward and try writing each one again from a blank file, without re-reading the steps, a day or two later. That second attempt, done from memory, is what actually cements the material before Semester 2 builds on top of it.

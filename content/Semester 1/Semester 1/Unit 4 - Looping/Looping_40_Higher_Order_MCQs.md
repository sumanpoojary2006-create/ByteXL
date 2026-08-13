# Unit 4: Looping - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 4 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, boundary testing, repair selection, behavior comparison, and practical application
- Opening coverage: Questions 1–10 collectively represent all seven Unit 4 taxonomy subtopics
- Pattern coverage: four distinct output-pattern problems appear in Questions 4 and 26–28
- Metadata: every question identifies its taxonomy and primary assessment behaviour
- Student expectation: predict or diagnose before running the code

---

## Questions

### 1. Repairing the badge-number endpoint

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying and repairing an incorrect boundary

An event desk must print badge numbers 1 through 6. The current loop omits badge 6:

```python
for badge in range(1, 6):
    print(badge)
```

Which smallest replacement preserves the starting value and includes the required endpoint without printing any extra badge?

A. `range(0, 6)`  
B. `range(1, 6, 2)`  
C. `range(1, 7)`  
D. `range(2, 7)`

### 2. Retrying a password for an unknown number of attempts

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `while-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate programming structure

A hostel Wi-Fi screen must keep asking until the correct password is entered. The designer cannot know which attempt will succeed. Which structure expresses that requirement most naturally?

A. A `while` loop controlled by whether the password is still incorrect  
B. A `for` loop fixed at exactly one attempt  
C. One `if` statement with no repetition  
D. A loop over the letters in the password

### 3. Completing direct iteration over changing data

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing iteration code

A warehouse stores recipient names in a list whose length changes each day:

```python
recipients = ["Asha", "Ravi", "Meera"]

for __________:
    print(f"Label for {recipient}")
```

Which completion visits each stored name directly and continues to work when the list length changes?

A. `recipient in range(3)`  
B. `recipients in recipient`  
C. `recipient in "recipients"`  
D. `recipient in recipients`

### 4. Tracing a shrinking launch-banner pattern

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Pattern problem; tracing nested loops

A launch display builds a row-dependent banner:

```python
for row in range(3, 0, -1):
    for column in range(row):
        print("#", end="")
    print()
```

Which banner will be produced after the inner loop finishes for every row?

A.

```text
#
##
###
```

B.

```text
###
##
#
```

C.

```text
###
###
###
```

D.

```text
##
#
```

### 5. Selecting data that exposes a broken accumulator

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; choosing an input that exposes a defect

Two donation reports are being compared:

Version A:

```python
total = 0
for amount in donations:
    total += amount
```

Version B:

```python
total = 0
for amount in donations:
    total = amount
```

Which input is the smallest clear demonstration that Version B keeps only the final donation instead of accumulating the complete total?

A. `[]`  
B. `[10, 20]`  
C. `[10]`  
D. `[0]`

### 6. A counter approaches its stopping point

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `while-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction; final value tracing

A loading screen displays:

```python
step = 3

while step <= 5:
    print(step)
    step += 1
```

Which progress sequence will the user see before the screen moves on?

A. `3, 4, 5, 6`  
B. `3` repeated without stopping  
C. `4, 5, 6`  
D. `3, 4, 5`

### 7. Processing commands until the stop signal

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a sentinel-controlled exit

A console receives the commands `"add"`, `"remove"`, `"quit"`, and `"add"` in that order. Its loop stops as soon as `"quit"` is read. Which command history should the application retain as processed work?

A. `"add"`, `"remove"`; the stop signal ends the session before the final command  
B. All four entries, because a sentinel is processed like ordinary work  
C. `"quit"` only  
D. The final `"add"` only

### 8. A progress display frozen at one percent

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an infinite-loop logic bug

A program appears frozen while repeatedly displaying `1%`:

```python
progress = 1

while progress <= 100:
    print(progress)
```

Which review finding explains the observed behavior?

A. The condition should use `for` as a comparison operator  
B. The initial value must be 100  
C. Nothing in the loop changes `progress`, so the true condition never moves toward false  
D. `print` automatically resets counters to 1

### 9. Completing an unknown-length confirmation retry

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `while-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing validation condition

A checkout should request confirmation again while the response is neither `"yes"` nor `"no"`. The number of invalid attempts is unknown:

```python
response = input("Confirm yes/no: ").lower()

while ______________________________:
    response = input("Enter yes or no: ").lower()
```

Which condition keeps retrying exactly while the current response is invalid?

A. `response != "yes" or response != "no"`  
B. `response not in ("yes", "no")`  
C. `response == "yes" and response == "no"`  
D. `response in ("yes", "no")`

### 10. The quit command is treated as ordinary work

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected behaviour; smallest correct repair

A command processor contains:

```python
command = ""

while command != "quit":
    command = input("Command: ")
    print(f"Processing {command}")
```

Users complain that the screen displays `Processing quit` just before closing. Which smallest repair preserves the sentinel loop while preventing that misleading action?

A. Remove the loop condition and process every entry forever  
B. Change the sentinel to an empty string without telling users  
C. Move the `input` call after the `print`  
D. After reading the command, break when it equals `"quit"`; otherwise process it

### 11. Five positions generated by one range

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based range prediction

A carousel assigns zero-based positions using:

```python
for position in range(5):
    print(position)
```

Which position list reaches the display?

A. `1, 2, 3, 4, 5`  
B. `0, 1, 2, 3, 4, 5`  
C. `0, 1, 2, 3, 4`  
D. `5` only

### 12. Even-numbered lockers below eight

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing start, stop, and step

A maintenance tool checks lockers selected by `range(2, 8, 2)`. Which locker sequence will it visit?

A. `2, 4, 6`  
B. `2, 4, 6, 8`  
C. `0, 2, 4, 6`  
D. `2, 3, 4, 5, 6, 7`

### 13. A ten-line multiplication table

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Completing an inclusive range boundary

A table must include multipliers 1 through 10, including both endpoints. Which range supplies exactly those values?

A. `range(10)`  
B. `range(1, 10)`  
C. `range(0, 11)`  
D. `range(1, 11)`

### 14. A launch countdown that stops before zero

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a descending range

A display must count `10, 9, 8, ... 1` and then show a separate `"Launch"` message. Which range drives the numeric countdown correctly?

A. `range(1, 10, -1)`  
B. `range(10, 0, -1)`  
C. `range(10, 1, 1)`  
D. `range(0, 10, -1)`

### 15. Verifying two fixed-count calibration loops

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `for-loops-and-range`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

A machine team proposes two versions of the same fixed-count calibration:

Version A:

```python
count = 0
while count < 500:
    calibrate()
    count += 1
```

Version B:

```python
for _ in range(500):
    calibrate()
```

Assuming `calibrate()` does not alter `count`, which equivalence finding is correct?

A. Both call `calibrate()` exactly 500 times; Version B expresses the known count with less manual state  
B. Version A calls it 499 times because its comparison is strict  
C. Version B calls it 501 times because `range(500)` includes both 0 and 500  
D. They are equivalent only if `count` begins at 1

### 16. Reading a tracking code one character at a time

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based sequence trace

A scanner runs:

```python
for character in "Code":
    print(character)
```

Which scan record matches the order of iteration?

A. `Code` is treated as one indivisible item  
B. `e, d, o, C`  
C. `C, o, d, e`  
D. `0, 1, 2, 3`

### 17. Sending one greeting per stored name

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting direct sequence iteration

A list contains `names = ["Asha", "Ravi", "Meera"]`. The application needs each name itself, not its numeric position. Which loop is the clearest Python expression of the requirement?

A. `for name in range(3):`  
B. `for name in names:`  
C. `while names:` without changing the list  
D. `for names in "name":`

### 18. Numbering a queue from one

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriate enumeration structure

A help desk must display:

```text
1 Asha
2 Ravi
3 Meera
```

Which loop obtains each position and name together without manually maintaining a counter?

A. `for name in range(names):`  
B. `for position in names:`  
C. `for name, position in names:`  
D. `for position, name in enumerate(names, start=1):`

### 19. Counting vowels in a visitor name

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing iteration with a condition; final value identification

A kiosk applies this logic to the name `"Asha"`:

```python
vowels = 0

for letter in "Asha":
    if letter.lower() in "aeiou":
        vowels += 1
```

Which count will be stored for the visitor?

A. `2`, for `A` and `a`  
B. `1`, because uppercase letters are ignored  
C. `3`, because `h` is treated as a vowel  
D. `4`, because every character is counted

### 20. Producing positions and values without parallel bookkeeping

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest structural repair

A developer writes one loop over a product list and a separate counter that must be incremented on every pass. A missed increment causes duplicate row numbers. Which refactor removes that synchronisation risk while preserving access to both values?

A. Loop over `range(1000)` regardless of the list length  
B. Convert every product name into a number  
C. Use `enumerate(products, start=1)` to receive the row number and product together  
D. Replace the loop with copied output statements

### 21. Stopping at the first square above fifty

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a search terminated by `break`

A search checks positive integers in order and stops at the first one whose square is greater than 50. Which number will be recorded when `break` ends the search?

A. `6`  
B. `7`  
C. `9`  
D. `8`

### 22. Skipping sponsored positions

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction with `continue`

A feed prototype skips every even position and displays the remaining positions from 1 through 5:

```python
for position in range(1, 6):
    if position % 2 == 0:
        continue
    print(position)
```

Which positions remain visible?

A. `2, 4`  
B. `1, 3, 5`  
C. `1` only  
D. `1, 2, 3, 4, 5`

### 23. A search succeeds before the list ends

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about `break` and loop `else`

A product search uses a `for` loop with `break` when the target is found and an attached `else` that displays `"Not found"`. The target appears as the second item. Which interface behavior follows Python's loop-`else` rule?

A. The search breaks at the match, and the `"Not found"` message is skipped  
B. The `else` runs because every `for` loop must finish with it  
C. Both success and `"Not found"` appear  
D. The loop ignores the target and checks only the last item

### 24. A complete search finds no matching ID

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about normal completion and loop `else`

A list search reaches its end without ever executing `break`. An `else` block is attached directly to the loop. Which status should the application produce?

A. It must repeat the search forever  
B. It must pretend the last item matched  
C. The loop's `else` runs and can report that no matching ID was found  
D. The `else` runs only if the first item fails

### 25. A skipped update traps a `while` loop

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `loop-control-statements`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an infinite-loop interaction with `continue`

A filter contains:

```python
number = 0

while number < 5:
    if number % 2 == 0:
        continue
    number += 1
```

The process never moves beyond its first value. Which explanation identifies the interaction causing the failure?

A. `continue` automatically ends every loop  
B. The modulo test changes `number` back to zero  
C. `number += 1` runs twice on every even value  
D. At zero, `continue` skips the update, so the next pass tests the unchanged zero again

### 26. Repairing a rectangle with an extra column

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Pattern problem; smallest correct repair

A ticket printer should create a rectangle with 3 rows and 4 stars per row. The current inner range prints five stars:

```python
for row in range(3):
    for column in range(5):
        print("*", end="")
    print()
```

Which smallest repair produces the required rectangle?

A. Change the outer range to `range(4)`  
B. Change the inner range to `range(4)`  
C. Change both ranges to `range(3)`  
D. Move the empty `print()` inside the inner loop

### 27. Tracing a row-number triangle

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Pattern problem; nested-loop output prediction

A classroom display repeats each row number as many times as the row number itself:

```python
for row in range(1, 4):
    for column in range(row):
        print(row, end="")
    print()
```

Which number pattern reaches the display?

A.

```text
123
123
123
```

B.

```text
111
22
3
```

C.

```text
1
22
333
```

D.

```text
1
2
3
```

### 28. A growing staircase of stars

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Pattern problem; nested-loop output prediction

A pattern generator uses:

```python
for row in range(1, 4):
    for column in range(row):
        print("*", end="")
    print()
```

Which badge design will it create?

A.

```text
*
**
***
```

B.

```text
***
**
*
```

C.

```text
***
***
***
```

D.

```text
*
*
*
```

### 29. Breaking only the inner search

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing nested loops with `break`

A grid scan contains:

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)
        break
```

Which coordinate sequence is logged?

A. `(1, 1)` only, because `break` exits both loops  
B. All nine row-column combinations  
C. `(1, 1), (1, 2), (1, 3)`  
D. `(1, 1), (2, 1), (3, 1)`, because each `break` exits only the current inner loop

### 30. A comparison job grows into one million checks

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `nested-loops`  
**Is Curriculum Based:** No  
**Assessment type:** Analysing nested-loop workload

A duplicate detector compares each of 1,000 records with 1,000 records using two nested loops. Which workload estimate should appear in the design review?

A. `2,000` inner checks  
B. `1,000,000` inner checks  
C. `1,000` inner checks  
D. `100,000` inner checks

### 31. Counting qualifying sensor readings

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a conditional counting pattern

A monitor counts the even values in `[2, 5, 8, 9, 12]` by starting a counter at zero and increasing it only for an even reading. Which count reaches the dashboard?

A. `2`  
B. `5`  
C. `3`  
D. `36`

### 32. Building a running donation total

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing an accumulation pattern

A fundraiser receives donations `[10, 20, 30]`. Its accumulator starts at zero and adds each donation once. Which total should be reconciled with the payment report?

A. `60`  
B. `30`  
C. `3`  
D. `0`

### 33. A maximum tracker invents a score

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a maximum-tracker bug; selecting a repair

A temperature report contains `[-8, -3, -12]`, but this loop reports `0` as the highest value:

```python
largest = 0

for temperature in [-8, -3, -12]:
    if temperature > largest:
        largest = temperature
```

Which repair prevents the tracker from inventing a value not present in an all-negative dataset?

A. Start `largest` at `100`  
B. Add every temperature to `largest`  
C. Reverse the `>` comparison and keep zero  
D. Initialise `largest` with the first temperature, then compare the remaining values

### 34. A search flag stays false

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the final value of a search flag

A catalog search starts `found = False`, changes it to `True` only on a matching product ID, and breaks immediately on a match. The entire catalog is checked without a match. Which state should the result screen trust?

A. `found` becomes the last product ID  
B. `found` remains `False`  
C. `found` becomes `True` because the loop completed  
D. `found` has no value after a loop

### 35. No numbers entered before “done”

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `common-loop-patterns`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct guard for an empty accumulation

A sentinel-controlled average calculator starts `total = 0` and `count = 0`. The user immediately types `"done"`. Which design guard prevents an invalid average calculation while preserving the sum-and-count pattern?

A. Divide `total` by `count` before reading the sentinel  
B. Set `count` to 1 even though no value was entered  
C. Calculate and display the average only when `count > 0`; otherwise report that no numbers were supplied  
D. Treat `"done"` as the numeric value zero and count it

### 36. Printing chair numbers one through five

**Difficulty:** Foundational

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest off-by-one repair

A room-label script uses `range(1, 5)` and produces chair numbers 1 through 4. The requirement includes chair 5. Which smallest boundary repair is correct?

A. Use `range(1, 6)`  
B. Use `range(0, 5)`  
C. Use `range(1, 5, 2)`  
D. Use `range(2, 6)`

### 37. A reward counter stops one level early

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Repairing an incorrect loop boundary

A game intends to display levels 1 through 5:

```python
level = 1

while level < 5:
    print(level)
    level += 1
```

Which one-symbol repair includes the advertised final level?

A. Change `<` to `>`  
B. Change `1` to `0`  
C. Change `+=` to `-=`  
D. Change `<` to `<=`

### 38. A countdown moves away from its exit

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing unexpected nontermination

A diagnostic loop begins at 1 and should stop after reaching 5:

```python
count = 1

while count <= 5:
    print(count)
    count -= 1
```

Which review note explains why the values continue downward without ending?

A. The loop condition excludes 5  
B. `print` changes positive values into negatives  
C. Decreasing `count` keeps it at or below 5, so the update moves away from making the condition false  
D. A `while` loop cannot use a numeric counter

### 39. Selecting one test that reveals the missing endpoint

**Difficulty:** Intermediate

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes an off-by-one defect

A booking system promises to generate seat labels 1 through 10 but uses `range(1, 10)`. QA can inspect one expected label to demonstrate the boundary defect immediately. Which label provides the clearest evidence?

A. Seat `1`  
B. Seat `10`  
C. Seat `5`  
D. Seat `9`

### 40. A deliberate loop with a controlled exit

**Difficulty:** Advanced

**Taxonomy:** `python` → `loops-and-iteration` → `loop-debugging`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a safe intentional infinite-loop structure

A console should accept commands indefinitely but must stop without processing the sentinel `"quit"`. Which implementation makes the apparently endless loop controlled and intentional?

A.

```python
while True:
    command = input("Command: ")
    if command == "quit":
        break
    print(f"Processing {command}")
```

B.

```python
while True:
    command = input("Command: ")
    print(f"Processing {command}")
```

C.

```python
command = ""
while command == "quit":
    command = input("Command: ")
```

D.

```python
while True:
    break
    command = input("Command: ")
```

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | A `range` excludes its stop value, so changing the stop to 7 preserves the start at 1 and produces 1 through 6. |
| 2 | A | Intermediate | The number of attempts is unknown, so repetition should depend on the changing password condition. |
| 3 | D | Foundational | Direct iteration binds `recipient` to each current element of `recipients` without assuming a fixed list length. |
| 4 | B | Intermediate | The outer values are 3, 2, and 1, so the inner loop prints three, then two, then one `#` character. |
| 5 | B | Advanced | With two non-zero donations, Version A stores 30 while Version B overwrites 10 with 20; the shorter alternatives do not distinguish them. |
| 6 | D | Foundational | The loop displays 3, 4, and 5, then increments to 6 and fails the condition. |
| 7 | A | Intermediate | The first two commands are ordinary work; the sentinel terminates the session before later input is processed. |
| 8 | C | Intermediate | `progress` remains 1, so `progress <= 100` stays true forever. |
| 9 | B | Intermediate | Membership negation is true exactly when the response is neither accepted value. Option A is always true because one inequality must hold. |
| 10 | D | Advanced | Testing the newly read command before the processing action prevents the sentinel from being handled as work. |
| 11 | C | Foundational | `range(5)` starts at zero and excludes the stop value 5. |
| 12 | A | Intermediate | The range starts at 2, advances by 2, and stops before 8. |
| 13 | D | Foundational | `range(1, 11)` begins at 1 and excludes 11, leaving exactly 1 through 10. |
| 14 | B | Intermediate | A negative step counts downward, and the exclusive stop at 0 leaves 1 as the final value. |
| 15 | A | Advanced | Version A uses count values 0 through 499, and Version B iterates over the same 500-value range, so both call the function 500 times. |
| 16 | C | Foundational | Iteration over a string visits its characters from left to right. |
| 17 | B | Intermediate | Direct list iteration gives each stored name without unnecessary index handling. |
| 18 | D | Intermediate | `enumerate` supplies position and item together, and `start=1` makes the visible numbering human-friendly. |
| 19 | A | Intermediate | Lowercasing lets both `A` and `a` match the vowel string, giving a count of 2. |
| 20 | C | Advanced | `enumerate` keeps each generated position paired with the item without a separate counter update. |
| 21 | D | Foundational | Seven squared is 49, while eight squared is 64, the first square greater than 50. |
| 22 | B | Intermediate | `continue` skips the print for 2 and 4 but allows the loop to process the remaining positions. |
| 23 | A | Intermediate | A `break` suppresses the loop's `else`, so a successful search does not also report failure. |
| 24 | C | Intermediate | Loop `else` specifically handles normal completion without a `break`, which represents an unsuccessful search here. |
| 25 | D | Advanced | At zero the condition triggers `continue` before the increment, causing the unchanged value to repeat forever. |
| 26 | B | Foundational | Only the inner bound controls the number of stars per row; changing it from 5 to 4 preserves three rows and prints four stars on each. |
| 27 | C | Intermediate | For rows 1, 2, and 3, the inner loop repeats the current row value one, two, and three times respectively. |
| 28 | A | Intermediate | The inner range has lengths 1, 2, and 3, while the empty `print()` starts a new line after each row. |
| 29 | D | Advanced | `break` exits only the inner loop; the outer loop proceeds to its next row and starts a new inner loop. |
| 30 | B | Intermediate | The inner comparison runs `1,000 × 1,000`, which is one million times. |
| 31 | C | Foundational | The qualifying readings are 2, 8, and 12. |
| 32 | A | Intermediate | The accumulator progresses from 0 to 10, then 30, then 60. |
| 33 | D | Advanced | Initialising from actual data lets -3 become the maximum without introducing an artificial zero. |
| 34 | B | Intermediate | Only a match changes the flag; with no match, its initial false value remains correct. |
| 35 | C | Advanced | The count guard prevents division by zero and truthfully handles an empty set of entered values. |
| 36 | A | Foundational | Since the stop is exclusive, using 6 includes the desired endpoint 5. |
| 37 | D | Intermediate | The inclusive condition `<= 5` allows the fifth level to run before the counter becomes 6. |
| 38 | C | Advanced | Subtracting moves the value farther below the upper limit, ensuring the condition remains true. |
| 39 | B | Intermediate | The stop value 10 is excluded, so the promised final seat label is the direct failing case. |
| 40 | A | Advanced | `while True` is controlled by a reachable `break`, and the sentinel check occurs before ordinary processing. |

## Taxonomy coverage

| Unit 4 taxonomy subtopic | Question numbers |
|---|---|
| `while-loops` | 2, 6, 9 |
| `for-loops-and-range` | 1, 11–15 |
| `sequence-iteration` | 3, 16–20 |
| `loop-control-statements` | 7, 10, 21–25 |
| `nested-loops` | 4, 26–30 |
| `common-loop-patterns` | 5, 31–35 |
| `loop-debugging` | 8, 36–40 |

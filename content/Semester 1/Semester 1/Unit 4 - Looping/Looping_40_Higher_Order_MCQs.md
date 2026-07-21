# Unit 4: Looping - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 4 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, boundary testing, repair selection, behavior comparison, and practical application
- Student expectation: predict or diagnose before running the code

---

## Questions

### 1. One reminder for every classmate

**Difficulty:** Foundational

A class representative has a fixed list of 60 students and must send the same reminder once to every name. Which loop choice best matches the shape of the task?

A. A `while` loop that waits for someone to type `"quit"`  
B. Sixty copied send instructions  
C. A `for` loop that visits each student in the list  
D. A nested loop with 60 rows and 60 columns

### 2. Retrying a password for an unknown number of attempts

**Difficulty:** Intermediate

A hostel Wi-Fi screen must keep asking until the correct password is entered. The designer cannot know which attempt will succeed. Which structure expresses that requirement most naturally?

A. A `while` loop controlled by whether the password is still incorrect  
B. A `for` loop fixed at exactly one attempt  
C. One `if` statement with no repetition  
D. A loop over the letters in the password

### 3. A thousand labels from one instruction

**Difficulty:** Foundational

A warehouse prototype prints five labels using five copied `print` lines. Production will require 10,000 labels, with the same action applied to changing data. Which review conclusion best supports replacing the copies with a loop?

A. Loops make every label contain identical data  
B. A loop is useful only when the program has no input  
C. Copying is safer because each line can develop a different typo  
D. A loop expresses the repeated action once, scales with the data, and reduces inconsistent edits

### 4. A calculation that happens only once

**Difficulty:** Intermediate

A receipt program reads one item's price and quantity, multiplies them once, and displays one total before ending. Which design decision is most appropriate?

A. Use a `while True` loop even though nothing repeats  
B. Keep the calculation sequential because the requirement contains no repeated task  
C. Add a nested loop so multiplication becomes faster  
D. Repeat the output until the user stops the program manually

### 5. Future changes to a copied notification block

**Difficulty:** Advanced

Version A contains 40 copied blocks that format and send a notification. Version B loops over 40 recipients and contains one copy of that block. A privacy sentence must now be added to every notification. Which maintenance assessment is strongest?

A. Version A is safer because editing 40 locations creates more review opportunities  
B. Version B centralises the behavior, so one correct edit applies consistently to every iteration  
C. The versions are equally maintainable because both currently send 40 messages  
D. Version B cannot personalise messages because loops always reuse identical values

### 6. A counter approaches its stopping point

**Difficulty:** Foundational

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

A console receives the commands `"add"`, `"remove"`, `"quit"`, and `"add"` in that order. Its loop stops as soon as `"quit"` is read. Which command history should the application retain as processed work?

A. `"add"`, `"remove"`; the stop signal ends the session before the final command  
B. All four entries, because a sentinel is processed like ordinary work  
C. `"quit"` only  
D. The final `"add"` only

### 8. A progress display frozen at one percent

**Difficulty:** Intermediate

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

### 9. Choosing a retry structure for payment confirmation

**Difficulty:** Intermediate

A checkout should request payment confirmation again whenever the response is neither `"yes"` nor `"no"`. The number of invalid responses is unknown. Which control plan best fits?

A. Repeat exactly twice with `for response in range(2)`  
B. Use a `while` loop whose condition remains true while the response is invalid, reading a new response inside the loop  
C. Read one response and use `if` without another input  
D. Loop through the characters in the first response

### 10. The quit command is treated as ordinary work

**Difficulty:** Advanced

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

A maintenance tool checks lockers selected by `range(2, 8, 2)`. Which locker sequence will it visit?

A. `2, 4, 6`  
B. `2, 4, 6, 8`  
C. `0, 2, 4, 6`  
D. `2, 3, 4, 5, 6, 7`

### 13. A ten-line multiplication table

**Difficulty:** Foundational

A table must include multipliers 1 through 10, including both endpoints. Which range supplies exactly those values?

A. `range(10)`  
B. `range(1, 10)`  
C. `range(0, 11)`  
D. `range(1, 11)`

### 14. A launch countdown that stops before zero

**Difficulty:** Intermediate

A display must count `10, 9, 8, ... 1` and then show a separate `"Launch"` message. Which range drives the numeric countdown correctly?

A. `range(1, 10, -1)`  
B. `range(10, 0, -1)`  
C. `range(10, 1, 1)`  
D. `range(0, 10, -1)`

### 15. Replacing manual counter bookkeeping

**Difficulty:** Advanced

A machine must run a calibration exactly 500 times. Version A uses a `while` loop with a manually initialised and updated counter. Version B uses `for _ in range(500)`. Which review decision is best supported by the requirement?

A. Prefer Version B because the count is known and the loop manages its own finite sequence  
B. Prefer Version A because a forgotten counter update is useful for continuous calibration  
C. Reject both because only nested loops can repeat 500 times  
D. Prefer Version A because `range(500)` contains 501 values

### 16. Reading a tracking code one character at a time

**Difficulty:** Foundational

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

A list contains `names = ["Asha", "Ravi", "Meera"]`. The application needs each name itself, not its numeric position. Which loop is the clearest Python expression of the requirement?

A. `for name in range(3):`  
B. `for name in names:`  
C. `while names:` without changing the list  
D. `for names in "name":`

### 18. Numbering a queue from one

**Difficulty:** Intermediate

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

A developer writes one loop over a product list and a separate counter that must be incremented on every pass. A missed increment causes duplicate row numbers. Which refactor removes that synchronisation risk while preserving access to both values?

A. Loop over `range(1000)` regardless of the list length  
B. Convert every product name into a number  
C. Use `enumerate(products, start=1)` to receive the row number and product together  
D. Replace the loop with copied output statements

### 21. Stopping at the first square above fifty

**Difficulty:** Foundational

A search checks positive integers in order and stops at the first one whose square is greater than 50. Which number will be recorded when `break` ends the search?

A. `6`  
B. `7`  
C. `9`  
D. `8`

### 22. Skipping sponsored positions

**Difficulty:** Intermediate

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

A product search uses a `for` loop with `break` when the target is found and an attached `else` that displays `"Not found"`. The target appears as the second item. Which interface behavior follows Python's loop-`else` rule?

A. The search breaks at the match, and the `"Not found"` message is skipped  
B. The `else` runs because every `for` loop must finish with it  
C. Both success and `"Not found"` appear  
D. The loop ignores the target and checks only the last item

### 24. A complete search finds no matching ID

**Difficulty:** Intermediate

A list search reaches its end without ever executing `break`. An `else` block is attached directly to the loop. Which status should the application produce?

A. It must repeat the search forever  
B. It must pretend the last item matched  
C. The loop's `else` runs and can report that no matching ID was found  
D. The `else` runs only if the first item fails

### 25. A skipped update traps a `while` loop

**Difficulty:** Advanced

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

### 26. Filling every cell in a small grid

**Difficulty:** Foundational

A seating chart has 3 rows and 4 seats per row. An outer loop handles rows and an inner loop handles seats. How many times must the inner seat-processing block run?

A. `7`  
B. `12`  
C. `3`  
D. `4`

### 27. Generating coordinate labels

**Difficulty:** Intermediate

A layout tool runs:

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

How many coordinate labels reach the layout log?

A. `5`  
B. `3`  
C. `6`  
D. `9`

### 28. A growing staircase of stars

**Difficulty:** Intermediate

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

A duplicate detector compares each of 1,000 records with 1,000 records using two nested loops. Which workload estimate should appear in the design review?

A. `2,000` inner checks  
B. `1,000,000` inner checks  
C. `1,000` inner checks  
D. `100,000` inner checks

### 31. Counting qualifying sensor readings

**Difficulty:** Foundational

A monitor counts the even values in `[2, 5, 8, 9, 12]` by starting a counter at zero and increasing it only for an even reading. Which count reaches the dashboard?

A. `2`  
B. `5`  
C. `3`  
D. `36`

### 32. Building a running donation total

**Difficulty:** Intermediate

A fundraiser receives donations `[10, 20, 30]`. Its accumulator starts at zero and adds each donation once. Which total should be reconciled with the payment report?

A. `60`  
B. `30`  
C. `3`  
D. `0`

### 33. A maximum tracker invents a score

**Difficulty:** Advanced

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

A catalog search starts `found = False`, changes it to `True` only on a matching product ID, and breaks immediately on a match. The entire catalog is checked without a match. Which state should the result screen trust?

A. `found` becomes the last product ID  
B. `found` remains `False`  
C. `found` becomes `True` because the loop completed  
D. `found` has no value after a loop

### 35. No numbers entered before “done”

**Difficulty:** Advanced

A sentinel-controlled average calculator starts `total = 0` and `count = 0`. The user immediately types `"done"`. Which design guard prevents an invalid average calculation while preserving the sum-and-count pattern?

A. Divide `total` by `count` before reading the sentinel  
B. Set `count` to 1 even though no value was entered  
C. Calculate and display the average only when `count > 0`; otherwise report that no numbers were supplied  
D. Treat `"done"` as the numeric value zero and count it

### 36. Printing chair numbers one through five

**Difficulty:** Foundational

A room-label script uses `range(1, 5)` and produces chair numbers 1 through 4. The requirement includes chair 5. Which smallest boundary repair is correct?

A. Use `range(1, 6)`  
B. Use `range(0, 5)`  
C. Use `range(1, 5, 2)`  
D. Use `range(2, 6)`

### 37. A reward counter stops one level early

**Difficulty:** Intermediate

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

A booking system promises to generate seat labels 1 through 10 but uses `range(1, 10)`. QA can inspect one expected label to demonstrate the boundary defect immediately. Which label provides the clearest evidence?

A. Seat `1`  
B. Seat `10`  
C. Seat `5`  
D. Seat `9`

### 40. A deliberate loop with a controlled exit

**Difficulty:** Advanced

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
| 1 | C | Foundational | The task visits every item in a known collection, which is the natural use of a `for` loop. |
| 2 | A | Intermediate | The number of attempts is unknown, so repetition should depend on the changing password condition. |
| 3 | D | Foundational | A loop removes copied instructions, applies one consistent action to changing items, and scales cleanly. |
| 4 | B | Intermediate | Loops serve repetition; adding one where the task occurs once adds complexity without solving a requirement. |
| 5 | B | Advanced | Centralising repeated behavior avoids 40 separate edits and the risk that some copies diverge. |
| 6 | D | Foundational | The loop displays 3, 4, and 5, then increments to 6 and fails the condition. |
| 7 | A | Intermediate | The first two commands are ordinary work; the sentinel terminates the session before later input is processed. |
| 8 | C | Intermediate | `progress` remains 1, so `progress <= 100` stays true forever. |
| 9 | B | Intermediate | A validation retry has no fixed count and must obtain a new value on each pass. |
| 10 | D | Advanced | Testing the newly read command before the processing action prevents the sentinel from being handled as work. |
| 11 | C | Foundational | `range(5)` starts at zero and excludes the stop value 5. |
| 12 | A | Intermediate | The range starts at 2, advances by 2, and stops before 8. |
| 13 | D | Foundational | `range(1, 11)` begins at 1 and excludes 11, leaving exactly 1 through 10. |
| 14 | B | Intermediate | A negative step counts downward, and the exclusive stop at 0 leaves 1 as the final value. |
| 15 | A | Advanced | A fixed repetition count is directly represented by `for` and `range`, with no update to forget. |
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
| 26 | B | Foundational | The inner work runs four times for each of three rows: `3 × 4 = 12`. |
| 27 | C | Intermediate | Two outer passes each run three inner passes, producing six coordinate pairs. |
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

## Topic coverage

| Unit 4 topic | Question numbers |
|---|---|
| Why loops, repetition, and automation | 1–5 |
| `while` loops, counters, and sentinels | 6–10 |
| `for` loops and `range()` | 11–15 |
| Iterating over sequences and strings | 16–20 |
| `break`, `continue`, and loop `else` | 21–25 |
| Nested loops, grids, and patterns | 26–30 |
| Count, sum, min/max, and search patterns | 31–35 |
| Infinite loops and off-by-one errors | 36–40 |


# Unit 2: Data Types and Operators - 40 Higher-Order MCQs

## Assessment design

- Scope: all ten Unit 2 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, repair selection, boundary analysis, design comparison, and practical application
- Student expectation: predict or diagnose from the scenario before running the code

---

## Questions

### 1. A wallet label keeps the updated amount

**Difficulty:** Foundational

A digital wallet starts a transaction with this state:

```python
balance = 1000
balance = balance - 250
print(f"Remaining: {balance}")
```

Which amount will the transaction screen show?

A. `1000`, because the first assignment cannot be changed  
B. `750`, because the second assignment stores the calculated value back under the same label  
C. `250`, because assignment keeps only the value being subtracted  
D. The screen remains blank because a variable cannot be reassigned

### 2. Naming a value another developer must maintain

**Difficulty:** Intermediate

A banking program needs a variable for the amount left after a withdrawal. Which proposed name is both valid Python and the clearest PEP 8-style choice?

A. `2ndBalance`  
B. `class`  
C. `Remaining Balance`  
D. `remaining_balance`

### 3. Two score labels that differ only by case

**Difficulty:** Intermediate

A scoreboard contains:

```python
score = 80
Score = 20
combined = score + Score
```

A reviewer initially assumes the second line replaces the first. Which audit note correctly describes the stored result?

A. `combined` is `100` because `score` and `Score` are two case-sensitive variable names  
B. `combined` is `40` because both names refer to the latest value  
C. `combined` is `160` because `Score` duplicates `score`  
D. Python rejects all variable names containing capital letters

### 4. A jar label quietly changes meaning

**Difficulty:** Advanced

A delivery script first uses `status` for text and later reuses it for a number:

```python
status = "Packed"
# several lines later
status = 3
```

Both lines are legal Python, but a later developer expects `status` to contain the delivery message. Which repair most improves maintainability without removing either value?

A. Rename both variables to `x`  
B. Write `status = "Packed" = 3` so both values remain attached  
C. Use separate descriptive names such as `delivery_status` and `attempt_count`  
D. Capitalise the second name as `Status` and leave its purpose unexplained

### 5. Selecting number types for a science lab

**Difficulty:** Foundational

A lab program stores the number of samples, a measured voltage with decimals, and an electrical value containing a real and imaginary part. Which mapping fits the quantities?

A. Samples: `float`; voltage: `complex`; electrical value: `int`  
B. Samples: `complex`; voltage: `int`; electrical value: `float`  
C. All three should be strings because they will eventually be displayed  
D. Samples: `int`; voltage: `float`; electrical value: `complex`

### 6. A receipt shows more decimal digits than expected

**Difficulty:** Intermediate

A prototype calculates:

```python
total = 0.1 + 0.2
```

The debug screen shows `0.30000000000000004`. Which support note gives the most accurate response?

A. Python performed addition in the wrong order  
B. Some decimal fractions cannot be represented exactly in binary floating point; format or round the displayed value when appropriate  
C. One operand must be converted to `complex`  
D. Python floats cannot store values below 1

### 7. Whole crates versus a decimal result

**Difficulty:** Intermediate

A warehouse has 8 bottles and packs 4 bottles per crate.

```python
result_a = 8 / 4
result_b = 8 // 4
```

The inventory API requires a whole-number crate count. Which value and explanation should the developer use?

A. `result_a`, because it stores the integer `2`  
B. Either value, because `/` and `//` always produce the same type  
C. `result_b`, because it stores the whole-number result `2`, while `result_a` is `2.0`  
D. Neither value, because division always produces a complex number

### 8. Fractional packet counts enter the inventory

**Difficulty:** Advanced

A shop's data model treats the number of sealed biscuit packets as a measurement and accepts `3.5`. The business sells only complete sealed packets. Which design correction best aligns the stored type with the real quantity?

A. Represent the count as an integer and reject data that is not a whole packet count  
B. Use a complex number so the fractional part becomes imaginary  
C. Keep a float because all numeric types mean the same thing  
D. Convert the count to text and perform arithmetic on it later

### 9. Joining a player's first and last name

**Difficulty:** Foundational

A profile card currently shows `SachinTendulkar`. The variables hold `"Sachin"` and `"Tendulkar"`. Which expression produces the intended display name?

A. `first_name - last_name`  
B. `first_name + " " + last_name`  
C. `first_name + last_name + 1`  
D. `first_name * last_name`

### 10. Storing an actual account verdict

**Difficulty:** Intermediate

A login service needs a Boolean indicating that an account is inactive. Which assignment stores an actual Boolean false value rather than text or an invalid spelling?

A. `is_active = "False"`  
B. `is_active = false`  
C. `is_active = ""`  
D. `is_active = False`

### 11. A text field containing a single zero

**Difficulty:** Intermediate

A form stores the typed entry `"0"` in `response`. Another developer plans to use its truthiness as an “entry supplied” flag. Which review conclusion is accurate?

A. It is falsy because zero is always false, even inside text  
B. It is a Boolean because it contains one of the digits used by computers  
C. It is truthy because it is a non-empty string  
D. It becomes falsy only because it has one character

### 12. A completion flag derived from a name

**Difficulty:** Advanced

A profile service contains:

```python
name = ""
is_complete = name != ""
status_text = "Complete"
```

Which data audit correctly distinguishes the values?

A. `name` and `status_text` are strings; `is_complete` is the Boolean `False`  
B. All three values are strings because they have variable names  
C. `name` is Boolean, `is_complete` is text, and `status_text` is numeric  
D. `is_complete` contains the string `"False"`

### 13. Adding one year to keyboard input

**Difficulty:** Foundational

A birthday kiosk receives an age and immediately adds 1:

```python
age = input("Age: ")
next_age = age + 1
```

It stops when the user types `20`. Which smallest repair gives `next_age` the numeric value `21`?

A. `age = str(input("Age: "))`  
B. `next_age = age + "1"`  
C. `next_age = bool(age) + 1`  
D. `age = int(input("Age: "))`

### 14. A decimal measurement becomes a whole number

**Difficulty:** Intermediate

A parcel measurement is `7.9` kg, and a developer stores `int(7.9)` in a report. Which value reaches the report, and how should the team interpret it?

A. `8`, because `int()` rounds to the nearest whole number  
B. `7`, because conversion to `int` discards the decimal part rather than rounding  
C. `7.9`, because conversion never changes a value  
D. The conversion fails because floats cannot become integers

### 15. Investigating a decimal-looking input

**Difficulty:** Intermediate

A price entered as `12.5` behaves differently from the number `12.5`. The developer adds:

```python
raw_price = input("Price: ")
print(type(raw_price))
```

Which diagnostic result should guide the repair?

A. `<class 'str'>`, confirming that keyboard input must be converted before numeric calculation  
B. `<class 'float'>`, confirming that `input()` detects decimal points  
C. `<class 'int'>`, because digits are always integers  
D. `<class 'bool'>`, because input is either present or absent

### 16. The word “False” creates a true Boolean

**Difficulty:** Advanced

A settings importer performs:

```python
raw_setting = "False"
enabled = bool(raw_setting)
```

The feature becomes enabled. Which review note best accounts for this result?

A. `bool()` checks whether text spells a Boolean word  
B. Every string converts to `False`  
C. Any non-empty string is truthy, so `bool("False")` becomes `True`; the text must be interpreted explicitly  
D. Capital letters automatically make a Boolean true

### 17. Packing complete boxes

**Difficulty:** Foundational

A warehouse must calculate how many complete boxes of 12 can be filled from 50 items. Which expression directly produces the required count?

A. `50 / 12`  
B. `50 // 12`  
C. `50 % 12`  
D. `50 ** 12`

### 18. Converting minutes for a travel display

**Difficulty:** Intermediate

A journey lasts 250 minutes. The display needs complete hours and leftover minutes. Which pair of expressions produces 4 hours and 10 minutes?

A. `250 / 60` and `250 * 60`  
B. `250 % 60` and `250 // 60`, assigned as hours and minutes respectively  
C. `250 ** 60` and `250 - 60`  
D. `250 // 60` for hours and `250 % 60` for minutes

### 19. Building a three-beat cheer

**Difficulty:** Intermediate

A game uses:

```python
cheer = "ha" * 3 + "!"
```

Which sound will the game display?

A. `ha3!`  
B. `ha ha ha !` with automatic spaces  
C. `hahaha!`  
D. The expression fails because strings cannot use arithmetic symbols

### 20. Full cartons and loose items

**Difficulty:** Advanced

A dispatch centre has `48` items and cartons that hold `5` items each. It needs both the number of full cartons and the number of loose items. Which calculation pair preserves both facts?

A. `full_cartons = 48 // 5` and `loose_items = 48 % 5`  
B. `full_cartons = 48 / 5` and `loose_items = 48 / 5`  
C. `full_cartons = 48 % 5` and `loose_items = 48 // 5`  
D. `full_cartons = 48 ** 5` and `loose_items = 0`

### 21. Voting on the eighteenth birthday

**Difficulty:** Foundational

A voting portal must mark a citizen eligible from the day they turn 18. Which comparison captures the boundary correctly?

A. `age > 18`  
B. `age == 18`  
C. `age != 18`  
D. `age >= 18`

### 22. Keeping exam marks inside their legal range

**Difficulty:** Intermediate

A marks validator needs one Boolean that is true from 0 through 100, including both limits. Which comparison expresses that interval most clearly?

A. `marks >= 0 or marks <= 100`  
B. `marks > 0 < 100`  
C. `0 <= marks <= 100`  
D. `marks == 0 == 100`

### 23. Checking a submitted PIN without overwriting it

**Difficulty:** Intermediate

A security review finds that a developer confused assignment with equality. Which expression asks whether `entered_pin` matches `saved_pin` without assigning either value?

A. `entered_pin == saved_pin`  
B. `entered_pin = saved_pin`  
C. `entered_pin >= saved_pin`  
D. `entered_pin != saved_pin`

### 24. Product codes compared as text

**Difficulty:** Advanced

A catalog sorts the string codes `"item10"` and `"item2"` alphabetically. A developer expects the numeric-looking suffix 10 to come after 2. Which observation matches Python's string comparison?

A. `"item10" > "item2"` is true because Python extracts the numbers  
B. `"item10" < "item2"` is true because string comparison reaches `'1'` versus `'2'` character by character  
C. Strings can only be tested with `==`, never `<`  
D. Both strings are equal because they begin with `"item"`

### 25. Two checks at a theme park ride

**Difficulty:** Foundational

A rider may enter only when they are at least 120 cm tall and at least 8 years old. Which condition represents the rule?

A. `height >= 120 or age >= 8`  
B. `not height >= 120`  
C. `height >= 120 and age >= 8`  
D. `height >= 120 and not age >= 8`

### 26. Two independent ways to earn a discount

**Difficulty:** Intermediate

A store grants a discount when the shopper is a member or when a festival offer is active. Either fact is sufficient. Which condition matches the policy?

A. `is_member or festival_offer`  
B. `is_member and festival_offer`  
C. `not is_member and festival_offer`  
D. `not (is_member or festival_offer)`

### 27. Turning a block flag into permission

**Difficulty:** Intermediate

A gate stores `is_blocked`. The permission value should be true exactly when the visitor is not blocked. Which assignment states that relationship directly?

A. `allowed = is_blocked`  
B. `allowed = is_blocked or True`  
C. `allowed = is_blocked and False`  
D. `allowed = not is_blocked`

### 28. Protecting a calculation with short-circuiting

**Difficulty:** Advanced

A score service should calculate `total / count` only when at least one score exists. Which condition places the safety check where Python can short-circuit before dividing by zero?

A. `total / count > 80 and count != 0`  
B. `count != 0 and total / count > 80`  
C. `count == 0 or total / count > 80`  
D. `not count != 0 and total / count > 80`

### 29. Awarding bonus points in place

**Difficulty:** Foundational

A game should increase the existing `score` by 15. Which statement communicates that update most directly?

A. `score += 15`  
B. `score = 15`  
C. `score == score + 15`  
D. `15 += score`

### 30. A cart total changes three times

**Difficulty:** Intermediate

A promotional cart runs these updates:

```python
total = 100
total += 50
total *= 2
total -= 40
```

Which amount will be sent to checkout?

A. `210`  
B. `2600`  
C. `260`  
D. `110`

### 31. Rewriting an update without changing behavior

**Difficulty:** Intermediate

A reviewer expands the shorthand `items //= 4` for a beginner. Which replacement is equivalent?

A. `items = 4 // items`  
B. `items = items // 4`  
C. `items = items / 4.0 + items`  
D. `items == items // 4`

### 32. Keeping only the seconds left after full minutes

**Difficulty:** Advanced

A timer stores `367` total seconds. After separately recording the full minutes, it wants to update `seconds` so it contains only the leftover seconds. Which in-place operation leaves `7` in `seconds`?

A. `seconds /= 60`  
B. `seconds //= 60`  
C. `seconds **= 60`  
D. `seconds %= 60`

### 33. A delivery formula is not evaluated left to right

**Difficulty:** Foundational

A small fee formula is:

```python
fee = 2 + 3 * 4
```

Which fee reaches the invoice under Python's precedence rules?

A. `20`, because addition is read first  
B. `9`, because only adjacent numbers combine  
C. `14`, because multiplication is performed before addition  
D. `24`, because every value is multiplied

### 34. Repairing an average that looks believable but is wrong

**Difficulty:** Intermediate

A sensor system intends to average `a` and `b` but uses:

```python
average = a + b / 2
```

Which replacement makes the intended order explicit?

A. `average = (a + b) / 2`  
B. `average = a + (b / 2)`  
C. `average = a * b / 2`  
D. `average = a + b * 2`

### 35. Three deductions of equal priority

**Difficulty:** Intermediate

A balance adjustment uses:

```python
remaining = 100 - 30 - 20
```

Which review note describes the calculation?

A. Python starts on the right, so the result is `90`  
B. Subtractions of equal precedence associate left to right, producing `50`  
C. Python adds the deductions before subtracting, producing `50` only by accident  
D. The expression is rejected unless parentheses are added

### 36. A VIP bypasses a mandatory account check

**Difficulty:** Advanced

A service computes:

```python
allowed = account_active and has_ticket or is_vip
```

The intended policy is that the account must be active and the user must have either a ticket or VIP status. Which replacement both fixes the grouping and communicates the policy clearly?

A. `allowed = (account_active and has_ticket) or is_vip`  
B. `allowed = account_active or (has_ticket and is_vip)`  
C. `allowed = not account_active and (has_ticket or is_vip)`  
D. `allowed = account_active and (has_ticket or is_vip)`

### 37. Two typed numbers join together

**Difficulty:** Foundational

A quick calculator contains:

```python
a = input("First: ")
b = input("Second: ")
print(a + b)
```

The user enters `7` and `10`. Which screen result should the support guide predict?

A. `710`, because both inputs are strings and `+` concatenates them  
B. `17`, because digit characters are converted automatically  
C. `7 10`, because `print` always inserts a space inside a string  
D. The result is `70`, because text multiplication occurs

### 38. Printing several values with automatic spacing

**Difficulty:** Intermediate

A beginner wants the sentence `Order 3 ready` and writes:

```python
quantity = 3
print("Order", quantity, "ready")
```

Which review observation is accurate?

A. The line fails because `quantity` is not converted with `str()`  
B. The output is `Order3ready` because commas remove spaces  
C. `print` displays the three values in order with a single space between them  
D. The line displays only the numeric value

### 39. Formatting a receipt total inside the message

**Difficulty:** Intermediate

A receipt stores `quantity = 2` and `price = 49.5`. The total must appear with exactly two decimal places. Which line produces `Total: ₹99.00`?

A. `print("Total: ₹" + quantity * price)`  
B. `print(f"Total: ₹{quantity + price:.2f}")`  
C. `print("Total: ₹", quantity, price, ".00")`  
D. `print(f"Total: ₹{quantity * price:.2f}")`

### 40. Presenting a performance rate and a large audience

**Difficulty:** Advanced

A dashboard stores `success_rate = 0.873` and `audience = 1500000`. It must display `Success: 87.3% | Audience: 1,500,000`. Which f-string applies both requested formats?

A. `f"Success: {success_rate:.1f}% | Audience: {audience}"`  
B. `f"Success: {success_rate:.1%} | Audience: {audience:,}"`  
C. `f"Success: {success_rate:%} | Audience: {audience:.2f}"`  
D. `f"Success: {success_rate * 100:,} | Audience: {audience:.1%}"`

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | B | Foundational | The expression uses the current balance, subtracts 250, and stores 750 back under the same name. |
| 2 | D | Intermediate | It is valid, descriptive snake_case and does not begin with a digit, contain spaces, or reuse a reserved word. |
| 3 | A | Intermediate | Python names are case-sensitive, so the two differently capitalised names hold separate values. |
| 4 | C | Advanced | Python permits reassignment to another type, but separate purpose-specific names prevent a misleading change of meaning. |
| 5 | D | Foundational | Counts are whole integers, measured voltage may be fractional, and complex electrical values need real and imaginary parts. |
| 6 | B | Intermediate | Binary floating point cannot exactly represent some decimal fractions; the tiny difference is expected and can be formatted for display. |
| 7 | C | Intermediate | `/` returns the float `2.0`, while `//` returns the whole-number result `2` for these integer operands. |
| 8 | A | Advanced | Whole sealed units are modelled as an integer count, and fractional data should be rejected rather than silently treated as meaningful. |
| 9 | B | Foundational | String concatenation includes only the characters supplied, so an explicit one-space string is required between the names. |
| 10 | D | Intermediate | Python Boolean literals are unquoted and capitalised exactly as `True` and `False`. |
| 11 | C | Intermediate | The integer `0` is falsy, but the string `"0"` contains one character and is therefore truthy. |
| 12 | A | Advanced | The comparison produces the Boolean `False`; the two quoted values are strings, including the empty string. |
| 13 | D | Foundational | `input()` returns text; converting that text to `int` allows numeric addition. |
| 14 | B | Intermediate | `int()` truncates the fractional part, so it produces 7 rather than rounding to 8. |
| 15 | A | Intermediate | Even decimal-looking keyboard input is returned as a string until explicitly converted. |
| 16 | C | Advanced | `bool()` evaluates emptiness, not the English meaning of text. Any non-empty string converts to `True`. |
| 17 | B | Foundational | Floor division gives the number of complete groups, which is 4 boxes. |
| 18 | D | Intermediate | Floor division gives 4 complete hours, while modulo gives the 10 minutes left over. |
| 19 | C | Intermediate | String multiplication repeats the exact characters with no automatic spaces, and `+` appends the exclamation mark. |
| 20 | A | Advanced | Floor division gives 9 full cartons and modulo preserves the 3 items that remain. |
| 21 | D | Foundational | “18 or older” requires an inclusive lower boundary, represented by `>=`. |
| 22 | C | Intermediate | Python's chained comparison checks both inclusive bounds in one readable expression. |
| 23 | A | Intermediate | `==` compares two values; a single `=` performs assignment. |
| 24 | B | Advanced | Strings compare character by character, so the first differing characters are `1` and `2`; `1` sorts first. |
| 25 | C | Foundational | Both requirements are mandatory, so the comparisons must be joined with `and`. |
| 26 | A | Intermediate | Either independent qualifying fact is sufficient, which is the meaning of `or`. |
| 27 | D | Intermediate | `not` reverses the blocked flag, making permission true exactly when blocking is false. |
| 28 | B | Advanced | If `count` is zero, the left side of `and` is false and Python skips the unsafe division. |
| 29 | A | Foundational | `+=` clearly means “add to the existing score and store the result back.” |
| 30 | C | Intermediate | The total changes from 100 to 150, then 300, then 260. |
| 31 | B | Intermediate | `x //= value` is shorthand for `x = x // value`. |
| 32 | D | Advanced | Modulo keeps the remainder after division by 60, leaving 7 seconds. |
| 33 | C | Foundational | Multiplication has higher precedence, so `3 * 4` becomes 12 before 2 is added. |
| 34 | A | Intermediate | Parentheses force the sum to be calculated before division, matching the average formula. |
| 35 | B | Intermediate | Operators of equal precedence such as subtraction normally associate left to right: `(100 - 30) - 20`. |
| 36 | D | Advanced | The active-account requirement must enclose the complete alternative of ticket or VIP status. |
| 37 | A | Foundational | `input()` returns strings, and `+` joins the two strings into `"710"`. |
| 38 | C | Intermediate | `print` accepts mixed types separated by commas and inserts one space between the displayed values. |
| 39 | D | Intermediate | The f-string performs multiplication in braces and `:.2f` displays the numeric result with two decimal places. |
| 40 | B | Advanced | `:.1%` converts 0.873 to one-decimal percentage form, and `:,` adds thousands separators. |

## Topic coverage

| Unit 2 topic | Question numbers |
|---|---|
| Variables, assignment, and naming | 1–4 |
| `int`, `float`, and `complex` | 5–8 |
| Strings and Booleans | 9–12 |
| Type conversion and `type()` | 13–16 |
| Arithmetic operators | 17–20 |
| Comparison operators | 21–24 |
| Logical operators | 25–28 |
| Assignment and augmented operators | 29–32 |
| Operator precedence and associativity | 33–36 |
| Input, output, and f-strings | 37–40 |

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

**Taxonomy:** `python` → `data-types-and-operators` → `variables-and-assignment`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction; final value of a variable

A digital wallet starts a transaction with this state:

```python
balance = 1000
balance = balance - 250
print(f"Remaining: {balance}")
```

Which amount will the transaction screen show?

A. `1250`, because reassignment adds the two numbers automatically  
B. `750`, because the second assignment stores the calculated value back under the same label  
C. `250`, because the rightmost numeric literal replaces the balance before subtraction  
D. `1000`, because the print statement uses the value from the first assignment

### 2. Choosing a type that preserves a sensor reading

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `numeric-types`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate data representation

A greenhouse sensor reports a temperature of `23.75°C`. A developer must preserve the fractional reading for later calculations. Which assignment best matches that requirement?

A. `temperature = 23`  
B. `temperature = "23.75"`  
C. `temperature = 23 + 75j`  
D. `temperature = 23.75`

### 3. Separating displayed text from a Boolean verdict

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `strings-and-booleans`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying final values and types

A registration service prepares a message and a machine-readable verdict:

```python
status_text = "Approved"
is_approved = status_text == "Approved"
```

A downstream rule requires an actual Boolean. Which audit record correctly identifies the two final values and their types?

A. `status_text` is the string `"Approved"`; `is_approved` is the Boolean `True`  
B. Both variables contain the string `"Approved"`  
C. `status_text` is a Boolean because it describes a decision  
D. `is_approved` contains the string `"True"`

### 4. A decimal price is converted with the wrong tool

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `type-conversion`  
**Is Curriculum Based:** No  
**Assessment type:** Error diagnosis; smallest correct repair

A checkout receives a decimal price as keyboard input:

```python
raw_price = input("Price: ")
price = int(raw_price)
```

When the customer enters `12.50`, the conversion fails. The system must preserve paise rather than discard them. Which single-line replacement is the smallest correct repair?

A. `price = bool(raw_price)`  
B. `price = int(float(raw_price))`  
C. `price = float(raw_price)`  
D. `price = raw_price + 0.0`

### 5. Recovering complete trays and leftover cups

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `arithmetic-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting operators for a realistic calculation

A caterer has `29` dessert cups and trays that hold `6` cups. The dashboard must show both the number of completely filled trays and the number of cups left over. Which pair gives the required values?

A. `full = 29 / 6` and `left = 29 / 6`  
B. `full = 29 % 6` and `left = 29 // 6`  
C. `full = int(29 / 6)` and `left = 29 - 6`  
D. `full = 29 // 6` and `left = 29 % 6`

### 6. Finding the test that reveals an age-boundary defect

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes an incorrect boundary

A portal is intended to accept applicants aged 18 or older, but the developer writes:

```python
eligible = age > 18
```

The test team can add only one input to expose the incorrect boundary. Which age should it choose?

A. `17`, because both the requirement and implementation reject it  
B. `18`, because the requirement accepts it while the implementation rejects it  
C. `19`, because both the requirement and implementation accept it  
D. `30`, because a value far from the boundary is the strongest boundary test

### 7. Restoring the missing stock update

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `assignment-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing code; final value of a variable

A kiosk begins with 20 bottles and completes a sale of 6:

```python
stock = 20
sold = 6
# missing update
```

Which line should replace the comment so `stock` finishes at `14` while expressing an in-place update?

A. `stock = sold - stock`  
B. `stock += sold`  
C. `stock -= sold`  
D. `sold -= stock`

### 8. Repairing a precedence defect without changing the formula

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `operator-precedence`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a logic defect; smallest correct repair

A billing rule says a base charge and service charge must be added before multiplying by the number of days. The implementation is:

```python
total = base_charge + service_charge * days
```

Which smallest repair makes the evaluation order match the written policy?

A. `total = (base_charge + service_charge) * days`  
B. `total = base_charge + (service_charge * days)`  
C. `total = base_charge * service_charge + days`  
D. `total = base_charge + service_charge + days`

### 9. Completing a receipt without manual conversion

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `input-and-output`  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing output code in a realistic situation

A café stores `item = "Sandwich"`, `quantity = 2`, and `total = 119.0`. The receipt must display `2 × Sandwich = ₹119.00`. Which line completes the output cleanly without manually converting each value to text?

A. `print(quantity + " × " + item + total)`  
B. `print(f"{quantity} × {item} = ₹{total:.2f}")`  
C. `print("quantity × item = ₹total")`  
D. `print(f"{quantity + item} = ₹{total}")`

### 10. Tracing a discount rule with two routes to qualification

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions

A store grants a discount when the cart is at least ₹500 and the shopper is either a member or shopping during a festival offer:

```python
cart_total = 700
is_member = False
festival_offer = True
discount_applies = cart_total >= 500 and (is_member or festival_offer)
```

Which review note correctly traces this shopper's result?

A. No discount, because both membership and the festival must be true  
B. No discount, because `False` appears anywhere in the expression  
C. The expression fails because comparisons cannot be combined with Booleans  
D. The discount applies: the cart meets the minimum and the festival satisfies the alternative qualification

### 11. A text field containing a single zero

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `strings-and-booleans`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about truthy and falsy values

A form stores the typed entry `"0"` in `response`. Another developer plans to use its truthiness as an “entry supplied” flag. Which review conclusion is accurate?

A. It is falsy because zero is always false, even inside text  
B. It is a Boolean because it contains one of the digits used by computers  
C. It is truthy because it is a non-empty string  
D. It becomes falsy only because it has one character

### 12. A completion flag derived from a name

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `strings-and-booleans`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying final values and types

A profile service contains:

```python
name = ""
is_complete = name != ""
status_text = "Complete"
```

Which data audit correctly distinguishes the values?

A. `name` and `status_text` are strings; `is_complete` is the Boolean `False`  
B. `name` is falsy, so Python changes its stored type from `str` to `bool`  
C. `is_complete` is the string `"False"` because it was derived from text  
D. `status_text` becomes the Boolean `True` because it is non-empty

### 13. Adding one year to keyboard input

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `type-conversion`  
**Is Curriculum Based:** No  
**Assessment type:** Error diagnosis; smallest correct repair

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

**Taxonomy:** `python` → `data-types-and-operators` → `type-conversion`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

A parcel measurement is `7.9` kg, and a developer stores `int(7.9)` in a report. Which value reaches the report, and how should the team interpret it?

A. `8`, because `int()` rounds to the nearest whole number  
B. `7`, because conversion to `int` discards the decimal part rather than rounding  
C. `7.9`, because conversion never changes a value  
D. The conversion fails because floats cannot become integers

### 15. Investigating a decimal-looking input

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `type-conversion`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing unexpected program behaviour

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

**Taxonomy:** `python` → `data-types-and-operators` → `type-conversion`  
**Is Curriculum Based:** No  
**Assessment type:** Truthiness analysis; unexpected behaviour

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

**Taxonomy:** `python` → `data-types-and-operators` → `arithmetic-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate operator

A warehouse must calculate how many complete boxes of 12 can be filled from 50 items. Which expression directly produces the required count?

A. `50 / 12`  
B. `50 // 12`  
C. `50 % 12`  
D. `50 ** 12`

### 18. Converting minutes for a travel display

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `arithmetic-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Applying paired operators in a realistic situation

A journey lasts 250 minutes. The display needs complete hours and leftover minutes. Which pair of expressions produces 4 hours and 10 minutes?

A. `250 / 60` and `250 * 60`  
B. `250 % 60` and `250 // 60`, assigned as hours and minutes respectively  
C. `250 ** 60` and `250 - 60`  
D. `250 // 60` for hours and `250 % 60` for minutes

### 19. Building a three-beat cheer

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `arithmetic-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

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

**Taxonomy:** `python` → `data-types-and-operators` → `arithmetic-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing calculation approaches

A dispatch centre has `48` items and cartons that hold `5` items each. It needs both the number of full cartons and the number of loose items. Which calculation pair preserves both facts?

A. `full_cartons = 48 // 5` and `loose_items = 48 % 5`  
B. `full_cartons = 48 / 5` and `loose_items = 48 / 5`  
C. `full_cartons = 48 % 5` and `loose_items = 48 // 5`  
D. `full_cartons = int(48 / 5)` and `loose_items = 48 - 5`

### 21. Voting on the eighteenth birthday

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct boundary condition

A voting portal must mark a citizen eligible from the day they turn 18. Which comparison captures the boundary correctly?

A. `age > 18`  
B. `age == 18`  
C. `age != 18`  
D. `age >= 18`

### 22. Keeping exam marks inside their legal range

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct validation approach

A marks validator needs one Boolean that is true from 0 through 100, including both limits. Which comparison expresses that interval most clearly?

A. `marks >= 0 or marks <= 100`  
B. `marks > 0 < 100`  
C. `0 <= marks <= 100`  
D. `marks == 0 == 100`

### 23. Checking a submitted PIN without overwriting it

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an operator-selection defect

A security review finds that a developer confused assignment with equality. Which expression asks whether `entered_pin` matches `saved_pin` without assigning either value?

A. `entered_pin == saved_pin`  
B. `entered_pin = saved_pin`  
C. `entered_pin >= saved_pin`  
D. `entered_pin != saved_pin`

### 24. Product codes compared as text

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting unexpected comparison behaviour

A catalog sorts the string codes `"item10"` and `"item2"` alphabetically. A developer expects the numeric-looking suffix 10 to come after 2. Which observation matches Python's string comparison?

A. `"item10" > "item2"` is true because Python extracts the numbers  
B. `"item10" < "item2"` is true because string comparison reaches `'1'` versus `'2'` character by character  
C. Python ignores the shared prefix and automatically compares the suffixes as integers, so `10 > 2`  
D. The shorter numeric suffix sorts first, so `"item2" < "item10"` regardless of character order

### 25. Two checks at a theme park ride

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing condition

A rider may enter only when they are at least 120 cm tall and at least 8 years old. Complete the missing condition:

```python
may_enter = __________
```

Which expression makes `may_enter` match the rule for every rider?

A. `height >= 120 or age >= 8`  
B. `not height >= 120`  
C. `height >= 120 and age >= 8`  
D. `height >= 120 and not age >= 8`

### 26. Two independent ways to earn a discount

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a condition for a realistic policy

A store grants a discount when the shopper is a member or when a festival offer is active. Either fact is sufficient. Which condition matches the policy?

A. `is_member or festival_offer`  
B. `is_member and festival_offer`  
C. `not is_member and festival_offer`  
D. `not (is_member or festival_offer)`

### 27. Turning a block flag into permission

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a Boolean relationship

A gate stores `is_blocked`. The permission value should be true exactly when the visitor is not blocked. Which assignment states that relationship directly?

A. `allowed = is_blocked`  
B. `allowed = is_blocked or True`  
C. `allowed = is_blocked and False`  
D. `allowed = not is_blocked`

### 28. Protecting a calculation with short-circuiting

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `comparison-and-logical-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions; selecting a safe validation expression

A score service should return `True` only when at least one score exists and the average exceeds 80. Which condition checks that complete rule while allowing Python to short-circuit before dividing by zero?

A. `total / count > 80 and count != 0`  
B. `count != 0 and total / count > 80`  
C. `count == 0 or total / count > 80`  
D. `not count != 0 and total / count > 80`

### 29. Awarding bonus points in place

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `assignment-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate update structure

A game should increase the existing `score` by 15. Which statement communicates that update most directly?

A. `score += 15`  
B. `score = 15`  
C. `score == score + 15`  
D. `15 += score`

### 30. A cart total changes three times

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `assignment-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the final value of a variable

A promotional cart runs these updates:

```python
total = 100
total += 50
total *= 2
total -= 40
```

Which amount will be sent to checkout?

A. `112`  
B. `110`  
C. `260`  
D. `300`

### 31. Rewriting an update without changing behavior

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `assignment-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Deciding whether two implementations are equivalent

A reviewer expands the shorthand `items //= 4` for a beginner. Which replacement is equivalent?

A. `items = 4 // items`  
B. `items = items // 4`  
C. `items = items / 4`  
D. `items == items // 4`

### 32. Keeping only the seconds left after full minutes

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `assignment-operators`  
**Is Curriculum Based:** No  
**Assessment type:** Completing an in-place update; final value tracing

A timer stores `367` total seconds. After separately recording the full minutes, it wants to update `seconds` so it contains only the leftover seconds. Which in-place operation leaves `7` in `seconds`?

A. `seconds /= 60`  
B. `seconds //= 60`  
C. `seconds **= 60`  
D. `seconds %= 60`

### 33. A delivery formula is not evaluated left to right

**Difficulty:** Foundational

**Taxonomy:** `python` → `data-types-and-operators` → `operator-precedence`  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating operator precedence

A small fee formula is:

```python
fee = 2 + 3 * 4
```

Which fee reaches the invoice under Python's precedence rules?

A. `20`, because the expression is mistakenly grouped as `(2 + 3) * 4`  
B. `9`, because both operator symbols are mistakenly treated as addition  
C. `14`, because multiplication is performed before addition  
D. `24`, because the expression is mistakenly treated as `2 * 3 * 4`

### 34. Repairing an average that looks believable but is wrong

**Difficulty:** Intermediate

**Taxonomy:** `python` → `data-types-and-operators` → `operator-precedence`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a logic bug; smallest correct repair

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

**Taxonomy:** `python` → `data-types-and-operators` → `operator-precedence`  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating associativity

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

**Taxonomy:** `python` → `data-types-and-operators` → `operator-precedence`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions; repairing a logic bug

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

**Taxonomy:** `python` → `data-types-and-operators` → `input-and-output`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction; unexpected behaviour

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

**Taxonomy:** `python` → `data-types-and-operators` → `input-and-output`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

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

**Taxonomy:** `python` → `data-types-and-operators` → `input-and-output`  
**Is Curriculum Based:** No  
**Assessment type:** Completing formatted output code

A receipt stores `quantity = 2` and `price = 49.5`. The total must appear with exactly two decimal places. Which line produces `Total: ₹99.00`?

A. `print("Total: ₹" + quantity * price)`  
B. `print(f"Total: ₹{quantity + price:.2f}")`  
C. `print("Total: ₹", quantity, price, ".00")`  
D. `print(f"Total: ₹{quantity * price:.2f}")`

### 40. Presenting a performance rate and a large audience

**Difficulty:** Advanced

**Taxonomy:** `python` → `data-types-and-operators` → `input-and-output`  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple format specifications

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
| 2 | D | Intermediate | The literal `23.75` is a float, so it preserves the fractional sensor reading for numeric calculations. |
| 3 | A | Intermediate | The quoted value is a string, while the equality comparison produces the Boolean `True`. |
| 4 | C | Advanced | `float(raw_price)` accepts decimal text such as `"12.50"` and preserves its fractional part; converting through `int` would discard it. |
| 5 | D | Foundational | Floor division gives 4 completely filled trays, while modulo gives the 5 cups left over. |
| 6 | B | Intermediate | At exactly 18, the inclusive requirement says eligible but the strict `>` implementation says ineligible, exposing the defect. |
| 7 | C | Intermediate | `stock -= sold` subtracts 6 from the existing stock and stores 14 back in `stock`. |
| 8 | A | Advanced | Parentheses make the addition occur before multiplication, matching the stated billing rule. |
| 9 | B | Foundational | The f-string inserts mixed value types and formats the total with exactly two decimal places. |
| 10 | D | Intermediate | The cart passes the minimum, and `festival_offer` makes the parenthesised alternative true even though membership is false. |
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
| 28 | B | Advanced | If `count` is zero, the left side is false, the unsafe division is skipped, and the complete condition correctly remains false. |
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
| Variables, assignment, and naming | 1 |
| `int`, `float`, and `complex` | 2 |
| Strings and Booleans | 3, 11–12 |
| Type conversion and `type()` | 4, 13–16 |
| Arithmetic operators | 5, 17–20 |
| Comparison operators | 6, 21–24 |
| Logical operators | 10, 25–28 |
| Assignment and augmented operators | 7, 29–32 |
| Operator precedence and associativity | 8, 33–36 |
| Input, output, and f-strings | 9, 37–40 |

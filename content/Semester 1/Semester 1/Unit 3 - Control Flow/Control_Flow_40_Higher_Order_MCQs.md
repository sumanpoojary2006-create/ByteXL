# Unit 3: Control Flow — 40 Higher-Order MCQs

## Assessment design

- Language: Python 3.10 or newer
- Scope: branching, `if`, `if/else`, `elif`, nested conditions, guard-style checks, `match/case`, truthiness, Boolean logic, conditional expressions, and input validation
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Student expectation: trace the code carefully. Running the code after making a prediction is encouraged.

---

## Questions

### 1. Wallet balance after a payment

**Difficulty:** Foundational

A customer with ₹900 in their wallet attempts a ₹700 payment. The payment service runs this code before showing its response:

```python
balance = 900
amount = 700

if amount > balance:
    print("Declined")

if balance - amount < 300:
    print("Low balance")
else:
    print("Balance healthy")
```

Which response sequence will the customer see?

A. `Declined` followed by `Low balance`  
B. `Balance healthy` only  
C. `Low balance` only  
D. Nothing, because the first condition is false

### 2. The hot-weather fee table

**Difficulty:** Foundational

A delivery service uses the following hot-weather fee rule. A test order is placed when the recorded temperature is 38°C:

```python
temperature = 38
fee = 0

if temperature >= 30:
    fee = 50
elif temperature >= 35:
    fee = 80
else:
    fee = 20
```

Which fee will reach the customer's invoice?

A. `80`  
B. `50`  
C. `20`  
D. `0`

### 3. The cold-chain acceptance gate

**Difficulty:** Intermediate

A lab accepts a temperature only from 2°C through 8°C, including both endpoints.

```python
temperature = 8

if __________:
    print("Accept sample")
else:
    print("Reject sample")
```

The current sample is exactly 8°C. Which condition releases this sample while also accepting every other temperature in the permitted interval—and no temperature outside it?

A. `temperature > 2 or temperature < 8`  
B. `temperature > 2 and temperature < 8`  
C. `temperature >= 2 or temperature <= 8`  
D. `temperature >= 2 and temperature <= 8`

### 4. An active account with the wrong PIN

**Difficulty:** Intermediate

During a security test, an active account opens even though the tester deliberately enters a wrong PIN. The intended rule is to grant access only when the PIN is correct **and** the account is active.

```python
pin_correct = False
account_active = True

if pin_correct or account_active:
    print("Access granted")
else:
    print("Access denied")
```

Which review action closes the security gap while preserving that policy?

A. `or` should be `and`  
B. `account_active` should be compared with `False`  
C. The `else` block should come first  
D. Both variables should be strings

### 5. Conflicting result labels

**Difficulty:** Intermediate

A result must print exactly one label. At a mark of 40, the program currently prints both.

```python
marks = 40

if marks >= 40:
    print("Pass")
if marks <= 40:
    print("Fail")
```

The team wants a one-line patch that also prevents future overlap between the two outcomes. Which patch should be approved?

A. Change the first `>=` to `>`  
B. Replace the second `if marks <= 40:` with `else:`  
C. Change the second `<=` to `>=`  
D. Delete the first `if` block

### 6. Registration on the eighteenth birthday

**Difficulty:** Foundational

A user may register if they are 18 or older.

```python
if age > 18:
    print("Eligible")
else:
    print("Not eligible")
```

The tester has time for one boundary-focused test. Which age should be entered to demonstrate that an eligible user is being rejected?

A. `17`  
B. `19`  
C. `0`  
D. `18`

### 7. Two messages on one result screen

**Difficulty:** Intermediate

The developer expects exactly one message.

```python
if score >= 40:
    print("Pass")

if score <= 50:
    print("Needs support")
```

Which test score should QA use to capture evidence that the screen can display two conflicting messages?

A. `39`  
B. `51`  
C. `45`  
D. `90`

### 8. An inventory rule under future edits

**Difficulty:** Intermediate

An inventory team is choosing between two implementations for a status that must be exactly `"Available"` or `"Sold out"`.

Version A:

```python
if stock > 0:
    message = "Available"
else:
    message = "Sold out"
```

Version B:

```python
if stock > 0:
    message = "Available"
if stock <= 0:
    message = "Sold out"
```

Both currently produce the same value for every integer `stock`. Which design review note gives the strongest reason to approve Version A?

A. It structurally guarantees exactly one branch and avoids maintaining two opposite conditions  
B. Python does not allow two consecutive `if` statements  
C. Version B fails whenever `stock` is zero  
D. Version A checks both conditions and is therefore safer

### 9. Refactoring a required-name check

**Difficulty:** Foundational

A developer simplifies the required-name check in a registration form. In this application, `name` is always a string.

```python
# Version A
if name != "":
    print("Continue")
```

```python
# Version B
if name:
    print("Continue")
```

Before approving the change, which conclusion should the reviewer record?

A. They differ only when `name` contains spaces  
B. They are equivalent for every string value of `name`  
C. Version B accepts only alphabetic names  
D. Version A treats `"0"` as empty, but Version B does not

### 10. Designing a command router

**Difficulty:** Foundational

A command-line assistant supports the fixed commands `"start"`, `"stop"`, and `"help"`, and must give a response for every other command. Which implementation structure would make that design clearest to the next developer?

A. Three unrelated `if` statements  
B. A nested conditional expression  
C. `match`/`case` with `case _`  
D. One `if` with several arithmetic comparisons

### 11. The warning that never appears

**Difficulty:** Intermediate

A road-safety dashboard never displays `"Dangerously fast"`, even when its sensor reports 110 km/h. Its classifier is:

```python
speed = 110

if speed >= 60:
    label = "Fast"
elif speed >= 100:
    label = "Dangerously fast"
else:
    label = "Normal"
```

Which code-review note correctly explains the missing warning?

A. The `else` branch is unreachable  
B. The first branch is unreachable  
C. All three branches are reachable  
D. The `elif` branch is unreachable because every value `>= 100` already matches `>= 60`

### 12. Streaming access with trial time remaining

**Difficulty:** Intermediate

A streaming app prepares one message after checking a signed-in user's subscription and remaining trial time:

```python
logged_in = True
subscription_active = False
trial_days = 2

if logged_in:
    if subscription_active:
        result = "Play"
    elif trial_days > 0:
        result = "Play trial"
    else:
        result = "Renew"
else:
    result = "Sign in"
```

Which message will be prepared for this user?

A. `"Play trial"`  
B. `"Play"`  
C. `"Renew"`  
D. `"Sign in"`

### 13. Operator precedence in an eligibility rule

**Difficulty:** Advanced

At an event gate, a 17-year-old presents a pass but is not accompanied by a parent. The gate applies this rule:

```python
age = 17
has_pass = True
with_parent = False

if age >= 18 or has_pass and with_parent:
    print("Enter")
else:
    print("Wait")
```

Which entry in the gate's audit log correctly describes the decision?

A. `Enter`, because `or` is evaluated before `and`  
B. `Enter`, because `has_pass` alone is true  
C. `Wait`, because the condition groups as `(age >= 18) or (has_pass and with_parent)`  
D. `Wait`, because every comparison with `17` is false

### 14. Zero entered into a stock screen

**Difficulty:** Foundational

In a stock-entry screen, the user types `0` and presses Enter. The developer expects zero quantity to behave like “nothing added.”

```python
quantity = input("Quantity: ")

if quantity:
    print("Item added")
else:
    print("Nothing added")
```

Which test observation will QA actually record?

A. `Nothing added`, because zero is falsy  
B. `Item added`, because `input()` returns the non-empty string `"0"`  
C. A `SyntaxError`  
D. Nothing

### 15. Coffee becomes an invalid selection

**Difficulty:** Intermediate

In a canteen menu, the user types `2`, expecting coffee.

```python
choice = input("Choose: ")

match choice:
    case 1:
        print("Tea")
    case 2:
        print("Coffee")
    case _:
        print("Invalid")
```

Which behaviour will the support team observe?

A. `Tea` prints because the first numeric case is tried first  
B. `Coffee` prints because `2` and `"2"` match  
C. Python raises an error at `match`  
D. `Invalid` prints because the input is the string `"2"`, not the integer `2`

### 16. Repairing a kiosk that crashed on letters

**Difficulty:** Intermediate

A registration kiosk must accept digit-only ages from 1 through 120. Four patches have been proposed after the kiosk crashed on `"abc"`. Which patch validates the text before conversion and handles the permitted range correctly?

A.

```python
raw_age = input("Age: ")
if not raw_age.isdigit():
    print("Use digits")
else:
    age = int(raw_age)
    if age < 1 or age > 120:
        print("Out of range")
    else:
        print("Accepted")
```

B.

```python
raw_age = input("Age: ")
age = int(raw_age)
if raw_age.isdigit() and 1 <= age <= 120:
    print("Accepted")
```

C.

```python
raw_age = input("Age: ")
if raw_age:
    print("Accepted")
```

D.

```python
raw_age = input("Age: ")
if not raw_age.isdigit() and int(raw_age) > 120:
    print("Invalid")
else:
    print("Accepted")
```

### 17. A coupon on a non-member order

**Difficulty:** Advanced

A checkout service calculates a coupon discount for this order:

```python
member = False
cart_total = 1200
coupon = "SAVE"

if member and cart_total >= 500 or coupon == "SAVE":
    discount = 100
else:
    discount = 0
```

Which discount amount will appear on the invoice?

A. `0`, because `member` is false  
B. `0`, because both sides of `or` must be true  
C. `100`, because the condition is `(member and cart_total >= 500) or coupon == "SAVE"`  
D. The code fails because `and` and `or` cannot appear together

### 18. The college event admission policy

**Difficulty:** Intermediate

A college event admits a student only if the student has an ID and either has registered or is on the guest list. Which condition exactly represents the policy?

A. `has_id or registered and on_guest_list`  
B. `has_id and (registered or on_guest_list)`  
C. `(has_id and registered) and on_guest_list`  
D. `has_id or registered or on_guest_list`

### 19. Avoiding division when no scores exist

**Difficulty:** Advanced

The program should print `"High average"` only when `count` is non-zero and `total / count` is greater than 80. Which condition is safe even when `count` is `0`?

A. `if total / count > 80 and count != 0:`  
B. `if count == 0 or total / count > 80:`  
C. `if total > 80 or count:`  
D. `if count != 0 and total / count > 80:`

### 20. The scholarship status badge

**Difficulty:** Intermediate

A scholarship portal prepares a status badge using the following checks:

```python
points = 70
verified = True
status = "Review"

if points >= 60:
    status = "Eligible"
    if not verified:
        status = "Verify first"
else:
    status = "Rejected"
```

Which badge will the applicant see after the checks finish?

A. `"Eligible"`  
B. `"Verify first"`  
C. `"Rejected"`  
D. `"Review"`

### 21. The order quantity gate

**Difficulty:** Intermediate

An ordering screen accepts quantities from 1 through 10, inclusive. The incomplete first branch must stop every value outside that range before the order continues.

```python
quantity = 10

if __________:
    print("Invalid quantity")
else:
    print("Accepted")
```

Which condition should replace the blank so that the gate rejects exactly the out-of-range quantities?

A. `quantity < 1 and quantity > 10`  
B. `quantity < 1 or quantity > 10`  
C. `quantity <= 1 or quantity >= 10`  
D. `quantity > 1 and quantity < 10`

### 22. The score validator that rejects nothing

**Difficulty:** Advanced

The intended valid score is from 0 through 100. During testing, `-5`, `50`, and `150` are all labelled valid.

```python
if score >= 0 or score <= 100:
    print("Valid")
else:
    print("Invalid")
```

Which code-review finding explains why the invalid cases never reach the rejection message?

A. Only the score `50` is accepted  
B. The condition fails only for negative scores  
C. The boundaries must both be made strict  
D. `or` makes the condition true for every numeric score; it should be `and`

### 23. A score of 95 receives grade C

**Difficulty:** Intermediate

A student who scores 95 is incorrectly assigned grade C. The team wants to preserve all existing thresholds and labels.

```python
if marks >= 40:
    grade = "C"
elif marks >= 75:
    grade = "B"
elif marks >= 90:
    grade = "A"
else:
    grade = "F"
```

Which proposed reorder should be approved?

A. Reorder the checks as `>= 90`, then `>= 75`, then `>= 40`  
B. Replace every `elif` with `if`  
C. Move `else` to the top  
D. Reverse only the labels, leaving the conditions in place

### 24. A coupon that expires one day early

**Difficulty:** Foundational

A coupon is valid through and including 31 July. Dates are represented here only by the July day number.

```python
if day >= 1 and day < 31:
    print("Coupon valid")
else:
    print("Coupon expired")
```

On 31 July, a customer is incorrectly told the coupon has expired. Which change aligns the program with the advertised validity period?

A. Change `day >= 1` to `day > 1`  
B. Change `and` to `or`  
C. Change `day < 31` to `day <= 31`  
D. Change `day < 31` to `day == 31`

### 25. Proving free delivery is too easy to obtain

**Difficulty:** Advanced

The rule says: “A delivery is free only when the customer is a member **and** the order total is at least ₹500.” The code is:

```python
if is_member or total >= 500:
    delivery_fee = 0
else:
    delivery_fee = 50
```

Which customer profile gives QA the clearest evidence that free delivery is being granted without satisfying the full policy?

A. `is_member = True`, `total = 500`  
B. `is_member = False`, `total = 500`  
C. `is_member = False`, `total = 499`  
D. `is_member = True`, `total = 900`

### 26. Stacking two earned discounts

**Difficulty:** Advanced

A shop may stack a coupon discount and a member discount. Two developers submit these implementations:

Version A:

```python
if has_coupon:
    discount += 50
if is_member:
    discount += 50
```

Version B:

```python
if has_coupon:
    discount += 50
elif is_member:
    discount += 50
```

Assume `discount` starts at `0`. Which customer profile demonstrates that only one version actually stacks both earned benefits?

A. Only when both values are false  
B. Whenever exactly one value is true  
C. They never differ  
D. Only when both `has_coupon` and `is_member` are true

### 27. Refactoring the login rejection rule

**Difficulty:** Advanced

A security engineer wants to refactor Version A without changing which login attempts are rejected:

```python
if not (correct_pin and active_account):
    print("Reject")
```

Which proposed Version B preserves the rejection decision for every combination of PIN and account state?

A. `if not correct_pin or not active_account:`  
B. `if not correct_pin and not active_account:`  
C. `if correct_pin or active_account:`  
D. `if correct_pin and not active_account:`

### 28. Assigning a report-card status

**Difficulty:** Foundational

A report-card program only needs to assign `"Pass"` when `marks >= 40` and `"Fail"` otherwise. No logging or additional action belongs to either path. Which implementation should the reviewer approve for this small value choice?

A. Two separate `if` statements  
B. A `match` statement with numeric ranges  
C. `status = "Pass" if marks >= 40 else "Fail"`  
D. A nested conditional expression

### 29. The missing large-transfer label

**Difficulty:** Intermediate

A payment dashboard correctly labels positive, zero, and negative amounts, but the `"Large payment"` label has never appeared—even for transfers above ₹1,000.

```python
if amount > 0:
    message = "Positive"
elif amount > 1000:
    message = "Large payment"
elif amount == 0:
    message = "Zero"
else:
    message = "Negative"
```

Which condition is being shadowed by an earlier decision?

A. `amount > 0`  
B. `amount > 1000`  
C. `amount == 0`  
D. `else`

### 30. A minor arrives with a valid cinema ticket

**Difficulty:** Intermediate

At a cinema gate, a 15-year-old arrives with a valid ticket. The screen follows these nested rules:

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enter alone")
    else:
        print("Adult required")
else:
    print("Buy ticket")
```

Which instruction will appear on the gate screen?

A. `Enter alone`  
B. `Buy ticket`  
C. Both `Adult required` and `Buy ticket`  
D. `Adult required`

### 31. The turnstile permission value

**Difficulty:** Advanced

An access service computes `allowed` before deciding whether to unlock a turnstile:

```python
is_blocked = False
is_admin = False
has_pass = True

allowed = not is_blocked and is_admin or has_pass
```

Which audit interpretation correctly predicts whether the stored decision will unlock the turnstile?

A. `False`, because `is_admin` is false  
B. `False`, because `not` applies to the entire expression  
C. `True`, because the expression groups as `((not is_blocked) and is_admin) or has_pass`  
D. The expression is invalid without parentheses

### 32. A zero reading in a non-empty batch

**Difficulty:** Intermediate

A sensor submits one reading, and that reading happens to be zero. The dashboard uses the collection itself to decide whether data arrived:

```python
readings = [0]

if readings:
    message = "Data received"
else:
    message = "No data"
```

Which message card will the dashboard display?

A. `"Data received"`, because the list contains one item even though that item is `0`  
B. `"No data"`, because `0` is falsy  
C. `"No data"`, because all lists are falsy  
D. Python raises an error when a list is used as a condition

### 33. A winter temperature rejected as non-numeric

**Difficulty:** Intermediate

A weather app should accept whole-number temperatures from -50 through 60.

```python
raw = input("Temperature: ")

if raw.isdigit():
    temperature = int(raw)
    if -50 <= temperature <= 60:
        print("Accepted")
    else:
        print("Out of range")
else:
    print("Use a whole number")
```

The perfectly valid temperature `-5` is rejected before the range check. Which review note accounts for that behaviour?

A. `int("-5")` cannot produce a negative integer  
B. The range condition excludes `-5`  
C. `input()` automatically converts `-5` to a float  
D. `"-5".isdigit()` is false because the minus sign is not a digit

### 34. A required name made entirely of spaces

**Difficulty:** Intermediate

A required name must contain something other than spaces. The current code accepts the input `"   "`.

```python
name = input("Name: ")

if name:
    print("Accepted")
else:
    print("Name required")
```

Which smallest condition change rejects this entry—and any other whitespace-only name—without rejecting a real name?

A. `if name == True:`  
B. `if name.strip():`  
C. `if name.isdigit():`  
D. `if not name:`

### 35. The ₹750 cart discount tier

**Difficulty:** Foundational

A shopping cart assigns a discount rate from the order amount. The current cart total is ₹750:

```python
amount = 750

if amount >= 1000:
    rate = 0.20
elif amount >= 500:
    rate = 0.10
elif amount >= 100:
    rate = 0.05
else:
    rate = 0
```

Which discount rate will be attached to this cart?

A. `0.10`  
B. `0.20`  
C. `0.05`  
D. `0`

### 36. Showing one loan rejection reason

**Difficulty:** Intermediate

A loan application should show one specific reason for rejection, checking these rules in order:

1. Applicant must be at least 21.
2. Income must be at least ₹25,000.
3. Existing debt must not exceed ₹10,000.
4. Otherwise approve.

Which implementation should the loan team select so that the applicant receives the first applicable reason—or approval—and never receives conflicting messages?

A.

```python
if age < 21:
    print("Too young")
if income < 25000:
    print("Income too low")
if debt > 10000:
    print("Debt too high")
else:
    print("Approved")
```

B.

```python
if age >= 21 and income >= 25000 and debt <= 10000:
    print("Approved")
else:
    print("Too young")
```

C.

```python
if age < 21:
    print("Too young")
elif income < 25000:
    print("Income too low")
elif debt > 10000:
    print("Debt too high")
else:
    print("Approved")
```

D.

```python
if age < 21 or income < 25000 or debt > 10000:
    print("Approved")
else:
    print("Rejected")
```

### 37. A catch-all command placed too early

**Difficulty:** Advanced

A command processor fails to start after a developer moves the catch-all case above the supported commands:

```python
command = "stop"

match command:
    case _:
        message = "Unknown"
    case "start":
        message = "Starting"
    case "stop":
        message = "Stopping"
```

Which build report correctly explains why the program cannot begin processing `"stop"`?

A. `message` becomes `"Unknown"`  
B. Python reports a syntax error because the wildcard makes the later cases unreachable  
C. `message` becomes `"Stopping"`  
D. All three cases run in order

### 38. The distinction badge overwrites the pass badge

**Difficulty:** Intermediate

A learning portal assigns a badge after checking both its general pass rule and its distinction rule:

```python
score = 85
badge = "None"

if score >= 50:
    badge = "Pass"

if score >= 80:
    badge = "Distinction"
else:
    badge = "Standard"
```

Which badge will be visible after both checks have run?

A. `"Pass"`  
B. `"Standard"`  
C. `"None"`  
D. `"Distinction"`

### 39. A blocked VIP enters the venue

**Difficulty:** Advanced

The intended rule is: a user may enter only if they are not blocked **and** they either have a ticket or are a VIP.

```python
if not blocked and has_ticket or is_vip:
    print("Enter")
```

During a security test, a blocked VIP is admitted. Which smallest patch makes the gate enforce the stated rule unambiguously?

A. `if not (blocked and has_ticket) or is_vip:`  
B. `if not blocked or (has_ticket and is_vip):`  
C. `if not blocked and (has_ticket or is_vip):`  
D. `if not (blocked and has_ticket and is_vip):`

### 40. A finance readability refactor

**Difficulty:** Foundational

A finance developer replaces Version A with Version B during a readability cleanup.

Version A:

```python
if balance >= amount:
    result = "Approved"
else:
    result = "Declined"
```

Version B:

```python
result = "Approved" if balance >= amount else "Declined"
```

Which review conclusion determines whether the refactor can be merged without changing customer decisions?

A. The versions assign the same `result` for all values of `balance` and `amount`; Version B is suitable because the decision only chooses one value  
B. Version B reverses the true and false outcomes  
C. Version A may run both assignments  
D. Version B works only when `balance` and `amount` are Boolean

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | The first `if` is false. The second `if` is true because `900 - 700` is `200`, which is below `300`; its `else` is skipped. |
| 2 | B | Foundational | `38 >= 30` is the first true condition, so the chain stops and assigns `50`. The later, more specific threshold is never checked. |
| 3 | D | Intermediate | Both limits must hold, so the comparisons need `and`; `>=` and `<=` include the endpoints. |
| 4 | A | Intermediate | The policy requires both facts to be true. `or` grants access when only one passes. |
| 5 | B | Intermediate | `else` makes failure the one mutually exclusive alternative to passing and removes the duplicated boundary test. |
| 6 | D | Foundational | Age `18` should qualify under “18 or older,” but `age > 18` rejects it. |
| 7 | C | Intermediate | `45` satisfies both `score >= 40` and `score <= 50`, so both independent blocks run. |
| 8 | A | Intermediate | The policy has exactly two complementary outcomes. `if/else` expresses that invariant without a second condition that a later edit could make overlap or leave a gap. |
| 9 | B | Foundational | For strings, only `""` is falsy. Therefore “not equal to the empty string” and direct truthiness give the same branch decision. |
| 10 | C | Foundational | `match/case` is designed for comparing one value with several fixed options, and `case _` handles everything else. |
| 11 | D | Intermediate | Every speed at least `100` is also at least `60`; the first branch captures it before the `elif` can be reached. |
| 12 | A | Intermediate | Login passes, subscription does not, and `trial_days > 0` is true, so `"Play trial"` is assigned. |
| 13 | C | Advanced | `and` binds more tightly than `or`. The age test is false and `True and False` is false, so the whole condition is false. |
| 14 | B | Foundational | `input()` returns text. The string `"0"` is non-empty and therefore truthy, unlike the integer `0`. |
| 15 | D | Intermediate | The cases contain integers, but `input()` returns `"2"`. No integer case matches, so the wildcard runs. |
| 16 | A | Intermediate | It checks the text shape before conversion, converts only in the safe branch, and then performs inclusive range validation. |
| 17 | C | Advanced | `and` is evaluated before `or`. The member subexpression is false, but the correct coupon makes the overall condition true. |
| 18 | B | Intermediate | ID is mandatory, while registration and guest-list membership are alternatives. The parentheses make that policy explicit. |
| 19 | D | Advanced | With `and`, a zero count makes the left side false and Python short-circuits before attempting division. |
| 20 | A | Intermediate | The outer condition assigns `"Eligible"`. Because `verified` is true, `not verified` is false and there is no later overwrite. |
| 21 | B | Intermediate | A value is invalid if it falls below the lower bound or above the upper bound. Values `1` and `10` remain accepted. |
| 22 | D | Advanced | No number can be both below `0` and above `100`; at least one side of the `or` is always true. The valid interval requires both comparisons. |
| 23 | A | Intermediate | In an `elif` chain, the first true branch wins. Testing the highest threshold first prevents a broad lower threshold from capturing higher scores. |
| 24 | C | Foundational | “Through and including 31” requires an inclusive upper comparison, `<= 31`. |
| 25 | B | Advanced | A non-member at exactly ₹500 fails the stated membership requirement but receives free delivery under the incorrect `or` condition. |
| 26 | D | Advanced | Two independent `if` statements apply both ₹50 discounts when both facts are true, producing ₹100. The `elif` version stops after the first and produces ₹50. |
| 27 | A | Advanced | A combined success fails when either required part fails: `not (A and B)` is equivalent to `not A or not B`. |
| 28 | C | Foundational | A conditional expression is appropriate for choosing between two values in one simple assignment. |
| 29 | B | Intermediate | Every amount over `1000` has already satisfied `amount > 0`, so the second branch cannot run. |
| 30 | D | Intermediate | The inner `else` pairs with the inner `if age >= 18`. The ticket check passes, but the age check does not. |
| 31 | C | Advanced | Precedence is `not`, then `and`, then `or`. The left combined part is false, but `has_pass` is true, so `allowed` becomes true. |
| 32 | A | Intermediate | The list itself is non-empty and therefore truthy. Python does not require the contained item to be truthy. |
| 33 | D | Intermediate | `.isdigit()` requires every character to be a digit. The leading minus sign causes the shape check to fail before conversion. |
| 34 | B | Intermediate | `.strip()` removes surrounding whitespace. A spaces-only entry becomes `""`, which is falsy. |
| 35 | A | Foundational | `750` misses the first threshold but meets `>= 500`; the first matching `elif` assigns `0.10`. |
| 36 | C | Intermediate | The ordered `if/elif/else` chain gives the first applicable rejection reason and guarantees exactly one outcome. |
| 37 | B | Advanced | `case _` matches every value. Python rejects later cases as unreachable instead of silently allowing a catch-all before specific cases. |
| 38 | D | Intermediate | The first `if` sets `"Pass"`, then the second independent `if` is also true and overwrites it with `"Distinction"`. |
| 39 | C | Advanced | The user must first pass `not blocked`; inside that requirement, either a ticket or VIP status is sufficient. |
| 40 | A | Foundational | Both versions make the same two-way value selection. The conditional expression is concise without hiding multiple branches or actions. |

## Coverage summary

| Assessment behaviour | Question numbers |
|---|---|
| Scenario-based output prediction | 1, 13, 14, 15, 30, 37 |
| Final value tracing | 2, 12, 17, 20, 31, 35, 38 |
| Missing conditions and validation | 3, 16, 19, 21, 34 |
| Logic bugs, boundaries, and repairs | 4, 5, 6, 7, 11, 22, 23, 24, 25, 29, 33, 39 |
| Comparing implementations and equivalence | 8, 9, 26, 27, 40 |
| Selecting an appropriate structure | 10, 18, 28, 36 |
| Truthiness and precedence | 13, 14, 17, 27, 31, 32 |

import random
import openpyxl

random.seed(17)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])
SET1 = [
    # 1. Scenario-based
    (
        "A ride-sharing app calculates a trip's cost from a base fare plus a per-kilometre rate.\n\n```python\nbase_fare = 50\ndistance_km = 12\nrate_per_km = 8\n\ncost = base_fare + distance_km * rate_per_km\n\nprint(cost)\n```\n\nA customer books a 12 km ride. What will the app print as the total cost?",
        "Multiplication runs before addition, so `distance_km * rate_per_km` is 96 first, then `50 + 96` is 146.",
        "medium", "apply", "arithmetic-operators",
        "146",
        ["744", "70", "116"],
    ),
    # 2. Output prediction
    (
        "A developer traces how variable assignment works when one variable is set equal to another.\n\n```python\nx = 5\ny = x\nx = x + 1\n\nprint(x, y)\n```\n\nWhat will this code print?",
        "`y = x` copies the value 5 into `y` at that moment. `x = x + 1` then changes `x` to 6, but `y` still holds 5, so `print(x, y)` shows `6 5`.",
        "easy", "apply", "variables-and-assignment",
        "6 5",
        ["6 6", "5 6", "5 5"],
    ),
    # 3. Error identification
    (
        "A login form reads a user's typed age and immediately compares it to a number.\n\n```python\nage = input('Age: ')\n\nif age > 18:\n    print('Eligible')\n```\n\nWhen a user types '25', this code raises a `TypeError`. Why does this happen?",
        "`input()` always returns a string, and Python cannot compare a string to the integer 18 with `>` without converting `age` to a number first.",
        "medium", "analyze", "input-and-output",
        "`input()` always returns a string, and a string can't be compared to an integer with `>`",
        ["The variable `age` was never assigned a value", "`if` statements cannot use the `>` operator", "`input()` only works inside a `print()` call"],
    ),
    # 4. Code correction
    (
        "A program is supposed to calculate a discounted price for a ₹1000 item at 20% off, but a teammate's rewrite always gives 0.\n\n```python\nprice = 1000\ndiscount_percent = 20\n\nfinal_price = (price - price) * discount_percent / 100\n```\n\nWhich option correctly fixes this code so it calculates the discount properly?",
        "The added parentheses force `price - price` to be calculated first, which is always 0. Removing them restores the correct order: subtract the discount amount from the original price.",
        "hard", "analyze", "operator-precedence",
        "Remove the parentheses: `final_price = price - price * discount_percent / 100`",
        ["Change `discount_percent = 20` to `discount_percent = 100`", "Change `-` to `+` inside the parentheses", "Divide by `1000` instead of `100`"],
    ),
    # 5. Concept identification
    (
        "A program runs this line:\n\n```python\nresult = 10 > 5\n```\n\nWhich data type does the value stored in `result` belong to?",
        "A comparison like `>` always produces a boolean value, `True` or `False`.",
        "easy", "understand", "strings-and-booleans",
        "Boolean (`bool`)",
        ["Integer (`int`)", "String (`str`)", "Floating-point (`float`)"],
    ),
    # 6. Dry-run / trace-based
    (
        "A savings app tracks a customer's balance through two operations: a withdrawal, followed by splitting what's left between two accounts.\n\n```python\nbalance = 100\nbalance -= 30\nbalance //= 2\n```\n\nWhat is the value of `balance` after this code runs?",
        "First `balance -= 30` makes balance 70. Then `balance //= 2` floor-divides 70 by 2, giving 35.",
        "medium", "apply", "assignment-operators",
        "35",
        ["50", "70", "17"],
    ),
    # 7. Best replacement code
    (
        "A developer writes this nested check to confirm both a payment and a seat are available:\n\n```python\nif payment_ok:\n    if seat_available:\n        confirmed = True\n    else:\n        confirmed = False\nelse:\n    confirmed = False\n```\n\nWhich option is the best way to simplify this into a single line?",
        "`confirmed` should only be True when both `payment_ok` and `seat_available` are True — exactly what `and` checks in one line.",
        "medium", "analyze", "comparison-and-logical-operators",
        "`confirmed = payment_ok and seat_available`",
        ["`confirmed = payment_ok or seat_available`", "`confirmed = not payment_ok and seat_available`", "`confirmed = payment_ok and not seat_available`"],
    ),
    # 8. Missing code / fill in the blank
    (
        "A form needs to convert a typed value into a whole number before doing arithmetic.\n\n```python\nage_text = '25'\nage = ______(age_text)\n```\n\nWhich function correctly replaces the blank so `age` becomes the integer 25?",
        "`int()` parses a digit string and returns the equivalent whole number.",
        "easy", "apply", "type-conversion",
        "int",
        ["str", "bool", "len"],
    ),
    # 9. Code-to-requirement matching
    (
        "A developer writes this code intending to check whether two calculated prices are equal:\n\n```python\nprice1 = 0.1 + 0.2\nprice2 = 0.3\n\nif price1 == price2:\n    same = True\nelse:\n    same = False\n```\n\nDoes this code correctly detect that `price1` and `price2` represent the same amount?",
        "Floating-point numbers can't represent some decimals exactly, so `0.1 + 0.2` comes out as a value very slightly different from `0.3`. `==` sees them as unequal, so `same` becomes False even though the amounts are conceptually the same.",
        "hard", "analyze", "numeric-types",
        "No — floating-point rounding means `0.1 + 0.2` is not exactly `0.3`, so `same` becomes False",
        ["Yes — `==` always works correctly for decimal numbers", "No — `==` cannot be used with `float` values at all", "Yes — but only because Python rounds automatically"],
    ),
    # 10. Edge-case reasoning
    (
        "A temperature-logging script computes the remainder of a negative reading using Python's `%` operator.\n\n```python\nresult = -7 % 3\n```\n\nWhat is the value of `result`?",
        "Python's `%` follows floor division, so the result always has the same sign as the divisor: `-7 % 3` is 2, since `-7 // 3` is -3 and `-3 * 3 + 2 = -7`.",
        "hard", "analyze", "arithmetic-operators",
        "2",
        ["-1", "-2", "1"],
    ),
]

SET2 = [
    # --- Scenario-based (3) ---
    (
        "A recipe app scales a serving size for a dinner party.\n\n```python\nservings = 7\nguests = 2\n\nportion = servings / guests\n\nprint(portion)\n```\n\nA recipe makes 7 portions and needs to be split evenly between 2 people. What will this app print as each person's share?",
        "`/` performs true division, so 7 divided by 2 is 3.5, which prints.",
        "easy", "apply", "numeric-types",
        "3.5",
        ["3", "4", "3.0"],
    ),
    (
        "A signup form reads a user's birth year as typed text and converts it to a number for an age calculation.\n\n```python\nbirth_year_text = '2007'\nbirth_year = int(birth_year_text)\n\nprint(birth_year)\n```\n\nA user types '2007' as their birth year. What will the form print as the converted value?",
        "`int('2007')` parses the digit string and returns the whole number 2007.",
        "easy", "apply", "type-conversion",
        "2007",
        ["'2007'", "2007.0", "Error"],
    ),
    (
        "A weather app only issues a storm warning when two separate sensor readings both cross their thresholds.\n\n```python\nreading1 = 5\nreading2 = 2\n\nwarning = (reading1 > 3) and (reading2 > 4)\n\nprint(warning)\n```\n\nThe first sensor reads 5 (threshold 3) and the second reads 2 (threshold 4). What will this app print?",
        "`reading1 > 3` is True, but `reading2 > 4` is False. `and` needs both to be True, so `warning` is False.",
        "medium", "apply", "comparison-and-logical-operators",
        "False",
        ["True", "Error", "None"],
    ),
    # --- Output prediction (3) ---
    (
        "A loyalty-program script counts how many of three checks passed by adding the boolean results directly.\n\n```python\npassed = True + True + False\n\nprint(passed)\n```\n\nWhat will this code print?",
        "Python treats `True` as 1 and `False` as 0 in arithmetic, so `True + True + False` becomes `1 + 1 + 0`, which is 2.",
        "hard", "analyze", "strings-and-booleans",
        "2",
        ["3", "Error", "True"],
    ),
    (
        "A shopping cart script starts empty and adds the same item price three times.\n\n```python\ntotal = 0\ntotal += 5\ntotal += 5\ntotal += 5\n\nprint(total)\n```\n\nWhat will this code print?",
        "Each `+=` adds 5 onto the existing value, so three additions build up to 0 + 5 + 5 + 5 = 15.",
        "medium", "apply", "assignment-operators",
        "15",
        ["5", "0", "20"],
    ),
    (
        "A voting app checks whether a submitted candidate ID matches the one on file.\n\n```python\ncandidate_id = 'C102'\n\nprint(candidate_id == 'C102')\n```\n\nWhat will this code print?",
        "The two strings are identical, so `==` evaluates to True.",
        "easy", "apply", "comparison-and-logical-operators",
        "True",
        ["False", "Error", "'C102'"],
    ),
    # --- Dry-run / trace-based (3) ---
    (
        "A marathon app updates a runner's registered age once their birthday passes.\n\n```python\nage = 25\nage = 26\n```\n\nWhat is the value of `age` after this code runs?",
        "The second assignment overwrites the first — `age` simply points to the new value, 26.",
        "easy", "understand", "variables-and-assignment",
        "26",
        ["25", "Error", "None"],
    ),
    (
        "A survey app reads a satisfaction rating typed as text.\n\n```python\nrating = float('4.5')\n```\n\nWhat is the value stored in `rating` after this line runs?",
        "`float('4.5')` parses the text and returns the decimal value 4.5.",
        "medium", "apply", "type-conversion",
        "4.5",
        ["'4.5'", "4", "Error"],
    ),
    (
        "A warehouse system packs 17 identical parcels into vans that each hold 5 parcels.\n\n```python\nparcels = 17\nvans = parcels // 5\n```\n\nWhat is the value of `vans` after this code runs?",
        "`//` is floor division. 17 divided by 5 is 3.4, and floor division drops the decimal part, giving 3.",
        "medium", "apply", "arithmetic-operators",
        "3",
        ["3.4", "3.0", "2"],
    ),
    # --- Edge-case reasoning (3) ---
    (
        "A program reads a price as text and tries to convert it directly into a whole number.\n\n```python\nprice_text = '199.99'\nprice = int(price_text)\n```\n\nWhat happens when this code runs?",
        "`int()` can only parse strings that represent whole numbers directly. `'199.99'` contains a decimal point, so `int('199.99')` raises a `ValueError`.",
        "hard", "analyze", "type-conversion",
        "It raises a ValueError",
        ["It stores 200, rounded up", "It stores 199", "It stores 0"],
    ),
    (
        "A feedback form treats an empty text response as 'no answer given.'\n\n```python\nresponse = ''\n```\n\nWhat does `bool(response)` evaluate to for this empty response?",
        "An empty string is falsy in Python, so `bool('')` is False.",
        "medium", "understand", "strings-and-booleans",
        "False",
        ["True", "Error", "None"],
    ),
    (
        "A student checks how Python handles a chain of exponents, since `**` can be applied more than once in a row.\n\n```python\nresult = 2 ** 3 ** 2\n```\n\nWhat is the value of `result`?",
        "`**` groups from right to left, so this is `2 ** (3 ** 2)` = `2 ** 9` = 512, not `(2 ** 3) ** 2` = 64.",
        "hard", "analyze", "operator-precedence",
        "512",
        ["64", "18", "36"],
    ),
    # --- Concept identification (3) ---
    (
        "A program runs this line:\n\n```python\nage = int('25')\n```\n\nWhich concept does this line demonstrate?",
        "This line converts a piece of text into a numeric type, which is type conversion.",
        "easy", "understand", "type-conversion",
        "Type conversion",
        ["Arithmetic operator", "Boolean logic", "String concatenation"],
    ),
    (
        "A program runs this line:\n\n```python\nleftover = 50 % 6\n```\n\nWhich concept does this line demonstrate?",
        "`%` computes the remainder left over after division — the modulus operator.",
        "easy", "understand", "arithmetic-operators",
        "The modulus (remainder) operator",
        ["Floor division", "Type conversion", "String formatting"],
    ),
    (
        "A program runs this code:\n\n```python\nx = 5\ny = x\nx = x + 1\n```\n\nWhich concept does this code demonstrate?",
        "This code stores a value in `x`, copies it to `y`, then reassigns `x` — variable assignment and reassignment.",
        "medium", "understand", "variables-and-assignment",
        "Variable assignment and reassignment",
        ["A boolean comparison", "A type conversion", "String formatting"],
    ),
    # --- Logic modification (3) ---
    (
        "A ride-sharing app currently calculates cost using a flat rate per kilometre, with no base fare.\n\n```python\ndistance_km = 12\nrate_per_km = 8\n\ncost = distance_km * rate_per_km\n```\n\nThe business now wants to add a fixed base fare of 50 to every trip. What should be changed in the code?",
        "Adding `50 +` to the calculation includes the fixed base fare on top of the distance-based cost.",
        "medium", "apply", "arithmetic-operators",
        "Change `cost = distance_km * rate_per_km` to `cost = 50 + distance_km * rate_per_km`",
        ["Change `rate_per_km = 8` to `rate_per_km = 58`", "Change `*` to `+` only", "Change `distance_km = 12` to `distance_km = 50`"],
    ),
    (
        "A billing app currently converts a typed price to a whole number, losing the paise.\n\n```python\nprice_text = '49.50'\nprice = int(price_text)\n```\n\nThe business wants the exact decimal amount preserved instead of rounding down to a whole number. What should be changed?",
        "`float()` parses a decimal string and keeps the fractional part, unlike `int()`.",
        "medium", "apply", "type-conversion",
        "Change `int(price_text)` to `float(price_text)`",
        ["Change `price_text = '49.50'` to `price_text = '4950'`", "Change `int` to `str`", "Add `+ 0.5` after `int(price_text)`"],
    ),
    (
        "A discount checker currently requires a customer to be BOTH a loyalty member AND to have spent over ₹1000 to get a discount.\n\n```python\nis_member = True\nspent_over_1000 = False\n\neligible = is_member and spent_over_1000\n```\n\nThe business now wants the discount if EITHER condition is true. What should be changed?",
        "`or` grants the discount if at least one condition is True, matching the new requirement.",
        "medium", "apply", "comparison-and-logical-operators",
        "Change `and` to `or`",
        ["Change `is_member = True` to `is_member = False`", "Change `eligible = is_member and spent_over_1000` to `eligible = not is_member`", "Swap the two variable names"],
    ),
    # --- Error identification (2) ---
    (
        "A signup form accidentally tries to add a number directly onto typed input.\n\n```python\nage = input('Age: ')\n\nprint(age + 1)\n```\n\nThis raises a `TypeError`. Why?",
        "`input()` always returns a string, and a string cannot be added to an integer without converting it first.",
        "medium", "apply", "input-and-output",
        "`age` is a string, and a string cannot be added to an integer directly",
        ["The `input()` function never works inside `print()`", "The `+` operator does not work on variables", "`age` must be declared as global first"],
    ),
    (
        "A student expects `10 - 2 * 3` to be evaluated strictly left to right, like reading normal text, expecting 24.\n\n```python\nresult = 10 - 2 * 3\n```\n\nPython gives `result = 4`, not 24. Why?",
        "Multiplication has higher precedence than subtraction, so `2 * 3` is calculated first, giving 6, and then `10 - 6 = 4`.",
        "medium", "analyze", "operator-precedence",
        "Multiplication happens before subtraction, so `2 * 3` is calculated first, giving `10 - 6 = 4`",
        ["Python evaluates every expression strictly left to right, with no exceptions", "The `-` operator is broken for expressions with multiplication", "`result` was assigned the wrong value by mistake elsewhere"],
    ),
    # --- Code correction (2) ---
    (
        "A program crashes when converting a decimal-looking price directly to an integer.\n\n```python\nprice_text = '199.99'\nprice = int(price_text)\n```\n\nWhich option correctly fixes this so the price is stored as a whole number without crashing?",
        "Converting to `float` first parses the decimal text safely, and wrapping that in `int()` then truncates it to a whole number.",
        "medium", "apply", "type-conversion",
        "Use `int(float(price_text))` instead",
        ["Use `str(price_text)` instead", "Use `bool(price_text)` instead", "Remove the quotes around `199.99` in the original text"],
    ),
    (
        "A grading tool wants to check whether a score is strictly between 2 and 10, but a developer writes the check incorrectly.\n\n```python\nscore = 15\nresult = 2 < score > 10\n```\n\nThis produces a misleading `True` for scores that are actually too high. Which option correctly fixes this check?",
        "`2 < score < 10` correctly chains both bounds, so a score of 15 correctly evaluates to False.",
        "hard", "analyze", "comparison-and-logical-operators",
        "Use `2 < score < 10` instead",
        ["Use `score > 2 or score > 10` instead", "Change `15` to `'15'`", "Remove the `2 <` part entirely"],
    ),
    # --- Best replacement code (2) ---
    (
        "A developer currently checks a discount using a verbose nested structure:\n\n```python\nif is_member:\n    if spent_over_1000:\n        discount = 0.10\n    else:\n        discount = 0\nelse:\n    discount = 0\n```\n\nWhich option is the best way to simplify this into a single line?",
        "`discount` should be 0.10 only when both conditions are True — a ternary expression combined with `and` captures this in one line.",
        "hard", "analyze", "comparison-and-logical-operators",
        "`discount = 0.10 if (is_member and spent_over_1000) else 0`",
        ["`discount = 0.10 if is_member or spent_over_1000 else 0`", "`discount = 0.10 if not is_member else 0`", "`discount = 0.10 if spent_over_1000 else is_member`"],
    ),
    (
        "A developer currently builds a formatted message using string concatenation with manual conversion:\n\n```python\nname = 'Asha'\nscore = 92\nmessage = 'Hello, ' + name + '! Your score is ' + str(score) + '.'\n```\n\nWhich option is the best way to rewrite this using an f-string?",
        "An f-string can embed `name` and `score` directly inside curly braces, without manual `+` concatenation or `str()` conversion.",
        "medium", "apply", "input-and-output",
        "`message = f'Hello, {name}! Your score is {score}.'`",
        ["`message = f'Hello, name! Your score is score.'`", "`message = 'Hello, {name}! Your score is {score}.'`", "`message = f'Hello, ' + {name} + '! Your score is ' + {score}`"],
    ),
    # --- Fill in the blank (2) ---
    (
        "A geometry app calculates the area of a square with side length 6.\n\n```python\nside = 6\narea = side ______ 2\n```\n\nWhich operator correctly replaces the blank so `area` becomes 36?",
        "`**` is Python's exponentiation operator, so `side ** 2` computes 6 squared, which is 36.",
        "easy", "apply", "arithmetic-operators",
        "**",
        ["*", "//", "%"],
    ),
    (
        "A club-membership app needs to flip a guest's membership status to decide whether to show a 'join now' banner.\n\n```python\nis_member = False\nshow_banner = ______ is_member\n```\n\nWhich keyword correctly replaces the blank so `show_banner` becomes `True` for a non-member?",
        "`not` flips a boolean, so `not False` evaluates to `True`.",
        "easy", "apply", "comparison-and-logical-operators",
        "not",
        ["and", "or", "is"],
    ),
    # --- Code-to-requirement matching (2) ---
    (
        "A developer writes this code to check if a number is even:\n\n```python\nnumber = 8\n\nif number % 2 == 0:\n    result = 'Even'\nelse:\n    result = 'Odd'\n```\n\nDoes this code correctly identify whether `number` is even?",
        "`%` gives the remainder after division by 2. A number is even exactly when that remainder is 0, so this check is correct.",
        "medium", "apply", "arithmetic-operators",
        "Yes — `number % 2 == 0` is True only when the number divides evenly by 2",
        ["No — it should check `number % 2 == 1` instead", "No — `%` only works with two whole numbers written directly in code", "No — this code will always print 'Odd'"],
    ),
    (
        "A developer writes this code intending to safely handle any typed input before converting it to a number:\n\n```python\nage_text = '25'\n\nif age_text.isdigit():\n    age = int(age_text)\nelse:\n    age = 0\n```\n\nDoes this code correctly avoid a crash when given non-numeric input?",
        "`isdigit()` confirms the text is purely numeric before `int()` is ever called, so non-numeric text falls into the safe `else` branch instead of crashing.",
        "medium", "apply", "type-conversion",
        "Yes — `isdigit()` confirms the text is safe to convert before `int()` is called",
        ["No — `isdigit()` cannot be used before `int()`", "No — this code always crashes on any input", "Yes — but only for negative numbers"],
    ),
    # --- Requirement-to-code selection (2) ---
    (
        "Which code correctly converts a Celsius temperature stored in `celsius` to Fahrenheit, using the formula F = C times 9/5, plus 32?",
        "Following the formula exactly: multiply `celsius` by `9 / 5` first, then add 32.",
        "medium", "apply", "arithmetic-operators",
        "`fahrenheit = celsius * 9 / 5 + 32`",
        ["`fahrenheit = celsius * (9 / 5 + 32)`", "`fahrenheit = celsius + 9 / 5 * 32`", "`fahrenheit = (celsius * 9) / (5 + 32)`"],
    ),
    (
        "A store wants to round a computed price to exactly 2 decimal places for display, without changing the stored value. Which code correctly does this?",
        "An f-string with `:.2f` formats the value for display with 2 decimal places, leaving the original `price` variable untouched.",
        "medium", "understand", "input-and-output",
        "`display = f'{price:.2f}'`",
        ["`price = int(price)`", "`display = price[:2]`", "`price = round(price)`"],
    ),
]

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"python - {set_label}",
            "subjects": "python",
            "topics": "data-types-and-operators",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "Python - MCQ - 2.1")
rows2 = build_rows(SET2, "Set 2", "Python - MCQ - 2.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Python - MCQ - Unit 2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/Unit 2 - Data Types and Operators/Unit 2 - Data Types and Operators - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")

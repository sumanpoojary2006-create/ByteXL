# Unit 7: Sets and Dictionaries - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 7 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, data modelling, operation selection, repair analysis, and practical reporting
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option
- Opening coverage: Questions 1–10 collectively represent all seven Unit 7 taxonomy subtopics
- Metadata: every question identifies its taxonomy and primary assessment behaviour

---

## Questions

### 1. Repeated wristband scans count once

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `sets`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based deduplication trace; final value identification

A gate log contains `['A101', 'A102', 'A101', 'A103', 'A102']`. Tara converts it with `set(scans)` and counts the result. Which attendance total reaches the report?

A. `5`  
B. `2`  
C. `4`  
D. `3`

### 2. Removing returning guests from a combined attendance set

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `set-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple set operations

A festival report starts with everyone seen on either day and must then remove those who attended both days:

```python
day1 = {"A1", "A2", "A3"}
day2 = {"A3", "A4"}
combined = day1 | day2
returning = day1 & day2
result = combined - returning
```

Which set reaches the report?

A. `{"A3"}`  
B. `{"A1", "A2", "A4"}`  
C. `{"A1", "A2", "A3", "A4"}`  
D. `set()`

### 3. A repeated key replaces its earlier value

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected duplicate-key behaviour

A ticket desk creates a dictionary from these entries:

```python
prices = {"Adult": 500, "Child": 250, "Adult": 450}
```

Which audit note correctly records the resulting mapping?

A. The dictionary has two entries, and `prices["Adult"]` is `450`  
B. The dictionary has three entries because repeated keys are counted separately  
C. `prices["Adult"]` is `[500, 450]`  
D. Python rejects the dictionary before assigning it

### 4. Completing a guard before direct dictionary access

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing validation condition

A merchandise screen may receive a product name that is not a key in `prices`. Complete the guard so direct lookup occurs only for an existing key:

```python
if __________________:
    amount = prices[item]
else:
    amount = "Unavailable"
```

Which condition prevents `KeyError` while preserving valid lookups?

A. `item in prices.values()`  
B. `prices[item]`  
C. `item in prices`  
D. `item not in prices`

### 5. Selecting data that exposes reversed comprehension keys

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes a data-loss defect

A report should map each item name to its price, but a developer accidentally reverses the pair:

```python
reversed_lookup = {price: item for item, price in prices.items()}
```

Which input most clearly exposes data loss caused by two items becoming the same dictionary key?

A. `{"Mug": 100, "Cap": 100}`  
B. `{"Mug": 100}`  
C. `{}`  
D. `{"Mug": 100, "Cap": 200}`

### 6. Reading a price through two named levels

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a nested dictionary lookup

A festival stores prices inside named stalls:

```python
fest = {
    "Food": {"Tea": 20, "Samosa": 30},
    "Merch": {"Mug": 150}
}
```

Which expression retrieves the mug price without confusing the outer and inner keys?

A. `fest["Mug"]["Merch"]`  
B. `fest["Merch", "Mug"]`  
C. `fest["Food"]["Mug"]`  
D. `fest["Merch"]["Mug"]`

### 7. Choosing a structure for unique IDs with attached scores

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate data structure

A teacher needs one score for each student ID, fast lookup by ID, and no duplicate ID entries. Which structure directly models that requirement?

A. A list of scores with the student IDs stored only in comments  
B. A set containing IDs and scores as unrelated individual values  
C. A dictionary mapping each student ID to its score  
D. A tuple containing every ID followed by every score

### 8. Starting a genuinely empty set

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `sets`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected empty-braces behaviour

A scanner needs an empty collection of unique IDs. Which initialisation creates a set rather than an empty dictionary?

A. `seen = {}`, because empty braces create an empty set  
B. `seen = set()`  
C. `seen = []`  
D. `seen = ()`

### 9. An empty price table follows its fallback branch

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about dictionary truthiness; final value tracing

A newly opened stall has no recorded prices yet:

```python
prices = {}

if prices:
    status = "Ready for sales"
else:
    status = "No items configured"
```

Which status is stored?

A. `"Ready for sales"`, because the dictionary variable exists  
B. Both statuses, because an empty dictionary is still a dictionary  
C. A `TypeError`, because dictionaries cannot be conditions  
D. `"No items configured"`, because an empty dictionary is falsy

### 10. Rebuilding symmetric difference from two operations

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `set-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

A reviewer replaces `day1 ^ day2` with a longer expression for teaching purposes. Which expression is equivalent for all two-set inputs?

A. `(day1 | day2) - (day1 & day2)`  
B. `(day1 & day2) - (day1 | day2)`  
C. `(day1 - day2) & (day2 - day1)`  
D. `(day1 | day2) & (day1 & day2)`

### 11. Looking up a mug price by name

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a direct key lookup

A stall stores `prices = {'T-shirt': 350, 'Mug': 150}`. Which expression retrieves the mug price directly?

A. `prices[1]`  
B. `prices['150']`  
C. `prices['Mug']`  
D. `prices.Mug`

### 12. One key is entered twice

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting duplicate-key overwrite behaviour

A price dictionary is created as `{'Badge': 50, 'Badge': 40}`. Which value remains paired with `"Badge"`?

A. `[50, 40]`  
B. `40`  
C. `50`  
D. Both entries remain under separate identical keys

### 13. Membership checks the labels, not their prices

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing key membership behaviour

For `prices = {'Mug': 150, 'Badge': 40}`, which membership result is accurate?

A. `'Mug' in prices` is `True`, while `150 in prices` is `False`  
B. Both expressions are `True` because keys and values are searched  
C. Both expressions are `False` until `.keys()` is called  
D. `150 in prices` is `True`, while `'Mug' in prices` is `False`

### 14. A missing merchandise key is requested directly

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Classifying unexpected missing-key behaviour

A screen evaluates `prices['Cap']`, but `"Cap"` was never added. Which failure classification belongs in the support record?

A. `IndexError`, because dictionaries use numeric positions  
B. `ValueError`, because the stored prices are numbers  
C. No failure; bracket lookup returns `None` for absent keys and creates the requested entry automatically  
D. `KeyError`, because direct lookup cannot find the requested key

### 15. Counting entries rather than individual objects

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting dictionary length

A dictionary contains three item-price pairs. Which interpretation of `len(prices)` is correct?

A. It returns 6 by counting each key and each value as separate objects inside the dictionary  
B. It returns 3 because each key-value pair is one dictionary entry  
C. It returns the sum of the three prices  
D. It returns 0 because dictionary length counts only keys whose type is numeric

### 16. Adding a newly arrived cap

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a dictionary insertion operation

The key `"Cap"` is not yet present in `prices`. Which statement adds it with price 200?

A. `prices.add('Cap', 200)`  
B. `prices['Cap'] == 200`  
C. `prices['Cap'] = 200`  
D. `prices.append({'Cap': 200})`

### 17. Revising an existing badge price

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an update operation

`prices['Badge']` currently stores 50. Which statement updates that same entry to 40 without creating a duplicate key?

A. `prices.add('Badge', 40)`  
B. `prices['Badge'] += 50`  
C. `prices.append('Badge', 40)`  
D. `prices['Badge'] = 40`

### 18. Removing an entry and keeping its old value

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a removal-and-return operation

A sold-out mug should disappear from `prices`, but its former price is needed for the sales log. Which operation performs both jobs?

A. `old_price = prices.pop('Mug')`  
B. `old_price = del prices['Mug']`  
C. `old_price = prices.remove('Mug')`  
D. `old_price = prices.get('Mug')`

### 19. A safe fallback for an unavailable product

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a safe missing-key approach

A display must show `"Unavailable"` when a requested item key is absent. Which lookup avoids a crash and supplies that fallback?

A. `prices[item] or 'Unavailable'`  
B. `prices.find(item, 'Unavailable')`  
C. `prices.get(item, 'Unavailable')`  
D. `prices.index(item, 'Unavailable')`

### 20. Removing a key that may already be gone

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a guarded deletion approach

A sequential cleanup job must delete `item` only when it exists and must not fail if an earlier cleanup step already removed it. Which taught approach is safest?

A. Always execute `del prices[item]` twice  
B. Check `if item in prices:` before executing `del prices[item]`  
C. Read `prices[item]` before deleting, even when it may be absent  
D. Replace the entire dictionary with an empty one

### 21. A direct dictionary loop visits item names

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting direct dictionary iteration

A report uses `for item in prices:`. Which values does `item` receive?

A. The dictionary's keys  
B. The dictionary's values  
C. Two-item lists containing key and value  
D. Numeric positions starting at zero

### 22. Totalling every stored price

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting value-only iteration

A treasurer needs only the numeric prices and not their item names. Which iteration source best matches that calculation?

A. `prices.keys()`  
B. `prices.items()` with one loop variable  
C. `prices.values()`  
D. `range(prices)`

### 23. Printing each merchandise pair

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting key-value pair iteration

A report needs item and price together on every pass. Which loop header supplies both directly?

A. `for item in prices.values():`  
B. `for item, price in prices.items():`  
C. `for price in prices.keys():`  
D. `for item, price in prices.values():`

### 24. Producing an alphabetic item report

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a non-mutating sorted iteration source

A dictionary retains insertion order, but the treasurer wants an alphabetically sorted report of item-price pairs. Which loop source meets that display requirement without rewriting the dictionary?

A. `prices.values()`  
B. `reversed(prices)`  
C. `prices.items().sort()`, which sorts the item view in place  
D. `sorted(prices.items())`

### 25. Avoiding a repeated lookup inside the report loop

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-operations`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing iteration implementations

Version A loops over keys and repeatedly looks up `prices[item]`. Version B should receive each key and value together. Which header makes Version B direct and readable?

A. `for price in prices:`  
B. `for item in prices.values():`  
C. `for item, price in prices.items():`  
D. `for item, price in prices.keys():`, which returns each stored key together with its associated price

### 26. Applying a closing discount to every item

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a value-transformation comprehension

A sale needs a new dictionary with the same keys and every price multiplied by 0.8. Which comprehension fits?

A. `{item: price * 0.8 for item, price in prices.items()}`  
B. `{item: price for item, price in prices.items()}`  
C. `{price: item for item, price in prices.items()}`  
D. `{item: price * 0.8 for item, price in prices.items() if price < 0}`

### 27. Showing only safe items still in stock

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple comprehension conditions

`stock` maps item names to quantities, and `recalled` is a set of unsafe item names. Which comprehension keeps only entries whose quantity is greater than zero **and** whose item is not recalled?

A. `{item: qty > 0 and item not in recalled for item, qty in stock.items()}`  
B. `{item: qty for item, qty in stock.items() if qty > 0 or item not in recalled}`  
C. `{qty: item for item, qty in stock.items() if qty > 0 and item not in recalled}`  
D. `{item: qty for item, qty in stock.items() if qty > 0 and item not in recalled}`

### 28. Pairing student names with seat numbers

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a `zip`-based mapping comprehension

Two equal-length lists store `names` and `seats`. Which comprehension turns corresponding positions into a lookup dictionary?

A. `{name: seat for name in names for seat in seats}`  
B. `{name: seat for name, seat in zip(names, seats)}`  
C. `{seat: name for name, seat in zip(names, seats)}`  
D. `{name: seat for name, seat in zip(names, seats) if seat is None}`

### 29. Keys and values are accidentally reversed

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting and repairing a reversed-mapping bug

A comprehension should map each item to its discounted price, but the result maps prices to item names. Which expression has the intended direction?

A. `{item: price * 0.8 for item, price in prices.items()}`  
B. `{price * 0.8: item for item, price in prices.items()}`  
C. `{item for price in prices.values()}`  
D. `{price: item for item, price in prices.items()}`

### 30. A comprehension contains logging and several decisions

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `dictionary-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a maintainable implementation structure

A proposed dictionary comprehension validates stock, prints a warning, updates a counter, applies tax, and rounds a price in one expression. Which review action best protects readability?

A. Add more nested expressions until validation, warnings, counting, taxation, and rounding all fit inside the same braces  
B. Remove the warning because comprehensions cannot build dictionaries  
C. Replace it with a regular loop that gives each decision and side effect a clear step  
D. Shorten every variable name to make the expression look smaller

### 31. Finding one food-stall price

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a nested lookup path

A nested dictionary contains:

```python
fest = {
    'Food': {'Samosa': 30, 'Tea': 20},
    'Merch': {'Mug': 150}
}
```

Which lookup retrieves the samosa price?

A. `fest['Samosa']['Food']`  
B. `fest['Food']['Samosa']`  
C. `fest['Food', 'Samosa']`  
D. `fest[0][0]`

### 32. Updating only the tea price

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a precise nested update

Using the same structure, which statement changes Tea to 25 without replacing another stall or item?

A. `fest['Tea'] = 25`  
B. `fest['Food'] = 25`  
C. `fest['Food']['Samosa'] = 25`  
D. `fest['Food']['Tea'] = 25`

### 33. Adding an entire games stall

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a new nested branch

The organiser wants a new outer key `"Games"` containing `{"Bowling": 50}`. Which statement adds the full inner dictionary?

A. `fest['Games']['Bowling'] = 50` before `Games` exists  
B. `fest.append({'Games': {'Bowling': 50}})`  
C. `fest['Games'] = {'Bowling': 50}`  
D. `fest['Bowling'] = 'Games'`

### 34. Walking through every stall and item

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting iteration that mirrors nested structure

A combined report needs each stall name and every item-price pair inside it. Which loop design mirrors the nested structure?

A. One loop over `fest.values()` that prints each entire inner dictionary once and treats the nested values as a finished report  
B. An outer loop over `fest.items()` and an inner loop over each `items.items()`  
C. One loop over numeric positions in the dictionary  
D. Two unrelated loops that never connect a stall to its items

### 35. A missing stall and item need a safe fallback

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `nested-dictionaries`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a safe nested lookup approach

A query may request a stall that does not exist. Which expression returns `"Unavailable"` without directly indexing a missing outer key?

A. `fest.get(stall, {}).get(item, 'Unavailable')`  
B. `fest[stall][item] or 'Unavailable'`, because a failed outer lookup produces an empty value that activates the fallback  
C. `fest.get(stall)[item]`  
D. `fest[item].get(stall)`

### 36. Tracking only whether an assignment was submitted

**Difficulty:** Foundational

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a structure for uniqueness and membership

A teacher needs unique student IDs and fast yes-or-no membership checks, with no score attached. Which structure is the best fit?

A. List  
B. Tuple  
C. Dictionary  
D. Set

### 37. Looking up each student's score

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a keyed lookup structure

The requirement changes: every student ID now needs an attached numeric score retrieved by ID. Which structure fits?

A. Set  
B. Dictionary  
C. Tuple  
D. Plain string

### 38. Protecting one fixed coordinate pair

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a fixed-record structure

A latitude-longitude pair is a fixed related record and should not change. Which structure communicates that intent?

A. Tuple  
B. List  
C. Set  
D. Dictionary

### 39. Maintaining an ordered playlist that changes

**Difficulty:** Intermediate

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a mutable ordered structure

Songs must preserve request order, allow duplicates, and support additions and removals. Which structure belongs in the design?

A. Set  
B. Tuple  
C. Dictionary keyed by position  
D. List

### 40. Modelling several named stalls with named item prices

**Difficulty:** Advanced

**Taxonomy:** `python` → `sets-and-dictionaries` → `choosing-data-structures`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a nested keyed data model

A festival report needs lookup first by stall name and then by item name, with prices at the final level. Which structure matches the two named lookup levels?

A. One flat set of every stall and item name  
B. A tuple containing a list of all prices  
C. A nested dictionary whose outer keys are stalls and inner keys are items  
D. A list whose numeric positions must be memorised separately for every stall, item, and price lookup in the report

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | D | Foundational | Converting to a set retains A101, A102, and A103 once each. |
| 2 | B | Intermediate | The union contains all four IDs, the intersection contains `A3`, and subtracting it leaves `A1`, `A2`, and `A4`. |
| 3 | A | Foundational | Dictionary keys are unique, so the later `"Adult": 450` entry replaces the earlier value and only two keys remain. |
| 4 | C | Intermediate | Direct dictionary membership checks keys, and the guarded bracket lookup runs only when `item` exists. |
| 5 | A | Advanced | Reversing two equal prices creates the same numeric key twice, so the later item overwrites the earlier one and exposes data loss. |
| 6 | D | Foundational | The first key selects the Merch dictionary, and the second key retrieves its Mug value of 150. |
| 7 | C | Intermediate | A dictionary provides one unique student key with an attached score value and direct lookup by ID. |
| 8 | B | Intermediate | Empty braces create a dictionary; `set()` is the empty-set constructor. |
| 9 | D | Intermediate | An empty dictionary is falsy, so the `else` branch assigns `"No items configured"`. |
| 10 | A | Advanced | Removing the intersection from the union leaves values present in exactly one set. |
| 11 | C | Foundational | Dictionary lookup uses the meaningful key `"Mug"`, not a numeric position. |
| 12 | B | Intermediate | Dictionary keys are unique, so the later value 40 overwrites 50. |
| 13 | A | Intermediate | Dictionary membership tests keys; 150 is a value, not a key. |
| 14 | D | Advanced | Bracket lookup raises `KeyError` when the supplied key is absent. |
| 15 | B | Advanced | Dictionary length is the number of entries, with each pair counted once. |
| 16 | C | Foundational | Assignment to an absent key creates a new entry. |
| 17 | D | Intermediate | Assignment to a present key replaces its associated value. |
| 18 | A | Intermediate | `pop` removes the key-value pair and returns the removed value. |
| 19 | C | Intermediate | `get` safely returns the chosen fallback when the key is missing. |
| 20 | B | Advanced | The membership guard prevents `del` from targeting an absent key. |
| 21 | A | Foundational | Direct dictionary iteration yields keys. |
| 22 | C | Intermediate | `.values()` supplies only the numeric values needed for the total. |
| 23 | B | Foundational | `.items()` yields key-value pairs that unpack into two loop variables. |
| 24 | D | Intermediate | `sorted(prices.items())` creates a sorted sequence of pairs without mutating the dictionary. |
| 25 | C | Advanced | `.items()` supplies both parts directly and avoids a second key lookup. |
| 26 | A | Foundational | The comprehension retains each key and transforms its paired price. |
| 27 | D | Intermediate | The pair expression preserves the mapping, while `and` requires both positive stock and absence from the recalled set. |
| 28 | B | Intermediate | `zip` supplies corresponding name-seat pairs for the comprehension. |
| 29 | A | Intermediate | The item remains the key and the discounted price becomes its value. |
| 30 | C | Advanced | Several decisions and side effects are clearer as explicit regular-loop steps. |
| 31 | B | Foundational | The first key selects the Food dictionary and the second selects Samosa. |
| 32 | D | Intermediate | Two successive key lookups target only the Tea value inside Food. |
| 33 | C | Intermediate | Assigning a dictionary value to a new outer key adds the complete stall. |
| 34 | B | Advanced | The outer pair supplies a stall and its inner dictionary; the inner pair supplies item and price. |
| 35 | A | Advanced | A missing stall falls back to an empty dictionary, whose second `get` safely returns the message. |
| 36 | D | Foundational | A set provides uniqueness and fast membership without attached details. |
| 37 | B | Intermediate | A dictionary attaches one score value to each meaningful student key. |
| 38 | A | Intermediate | A tuple represents a fixed, related group and prevents item mutation. |
| 39 | D | Intermediate | A list preserves order and duplicates while remaining mutable. |
| 40 | C | Advanced | The nested dictionary mirrors the required stall-then-item lookup path. |

## Taxonomy coverage

| Unit 7 taxonomy subtopic | Question numbers |
|---|---|
| `sets` | 1, 8 |
| `set-operations` | 2, 10 |
| `dictionaries` | 3, 9, 11–15 |
| `dictionary-operations` | 4, 16–25 |
| `dictionary-comprehensions` | 5, 26–30 |
| `nested-dictionaries` | 6, 31–35 |
| `choosing-data-structures` | 7, 36–40 |

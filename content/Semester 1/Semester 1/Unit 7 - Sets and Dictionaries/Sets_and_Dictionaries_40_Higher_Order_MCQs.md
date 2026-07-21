# Unit 7: Sets and Dictionaries - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 7 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, data modelling, operation selection, repair analysis, and practical reporting
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option

---

## Questions

### 1. Repeated wristband scans count once

**Difficulty:** Foundational

A gate log contains `['A101', 'A102', 'A101', 'A103', 'A102']`. Tara converts it with `set(scans)` and counts the result. Which attendance total reaches the report?

A. `5`  
B. `2`  
C. `4`  
D. `3`

### 2. Starting a genuinely empty set

**Difficulty:** Intermediate

A scanner needs an empty collection of unique IDs. Which initialisation creates a set rather than an empty dictionary?

A. `seen = {}`, because empty braces create an empty set  
B. `seen = set()`  
C. `seen = []`  
D. `seen = ()`

### 3. Presence matters, position does not

**Difficulty:** Foundational

A submission tracker only needs to answer whether an ID has appeared before. It never needs a first or last ID. Which collection behavior fits that requirement?

A. Use set membership and avoid positional indexing  
B. Use a set and read the earliest ID with `[0]`  
C. Use a list because it automatically removes duplicates  
D. Use a tuple and append each new submission

### 4. Deduplicating a noisy city list

**Difficulty:** Intermediate

A survey receives `['Pune', 'Pune', 'Nashik', 'Surat', 'Nashik']`. Which expression gives the number of distinct cities?

A. `len(cities)`  
B. `cities.count()`  
C. `len(set(cities))`  
D. `set(len(cities))`

### 5. Unique attendance must still retain arrival order

**Difficulty:** Advanced

A ceremony needs both the number of unique guests and the order in which each guest first arrived. A developer stores only one set. Which redesign preserves both requirements?

A. Keep an ordered list for first arrivals and a set for fast seen-before checks  
B. Index the set after every scan to recover arrival order, because sets retain each ID's first insertion position  
C. Sort the set and treat alphabetical order as arrival order  
D. Store every scan in one set, including intentional duplicates

### 6. Everyone who attended either fest day

**Difficulty:** Foundational

Day 1 IDs are `{'A1', 'A2', 'A3'}` and Day 2 IDs are `{'A3', 'A4'}`. Which operation produces every distinct attendee across both days?

A. `day1 & day2`  
B. `day1 - day2`  
C. `day1 ^ day2`  
D. `day1 | day2`

### 7. Guests present on both days

**Difficulty:** Intermediate

Using the same two sets, the organiser needs only returning guests. Which expression isolates the overlap?

A. `day1 | day2`  
B. `day2 - day1`  
C. `day1 & day2`  
D. `day1 ^ day2`

### 8. Guests who came only on Day 1

**Difficulty:** Intermediate

The coordinator needs IDs present in `day1` but absent from `day2`. Which operation respects that direction?

A. `day2 - day1`  
B. `day1 - day2`  
C. `day1 & day2`  
D. `day1 | day2`

### 9. Attendees who came on exactly one day

**Difficulty:** Intermediate

The report should include IDs from either day but exclude those present on both. Which expression matches the policy?

A. `day1 & day2`  
B. `day1 | day2`  
C. `day1 - day2`  
D. `day1 ^ day2`

### 10. Rebuilding symmetric difference from two operations

**Difficulty:** Advanced

A reviewer replaces `day1 ^ day2` with a longer expression for teaching purposes. Which expression is equivalent for all two-set inputs?

A. `(day1 | day2) - (day1 & day2)`  
B. `(day1 & day2) - (day1 | day2)`  
C. `(day1 - day2) & (day2 - day1)`  
D. `(day1 | day2) & (day1 & day2)`

### 11. Looking up a mug price by name

**Difficulty:** Foundational

A stall stores `prices = {'T-shirt': 350, 'Mug': 150}`. Which expression retrieves the mug price directly?

A. `prices[1]`  
B. `prices['150']`  
C. `prices['Mug']`  
D. `prices.Mug`

### 12. One key is entered twice

**Difficulty:** Intermediate

A price dictionary is created as `{'Badge': 50, 'Badge': 40}`. Which value remains paired with `"Badge"`?

A. `[50, 40]`  
B. `40`  
C. `50`  
D. Both entries remain under separate identical keys

### 13. Membership checks the labels, not their prices

**Difficulty:** Intermediate

For `prices = {'Mug': 150, 'Badge': 40}`, which membership result is accurate?

A. `'Mug' in prices` is `True`, while `150 in prices` is `False`  
B. Both expressions are `True` because keys and values are searched  
C. Both expressions are `False` until `.keys()` is called  
D. `150 in prices` is `True`, while `'Mug' in prices` is `False`

### 14. A missing merchandise key is requested directly

**Difficulty:** Advanced

A screen evaluates `prices['Cap']`, but `"Cap"` was never added. Which failure classification belongs in the support record?

A. `IndexError`, because dictionaries use numeric positions  
B. `ValueError`, because the stored prices are numbers  
C. No failure; bracket lookup returns `None` for absent keys and creates the requested entry automatically  
D. `KeyError`, because direct lookup cannot find the requested key

### 15. Counting entries rather than individual objects

**Difficulty:** Advanced

A dictionary contains three item-price pairs. Which interpretation of `len(prices)` is correct?

A. It returns 6 by counting each key and each value as separate objects inside the dictionary  
B. It returns 3 because each key-value pair is one dictionary entry  
C. It returns the sum of the three prices  
D. It returns only the number of numeric values

### 16. Adding a newly arrived cap

**Difficulty:** Foundational

The key `"Cap"` is not yet present in `prices`. Which statement adds it with price 200?

A. `prices.add('Cap', 200)`  
B. `prices['Cap'] == 200`  
C. `prices['Cap'] = 200`  
D. `prices.append({'Cap': 200})`

### 17. Revising an existing badge price

**Difficulty:** Intermediate

`prices['Badge']` currently stores 50. Which statement updates that same entry to 40 without creating a duplicate key?

A. `prices.add('Badge', 40)`  
B. `prices['Badge'] += 50`  
C. `prices.append('Badge', 40)`  
D. `prices['Badge'] = 40`

### 18. Removing an entry and keeping its old value

**Difficulty:** Intermediate

A sold-out mug should disappear from `prices`, but its former price is needed for the sales log. Which operation performs both jobs?

A. `old_price = prices.pop('Mug')`  
B. `old_price = del prices['Mug']`  
C. `old_price = prices.remove('Mug')`  
D. `old_price = prices.get('Mug')`

### 19. A safe fallback for an unavailable product

**Difficulty:** Intermediate

A display must show `"Unavailable"` when a requested item key is absent. Which lookup avoids a crash and supplies that fallback?

A. `prices[item] or 'Unavailable'`  
B. `prices.find(item, 'Unavailable')`  
C. `prices.get(item, 'Unavailable')`  
D. `prices.index(item, 'Unavailable')`

### 20. Removing a key that may already be gone

**Difficulty:** Advanced

A cleanup job must delete `item` only when it exists and must not fail if another process removed it first. Which taught approach is safest?

A. Always execute `del prices[item]` twice  
B. Check `if item in prices:` before executing `del prices[item]`  
C. Read `prices[item]` before deleting, even when it may be absent  
D. Replace the entire dictionary with an empty one

### 21. A direct dictionary loop visits item names

**Difficulty:** Foundational

A report uses `for item in prices:`. Which values does `item` receive?

A. The dictionary's keys  
B. The dictionary's values  
C. Two-item lists containing key and value  
D. Numeric positions starting at zero

### 22. Totalling every stored price

**Difficulty:** Intermediate

A treasurer needs only the numeric prices and not their item names. Which iteration source best matches that calculation?

A. `prices.keys()`  
B. `prices.items()` with one loop variable  
C. `prices.values()`  
D. `range(prices)`

### 23. Printing each merchandise pair

**Difficulty:** Foundational

A report needs item and price together on every pass. Which loop header supplies both directly?

A. `for item in prices.values():`  
B. `for item, price in prices.items():`  
C. `for price in prices.keys():`  
D. `for item, price in prices.values():`

### 24. Producing an alphabetic item report

**Difficulty:** Intermediate

A dictionary retains insertion order, but the treasurer wants an alphabetically sorted report of item-price pairs. Which loop source meets that display requirement without rewriting the dictionary?

A. `prices.values()`  
B. `reversed(prices)`  
C. `prices.items().sort()`, which sorts the item view in place  
D. `sorted(prices.items())`

### 25. Avoiding a repeated lookup inside the report loop

**Difficulty:** Advanced

Version A loops over keys and repeatedly looks up `prices[item]`. Version B should receive each key and value together. Which header makes Version B direct and readable?

A. `for price in prices:`  
B. `for item in prices.values():`  
C. `for item, price in prices.items():`  
D. `for item, price in prices.keys():`, which returns each stored key together with its associated price

### 26. Applying a closing discount to every item

**Difficulty:** Foundational

A sale needs a new dictionary with the same keys and every price multiplied by 0.8. Which comprehension fits?

A. `{item: price * 0.8 for item, price in prices.items()}`  
B. `[item: price * 0.8 for item, price in prices]`  
C. `{price: item for item in prices.values()}`  
D. `{item for item, price in prices.items() if price * 0.8}`

### 27. Showing only items still in stock

**Difficulty:** Intermediate

`stock` maps item names to quantities. Which comprehension keeps only entries whose quantity is greater than zero?

A. `{item: qty > 0 for item, qty in stock.items()}`, which retains every item and stores its availability test  
B. `{qty: item for item, qty in stock.items()}`  
C. `[item for item, qty in stock.items() if qty > 0]`  
D. `{item: qty for item, qty in stock.items() if qty > 0}`

### 28. Pairing student names with seat numbers

**Difficulty:** Intermediate

Two equal-length lists store `names` and `seats`. Which comprehension turns corresponding positions into a lookup dictionary?

A. `{name: seat for name in names for seat in seats}`  
B. `{name: seat for name, seat in zip(names, seats)}`  
C. `{names: seats for name, seat in zip(names, seats)}`  
D. `[name, seat for name, seat in zip(names, seats)]`

### 29. Keys and values are accidentally reversed

**Difficulty:** Intermediate

A comprehension should map each item to its discounted price, but the result maps prices to item names. Which expression has the intended direction?

A. `{item: price * 0.8 for item, price in prices.items()}`  
B. `{price * 0.8: item for item, price in prices.items()}`  
C. `{item for price in prices.values()}`  
D. `{price: item for item, price in prices.items()}`

### 30. A comprehension contains logging and several decisions

**Difficulty:** Advanced

A proposed dictionary comprehension validates stock, prints a warning, updates a counter, applies tax, and rounds a price in one expression. Which review action best protects readability?

A. Add more nested expressions until validation, warnings, counting, taxation, and rounding all fit inside the same braces  
B. Remove the warning because comprehensions cannot build dictionaries  
C. Replace it with a regular loop that gives each decision and side effect a clear step  
D. Shorten every variable name to make the expression look smaller

### 31. Finding one food-stall price

**Difficulty:** Foundational

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

Using the same structure, which statement changes Tea to 25 without replacing another stall or item?

A. `fest['Tea'] = 25`  
B. `fest['Food'] = 25`  
C. `fest['Food']['Samosa'] = 25`  
D. `fest['Food']['Tea'] = 25`

### 33. Adding an entire games stall

**Difficulty:** Intermediate

The organiser wants a new outer key `"Games"` containing `{"Bowling": 50}`. Which statement adds the full inner dictionary?

A. `fest['Games']['Bowling'] = 50` before `Games` exists  
B. `fest.append({'Games': {'Bowling': 50}})`  
C. `fest['Games'] = {'Bowling': 50}`  
D. `fest['Bowling'] = 'Games'`

### 34. Walking through every stall and item

**Difficulty:** Advanced

A combined report needs each stall name and every item-price pair inside it. Which loop design mirrors the nested structure?

A. One loop over `fest.values()` that prints each entire inner dictionary once and treats the nested values as a finished report  
B. An outer loop over `fest.items()` and an inner loop over each `items.items()`  
C. One loop over numeric positions in the dictionary  
D. Two unrelated loops that never connect a stall to its items

### 35. A missing stall and item need a safe fallback

**Difficulty:** Advanced

A query may request a stall that does not exist. Which expression returns `"Unavailable"` without directly indexing a missing outer key?

A. `fest.get(stall, {}).get(item, 'Unavailable')`  
B. `fest[stall][item] or 'Unavailable'`, because a failed outer lookup produces an empty value that activates the fallback  
C. `fest.get(stall)[item]`  
D. `fest[item].get(stall)`

### 36. Tracking only whether an assignment was submitted

**Difficulty:** Foundational

A teacher needs unique student IDs and fast yes-or-no membership checks, with no score attached. Which structure is the best fit?

A. List  
B. Tuple  
C. Dictionary  
D. Set

### 37. Looking up each student's score

**Difficulty:** Intermediate

The requirement changes: every student ID now needs an attached numeric score retrieved by ID. Which structure fits?

A. Set  
B. Dictionary  
C. Tuple  
D. Plain string

### 38. Protecting one fixed coordinate pair

**Difficulty:** Intermediate

A latitude-longitude pair is a fixed related record and should not change. Which structure communicates that intent?

A. Tuple  
B. List  
C. Set  
D. Dictionary

### 39. Maintaining an ordered playlist that changes

**Difficulty:** Intermediate

Songs must preserve request order, allow duplicates, and support additions and removals. Which structure belongs in the design?

A. Set  
B. Tuple  
C. Dictionary keyed by position  
D. List

### 40. Modelling several named stalls with named item prices

**Difficulty:** Advanced

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
| 2 | B | Intermediate | Empty braces create a dictionary; `set()` is the empty-set constructor. |
| 3 | A | Foundational | Sets are designed around uniqueness and membership, not position. |
| 4 | C | Intermediate | The set removes repeated city values, and `len` counts the three survivors. |
| 5 | A | Advanced | The set handles fast uniqueness checks, while the list preserves first-arrival order. |
| 6 | D | Foundational | Union includes every value present in either input and removes overlap duplicates. |
| 7 | C | Intermediate | Intersection keeps only values that occur in both sets. |
| 8 | B | Intermediate | Difference reads left to right, retaining Day 1 values not covered by Day 2. |
| 9 | D | Intermediate | Symmetric difference retains values from exactly one input set. |
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
| 27 | D | Intermediate | The pair expression preserves the mapping, while the condition filters zero stock. |
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

## Topic coverage

| Unit 7 topic | Question numbers |
|---|---|
| Set uniqueness and creation | 1–5 |
| Set operations | 6–10 |
| Dictionary key-value pairs | 11–15 |
| Accessing, adding, updating, and removing items | 16–20 |
| Iterating dictionaries | 21–25 |
| Dictionary comprehensions | 26–30 |
| Nested dictionaries | 31–35 |
| Choosing the right data structure | 36–40 |

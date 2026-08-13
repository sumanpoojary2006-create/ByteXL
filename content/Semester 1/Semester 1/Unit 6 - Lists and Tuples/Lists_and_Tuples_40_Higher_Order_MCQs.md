# Unit 6: Lists and Tuples - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 6 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, repair selection, implementation comparison, and practical data modelling
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option
- Opening coverage: Questions 1–10 collectively represent all seven Unit 6 taxonomy subtopics
- Metadata: every question identifies its taxonomy and primary assessment behaviour

---

## Questions

### 1. One trip record holds different kinds of values

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an appropriate collection representation

A trip summary is stored as:

```python
trip = ["Pune", 3, 4500.0, True]
```

Which audit note accurately describes the collection?

A. It is a tuple because it contains four values  
B. It is invalid because every item in a Python list must use the same data type  
C. It is a four-item list that preserves the written order  
D. It is a string because the first item contains text

### 2. Tracing removal by value and then by position

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based mutation trace; final value identification

A queue contains a repeated request and applies two different removal methods:

```python
requests = ["Tea", "Coffee", "Tea"]
requests.remove("Tea")
served = requests.pop(0)
```

Which audit state correctly records both the returned value and the remaining list?

A. `served == "Coffee"` and `requests == ["Tea"]`  
B. `served == "Tea"` and `requests == ["Coffee"]`  
C. `served is None` and `requests == ["Coffee", "Tea"]`  
D. `served == "Coffee"` and `requests == []`

### 3. Completing a filtered square comprehension

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing transformation and filter code

A report needs the square of each positive value in `numbers`, while zero and negative values must be omitted:

```python
squares = [____________________________]
```

Which completion performs both the transformation and the filter?

A. `number for number in numbers if number < 0`  
B. `number > 0 for number in numbers`  
C. `number ** 2 for number in numbers`  
D. `number ** 2 for number in numbers if number > 0`

### 4. A tuple contains a list that can still change

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected mutability behaviour

A trip record contains a mutable stop list inside a tuple:

```python
trip = (["Pune"], 2026)
trip[0].append("Nashik")
```

Which review note states the tuple rule precisely?

A. The code fails because every object stored in a tuple becomes immutable  
B. The append succeeds because the tuple still refers to the same inner list; replacing `trip[0]` itself would fail  
C. The append converts `trip` into a list automatically  
D. The year changes to 2027 whenever the inner list changes

### 5. Selecting the record that exposes an unpacking defect

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `packing-and-unpacking`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes a structural defect

A loader assumes that every student record contains exactly two values:

```python
name, score = record
```

Which proposed record is the smallest input that exposes the assumption by producing too many values to unpack?

A. `("Asha", 90)`  
B. `["Ravi", 82]`  
C. `("Meera",)`  
D. `("Dev", 75, "Pune")`

### 6. Completing a safe lookup in a ragged seating chart

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a safe validation condition; tracing multiple conditions

A seating chart may contain rows of different lengths. Before reading `seating[row][column]`, the program must validate both positions:

```python
if ______________________________________________:
    seat = seating[row][column]
else:
    seat = "Invalid position"
```

Which condition checks the selected row before using that row's actual length for the column check?

A. `row < len(seating) or column < len(seating[row])`  
B. `0 <= column < len(seating) and 0 <= row < len(seating[column])`  
C. `0 <= row < len(seating) and 0 <= column < len(seating[row])`  
D. `row in seating and column in seating`

### 7. Comparing direct and index-based sequence iteration

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

Two versions build uppercase copies of every stored name.

Version A:

```python
result = []
for name in names:
    result.append(name.upper())
```

Version B:

```python
result = []
for index in range(len(names)):
    result.append(names[index].upper())
```

Assume `names` is a list of strings. Which comparison is correct?

A. The versions produce the same `result` for every such list, although Version A avoids unnecessary index handling  
B. Version B skips the final name because `range(len(names))` excludes the list length  
C. Version A changes `names` in place, while Version B does not  
D. The versions differ whenever `names` is empty

### 8. Choosing data that reveals aliasing instead of copying

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a test that exposes an aliasing defect

A developer intends to preserve an original list but writes `backup = items`. Which test most clearly reveals that `backup` is an alias rather than an independent copy?

A. Start with `[]` and compare `items == backup` without changing either name  
B. Start with `["A"]`, append `"B"` through `backup`, and observe that `items` also becomes `["A", "B"]`  
C. Start with `["A"]` and read `items[0]`  
D. Start with two separately created lists and compare their lengths

### 9. An empty queue skips its processing branch

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about collection truthiness; final value tracing

A dispatch screen uses collection truthiness to decide whether work is waiting:

```python
tasks = []

if tasks:
    status = "Process next task"
else:
    status = "Queue empty"
```

Which state should the dashboard display?

A. `"Queue empty"`, because an empty list is falsy  
B. `"Process next task"`, because the variable exists  
C. Both messages, because a list can be both empty and valid  
D. A `TypeError`, because lists cannot be used as conditions

### 10. Two names point to one snack list

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an aliasing bug; selecting the smallest correct repair

A coordinator expects an independent official copy:

```python
snacks = ["fruit", "nuts"]
official = snacks
official.append("chips")
```

Both screens now show `"chips"`. Which repair separates future edits?

A. Use `official = snacks.append([])`  
B. Rename `official` without changing the assignment, because a different variable name automatically creates another container  
C. Convert both names to strings before appending  
D. Create it with `official = snacks.copy()` or `list(snacks)`

### 11. Counting repeated song requests

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a counting method

A request list is `['Sky', 'Road', 'Sky', 'Sky']`. Which expression returns the number of `"Sky"` entries?

A. `requests.index("Sky")`  
B. `requests.count("Sky")`  
C. `requests.find("Sky")`  
D. `requests.sort("Sky")`

### 12. Locating the first matching stop

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting first-match search behaviour

A route is `['Pune', 'Nashik', 'Pune']`. The planner uses `route.index('Pune')`. Which position is returned?

A. `2`  
B. `3`  
C. `0`  
D. `[0, 2]`

### 13. Newest additions should play first

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate order mutation

A playlist is already in request order. The newest requests should temporarily become first without alphabetising anything. Which in-place method flips the current order?

A. `playlist.sort(reverse=True)`  
B. `sorted(playlist)`  
C. `playlist.count()`  
D. `playlist.reverse()`

### 14. A sorted playlist becomes `None`

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an in-place-method return-value bug

A developer writes:

```python
playlist = ["Zed", "Asha", "Mira"]
playlist = playlist.sort()
```

Why does the variable no longer hold the songs?

A. Sorting strings is unsupported when names have different lengths, so the operation discards the collection instead of arranging it  
B. `sort()` changes the list in place and returns `None`, which is then assigned to `playlist`  
C. `sort()` returns the first item instead of a collection  
D. Assignment automatically empties any list used on its right side

### 15. Showing an alphabetic preview without disturbing play order

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `list-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a non-mutating implementation

A music app must display songs alphabetically while preserving the original request order for playback. Which plan meets both needs?

A. Call `playlist.sort()` and use the permanently changed list for both display and later playback  
B. Call `playlist.reverse()` before every display  
C. Store `alphabetic = sorted(playlist)` and leave `playlist` unchanged  
D. Assign `alphabetic = playlist.sort()`

### 16. Selecting only the even seat numbers

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct filter comprehension

A bus system has `seats = [1, 2, 3, 4, 5, 6]`. Which comprehension builds `[2, 4, 6]`?

A. `[seat for seat in seats if seat % 2 == 0]`  
B. `[seat % 2 == 0 for seat in seats]`  
C. `[seat for seat in seats if seat % 2 != 0]`  
D. `[seat * 2 for seat in seats if seat % 2 == 0]`

### 17. Applying the same discount to every price

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a transformation comprehension

A sale preview needs a new list containing 90% of every value in `prices`, with no filtering. Which comprehension fits?

A. `[price for price in prices if price == 0.9]`  
B. `[price * 0.9 for price in prices]`  
C. `[price + 0.9 for price in prices]`  
D. `[price * 0.9 for price in prices if price > 0]`

### 18. Filtering and formatting qualifying names

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing combined filtering and transformation

A report should keep names longer than four characters and title-case those retained. Which comprehension performs both operations?

A. `[name for name in names if len(name) > 4]`  
B. `[len(name) > 4 for name in names]`  
C. `[name.title() for name in names if len(name) <= 4]`  
D. `[name.title() for name in names if len(name) > 4]`

### 19. Replacing a loop-and-append filter

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

Version A appends each positive value from `numbers` into a new list. Which Version B is equivalent?

A. `positives = [number for number in numbers if number > 0]`  
B. `positives = [number > 0 for number in numbers]`  
C. `positives = [numbers for number > 0]`  
D. `positives = [number for number in numbers if number < 0]`

### 20. A comprehension hides a multi-step workflow

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `list-comprehensions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most maintainable programming structure

A proposed comprehension validates each record, prints a rejection reason, updates an audit counter, and transforms accepted data in one dense line. Which review decision best supports maintainability?

A. Add another nested comprehension so validation, printing, counter updates, and transformation all remain inside one compact expression  
B. Remove validation because comprehensions cannot include conditions  
C. Use a regular loop because several steps and side effects make the comprehension hard to reason about  
D. Replace every variable name with one letter to shorten the line

### 21. Creating a one-item tuple

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct one-item tuple representation

A coordinate record must be a tuple containing only the value `5`. Which expression creates that one-item tuple?

A. `(5,)`  
B. `(5)`, because parentheses around one value always create a tuple  
C. `tuple(5)`  
D. `(5, 5)`

### 22. Reading one value from a fixed coordinate

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying a tuple element by position

A GPS coordinate is `location = (18.52, 73.85)`. Which expression retrieves the longitude `73.85`?

A. `location[-2]`  
B. `location[0]`  
C. `location[1]`  
D. `location[1:]`

### 23. An accidental coordinate edit is refused

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing tuple-position assignment failure

A navigation tool tries `location[0] = 19.0` where `location` is a tuple. Which design property blocks the operation?

A. Tuple positions can be replaced only when the new value has the same type as the old value  
B. Numeric values may be read from tuples but can be replaced only through slice assignment  
C. Item assignment would work after calling `location.copy()` because copying unlocks a tuple  
D. The tuple itself is immutable, so assigning a new value to `location[0]` is not supported

### 24. Giving names to a packed stop record

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `packing-and-unpacking`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct unpacking structure

A fixed stop is `stop = ('Fort', 18.4, 73.7)`. Which assignment creates the three separate variables `name`, `latitude`, and `longitude` by position?

A. `name, latitude = stop`  
B. `name, latitude, longitude = stop`  
C. `name, *latitude = stop`  
D. `name, latitude, longitude = [stop]`

### 25. Three values enter two variables

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `packing-and-unpacking`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a structural unpacking mismatch

A route import attempts:

```python
place, latitude = ("Fort", 18.4, 73.7)
```

Which review note identifies the mismatch?

A. Tuples can contain no more than two items  
B. Parentheses prevent values from being assigned unless the two target variables are changed to use square brackets  
C. Three packed values cannot unpack into only two target variables  
D. Latitude values must be stored as integers

### 26. A packing checklist changes throughout the day

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a collection for mutable requirements

Items will be added, removed, and reordered until the bus leaves. Which container communicates those needs?

A. A tuple, because its locked contents can be rebuilt as a fresh tuple after every addition or removal  
B. A list, because it supports in-place membership changes  
C. A string containing comma-separated items  
D. A number recording only the item count

### 27. Protecting one fixed GPS pair

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a fixed-record representation

A destination's latitude and longitude form one fixed record that should not be edited after lookup. Which representation best documents that intent?

A. `coordinates = (18.52, 73.85)`  
B. `coordinates = [18.52, 73.85]`  
C. `coordinates = "18.52" + "73.85"`  
D. `coordinates = {18.52, 73.85}`

### 28. A route grows, but each stop remains fixed

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a composite list-and-tuple structure

An itinerary must accept new stops, while every stored stop remains a fixed `(name, latitude, longitude)` record. Which overall shape matches both requirements?

A. One tuple containing every mutable stop list  
B. A string containing all values with commas  
C. A tuple of names and a separate unrelated number  
D. A list whose items are stop tuples

### 29. Making an intent promise to future readers

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `tuples`  
**Is Curriculum Based:** No  
**Assessment type:** Applying immutability to data modelling

A record always consists of a student's roll number and admission year. Neither field should change inside the program. Why is a tuple preferable to a list here?

A. Tuples automatically validate every roll number and prevent an admission year outside the permitted institutional range  
B. The tuple communicates a fixed related record and blocks item-level mutation  
C. Lists cannot hold an integer and a year together  
D. Tuples sort their contents as soon as they are created

### 30. Choosing a tuple only for tiny speed gains

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `lists`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing data-structure trade-offs

A developer selects a tuple for a shopping cart that must frequently add and remove products, arguing that tuples are slightly lighter. Which review response gives the sounder priority?

A. Use a list because required mutation matters more than the small tuple performance difference  
B. Keep the tuple and recreate the entire cart after every small change, because repeated replacement preserves immutability and avoids list methods  
C. Store each product in a separate variable to avoid both containers  
D. Use a tuple because performance always overrides the data's behavior

### 31. Reaching one seat by row and column

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a two-dimensional lookup

A seating chart is:

```python
seating = [
    ["Asha", "Ravi", "Meera"],
    ["Dev", "Isha", "Aman"]
]
```

Which expression retrieves `"Aman"`?

A. `seating[2][3]`  
B. `seating[1]`  
C. `seating[1][2]`  
D. `seating[2][1]`

### 32. Reassigning exactly one nested seat

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a precise nested mutation

Using the same chart, the coordinator must replace `"Ravi"` with `"Kabir"` without changing another seat. Which statement is precise?

A. `seating[1] = "Kabir"`  
B. `seating[1][0] = "Kabir"`  
C. `seating[0] = "Kabir"`  
D. `seating[0][1] = "Kabir"`

### 33. Visiting every seat in every row

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting iteration that follows nested structure

A chart contains rows of seat names. Which loop structure follows the two-level data shape and visits every individual name?

A. An outer `for row in seating` containing an inner `for seat in row`  
B. One `for seat in seating` loop that prints the complete seating chart once for every row it receives  
C. `for row in seating[0]: print(row)`  
D. `for seat in range(1): print(seat)`

### 34. Building independent rows of zeros

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a nested-comprehension structure

A program needs a 2-row by 3-column zero grid using the nested-comprehension pattern taught in the unit. Which expression builds the required shape?

A. `[0 for row in range(2) for column in range(3)]`, which produces a single flat sequence instead of separate rows  
B. `[[0, 0] for column in range(3)]`  
C. `[[0] * 2] * 3`  
D. `[[0 for column in range(3)] for row in range(2)]`

### 35. Counting work in uneven rows

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `nested-lists`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a ragged nested collection

A nested list contains `[[1, 2], [3], [4, 5, 6]]`. An outer loop visits rows and an inner loop handles each contained value. How many times does the inner action run?

A. `3`  
B. `6`  
C. `9`  
D. `2`

### 36. Reading every checklist item directly

**Difficulty:** Foundational

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting direct sequence iteration

A briefing needs every value from `packing_list`, and numeric positions are irrelevant. Which loop is clearest?

A. `for index in range(len(packing_list)): print(index)`  
B. `while packing_list:` without modifying it  
C. `for item in packing_list:`  
D. `for item in [packing_list]: print(item)`

### 37. Numbering itinerary days from one

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting correct `enumerate` usage

A public itinerary should label its first stored plan as Day 1 rather than Day 0. Which loop obtains number and plan together?

A. `for day, plan in enumerate(itinerary):`  
B. `for day in range(len(itinerary)):`  
C. `for plan, day in enumerate(itinerary, start=1):`  
D. `for day, plan in enumerate(itinerary, start=1):`

### 38. Unpacking each stop while looping

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting tuple unpacking during iteration

A route is a list of `(name, latitude, longitude)` tuples. Which loop header gives three separate variables with exactly those meanings on every pass?

A. `for name, latitude, longitude in route:`  
B. `for stop in route:`  
C. `for name, *coordinates in route:`  
D. `for (name, latitude), longitude in route:`

### 39. One list runs out before the other

**Difficulty:** Intermediate

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting unequal-length `zip` behaviour

`names` contains four students, while `seats` contains three seat numbers. A loop uses `zip(names, seats)`. How many pairs will it process?

A. `4`, with the last seat stored as `None`  
B. `7`, because both lengths are added  
C. `3`, because `zip` stops with the shorter input  
D. `0`, because `zip` rejects unequal lengths before producing any paired values

### 40. Numbering and unpacking itinerary records together

**Difficulty:** Advanced

**Taxonomy:** `python` → `lists-and-tuples` → `sequence-iteration`  
**Is Curriculum Based:** No  
**Assessment type:** Combining `enumerate` with nested unpacking

An itinerary stores tuples such as `("Day 1", "Museum")`. The briefing needs a sequence number plus both fields. Which loop header combines `enumerate` and tuple unpacking correctly?

A. `for number, day, plan in enumerate(itinerary, start=1):`, because `enumerate` expands each inner tuple into separate loop variables automatically  
B. `for number, (day, plan) in enumerate(itinerary, start=1):`  
C. `for (number, day), plan in itinerary:`  
D. `for number in enumerate(day, plan):`

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | Square brackets create a list, and the four mixed-type values remain in their written order. |
| 2 | A | Intermediate | `remove` deletes the first `"Tea"`, leaving `["Coffee", "Tea"]`; `pop(0)` then returns `"Coffee"` and leaves `["Tea"]`. |
| 3 | D | Foundational | The expression squares each value before the `for`, while the trailing condition retains only positive inputs. |
| 4 | B | Intermediate | The tuple's positions cannot be replaced, but the list already stored at position 0 remains a mutable list and can be appended to. |
| 5 | D | Advanced | The loader has two targets, while the three-item tuple supplies one extra value and raises a too-many-values unpacking error. |
| 6 | C | Foundational | `and` checks the row bound first; only for a valid row does Python inspect the selected row's actual length for the column bound. |
| 7 | A | Intermediate | Both loops visit indices or values covering every list item in order and append the same uppercase strings; direct iteration is clearer. |
| 8 | B | Intermediate | Assignment shares one list object, so appending through `backup` also changes the list observed through `items`. |
| 9 | A | Intermediate | An empty list is falsy, so the `else` branch assigns `"Queue empty"`. |
| 10 | D | Advanced | Plain assignment creates an alias; an explicit copy provides an independently mutable list. |
| 11 | B | Foundational | `count` returns how many times the requested value occurs. |
| 12 | C | Intermediate | `index` returns the first matching position, which is zero here. |
| 13 | D | Intermediate | `reverse()` flips the current sequence in place without sorting by value. |
| 14 | B | Advanced | The in-place method returns `None`, and the assignment overwrites the variable with that return value. |
| 15 | C | Advanced | `sorted()` returns a new ordered list and preserves the original playback sequence. |
| 16 | A | Foundational | The expression retains each seat whose remainder on division by two is zero. |
| 17 | B | Intermediate | The expression transforms every price and has no filter clause. |
| 18 | D | Intermediate | The condition filters by length, while the expression before `for` title-cases each retained name. |
| 19 | A | Intermediate | It builds a new list containing the original values that pass the positive-number condition. |
| 20 | C | Advanced | Multiple actions and side effects are clearer and easier to verify in an ordinary loop. |
| 21 | A | Foundational | A trailing comma distinguishes a one-item tuple from parenthesised arithmetic. |
| 22 | C | Intermediate | The second tuple value is at zero-based index 1. |
| 23 | D | Foundational | Tuples are immutable and reject item assignment. |
| 24 | B | Intermediate | Three variables on the left receive the tuple's three values in positional order. |
| 25 | C | Advanced | Unpacking requires the number of target variables to match the number of tuple items. |
| 26 | B | Foundational | A list is designed for a collection that must grow, shrink, and reorder. |
| 27 | A | Intermediate | A tuple groups the related coordinates and prevents either tuple position from being replaced after creation. |
| 28 | D | Intermediate | The list can grow, while each tuple inside it remains a fixed record. |
| 29 | B | Intermediate | The container communicates a fixed record shape and prevents accidental item reassignment. |
| 30 | A | Advanced | The required operations determine the container; a minor efficiency difference cannot replace needed mutation. |
| 31 | C | Foundational | Row index 1 selects the second row, and inner index 2 selects its third item. |
| 32 | D | Intermediate | `seating[0][1]` targets the second item of the first row. |
| 33 | A | Intermediate | One loop visits each row and the nested loop visits every item within that row. |
| 34 | D | Advanced | The inner comprehension creates three zeros per row and the outer comprehension creates two rows. |
| 35 | B | Advanced | The row lengths are 2, 1, and 3, for six inner visits in total. |
| 36 | C | Foundational | Direct iteration yields each item without unnecessary index management. |
| 37 | D | Intermediate | `enumerate` supplies both values, and `start=1` creates human-friendly numbering. |
| 38 | A | Intermediate | The loop header unpacks each three-value tuple into three named variables. |
| 39 | C | Intermediate | `zip` ends as soon as the shorter three-item list is exhausted. |
| 40 | B | Advanced | `enumerate` yields a number and one tuple, whose two elements are unpacked by the nested target. |

## Taxonomy coverage

| Unit 6 taxonomy subtopic | Question numbers |
|---|---|
| `lists` | 1, 8–10, 26, 28, 30 |
| `list-methods` | 2, 11–15 |
| `list-comprehensions` | 3, 16–20 |
| `tuples` | 4, 21–23, 27, 29 |
| `packing-and-unpacking` | 5, 24–25 |
| `nested-lists` | 6, 31–35 |
| `sequence-iteration` | 7, 36–40 |

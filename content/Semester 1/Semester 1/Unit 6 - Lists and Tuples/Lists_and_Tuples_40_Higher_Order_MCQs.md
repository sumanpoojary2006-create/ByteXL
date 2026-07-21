# Unit 6: Lists and Tuples - 40 Higher-Order MCQs

## Assessment design

- Scope: all eight Unit 6 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, repair selection, implementation comparison, and practical data modelling
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option

---

## Questions

### 1. One trip record holds different kinds of values

**Difficulty:** Foundational

A trip summary is stored as:

```python
trip = ["Pune", 3, 4500.0, True]
```

Which audit note accurately describes the collection?

A. It is a tuple because it contains four values  
B. It is invalid because every item in a Python list must use the same data type  
C. It is a four-item list that preserves the written order  
D. It is a string because the first item contains text

### 2. Reaching the final packing item without counting

**Difficulty:** Intermediate

A packing list may grow before departure. The checklist screen always needs its final item. Which expression remains correct as the length changes?

A. `packing_list[-1]`  
B. `packing_list[1]`  
C. `packing_list[len(packing_list)]`  
D. `packing_list[0]`

### 3. Previewing the middle two destinations

**Difficulty:** Foundational

A route is `['Pune', 'Nashik', 'Surat', 'Vadodara']`. Which slice produces `['Nashik', 'Surat']`?

A. `route[1:2]`  
B. `route[0:2]`  
C. `route[2:4]`  
D. `route[1:3]`

### 4. A seat lookup steps beyond the list

**Difficulty:** Intermediate

A row contains three names, so its valid indices are 0, 1, and 2. A screen requests `row[3]`. Which support classification fits the failed lookup?

A. `ValueError`, because the name is missing  
B. `IndexError`, because position 3 lies outside the list  
C. `TypeError`, because lists cannot use integer indices during a lookup at runtime  
D. No failure; Python returns an empty item

### 5. Editing a sliced preview

**Difficulty:** Advanced

A planner creates and edits a preview:

```python
route = ["Pune", "Nashik", "Surat", "Vadodara"]
preview = route[1:3]
preview[0] = "Mumbai"
```

Which state should the route review record?

A. Both values begin with `"Mumbai"` because slicing creates an alias that shares the original list's storage  
B. `route` becomes empty when its slice is edited  
C. `route[1]` changes because every sub-list edit changes its source  
D. `preview` changes, while `route` keeps `"Nashik"` because slicing made a new list

### 6. Adding one snack at the end

**Difficulty:** Foundational

A snack checklist must add `"chips"` after every existing item. Which method expresses that mutation directly?

A. `snacks.insert(0, "chips")`  
B. `snacks.remove("chips")`  
C. `snacks.append("chips")`  
D. `snacks.pop("chips")`

### 7. Protecting a fragile item at the front

**Difficulty:** Intermediate

A trip coordinator must place `"cake"` at index 0 while shifting the existing snacks right. Which operation fits?

A. `snacks.insert(0, "cake")`  
B. `snacks.append(0, "cake")`  
C. `snacks[0].append("cake")`  
D. `snacks.remove(0)`

### 8. Removing only the first duplicate request

**Difficulty:** Intermediate

A playlist is `['Song A', 'Song B', 'Song A']`. The coordinator runs `playlist.remove('Song A')`. Which list remains?

A. `['Song A', 'Song B']`  
B. `['Song B', 'Song A']`  
C. `['Song B']`  
D. `['Song A', 'Song B', 'Song A']`

### 9. Taking the last task out for immediate use

**Difficulty:** Intermediate

A stack-like checklist contains `tasks = ['pack', 'call', 'pay']` and runs `current = tasks.pop()`. Which state follows?

A. `current` is `'pay'` and `tasks` is `['pack', 'call']`  
B. `current` is `None` and the list remains unchanged  
C. `current` is `'pack'` and only the first item is removed  
D. All tasks move into `current` as another list

### 10. Two names point to one snack list

**Difficulty:** Advanced

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

A request list is `['Sky', 'Road', 'Sky', 'Sky']`. Which expression returns the number of `"Sky"` entries?

A. `requests.index("Sky")`  
B. `requests.count("Sky")`  
C. `requests.find("Sky")`  
D. `requests.sort("Sky")`

### 12. Locating the first matching stop

**Difficulty:** Intermediate

A route is `['Pune', 'Nashik', 'Pune']`. The planner uses `route.index('Pune')`. Which position is returned?

A. `2`  
B. `3`  
C. `0`  
D. `[0, 2]`

### 13. Newest additions should play first

**Difficulty:** Intermediate

A playlist is already in request order. The newest requests should temporarily become first without alphabetising anything. Which in-place method flips the current order?

A. `playlist.sort(reverse=True)`  
B. `sorted(playlist)`  
C. `playlist.count()`  
D. `playlist.reverse()`

### 14. A sorted playlist becomes `None`

**Difficulty:** Advanced

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

A music app must display songs alphabetically while preserving the original request order for playback. Which plan meets both needs?

A. Call `playlist.sort()` and use the permanently changed list for both display and later playback  
B. Call `playlist.reverse()` before every display  
C. Store `alphabetic = sorted(playlist)` and leave `playlist` unchanged  
D. Assign `alphabetic = playlist.sort()`

### 16. Selecting only the even seat numbers

**Difficulty:** Foundational

A bus system has `seats = [1, 2, 3, 4, 5, 6]`. Which comprehension builds `[2, 4, 6]`?

A. `[seat for seat in seats if seat % 2 == 0]`  
B. `[seat % 2 for seat in seats]`  
C. `[seats if seat % 2 == 0]`  
D. `[seat for seats in seat if seat == 2]`, which loops through each stored seat value

### 17. Applying the same discount to every price

**Difficulty:** Intermediate

A sale preview needs a new list containing 90% of every value in `prices`, with no filtering. Which comprehension fits?

A. `[price for price in prices if price == 0.9]`  
B. `[price * 0.9 for price in prices]`  
C. `[0.9 for price * prices]`  
D. `[price * 0.9 if prices]`

### 18. Filtering and formatting qualifying names

**Difficulty:** Intermediate

A report should keep names longer than four characters and title-case those retained. Which comprehension performs both operations?

A. `[name for name.title() in names if len(name) > 4]`  
B. `[len(name) > 4 for name in names]`  
C. `[name.title() for names if len(name) > 4]`  
D. `[name.title() for name in names if len(name) > 4]`

### 19. Replacing a loop-and-append filter

**Difficulty:** Intermediate

Version A appends each positive value from `numbers` into a new list. Which Version B is equivalent?

A. `positives = [number for number in numbers if number > 0]`  
B. `positives = [number > 0 for number in numbers]`  
C. `positives = [numbers for number > 0]`  
D. `positives = [number for number in numbers if number < 0]`

### 20. A comprehension hides a multi-step workflow

**Difficulty:** Advanced

A proposed comprehension validates each record, prints a rejection reason, updates an audit counter, and transforms accepted data in one dense line. Which review decision best supports maintainability?

A. Add another nested comprehension so validation, printing, counter updates, and transformation all remain inside one compact expression  
B. Remove validation because comprehensions cannot include conditions  
C. Use a regular loop because several steps and side effects make the comprehension hard to reason about  
D. Replace every variable name with one letter to shorten the line

### 21. Creating a one-item tuple

**Difficulty:** Foundational

A coordinate record must be a tuple containing only the value `5`. Which expression creates that one-item tuple?

A. `(5,)`  
B. `(5)`, because parentheses around one value always create a tuple  
C. `[5]`  
D. `{5}`

### 22. Reading one value from a fixed coordinate

**Difficulty:** Intermediate

A GPS coordinate is `location = (18.52, 73.85)`. Which expression retrieves the longitude `73.85`?

A. `location[-3]`  
B. `location[0]`  
C. `location[1]`  
D. `location(1)`

### 23. An accidental coordinate edit is refused

**Difficulty:** Foundational

A navigation tool tries `location[0] = 19.0` where `location` is a tuple. Which design property blocks the operation?

A. Tuples accept only string coordinates, so numeric latitude values must be converted before any position can be replaced  
B. Position zero cannot be used in sequences  
C. Coordinates must be sorted before editing  
D. Tuple items are immutable and do not support item assignment

### 24. Giving names to a packed stop record

**Difficulty:** Intermediate

A fixed stop is `stop = ('Fort', 18.4, 73.7)`. Which assignment unpacks the values by position?

A. `stop = name, latitude, longitude`  
B. `name, latitude, longitude = stop`  
C. `name = latitude = longitude = stop`  
D. `name, stop = latitude, longitude`

### 25. Three values enter two variables

**Difficulty:** Advanced

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

Items will be added, removed, and reordered until the bus leaves. Which container communicates those needs?

A. A tuple, because its locked contents can be rebuilt as a fresh tuple after every addition or removal  
B. A list, because it supports in-place membership changes  
C. A string containing comma-separated items  
D. A number recording only the item count

### 27. Protecting one fixed GPS pair

**Difficulty:** Intermediate

A destination's latitude and longitude form one fixed record that should not be edited after lookup. Which representation best documents that intent?

A. `coordinates = (18.52, 73.85)`  
B. `coordinates = [18.52, 73.85]`  
C. `coordinates = "18.52" + "73.85"`  
D. `coordinates = {18.52, 73.85}`

### 28. A route grows, but each stop remains fixed

**Difficulty:** Intermediate

An itinerary must accept new stops, while every stored stop remains a fixed `(name, latitude, longitude)` record. Which overall shape matches both requirements?

A. One tuple containing every mutable stop list  
B. A string containing all values with commas  
C. A tuple of names and a separate unrelated number  
D. A list whose items are stop tuples

### 29. Making an intent promise to future readers

**Difficulty:** Intermediate

A record always consists of a student's roll number and admission year. Neither field should change inside the program. Why is a tuple preferable to a list here?

A. Tuples automatically validate every roll number and prevent an admission year outside the permitted institutional range  
B. The tuple communicates a fixed related record and blocks item-level mutation  
C. Lists cannot hold an integer and a year together  
D. Tuples sort their contents as soon as they are created

### 30. Choosing a tuple only for tiny speed gains

**Difficulty:** Advanced

A developer selects a tuple for a shopping cart that must frequently add and remove products, arguing that tuples are slightly lighter. Which review response gives the sounder priority?

A. Use a list because required mutation matters more than the small tuple performance difference  
B. Keep the tuple and recreate the entire cart after every small change, because repeated replacement preserves immutability and avoids list methods  
C. Store each product in a separate variable to avoid both containers  
D. Use a tuple because performance always overrides the data's behavior

### 31. Reaching one seat by row and column

**Difficulty:** Foundational

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

Using the same chart, the coordinator must replace `"Ravi"` with `"Kabir"` without changing another seat. Which statement is precise?

A. `seating[1] = "Kabir"`  
B. `seating[1][0] = "Kabir"`  
C. `seating[0] = "Kabir"`  
D. `seating[0][1] = "Kabir"`

### 33. Visiting every seat in every row

**Difficulty:** Intermediate

A chart contains rows of seat names. Which loop structure follows the two-level data shape and visits every individual name?

A. An outer `for row in seating` containing an inner `for seat in row`  
B. One `for seat in seating` loop that prints the complete seating chart once for every row it receives  
C. `for row in seating[0]: print(row)`  
D. `for seat in range(1): print(seat)`

### 34. Building independent rows of zeros

**Difficulty:** Advanced

A program needs a 2-row by 3-column zero grid using the nested-comprehension pattern taught in the unit. Which expression builds the required shape?

A. `[0 for row in range(2) for column in range(3)]`, which produces a single flat sequence instead of separate rows  
B. `[[0, 0] for column in range(3)]`  
C. `[[0] * 2] * 3`  
D. `[[0 for column in range(3)] for row in range(2)]`

### 35. Counting work in uneven rows

**Difficulty:** Advanced

A nested list contains `[[1, 2], [3], [4, 5, 6]]`. An outer loop visits rows and an inner loop handles each contained value. How many times does the inner action run?

A. `3`  
B. `6`  
C. `9`  
D. `2`

### 36. Reading every checklist item directly

**Difficulty:** Foundational

A briefing needs every value from `packing_list`, and numeric positions are irrelevant. Which loop is clearest?

A. `for item in range(packing_list):`  
B. `while packing_list:` without modifying it  
C. `for item in packing_list:`  
D. `for packing_list in item:`

### 37. Numbering itinerary days from one

**Difficulty:** Intermediate

A public itinerary should label its first stored plan as Day 1 rather than Day 0. Which loop obtains number and plan together?

A. `for day, plan in itinerary:`  
B. `for day in range(itinerary):`  
C. `for plan in enumerate(1, itinerary):`, because the visible starting value must be supplied before the collection  
D. `for day, plan in enumerate(itinerary, start=1):`

### 38. Unpacking each stop while looping

**Difficulty:** Intermediate

A route is a list of `(name, latitude, longitude)` tuples. Which loop header gives readable variables on every pass?

A. `for name, latitude, longitude in route:`  
B. `for stop in name, latitude, longitude:`, which iterates across the three variable names before reading the route  
C. `for route in name:`  
D. `for name in latitude in longitude:`

### 39. One list runs out before the other

**Difficulty:** Intermediate

`names` contains four students, while `seats` contains three seat numbers. A loop uses `zip(names, seats)`. How many pairs will it process?

A. `4`, with the last seat stored as `None`  
B. `7`, because both lengths are added  
C. `3`, because `zip` stops with the shorter input  
D. `0`, because `zip` rejects unequal lengths before producing any paired values

### 40. Numbering and unpacking itinerary records together

**Difficulty:** Advanced

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
| 2 | A | Intermediate | Index -1 always selects the final item without requiring the current length. |
| 3 | D | Foundational | The slice begins at index 1 and stops before index 3, selecting indices 1 and 2. |
| 4 | B | Intermediate | A three-item list has no index 3, so the lookup raises `IndexError`. |
| 5 | D | Advanced | A slice creates a separate list, so mutating the preview does not rewrite the source list. |
| 6 | C | Foundational | `append` mutates the list by adding one item at its end. |
| 7 | A | Intermediate | `insert(0, value)` places the new value first and shifts existing items right. |
| 8 | B | Intermediate | `remove` deletes only the first matching value, leaving the later duplicate. |
| 9 | A | Intermediate | With no index, `pop` removes and returns the final item. |
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
| 27 | A | Intermediate | A tuple groups the related coordinates while signalling and enforcing item immutability. |
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

## Topic coverage

| Unit 6 topic | Question numbers |
|---|---|
| List creation, indexing, and slicing | 1–5 |
| Mutating lists | 6–10 |
| List methods and sorting | 11–15 |
| List comprehensions | 16–20 |
| Tuples, immutability, packing, and unpacking | 21–25 |
| Choosing tuples versus lists | 26–30 |
| Nested lists | 31–35 |
| Iterating over lists and tuples | 36–40 |

# Unit 5: Strings - 40 Higher-Order MCQs

## Assessment design

- Scope: all nine Unit 5 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, repair selection, text-pipeline analysis, and practical application
- Answer-quality controls: balanced answer positions, no consecutive repeated correct letter, and varied option lengths
- Opening coverage: Questions 1–10 collectively represent all eight Unit 5 taxonomy subtopics
- Metadata: every question identifies its taxonomy and primary assessment behaviour

---

## Questions

### 1. A username counter includes the separator

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `string-basics`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

A craft-page username field contains `"Meera Arts"`. Its counter uses `len()` and treats every character, including spaces, as part of the text. Which count will appear beside the field?

A. `9`  
B. `10`  
C. `11`  
D. `2`

### 2. Repairing an off-by-one category slice

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `indexing-and-slicing`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an incorrect boundary; smallest correct repair

A product code stores its category at indices 2 through 5 inclusive. The current slice loses the final category character:

```python
code = "ABCD1234"
category = code[2:5]       # currently "CD1"
```

Which smallest replacement produces the required `"CD12"` without changing the starting index?

A. `code[2:5:2]`  
B. `code[1:5]`  
C. `code[2:7]`  
D. `code[2:6]`

### 3. Retaining a cleaned required name

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a discarded-result bug; truthiness reasoning; smallest repair

A registration field containing only spaces must become an empty string after cleaning, and its validity flag must then be false:

```python
name = "   "
name.strip()
has_name = bool(name)
```

The current code discards the cleaned result and incorrectly stores `True` in `has_name`. Which smallest repair creates the intended state?

A. Replace `name.strip()` with `name = name.strip()` before calculating `has_name`  
B. Replace `bool(name)` with `len(name) > 0` without storing the stripped result  
C. Replace `name.strip()` with `name.upper()`  
D. Set `has_name = True` whenever the original input contains characters

### 4. Selecting the input that exposes a faulty email search

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `searching-and-membership`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes a defect; truthiness reasoning

A signup form uses the integer returned by `.find()` directly as a Boolean:

```python
if email.find("@"):
    status = "Accepted"
else:
    status = "Rejected"
```

The policy requires an at sign anywhere in the address. Which input most clearly proves that the implementation can accept an address containing no at sign?

A. `"a@b.com"`  
B. `"meera@shop.in"`  
C. `"meerashop.in"`  
D. `"x@y"`

### 5. Checking whether two slug builders are equivalent

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `split-and-join`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

Two developers convert comma-separated tags into a hyphenated slug.

Version A:

```python
slug = "-".join(tags.split(","))
```

Version B:

```python
slug = tags.replace(",", "-")
```

Assume `tags` is always a string. Which equivalence finding is correct, including for adjacent or trailing commas?

A. Version A deletes empty pieces, so the versions differ whenever commas touch  
B. Both replace every comma boundary with one hyphen and produce the same string for every `tags` value  
C. Version B replaces only the first comma  
D. They are equivalent only when `tags` contains exactly one comma

### 6. Repairing a price that shows one decimal place

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-formatting`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest formatting repair

A receipt stores `price = 49.5` but currently displays `₹49.5`:

```python
line = f"₹{price:.1f}"
```

Which smallest format-specifier repair produces the required `₹49.50` while leaving the numeric value unchanged?

A. `line = f"₹{price:.2f}"`  
B. `line = f"₹{price:2}"`  
C. `line = f"₹{price:.2%}"`  
D. `line = f"₹{price:,}"`

### 7. Preserving a path and moving the filename to a new line

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `escape-sequences`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a literal with two layout requirements

A deployment note must display a Windows folder literally and place the filename on the next line:

```text
C:\new\table
report.txt
```

Which assignment preserves the backslashes and inserts the required line break?

A. `note = "C:\new\table report.txt"`  
B. `note = r"C:\new\table\nreport.txt"`  
C. `note = "C:\new\table\nreport.txt"`  
D. `note = "C:\\new\\table\nreport.txt"`

### 8. Auditing a complete campaign-cleaning pipeline

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple transformations; final value identification

A campaign tool normalises a short message and prepares a compact summary:

```python
message = "  RED, blue,Red  "
clean = message.strip().lower().replace(",", " ")
words = clean.split()
summary = f"{len(words)} words | red={clean.count('red')}"
```

Which summary reaches the audit log after every transformation?

A. `"4 words | red=1"`  
B. `"3 words | red=1"`  
C. `"3 words | red=2"`  
D. `"4 words | red=2"`

### 9. Editing one character of a locked string

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `string-basics`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected immutable-string behaviour

A developer tries to correct `"Nython"` using:

```python
word = "Nython"
word[0] = "P"
```

Which review note accounts for the failed update?

A. Strings do not support item assignment because they are immutable  
B. Index zero refers to the final character of a string  
C. Only lowercase replacement characters are allowed  
D. Square brackets can be used only with numeric values, so text must be converted before editing

### 10. Rebuilding a misspelled language name

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `indexing-and-slicing`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct immutable-string repair

A code label contains `word = "Nython"`. Which assignment creates `"Python"` without attempting to mutate the original string object?

A. `word[0] = "P"`  
B. `word = word[0] + "P"`  
C. `word = "P" + word[1:]`  
D. `word = word[:-1] + "P"`

### 11. An uppercase result is discarded

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a logic bug; final value tracing

A profile service runs:

```python
name = "asha"
name.upper()
print(name)
```

The screen still shows lowercase text. Which explanation should appear in the review?

A. `upper()` changes only the first character  
B. The method returned a new string, but no variable stored that result  
C. Printing converts uppercase strings back to lowercase  
D. String methods work only on text entered with `input()` and cannot transform literals or stored variables

### 12. Original and transformed captions remain separate

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying final values after a transformation

A moderation tool keeps both versions:

```python
original = "summer sale"
display = original.title()
```

Which pair should the audit report contain?

A. `original = "Summer Sale"`, `display = "Summer Sale"`  
B. `original = "summer sale"`, `display = "summer sale"`  
C. Both variables become empty after the method call  
D. `original = "summer sale"`, `display = "Summer Sale"`

### 13. Normalising an email before comparison

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct normalisation approach

A login field may contain capital letters and accidental spaces at both ends. Which expression produces a trimmed, lowercase version for comparison?

A. `email.upper().strip()`  
B. `email.replace(" ", "_")`  
C. `email.strip().lower()`  
D. `email.title()`

### 14. Replacing every matching letter

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based output prediction

A word-game hint applies:

```python
hint = "banana".replace("a", "o")
```

Which hint is stored?

A. `"bonana"`  
B. `"bonono"`  
C. `"banana"`  
D. `"booooo"`

### 15. A decimal point fails a digit-only check

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected validation behaviour

A form receives `raw_price = "12.5"` and evaluates `raw_price.isdigit()`. Which validation result should the team expect?

A. `True`, because the text represents a numeric value  
B. `True`, because punctuation is ignored by `isdigit()`  
C. A conversion error before any Boolean is produced  
D. `False`, because the decimal point is not a digit

### 16. Capturing every cleanup step

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `string-methods`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct pipeline repair

A customer name arrives as `"   meera shah   "`. The stored value must become `"Meera Shah"`. Which one-line repair both transforms and retains the cleaned result?

A. `name = name.strip().title()`  
B. `name.strip().title()`  
C. `name = name.upper().replace(" ", "")`  
D. `name = name.lower().rstrip()`

### 17. Turning one tag line into three values

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `split-and-join`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriate split operation

A craft form stores `tags = "handmade,gifts,pune"`. Which expression separates it at the commas?

A. `tags.join(",")`, because `join` separates text  
B. `tags.split()`  
C. `",".join(tags)`  
D. `tags.split(",")`

### 18. Several spaces still represent one boundary

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `split-and-join`  
**Is Curriculum Based:** No  
**Assessment type:** Predicting default split behaviour

A sentence contains irregular spacing:

```python
words = "fresh   handmade  gifts".split()
```

Which list structure is produced by the default split behavior?

A. `['fresh', 'handmade', 'gifts']`  
B. `['fresh', '', '', 'handmade', '', 'gifts']`  
C. `['fresh   handmade  gifts']`  
D. `['fresh', '   ', 'handmade', '  ', 'gifts']`

### 19. Constructing a URL-friendly tag

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `split-and-join`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a realistic join operation

A page has `parts = ["handmade", "gifts", "pune"]` and needs `"handmade-gifts-pune"`. Which expression uses the intended separator?

A. `parts.join("-")`  
B. `"".join(parts)`  
C. `"-".join(parts)`  
D. `parts.split("-")`

### 20. Numeric IDs cannot be joined directly

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `split-and-join`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a type defect; selecting the smallest redesign

A report tries to build a code using `"-".join([10, 20, 30])` and is rejected. Which diagnosis guides the smallest appropriate redesign?

A. Wrap the complete `join` call in `str()`; conversion after joining will make the integer elements acceptable  
B. Every joined piece must already be a string, so the numeric IDs need string representations  
C. Convert the entire list once with `str([10, 20, 30])` and pass that one string to `join`, which will preserve each ID as one piece  
D. Call `[10, 20, 30].join("-")` so the collection, rather than the separator, controls the operation

### 21. Completing a rough email membership condition

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `searching-and-membership`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing condition

A signup form needs a quick branch that accepts text containing an at sign anywhere:

```python
if __________________:
    status = "Continue"
else:
    status = "Missing @"
```

Which expression completes the condition directly without relying on a numeric search position?

A. `"@" in email`  
B. `email.find("@")`  
C. `email.count("@") + 1`  
D. `email.startswith("@") and email.endswith("@")`

### 22. Searching safely for an optional marker

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `searching-and-membership`  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting a search sentinel value

A tracking reference may or may not contain `"-"`. The program uses `reference.find("-")`. Which value signals that the marker is absent without raising an exception?

A. `0`  
B. `False`  
C. `None`  
D. `-1`

### 23. Case-sensitive sale counting

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `searching-and-membership`  
**Is Curriculum Based:** No  
**Assessment type:** Scenario-based search prediction

A caption is `"Sale sale SALE"`. The analytics code uses `caption.count("sale")` without normalising case. Which count is recorded?

A. `3`  
B. `1`  
C. `2`  
D. `0`

### 24. Tracing an upload rule with two required text checks

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `searching-and-membership`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions; validation reasoning

A portal accepts an upload only when its name ends in `.jpg` regardless of case and its caption is not empty after surrounding spaces are removed:

```python
filename = "PRODUCT.JPG"
caption = "  Summer sale  "

accepted = filename.lower().endswith(".jpg") and bool(caption.strip())
```

Which audit result correctly traces both requirements?

A. `False`, because lowercasing the filename changes the stored original  
B. `False`, because `.strip()` always produces an empty string  
C. `True`, because the normalised filename has the required suffix and the cleaned caption is non-empty  
D. `True`, because `and` needs only one side to succeed

### 25. Showing a price with two decimal places

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `string-formatting`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a numeric format specification

A product stores `price = 49.5`. Which f-string displays the customer-facing value as `₹49.50`?

A. `f"₹{price}"`  
B. `f"₹{price:2}"`  
C. `f"₹{price:.1f}"`  
D. `f"₹{price:.2f}"`

### 26. Making a large order total readable

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-formatting`  
**Is Curriculum Based:** No  
**Assessment type:** Applying a thousands-separator format

A wholesale order total is `1500000`. Which f-string displays it as `1,500,000`?

A. `f"{total:.2f}"`  
B. `f"{total:,}"`  
C. `f"{total:.1%}"`  
D. `f"{total:^10}"`

### 27. Repairing a percentage that is scaled twice

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `string-formatting`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a formatting bug; selecting the smallest repair

A dashboard stores `completion = 0.873` but incorrectly multiplies it before applying percentage formatting:

```python
display = f"{completion * 100:.1%}"
```

The screen shows `8730.0%` instead of `87.3%`. Which smallest repair removes the double scaling?

A. `f"{completion:.1f}%"`  
B. `f"{completion * 100:.1%}"`  
C. `f"{completion:.1%}"`  
D. `f"{completion:,.1f}"`

### 28. Aligning a product name and its price

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `string-formatting`  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple alignment and precision requirements

A price list requires the product name left-aligned in a width of 12 and its price right-aligned in a width of 8. Which template applies those two alignments?

A. `f"{name:<12}{price:>8.2f}"`  
B. `f"{name:>12}{price:<8.2f}"`  
C. `f"{name:^12}{price:^8.2f}"`  
D. `f"{name:12.2f}{price:8}"`

### 29. Placing the order total on a new line

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `escape-sequences`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a required output layout

A receipt needs `Item: Notebook` on the first line and `Total: 80` on the second. Which escape sequence creates that line break inside one string?

A. `\t`  
B. `\n`  
C. `\\`  
D. `\"`

### 30. Preserving quotation marks in a review

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `escape-sequences`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a syntactically valid escaped literal

A message must contain the exact text `She said "great"` while using double quotes around the Python string. Which assignment is valid?

A. `review = "She said "great""`  
B. `review = "She said \great\"`  
C. `review = "She said \"great\""`  
D. `review = "She said /"great/""`

### 31. A Windows path must keep its backslashes

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `escape-sequences`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected escape behaviour; selecting a repair

A configuration value must preserve the characters in `C:\new\table` rather than interpreting `\n` and `\t`. Which literal is clearest for that purpose?

A. `path = r"C:\new\table"`  
B. `path = "C:\new\table"`  
C. `path = "C:/n/e/w/t/a/b/l/e"`  
D. `path = "C:newtable"`

### 32. Keeping a three-line message readable in source code

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `escape-sequences`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriate multiline representation

A confirmation email has three fixed lines and should be written in source with the same visible line structure. Which representation best fits?

A. A one-line string with every space replaced by a tab  
B. Three unrelated variables that are never combined  
C. A raw string with no actual line breaks  
D. A triple-quoted string containing the three lines

### 33. Cleaning a caption through a method pipeline

**Difficulty:** Foundational

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a cleanup pipeline

A caption arrives as `"  Hello, WORLD  "`. The pipeline is:

```python
clean = caption.strip().lower().replace(",", "")
```

Which cleaned caption is stored?

A. `"Hello WORLD"`  
B. `"  hello world  "`  
C. `"hello world"`  
D. `"hello, world"`

### 34. Unpacking a structured customer record

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying a final field value after parsing

A line contains `"Asha,20,Pune"` and is processed with:

```python
name, age, city = line.split(",")
```

Which city value reaches the customer profile?

A. `"Pune"`  
B. `"20"`  
C. `"Asha,20"`  
D. `"Asha"`

### 35. Counting words despite irregular spacing

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Applying a word-count pipeline

A feedback message is `"fast   delivery and packaging"`. The analyzer uses `len(message.split())`. Which word count is reported?

A. `6`  
B. `3`  
C. `5`  
D. `4`

### 36. Counting characters but excluding spaces

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a character-cleaning calculation

An analyzer measures `"data science"` after removing ordinary spaces:

```python
character_count = len(text.replace(" ", ""))
```

Which count reaches the report?

A. `12`  
B. `11`  
C. `10`  
D. `2`

### 37. Finding a keyword without caring about case

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct normalised validation approach

A moderator searches for a user-supplied `keyword` inside `message`, and capitalisation should not affect the result. Which condition normalises both sides?

A. `keyword.lower() in message.lower()`  
B. `keyword in message.lower()`  
C. `keyword.upper() == message.lower()`  
D. `message.find(keyword) == 0`

### 38. Converting messy tags into a clean slug

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple text transformations

A tag line is `" red,BLUE, green "`. The program runs:

```python
parts = tag_line.replace(" ", "").lower().split(",")
slug = "-".join(parts)
```

Which slug is produced?

A. `"redbluegreen"`  
B. `"red,blue,green"`  
C. `"red-blue-green"`  
D. `" Red-Blue-Green "`

### 39. An extra comma changes the record shape

**Difficulty:** Intermediate

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a structural parsing defect

An importer expects exactly three fields:

```python
name, age, city = line.split(",")
```

The line is `"Asha,20,Pune,India"`, and the importer rejects it. Which support note identifies the structural mismatch?

A. Adding `maxsplit=2` proves the original line has only three fields because the last value would automatically remain just `"Pune"`  
B. The split creates four pieces, but the assignment provides only three variables  
C. A fourth variable is required because `split` returns one comma character as an extra value in addition to the three fields  
D. Joining the result with commas before unpacking would preserve four separate values while making three variables sufficient

### 40. Summarising a cleaned campaign message

**Difficulty:** Advanced

**Taxonomy:** `python` → `strings` → `text-processing`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a complete text-processing pipeline

A campaign analyzer runs:

```python
message = "  Python, python makes TEXT fun  "
clean = message.strip().lower().replace(",", "")
words = clean.split()
python_mentions = clean.count("python")
summary = f"{len(words)} words | python={python_mentions}"
```

Which summary is generated after the full pipeline?

A. `"6 words | python=1"`  
B. `"5 words | python=1"`  
C. `"6 words | python=2"`  
D. `"5 words | python=2"`

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | B | Foundational | The nine letters plus the space give a total length of 10. |
| 2 | D | Foundational | Slice stops are exclusive, so changing the stop from 5 to 6 includes index 5 and produces `"CD12"`. |
| 3 | A | Intermediate | Reassignment retains the empty result of stripping the spaces, after which `bool(name)` correctly produces `False`. |
| 4 | C | Advanced | An absent at sign makes `.find()` return `-1`, and `-1` is truthy, so the faulty condition accepts the invalid input. |
| 5 | B | Intermediate | Splitting on an explicit comma preserves empty pieces, and joining places one hyphen at every former comma boundary, exactly like `replace`. |
| 6 | A | Intermediate | Changing `.1f` to `.2f` preserves the value and displays exactly two digits after the decimal point. |
| 7 | D | Intermediate | Doubled backslashes preserve the folder separators, while `\n` between the path and filename creates the required line break. |
| 8 | C | Advanced | Cleaning produces `"red  blue red"`; default splitting yields three words, and `red` occurs twice. |
| 9 | A | Foundational | Indexing can read a string but cannot assign into it because strings are immutable. |
| 10 | C | Intermediate | The expression builds a new string from `"P"` and the unchanged slice `"ython"`. |
| 11 | B | Foundational | Transforming methods return a new string; ignoring the return value leaves the original variable unchanged. |
| 12 | D | Advanced | `title()` produces a new value for `display` and does not modify `original`. |
| 13 | C | Foundational | `strip()` removes surrounding whitespace and `lower()` normalises the remaining characters. |
| 14 | B | Intermediate | `replace` swaps every lowercase `a`, producing `"bonono"`. |
| 15 | D | Intermediate | `.isdigit()` requires every character to be a digit, and the decimal point fails that test. |
| 16 | A | Advanced | The chained methods produce the required form, and reassignment retains the new string. |
| 17 | D | Foundational | `split(",")` cuts the original string wherever a comma occurs. |
| 18 | A | Intermediate | With no argument, `split()` treats runs of whitespace as separators and does not create empty pieces. |
| 19 | C | Intermediate | `join` is called on the separator string and places that separator between all list items. |
| 20 | B | Advanced | `join` requires string pieces; integers need to be represented as strings before joining. |
| 21 | A | Foundational | The `in` operator directly returns whether the at sign occurs anywhere in the email. |
| 22 | D | Intermediate | `find` returns -1 when the searched text is absent. |
| 23 | B | Intermediate | Search is case-sensitive, so only the exact lowercase occurrence matches. |
| 24 | C | Advanced | The lowercased filename ends in `.jpg`, and stripping leaves the non-empty caption `"Summer sale"`, so both sides of `and` are true. |
| 25 | D | Foundational | The `.2f` specifier displays a numeric value with exactly two digits after the decimal point. |
| 26 | B | Intermediate | The comma format specifier inserts thousands separators. |
| 27 | C | Intermediate | `.1%` scales the proportion and displays one decimal place plus a percent sign. |
| 28 | A | Advanced | `<12` left-aligns the name, while `>8.2f` right-aligns a two-decimal price. |
| 29 | B | Foundational | `\n` inserts a newline within a string. |
| 30 | C | Intermediate | Escaped double quotes remain part of the text rather than terminating the string. |
| 31 | A | Intermediate | The raw-string prefix treats backslashes literally, preventing newline and tab escapes. |
| 32 | D | Advanced | Triple quotes preserve a multi-line block in the same visible layout used in the source. |
| 33 | C | Foundational | The chain trims the ends, lowercases the letters, and removes the comma. |
| 34 | A | Intermediate | Splitting yields `"Asha"`, `"20"`, and `"Pune"` in that order. |
| 35 | D | Intermediate | Default splitting yields the four words fast, delivery, and, and packaging. |
| 36 | B | Advanced | The four letters in data plus seven in science give 11 after the space is removed. |
| 37 | A | Intermediate | Lowercasing both strings makes the containment test case-insensitive. |
| 38 | C | Intermediate | The pipeline removes spaces, normalises case, splits on commas, and rejoins with hyphens. |
| 39 | B | Intermediate | The three commas create four pieces, which cannot be unpacked into only three variables. |
| 40 | D | Advanced | Cleaning produces five words, and the lowercase text contains two occurrences of `python`. |

## Topic coverage

| Unit 5 taxonomy subtopic | Question numbers |
|---|---|
| `string-basics` | 1, 9 |
| `indexing-and-slicing` | 2, 10 |
| `string-methods` | 3, 11–16 |
| `searching-and-membership` | 4, 21–24 |
| `split-and-join` | 5, 17–20 |
| `string-formatting` | 6, 25–28 |
| `escape-sequences` | 7, 29–32 |
| `text-processing` | 8, 33–40 |

# Unit 5: Strings - 40 Higher-Order MCQs

## Assessment design

- Scope: all nine Unit 5 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, repair selection, text-pipeline analysis, and practical application
- Answer-quality controls: balanced answer positions, no consecutive repeated correct letter, and varied option lengths

---

## Questions

### 1. A username counter includes the separator

**Difficulty:** Foundational

A craft-page username field contains `"Meera Arts"`. Its counter uses `len()` and treats every character, including spaces, as part of the text. Which count will appear beside the field?

A. `9`  
B. `10`  
C. `11`  
D. `2`

### 2. Keeping an apostrophe inside the shop name

**Difficulty:** Foundational

A developer needs to store the exact text `Meera's Crafts` without ending the string at the apostrophe. Which assignment is valid and preserves the intended text?

A. `shop = 'Meera's Crafts'`  
B. `shop = Meera's Crafts`  
C. `shop = "Meera"s Crafts"`  
D. `shop = "Meera's Crafts"`

### 3. An untouched optional bio

**Difficulty:** Intermediate

A new profile starts with:

```python
bio = ""
bio_length = len(bio)
has_bio = bool(bio)
```

Which stored state accurately represents the untouched field?

A. `bio_length` is `0` and `has_bio` is `False`  
B. `bio_length` is `1` and `has_bio` is `True`  
C. `bio_length` is `2` because the quote marks are characters  
D. `bio` contains a single invisible space

### 4. Preserving a code that begins with zero

**Difficulty:** Advanced

A parcel identifier is `"00751"`. It is displayed, searched, and sliced, but never used in arithmetic. Which storage decision preserves its meaning best?

A. Store it as `751.0` because every identifier is a measurement  
B. Store it as `751` and recreate the missing zeros from a separate width rule whenever it is displayed  
C. Keep it as a string so its ordered characters and leading zeros remain intact  
D. Convert it to `True` because the identifier is present

### 5. Taking the first initial from a name

**Difficulty:** Foundational

A badge generator stores `name = "Meera"` and needs the first initial. Which expression selects it directly?

A. `name[1]`  
B. `name[0]`  
C. `name[-1]`  
D. `name[:0]`

### 6. Masking all but the final four digits

**Difficulty:** Intermediate

A payment message must show only the final four characters of a phone number whose total length may vary. Which slice is robust to that variation?

A. `phone[-4:]`  
B. `phone[4:]`  
C. `phone[:4]`  
D. `phone[-1:4]`

### 7. Extracting the middle of a product code

**Difficulty:** Intermediate

A product code is `"ABCD1234"`. The category is stored at indices 2 through 5 inclusive, which should produce `"CD12"`. Which slice matches that requirement?

A. `code[2:5]`  
B. `code[1:5]`  
C. `code[2:5:2]`  
D. `code[2:6]`

### 8. Sampling alternate characters from a label

**Difficulty:** Advanced

A scanner applies this slice:

```python
label = "ABCDEFG"
sample = label[1:6:2]
```

Which sample reaches the audit log?

A. `"ACE"`  
B. `"BCDEF"`  
C. `"BDF"`  
D. `"BDFG"`

### 9. Editing one character of a locked string

**Difficulty:** Foundational

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

A code label contains `word = "Nython"`. Which assignment creates `"Python"` without attempting to mutate the original string object?

A. `word[0] = "P"`  
B. `word = word[0] + "P"`  
C. `word = "P" + word[1:]`  
D. `word = word[:-1] + "P"`

### 11. An uppercase result is discarded

**Difficulty:** Intermediate

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

A login field may contain capital letters and accidental spaces at both ends. Which expression produces a trimmed, lowercase version for comparison?

A. `email.upper().strip()`  
B. `email.replace(" ", "_")`  
C. `email.strip().lower()`  
D. `email.title()`

### 14. Replacing every matching letter

**Difficulty:** Intermediate

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

A form receives `raw_price = "12.5"` and evaluates `raw_price.isdigit()`. Which validation result should the team expect?

A. `True`, because the text represents a numeric value  
B. `True`, because punctuation is ignored by `isdigit()`  
C. A conversion error before any Boolean is produced  
D. `False`, because the decimal point is not a digit

### 16. Capturing every cleanup step

**Difficulty:** Advanced

A customer name arrives as `"   meera shah   "`. The stored value must become `"Meera Shah"`. Which one-line repair both transforms and retains the cleaned result?

A. `name = name.strip().title()`  
B. `name.strip().title()`  
C. `name = name.upper().replace(" ", "")`  
D. `name = name.lower().rstrip()`

### 17. Turning one tag line into three values

**Difficulty:** Foundational

A craft form stores `tags = "handmade,gifts,pune"`. Which expression separates it at the commas?

A. `tags.join(",")`, because `join` separates text  
B. `tags.split()`  
C. `",".join(tags)`  
D. `tags.split(",")`

### 18. Several spaces still represent one boundary

**Difficulty:** Intermediate

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

A page has `parts = ["handmade", "gifts", "pune"]` and needs `"handmade-gifts-pune"`. Which expression uses the intended separator?

A. `parts.join("-")`  
B. `"".join(parts)`  
C. `"-".join(parts)`  
D. `parts.split("-")`

### 20. Numeric IDs cannot be joined directly

**Difficulty:** Advanced

A report tries to build a code using `"-".join([10, 20, 30])` and is rejected. Which diagnosis guides the smallest appropriate redesign?

A. `join` accepts only one item at a time, so loop through the list and append each numeric ID to the final string separately  
B. Every joined piece must already be a string, so the numeric IDs need string representations  
C. Hyphens cannot be used as separators between values  
D. `join` works only when called on a list rather than a string

### 21. A rough email check for the at sign

**Difficulty:** Foundational

A signup form only needs a quick Boolean indicating whether `email` contains `"@"`. Which expression communicates that check directly?

A. `"@" in email`  
B. `email.find("@")`  
C. `email.count("@") + 1`  
D. `email.startswith("@") and email.endswith("@")`

### 22. Searching safely for an optional marker

**Difficulty:** Intermediate

A tracking reference may or may not contain `"-"`. The program uses `reference.find("-")`. Which value signals that the marker is absent without raising an exception?

A. `0`  
B. `False`  
C. `None`  
D. `-1`

### 23. Case-sensitive sale counting

**Difficulty:** Intermediate

A caption is `"Sale sale SALE"`. The analytics code uses `caption.count("sale")` without normalising case. Which count is recorded?

A. `3`  
B. `1`  
C. `2`  
D. `0`

### 24. Accepting an image extension regardless of case

**Difficulty:** Advanced

An upload named `"PRODUCT.JPG"` should pass a rough `.jpg` extension check. Which condition handles the stated case variation?

A. `filename.lower().startswith(".jpg")`  
B. `filename.find(".jpg") == 0`  
C. `filename.lower().endswith(".jpg")`  
D. `filename.count("JPG") > 1`

### 25. Showing a price with two decimal places

**Difficulty:** Foundational

A product stores `price = 49.5`. Which f-string displays the customer-facing value as `₹49.50`?

A. `f"₹{price}"`  
B. `f"₹{price:2}"`  
C. `f"₹{price:.1f}"`  
D. `f"₹{price:.2f}"`

### 26. Making a large order total readable

**Difficulty:** Intermediate

A wholesale order total is `1500000`. Which f-string displays it as `1,500,000`?

A. `f"{total:.2f}"`  
B. `f"{total:,}"`  
C. `f"{total:.1%}"`  
D. `f"{total:^10}"`

### 27. Converting a ratio into a percentage display

**Difficulty:** Intermediate

A dashboard stores `completion = 0.873`. Which format produces `87.3%` directly?

A. `f"{completion:.1f}%"`  
B. `f"{completion * 100:.1%}"`  
C. `f"{completion:.1%}"`  
D. `f"{completion:,.1f}"`

### 28. Aligning a product name and its price

**Difficulty:** Advanced

A price list requires the product name left-aligned in a width of 12 and its price right-aligned in a width of 8. Which template applies those two alignments?

A. `f"{name:<12}{price:>8.2f}"`  
B. `f"{name:>12}{price:<8.2f}"`  
C. `f"{name:^12}{price:^8.2f}"`  
D. `f"{name:12.2f}{price:8}"`

### 29. Placing the order total on a new line

**Difficulty:** Foundational

A receipt needs `Item: Notebook` on the first line and `Total: 80` on the second. Which escape sequence creates that line break inside one string?

A. `\t`  
B. `\n`  
C. `\\`  
D. `\"`

### 30. Preserving quotation marks in a review

**Difficulty:** Intermediate

A message must contain the exact text `She said "great"` while using double quotes around the Python string. Which assignment is valid?

A. `review = "She said "great""`  
B. `review = "She said \great\"`  
C. `review = "She said \"great\""`  
D. `review = "She said /"great/""`

### 31. A Windows path must keep its backslashes

**Difficulty:** Intermediate

A configuration value must preserve the characters in `C:\new\table` rather than interpreting `\n` and `\t`. Which literal is clearest for that purpose?

A. `path = r"C:\new\table"`  
B. `path = "C:\new\table"`  
C. `path = "C:/n/e/w/t/a/b/l/e"`  
D. `path = "C:newtable"`

### 32. Keeping a three-line message readable in source code

**Difficulty:** Advanced

A confirmation email has three fixed lines and should be written in source with the same visible line structure. Which representation best fits?

A. A one-line string with every space replaced by a tab  
B. Three unrelated variables that are never combined  
C. A raw string with no actual line breaks  
D. A triple-quoted string containing the three lines

### 33. Cleaning a caption through a method pipeline

**Difficulty:** Foundational

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

A feedback message is `"fast   delivery and packaging"`. The analyzer uses `len(message.split())`. Which word count is reported?

A. `6`  
B. `3`  
C. `5`  
D. `4`

### 36. Counting characters but excluding spaces

**Difficulty:** Advanced

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

A moderator searches for a user-supplied `keyword` inside `message`, and capitalisation should not affect the result. Which condition normalises both sides?

A. `keyword.lower() in message.lower()`  
B. `keyword in message.lower()`  
C. `keyword.upper() == message.lower()`  
D. `message.find(keyword) == 0`

### 38. Converting messy tags into a clean slug

**Difficulty:** Intermediate

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

An importer expects exactly three fields:

```python
name, age, city = line.split(",")
```

The line is `"Asha,20,Pune,India"`, and the importer rejects it. Which support note identifies the structural mismatch?

A. `split` removes the final field whenever three commas occur, so the country is discarded and only three pieces remain  
B. The split creates four pieces, but the assignment provides only three variables  
C. Commas are not valid separators for strings  
D. `split` joins the city and country into one field automatically

### 40. Summarising a cleaned campaign message

**Difficulty:** Advanced

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
| 2 | D | Foundational | Double quotes safely contain the apostrophe as an ordinary character. |
| 3 | A | Intermediate | The empty string has length zero and is falsy. |
| 4 | C | Advanced | An identifier is text, and string storage preserves the meaningful leading zeros and character order. |
| 5 | B | Foundational | String indices begin at zero, so index 0 selects the first character. |
| 6 | A | Intermediate | `[-4:]` starts four positions from the end and continues through the final character. |
| 7 | D | Intermediate | The stop is excluded, so a stop of 6 includes indices 2, 3, 4, and 5. |
| 8 | C | Advanced | Starting at index 1 and stepping by 2 visits B, D, and F before the exclusive stop at 6. |
| 9 | A | Foundational | Indexing can read a string but cannot assign into it because strings are immutable. |
| 10 | C | Intermediate | The expression builds a new string from `"P"` and the unchanged slice `"ython"`. |
| 11 | B | Intermediate | Transforming methods return a new string; ignoring the return value leaves the original variable unchanged. |
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
| 24 | C | Advanced | Lowercasing first makes the extension test independent of the filename's capitalisation. |
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

| Unit 5 topic | Question numbers |
|---|---|
| What a string is and how it is stored | 1–4 |
| Indexing and slicing | 5–8 |
| String immutability | 9–12 |
| Common string methods | 13–16 |
| Splitting and joining | 17–20 |
| Searching within strings | 21–24 |
| String formatting and f-strings | 25–28 |
| Escape sequences and multi-line strings | 29–32 |
| Practical text processing | 33–40 |

# Mini Project 8: JSON Data Processor

## Background

Real-world JSON rarely arrives clean. Files go missing, fields get renamed, a price shows up as the string "10" instead of a number, an entire record is missing a required key. A JSON processor that assumes the data is always well-formed will crash the moment it meets production data. This project puts everything from this unit to work: `try`/`except`, specific exception types, custom exceptions, and defensive validation, all applied to a single realistic task.

## What You Will Build

A CLI tool that loads a JSON inventory file, validates every record, reports which ones are broken and why, and computes summary statistics for the valid ones — without ever crashing, no matter how badly the file is broken.

## Dataset

Create this file manually and save it as `inventory.json`. Keep the errors exactly as shown — they are intentional:

```json
[
  {"name": "Notebook", "price": 45, "quantity": 120, "category": "Stationery"},
  {"name": "Pen", "price": "10", "quantity": 300, "category": "Stationery"},
  {"name": "Charger", "price": 599, "quantity": 40, "category": "Electronics"},
  {"price": 250, "quantity": 15, "category": "Electronics"},
  {"name": "Notebook Bag", "price": -199, "quantity": 25, "category": "Accessories"},
  {"name": "Water Bottle", "price": 150, "quantity": "unknown", "category": "Accessories"},
  {"name": "Desk Lamp", "price": 350, "quantity": 60, "category": "Electronics"}
]
```

## Tasks

### Task 1: Load the File Safely

1. Write a function `load_inventory(filepath)` that opens and parses the JSON file using `json.load()`.
2. Wrap the file operation in a `try`/`except` block that handles `FileNotFoundError` (clear message, tool exits gracefully) and `json.JSONDecodeError` (tells the user the file's JSON is malformed) separately.
3. If loading succeeds, display the total number of records found.

### Task 2: Validate Every Record

1. Define a custom exception `InvalidRecordError` with a message describing what is wrong.
2. Write a function `validate_record(record)` that raises `InvalidRecordError` when:
   - The `name` key is missing
   - `price` cannot be converted to a float, or converts to a value less than 0
   - `quantity` cannot be converted to a non-negative integer

   When `price` or `quantity` convert successfully, overwrite the record's value with the converted number (not the original string) so every later calculation works with real numbers.
3. Loop through every record from the file. For each one, call `validate_record()` inside a `try`/`except` that catches `InvalidRecordError` — on failure, record the problem (which record, and why) instead of stopping the whole program.
4. At the end, display two lists: valid records and invalid records with their specific error messages.

   ```
   VALID RECORDS: 4
   INVALID RECORDS: 3
     - Record 4: missing required field 'name'
     - Record 5: price is negative (-199)
     - Record 6: quantity is not a valid number ('unknown')
   ```

### Task 3: Statistics and a Clean Report

1. Using only the valid records, compute and display:
   - Total number of valid products
   - Total inventory value (sum of price × quantity across valid records)
   - Highest-priced product and its price
   - Number of products per category

2. Wrap the statistics section in a `try`/`except`/`else`/`finally`: the `else` block runs the report only if no unexpected error occurred while computing it, and the `finally` block always prints "Processing complete" regardless of outcome.

3. Give the user the option to re-run the whole tool on a different filename, so they can test it against a file that does not exist.

**Answer these questions after completing all tasks:**
- Record 2 has a price of `"10"` (a string) rather than `10`. Your `validate_record()` is expected to convert it and overwrite the record so it holds a real number. If you checked convertibility but forgot the overwrite, what happens when Task 3 computes price × quantity for this record — does it crash, or produce a silently wrong number? Test it by removing the overwrite line and rerunning.
- You catch `InvalidRecordError` per-record inside the loop, but `FileNotFoundError` and `json.JSONDecodeError` stop the whole program. Why is a bad individual record recoverable while a missing file is not?
- Add an eighth record to `inventory.json` with `price` as `null`. Run your program without changing any code. What happens, and which of your existing `except` blocks — if any — catches it?

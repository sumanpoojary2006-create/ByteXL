## Introduction

Tara's merch stall sales would be perfect in a spreadsheet: item name in one column, quantity sold in the next, price in the next, one row per sale. Plain text files do not naturally have columns at all, only lines, so she has been separating values with commas inside each line by hand, "T-shirt,2,350", and splitting them back apart with `.split(",")` whenever she reads them, exactly the string technique from several units ago. It works, but every comma inside an item name, or every tiny formatting slip, breaks the split in a way that is easy to get wrong.

This comma-separated layout is common enough to have its own standard format, called **CSV**, short for comma-separated values, and Python's built-in `csv` module handles its real-world quirks far more reliably than splitting strings by hand ever could.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/07_csv_rows_and_columns.png)

## What a CSV File Looks Like

A CSV file is plain text, where each line is a row, and commas separate that row's columns.

```
item,quantity,price
T-shirt,2,350
Mug,1,150
Badge,5,50
```

The very first line is conventionally a **header**, naming each column, though nothing about the file format strictly requires one.

## Writing a CSV File

The `csv` module's `writer` takes a file object and writes one row at a time, as a list, correctly handling commas and quoting for you.

```python
import csv

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "quantity", "price"])
    writer.writerow(["T-shirt", 2, 350])
    writer.writerow(["Mug", 1, 150])
    writer.writerow(["Badge", 5, 50])

with open("sales.csv", "r") as file:
    print(file.read())
```

The `newline=""` argument prevents the `csv` module from writing extra blank lines on some operating systems; it is a small, easy-to-forget detail worth simply including by habit every time you open a file for CSV writing.

## Reading a CSV File

`csv.reader` reads a file back, handing you each row as a list of strings.

```csv file=sales.csv
item,quantity,price
T-shirt,2,350
Mug,1,150
Badge,5,50
```

```python with=sales.csv
import csv

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Output:

```
['item', 'quantity', 'price']
['T-shirt', '2', '350']
['Mug', '1', '150']
['Badge', '5', '50']
```

Notice every value comes back as a string, even `quantity` and `price`, which looked like numbers in the file. CSV itself has no concept of types, only text, so converting "2" to an actual `int` with `int(row[1])` is your responsibility, exactly the type-conversion habit from the data types unit.

## Reading Into Dictionaries: DictReader

`csv.DictReader` reads each row directly into a dictionary, using the header row as the keys automatically, which is often far more readable than tracking column positions by number.

```python with=sales.csv
import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["item"], "x", row["quantity"], "at", row["price"])
```

Output:

```
T-shirt x 2 at 350
Mug x 1 at 150
Badge x 5 at 50
```

`row["item"]` reads far more clearly than `row[0]` would, exactly the same readability argument that favoured dictionaries over plain lists, back in the sets and dictionaries unit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/07_csv_dictreader_dictwriter.png)


## Writing From Dictionaries: DictWriter

`csv.DictWriter` is the matching counterpart, writing a list of dictionaries out as proper CSV rows, with the header row specified once up front.

```python
import csv

sales = [
    {"item": "T-shirt", "quantity": 2, "price": 350},
    {"item": "Mug", "quantity": 1, "price": 150},
]

with open("sales.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "quantity", "price"])
    writer.writeheader()
    writer.writerows(sales)

with open("sales.csv", "r") as file:
    print(file.read())
```

`fieldnames` tells the writer the exact column order, `writeheader()` writes that header row once, and `writerows()` writes every dictionary in the list as its own row, matching each dictionary's keys to the correct column.

## CSV Tools at a Glance

| Tool | Reads or Writes | Row Shape |
|---|---|---|
| `csv.reader(file)` | Reads | Each row as a list of strings |
| `csv.writer(file)` | Writes | Each row written from a list |
| `csv.DictReader(file)` | Reads | Each row as a dictionary, keyed by header |
| `csv.DictWriter(file, fieldnames=...)` | Writes | Each row written from a dictionary |

## Your Turn: Total the Sales From a CSV

```python with=sales.csv
import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    total_revenue = 0
    for row in reader:
        total_revenue += int(row["quantity"]) * int(row["price"])

print("Total revenue:", total_revenue)    # 2*350 + 1*150 + 5*50 = 1100
```

Notice the explicit `int(...)` conversions on every value pulled from the row, a reminder that everything read from CSV starts out as text, no matter how numeric it looks.

## Conclusion

CSV files store rows of comma-separated values, with `csv.reader` and `csv.writer` handling plain list-shaped rows, and `csv.DictReader` and `csv.DictWriter` handling rows as dictionaries keyed by a header, both correctly managing the format's real-world quirks far more reliably than splitting strings by hand. Every value read from a CSV file arrives as text and needs explicit conversion before any arithmetic. CSV is excellent for flat, table-shaped data; the next lesson covers JSON, the format of choice for data with real structure and nesting, like the multi-stall reports from the sets and dictionaries unit.

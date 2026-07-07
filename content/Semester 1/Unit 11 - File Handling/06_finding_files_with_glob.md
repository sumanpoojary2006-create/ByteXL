## Introduction

The fest ran for three days, and Tara's `reports` folder now holds `day1_sales.txt`, `day2_sales.txt`, and `day3_sales.txt`, alongside a handful of unrelated notes she also dropped in there. She wants every sales report, and only the sales reports, without typing each exact filename by hand, and definitely without that approach breaking the moment a fourth day gets added next year.

This is exactly what pattern matching against filenames is for, using wildcard characters to describe a shape a filename should match, rather than naming every file individually. Python's `glob` module, and `pathlib`'s own built-in `.glob()` method, both do exactly this.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/06_glob_pattern_matching_files.png)

## The Wildcard: *

The asterisk, `*`, in a glob pattern matches any sequence of characters, standing in for "anything at all" in that part of the filename.

```python
from pathlib import Path

reports_folder = Path("reports")
reports_folder.mkdir(exist_ok=True)
(reports_folder / "day1_sales.txt").write_text("Total: 4500\n")
(reports_folder / "day2_sales.txt").write_text("Total: 5200\n")
(reports_folder / "day3_sales.txt").write_text("Total: 3900\n")

sales_files = list(reports_folder.glob("day*_sales.txt"))
print(sales_files)    # the three day*_sales.txt files, in some order
```

`day*_sales.txt` matches `day1_sales.txt`, `day2_sales.txt`, `day3_sales.txt`, and would just as happily match a future `day4_sales.txt`, because the `*` absorbs whatever digit, or digits, sits in that position, without Tara ever needing to know in advance how many days there will be.

## Matching Any File of a Given Type

A very common pattern matches every file with a particular extension, regardless of its name.

```python
from pathlib import Path

reports_folder = Path("reports")
reports_folder.mkdir(exist_ok=True)
(reports_folder / "day1_sales.csv").write_text("item,total\nT-shirt,4500\n")
(reports_folder / "day2_sales.csv").write_text("item,total\nMug,3200\n")
(reports_folder / "notes.txt").write_text("Not a CSV\n")

all_csv_files = list(Path("reports").glob("*.csv"))
print(all_csv_files)    # only the two .csv files, not notes.txt
```

`*.csv` matches any filename at all, as long as it ends in `.csv`, exactly the "I do not care about the name, only the type" question this pattern answers directly.

## The glob Module's Function Form

The standalone `glob` module offers the same matching as a plain function, returning filenames as strings rather than `Path` objects, useful when you are not otherwise using `pathlib`.

```python
import glob
from pathlib import Path

reports_folder = Path("reports")
reports_folder.mkdir(exist_ok=True)
(reports_folder / "day1_sales.txt").write_text("Total: 4500\n")
(reports_folder / "day2_sales.txt").write_text("Total: 5200\n")
(reports_folder / "day3_sales.txt").write_text("Total: 3900\n")

sales_files = sorted(glob.glob("reports/day*_sales.txt"))
print(sales_files)    # ['reports/day1_sales.txt', 'reports/day2_sales.txt', 'reports/day3_sales.txt']
```

Both forms answer the same question; `Path.glob()` fits naturally once you are already working with `Path` objects from the last lesson, while `glob.glob()` is the older, string-based form you will also see often in other people's code.

## Searching Subfolders Too: **

A double asterisk, `**`, matches across any number of nested subfolders, not just the files directly inside one folder.

```python
from pathlib import Path

# Create a small tree to search through
Path("data").mkdir(exist_ok=True)
Path("data/logs").mkdir(exist_ok=True)
Path("data/notes.txt").write_text("Top-level note\n")
Path("data/logs/day1.txt").write_text("Log entry 1\n")
Path("data/logs/day2.txt").write_text("Log entry 2\n")

all_txt_anywhere = sorted(Path("data").glob("**/*.txt"))
print(all_txt_anywhere)    # notes.txt and both log files, across all levels
```

This finds every `.txt` file anywhere underneath the current folder, including inside subfolders of subfolders, which a plain single `*` would not reach, since a single `*` only matches within one folder level at a time.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/06_glob_recursive_pattern.png)


## Wildcard Patterns at a Glance

| Pattern | Matches |
|---|---|
| `*.csv` | Any filename ending in `.csv`, in this folder |
| `day*_sales.txt` | Any filename starting with `day`, then anything, then ending in `_sales.txt` |
| `**/*.txt` | Any `.txt` file, in this folder or any subfolder beneath it |

## Why This Matters

Hard-coding a list of exact filenames works exactly until the data changes shape, a new day gets added, a file gets renamed, a folder gains an extra subfolder, at which point every hard-coded list needs manual updating, and it is easy to forget. Pattern matching describes the shape you actually care about once, and correctly keeps working as real files come and go around it.

## Your Turn: Gather Every Sales Report

```python
from pathlib import Path

reports_folder = Path("reports")
reports_folder.mkdir(exist_ok=True)
(reports_folder / "day1_sales.txt").write_text("Total: 4500\n")
(reports_folder / "day2_sales.txt").write_text("Total: 5200\n")
(reports_folder / "notes.txt").write_text("Remember to thank the volunteers\n")

sales_files = sorted(reports_folder.glob("day*_sales.txt"))
for file in sales_files:
    print(file.name, "->", file.read_text().strip())
```

Notice `notes.txt`, despite sitting in the very same folder, never matches `day*_sales.txt`, and so it is correctly left out of the loop entirely.

## Conclusion

A glob pattern describes the shape of filenames you want, using `*` to match any sequence of characters within one folder level and `**` to also reach into subfolders, letting you gather exactly the files you need without knowing their exact names or count in advance. `Path.glob()` and the standalone `glob.glob()` answer the same question, the first returning `Path` objects, the second plain strings. With the ability to find and read text files reliably, the next two lessons turn to two specific, structured file formats used constantly in real programs: CSV and JSON.

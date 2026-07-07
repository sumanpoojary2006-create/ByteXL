## Introduction

The fest ran for three days, and Tara's `reports` folder now holds `day1_sales.txt`, `day2_sales.txt`, and `day3_sales.txt`, alongside a handful of unrelated notes she also dropped in there. She wants every sales report, and only the sales reports, without typing each exact filename by hand, and definitely without that approach breaking the moment a fourth day gets added next year.

This is exactly what pattern matching against filenames is for, using wildcard characters to describe a shape a filename should match, rather than naming every file individually. Python's `glob` module, and `pathlib`'s own built-in `.glob()` method, both do exactly this.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/06_glob_pattern_matching_files.png)

## The Wildcard: *

The asterisk, `*`, in a glob pattern matches any sequence of characters, standing in for "anything at all" in that part of the filename.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2ZpbmRpbmdfZmlsZXNfd2l0aF9nbG9iIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxucmVwb3J0c19mb2xkZXIgPSBQYXRoKFwicmVwb3J0c1wiKVxucmVwb3J0c19mb2xkZXIubWtkaXIoZXhpc3Rfb2s9VHJ1ZSlcbihyZXBvcnRzX2ZvbGRlciAvIFwiZGF5MV9zYWxlcy50eHRcIikud3JpdGVfdGV4dChcIlRvdGFsOiA0NTAwXFxuXCIpXG4ocmVwb3J0c19mb2xkZXIgLyBcImRheTJfc2FsZXMudHh0XCIpLndyaXRlX3RleHQoXCJUb3RhbDogNTIwMFxcblwiKVxuKHJlcG9ydHNfZm9sZGVyIC8gXCJkYXkzX3NhbGVzLnR4dFwiKS53cml0ZV90ZXh0KFwiVG90YWw6IDM5MDBcXG5cIilcblxuc2FsZXNfZmlsZXMgPSBsaXN0KHJlcG9ydHNfZm9sZGVyLmdsb2IoXCJkYXkqX3NhbGVzLnR4dFwiKSlcbnByaW50KHNhbGVzX2ZpbGVzKSAgICAjIHRoZSB0aHJlZSBkYXkqX3NhbGVzLnR4dCBmaWxlcywgaW4gc29tZSBvcmRlciJ9"
 width="100%"
></iframe>

`day*_sales.txt` matches `day1_sales.txt`, `day2_sales.txt`, `day3_sales.txt`, and would just as happily match a future `day4_sales.txt`, because the `*` absorbs whatever digit, or digits, sits in that position, without Tara ever needing to know in advance how many days there will be.

## Matching Any File of a Given Type

A very common pattern matches every file with a particular extension, regardless of its name.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2ZpbmRpbmdfZmlsZXNfd2l0aF9nbG9iIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuYWxsX2Nzdl9maWxlcyA9IGxpc3QoUGF0aChcInJlcG9ydHNcIikuZ2xvYihcIiouY3N2XCIpKVxucHJpbnQoYWxsX2Nzdl9maWxlcykifQ"
 width="100%"
></iframe>

`*.csv` matches any filename at all, as long as it ends in `.csv`, exactly the "I do not care about the name, only the type" question this pattern answers directly.

## The glob Module's Function Form

The standalone `glob` module offers the same matching as a plain function, returning filenames as strings rather than `Path` objects, useful when you are not otherwise using `pathlib`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2ZpbmRpbmdfZmlsZXNfd2l0aF9nbG9iIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgZ2xvYlxuXG5zYWxlc19maWxlcyA9IGdsb2IuZ2xvYihcInJlcG9ydHMvZGF5Kl9zYWxlcy50eHRcIilcbnByaW50KHNhbGVzX2ZpbGVzKSAgICAjIFsncmVwb3J0cy9kYXkxX3NhbGVzLnR4dCcsICdyZXBvcnRzL2RheTJfc2FsZXMudHh0JywgJ3JlcG9ydHMvZGF5M19zYWxlcy50eHQnXSJ9"
 width="100%"
></iframe>

Both forms answer the same question; `Path.glob()` fits naturally once you are already working with `Path` objects from the last lesson, while `glob.glob()` is the older, string-based form you will also see often in other people's code.

## Searching Subfolders Too: **

A double asterisk, `**`, matches across any number of nested subfolders, not just the files directly inside one folder.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2ZpbmRpbmdfZmlsZXNfd2l0aF9nbG9iIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuYWxsX3R4dF9hbnl3aGVyZSA9IGxpc3QoUGF0aChcIi5cIikuZ2xvYihcIioqLyoudHh0XCIpKVxucHJpbnQoYWxsX3R4dF9hbnl3aGVyZSkifQ"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2ZpbmRpbmdfZmlsZXNfd2l0aF9nbG9iIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxucmVwb3J0c19mb2xkZXIgPSBQYXRoKFwicmVwb3J0c1wiKVxucmVwb3J0c19mb2xkZXIubWtkaXIoZXhpc3Rfb2s9VHJ1ZSlcbihyZXBvcnRzX2ZvbGRlciAvIFwiZGF5MV9zYWxlcy50eHRcIikud3JpdGVfdGV4dChcIlRvdGFsOiA0NTAwXFxuXCIpXG4ocmVwb3J0c19mb2xkZXIgLyBcImRheTJfc2FsZXMudHh0XCIpLndyaXRlX3RleHQoXCJUb3RhbDogNTIwMFxcblwiKVxuKHJlcG9ydHNfZm9sZGVyIC8gXCJub3Rlcy50eHRcIikud3JpdGVfdGV4dChcIlJlbWVtYmVyIHRvIHRoYW5rIHRoZSB2b2x1bnRlZXJzXFxuXCIpXG5cbnNhbGVzX2ZpbGVzID0gc29ydGVkKHJlcG9ydHNfZm9sZGVyLmdsb2IoXCJkYXkqX3NhbGVzLnR4dFwiKSlcbmZvciBmaWxlIGluIHNhbGVzX2ZpbGVzOlxuICAgIHByaW50KGZpbGUubmFtZSwgXCItPlwiLCBmaWxlLnJlYWRfdGV4dCgpLnN0cmlwKCkpIn0"
 width="100%"
></iframe>

Notice `notes.txt`, despite sitting in the very same folder, never matches `day*_sales.txt`, and so it is correctly left out of the loop entirely.

## Conclusion

A glob pattern describes the shape of filenames you want, using `*` to match any sequence of characters within one folder level and `**` to also reach into subfolders, letting you gather exactly the files you need without knowing their exact names or count in advance. `Path.glob()` and the standalone `glob.glob()` answer the same question, the first returning `Path` objects, the second plain strings. With the ability to find and read text files reliably, the next two lessons turn to two specific, structured file formats used constantly in real programs: CSV and JSON.

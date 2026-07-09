## Introduction

Meera runs the online ordering system for a chain of five restaurants, and the `restaurants` table she inherited is a mess of typing habits:

- Some branch names are in all caps because a manager once left caps lock on.
- Some values have trailing spaces from a copy-paste out of a spreadsheet.
- The app needs a single clean display line like "Spice Route - Koramangala" built out of two separate columns.

None of this needs a new column or a data-entry fix from head office. It needs SQL to reshape the text on the way out, using a set of built-in **string functions** that every relational database ships with.

## Joining Text Together

The `restaurants` table stores a branch name and a locality in separate columns, but the delivery app wants them shown as one combined string.

```postgresql file=restaurants.sql
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    branch_name TEXT,
    locality TEXT,
    manager_email TEXT
);

INSERT INTO restaurants (restaurant_id, branch_name, locality, manager_email) VALUES
(1, 'Spice Route', 'Koramangala', '  RAVI.KUMAR@SPICEROUTE.COM  '),
(2, 'SPICE ROUTE', 'Indiranagar', 'anita.rao@spiceroute.com'),
(3, 'Curry Leaf', 'Whitefield', 'sunil.d@curryleaf.com'),
(4, 'curry leaf', 'HSR Layout', '  priya.n@curryleaf.com'),
(5, 'Tandoor Express', 'Jayanagar', 'kiran.m@tandoorexpress.com  ');
```

```postgresql with=restaurants.sql
SELECT CONCAT(branch_name, ' - ', locality) AS display_name
FROM restaurants;
```

`CONCAT` glues its arguments together into one string, and the literal `' - '` in the middle inserts a separator between the two column values. Meera now has exactly the label the app's restaurant list needs, without touching the underlying columns.

## Fixing Inconsistent Case

The `branch_name` column has the same restaurant stored two different ways: "Spice Route" and "SPICE ROUTE" are meant to be the same branch, but a case-sensitive grouping or comparison would treat them as different values. `UPPER` and `LOWER` force text into one case so comparisons and grouping stop caring about how someone originally typed it.

```postgresql with=restaurants.sql
SELECT branch_name, UPPER(branch_name) AS shout_case, LOWER(branch_name) AS quiet_case
FROM restaurants;
```

For a report grouped by restaurant name, applying `LOWER(branch_name)` to every row before comparing means "Spice Route" and "SPICE ROUTE" collapse into a single group instead of two. Standardizing case at query time is often faster than tracking down and fixing every inconsistent row in the source table.

## Trimming Stray Whitespace

The `manager_email` column has a worse problem: some values have leading or trailing spaces, likely left over from a spreadsheet import. A space at the end of an email address makes `WHERE manager_email = 'ravi.kumar@spiceroute.com'` fail to match, even though the value looks identical on screen.

```postgresql with=restaurants.sql
SELECT manager_email, TRIM(manager_email) AS cleaned_email, LENGTH(manager_email) AS raw_length, LENGTH(TRIM(manager_email)) AS clean_length
FROM restaurants
WHERE restaurant_id IN (1, 4, 5);
```

`TRIM` removes whitespace from both ends of a string, and `LENGTH` counts characters, which is how Meera confirmed the raw column had extra characters an eyeball check could not catch. Comparing `raw_length` against `clean_length` for each row makes the hidden whitespace visible instead of invisible.

## Pulling Out Part of a String

Meera also needs just the domain of each manager's email, to check which restaurants still use the old `curryleaf.com` address before a rebrand. `SUBSTRING` extracts a piece of a string given a starting position and, optionally, a length.

```postgresql with=restaurants.sql
SELECT manager_email,
       SUBSTRING(TRIM(manager_email) FROM POSITION('@' IN TRIM(manager_email)) + 1) AS domain
FROM restaurants;
```

`POSITION('@' IN ...)` finds where the `@` sits in the cleaned email, and `SUBSTRING ... FROM` starts pulling characters one position after it, giving back everything from the domain onward. Wrapping the argument in `TRIM` first matters here too, since a stray trailing space would otherwise show up glued onto the domain.

## Before and After, Side by Side

Lining up a few raw values against their cleaned results makes the transformation concrete:

| Raw value | Function applied | Cleaned result |
|---|---|---|
| `'SPICE ROUTE'` | `LOWER(branch_name)` | `'spice route'` |
| `'  RAVI.KUMAR@SPICEROUTE.COM  '` | `LOWER(TRIM(manager_email))` | `'ravi.kumar@spiceroute.com'` |
| `'  priya.n@curryleaf.com'` | `TRIM(manager_email)` | `'priya.n@curryleaf.com'` |

## String Functions at a Glance

| Function | Purpose | Example |
|---|---|---|
| `CONCAT(a, b, ...)` | Join strings into one | `CONCAT(branch_name, ' - ', locality)` |
| `UPPER(text)` / `LOWER(text)` | Force a consistent case | `LOWER(branch_name)` |
| `TRIM(text)` | Remove leading/trailing whitespace | `TRIM(manager_email)` |
| `LENGTH(text)` | Count characters | `LENGTH(branch_name)` |
| `SUBSTRING(text FROM start FOR length)` | Extract part of a string | `SUBSTRING(email FROM 1 FOR 5)` |

## Your Turn

Head office wants a cleaned-up manager directory: one column with the branch name in title case is out of scope for now, but they do want the trimmed, lowercase email for every restaurant, aliased as `contact_email`. Write that query against the `restaurants` table above.

```postgresql with=restaurants.sql
-- Write your query below
```

If your query is `SELECT LOWER(TRIM(manager_email)) AS contact_email FROM restaurants;`, every address now reads the same clean way regardless of how it was originally typed.

## Conclusion

String functions let a query reshape text as it leaves the table, joining columns together, normalizing case, stripping stray whitespace, and pulling out just the substring that matters, all without ever editing the stored data. Meera's restaurant list, manager directory, and domain check all came from the same five rows of raw data, just viewed through different functions. Text is only one kind of data a table holds, and numbers need their own set of tools next.

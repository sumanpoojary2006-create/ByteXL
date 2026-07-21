## Introduction

Meera runs the online ordering system for a chain of five restaurants, and the `restaurants` table she inherited is a mess of typing habits:

- Some branch names are in all caps because a manager once left caps lock on.
- Some values have trailing spaces from a copy-paste out of a spreadsheet.
- The app needs a single clean display line like "Spice Route - Koramangala" built out of two separate columns.

None of this needs a new column or a data-entry fix from head office. It needs SQL to reshape the text on the way out, using a set of built-in **string functions** that every relational database ships with.

![CONCAT joining branch name and locality into one restaurant display name](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_concat_branch_locality_display_name.png)

**Definition:** String functions let a query reshape text as it leaves the table, joining columns together, normalizing case, stripping stray whitespace, and pulling out just the substring that matters, all without ever editing the stored data.

## Joining Text Together

The `restaurants` table stores a branch name and a locality in separate columns, but the delivery app wants them shown as one combined string.

Before transforming anything, inspect the five source rows:

| restaurant_id | branch_name | locality | manager_email |
| ------------: | --------------- | ------------ | --------------------------------- |
| 1 | Spice Route | Koramangala | `  RAVI.KUMAR@SPICEROUTE.COM  ` |
| 2 | SPICE ROUTE | Indiranagar | `anita.rao@spiceroute.com` |
| 3 | Curry Leaf | Whitefield | `sunil.d@curryleaf.com` |
| 4 | curry leaf | HSR Layout | `  priya.n@curryleaf.com` |
| 5 | Tandoor Express | Jayanagar | `kiran.m@tandoorexpress.com  ` |

Meera wants a display label that combines each branch with its locality. The query is `SELECT CONCAT(branch_name, ' - ', locality) AS display_name FROM restaurants;`. `CONCAT` joins its arguments in order, while the literal `' - '` supplies the separator between the two stored values.

## Hands-On Practice: Build a Display Name

The OneCompiler exercise uses two files. `init.sql` creates and populates the visual `restaurants` table. The active query file contains only the string-function query being practised. Where a query does not include `ORDER BY`, the database may return the correct rows in a different order from the example output.

First, `init.sql` prepares the dataset:

```postgresql
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

Then the active query file creates the display names:

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakru5" 
 width="100%"
></iframe>

Expected output:

| display_name |
| ------------------------------- |
| Spice Route - Koramangala |
| SPICE ROUTE - Indiranagar |
| Curry Leaf - Whitefield |
| curry leaf - HSR Layout |
| Tandoor Express - Jayanagar |

The result contains one calculated column. The original `branch_name` and `locality` values remain unchanged because a string function transforms the query result, not the stored data.

## Fixing Inconsistent Case

- The `branch_name` column has the same restaurant stored two different ways: "Spice Route" and "SPICE ROUTE" are meant to be the same branch, but a case-sensitive grouping or comparison would treat them as different values.
- `UPPER` and `LOWER` force text into one case so comparisons and grouping stop caring about how someone originally typed it.

To compare both transformations, Meera uses `SELECT branch_name, UPPER(branch_name) AS shout_case, LOWER(branch_name) AS quiet_case FROM restaurants;`. The raw value remains visible beside its uppercase and lowercase forms.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaks6y" 
 width="100%"
></iframe>

Expected output:

| branch_name | shout_case | quiet_case |
| --------------- | --------------- | --------------- |
| Spice Route | SPICE ROUTE | spice route |
| SPICE ROUTE | SPICE ROUTE | spice route |
| Curry Leaf | CURRY LEAF | curry leaf |
| curry leaf | CURRY LEAF | curry leaf |
| Tandoor Express | TANDOOR EXPRESS | tandoor express |

- For a report grouped by restaurant name, applying `LOWER(branch_name)` to every row before comparing means "Spice Route" and "SPICE ROUTE" collapse into a single group instead of two.
- Standardizing case at query time is often faster than tracking down and fixing every inconsistent row in the source table.

## Trimming Stray Whitespace

The `manager_email` column has a worse problem: some values have leading or trailing spaces, likely left over from a spreadsheet import. A space at the end of an email address makes `WHERE manager_email = 'ravi.kumar@spiceroute.com'` fail to match, even though the value looks identical on screen.

Meera selects the three affected rows with `SELECT manager_email, TRIM(manager_email) AS cleaned_email, LENGTH(manager_email) AS raw_length, LENGTH(TRIM(manager_email)) AS clean_length FROM restaurants WHERE restaurant_id IN (1, 4, 5);`. The two length columns make otherwise invisible spaces measurable.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakssr" 
 width="100%"
></iframe>

Expected output:

| manager_email | cleaned_email | raw_length | clean_length |
| --------------------------------- | ----------------------------- | ---------: | -----------: |
| `  RAVI.KUMAR@SPICEROUTE.COM  ` | RAVI.KUMAR@SPICEROUTE.COM | 29 | 25 |
| `  priya.n@curryleaf.com` | priya.n@curryleaf.com | 23 | 21 |
| `kiran.m@tandoorexpress.com  ` | kiran.m@tandoorexpress.com | 28 | 26 |

- `TRIM` removes whitespace from both ends of a string, and `LENGTH` counts characters, which is how Meera confirmed the raw column had extra characters an eyeball check could not catch.
- Comparing `raw_length` against `clean_length` for each row makes the hidden whitespace visible instead of invisible.

![LOWER and TRIM cleaning a messy email into a normalized contact address](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_lower_trim_clean_email.png)

## Pulling Out Part of a String

Meera also needs just the domain of each manager's email, to check which restaurants still use the old `curryleaf.com` address before a rebrand. `SUBSTRING` extracts a piece of a string given a starting position and, optionally, a length. Her query is `SELECT manager_email, SUBSTRING(TRIM(manager_email) FROM POSITION('@' IN TRIM(manager_email)) + 1) AS domain FROM restaurants;`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakt6p" 
 width="100%"
></iframe>

Expected output:

| manager_email | domain |
| --------------------------------- | ------------------ |
| `  RAVI.KUMAR@SPICEROUTE.COM  ` | SPICEROUTE.COM |
| anita.rao@spiceroute.com | spiceroute.com |
| sunil.d@curryleaf.com | curryleaf.com |
| `  priya.n@curryleaf.com` | curryleaf.com |
| `kiran.m@tandoorexpress.com  ` | tandoorexpress.com |

- `POSITION('@' IN ...)` finds where the `@` sits in the cleaned email.
- `SUBSTRING ... FROM` starts one character after the `@`, returning the domain.
- Wrapping the argument in `TRIM` first matters here too, since a stray trailing space would otherwise show up glued onto the domain.

## Before and After, Side by Side

Lining up a few raw values against their cleaned results makes the transformation concrete:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Raw value</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function applied</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cleaned result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;SPICE ROUTE&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LOWER(branch_name)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;spice route&#x27;</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;  RAVI.KUMAR@SPICEROUTE.COM  &#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LOWER(TRIM(manager_email))</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;ravi.kumar@spiceroute.com&#x27;</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;  priya.n@curryleaf.com&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>TRIM(manager_email)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;priya.n@curryleaf.com&#x27;</code></td>
    </tr>
  </tbody>
</table>

## String Functions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CONCAT(a, b, ...)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Join strings into one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CONCAT(branch_name, &#x27; - &#x27;, locality)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>UPPER(text)</code> / <code>LOWER(text)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Force a consistent case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LOWER(branch_name)</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>TRIM(text)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove leading/trailing whitespace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>TRIM(manager_email)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LENGTH(text)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Count characters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LENGTH(branch_name)</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SUBSTRING(text FROM start FOR length)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract part of a string</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SUBSTRING(email FROM 1 FOR 5)</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

Head office wants a cleaned-up manager directory: one column with the branch name in title case is out of scope for now, but they do want the trimmed, lowercase email for every restaurant, aliased as `contact_email`. Write that query against the `restaurants` table above.

The required transformation is `LOWER(TRIM(manager_email))`: `TRIM` removes the outer spaces first, and `LOWER` then normalizes the remaining address.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaktfg" 
 width="100%"
></iframe>

If your query is `SELECT LOWER(TRIM(manager_email)) AS contact_email FROM restaurants;`, every address now reads the same clean way regardless of how it was originally typed.

Expected output:

| contact_email |
| ----------------------------- |
| ravi.kumar@spiceroute.com |
| anita.rao@spiceroute.com |
| sunil.d@curryleaf.com |
| priya.n@curryleaf.com |
| kiran.m@tandoorexpress.com |

## Conclusion

String functions let a query reshape text as it leaves the table, joining columns together, normalizing case, stripping stray whitespace, and pulling out just the substring that matters, all without ever editing the stored data. Meera's restaurant list, manager directory, and domain check all came from the same five rows of raw data, just viewed through different functions.

Text is only one kind of data a table holds, and numbers need their own set of tools next.

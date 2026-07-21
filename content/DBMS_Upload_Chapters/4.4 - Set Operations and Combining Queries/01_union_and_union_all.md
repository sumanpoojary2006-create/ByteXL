## Introduction

Tanvi runs marketing for a retail brand that sells both through its website and through physical stores, and each channel keeps its own customer list in a separate table, `online_customers` and `store_customers`. For an upcoming sale announcement, she needs one single mailing list combining names and emails from both tables, with no regard for which channel a customer originally came from.

This is not a join, since she is not trying to match rows between the two tables and widen them with extra columns; she wants to stack the rows from both tables on top of each other into one combined list. SQL's **`UNION`** and **`UNION ALL`** are built for exactly that: combining the results of two queries vertically.

**Definition:** `UNION` and `UNION ALL` combine the results of two or more queries vertically into one result set, with `UNION` removing exact duplicates and `UNION ALL` keeping every row, both requiring the same number and type of columns from each query involved.

![Intro visual for union and union all](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_union_and_union_all_actual3d_adec609b.png)

## Stacking Two Result Sets Into One

Both customer tables share the same shape, a name and an email, which is a requirement for combining them this way.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `online_customers`

| customer_name | email |
| --- | --- |
| Aditi Kulkarni | aditi.k@example.com |
| Rohan Das | rohan.das@example.com |
| Kavya Nair | kavya.nair@example.com |

### `store_customers`

| customer_name | email |
| --- | --- |
| Kavya Nair | kavya.nair@example.com |
| Imran Sheikh | imran.s@example.com |
| Neha Bhatt | neha.bhatt@example.com |

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

## Hands-On Setup: Prepare the Data

```postgresql
CREATE TABLE online_customers (
    customer_name TEXT,
    email TEXT
);

CREATE TABLE store_customers (
    customer_name TEXT,
    email TEXT
);

INSERT INTO online_customers (customer_name, email) VALUES
('Aditi Kulkarni', 'aditi.k@example.com'),
('Rohan Das', 'rohan.das@example.com'),
('Kavya Nair', 'kavya.nair@example.com');

INSERT INTO store_customers (customer_name, email) VALUES
('Kavya Nair', 'kavya.nair@example.com'),
('Imran Sheikh', 'imran.s@example.com'),
('Neha Bhatt', 'neha.bhatt@example.com');
```

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahsjw" 
 width="100%"
></iframe>

Expected output:

| customer_name | email |
| --- | --- |
| Aditi Kulkarni | aditi.k@example.com |
| Imran Sheikh | imran.s@example.com |
| Kavya Nair | kavya.nair@example.com |
| Neha Bhatt | neha.bhatt@example.com |
| Rohan Das | rohan.das@example.com |

`UNION` takes the result of the first `SELECT`, the result of the second `SELECT`, and stacks them into one combined result set:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">customer_name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">email</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aditi Kulkarni</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">aditi.k@example.com</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan Das</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">rohan.das@example.com</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kavya Nair</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">kavya.nair@example.com</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Imran Sheikh</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">imran.s@example.com</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neha Bhatt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">neha.bhatt@example.com</td>
    </tr>
  </tbody>
</table>

- Kavya Nair appears in both source tables, since she shops both online and in-store, but she only appears once in the combined output.
- `UNION` automatically removes exact duplicate rows across the two result sets, which is precisely the behavior Tanvi wants for a mailing list, since sending Kavya the same announcement twice would be an obvious mistake.

![UNION stacking two customer lists while removing an exact duplicate row](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_union_removes_duplicates.png)

## Keeping Duplicates with UNION ALL

Sometimes the duplicate itself is meaningful, not a mistake to clean up. If Tanvi instead wants to know exactly how many total customer records exist across both channels, including counting Kavya twice since she is genuinely a customer of both, `UNION ALL` keeps every row from both queries with no deduplication.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahsvp" 
 width="100%"
></iframe>

Expected output:

| customer_name | email |
| --- | --- |
| Aditi Kulkarni | aditi.k@example.com |
| Rohan Das | rohan.das@example.com |
| Kavya Nair | kavya.nair@example.com |
| Kavya Nair | kavya.nair@example.com |
| Imran Sheikh | imran.s@example.com |
| Neha Bhatt | neha.bhatt@example.com |

This returns 6 rows instead of 5, with Kavya Nair listed twice, once from each source table. `UNION ALL` is also faster than plain `UNION` in most databases, since checking for and removing duplicates takes real work. Two things follow from that:

- When duplicates genuinely do not matter for the question being asked, `UNION ALL` is the more accurate choice.
- It is also the more efficient one, since skipping the duplicate check saves real work.

![UNION ALL stacking two customer lists while keeping duplicate rows](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_union_all_keeps_duplicates.png)

## The Column Rules UNION Requires

- Both `SELECT` statements combined with `UNION` or `UNION ALL` must return the same number of columns, in compatible data types, in the same order.
- The column names in the final result come from the first `SELECT` statement, regardless of what the second one calls them.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaht6h" 
 width="100%"
></iframe>

Expected output:

| person | contact_email | source |
| --- | --- | --- |
| Aditi Kulkarni | aditi.k@example.com | online |
| Rohan Das | rohan.das@example.com | online |
| Kavya Nair | kavya.nair@example.com | online |
| Kavya Nair | kavya.nair@example.com | store |
| Imran Sheikh | imran.s@example.com | store |
| Neha Bhatt | neha.bhatt@example.com | store |

- Here, a literal string, `'online'` or `'store'`, is added as a third column to each query, letting Tanvi see which channel every row originally came from, even after the two result sets are combined.
- This is a common pattern for tagging the origin of each row once separate sources get merged into one list.
- Note that the final column headers, `person` and `contact_email`, come from the first `SELECT`'s aliases; the second `SELECT`'s column names are ignored entirely for labeling purposes, though the values themselves still combine correctly, since only the position and type of each column matters, not its name.

## Sorting a Combined Result

`ORDER BY` can only appear once, at the very end of the combined query, and it sorts the final stacked result rather than either query individually.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahtgw" 
 width="100%"
></iframe>

Expected output:

| customer_name | email |
| --- | --- |
| Aditi Kulkarni | aditi.k@example.com |
| Imran Sheikh | imran.s@example.com |
| Kavya Nair | kavya.nair@example.com |
| Neha Bhatt | neha.bhatt@example.com |
| Rohan Das | rohan.das@example.com |

Placing `ORDER BY` after both `SELECT` statements sorts the entire combined list of 5 unique customers alphabetically by name, which is the standard way to present a merged mailing list for review before it goes out.

## UNION vs. UNION ALL at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operator</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Duplicates</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>UNION</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removed automatically</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A clean, deduplicated combined list</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>UNION ALL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Counting every record, or when duplicates cannot occur anyway</td>
    </tr>
  </tbody>
</table>

## Your Turn

Tanvi wants a single list of every unique email address across both channels, with no names, sorted alphabetically. Write that query against `online_customers` and `store_customers` above.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahttc" 
 width="100%"
></iframe>

If your query is `SELECT email FROM online_customers UNION SELECT email FROM store_customers ORDER BY email;`, it returns 5 unique email addresses, with `kavya.nair@example.com` appearing only once despite being present in both source tables.


Expected output for the practice query:

| email |
| --- |
| aditi.k@example.com |
| imran.s@example.com |
| kavya.nair@example.com |
| neha.bhatt@example.com |
| rohan.das@example.com |

## Conclusion

`UNION` and `UNION ALL` combine the results of two or more queries vertically into one result set, with `UNION` removing exact duplicates and `UNION ALL` keeping every row, both requiring the same number and type of columns from each query involved.

Tanvi can now build a single clean mailing list or a full record count across two separate customer tables.

`UNION` finds everything from either source; the next lesson covers finding only what two result sets have in common, or only what one has that the other does not.

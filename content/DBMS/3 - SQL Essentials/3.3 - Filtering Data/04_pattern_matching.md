## Introduction

Siddharth has been asked to pull together a list of everyone still using their college-issued email address, ahead of a migration to a new mail provider. He does not have a fixed value to compare against; he cannot write `email = 'something'` because the local part of every address is different, it is only the ending that is shared.

What he needs is a way to match a partial shape of text rather than an exact value, and that is what **pattern matching** with `LIKE` is for.

![LIKE with percent wildcard matching any email that ends in campusmail.edu](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_like_percent_email_pattern.png)

**Definition:** `LIKE` turns `WHERE` from a tool that only recognises exact values into one that can recognise the shape of text.

## Matching Part of a String with LIKE

`LIKE` compares a text `column` against a pattern instead of a fixed value. The pattern can include two special wildcard characters:

- `%` stands in for any number of characters, including zero.
- `_` stands in for exactly one character.

The `students` `table` holds this data:

| student_id | full_name | email | city | phone | joined_on |
| ---------- | ------------- | ----------------------------- | --------- | ---------- | ---------- |
| 1 | Omkar Rane | omkar.rane@campusmail.edu | Bengaluru | 9845011111 | 2025-01-10 |
| 2 | Neha Sharma | neha.sharma@campusmail.edu | Mysuru | *NULL* | 2025-01-12 |
| 3 | Varun Nair | varun.nair@gmail.com | Chennai | 9845022222 | 2025-01-15 |
| 4 | Siddharth Rao | siddharth.rao@campusmail.edu | Hyderabad | 9845033333 | 2025-01-18 |
| 5 | Yusuf Khan | yusuf.khan@gmail.com | Pune | *NULL* | 2025-01-20 |
| 6 | Ishita Menon | ishita.menon@campusmail.edu | Bengaluru | 9845044444 | 2025-01-22 |
| 7 | Rahul Verma | rahul.verma@gmail.com | Chennai | 9845055555 | 2025-01-25 |
| 8 | Sanya Iyer | sanya.iyer@campusmail.edu | Mysuru | *NULL* | 2025-01-28 |

Siddharth needs addresses that end with the college domain. The query is `SELECT full_name, email FROM students WHERE email LIKE '%campusmail.edu';`. The leading `%` allows any text before `campusmail.edu`, while the rest of the pattern requires that exact ending.

For hands-on practice, `init.sql` creates and populates only the visual `students` table:

```postgresql file=init.sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    city TEXT,
    phone TEXT,
    joined_on DATE
);

INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES
(1, 'Omkar Rane', 'omkar.rane@campusmail.edu', 'Bengaluru', '9845011111', '2025-01-10'),
(2, 'Neha Sharma', 'neha.sharma@campusmail.edu', 'Mysuru', NULL, '2025-01-12'),
(3, 'Varun Nair', 'varun.nair@gmail.com', 'Chennai', '9845022222', '2025-01-15'),
(4, 'Siddharth Rao', 'siddharth.rao@campusmail.edu', 'Hyderabad', '9845033333', '2025-01-18'),
(5, 'Yusuf Khan', 'yusuf.khan@gmail.com', 'Pune', NULL, '2025-01-20'),
(6, 'Ishita Menon', 'ishita.menon@campusmail.edu', 'Bengaluru', '9845044444', '2025-01-22'),
(7, 'Rahul Verma', 'rahul.verma@gmail.com', 'Chennai', '9845055555', '2025-01-25'),
(8, 'Sanya Iyer', 'sanya.iyer@campusmail.edu', 'Mysuru', NULL, '2025-01-28');
```

The active query file contains only the pattern-matching query:

```postgresql with=init.sql
SELECT full_name, email
FROM students
WHERE email LIKE '%campusmail.edu';
```

Expected output:

| full_name | email |
| ------------- | ----------------------------- |
| Omkar Rane | omkar.rane@campusmail.edu |
| Neha Sharma | neha.sharma@campusmail.edu |
| Siddharth Rao | siddharth.rao@campusmail.edu |
| Ishita Menon | ishita.menon@campusmail.edu |
| Sanya Iyer | sanya.iyer@campusmail.edu |

- Five students come back: Omkar Rane, Neha Sharma, Siddharth Rao, Ishita Menon, and Sanya Iyer.
- The `%` before `campusmail.edu` means "anything at all can appear before this text," so the pattern matches regardless of what the local part of the address looks like, as long as the address ends with `campusmail.edu`.
- Varun Nair, Yusuf Khan, and Rahul Verma are left out, since their addresses end with `gmail.com` instead.

## Anchoring a Pattern to the Start or Middle

`%` is not limited to the end of a pattern. Placing it at the start checks a suffix, placing it in the middle checks that two fragments both appear in order, and leaving it off one side anchors the match to that side.

```postgresql with=init.sql
SELECT full_name
FROM students
WHERE full_name LIKE 'S%';
```

Expected output:

| full_name |
| ------------- |
| Siddharth Rao |
| Sanya Iyer |

- This returns Siddharth Rao and Sanya Iyer, the two students whose name begins with the letter S.
- The trailing `%` in `'S%'` is doing the real work here: it is what allows any amount of text to follow the S, matching a name of any length as long as it starts with that letter.
- `LIKE` never adds a wildcard on its own, so dropping that `%` and writing `full_name LIKE 'S'` would demand an exact, single-character match and return nothing at all, since no student's full name is just the letter S by itself.

## Matching Exactly One Character with _

`_` is stricter than `%`. It stands for exactly one character, no more and no fewer, which makes it useful when you know the shape of the text but not one specific letter in it.

```postgresql with=init.sql
SELECT full_name
FROM students
WHERE full_name LIKE '_a%';
```

Expected output:

| full_name |
| ----------- |
| Varun Nair |
| Rahul Verma |
| Sanya Iyer |

- Three names come back: Varun Nair, Rahul Verma, and Sanya Iyer.
- The pattern says "any single character, followed by the letter a, followed by anything," and all three names happen to have `a` as their second letter.
- Compare this with `full_name LIKE 'a%'`, which would look for names starting with `a` itself, a completely different and, in this data, empty result.

![LIKE patterns showing percent for many characters and underscore for exactly one character](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_like_percent_and_underscore_wildcards.png)

## Case-Insensitive Matching with ILIKE

`LIKE` is case-sensitive by default, so a pattern written in uppercase will not match lowercase text. PostgreSQL offers `ILIKE` as a convenience that matches regardless of letter case, which is handy when you are not sure how something was typed in.

```postgresql with=init.sql
SELECT full_name, email
FROM students
WHERE email ILIKE '%GMAIL%';
```

Expected output:

| full_name | email |
| ----------- | --------------------- |
| Varun Nair | varun.nair@gmail.com |
| Yusuf Khan | yusuf.khan@gmail.com |
| Rahul Verma | rahul.verma@gmail.com |

- This still returns Varun Nair, Yusuf Khan, and Rahul Verma, even though the pattern is written in uppercase and the stored addresses are all lowercase.
- Swapping `ILIKE` for `LIKE` here with the same uppercase pattern would return nothing at all, since `LIKE` treats `GMAIL` and `gmail` as different text entirely.
- `ILIKE` is specific to PostgreSQL; other `database` systems handle case-insensitive matching differently, so it is worth knowing it is a PostgreSQL convenience rather than a universal SQL feature.

## Pattern Matching at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symbol or keyword</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Matches</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Matches values like</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>%</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any number of characters, including none</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;%edu&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>omkar.rane@campusmail.edu</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>_</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exactly one character</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;_a%&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Sanya</code>, <code>Varun</code>, <code>Rahul</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LIKE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Case-sensitive pattern match</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;S%&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Siddharth</code>, <code>Sanya</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ILIKE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Case-insensitive pattern match (PostgreSQL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;%GMAIL%&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">any casing of &quot;gmail&quot;</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write a `query` that finds every student whose email address contains the text "verma", regardless of where it appears in the address.

```postgresql with=init.sql
SELECT full_name, email
FROM students
WHERE email LIKE '%verma%';
```

Expected output:

| full_name | email |
| ----------- | ---------------------- |
| Rahul Verma | rahul.verma@gmail.com |

This should return exactly one `row`, Rahul Verma, since his email address is the only one containing that fragment anywhere in it. Try replacing `%verma%` with just `verma%` and notice the result becomes empty, since that pattern demands the address start with "verma" rather than merely contain it.

## Conclusion

`LIKE` turns `WHERE` from a tool that only recognises exact values into one that can recognise the shape of text. `%` stands for a stretch of any length, `_` stands for one character, and PostgreSQL's `ILIKE` ignores letter case. Siddharth can therefore retrieve every college-issued address with `WHERE email LIKE '%campusmail.edu'` without knowing each complete address beforehand.

Text is not the only place where an exact comparison falls short. Some `columns` hold no known value at all, and working with that absence requires SQL's special `NULL` rules.

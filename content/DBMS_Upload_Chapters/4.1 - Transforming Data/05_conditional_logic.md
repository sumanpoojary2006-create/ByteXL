## Introduction

Farah builds reports for a small gym chain, and the `members` `table` stores each member's total visits this month as a plain number. The front desk does not want to stare at raw visit counts; they want members labeled "Highly Active," "Active," or "At Risk" so staff can decide who needs a check-in call.

That label does not exist anywhere in the `table`, it depends on a rule applied to the visit count, and different visit counts should produce different labels within the very same `query`. This is exactly what SQL's **`CASE`** expression is for: choosing between several possible outputs based on a condition, `row` by `row`.

**Definition:** `CASE` turns a raw `column` value into whatever label, category, or calculated result a business question actually needs, checking conditions in order and returning the first match, with `ELSE` as a safety net for everything else.

![Intro visual for conditional logic](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_conditional_logic.png)

## Writing a Simple CASE Expression

The `members` `table` tracks each member's visits for the current month.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `members`

| member_id | full_name | visits_this_month | membership_type |
| --- | --- | --- | --- |
| 1 | Karan Malhotra | 18 | premium |
| 2 | Nisha Verma | 4 | standard |
| 3 | Aakash Jain | 11 | standard |
| 4 | Ritu Sharma | 0 | premium |
| 5 | Yusuf Ali | 9 | basic |

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

## Hands-On Setup: Prepare the Data

```postgresql
CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    full_name TEXT,
    visits_this_month INTEGER,
    membership_type TEXT
);

INSERT INTO members (member_id, full_name, visits_this_month, membership_type) VALUES
(1, 'Karan Malhotra', 18, 'premium'),
(2, 'Nisha Verma', 4, 'standard'),
(3, 'Aakash Jain', 11, 'standard'),
(4, 'Ritu Sharma', 0, 'premium'),
(5, 'Yusuf Ali', 9, 'basic');
```

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaktv5" 
 width="100%"
></iframe>

Expected output:

| full_name | visits_this_month | activity_label |
| --- | --- | --- |
| Karan Malhotra | 18 | Highly Active |
| Nisha Verma | 4 | Active |
| Aakash Jain | 11 | Active |
| Ritu Sharma | 0 | At Risk |
| Yusuf Ali | 9 | Active |

- `CASE` checks each `WHEN` condition in order, top to bottom, and returns the value after the first `THEN` whose condition is true.
- If none of the `WHEN` conditions match, it falls back to whatever follows `ELSE`.
- Karan's 18 visits satisfy the first condition and get "Highly Active," while Ritu's 0 visits fail both `WHEN` checks and land on "At Risk" through the `ELSE` branch.

![CASE assigning activity labels by checking conditions in order](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_case_first_matching_condition.png)

Walking through every member against the rule shows exactly which branch each one lands on:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Member</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Visits</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">First true condition</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Label</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Karan Malhotra</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">18</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&gt;= 12</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Highly Active</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nisha Verma</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&gt;= 4</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Active</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aakash Jain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&gt;= 4</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Active</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ritu Sharma</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">none, falls to <code>ELSE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At Risk</td>
    </tr>
  </tbody>
</table>

## Why Order Inside CASE Matters

The conditions are evaluated top to bottom, and the first true one wins, so the order they are written in changes the result. Writing the loosest condition first would break the logic above.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaku6v" 
 width="100%"
></iframe>

Expected output:

| full_name | visits_this_month | mislabeled |
| --- | --- | --- |
| Karan Malhotra | 18 | Active |
| Nisha Verma | 4 | Active |
| Aakash Jain | 11 | Active |
| Ritu Sharma | 0 | At Risk |
| Yusuf Ali | 9 | Active |

Run this version and Karan, with 18 visits, gets labeled "Active" instead of "Highly Active," because `visits_this_month >= 4` is checked first and is already true at 18 visits, so the `CASE` expression stops right there and never reaches the "Highly Active" condition. The rule to remember is simple: put the most specific or most restrictive condition first.

## Branching on a Column Value Instead of a Range

`CASE` does not only compare numbers against thresholds; it can also branch on an exact match, which suits the `membership_type` `column` here.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakufq" 
 width="100%"
></iframe>

Expected output:

| full_name | membership_type | plan_description |
| --- | --- | --- |
| Karan Malhotra | premium | Full access, all branches |
| Nisha Verma | standard | Full access, home branch only |
| Aakash Jain | standard | Full access, home branch only |
| Ritu Sharma | premium | Full access, all branches |
| Yusuf Ali | basic | Gym floor only, no classes |

This shorter form, `CASE membership_type WHEN 'premium' THEN ...`, compares the `column` directly against each listed value instead of writing out a full condition each time:

- Use it when every branch is a simple equality check against the same `column`.
- Fall back to the earlier `CASE WHEN condition THEN ...` form whenever a condition is more than a plain equality.

## Combining CASE with a Calculation

`CASE` expressions can be used anywhere a normal value is allowed, including inside arithmetic, which lets Farah calculate a loyalty bonus that depends on both membership type and visit count in one pass.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakutp" 
 width="100%"
></iframe>

Expected output:

| full_name | loyalty_points |
| --- | --- |
| Karan Malhotra | 180 |
| Nisha Verma | 20 |
| Aakash Jain | 55 |
| Ritu Sharma | 0 |
| Yusuf Ali | 18 |

The `CASE` expression resolves to a plain number for each `row`, either 10, 5, or 2 depending on membership type, and that number is then multiplied directly by `visits_this_month`, producing a single loyalty-points `column` without a second `query` or a temporary `table`.

![CASE choosing a membership multiplier before calculating loyalty points](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_case_multiplier_loyalty_points.png)

## Your Turn

The gym wants a discount eligibility flag: members with fewer than 5 visits this month get the label "Send Offer," everyone else gets "No Offer Needed." Write that `query` against the `members` `table` above, aliasing the result as `offer_status`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakv64" 
 width="100%"
></iframe>

If your `query` uses `CASE WHEN visits_this_month < 5 THEN 'Send Offer' ELSE 'No Offer Needed' END AS offer_status`, only Nisha and Ritu will be flagged for an offer, matching their visit counts of 4 and 0.


Expected output for the practice query:

| full_name | offer_status |
| --- | --- |
| Karan Malhotra | No Offer Needed |
| Nisha Verma | Send Offer |
| Aakash Jain | No Offer Needed |
| Ritu Sharma | Send Offer |
| Yusuf Ali | No Offer Needed |

## Conclusion

`CASE` turns a raw `column` value into whatever label, category, or calculated result a business question actually needs, checking conditions in order and returning the first match, with `ELSE` as a safety net for everything else.

Farah used it to label activity levels, describe membership plans in plain language, and calculate loyalty points, all from two `columns` of raw data.

Individual `rows` transformed this way are useful, but many real questions need entire groups of `rows` summarized into one number, which is where aggregation begins.

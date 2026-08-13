## Introduction

Leela's next report tracks month-over-month growth: for each salesperson's monthly total, how much did it change compared to the previous month? Answering this means comparing a row to a different row, specifically, whichever row comes immediately before it once the data is ordered by month. A plain `SELECT` has no built-in way to reach into a neighboring row like that.

SQL's **offset functions**, `LAG` and `LEAD`, are `window functions` purpose-built for exactly this: pulling a value from a row a fixed number of positions before or after the current one, within an ordered window.

**Definition:** `LAG` and `LEAD` pull a value from a neighboring row, before or after the current one within an ordered window, turning row-to-row comparisons like month-over-month change into a straightforward calculation on a single row instead of a self join across two.

![Intro visual for offset functions lag and lead](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_offset_functions_lag_and_lead_actual3d_a329031c.png)

## Looking Back at the Previous Row with LAG

The `monthly_sales` table holds one row per salesperson per month.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `monthly_sales`

| salesperson | sale_month | total_amount |
| --- | --- | --- |
| Nikhil Rao | 2025-03-01 | 22000.00 |
| Nikhil Rao | 2025-04-01 | 25500.00 |
| Nikhil Rao | 2025-05-01 | 21000.00 |
| Nikhil Rao | 2025-06-01 | 29700.00 |
| Sana Fatima | 2025-05-01 | 18000.00 |
| Sana Fatima | 2025-06-01 | 21000.00 |

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE monthly_sales (
    salesperson TEXT,
    sale_month DATE,
    total_amount NUMERIC(10, 2)
);

INSERT INTO monthly_sales (salesperson, sale_month, total_amount) VALUES
('Nikhil Rao', '2025-03-01', 22000.00),
('Nikhil Rao', '2025-04-01', 25500.00),
('Nikhil Rao', '2025-05-01', 21000.00),
('Nikhil Rao', '2025-06-01', 29700.00),
('Sana Fatima', '2025-05-01', 18000.00),
('Sana Fatima', '2025-06-01', 21000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaghe4" 
 width="100%"
></iframe>

`LAG(total_amount)` reaches back one row within each salesperson's partition, ordered by month, and returns that prior row's `total_amount`:

Expected output:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">salesperson</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">sale_month</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">total_amount</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">previous_month</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nikhil Rao</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2025-03-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">22000.00</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nikhil Rao</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2025-04-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">25500.00</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">22000.00</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nikhil Rao</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2025-05-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21000.00</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">25500.00</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nikhil Rao</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2025-06-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">29700.00</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21000.00</td>
    </tr>
  </tbody>
</table>

Nikhil's April row shows 22000.00 as its `previous_month`, exactly March's total. His March row, having nothing before it in the partition, shows `NULL`, since there is no earlier row for `LAG` to reach.

![LAG reaching backward from the current row to the previous month](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_lag_previous_row.png)

## Calculating Change Using LAG

With the previous month's value sitting in the same row, calculating growth is now a plain subtraction.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaghq3" 
 width="100%"
></iframe>

Expected output:

| salesperson | sale_month | total_amount | change_from_last_month |
| --- | --- | --- | --- |
| Nikhil Rao | 2025-03-01 | 22000.00 | NULL |
| Nikhil Rao | 2025-04-01 | 25500.00 | 3500.00 |
| Nikhil Rao | 2025-05-01 | 21000.00 | -4500.00 |
| Nikhil Rao | 2025-06-01 | 29700.00 | 8700.00 |
| Sana Fatima | 2025-05-01 | 18000.00 | NULL |
| Sana Fatima | 2025-06-01 | 21000.00 | 3000.00 |

Nikhil's April change is 3500.00, an increase, and his May change is -4500.00, a drop, computed directly from two values that now live on the same logical row thanks to `LAG`. Before `window functions`, this same calculation would have needed a self join matching each row to "the row for the same salesperson, one month earlier," a noticeably more complex query for the same result.

## Looking Ahead to the Next Row with LEAD

`LEAD` is the mirror of `LAG`, reaching forward to a later row instead of an earlier one.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaghyx" 
 width="100%"
></iframe>

Expected output:

| salesperson | sale_month | total_amount | next_month |
| --- | --- | --- | --- |
| Nikhil Rao | 2025-03-01 | 22000.00 | 25500.00 |
| Nikhil Rao | 2025-04-01 | 25500.00 | 21000.00 |
| Nikhil Rao | 2025-05-01 | 21000.00 | 29700.00 |
| Nikhil Rao | 2025-06-01 | 29700.00 | NULL |
| Sana Fatima | 2025-05-01 | 18000.00 | 21000.00 |
| Sana Fatima | 2025-06-01 | 21000.00 | NULL |

- Nikhil's March row now shows 25500.00 as `next_month`, April's total, and his last row, June, shows `NULL`, since there is no later row in his partition for `LEAD` to reach forward into.
- `LEAD` is useful for questions phrased the other way around, such as "what did this salesperson do right after this particular month."

![LEAD reaching forward from the current row to the next month](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_lead_next_row.png)

## Reaching More Than One Row Away

Both `LAG` and `LEAD` accept two optional extra arguments:

- A second argument specifying how many rows to look back or forward, defaulting to 1 when left out.
- A third argument specifying what to return when there is no such row, instead of `NULL`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagj9w" 
 width="100%"
></iframe>

Expected output:

| salesperson | sale_month | total_amount | two_months_ago |
| --- | --- | --- | --- |
| Nikhil Rao | 2025-03-01 | 22000.00 | 0.00 |
| Nikhil Rao | 2025-04-01 | 25500.00 | 0.00 |
| Nikhil Rao | 2025-05-01 | 21000.00 | 22000.00 |
| Nikhil Rao | 2025-06-01 | 29700.00 | 25500.00 |
| Sana Fatima | 2025-05-01 | 18000.00 | 0.00 |
| Sana Fatima | 2025-06-01 | 21000.00 | 0.00 |

`LAG(total_amount, 2, 0)` reaches back two rows instead of one, and supplies 0 instead of `NULL` whenever there is no row that far back, which is useful when a downstream calculation needs a real number rather than a `NULL` to work with.

## LAG and LEAD at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Direction</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Default offset</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Default fallback</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LAG(col)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backward, to an earlier row</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1 row</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LEAD(col)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forward, to a later row</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1 row</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LAG(col, n)</code> / <code>LEAD(col, n)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">n rows in that direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">n</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LAG(col, n, default)</code> / <code>LEAD(col, n, default)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">n rows, with a fallback value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">n</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>default</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

Leela wants to flag any month where a salesperson's total dropped compared to the previous month. Write a query against `monthly_sales` above that shows `salesperson`, `sale_month`, `total_amount`, and a `trend` column reading either "up" or "down" based on `LAG`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagjkw" 
 width="100%"
></iframe>

One valid answer wraps the `LAG` comparison in a `CASE` expression: `CASE WHEN total_amount < LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend`. This correctly labels Nikhil's May row as "down" and every other row as "up." The first row of each salesperson has nothing to compare against, so it defaults to "up" through the `ELSE` branch.

Expected output:

| salesperson | sale_month | total_amount | trend |
| --- | --- | --- | --- |
| Nikhil Rao | 2025-03-01 | 22000.00 | up |
| Nikhil Rao | 2025-04-01 | 25500.00 | up |
| Nikhil Rao | 2025-05-01 | 21000.00 | down |
| Nikhil Rao | 2025-06-01 | 29700.00 | up |
| Sana Fatima | 2025-05-01 | 18000.00 | up |
| Sana Fatima | 2025-06-01 | 21000.00 | up |

## Conclusion

`LAG` and `LEAD` pull a value from a neighboring row, before or after the current one within an ordered window, turning row-to-row comparisons like month-over-month change into a straightforward calculation on a single row instead of a self join across two. Leela can now show growth, decline, and trend directly in her monthly report. Comparing to one neighboring row is useful, but some calculations need to look across a whole range of surrounding rows at once, which is where window frames come in.

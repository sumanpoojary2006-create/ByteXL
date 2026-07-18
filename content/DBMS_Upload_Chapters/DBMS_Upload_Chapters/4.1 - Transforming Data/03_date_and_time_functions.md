## Introduction

Divya runs the front desk software for a small clinic, and the `appointments` `table` logs every visit with a timestamp. Doctors keep asking questions that a raw timestamp cannot answer by itself:

- "How many days ago was this patient's last visit?"
- "Which appointments were booked in the last 7 days?"
- "Just give me the hour of day patients tend to show up, not the full date."

A timestamp is a single value, but the questions above need it pulled apart, compared, or measured against right now. SQL's **date and time `functions`** exist for exactly this kind of work.

**Definition:** Date and time `functions` turn a single stored timestamp into whatever shape a question needs: `NOW()` and `CURRENT_DATE` for a reference point, interval arithmetic for shifting dates forward or measuring spans, and `EXTRACT` for pulling out just a weekday or an hour.

## Getting the Current Moment

Every date calculation eventually needs to know what "now" is, so that is the natural starting point.

The query `SELECT NOW() AS current_timestamp_value, CURRENT_DATE AS current_date_value;` returns the database server's current timestamp and its current calendar date. Because both values are evaluated when the query runs, they naturally change over time.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `appointments`

| appointment_id | patient_name | visit_time |
| --- | --- | --- |
| 1 | Rohit Nair | 2025-01-10 09:15:00 |
| 2 | Sanya Kapoor | 2025-02-03 14:30:00 |
| 3 | Faisal Ahmed | 2025-02-20 11:00:00 |
| 4 | Lakshmi Iyer | 2025-03-05 16:45:00 |
| 5 | Devika Menon | 2025-03-18 10:00:00 |

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

## Hands-On Setup: Prepare the Data

```postgresql
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    visit_time TIMESTAMP
);

INSERT INTO appointments (appointment_id, patient_name, visit_time) VALUES
(1, 'Rohit Nair', '2025-01-10 09:15:00'),
(2, 'Sanya Kapoor', '2025-02-03 14:30:00'),
(3, 'Faisal Ahmed', '2025-02-20 11:00:00'),
(4, 'Lakshmi Iyer', '2025-03-05 16:45:00'),
(5, 'Devika Menon', '2025-03-18 10:00:00');
```

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakwxk" 
 width="100%"
></iframe>

Expected output shape:

| current_timestamp_value | current_date_value |
| --- | --- |
| Current timestamp at execution time | Current date at execution time |

`NOW()` returns the exact current timestamp the `database` sees at `query` time, down to the second, while `CURRENT_DATE` returns just today's date with no time component. Divya will use `NOW()` as the anchor point for every "how long ago" question the clinic asks.

![NOW, CURRENT_DATE, and INTERVAL using the current moment to suggest a follow-up date](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_now_current_date_interval_followup.png)

## Doing Arithmetic on Dates

With a reference point available, Divya can measure how far in the past each appointment falls, or shift a date forward to schedule a follow-up.

The query below calculates a readable age from `NOW()` and adds a seven-day interval to every stored visit. The age changes with the execution date, but the suggested follow-up is always exactly seven days after the visit.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakx9h" 
 width="100%"
></iframe>

Expected output:

| patient_name | visit_time | time_since_visit | suggested_followup |
| --- | --- | --- | --- |
| Rohit Nair | 2025-01-10 09:15:00 | Calculated from current time | 2025-01-17 09:15:00 |
| Sanya Kapoor | 2025-02-03 14:30:00 | Calculated from current time | 2025-02-10 14:30:00 |
| Faisal Ahmed | 2025-02-20 11:00:00 | Calculated from current time | 2025-02-27 11:00:00 |
| Lakshmi Iyer | 2025-03-05 16:45:00 | Calculated from current time | 2025-03-12 16:45:00 |
| Devika Menon | 2025-03-18 10:00:00 | Calculated from current time | 2025-03-25 10:00:00 |

- `AGE(later, earlier)` returns a readable span, such as "11 months 2 days," which is friendlier for a doctor to scan than a raw number of seconds.
- Adding an `INTERVAL` directly to a timestamp, like `+ INTERVAL '7 days'`, produces a new timestamp shifted forward by exactly that span, which is how Divya generates a suggested follow-up date for every patient in one `query`.

## Extracting Just One Part of a Date

Sometimes the full timestamp is more detail than the question needs. Divya wants to know which weekday and which hour patients tend to book, without caring about the specific date at all.

Her query uses `EXTRACT(DOW FROM visit_time)` for PostgreSQL's Sunday-to-Saturday number and `EXTRACT(HOUR FROM visit_time)` for the 24-hour clock value.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakxky" 
 width="100%"
></iframe>

Expected output:

| patient_name | visit_time | day_of_week_number | hour_of_day |
| --- | --- | ---: | ---: |
| Rohit Nair | 2025-01-10 09:15:00 | 5 | 9 |
| Sanya Kapoor | 2025-02-03 14:30:00 | 1 | 14 |
| Faisal Ahmed | 2025-02-20 11:00:00 | 4 | 11 |
| Lakshmi Iyer | 2025-03-05 16:45:00 | 3 | 16 |
| Devika Menon | 2025-03-18 10:00:00 | 2 | 10 |

- `EXTRACT(field FROM timestamp)` pulls a single component out of a date or timestamp.
- `DOW` (day of week) returns 0 for Sunday through 6 for Saturday, and `HOUR` returns the hour in 24-hour format.
- Grouping later by `EXTRACT(HOUR FROM visit_time)` is how Divya would eventually find the clinic's busiest hour, one topic ahead once grouping is introduced.

![EXTRACT pulling hour and day-of-week parts from a visit timestamp](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_extract_timestamp_parts.png)

## Comparing Two Dates Directly

Divya also wants a simple flag: was a given appointment booked in the last 30 days from today, or is it older than that? Subtracting two dates in most `databases` returns the number of days between them as a plain number.

The query converts each timestamp to a date, subtracts it from `CURRENT_DATE`, and orders the calculated day counts from smallest to largest. The exact numbers increase as time passes.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakxwk" 
 width="100%"
></iframe>

Expected output shape:

| patient_name | visit_time | days_since_visit |
| --- | --- | ---: |
| Devika Menon | 2025-03-18 10:00:00 | Calculated from current date |
| Lakshmi Iyer | 2025-03-05 16:45:00 | Calculated from current date |
| Faisal Ahmed | 2025-02-20 11:00:00 | Calculated from current date |
| Sanya Kapoor | 2025-02-03 14:30:00 | Calculated from current date |
| Rohit Nair | 2025-01-10 09:15:00 | Calculated from current date |

- `visit_time::DATE` converts the timestamp to a plain date first, dropping the time-of-day portion so the subtraction returns a clean whole number of days rather than a mixed interval.
- Ordering by that computed `column` puts the most recent visits first, which is exactly the list the front desk checks each morning.

## EXTRACT Fields Worth Knowing

`EXTRACT` accepts several different field names besides `DOW` and `HOUR`, each pulling out a different slice of a timestamp:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Field</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Returns</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example on <code>2025-03-18 10:00:00</code></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>YEAR</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The calendar year</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>2025</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>MONTH</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The month number, 1 to 12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>3</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>DAY</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The day of the month</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>18</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>DOW</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Day of week, 0 (Sunday) to 6 (Saturday)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>2</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>HOUR</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The hour, 0 to 23</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>10</code></td>
    </tr>
  </tbody>
</table>

## Date and Time Functions at a Glance

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NOW()</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Current timestamp</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NOW()</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CURRENT_DATE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Current date, no time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CURRENT_DATE</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>AGE(a, b)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable span between two timestamps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>AGE(NOW(), visit_time)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>date + INTERVAL &#x27;...&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shift a date forward or backward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>visit_time + INTERVAL &#x27;7 days&#x27;</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>EXTRACT(field FROM date)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull out one component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>EXTRACT(HOUR FROM visit_time)</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

The clinic wants a simple recall list: patient name and visit date for every appointment more than 60 days old, counting from today, ordered with the oldest visit first. Write that `query` against the `appointments` `table` above.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaky8m" 
 width="100%"
></iframe>

If your `query` filters with `WHERE CURRENT_DATE - visit_time::DATE > 60` and orders by `visit_time`, the earliest visits in the `table` surface first, which is exactly who the clinic should be calling back.

Expected output depends on the date the query is run. Once all five sample visits are more than 60 days old, the ordered result is:

| patient_name | visit_time |
| --- | --- |
| Rohit Nair | 2025-01-10 09:15:00 |
| Sanya Kapoor | 2025-02-03 14:30:00 |
| Faisal Ahmed | 2025-02-20 11:00:00 |
| Lakshmi Iyer | 2025-03-05 16:45:00 |
| Devika Menon | 2025-03-18 10:00:00 |

## Conclusion

Date and time `functions` turn a single stored timestamp into whatever shape a question needs: `NOW()` and `CURRENT_DATE` for a reference point, interval arithmetic for shifting dates forward or measuring spans, and `EXTRACT` for pulling out just a weekday or an hour. Divya answered four different scheduling questions from one `column` of raw timestamps. Not every gap in a `table` is a wrong value, though.

Some of it is genuinely missing data, and that needs its own handling.

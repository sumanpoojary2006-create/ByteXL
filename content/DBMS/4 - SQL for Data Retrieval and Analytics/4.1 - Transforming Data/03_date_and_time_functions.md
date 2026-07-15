## Introduction

Divya runs the front desk software for a small clinic, and the `appointments` `table` logs every visit with a timestamp. Doctors keep asking questions that a raw timestamp cannot answer by itself:

- "How many days ago was this patient's last visit?"
- "Which appointments were booked in the last 7 days?"
- "Just give me the hour of day patients tend to show up, not the full date."

A timestamp is a single value, but the questions above need it pulled apart, compared, or measured against right now. SQL's **date and time `functions`** exist for exactly this kind of work.

## Getting the Current Moment

Every date calculation eventually needs to know what "now" is, so that is the natural starting point.

```postgresql file=appointments.sql
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

```postgresql with=appointments.sql
SELECT NOW() AS current_timestamp_value, CURRENT_DATE AS current_date_value;
```

`NOW()` returns the exact current timestamp the `database` sees at `query` time, down to the second, while `CURRENT_DATE` returns just today's date with no time component. Divya will use `NOW()` as the anchor point for every "how long ago" question the clinic asks.

![NOW, CURRENT_DATE, and INTERVAL using the current moment to suggest a follow-up date](images/05_now_current_date_interval_followup.png)

## Doing Arithmetic on Dates

With a reference point available, Divya can measure how far in the past each appointment falls, or shift a date forward to schedule a follow-up.

```postgresql with=appointments.sql
SELECT patient_name, visit_time,
       AGE(NOW(), visit_time) AS time_since_visit,
       visit_time + INTERVAL '7 days' AS suggested_followup
FROM appointments;
```

- `AGE(later, earlier)` returns a readable span, such as "11 months 2 days," which is friendlier for a doctor to scan than a raw number of seconds.
- Adding an `INTERVAL` directly to a timestamp, like `+ INTERVAL '7 days'`, produces a new timestamp shifted forward by exactly that span, which is how Divya generates a suggested follow-up date for every patient in one `query`.

## Extracting Just One Part of a Date

Sometimes the full timestamp is more detail than the question needs. Divya wants to know which weekday and which hour patients tend to book, without caring about the specific date at all.

```postgresql with=appointments.sql
SELECT patient_name, visit_time,
       EXTRACT(DOW FROM visit_time) AS day_of_week_number,
       EXTRACT(HOUR FROM visit_time) AS hour_of_day
FROM appointments;
```

- `EXTRACT(field FROM timestamp)` pulls a single component out of a date or timestamp.
- `DOW` (day of week) returns 0 for Sunday through 6 for Saturday, and `HOUR` returns the hour in 24-hour format.
- Grouping later by `EXTRACT(HOUR FROM visit_time)` is how Divya would eventually find the clinic's busiest hour, one topic ahead once grouping is introduced.

![EXTRACT pulling hour and day-of-week parts from a visit timestamp](images/06_extract_timestamp_parts.png)

## Comparing Two Dates Directly

Divya also wants a simple flag: was a given appointment booked in the last 30 days from today, or is it older than that? Subtracting two dates in most `databases` returns the number of days between them as a plain number.

```postgresql with=appointments.sql
SELECT patient_name, visit_time,
       CURRENT_DATE - visit_time::DATE AS days_since_visit
FROM appointments
ORDER BY days_since_visit;
```

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

```postgresql with=appointments.sql
-- Write your query below
```

If your `query` filters with `WHERE CURRENT_DATE - visit_time::DATE > 60` and orders by `visit_time`, the earliest visits in the `table` surface first, which is exactly who the clinic should be calling back.

## Conclusion

Date and time `functions` turn a single stored timestamp into whatever shape a question needs: `NOW()` and `CURRENT_DATE` for a reference point, interval arithmetic for shifting dates forward or measuring spans, and `EXTRACT` for pulling out just a weekday or an hour. Divya answered four different scheduling questions from one `column` of raw timestamps. Not every gap in a `table` is a wrong value, though.

Some of it is genuinely missing data, and that needs its own handling.

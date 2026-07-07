## Introduction

Nadia's library system tracks when books are borrowed and when they are due back. Her homegrown date arithmetic subtracted integers from day numbers and crashed on the first day of a month (subtracting 14 days from March 1 does not give February 15 by simple subtraction). Her manager pointed her to the `datetime` module, which handles all calendar arithmetic correctly, including leap years, month boundaries, and time zones.

![A timeline showing date, datetime, timedelta, and timezone as building blocks: date for calendar days, datetime for exact moments, timedelta for durations, and timezone for offsets](images/04_datetime_module.png)

## The Three Core Types

`datetime` gives you three types that cover almost every date/time need:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-001-0bf94803ea.html"
 width="100%"
></iframe>

## Date Arithmetic with timedelta

`timedelta` is the key to correct date arithmetic. Add it to a `date` or `datetime` to move forward or backward in time:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-002-326a8f9f65.html"
 width="100%"
></iframe>

`date - date` produces a `timedelta`. Call `.days` on it to get the integer number of days.

## Parsing and Formatting Dates

Convert between strings and dates using `strptime` (parse) and `strftime` (format):

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-003-692cd163b3.html"
 width="100%"
></iframe>

Common format codes:

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | 2026 |
| `%m` | Month (01-12) | 07 |
| `%d` | Day (01-31) | 01 |
| `%H` | Hour 24h (00-23) | 14 |
| `%M` | Minute (00-59) | 30 |
| `%b` | Month name abbreviated | Jul |
| `%B` | Month name full | July |

## ISO 8601 Format

The ISO 8601 format (`YYYY-MM-DD`) is the safest for storing dates in files and databases:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-004-d4eca4b32b.html"
 width="100%"
></iframe>

`isoformat()` and `fromisoformat()` are the cleanest round-trip for dates that go into and come back from storage.

## Time Zones

By default, `datetime.now()` is "naive" -- it has no timezone information. For production systems that handle users in multiple time zones, use `datetime.now(tz=timezone.utc)` to get a timezone-aware datetime:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-005-2b53899978.html"
 width="100%"
></iframe>

For full time zone database support (named zones like "America/New_York"), install the third-party `zoneinfo` module (built into Python 3.9+) or `pytz`.

## The datetime Module at a Glance

| Type / Method | What it does |
|---|---|
| `date.today()` | Today's date (no time) |
| `datetime.now()` | Current local date and time |
| `timedelta(days=N)` | Duration of N days |
| `date + timedelta` | Move a date forward/backward |
| `date - date` | Duration between two dates |
| `datetime.strptime(s, fmt)` | Parse a string to datetime |
| `datetime.strftime(fmt)` | Format a datetime to string |
| `date.isoformat()` | `'YYYY-MM-DD'` string |
| `datetime.now(tz=timezone.utc)` | Timezone-aware UTC now |

## Your Turn

Write a function `overdue_report(records)` that takes a list of borrow records (each with `isbn`, `patron_id`, `borrow_date` as an ISO string, and `loan_days`), computes the due date, and returns a list of overdue records with the number of days overdue.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-04-datetime-module-006-d546f1762f.html"
 width="100%"
></iframe>

Pass `today` explicitly so the function is testable without depending on the current date.

## Conclusion

`datetime` provides three types: `date` for calendar days, `datetime` for exact moments, and `timedelta` for durations. Parsing uses `strptime`, formatting uses `strftime`, and ISO 8601 is the recommended storage format. Time-zone-aware datetimes prevent subtle bugs when users span multiple regions. The next lesson moves to `collections`, Python's toolkit for specialized data structures that go beyond basic lists and dictionaries.

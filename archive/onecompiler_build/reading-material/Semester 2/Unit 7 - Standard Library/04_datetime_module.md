## Introduction

Nadia's library system tracks when books are borrowed and when they are due back. Her homegrown date arithmetic subtracted integers from day numbers and crashed on the first day of a month (subtracting 14 days from March 1 does not give February 15 by simple subtraction). Her manager pointed her to the `datetime` module, which handles all calendar arithmetic correctly, including leap years, month boundaries, and time zones.

![A timeline showing date, datetime, timedelta, and timezone as building blocks: date for calendar days, datetime for exact moments, timedelta for durations, and timezone for offsets](images/04_datetime_module.png)

## The Three Core Types

`datetime` gives you three types that cover almost every date/time need:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZSwgZGF0ZXRpbWUsIHRpbWVkZWx0YVxuXG4jIGRhdGU6IGEgY2FsZW5kYXIgZGF5IChubyB0aW1lIGNvbXBvbmVudClcbnRvZGF5ID0gZGF0ZS50b2RheSgpXG5wcmludCh0b2RheSkgICAgICAgICAgIyBlLmcuIDIwMjYtMDctMDFcbnByaW50KHRvZGF5LnllYXIsIHRvZGF5Lm1vbnRoLCB0b2RheS5kYXkpICAjIDIwMjYgNyAxXG5cbiMgZGF0ZXRpbWU6IGEgc3BlY2lmaWMgbW9tZW50IGluIHRpbWVcbm5vdyA9IGRhdGV0aW1lLm5vdygpXG5wcmludChub3cpICAgICAgICAgICAgIyBlLmcuIDIwMjYtMDctMDEgMTQ6MjM6MDcuMTIzNDU2XG5cbiMgdGltZWRlbHRhOiBhIGR1cmF0aW9uXG50d29fd2Vla3MgPSB0aW1lZGVsdGEoZGF5cz0xNClcbnByaW50KHRvZGF5ICsgdHdvX3dlZWtzKSAgIyAyMDI2LTA3LTE1In0"
 width="100%"
></iframe>

## Date Arithmetic with timedelta

`timedelta` is the key to correct date arithmetic. Add it to a `date` or `datetime` to move forward or backward in time:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZSwgdGltZWRlbHRhXG5cbmJvcnJvd19kYXRlID0gZGF0ZSgyMDI2LCA2LCAyMClcbmxvYW5fcGVyaW9kID0gdGltZWRlbHRhKGRheXM9MjEpXG5kdWVfZGF0ZSA9IGJvcnJvd19kYXRlICsgbG9hbl9wZXJpb2RcbnByaW50KGZcIkR1ZToge2R1ZV9kYXRlfVwiKSAgICAjIDIwMjYtMDctMTFcblxuIyBEYXlzIG92ZXJkdWU6XG50b2RheSA9IGRhdGUoMjAyNiwgNywgMTUpXG5pZiB0b2RheSA-IGR1ZV9kYXRlOlxuICAgIG92ZXJkdWVfZGF5cyA9ICh0b2RheSAtIGR1ZV9kYXRlKS5kYXlzXG4gICAgcHJpbnQoZlwiT3ZlcmR1ZSBieSB7b3ZlcmR1ZV9kYXlzfSBkYXlzXCIpICAgIyA0IGRheXMifQ"
 width="100%"
></iframe>

`date - date` produces a `timedelta`. Call `.days` on it to get the integer number of days.

## Parsing and Formatting Dates

Convert between strings and dates using `strptime` (parse) and `strftime` (format):

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWVcblxuIyBQYXJzZSBhIHN0cmluZyBpbnRvIGEgZGF0ZXRpbWVcbnJhdyA9IFwiMjAyNi0wNy0wMVwiXG5wYXJzZWQgPSBkYXRldGltZS5zdHJwdGltZShyYXcsIFwiJVktJW0tJWRcIilcbnByaW50KHBhcnNlZCkgICAjIDIwMjYtMDctMDEgMDA6MDA6MDBcblxuIyBQYXJzZSBhIG1vcmUgY29tcGxleCBzdHJpbmdcbnJhdzIgPSBcIjAxIEp1bCAyMDI2IDE0OjMwXCJcbnBhcnNlZDIgPSBkYXRldGltZS5zdHJwdGltZShyYXcyLCBcIiVkICViICVZICVIOiVNXCIpXG5wcmludChwYXJzZWQyKSAgIyAyMDI2LTA3LTAxIDE0OjMwOjAwXG5cbiMgRm9ybWF0IGEgZGF0ZXRpbWUgYXMgYSBzdHJpbmdcbmZvcm1hdHRlZCA9IHBhcnNlZDIuc3RyZnRpbWUoXCIlQiAlZCwgJVkgYXQgJUk6JU0gJXBcIilcbnByaW50KGZvcm1hdHRlZCkgICAjIEp1bHkgMDEsIDIwMjYgYXQgMDI6MzAgUE0ifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZSwgZGF0ZXRpbWVcblxudG9kYXkgPSBkYXRlLnRvZGF5KClcbnByaW50KHRvZGF5Lmlzb2Zvcm1hdCgpKSAgICAgICAgICAgICMgJzIwMjYtMDctMDEnXG5cbm5vdyA9IGRhdGV0aW1lLm5vdygpXG5wcmludChub3cuaXNvZm9ybWF0KCkpICAgICAgICAgICAgICAjICcyMDI2LTA3LTAxVDE0OjIzOjA3LjEyMzQ1NidcbnByaW50KG5vdy5pc29mb3JtYXQoc2VwPVwiIFwiKSkgICAgICAgIyAnMjAyNi0wNy0wMSAxNDoyMzowNy4xMjM0NTYnXG5cbiMgUGFyc2UgSVNPIGZvcm1hdDpcbnBhcnNlZCA9IGRhdGUuZnJvbWlzb2Zvcm1hdChcIjIwMjYtMDctMDFcIilcbnByaW50KHBhcnNlZCkgICAgICAgICAgICAgICAgICAgICAgICMgMjAyNi0wNy0wMSJ9"
 width="100%"
></iframe>

`isoformat()` and `fromisoformat()` are the cleanest round-trip for dates that go into and come back from storage.

## Time Zones

By default, `datetime.now()` is "naive" -- it has no timezone information. For production systems that handle users in multiple time zones, use `datetime.now(tz=timezone.utc)` to get a timezone-aware datetime:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lLCB0aW1lZGVsdGFcblxuIyBVVEMgbm93ICh0aW1lem9uZS1hd2FyZSlcbm5vd191dGMgPSBkYXRldGltZS5ub3codHo9dGltZXpvbmUudXRjKVxucHJpbnQobm93X3V0YykgICAjIDIwMjYtMDctMDEgMDk6MjM6MDcuMTIzNDU2KzAwOjAwXG5cbiMgQ29udmVydCB0byBhIGZpeGVkIG9mZnNldFxuaXN0ID0gdGltZXpvbmUodGltZWRlbHRhKGhvdXJzPTUsIG1pbnV0ZXM9MzApKSAgICMgSW5kaWEgU3RhbmRhcmQgVGltZVxubm93X2lzdCA9IG5vd191dGMuYXN0aW1lem9uZShpc3QpXG5wcmludChub3dfaXN0KSAgICMgMjAyNi0wNy0wMSAxNDo1MzowNy4xMjM0NTYrMDU6MzAifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RhdGV0aW1lX21vZHVsZSBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZSwgdGltZWRlbHRhXG5cbmRlZiBvdmVyZHVlX3JlcG9ydChyZWNvcmRzLCB0b2RheT1Ob25lKTpcbiAgICB0b2RheSA9IHRvZGF5IG9yIGRhdGUudG9kYXkoKVxuICAgIG92ZXJkdWUgPSBbXVxuICAgIGZvciByZWNvcmQgaW4gcmVjb3JkczpcbiAgICAgICAgYm9ycm93ID0gZGF0ZS5mcm9taXNvZm9ybWF0KHJlY29yZFtcImJvcnJvd19kYXRlXCJdKVxuICAgICAgICBkdWUgPSBib3Jyb3cgKyB0aW1lZGVsdGEoZGF5cz1yZWNvcmRbXCJsb2FuX2RheXNcIl0pXG4gICAgICAgIGlmIHRvZGF5ID4gZHVlOlxuICAgICAgICAgICAgb3ZlcmR1ZS5hcHBlbmQoeyoqcmVjb3JkLCBcImRheXNfb3ZlcmR1ZVwiOiAodG9kYXkgLSBkdWUpLmRheXN9KVxuICAgIHJldHVybiBvdmVyZHVlXG5cbnJlY29yZHMgPSBbXG4gICAge1wiaXNiblwiOiBcIjk3OC0wMDFcIiwgXCJwYXRyb25faWRcIjogXCJQMDFcIiwgXCJib3Jyb3dfZGF0ZVwiOiBcIjIwMjYtMDYtMDFcIiwgXCJsb2FuX2RheXNcIjogMjF9LFxuICAgIHtcImlzYm5cIjogXCI5NzgtMDAyXCIsIFwicGF0cm9uX2lkXCI6IFwiUDAyXCIsIFwiYm9ycm93X2RhdGVcIjogXCIyMDI2LTA2LTIwXCIsIFwibG9hbl9kYXlzXCI6IDIxfSxcbl1cbnByaW50KG92ZXJkdWVfcmVwb3J0KHJlY29yZHMsIHRvZGF5PWRhdGUoMjAyNiwgNywgMSkpKSJ9"
 width="100%"
></iframe>

Pass `today` explicitly so the function is testable without depending on the current date.

## Conclusion

`datetime` provides three types: `date` for calendar days, `datetime` for exact moments, and `timedelta` for durations. Parsing uses `strptime`, formatting uses `strftime`, and ISO 8601 is the recommended storage format. Time-zone-aware datetimes prevent subtle bugs when users span multiple regions. The next lesson moves to `collections`, Python's toolkit for specialized data structures that go beyond basic lists and dictionaries.

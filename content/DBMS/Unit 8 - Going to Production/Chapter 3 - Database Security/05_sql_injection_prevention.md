## Introduction

The `prepared statements` lesson, back in the application-code chapter, briefly demonstrated what happens when untrusted input is pasted directly into a SQL string: a query's actual logic can be hijacked entirely. This attack has a name, **SQL injection**, and it remains one of the most common, most damaging vulnerabilities in real software, precisely because the mistake that causes it, building SQL by string concatenation, is so easy to write without realizing the danger. This lesson revisits the mechanism in more depth and lays out the full set of defenses, `prepared statements` as the primary one, backed by everything covered earlier in this chapter.

## A More Damaging Injection Example

The earlier example returned extra rows; a real injection can go much further, touching data the query was never meant to involve at all.

```postgresql file=injection_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');
```

```postgresql with=injection_demo.sql
-- Imagine application code building a query like this:
-- shipment_id_input = "1; DROP TABLE shipments; --"
-- sql_text = "SELECT * FROM shipments WHERE shipment_id = " + shipment_id_input
-- If the database allowed multiple statements per call, this would become:
-- SELECT * FROM shipments WHERE shipment_id = 1; DROP TABLE shipments; --
-- The semicolon ends the intended SELECT, DROP TABLE shipments is then run
-- as a completely separate, second statement, and -- comments out
-- whatever trailing text the original query template had left over.
SELECT * FROM shipments WHERE shipment_id = 1;
```

This is the severity that makes SQL injection so dangerous in practice. It is not limited to reading extra rows:

- It can delete, modify, or destroy data entirely.
- Depending on the database account's granted privileges, it can reach into tables the application was never designed to touch at all, exactly the blast radius the least-privilege lesson in this chapter warned about.

## Prepared Statements Prevent Injection by Construction

The core defense, already introduced in the application-code chapter, is worth restating precisely here: a `prepared statement` never lets user-supplied text become part of the query's structure, no matter what that text contains.

```postgresql with=injection_demo.sql
PREPARE get_shipment (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = $1;

EXECUTE get_shipment(1);
```

Because `$1` is a genuine parameter, not text pasted into a string, there is no possible value that could be supplied for it that would change the query's structure; a value like `1; DROP TABLE shipments; --` passed as this parameter would simply fail to match any `shipment_id`, since it would be compared, as a single piece of data, against an integer column, never interpreted as additional SQL syntax at all. This is why `prepared statements` are described as preventing injection "by construction," rather than by filtering or detecting dangerous input: the vulnerability has no path to exist in the first place.

## Input Validation Is a Second Layer, Not a Replacement

It might seem like carefully checking and sanitizing user input before building a query would be enough on its own. It is a reasonable additional layer, but it is not a reliable substitute for `prepared statements`, since it depends entirely on the validation logic anticipating every possible dangerous pattern, an approach that has repeatedly proven incomplete in real-world security history.

```postgresql with=injection_demo.sql
-- A validation-only approach, without prepared statements, might try to
-- reject any input containing a semicolon or the word "DROP":
-- if ";" in user_input or "DROP" in user_input.upper():
--     reject the request
-- This can still be bypassed by encoding, case variations, or SQL
-- constructs the validation logic simply did not anticipate.
-- Prepared statements avoid this arms race entirely, since the parameter
-- is never treated as SQL syntax regardless of its content.
SELECT * FROM shipments WHERE shipment_id = 1;
```

Input validation still has real value, rejecting obviously malformed input early, improving error messages, catching genuine mistakes, but it should never be relied upon as the sole defense against injection; that role belongs to `prepared statements`.

## Least Privilege as a Defense-in-Depth Layer

Even with `prepared statements` used everywhere, the least-privilege principle from earlier in this chapter provides a valuable second line of defense: if an injection vulnerability somehow still existed, the damage it could do is bounded by what the compromised database account was actually granted.

```postgresql with=injection_demo.sql
CREATE ROLE web_app WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT SELECT, INSERT ON shipments TO web_app;
```

A `web_app` `role` granted only `SELECT` and `INSERT` on `shipments`, with no `DELETE`, no `DROP` privilege, and no access to any other table, could not have actually executed the destructive `DROP TABLE shipments` attempted in the earlier example, even in a world where the injection itself had somehow succeeded, since that `role` was never granted the privilege to drop anything at all. This is exactly why layered defenses matter: prepared statements should make injection impossible in the first place, and `least privilege` limits the damage in case some other, unanticipated flaw ever slips through.

## SQL Injection Prevention at a Glance

| Defense | Role |
|---|---|
| Prepared statements / parameterized queries | Primary defense; makes injection structurally impossible |
| Input validation | Secondary layer; catches malformed input, not a substitute for parameterization |
| Least privilege | Defense in depth; bounds the damage if some other flaw is ever exploited |
| String concatenation into SQL | Never acceptable for any value that originates from outside the application's own trusted code |

## Your Turn

Rewrite the vulnerable, string-concatenation-style query from the beginning of this lesson as a safe, `prepared statement`, and explain in a comment exactly why the injected value can no longer change the query's behavior.

```postgresql with=injection_demo.sql
-- Write your prepared statement, execution, and comment below
```

`PREPARE safe_lookup (INTEGER) AS SELECT * FROM shipments WHERE shipment_id = $1;` followed by `EXECUTE safe_lookup(1);` is the safe rewrite; because `$1` is a typed parameter position, not a location where raw text is spliced into the SQL string, any value supplied for it, however maliciously crafted, is compared purely as data against `shipment_id`, with no way to introduce new SQL syntax into the statement at all.

## Conclusion

SQL injection happens when untrusted input is allowed to become part of a query's structure rather than staying confined to a value being compared or inserted, and prepared statements prevent this by construction, keeping structure and data permanently separate, with input validation and `least privilege` serving as valuable additional layers rather than substitutes for that primary defense. The final lesson in this chapter looks at what happens after a query has already run: recording who did what, and when.

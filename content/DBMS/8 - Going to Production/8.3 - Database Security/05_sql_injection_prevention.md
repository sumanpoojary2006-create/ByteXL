## Introduction

The `prepared statements` lesson, back in the application-code chapter, briefly demonstrated what happens when untrusted input is pasted directly into a SQL string: a `query`'s actual logic can be hijacked entirely.

This attack has a name, **SQL injection**, and it remains one of the most common, most damaging vulnerabilities in real software, precisely because the mistake that causes it, building SQL by string concatenation, is so easy to write without realizing the danger. This lesson revisits the mechanism in more depth and lays out the full set of defenses, `prepared statements` as the primary one, backed by everything covered earlier in this chapter.

## A More Damaging Injection Example

The earlier example returned extra `rows`; a real injection can go much further, touching data the `query` was never meant to involve at all.

```text
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');
```

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');

-- Query
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

This is the severity that makes SQL injection so dangerous in practice. It is not limited to reading extra `rows`:

- It can delete, modify, or destroy data entirely.
- Depending on the `database` account's granted privileges, it can reach into `tables` the application was never designed to touch at all, exactly the blast radius the least-privilege lesson in this chapter warned about.

![SQL injection happens when input is allowed to change the query structure](images/09_sql_injection_changes_query_structure.png)

## Prepared Statements Prevent Injection by Construction

The core defense, already introduced in the application-code chapter, is worth restating precisely here: a `prepared statement` never lets user-supplied text become part of the `query`'s structure, no matter what that text contains.

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');

-- Query
PREPARE get_shipment (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = $1;

EXECUTE get_shipment(1);
```

- Because `$1` is a genuine parameter, not text pasted into a string, there is no possible value that could be supplied for it that would change the `query`'s structure.
- Since `get_shipment` declares `$1` as `INTEGER`, a value like `1; DROP TABLE shipments; --` would actually be rejected outright with a type error before the `query` ever ran, PostgreSQL refusing to treat that text as a valid integer in the first place; for a `TEXT`-typed parameter instead, the same malicious string would be accepted as data and compared literally, simply matching no `row`, but either way it is never interpreted as additional SQL syntax.
- This is why `prepared statements` are described as preventing injection "by construction," rather than by filtering or detecting dangerous input: the vulnerability has no path to exist in the first place.

## Input Validation Is a Second Layer, Not a Replacement

It might seem like carefully checking and sanitizing user input before building a `query` would be enough on its own. It is a reasonable additional layer, but it is not a reliable substitute for `prepared statements`, since it depends entirely on the validation logic anticipating every possible dangerous pattern, an approach that has repeatedly proven incomplete in real-world security history.

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');

PREPARE get_shipment (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = $1;

EXECUTE get_shipment(1);

-- Query
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

Input validation still has real value, rejecting obviously malformed input early, improving error messages, catching genuine mistakes, but it should never be relied upon as the sole defense against injection; that `role` belongs to `prepared statements`.

## Least Privilege as a Defense-in-Depth Layer

Even with `prepared statements` used everywhere, the least-privilege principle from earlier in this chapter provides a valuable second line of defense: if an injection vulnerability somehow still existed, the damage it could do is bounded by what the compromised `database` account was actually granted.

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');

PREPARE get_shipment (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = $1;

EXECUTE get_shipment(1);

-- Query
CREATE ROLE web_app WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT SELECT, INSERT ON shipments TO web_app;
```

A `web_app` `role` granted only `SELECT` and `INSERT` on `shipments`, with no `DELETE`, no `DROP` privilege, and no access to any other `table`, could not have actually executed the destructive `DROP TABLE shipments` attempted in the earlier example, even in a world where the injection itself had somehow succeeded, since that `role` was never granted the privilege to drop anything at all.

This is exactly why layered defenses matter: `prepared statements` should make injection impossible in the first place, and `least privilege` limits the damage in case some other, unanticipated flaw ever slips through.

![Prepared statements, input validation, and least privilege form defense in depth](images/10_sql_injection_defense_in_depth.png)

## SQL Injection Prevention at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Defense</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prepared statements / parameterized queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primary defense; makes injection structurally impossible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Input validation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secondary layer; catches malformed input, not a substitute for parameterization</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Least privilege</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defense in depth; bounds the damage if some other flaw is ever exploited</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">String concatenation into SQL</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Never acceptable for any value that originates from outside the application&#x27;s own trusted code</td>
    </tr>
  </tbody>
</table>

## Your Turn

Rewrite the vulnerable, string-concatenation-style `query` from the beginning of this lesson as a safe, `prepared statement`, and explain in a comment exactly why the injected value can no longer change the `query`'s behavior.

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');

PREPARE get_shipment (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = $1;

EXECUTE get_shipment(1);

CREATE ROLE web_app WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT SELECT, INSERT ON shipments TO web_app;

-- Query
-- Write your prepared statement, execution, and comment below
```

- `PREPARE safe_lookup (INTEGER) AS SELECT * FROM shipments WHERE shipment_id = $1;` followed by `EXECUTE safe_lookup(1);` is the safe rewrite
- Because `$1` is a typed parameter position, not a place where raw text is spliced into SQL, any supplied value is compared purely as data against `shipment_id`.
- No malicious value can introduce new SQL syntax into the statement.

## Conclusion

SQL injection happens when untrusted input is allowed to become part of a `query`'s structure rather than staying confined to a value being compared or inserted, and `prepared statements` prevent this by construction, keeping structure and data permanently separate, with input validation and `least privilege` serving as valuable additional layers rather than substitutes for that primary defense.

The final lesson in this chapter looks at what happens after a `query` has already run: recording who did what, and when.

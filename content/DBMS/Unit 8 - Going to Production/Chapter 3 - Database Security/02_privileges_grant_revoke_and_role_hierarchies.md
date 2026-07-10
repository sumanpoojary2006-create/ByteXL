## Introduction

Creating a `role`, covered in the previous lesson, establishes an identity, but by default, a freshly created `role` can do almost nothing beyond connect. `reporting_app` cannot read a single row until it is explicitly told it is allowed to. **`GRANT`** and **`REVOKE`** are the two commands that add and remove specific permissions, called privileges, on specific database objects, for a specific `role`, and together they are how PostgreSQL enforces exactly who can do exactly what.

## Granting a Specific Privilege on a Specific Table

The `shipments` table sets up a concrete case: `reporting_app` needs to read shipment data, but should never be able to change it.

```postgresql file=grant_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO shipments (shipment_id, status, amount) VALUES
(1, 'in_transit', 450.00), (2, 'delivered', 620.00);

CREATE ROLE reporting_app WITH LOGIN PASSWORD 'change_this_in_real_use';
```

```postgresql with=grant_demo.sql
GRANT SELECT ON shipments TO reporting_app;
```

`GRANT SELECT ON shipments TO reporting_app` grants exactly one privilege, the ability to read, on exactly one table, to exactly one `role`. `reporting_app` can now run `SELECT` queries against `shipments`, but it still has no ability to:

- `INSERT`
- `UPDATE`
- `DELETE`

since none of those privileges were ever granted. Every privilege in PostgreSQL works this way: nothing is allowed until it is explicitly granted, the opposite of a system that allows everything by default and requires explicit restriction.

## Granting Multiple Privileges and Revoking One

Privileges can be granted together in a single statement, and `REVOKE` removes a previously granted privilege without affecting any others the `role` still holds.

```postgresql with=grant_demo.sql
GRANT SELECT, INSERT, UPDATE ON shipments TO reporting_app;

REVOKE UPDATE ON shipments FROM reporting_app;
```

After these two statements, `reporting_app` can read and insert new shipment rows, but the specific `UPDATE` privilege, granted a moment earlier, has been removed again, leaving `SELECT` and `INSERT` intact. `REVOKE` is precise in exactly this way: it removes only the named privilege, never accidentally sweeping away other permissions the `role` was separately granted.

## Granting Privileges Through a Role Hierarchy

Rather than granting privileges to every individual login `role` directly, the standard pattern, building on the group `role`s from the previous lesson, is to grant privileges to a group `role` once, and let membership in that group carry the permission automatically.

```postgresql with=grant_demo.sql
CREATE ROLE shipment_readers;
GRANT SELECT ON shipments TO shipment_readers;

CREATE ROLE dev_alia WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT shipment_readers TO dev_alia;
```

`dev_alia` was never directly granted `SELECT` on `shipments`; the privilege exists only on `shipment_readers`, and `dev_alia` inherits it purely through membership. This is the payoff of the group-`role` pattern: granting a new privilege to `shipment_readers` in the future instantly applies to every current and future member, without needing to remember and repeat the grant individually for each one.

## Column-Level and Fine-Grained Privileges

`GRANT` is not limited to whole tables; a privilege can be scoped down to specific columns, useful when a `role` should see most of a table but not one sensitive column.

```postgresql with=grant_demo.sql
CREATE ROLE support_staff WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT SELECT (shipment_id, status) ON shipments TO support_staff;
```

`support_staff` can now select `shipment_id` and `status`, but attempting to select `amount` as well would be rejected, since the grant explicitly named only those two columns. This finer-grained control previews the `column-level security` covered in more depth later in this chapter, but the mechanism is the same `GRANT` command already introduced here, just applied more narrowly.

## GRANT and REVOKE at a Glance

| Command | Effect |
|---|---|
| `GRANT privilege ON object TO role` | Adds a specific permission for a `role` on a specific object |
| `REVOKE privilege ON object FROM role` | Removes a specific permission, leaving other privileges untouched |
| `GRANT privilege ON object TO group_role` | Grants once, inherited by every member of that group `role` |
| `GRANT SELECT (columns) ON table TO role` | Restricts a read privilege to specific columns only |

## Your Turn

Grant `INSERT` on `shipments` to `support_staff`, on top of the column-restricted `SELECT` it already holds from earlier in this lesson, then revoke just the `INSERT` privilege, confirming `support_staff` retains its existing read access but loses the ability to insert.

```postgresql with=grant_demo.sql
-- Write your grant and revoke below
```

Running `GRANT INSERT ON shipments TO support_staff; REVOKE INSERT ON shipments FROM support_staff;` leaves `support_staff` able to read only `shipment_id` and `status`, exactly the column restriction granted earlier in this lesson, but unable to insert new rows, exactly the precise, additive-then-subtractive control `GRANT` and `REVOKE` are designed to offer. Granting a fresh, unrestricted `SELECT` on the whole table here instead would have quietly widened `support_staff`'s access to every column, `amount` included, overriding the earlier column-level grant rather than coexisting with it.

## Conclusion

`GRANT` adds a specific privilege for a specific `role` on a specific object, `REVOKE` removes one without disturbing others, and granting privileges to a group `role` rather than individual login `role`s lets an entire team's permissions be managed in one place, changes that propagate automatically to every member. Every one of Devraj's `role`s from the previous lesson can now be given exactly the access it needs and nothing more. The next lesson names the principle that should guide every one of these grants: giving a `role` only what it genuinely needs, and no more.

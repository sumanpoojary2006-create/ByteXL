## Introduction

`GRANT` and `REVOKE`, covered in the previous lesson, are just tools; they say nothing about how much access any given `role` should actually have. The **principle of `least privilege`** answers that question directly: every `role` should be granted exactly the access it needs to do its job, and nothing more, not "might need someday," not "it's easier to just grant everything." This lesson is less about new syntax and more about the judgment that should guide every `GRANT` statement written from here on.

## The Tempting Shortcut, and Why It Is a Real Risk

Granting broad, unrestricted access up front avoids the friction of figuring out exactly what a `role` needs, but it turns every `role` into a much larger liability than it needs to be.

```postgresql file=least_privilege_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT,
    amount NUMERIC(10, 2)
);

CREATE TABLE payroll (
    employee_id INTEGER PRIMARY KEY,
    salary NUMERIC(10, 2)
);

CREATE ROLE reporting_app WITH LOGIN PASSWORD 'change_this_in_real_use';
```

```postgresql with=least_privilege_demo.sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO reporting_app;
```

This single statement gives `reporting_app`, a service that only ever needs to read shipment data for dashboards, full read, write, and delete access to every table in the `schema`, including `payroll`, a table it has no legitimate business touching at all.

Two risks follow directly from this:

1. If this reporting service ever had a bug, the actual damage possible is bounded only by what it was granted, not by what it was ever supposed to do.
2. If its credentials were ever compromised, that same boundary applies, and here that boundary is "everything."

## Granting Exactly What a Role Needs

The least-privilege alternative starts from the opposite direction: name exactly what this `role` needs, and grant only that.

```postgresql with=least_privilege_demo.sql
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM reporting_app;

GRANT SELECT ON shipments TO reporting_app;
```

`reporting_app` can now read `shipments`, exactly what a reporting dashboard needs, and nothing else; it has no access to `payroll` at all, and no ability to modify `shipments` either, since `INSERT`, `UPDATE`, and `DELETE` were never granted. If this service's credentials were ever compromised, the worst an attacker could do through this specific account is read shipment data, not touch payroll, not delete anything, a dramatically smaller blast radius than the broad grant above.

## Least Privilege Applies to People, Not Just Services

The same discipline applies to individual developer accounts, not only automated services. A developer debugging a shipment-tracking issue does not need write access to `payroll` either, even though as a human they might reasonably need broader access than an automated reporting service in other ways.

```postgresql with=least_privilege_demo.sql
CREATE ROLE dev_alia WITH LOGIN PASSWORD 'change_this_in_real_use';
GRANT SELECT, UPDATE ON shipments TO dev_alia;
```

`dev_alia` gets exactly what her current debugging work requires, read and update access on `shipments`, and nothing on `payroll`. If her `role`'s responsibilities later genuinely expand, the fix is an additional, deliberate `GRANT` at that point, not a blanket grant made in advance "just in case," which is precisely the shortcut `least privilege` exists to avoid.

## Periodically Reviewing What Has Actually Been Granted

`Least privilege` is not a one-time setup step; permissions tend to accumulate over time as `role`s are granted access for a specific, temporary task and then never revisited. Periodically auditing what a `role` can actually do, compared to what it currently needs, is part of maintaining the principle over the long run.

```postgresql with=least_privilege_demo.sql
SELECT grantee, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'reporting_app';
```

`information_schema.role_table_grants` lists every privilege currently held by a given `role`, across every table, a direct way to check whether `reporting_app`'s actual granted permissions still match what it genuinely needs, or whether some stale grant from an earlier, now-irrelevant task is still sitting there, unnoticed, quietly widening that account's blast radius.

## Least Privilege at a Glance

| Question to ask before any GRANT | Why |
|---|---|
| What does this `role` actually need to do its job, right now? | Grants should match current, real need, not hypothetical future need |
| Could this be scoped to specific columns instead of a whole table? | Narrower access means a smaller blast radius if compromised |
| Is this grant still needed, months later? | Permissions accumulate; periodic review catches stale, unnecessary access |
| What is the worst outcome if this specific `role`'s credentials leak? | The answer should be small and specific, not "everything" |

## Your Turn

Audit `dev_alia`'s current privileges using `information_schema.role_table_grants`, then revoke her `UPDATE` privilege on `shipments`, reasoning in a comment about whether a read-only debugging task genuinely needs write access at all.

```postgresql with=least_privilege_demo.sql
-- Write your query, revoke, and comment below
```

`SELECT grantee, table_name, privilege_type FROM information_schema.role_table_grants WHERE grantee = 'dev_alia';` followed by `REVOKE UPDATE ON shipments FROM dev_alia;` leaves her with read-only access; a debugging task that only needs to inspect data, not change it, should indeed be granted `SELECT` alone, exactly the least-privilege judgment this lesson has been building toward.

## Conclusion

The principle of `least privilege` means granting a `role` exactly the access its actual, current responsibilities require, and nothing broader, since every unnecessary privilege granted is unnecessary risk carried indefinitely, whether that `role` represents an automated service or an individual developer, and periodically reviewing existing grants is what keeps this discipline from quietly eroding over time. The next lesson looks at an even finer-grained security mechanism, restricting access not just by table or column, but by which specific rows a `role` is allowed to see at all.

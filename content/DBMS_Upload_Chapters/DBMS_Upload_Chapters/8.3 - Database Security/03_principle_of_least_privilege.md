## Introduction

`GRANT` and `REVOKE`, covered in the previous lesson, are just tools; they say nothing about how much access any given `role` should actually have. The **principle of `least privilege`** answers that question directly: every `role` should be granted exactly the access it needs to do its job, and nothing more, not "might need someday," not "it's easier to just grant everything." This lesson is less about new syntax and more about the judgment that should guide every `GRANT` statement written from here on.

**Definition:** The principle of `least privilege` means granting a `role` exactly the access its actual, current responsibilities require, and nothing broader, since every unnecessary privilege granted is unnecessary risk carried indefinitely, whether that `role` represents an automated service or an individual developer, and periodically reviewing existing grants is what keeps this discipline from quietly eroding over time.

## The Tempting Shortcut, and Why It Is a Real Risk

Granting broad, unrestricted access up front avoids the friction of figuring out exactly what a `role` needs, but it turns every `role` into a much larger liability than it needs to be.

## Source Data Used in This Lesson

The setup also creates the following empty supporting tables. Later statements populate them as the operation runs.

### Empty `shipments` table

| Column | Definition in the setup |
| --- | --- |
| `shipment_id` | `INTEGER PRIMARY KEY` |
| `status` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |

### Empty `payroll` table

| Column | Definition in the setup |
| --- | --- |
| `employee_id` | `INTEGER PRIMARY KEY` |
| `salary` | `NUMERIC(10, 2)` |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj8uc" 
 width="100%"
></iframe>

Expected result: PostgreSQL completes the definition or privilege command without returning a business-data table. The later query in the lesson verifies the object or access rule that was created.

This single statement gives `reporting_app`, a service that only ever needs to read shipment data for dashboards, full read, write, and delete access to every `table` in the `schema`, including `payroll`, a `table` it has no legitimate business touching at all.

Two risks follow directly from this:

1. If this reporting service ever had a bug, the actual damage possible is bounded only by what it was granted, not by what it was ever supposed to do.

2. If its credentials were ever compromised, that same boundary applies, and here that boundary is "everything."

## Granting Exactly What a Role Needs

The least-privilege alternative starts from the opposite direction: name exactly what this `role` needs, and grant only that.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj95n" 
 width="100%"
></iframe>

Expected result: PostgreSQL completes the definition or privilege command without returning a business-data table. The later query in the lesson verifies the object or access rule that was created.

- `reporting_app` can now read `shipments`, exactly what a reporting dashboard needs, and nothing else; it has no access to `payroll` at all, and no ability to modify `shipments` either, since `INSERT`, `UPDATE`, and `DELETE` were never granted.
- If this service's credentials were ever compromised, the worst an attacker could do through this specific account is read shipment data, not touch payroll, not delete anything, a dramatically smaller blast radius than the broad grant above.

![Least privilege gives a role only the access it needs, reducing the blast radius](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_least_privilege_smaller_blast_radius.png)

## Least Privilege Applies to People, Not Just Services

The same discipline applies to individual developer accounts, not only automated services. A developer debugging a shipment-tracking issue does not need write access to `payroll` either, even though as a human they might reasonably need broader access than an automated reporting service in other ways.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj9ge" 
 width="100%"
></iframe>

Expected result: PostgreSQL completes the definition or privilege command without returning a business-data table. The later query in the lesson verifies the object or access rule that was created.

- `dev_alia` gets exactly what her current debugging work requires, read and update access on `shipments`, and nothing on `payroll`.
- If her `role`'s responsibilities later genuinely expand, the fix is an additional, deliberate `GRANT` at that point, not a blanket grant made in advance "just in case," which is precisely the shortcut `least privilege` exists to avoid.

## Periodically Reviewing What Has Actually Been Granted

- `Least privilege` is not a one-time setup step; permissions tend to accumulate over time as `role`s are granted access for a specific, temporary task and then never revisited.
- Periodically auditing what a `role` can actually do, compared to what it currently needs, is part of maintaining the principle over the long run.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj9vm" 
 width="100%"
></iframe>

Expected output:

| grantee | table_name | privilege_type |
| --- | --- | --- |
| *(no rows)* | | |

This block only grants `SELECT` and `UPDATE` to `dev_alia`; `reporting_app` was created by `init.sql` but was never granted anything in this fresh session, so filtering `role_table_grants` for `reporting_app` correctly comes back empty here. In a real, long-running `database`, this same `query` is exactly how a team would spot that `reporting_app` unexpectedly does, or does not, hold a grant it should. `information_schema.role_table_grants` lists every privilege currently held by a given `role`, across every `table`, a direct way to check whether `reporting_app`'s actual granted permissions still match what it genuinely needs, or whether some stale grant from an earlier, now-irrelevant task is still sitting there, unnoticed, quietly widening that account's blast radius.

![Periodic grant review compares current permissions with current need and removes stale access](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_review_grants_revoke_stale_access.png)

## Least Privilege at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question to ask before any GRANT</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What does this <code>role</code> actually need to do its job, right now?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grants should match current, real need, not hypothetical future need</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Could this be scoped to specific columns instead of a whole table?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Narrower access means a smaller blast radius if compromised</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is this grant still needed, months later?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permissions accumulate; periodic review catches stale, unnecessary access</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the worst outcome if this specific <code>role</code>&#x27;s credentials leak?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The answer should be small and specific, not &quot;everything&quot;</td>
    </tr>
  </tbody>
</table>

## Your Turn

Audit `dev_alia`'s current privileges using `information_schema.role_table_grants`, then revoke her `UPDATE` privilege on `shipments`, reasoning in a comment about whether a read-only debugging task genuinely needs write access at all.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajaek" 
 width="100%"
></iframe>

Expected result and verification:

- `SELECT grantee, table_name, privilege_type FROM information_schema.role_table_grants WHERE grantee = 'dev_alia';` followed by `REVOKE UPDATE ON shipments FROM dev_alia;` leaves her with read-only access
- a debugging task that only needs to inspect data, not change it, should indeed be granted `SELECT` alone, exactly the least-privilege judgment this lesson has been building toward.

## Conclusion

The principle of `least privilege` means granting a `role` exactly the access its actual, current responsibilities require, and nothing broader, since every unnecessary privilege granted is unnecessary risk carried indefinitely, whether that `role` represents an automated service or an individual developer, and periodically reviewing existing grants is what keeps this discipline from quietly eroding over time.

The next lesson looks at an even finer-grained security mechanism, restricting access not just by `table` or `column`, but by which specific `rows` a `role` is allowed to see at all.

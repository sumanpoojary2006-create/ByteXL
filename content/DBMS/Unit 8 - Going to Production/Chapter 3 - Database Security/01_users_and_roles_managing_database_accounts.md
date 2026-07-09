## Introduction

Every query in this course has run under a single, implicit database account, with no attention paid to who or what is actually connecting. A production database serves many different consumers at once, a reporting dashboard, a background job, individual developers debugging an issue, and each of these deserves its own identity, not a single shared login everyone uses interchangeably. PostgreSQL's answer to this is **`role`s**, the unified mechanism it uses to represent both individual users and groups of permissions, and understanding `role`s is the foundation the rest of this chapter's security material builds on.

## Creating a Role

A `role` can represent a login-capable user or a non-login group, and the same `CREATE ROLE` command handles both, differing only in the options supplied.

```postgresql file=roles_demo.sql
CREATE ROLE reporting_app WITH LOGIN PASSWORD 'change_this_in_real_use';
CREATE ROLE dev_alia WITH LOGIN PASSWORD 'change_this_in_real_use';
```

```postgresql with=roles_demo.sql
SELECT rolname, rolcanlogin FROM pg_roles WHERE rolname IN ('reporting_app', 'dev_alia');
```

`WITH LOGIN` marks a `role` as one that can actually authenticate and open a connection, exactly the two `role`s created here:

- `reporting_app`, representing an automated reporting service
- `dev_alia`, representing an individual developer

`pg_roles` confirms both now exist, with `rolcanlogin` showing `true` for each, distinguishing them from a `role` created without login rights, covered next.

## Roles Without Login: Grouping Permissions Together

A `role` does not have to represent a person or a service at all; it can exist purely as a named bundle of permissions that other `role`s can be added to.

```postgresql with=roles_demo.sql
CREATE ROLE shipment_readers;

GRANT shipment_readers TO reporting_app;
GRANT shipment_readers TO dev_alia;
```

`shipment_readers` here has no `LOGIN` option, meaning nothing can connect to the database directly as `shipment_readers`; it exists purely as a named group. `GRANT shipment_readers TO reporting_app` adds `reporting_app` as a member of that group, and any permission granted to `shipment_readers` as a whole, covered in the next lesson, automatically applies to every member. This is the standard pattern for managing permissions at scale: define what a group of accounts should be allowed to do once, on the group `role`, rather than repeating the same permission grants individually on every single user `role`.

## Why Shared Logins Are a Security Anti-Pattern

It might seem simpler to give every developer and every service the same single database login. This is a well-known anti-pattern, for reasons that go beyond convenience.

```postgresql with=roles_demo.sql
SELECT usename, query, query_start
FROM pg_stat_activity
WHERE usename = 'reporting_app';
```

`pg_stat_activity`, introduced in the previous chapter, records which `role` issued each active query, which is exactly the accountability a shared login destroys. If every developer and every application connected as one single, shared account, there would be no way to answer "who ran this slow query" or "which service made this change" after the fact, since the log would show only the one shared name for every single action, regardless of who or what actually took it. Separate `role`s per person and per service are what make that kind of accountability possible at all.

## Altering and Dropping Roles

A `role`'s properties can be changed after creation, and a `role` that is no longer needed can be removed, though only once nothing still depends on it.

```postgresql with=roles_demo.sql
ALTER ROLE dev_alia WITH PASSWORD 'a_new_stronger_password';

DROP ROLE shipment_readers;
```

Dropping `shipment_readers` succeeds here since nothing else in this example still references it structurally beyond the membership grants already made; in a real system with actual permissions and dependent objects attached to a `role`, PostgreSQL would refuse to drop it until those dependencies were resolved first, a safeguard against silently breaking access for every account that depended on that `role`'s permissions.

## Roles at a Glance

| Concept | Detail |
|---|---|
| `CREATE ROLE name WITH LOGIN PASSWORD '...'` | A `role` that can authenticate and open a connection |
| `CREATE ROLE name` (no `LOGIN`) | A group `role`, used purely to bundle permissions |
| `GRANT group_role TO member_role` | Adds a `role` as a member of a group, inheriting its permissions |
| Shared logins | An anti-pattern; destroys per-account accountability |

## Your Turn

Create a new login `role` named `dev_farah` and a group `role` named `shipment_writers`, then add `dev_farah` as a member of `shipment_writers`.

```postgresql with=roles_demo.sql
-- Write your role creation and grant below
```

If you run `CREATE ROLE dev_farah WITH LOGIN PASSWORD 'change_this_in_real_use'; CREATE ROLE shipment_writers; GRANT shipment_writers TO dev_farah;`, querying `pg_roles` and the membership catalog confirms `dev_farah` now inherits whatever permissions get granted to `shipment_writers` as a group.

## Conclusion

A `role` in PostgreSQL can represent either an individually authenticating account or a non-login group used to bundle permissions, and structuring access around distinct `role`s per person and per service, rather than a single shared login, is what makes accountability and precise permission management possible at all. With `role`s established as the foundation, the next lesson covers exactly how permissions are actually granted to, and revoked from, a `role`.

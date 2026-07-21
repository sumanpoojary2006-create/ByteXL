## Introduction

Every `query` in this course has run under a single, implicit `database` account, with no attention paid to who or what is actually connecting. A production `database` serves many different consumers at once, a reporting dashboard, a background job, individual developers debugging an issue, and each of these deserves its own identity, not a single shared login everyone uses interchangeably.

PostgreSQL's answer to this is **`role`s**, the unified mechanism it uses to represent both individual users and groups of permissions, and understanding `role`s is the foundation the rest of this chapter's security material builds on.

**Definition:** A `role` in PostgreSQL can represent either an individually authenticating account or a non-login group used to bundle permissions, and structuring access around distinct `role`s per person and per service, rather than a single shared login, is what makes accountability and precise permission management possible at all.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_users_and_roles_managing_database_accounts.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Every query in this course has run under a single, implicit database account, with no attention paid to who or what is actually connecting. A production database serves many different consumers at once, a reporting dashboard, a background job, individual.

ON-IMAGE TEXT: show a short bold title "Users And Roles Managing Database Accounts" plus only these few labels, large and legible: Query, Role, Users. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for users and roles managing database accounts](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_users_and_roles_managing_database_accounts_clean_086cba44.png)

## Creating a Role

A `role` can represent a login-capable user or a non-login group, and the same `CREATE ROLE` command handles both, differing only in the options supplied.

## Source Data Used in This Lesson

This lesson works with database accounts rather than business rows. Before running the examples, inspect the roles created by the setup file.

| Role | Purpose in the activity |
| --- | --- |
| `reporting_app` | Account used to demonstrate role membership or privileges |
| `dev_alia` | Account used to demonstrate role membership or privileges |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE ROLE reporting_app WITH LOGIN PASSWORD 'change_this_in_real_use';
CREATE ROLE dev_alia WITH LOGIN PASSWORD 'change_this_in_real_use';
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
SELECT rolname, rolcanlogin FROM pg_roles WHERE rolname IN ('reporting_app', 'dev_alia');
```

Expected output:

| rolname | rolcanlogin |
| --- | --- |
| reporting_app | TRUE |
| dev_alia | TRUE |

`WITH LOGIN` marks a `role` as one that can actually authenticate and open a `connection`, exactly the two `role`s created here:

- `reporting_app`, representing an automated reporting service
- `dev_alia`, representing an individual developer

`pg_roles` confirms both now exist, with `rolcanlogin` showing `true` for each, distinguishing them from a `role` created without login rights, covered next.

## Roles Without Login: Grouping Permissions Together

A `role` does not have to represent a person or a service at all; it can exist purely as a named bundle of permissions that other `role`s can be added to.

```postgresql with=init.sql
CREATE ROLE shipment_readers;

GRANT shipment_readers TO reporting_app;
GRANT shipment_readers TO dev_alia;
```

Expected result: PostgreSQL completes the definition or privilege command without returning a business-data table. The later query in the lesson verifies the object or access rule that was created.

- `shipment_readers` here has no `LOGIN` option, meaning nothing can connect to the `database` directly as `shipment_readers`; it exists purely as a named group.
- `GRANT shipment_readers TO reporting_app` adds `reporting_app` as a member of that group, and any permission granted to `shipment_readers` as a whole, covered in the next lesson, automatically applies to every member.
- This is the standard pattern for managing permissions at scale: define what a group of accounts should be allowed to do once, on the group `role`, rather than repeating the same permission grants individually on every single user `role`.

![Login roles can inherit a group role that bundles permissions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_login_roles_and_group_role_permissions.png)

## Why Shared Logins Are a Security Anti-Pattern

It might seem simpler to give every developer and every service the same single `database` login. This is a well-known anti-pattern, for reasons that go beyond convenience.

```postgresql with=init.sql
CREATE ROLE shipment_readers;

GRANT shipment_readers TO reporting_app;
GRANT shipment_readers TO dev_alia;

SELECT usename, query, query_start
FROM pg_stat_activity
WHERE usename = 'reporting_app';
```

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `pg_stat_activity`, introduced in the previous chapter, records which `role` issued each active `query`, which is exactly the accountability a shared login destroys.
- If every developer and every application connected as one single, shared account, there would be no way to answer "who ran this slow `query`" or "which service made this change" after the fact, since the log would show only the one shared name for every single action, regardless of who or what actually took it.
- Separate `role`s per person and per service are what make that kind of accountability possible at all.

![Shared logins hide who performed an action, while separate roles preserve accountability](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_shared_login_loses_accountability.png)

## Altering and Dropping Roles

A `role`'s properties can be changed after creation, and a `role` that is no longer needed can be removed, though only once nothing still depends on it.

```postgresql with=init.sql
CREATE ROLE shipment_readers;

GRANT shipment_readers TO reporting_app;
GRANT shipment_readers TO dev_alia;

ALTER ROLE dev_alia WITH PASSWORD 'a_new_stronger_password';

DROP ROLE shipment_readers;
```

Expected result: PostgreSQL completes the definition or privilege command without returning a business-data table. The later query in the lesson verifies the object or access rule that was created.

Dropping `shipment_readers` succeeds here since nothing else in this example still references it structurally beyond the membership grants already made in a real system with actual permissions and dependent objects attached to a `role`, PostgreSQL would refuse to drop it until those dependencies were resolved first, a safeguard against silently breaking access for every account that depended on that `role`'s permissions.

## Roles at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CREATE ROLE name WITH LOGIN PASSWORD &#x27;...&#x27;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A <code>role</code> that can authenticate and open a connection</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CREATE ROLE name</code> (no <code>LOGIN</code>)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A group <code>role</code>, used purely to bundle permissions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>GRANT group_role TO member_role</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adds a <code>role</code> as a member of a group, inheriting its permissions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared logins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An anti-pattern; destroys per-account accountability</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create a new login `role` named `dev_farah` and a group `role` named `shipment_writers`, then add `dev_farah` as a member of `shipment_writers`.

```postgresql with=init.sql
CREATE ROLE shipment_readers;

GRANT shipment_readers TO reporting_app;
GRANT shipment_readers TO dev_alia;

-- Write your role creation and grant below
```

Expected result and verification:

If you run `CREATE ROLE dev_farah WITH LOGIN PASSWORD 'change_this_in_real_use'; CREATE ROLE shipment_writers; GRANT shipment_writers TO dev_farah;`, querying `pg_roles` and the membership catalog confirms `dev_farah` now inherits whatever permissions get granted to `shipment_writers` as a group.

## Conclusion

A `role` in PostgreSQL can represent either an individually authenticating account or a non-login group used to bundle permissions, and structuring access around distinct `role`s per person and per service, rather than a single shared login, is what makes accountability and precise permission management possible at all. With `role`s established as the foundation, the next lesson covers exactly how permissions are actually granted to, and revoked from, a `role`.

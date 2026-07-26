# DBMS 8.3: Database Security — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Going to Production
- **Chapter:** Database Security
- **Scope:** Users and Roles; Privileges and Role Hierarchies; Principle of Least Privilege; Row-Level and Column-Level Security; SQL Injection Prevention; Auditing and Tracking Data Access
- **SQL dialect:** PostgreSQL
- **Format:** Four plausible options with exactly one best answer
- **Is Curriculum Based:** No
- **Coverage rule:** Questions 1–10 collectively cover all six chapter subtopics.
- **Design standard:** Decisions depend on supplied roles, grants, policies, attack inputs, SQL, or audit rows.
- **Answer-quality controls:** A/B/C/D are each correct exactly 10 times; no answer letter occurs more than twice consecutively.

---

## Questions

### 1. A permission bundle that cannot log in

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a role structure

`reporting_app` and `dev_alia` need the same read permissions, but the team does not want a third account that anyone can authenticate as.

Which design fits?

A. Give both people the same password.  
B. Create another login and publish its credentials.  
C. Create non-login `shipment_readers` and grant membership to both login roles.  
D. Store the permissions in an audit table.

### 2. Removing one permission without disturbing another

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Tracing privilege state

```sql
GRANT SELECT, INSERT, UPDATE ON shipments TO reporting_app;
REVOKE UPDATE ON shipments FROM reporting_app;
```

What can `reporting_app` do afterward?

A. Select and insert, but not update.  
B. Update only.  
C. Select only.  
D. Nothing on `shipments`.

### 3. The dashboard does not need payroll

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest grant

A service only reads shipment rows for a dashboard. Which grant best limits its blast radius?

A. `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO reporting_app;`  
B. `GRANT SELECT, UPDATE ON shipments, payroll TO reporting_app;`  
C. `GRANT ALL PRIVILEGES ON shipments TO reporting_app;`  
D. `GRANT SELECT ON shipments TO reporting_app;`

### 4. A missing WHERE clause must not leak Pune rows

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an enforcement mechanism

`mumbai_coordinator` may read only Mumbai shipment rows, even if application code runs `SELECT * FROM shipments` without a filter.

Which mechanism enforces this inside PostgreSQL?

A. A comment reminding developers to filter  
B. Enable RLS and create a `USING (branch='Mumbai')` policy for the role.  
C. Rename all Pune rows.  
D. Log the query after it returns.

### 5. The input becomes a second SQL statement

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an attack path

Application code concatenates an ID into SQL. Input is `1; DROP TABLE shipments; --`.

What defect permits the destructive text to affect query structure?

A. The ID column is an integer.  
B. The role has a password.  
C. Untrusted text is pasted into SQL instead of bound as a value.  
D. The table lacks row-level security.

### 6. Recording who changed what

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an audit mechanism

Every insert, update, and delete on `shipments` must record the operation, acting role, timestamp, and old/new row images.

Which implementation matches the lesson?

A. An `AFTER` row trigger that writes `TG_OP`, `current_user`, `OLD`, and `NEW` to an audit table  
B. A row-level policy that silently filters results  
C. A column-level `SELECT` grant  
D. One shared login for all writers

### 7. Login role versus group role

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two role definitions

```sql
CREATE ROLE dev_farah WITH LOGIN PASSWORD '...';
CREATE ROLE shipment_writers;
```

Which statement is correct?

A. Both can authenticate.  
B. Neither can authenticate.  
C. `dev_farah` can log in; `shipment_writers` is a permission group unless altered.  
D. `shipment_writers` automatically inherits from `dev_farah`.

### 8. Inheriting a grant through membership

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a role hierarchy

```sql
CREATE ROLE shipment_readers;
GRANT SELECT ON shipments TO shipment_readers;
GRANT shipment_readers TO dev_alia;
```

No direct table grant is made to `dev_alia`. Why can she read `shipments`?

A. Every login receives `SELECT` automatically.  
B. Membership carries the group role’s privilege.  
C. `CREATE ROLE` grants access to all public tables.  
D. Audit triggers grant temporary read access.

### 9. Restricting rows and columns together

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Tracing layered restrictions

`mumbai_coordinator` has:

- RLS policy `USING (branch='Mumbai')`
- `GRANT SELECT (shipment_id, branch, status)` on a table also containing `internal_cost`

Which access is allowed?

A. Every column for Mumbai rows  
B. The three granted columns for every branch  
C. `internal_cost` only for Mumbai rows  
D. The three granted columns, and only for Mumbai rows

### 10. Primary defense and supporting layers

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a defense-in-depth design

Which combination assigns the correct roles to the defenses?

A. Parameterization is primary; validation and least privilege are supporting layers.  
B. Validation replaces parameterization; broad privileges simplify recovery.  
C. Auditing prevents injection before execution.  
D. RLS safely converts concatenated text into values.

### 11. Shared credentials erase attribution

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an accountability defect

Ten developers and two services connect as `shared_app`. An incident log shows `shared_app` deleted rows.

Why is investigation blocked?

A. PostgreSQL never records role names.  
B. The shared identity cannot distinguish which person or service acted.  
C. DELETE operations cannot be audited.  
D. Group roles erase table names.

### 12. Dropping a role with dependencies

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Predicting administrative behaviour

A role still owns or depends on database objects and permissions. An administrator immediately runs `DROP ROLE`.

What safeguard should be expected?

A. All dependent objects are silently deleted.  
B. The role becomes a superuser.  
C. Memberships turn into passwords.  
D. PostgreSQL can refuse the drop until dependencies are resolved.

### 13. Granting only visible columns

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Completing a column-level grant

Support staff may read `shipment_id` and `status`, but not `amount`.

Which statement implements that boundary?

A. `GRANT SELECT (shipment_id, status) ON shipments TO support_staff;`  
B. `GRANT SELECT ON shipments TO support_staff;`  
C. `REVOKE SELECT ON amount FROM shipments;`  
D. `CREATE POLICY amount_hidden ON status;`

### 14. Revoking INSERT preserves the narrow SELECT

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Identifying final privileges

Support already has column-level `SELECT`, then receives `INSERT`. Later:

```sql
REVOKE INSERT ON shipments FROM support_staff;
```

What remains?

A. No privileges at all  
B. The earlier column-level read access, but no insert  
C. Full-table `SELECT` and update  
D. Insert only

### 15. A stale developer grant

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct review action

`dev_alia` received `UPDATE` for a short repair. Months later her role is read-only support, but `role_table_grants` still lists `UPDATE`.

What is the appropriate repair?

A. Grant `DELETE` so write permissions are consistent.  
B. Ignore it because unused privileges have no risk.  
C. Revoke `UPDATE` and retain only currently required access.  
D. Replace her individual account with a shared login.

### 16. Measuring the compromised account’s blast radius

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two privilege designs

Role P has `ALL` on every public table. Role Q has `SELECT` on `shipments` only. Both credentials leak.

Which comparison is valid?

A. Both accounts permit identical damage.  
B. Q is riskier because it has fewer privileges.  
C. P is safe because `ALL` is easier to audit.  
D. Q’s possible actions are bounded to a much smaller scope.

### 17. Reviewing actual grants

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Selecting audit evidence

Which catalog view helps compare a role’s table privileges with its current job?

A. `information_schema.role_table_grants`  
B. A materialized shipment summary  
C. `pg_stat_activity` query text only  
D. The application’s login page

### 18. RLS needs both enabling and a policy

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Completing security SQL

Which pair establishes Mumbai-only reads for `mumbai_coordinator`?

A. A column grant plus an audit trigger  
B. `ENABLE ROW LEVEL SECURITY` plus a `FOR SELECT ... USING (branch='Mumbai')` policy  
C. A view name plus a shared password  
D. `REVOKE UPDATE` plus `ORDER BY branch`

### 19. The policy applies without application cooperation

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Predicting query output

Data contains Mumbai IDs 1 and 3 and Pune IDs 2 and 4. Under the Mumbai RLS role:

```sql
SELECT shipment_id FROM shipments ORDER BY shipment_id;
```

What is returned?

A. 1, 2, 3, 4  
B. No rows without an explicit WHERE clause  
C. 1 and 3  
D. 2 and 4

### 20. RLS and column grants solve different dimensions

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Comparing security mechanisms

Which mapping is correct?

A. RLS hides columns; column grants choose branches.  
B. Both mechanisms only record access.  
C. Both mechanisms restrict passwords.  
D. RLS restricts rows; column-level grants restrict columns.

### 21. The input that exposes concatenation

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Choosing defect-exposing input

Code builds `... WHERE shipment_id = ` plus raw input. Which input most clearly changes the intended one-ID predicate?

A. `1 OR 1=1`  
B. `2`  
C. `0003`  
D. `4`

### 22. Typed parameters reject or contain hostile text

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about prepared values

`$1` is declared `INTEGER`. Input is `1; DROP TABLE shipments; --`.

What happens under parameter binding?

A. The semicolon starts a second statement.  
B. The value is rejected as an invalid integer; it never becomes SQL syntax.  
C. The database drops only rows visible through RLS.  
D. Input validation rewrites it to 1 automatically.

### 23. Validation is useful but insufficient alone

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a security logic gap

A filter rejects semicolons and the word `DROP`, then concatenates all other input into SQL.

What is the flaw?

A. Validation prevents all malformed input and needs no parameterization.  
B. Least privilege makes concatenation safe.  
C. A blacklist may miss other encodings or constructs; bound parameters are still required.  
D. RLS automatically parameterizes the string.

### 24. Least privilege after a missed injection defect

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Analysing defense in depth

An injection bug exists, but `web_app` has only `SELECT, INSERT` on `shipments` and no rights on payroll.

Which conclusion is sound?

A. The injection bug no longer matters.  
B. The account can now grant itself privileges.  
C. Prepared statements are unnecessary for this role.  
D. Least privilege limits possible damage, but the injection must still be fixed.

### 25. UPDATE audit row

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Tracing audit values

Shipment 1 changes from `in_transit` to `delivered`. The audit trigger stores `TG_OP`, `current_user`, `OLD`, and `NEW`.

Which record shape is correct?

A. Action INSERT; OLD null; NEW delivered  
B. Action UPDATE; OLD in_transit; NEW delivered; acting role recorded  
C. Action SELECT; OLD delivered; NEW null  
D. Action DELETE; OLD in_transit; NEW delivered

### 26. INSERT followed by DELETE

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple audit events

An audited row is inserted and then deleted. How should the two entries differ?

A. Both have OLD and NEW populated.  
B. Both have only NEW populated.  
C. INSERT has NEW only; DELETE has OLD only.  
D. DELETE is invisible to row triggers.

### 27. Trigger auditing cannot see SELECT

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

Compliance now requires recording who reads a sensitive table. The existing trigger covers insert, update, and delete.

What additional approach is needed?

A. Server-level statement logging or a purpose-built auditing extension  
B. Another `AFTER SELECT` row trigger  
C. A wider column grant  
D. A non-login group role

### 28. Auditing does not block the action

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Deciding whether mechanisms are equivalent

Can an audit trail replace least privilege and RLS?

A. Yes, because recording an action reverses it.  
B. Yes, if JSON stores OLD and NEW.  
C. No, because auditing changes every role into a superuser.  
D. No. Auditing supports detection and investigation; prevention controls block access.

### 29. Removing a member’s inherited access

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a hierarchy repair

`dev_alia` receives shipment read access only through membership in `shipment_readers`. She changes teams; other group members still need access.

Which smallest change removes only her inherited access?

A. Revoke SELECT from the group.  
B. Drop the `shipments` table.  
C. Revoke `shipment_readers` membership from `dev_alia`.  
D. Change every member’s password.

### 30. One grant for current and future readers

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Privileges: GRANT, REVOKE, and Role Hierarchies  
**Is Curriculum Based:** No  
**Assessment type:** Selecting scalable permission management

Which design avoids repeating the same table grant for every new reporting account?

A. Grant SELECT to a group role, then manage group membership.  
B. Use one shared reporting login.  
C. Grant ALL directly to every account.  
D. Copy permissions into application code.

### 31. RLS policy versus application filter

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two implementations

Version A relies on every query adding `WHERE branch=current_branch`. Version B enforces the branch rule through RLS.

Which advantage does B provide?

A. It makes all branches visible to every role.  
B. The database applies the restriction even when a query omits the filter.  
C. It records every read automatically in `audit_log`.  
D. It removes the need for SELECT privilege.

### 32. Overbroad debugging permission

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

A developer needs to inspect shipment rows for one week. The proposed grant is `ALL PRIVILEGES ON ALL TABLES`.

Which alternative best matches the actual task?

A. Grant payroll update access too.  
B. Make the developer a shared service account.  
C. Grant permanent DELETE on shipments.  
D. Grant SELECT on shipments, then review/revoke when the task ends.

### 33. Filling the audit operation

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Completing trigger code

Which special variable fills `action` with INSERT, UPDATE, or DELETE?

```sql
INSERT INTO audit_log(action, changed_by)
VALUES (_____, current_user);
```

A. `OLD`  
B. `TG_OP`  
C. `NEW`  
D. `rolcanlogin`

### 34. Why separate roles improve audit evidence

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Applying role design to auditing

An audit trigger records `current_user`. Which account strategy makes that field most informative?

A. One credential shared across all services  
B. A non-login group used directly by every connection  
C. Distinct login roles for each person and service  
D. No roles, only IP addresses

### 35. Completing a prepared lookup

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** SQL Injection Prevention  
**Is Curriculum Based:** No  
**Assessment type:** Filling missing SQL

```sql
PREPARE safe_lookup (INTEGER) AS
SELECT * FROM shipments WHERE shipment_id = _____;
```

A. `$1`  
B. `input + ''`  
C. `{raw_text}`  
D. `EXECUTE`

### 36. Read auditing has a cost

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating an audit boundary

Why might comprehensive statement logging be reserved for especially sensitive data rather than enabled indiscriminately?

A. It disables all write triggers.  
B. It prevents roles from logging in.  
C. It removes RLS policies.  
D. Recording every query adds real logging and performance overhead.

### 37. Policy plus privilege

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Row-Level and Column-Level Security  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions

A role has a Mumbai-only RLS policy but has never been granted `SELECT` on `shipments`.

Which conclusion is correct?

A. The policy itself grants full read access.  
B. The role still needs SELECT privilege; the policy restricts permitted rows rather than granting access.  
C. The role may read only the branch column.  
D. RLS turns the role into the table owner.

### 38. Updating a password without replacing the role

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Users and Roles: Managing Database Accounts  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an account repair

Which command changes `dev_alia`’s credential while preserving the role identity?

A. `DROP ROLE dev_alia;`  
B. `GRANT PASSWORD TO dev_alia;`  
C. `ALTER ROLE dev_alia WITH PASSWORD 'new_value';`  
D. `UPDATE pg_roles SET password='new_value';`

### 39. Narrowing a reporting role after review

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Principle of Least Privilege  
**Is Curriculum Based:** No  
**Assessment type:** Comparing final privilege states

```sql
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM reporting_app;
GRANT SELECT ON shipments TO reporting_app;
```

What is the intended final boundary?

A. Full access to shipments and payroll  
B. Write-only access to shipments  
C. No ability to connect under any circumstances  
D. Read access to shipments, with no implied access to payroll or shipment writes

### 40. Layering prevention and investigation

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Auditing and Tracking Data Access  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple security concepts

A branch application accepts untrusted IDs, must see only its branch, and every write must be attributable.

Which combined design is strongest?

A. Parameterized queries, least-privilege distinct login roles, RLS, and a write-audit trigger  
B. String concatenation, one shared superuser, and server logs  
C. Application WHERE clauses only, with no database policy  
D. An audit table alone, because records prevent misuse

---

## Instructor Key

### 1. C
A non-login role bundles permissions, while individual login roles retain distinct identities and inherit through membership.
### 2. A
REVOKE removes only UPDATE; SELECT and INSERT remain.
### 3. D
The dashboard needs only SELECT on shipments, so broader table, write, or payroll access is unnecessary risk.
### 4. B
RLS plus a policy makes PostgreSQL apply the branch predicate automatically.
### 5. C
Concatenation lets untrusted text cross from data into SQL structure.
### 6. A
An AFTER row trigger can capture the operation, role, time, and before/after images for every write.
### 7. C
WITH LOGIN permits authentication; the role without LOGIN serves as a group by default.
### 8. B
The table privilege belongs to the group and is inherited by its member.
### 9. D
RLS limits rows to Mumbai, while the column grant withholds internal_cost.
### 10. A
Parameters are the primary structural defense; validation and restricted privileges add defense in depth.
### 11. B
Every action has the same database identity, so the evidence cannot identify the actual actor.
### 12. D
PostgreSQL protects dependencies rather than silently destroying or orphaning them.
### 13. A
The column list grants only the two named fields.
### 14. B
Revoking INSERT leaves the separately granted column-level SELECT intact.
### 15. C
Least privilege requires removing stale access once the task no longer needs it.
### 16. D
Q’s compromise is constrained to the one granted read surface, unlike P’s broad authority.
### 17. A
The information-schema view lists table grants held by roles.
### 18. B
Enabling RLS activates enforcement; the policy supplies the role-specific predicate.
### 19. C
The database injects the policy restriction even though the SQL has no WHERE clause.
### 20. D
The two mechanisms restrict orthogonal dimensions: rows and columns.
### 21. A
`OR 1=1` changes a concatenated predicate from one ID to an always-true condition.
### 22. B
The typed value cannot be parsed as an integer and never becomes executable SQL text.
### 23. C
Blacklists cannot reliably anticipate every representation; parameter binding removes the structural path.
### 24. D
Restricted privileges reduce blast radius but do not excuse the underlying injection vulnerability.
### 25. B
An update supplies both row images, TG_OP=UPDATE, and current_user identifies the actor.
### 26. C
An inserted row has no OLD image; a deleted row has no NEW image.
### 27. A
Plain SELECT does not fire a row trigger, so read auditing needs server-level statement facilities.
### 28. D
Auditing preserves evidence after events; privilege and row controls prevent disallowed access.
### 29. C
Removing only her group membership preserves access for every other member.
### 30. A
One group grant serves current and future accounts through membership management.
### 31. B
RLS closes the missed-WHERE failure path by enforcing the predicate below application SQL.
### 32. D
Temporary read work warrants narrowly scoped SELECT with later review, not broad permanent authority.
### 33. B
TG_OP contains the triggering operation name.
### 34. C
Distinct login identities make current_user attributable to a particular person or service.
### 35. A
`$1` is the typed parameter placeholder in PostgreSQL PREPARE syntax.
### 36. D
Capturing every statement adds logging volume and execution overhead.
### 37. B
Privileges authorize the operation; RLS narrows the rows visible within that authorized operation.
### 38. C
ALTER ROLE changes the credential without discarding the account’s identity and memberships.
### 39. D
The broad grants are removed and replaced with exactly one read privilege on shipments.
### 40. A
The combination prevents query manipulation, narrows access and rows, preserves attribution, and records writes.

---

## Coverage summary

| Subtopic | Questions |
|---|---|
| Users and Roles: Managing Database Accounts | 1, 7, 11, 12, 34, 38 |
| Privileges: GRANT, REVOKE, and Role Hierarchies | 2, 8, 13, 14, 29, 30 |
| Principle of Least Privilege | 3, 15, 16, 17, 32, 39 |
| Row-Level and Column-Level Security | 4, 9, 18, 19, 20, 31, 37 |
| SQL Injection Prevention | 5, 10, 21, 22, 23, 24, 35 |
| Auditing and Tracking Data Access | 6, 25, 26, 27, 28, 33, 36, 40 |

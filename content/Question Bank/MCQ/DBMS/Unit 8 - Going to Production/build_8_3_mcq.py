import random
import openpyxl

random.seed(183)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

USERS_AND_ROLES = [
    (
        "Every query in this course so far ran under a single, implicit database account, but a production database serves many different consumers, a reporting dashboard, a background job, individual developers, each deserving its own identity rather than a single shared login.\n\nWhat does PostgreSQL use as its unified mechanism to represent both individual users and groups of permissions?",
        "Roles — PostgreSQL's unified mechanism for representing both individual login-capable users and non-login groups of permissions, the foundation the rest of the security chapter builds on.",
        "easy", "remember", "users-and-roles-managing-database-accounts",
        "Roles, PostgreSQL's unified mechanism for representing both individual users and groups of permissions",
        ["Schemas, which organize tables into separate namespaces within a database", "Views, which save a reusable query definition under a name", "Indexes, which speed up lookups on specific columns"],
    ),
    (
        "`CREATE ROLE reporting_app WITH LOGIN PASSWORD 'change_this_in_real_use';` creates a role, and `pg_roles` confirms `rolcanlogin` is true for it.\n\nWhat does the WITH LOGIN option specifically mark a role as?",
        "WITH LOGIN marks a role as one that can actually authenticate and open a connection, distinguishing it from a role created without login rights, which cannot connect to the database directly at all.",
        "easy", "understand", "users-and-roles-managing-database-accounts",
        "It marks a role as one that can actually authenticate and open a connection to the database",
        ["It marks a role as a member of every group role that currently exists", "It grants the role SELECT access on every table in the schema automatically", "It marks the role as read-only, unable to modify any data it can see"],
    ),
    (
        "`CREATE ROLE shipment_readers;` (no LOGIN option) is followed by `GRANT shipment_readers TO reporting_app;` and `GRANT shipment_readers TO dev_alia;`.\n\nWhat is the purpose of a role like shipment_readers that has no LOGIN option?",
        "It exists purely as a named bundle of permissions that other roles can be added to; nothing can connect to the database directly as shipment_readers, but any permission granted to it as a whole automatically applies to every member, the standard pattern for managing permissions at scale.",
        "medium", "understand", "users-and-roles-managing-database-accounts",
        "It exists purely as a named group bundling permissions, letting members inherit whatever is granted to the group as a whole, rather than repeating grants individually",
        ["It exists to temporarily disable login access for reporting_app and dev_alia during maintenance", "It exists only to log which roles have connected to the database recently", "It exists as a backup account in case reporting_app or dev_alia's passwords are forgotten"],
    ),
    (
        "`pg_stat_activity` records which role issued each active query, described as \"exactly the accountability a shared login destroys.\"\n\nWhy does a shared login destroy this kind of accountability, according to the lesson?",
        "If every developer and every application connected as one single, shared account, there would be no way to answer \"who ran this slow query\" or \"which service made this change\" after the fact, since the log would show only the one shared name for every action, regardless of who actually took it.",
        "medium", "analyze", "users-and-roles-managing-database-accounts",
        "With one shared account, the log shows only that one shared name for every action, making it impossible to determine who or what actually performed a specific action after the fact",
        ["A shared login destroys accountability because pg_stat_activity cannot log shared accounts at all", "A shared login is actually more accountable, since it centralizes all activity under one name", "This is only a problem if the shared login also has LOGIN privileges revoked"],
    ),
    (
        "`DROP ROLE shipment_readers;` succeeds in the lesson's example, but the lesson notes that \"in a real system with actual permissions and dependent objects attached to a role, PostgreSQL would refuse to drop it until those dependencies were resolved first.\"\n\nWhat is this refusal described as protecting against?",
        "A safeguard against silently breaking access for every account that depended on that role's permissions, preventing an accidental drop from quietly cutting off access for role members or dependent objects without anyone noticing.",
        "medium", "analyze", "users-and-roles-managing-database-accounts",
        "It's a safeguard against silently breaking access for every account that depended on that role's permissions, preventing an accidental drop from quietly cutting off dependent access",
        ["It protects against the role's password being reset without administrator approval", "It protects the database from running out of available role name slots", "It protects against the role being recreated with a different set of privileges later"],
    ),
    (
        "According to the \"Roles at a Glance\" table, what does `GRANT group_role TO member_role` do?",
        "It adds a role as a member of a group, letting that member inherit the group's permissions, the mechanism behind the shipment_readers pattern shown earlier in the lesson.",
        "medium", "remember", "users-and-roles-managing-database-accounts",
        "It adds a role as a member of a group role, so the member inherits the group's permissions",
        ["It permanently merges two roles into a single combined role", "It grants login rights to a role that previously had none", "It transfers ownership of a table from one role to another"],
    ),
]

PRIVILEGES_GRANT_REVOKE = [
    (
        "By default, a freshly created role can do almost nothing beyond connect; reporting_app cannot read a single row until it is explicitly told it is allowed to.\n\nWhat two commands does the lesson introduce as how PostgreSQL enforces exactly who can do exactly what?",
        "GRANT and REVOKE add and remove specific permissions, called privileges, on specific database objects for a specific role, together forming the mechanism PostgreSQL uses to enforce access.",
        "easy", "remember", "privileges-grant-revoke-and-role-hierarchies",
        "GRANT and REVOKE, which add and remove specific privileges on specific database objects for a specific role",
        ["CREATE and DROP, which add and remove entire roles from the database", "BEGIN and COMMIT, which control transaction boundaries for privilege changes", "ALTER and RENAME, which modify a role's name and login credentials"],
    ),
    (
        "After `GRANT SELECT ON shipments TO reporting_app;`, the lesson states reporting_app \"still has no ability to INSERT, UPDATE, or DELETE, since none of those privileges were ever granted.\"\n\nWhat general principle about PostgreSQL's privilege system does this illustrate?",
        "Every privilege in PostgreSQL works this way: nothing is allowed until it is explicitly granted, the opposite of a system that allows everything by default and requires explicit restriction.",
        "medium", "understand", "privileges-grant-revoke-and-role-hierarchies",
        "Nothing is allowed until it is explicitly granted, the opposite of a system that allows everything by default and requires explicit restriction",
        ["Every role automatically receives all privileges except the ones explicitly revoked", "GRANT SELECT automatically implies INSERT and UPDATE unless separately restricted", "Privileges granted on one table automatically extend to every other table in the schema"],
    ),
    (
        "`GRANT SELECT, INSERT, UPDATE ON shipments TO reporting_app;` is followed by `REVOKE UPDATE ON shipments FROM reporting_app;`.\n\nWhat privileges does reporting_app end up with, and what does this demonstrate about how REVOKE works?",
        "reporting_app is left with SELECT and INSERT intact, since REVOKE removed only the named UPDATE privilege, never accidentally sweeping away other permissions the role was separately granted — REVOKE is precise in exactly this targeted way.",
        "medium", "apply", "privileges-grant-revoke-and-role-hierarchies",
        "reporting_app ends up with SELECT and INSERT intact; REVOKE removes only the specifically named privilege without disturbing any other permissions the role holds",
        ["reporting_app ends up with no privileges at all, since REVOKE always clears every granted permission", "reporting_app keeps UPDATE but loses SELECT and INSERT instead", "REVOKE UPDATE also automatically revokes INSERT, since they were granted together in one statement"],
    ),
    (
        "`shipment_readers` is granted SELECT on shipments once, and dev_alia is added as a member via `GRANT shipment_readers TO dev_alia;`, without dev_alia ever being directly granted SELECT herself.\n\nWhat is \"the payoff of the group-role pattern\" the lesson describes here?",
        "Granting a new privilege to shipment_readers in the future instantly applies to every current and future member, without needing to remember and repeat the grant individually for each one, since dev_alia inherits the privilege purely through membership.",
        "medium", "analyze", "privileges-grant-revoke-and-role-hierarchies",
        "A future privilege granted to the group role instantly applies to every current and future member automatically, without needing to repeat the grant individually for each member role",
        ["The payoff is that dev_alia can now log in using shipment_readers' own credentials directly", "The payoff is that group roles automatically expire after a fixed time period, unlike individual grants", "The payoff is that dev_alia's own login password is now managed by shipment_readers"],
    ),
    (
        "`GRANT SELECT (shipment_id, status) ON shipments TO support_staff;` lets support_staff select shipment_id and status, but attempting to select amount as well would be rejected.\n\nWhy is this rejection expected, given exactly what was granted?",
        "The grant explicitly named only shipment_id and status as the columns support_staff can select, so a column-level privilege restricts access specifically to the named columns, and any column not included, like amount, remains inaccessible to that role.",
        "medium", "apply", "privileges-grant-revoke-and-role-hierarchies",
        "The grant explicitly named only shipment_id and status, so any column not included in that list, like amount, remains inaccessible to the role",
        ["The rejection is a bug, since GRANT SELECT on any columns should always unlock the entire table", "amount is rejected because it's a NUMERIC column, and column-level grants only work on TEXT columns", "support_staff was never actually granted SELECT at all in this example"],
    ),
    (
        "The \"Your Turn\" exercise notes that granting a fresh, unrestricted SELECT on the whole table to support_staff \"would have quietly widened support_staff's access to every column, amount included, overriding the earlier column-level grant rather than coexisting with it.\"\n\nWhat practical lesson does this warning illustrate about combining grants?",
        "A broader grant on the same object doesn't simply add to a narrower one while leaving the restriction intact; it can override and widen access beyond what was originally intended, so care is needed when adding new grants to avoid accidentally undoing an earlier, more restrictive one.",
        "hard", "analyze", "privileges-grant-revoke-and-role-hierarchies",
        "A broader grant on the same object can override and widen access beyond an earlier, more restrictive grant, rather than simply coexisting alongside it, so new grants must be added carefully",
        ["It illustrates that column-level and table-level grants can never both apply to the same role", "It illustrates that REVOKE must always be run before any new GRANT statement", "It illustrates that unrestricted SELECT grants are automatically rejected by PostgreSQL"],
    ),
]

LEAST_PRIVILEGE = [
    (
        "GRANT and REVOKE, covered in the previous lesson, are described as \"just tools; they say nothing about how much access any given role should actually have.\"\n\nWhat question does the principle of least privilege answer that GRANT and REVOKE alone do not?",
        "Least privilege answers how much access a role should actually have: exactly what it needs to do its job, and nothing more, not \"might need someday,\" not \"it's easier to just grant everything\" — a judgment question, not a syntax question.",
        "easy", "understand", "principle-of-least-privilege",
        "How much access a role should actually have: exactly what its job requires, and nothing more, a judgment call rather than something GRANT/REVOKE syntax decides on its own",
        ["It answers exactly which SQL syntax should be used to grant a given privilege", "It answers how many roles a single database should be allowed to have in total", "It answers whether a role should use LOGIN or non-LOGIN when it is created"],
    ),
    (
        "`GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO reporting_app;` gives a service that only needs to read shipment data full read, write, and delete access to every table, including payroll.\n\nWhat two risks does the lesson say follow directly from this kind of broad grant?",
        "If the reporting service ever had a bug, the actual damage possible is bounded only by what it was granted, not by what it was supposed to do; and if its credentials were ever compromised, that same boundary applies, and here that boundary is \"everything.\"",
        "medium", "analyze", "principle-of-least-privilege",
        "A bug's potential damage is bounded by what was granted rather than what was actually needed, and if credentials are compromised, an attacker's reach is bounded by that same overly broad grant",
        ["The two risks are that the grant runs slowly and that it consumes excessive disk space", "The two risks are that payroll data becomes permanently corrupted and that reporting_app can no longer log in", "The two risks are unrelated to security and concern only query performance"],
    ),
    (
        "After `REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM reporting_app;` followed by `GRANT SELECT ON shipments TO reporting_app;`, the lesson says the worst an attacker could do through this account, if compromised, is now \"read shipment data, not touch payroll, not delete anything.\"\n\nWhat does the lesson call this outcome?",
        "A dramatically smaller blast radius than the broad grant, since the account's actual capabilities are now bounded tightly to exactly what a reporting dashboard needs, limiting the worst-case damage from a compromise or bug.",
        "medium", "apply", "principle-of-least-privilege",
        "A dramatically smaller blast radius, since the account's capabilities are now tightly bounded to exactly what it needs, limiting worst-case damage from a compromise or bug",
        ["The lesson calls this outcome a complete elimination of all security risk for the account", "The lesson calls this outcome a temporary measure that should be reversed once testing completes", "The lesson calls this outcome a violation of the role hierarchy established in the previous lesson"],
    ),
    (
        "dev_alia, an individual developer debugging a shipment-tracking issue, is granted SELECT and UPDATE on shipments but nothing on payroll.\n\nThe lesson says if her responsibilities later genuinely expand, the fix is \"an additional, deliberate GRANT at that point, not a blanket grant made in advance 'just in case.'\" Why does the lesson insist on this specific ordering?",
        "Granting broad access in advance \"just in case\" is precisely the shortcut least privilege exists to avoid, since it grants speculative access before it's actually needed, carrying unnecessary risk the whole time it sits unused, rather than granting access only once a genuine, current need exists.",
        "medium", "analyze", "principle-of-least-privilege",
        "Granting broad access in advance carries unnecessary risk for however long it sits unused before (or if) it's ever actually needed, which is precisely the shortcut least privilege is meant to avoid",
        ["The ordering matters only because PostgreSQL technically cannot process two GRANT statements in one session", "It insists on this ordering because dev_alia's password would otherwise need to be reset", "The ordering is arbitrary and stated only as a stylistic preference with no security rationale"],
    ),
    (
        "`information_schema.role_table_grants` lists every privilege currently held by a given role, described as a way to check for \"some stale grant from an earlier, now-irrelevant task... still sitting there, unnoticed.\"\n\nWhy does the lesson emphasize that least privilege \"is not a one-time setup step\"?",
        "Permissions tend to accumulate over time as roles are granted access for a specific, temporary task and then never revisited, so periodically auditing what a role can actually do, compared to what it currently needs, is necessary to keep the principle from quietly eroding over the long run.",
        "medium", "understand", "principle-of-least-privilege",
        "Permissions tend to accumulate over time from temporary tasks that are never revisited, so periodic review is needed to catch stale access and keep the principle from eroding",
        ["Because PostgreSQL automatically re-grants all previously revoked privileges every 30 days", "Because information_schema.role_table_grants only shows results for the current session", "Because least privilege only applies to roles created within the last month"],
    ),
    (
        "According to the \"Least Privilege at a Glance\" table, what should the answer be to \"What is the worst outcome if this specific role's credentials leak?\"",
        "The answer should be small and specific, not \"everything,\" reflecting that a role's granted access should be narrow enough that a compromise has a clearly bounded, limited impact.",
        "medium", "remember", "principle-of-least-privilege",
        "The answer should be small and specific, not \"everything\"",
        ["The answer should always be that no data is ever accessible under any role", "The answer should be identical for every role in the database, regardless of its purpose", "The answer is not relevant to how privileges should actually be granted"],
    ),
]

ROW_AND_COLUMN_SECURITY = [
    (
        "A warehouse manager should see every shipment, but a branch coordinator should only see shipments belonging to their own branch, the same table, the same columns, restricted only by which rows.\n\nWhat does the lesson say PostgreSQL's row-level security (RLS) makes possible that column-level privileges alone cannot?",
        "RLS restricts access by which specific rows a role is allowed to see, enforced automatically by the database itself, rather than trusted to every application query remembering to add the right filter, addressing a dimension column-level grants don't cover.",
        "easy", "understand", "rowlevel-and-column-level-security",
        "It restricts access by which specific rows a role can see, enforced automatically by the database rather than relying on every application query to add the correct filter",
        ["It restricts access by which specific columns a role can see, identical to what column-level grants already do", "It restricts access by time of day, allowing queries only during business hours", "It restricts access by encrypting row data so only the row's original author can decrypt it"],
    ),
    (
        "Without row-level security, mumbai_coordinator's `GRANT SELECT` on shipments gives access to every row, Mumbai's and Pune's alike, relying entirely on every application query remembering to add `WHERE branch = 'Mumbai'` by hand.\n\nWhat specific risk does the lesson identify with this approach?",
        "Forgetting that filter even once, in one report, one script, one ad-hoc query, would leak Pune's shipment data to a role that should never see it, since nothing in the database itself enforces the restriction.",
        "medium", "analyze", "rowlevel-and-column-level-security",
        "Forgetting the WHERE filter even once, in any single report or script, would leak data belonging to a branch the role should never see, since nothing enforces the restriction automatically",
        ["The risk is that GRANT SELECT would fail outright without a WHERE clause specified in advance", "The risk is that mumbai_coordinator would be unable to connect to the database at all", "The risk is limited to slower query performance, not to any actual data exposure"],
    ),
    (
        "`SET ROLE mumbai_coordinator; SELECT * FROM shipments;` with no WHERE clause written at all still returns only the two Mumbai rows, once a row-level security policy is active.\n\nWhy does the lesson emphasize that this happens \"even without a WHERE clause\"?",
        "The entire point of row-level security is that it cannot be bypassed by simply forgetting to filter, since the database enforces the policy beneath the query itself, a guarantee application-side filtering alone could never provide, since that only protects queries that remembered to include it.",
        "medium", "analyze", "rowlevel-and-column-level-security",
        "It demonstrates that the database enforces the policy automatically beneath every query, a guarantee application-side filtering can't provide since that only protects queries that remembered to filter",
        ["It happens only because SET ROLE automatically injects a WHERE clause into every subsequent query", "It demonstrates a bug in the policy that should be reported, since RLS is expected to require a WHERE clause", "It happens because mumbai_coordinator has no SELECT privilege at all on the table"],
    ),
    (
        "`shipments_with_cost` combines a row-level policy restricting mumbai_coordinator to branch = 'Mumbai' with a column-level grant limiting the role to shipment_id, branch, and status, leaving internal_cost withheld entirely.\n\nWhat does this combination demonstrate about how row-level and column-level security interact?",
        "The two mechanisms can be combined on the same table, restricting both which columns and which rows a role can see at once, addressing both dimensions of \"this role should not see that data\" together, both enforced automatically on every query.",
        "medium", "apply", "rowlevel-and-column-level-security",
        "They can be combined on the same table to restrict both dimensions, which rows and which columns, together, both enforced automatically on every query the role runs",
        ["The two mechanisms are mutually exclusive and cannot both be applied to the same table", "Column-level grants automatically override any row-level policy defined on the same table", "Row-level security only works if no column-level grants exist on the same table"],
    ),
    (
        "The lesson describes row-level security as enforced by the database \"on every query, cannot be bypassed by an incomplete WHERE.\"\n\nWhy does this specific phrasing matter compared to relying on developers to write correct WHERE clauses in every query?",
        "It matters because the enforcement doesn't depend on any individual developer's diligence or memory across every query ever written; a single missed filter anywhere would otherwise leak data, but RLS removes that dependency entirely by enforcing the restriction inside the database itself, for every query, without exception.",
        "hard", "analyze", "rowlevel-and-column-level-security",
        "Enforcement doesn't depend on developer diligence across every query ever written; RLS removes that dependency by enforcing the restriction inside the database itself for every query, without exception",
        ["The phrasing only matters for SELECT statements and has no bearing on UPDATE or DELETE", "It matters because WHERE clauses are syntactically forbidden once RLS is enabled on a table", "It matters only for performance reasons, not for correctness or security"],
    ),
    (
        "According to the \"Row-Level and Column-Level Security at a Glance\" table, how is a row-level security policy enforced, compared to an incomplete WHERE clause?",
        "It's enforced by the database, on every query, and specifically cannot be bypassed by an incomplete WHERE, unlike relying on application code to remember to filter correctly.",
        "medium", "remember", "rowlevel-and-column-level-security",
        "It's enforced by the database on every query, and cannot be bypassed by an incomplete WHERE clause",
        ["It's enforced only when the query explicitly includes a matching WHERE clause", "It's enforced by the application layer, not by the database itself", "It's enforced only for INSERT and UPDATE statements, never for SELECT"],
    ),
]

SQL_INJECTION_PREVENTION = [
    (
        "The lesson revisits SQL injection, describing it as \"one of the most common, most damaging vulnerabilities in real software,\" precisely because building SQL by string concatenation \"is so easy to write without realizing the danger.\"\n\nWhat does the more damaging example, `shipment_id_input = \"1; DROP TABLE shipments; --\"`, illustrate beyond the earlier example that just returned extra rows?",
        "A real injection can go much further than reading extra rows: it can delete, modify, or destroy data entirely, and depending on the database account's granted privileges, it can reach into tables the application was never designed to touch at all.",
        "easy", "understand", "sql-injection-prevention",
        "A real injection can delete, modify, or destroy data entirely, and depending on the account's privileges, reach into tables the application was never designed to touch at all",
        ["It illustrates that injection can only ever affect the specific table named in the original query", "It illustrates that injection is limited strictly to read-only operations like extra SELECT results", "It illustrates that injection requires physical access to the database server itself"],
    ),
    (
        "For `PREPARE get_shipment (INTEGER) AS SELECT * FROM shipments WHERE shipment_id = $1;`, a value like `1; DROP TABLE shipments; --` supplied to `$1` would be \"rejected outright with a type error before the query ever ran.\"\n\nWhy specifically does this happen for an INTEGER-typed parameter?",
        "PostgreSQL refuses to treat that text as a valid integer in the first place, since the parameter is declared as INTEGER, so a value that isn't a valid integer fails type validation before the query can even execute, regardless of what SQL-like text it contains.",
        "medium", "analyze", "sql-injection-prevention",
        "PostgreSQL refuses to treat the text as a valid integer, since the parameter is declared INTEGER, so it fails type validation before the query can even execute, regardless of any SQL-like content in the string",
        ["It happens because PREPARE statements automatically scan for the word DROP and block it specifically", "It happens because $1 placeholders are always converted to TEXT type regardless of declaration", "It happens only because the shipments table has a PRIMARY KEY constraint on shipment_id"],
    ),
    (
        "The lesson says prepared statements prevent injection \"by construction,\" rather than by filtering or detecting dangerous input.\n\nWhat is the distinction being drawn here between \"by construction\" and a filtering-based approach like checking input for semicolons or the word DROP?",
        "\"By construction\" means the vulnerability has no path to exist in the first place, since a parameter is never treated as SQL syntax regardless of its content; a filtering approach instead depends on the validation logic anticipating every possible dangerous pattern, which can still be bypassed by encoding, case variations, or constructs the validation didn't anticipate.",
        "medium", "analyze", "sql-injection-prevention",
        "\"By construction\" means the vulnerability has no path to exist at all, since a parameter is never treated as SQL syntax; filtering instead depends on anticipating every dangerous pattern, which can be bypassed by unanticipated encodings or constructs",
        ["There is no real distinction; both approaches provide exactly the same guarantee against injection", "Filtering-based approaches are actually more reliable, since they can be updated as new attacks emerge", "\"By construction\" means the database physically deletes any semicolon found in a query before running it"],
    ),
    (
        "The lesson states input validation \"still has real value... but it should never be relied upon as the sole defense against injection; that role belongs to prepared statements.\"\n\nWhat specific real value does input validation retain, according to the lesson, even though it isn't a substitute for prepared statements?",
        "Rejecting obviously malformed input early, improving error messages, and catching genuine mistakes are the real values input validation retains, even though it cannot serve as the sole or primary defense against injection the way prepared statements can.",
        "medium", "understand", "sql-injection-prevention",
        "Rejecting obviously malformed input early, improving error messages, and catching genuine mistakes, even though it can't serve as the primary defense against injection",
        ["Input validation's only real value is blocking every possible SQL injection attempt completely on its own", "Input validation has no real value at all and should be removed entirely from application code", "Input validation's real value is that it replaces the need for database-level privilege restrictions"],
    ),
    (
        "A `web_app` role granted only SELECT and INSERT on shipments, with no DELETE and no DROP privilege, \"could not have actually executed the destructive DROP TABLE shipments attempted in the earlier example, even in a world where the injection itself had somehow succeeded.\"\n\nWhat does this demonstrate about how least privilege functions as a layer of defense here?",
        "Even if prepared statements somehow failed to prevent an injection, the least-privilege principle bounds the actual damage possible to whatever the compromised account was genuinely granted, meaning a role with no DROP privilege simply cannot execute a DROP, regardless of what SQL text an attacker manages to inject.",
        "hard", "analyze", "sql-injection-prevention",
        "Least privilege bounds the damage possible to whatever the account was genuinely granted, so a role with no DROP privilege cannot execute a DROP even if an injection somehow succeeded, providing defense in depth",
        ["It demonstrates that least privilege makes prepared statements entirely unnecessary as a defense", "It demonstrates that web_app's SELECT and INSERT grants would also block a successful DROP TABLE attack through some other mechanism", "It demonstrates that least privilege only matters for services, not for preventing SQL injection specifically"],
    ),
    (
        "According to the \"SQL Injection Prevention at a Glance\" table, what role does least privilege play in the defense-in-depth model described?",
        "Defense in depth: it bounds the damage if some other, unanticipated flaw is ever exploited, complementing prepared statements as the primary defense rather than replacing it.",
        "medium", "remember", "sql-injection-prevention",
        "Defense in depth — it bounds the damage if some other flaw is ever exploited, complementing rather than replacing prepared statements as the primary defense",
        ["Least privilege is listed as the primary defense, replacing the need for prepared statements", "Least privilege is listed as having no relevant role in preventing SQL injection at all", "Least privilege is listed as a substitute for input validation, not a separate layer"],
    ),
]

AUDITING_AND_TRACKING = [
    (
        "Roles, privileges, least privilege, row-level security, and injection prevention all work to prevent unwanted access before it happens.\n\nHow does the lesson describe auditing as the \"complementary discipline\" to these prevention mechanisms?",
        "Auditing is the complementary discipline for after the fact: recording who did what and when, so that if something goes wrong, or simply needs reviewing later, the team has an actual trail to examine instead of forcing everyone to guess.",
        "easy", "understand", "auditing-and-tracking-data-access",
        "Auditing works for after the fact, recording who did what and when, giving the team an actual trail to examine instead of forcing everyone to guess when something needs reviewing",
        ["Auditing replaces the need for row-level security and least privilege entirely", "Auditing is a mechanism that actively blocks unauthorized access before it can happen", "Auditing works exclusively before an action happens, identical in role to GRANT and REVOKE"],
    ),
    (
        "Inside `audit_shipments_change()`, `TG_OP` and `current_user` are both referenced when inserting into audit_log.\n\nWhat does each of these two values specifically capture?",
        "TG_OP is a special variable automatically available inside a trigger function, holding the operation that fired it ('INSERT', 'UPDATE', or 'DELETE'), while current_user captures exactly which role's connection made the change, tying every audit entry back to a specific, accountable identity.",
        "medium", "remember", "auditing-and-tracking-data-access",
        "TG_OP captures which operation fired the trigger (INSERT, UPDATE, or DELETE), and current_user captures exactly which role made the change",
        ["TG_OP captures the table's name, and current_user captures the timestamp of the change", "TG_OP captures the old row's values, and current_user captures the new row's values", "TG_OP and current_user both capture the same thing: the role that owns the audited table"],
    ),
    (
        "`to_jsonb(OLD)` and `to_jsonb(NEW)` capture a row's full contents before and after a change as flexible JSON, stored in a single generic audit_log table.\n\nWhy does the lesson say this lets \"one generic audit table handle any table's structure without needing a matching column-for-column schema of its own\"?",
        "Since the old and new row data are stored as flexible JSON rather than fixed, named columns matching each audited table's own structure, the same audit_log table can capture changes from any table's rows, regardless of what columns that particular table happens to have.",
        "medium", "analyze", "auditing-and-tracking-data-access",
        "Storing row data as flexible JSON, rather than fixed columns matching each table's structure, lets the same audit_log table capture changes from any table regardless of its specific columns",
        ["It's because JSONB automatically compresses data, making the audit_log table smaller than the original tables", "It's because to_jsonb() only works on tables that already have a JSONB column defined", "It's because JSON data cannot be queried, so no schema is needed to store it"],
    ),
    (
        "After `UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;`, the audit entry shows action = 'UPDATE', changed_by recording the role, and both old_data (status: in_transit) and new_data (status: delivered).\n\nWhat does the lesson call this level of detail?",
        "A complete, precise record: not just that something changed, but exactly what changed, who changed it, and when, capturing the full before-and-after state alongside the identity of whoever made the change.",
        "medium", "apply", "auditing-and-tracking-data-access",
        "A complete, precise record capturing exactly what changed, who changed it, and when, not just the fact that a change occurred",
        ["A partial record, since the audit log only captures that a change happened without any further detail", "An incomplete record, since old_data and new_data cannot both be populated for the same UPDATE", "A duplicate of the shipments table itself, offering no additional information"],
    ),
    (
        "The lesson explains a trigger naturally captures INSERT, UPDATE, and DELETE, but auditing \"who read this sensitive data\" is \"a genuinely different, harder problem, since a plain SELECT does not fire a trigger at all.\"\n\nHow does PostgreSQL address auditing reads instead, and what cost does the lesson attach to it?",
        "PostgreSQL addresses this through server-level logging configuration (like log_statement) and extensions purpose-built for statement auditing, tracking every query against the server, but enabling comprehensive read-level auditing has a real performance cost, since every query then incurs additional logging overhead, which is why it's typically reserved for especially sensitive tables rather than applied database-wide.",
        "hard", "analyze", "auditing-and-tracking-data-access",
        "Through server-level logging settings like log_statement and purpose-built extensions, tracking every query; this has a real performance cost from added logging overhead on every query, so it's typically reserved for especially sensitive tables rather than applied database-wide",
        ["PostgreSQL addresses this by silently converting every SELECT into an UPDATE so a trigger can fire", "PostgreSQL cannot audit reads under any circumstances, making this an unsolvable limitation", "Read auditing is handled entirely by the same trg_audit_shipments trigger used for writes, with no extra cost"],
    ),
    (
        "The lesson states an audit trail \"does not stop an unauthorized action from happening; row-level security, least privilege, and careful GRANTs are what actually prevent it.\"\n\nWhat three purposes does the lesson list auditing as serving instead, purposes prevention alone cannot fully cover?",
        "Detecting misuse by someone who did have legitimate access, investigating an incident after the fact to understand exactly what happened, and satisfying compliance requirements that specifically demand a record of who touched sensitive data, independent of whether that access was ultimately appropriate.",
        "medium", "remember", "auditing-and-tracking-data-access",
        "Detecting misuse by someone with legitimate access, investigating incidents after the fact, and satisfying compliance requirements demanding a record of who touched sensitive data",
        ["Blocking unauthorized writes, encrypting sensitive columns, and enforcing password complexity rules", "Speeding up query performance, reducing storage costs, and simplifying schema migrations", "Replacing the need for row-level security, replacing least privilege, and replacing GRANT statements"],
    ),
]

SYNTHESIS = [
    (
        "The users-and-roles lesson establishes that shared logins destroy accountability, since pg_stat_activity would show only one shared name for every action. The auditing lesson's trigger captures current_user for every INSERT, UPDATE, and DELETE.\n\nHow does the auditing lesson's use of current_user directly depend on the discipline established in the users-and-roles lesson?",
        "current_user inside a trigger can only meaningfully identify who made a change if each person or service actually connects under its own distinct role rather than a shared login; if everyone shared one login, current_user would capture that same shared name for every audit entry, recreating exactly the accountability problem the roles lesson warned against, just inside the audit log instead of pg_stat_activity.",
        "medium", "analyze", "auditing-and-tracking-data-access",
        "current_user can only meaningfully identify who made a change if each person/service uses its own distinct role; with a shared login, every audit entry would show the same shared name, recreating the exact accountability problem the roles lesson warned against",
        ["The two lessons are unrelated, since current_user works identically regardless of whether logins are shared", "Auditing eliminates the need for separate roles entirely, since it tracks changes on its own", "current_user only functions correctly when row-level security is also enabled on the audited table"],
    ),
    (
        "The least-privilege lesson shows reporting_app's blast radius shrinking from \"everything\" to just SELECT on shipments. The SQL-injection lesson shows a web_app role with only SELECT and INSERT being unable to execute a DROP TABLE, even if an injection somehow succeeded.\n\nHow does the injection-prevention lesson's example serve as a concrete demonstration of the earlier least-privilege lesson's abstract \"blast radius\" argument?",
        "The least-privilege lesson argues in the abstract that a smaller grant means a smaller worst-case outcome if credentials are compromised; the injection lesson makes this concrete with a specific attack scenario, showing that a role without DROP privilege literally cannot execute a DROP regardless of what malicious SQL text an attacker manages to inject, proving the abstract blast-radius argument with a real, specific mechanism of compromise.",
        "hard", "analyze", "sql-injection-prevention",
        "The least-privilege lesson argues abstractly that a smaller grant means smaller worst-case damage if compromised; the injection lesson makes this concrete by showing a role without DROP privilege literally cannot execute a DROP even via a successful injection attack",
        ["The two lessons contradict each other, since injection prevention argues privileges don't actually matter", "The injection lesson shows that least privilege only matters for services, not for the specific case of SQL injection", "The connection is that least privilege prevents injection attacks from being attempted in the first place"],
    ),
    (
        "The privileges lesson shows column-level GRANT restricting which columns support_staff can see. The row-and-column-security lesson combines a row-level policy with a column-level grant on shipments_with_cost, restricting both rows and columns for mumbai_coordinator at once.\n\nHow does the row-and-column-security lesson build directly on the column-level mechanism already introduced in the earlier privileges lesson?",
        "The privileges lesson previews column-level restriction as a narrower form of the same GRANT command already covered for whole tables; the row-and-column-security lesson then adds a second, independent restriction dimension (rows, via CREATE POLICY) on top of that same column-level GRANT mechanism, showing the two can be layered together rather than needing to choose one or the other.",
        "medium", "analyze", "rowlevel-and-column-level-security",
        "The privileges lesson introduces column-level GRANT as a narrower form of the same command used for whole tables; the row-and-column-security lesson then layers a separate row-restricting mechanism (CREATE POLICY) on top of that same column-level GRANT, combining both dimensions",
        ["The two lessons are unrelated, since row-level security replaces the need for column-level grants entirely", "Column-level grants automatically disable any row-level policy applied to the same table", "The row-and-column-security lesson only works if column-level grants were never used on the table"],
    ),
    (
        "The prepared-statements coverage in this chapter's SQL-injection lesson explicitly says it \"revisits the mechanism in more depth\" from the application-code chapter. The auditing lesson closes the security chapter by saying security \"has been addressed from every angle this course covers.\"\n\nHow do the six lessons in this chapter, roles, privileges, least privilege, row/column security, injection prevention, and auditing, collectively form a layered security model, based on what each one specifically contributes?",
        "Roles establish accountable identity, privileges (via GRANT/REVOKE) control what each identity can do, least privilege ensures those grants stay minimal, row/column security narrows access further to specific data within an object, injection prevention protects the mechanism by which access is exercised from being subverted, and auditing provides the after-the-fact record when all of that still needs review, together covering identity, authorization scope, minimization, granularity, structural safety, and accountability as distinct, complementary layers.",
        "hard", "analyze", "principle-of-least-privilege",
        "Together they cover distinct layers: roles establish identity, privileges control capability, least privilege minimizes that capability, row/column security narrows it to specific data, injection prevention protects the access mechanism itself, and auditing records activity after the fact — each addressing a different angle rather than duplicating the others",
        ["All six lessons address exactly the same concern, injection prevention, from six different syntactic angles", "The six lessons are ordered by decreasing importance, with roles being the only one that actually matters in practice", "Auditing alone is sufficient to replace all five of the other mechanisms covered earlier in the chapter"],
    ),
]

SET1_SOURCES = [
    (USERS_AND_ROLES, 0),
    (PRIVILEGES_GRANT_REVOKE, 0),
    (LEAST_PRIVILEGE, 0),
    (ROW_AND_COLUMN_SECURITY, 0),
    (SQL_INJECTION_PREVENTION, 0),
    (AUDITING_AND_TRACKING, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    USERS_AND_ROLES[1:]
    + PRIVILEGES_GRANT_REVOKE[1:]
    + LEAST_PRIVILEGE[1:]
    + ROW_AND_COLUMN_SECURITY[1:]
    + SQL_INJECTION_PREVENTION[1:]
    + AUDITING_AND_TRACKING[1:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "going-to-production",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 8.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 8.3.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DBMS - MCQ - Unit 8.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 8 - Going to Production/8.3 - Database Security - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")

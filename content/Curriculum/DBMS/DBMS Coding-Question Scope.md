# DBMS Coding-Question Scope

Source of truth for chapters: `Course Blueprint for RDBMS.xlsx`, sheet `Syllabus`
(Unit -> Chapter -> Topic). This note records which chapters get a 20-30
question coding bank (Postgres + MySQL solutions each) versus reading
material only. Judgment call made 2026-07-08; revisit if the blueprint
changes.

**Rule of thumb applied:** a chapter is coding-eligible if its topics are
runnable SQL a student types and executes. Chapters that are pure setup,
internals, or policy/theory (no SQL a learner writes) are reading-only.

## In scope for coding-question banks

| Unit | Chapter |
|---|---|
| 3. SQL Essentials | Reading Data with SELECT |
| 3. SQL Essentials | Filtering Data |
| 3. SQL Essentials | Modifying Data |
| 4. SQL for Data Retrieval and Analytics | Transforming Data |
| 4. SQL for Data Retrieval and Analytics | Aggregation |
| 4. SQL for Data Retrieval and Analytics | Joins |
| 4. SQL for Data Retrieval and Analytics | Set Operations and Combining Queries |
| 5. Advanced Querying with SQL | Subqueries and CTEs |
| 5. Advanced Querying with SQL | Window Functions |
| 6. Transactions & Reliability | Transactions and ACID |
| 7. Performance | Indexes |
| 7. Performance | Query Optimization |
| 8. Going to Production | Views and Programmability |

That is 13 chapters. At 20-30 questions per chapter this is roughly
260-390 coding questions.

**Dialect decision (2026-07-17, revises the note below):** PostgreSQL only,
no MySQL solutions. Every lesson in this course uses Postgres-only syntax
throughout (SERIAL, plpgsql, JSONB, RETURNING, ON CONFLICT, row-level
security, pg_stat_activity, etc.), and several in-scope chapters (Transactions
and ACID's procedural examples, Views and Programmability's triggers) have no
real MySQL equivalent for parts of what they teach. The uploader's own
language mechanism is also all-or-nothing per question (enabling multiple
languages exposes a student to 5 language options, but only the ones with
real solutions actually work), so a partial dual-dialect approach would risk
shipping broken language choices.

## Reading-only (no coding bank)

| Unit | Chapter | Why excluded |
|---|---|---|
| 1. Database Foundations | What is a Database?, The Relational Model, DBMS Architecture, Relational Algebra | Conceptual; no SQL yet |
| 2. Database Design & Modeling | ER Modeling, Normalization, Practical Schema Design | Design theory, diagrams, not query-writing |
| 3. SQL Essentials | Setting Up Your Environment | Install/tooling, not coding practice |
| 6. Transactions & Reliability | Concurrency Control, Recovery | Internals (locks, WAL, checkpoints); little runnable code a learner writes |
| 7. Performance | Storage and File Organization | Internals, no learner-written SQL |
| 8. Going to Production | Using Databases from Application Code | Application-layer, not SQL coding |
| 8. Going to Production | Database Security | Mostly policy/theory; GRANT/REVOKE mechanics get light coverage in reading material only |
| 8. Going to Production | Database Administration Basics | Ops procedures, not coding |

## Notes

- Every reading-material lesson in ALL units still gets runnable SQL/prose
  examples embedded via the OneCompiler fence-info convention where the
  topic is hands-on; the distinction above is only about whether a
  standalone Question Bank workbook is built for that chapter.
- Build system: `content/Question Bank/Coding Questions/DBMS/_generator/dbms_cqlib.py`
  extends the Python cqlib.py pattern for PostgreSQL-only questions. No local
  Postgres/Docker is available in this environment, so each question's expected
  output is computed by a Python "oracle" function run against the same
  in-memory table data used to generate `preloadCode_postgresql`'s INSERT
  statements (via `sql_insert`), rather than executed against a real database
  or hand-typed. The SQL solution <-> Python oracle equivalence is a manual
  claim, not an executed one -- treat as a real (if lower) residual risk
  compared to the Python bank's fully-executed verification.
- Output convention: a header row (exact column/alias names the query
  produces), then one comma-separated data row per line, NULL rendered as the
  literal text `NULL`. This is a project convention, not a confirmed spec of
  ByteXL's actual SQL grader (no sample DBMS coding-question file or live
  grader was available to reverse-engineer it against). Revisit if upload
  validation reveals a different expected format.
- Progress: 3.2 Reading Data with SELECT (27), 3.3 Filtering Data (29), 3.4
  Modifying Data (32), 4.1 Transforming Data (30), 4.2 Aggregation (28), 4.3
  Joins (34), 4.4 Set Operations (22), 5.1 Subqueries and CTEs (32), 5.2
  Window Functions (33), 6.1 Transactions and ACID (25), 7.2 Indexes (23),
  7.3 Query Optimization (14, deliberately reduced set) done -- 329
  questions across 12 of 13 chapters. Remaining 1 chapter not yet started:
  8.1 Views and Programmability.
- 7.2 is heavily EXPLAIN-plan and pg_relation_size based in the lesson text,
  neither of which is gradeable via fixed-output comparison (planner cost
  estimates and exact plan text aren't reproducible without a live server).
  Every question instead pairs a CREATE INDEX with a query whose RETURNED
  DATA is correct regardless of whether the planner uses that index; where a
  question confirms an index exists, it checks pg_indexes.indexname only,
  never indexdef's reconstructed definition text (schema-qualification,
  explicit casts, and function-name casing in that text aren't verifiable
  without a live server either).
- 7.3 faced the same EXPLAIN-unpredictability constraint as 7.2, even more
  acutely -- confirmed with the user before building, who chose a smaller,
  best-effort set (14 questions instead of the usual 20-30) rather than
  forcing full coverage or skipping the chapter outright. reading-explain
  has zero questions (no gradeable angle exists: the lesson content IS the
  plan text). inside-the-query-optimizer is reduced to COUNT-based
  selectivity questions (row counts the optimizer's decision is based on,
  not the decision itself). reading-explain-analyze has one question testing
  the lesson's own ROLLBACK-wrapped-write safety pattern. join-algorithms
  and common-bottlenecks test the queries' returned data, which is correct
  regardless of which algorithm/access-path the planner actually picks.
  iterative-performance-tuning tests the underlying aggregation query and
  index creation, not the measure/remeasure timing workflow itself.
- 6.1 is a documented exception to the single-RETURNING-statement rule: a
  transaction is inherently multi-statement (BEGIN...COMMIT/ROLLBACK), so
  every solution there is a short script graded on its final SELECT. No
  solution ever executes a statement that would actually violate a
  CHECK/FK constraint, since that would raise a hard Postgres error and
  abort the script before any gradeable output -- atomicity/consistency
  questions are framed as the positive case (valid transactions respecting
  a constraint) instead. Crash survival and cross-session concurrent
  visibility are not testable via SQL at all and are left to the MCQ bank.
- ROW_NUMBER questions (5.2) add a deterministic secondary ORDER BY key
  inside OVER(...), since the lesson itself states ROW_NUMBER breaks ties
  "arbitrarily" -- unsafe for exact-match grading. RANK/DENSE_RANK don't need
  that fix (tied rows always get the identical rank value), but every
  ranking question still adds an explicit outer ORDER BY, since a window
  function's OVER(...) ordering never controls the query's own displayed row
  order.
- Recursive-CTE questions (5.1) are verified with small walk_up/walk_down
  BFS helpers (in build_5_1_coding.py) that replicate the recursive CTE's
  own round-by-round evaluation, so level numbers and same-level row order
  come from code execution, not hand-tracing.
- Join questions (4.3) use small Python inner_join/left_join/right_join/
  full_outer_join helpers (in build_4_3_coding.py) that replicate SQL join
  semantics directly against the in-memory dataset, so join logic is
  verified by code execution rather than hand-traced per question.
- Modification questions (3.4) always use a single RETURNING statement, never
  a write followed by a separate verification SELECT, since multi-statement
  output-capture semantics are unconfirmed for this grader.
- Numeric columns are modeled as Python decimal.Decimal (never float), with
  ROUND_HALF_UP rounding to match PostgreSQL's numeric type exactly
  (trailing zeros, scale-preserving arithmetic). NOW()/CURRENT_DATE/AGE(NOW())
  are never used in a graded solution since their output isn't reproducible;
  deterministic EXTRACT and fixed-literal date arithmetic substitute where a
  lesson's own examples use "today" as a reference point.

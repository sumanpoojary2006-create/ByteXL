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
260-390 coding questions, each shipped with a Postgres solution and a
MySQL solution (dialect differences noted inline where the two diverge,
e.g. LIMIT/OFFSET vs FETCH, string concatenation, UPSERT syntax).

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
- Dual-solution requirement: every coding question in an in-scope chapter
  ships `solution_postgresql` and `solution_mysql` (and matching
  `preloadCode_*` where a chapter needs a pre-seeded schema). This extends
  `cqlib.py`'s column schema (Python-only today) with a `_generator/` for
  DBMS; see the coding-question generator work item.

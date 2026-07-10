# Transactions & Reliability

**Database Management Systems**

Goal of this unit: Build reliable database applications that preserve consistency and correctness.

## Chapters and Topics (teach in order)

### Transactions and ACID

| # | Topic | File |
|---|-------|------|
| 1 | What is a Transaction? | [01_what_is_a_transaction.md](6.1%20-%20Transactions%20and%20ACID/01_what_is_a_transaction.md) |
| 2 | Atomicity: All or Nothing | [02_atomicity_all_or_nothing.md](6.1%20-%20Transactions%20and%20ACID/02_atomicity_all_or_nothing.md) |
| 3 | Consistency: Valid States Only | [03_consistency_valid_states_only.md](6.1%20-%20Transactions%20and%20ACID/03_consistency_valid_states_only.md) |
| 4 | Isolation: Running Transactions Safely Together | [04_isolation_running_transactions_safely_together.md](6.1%20-%20Transactions%20and%20ACID/04_isolation_running_transactions_safely_together.md) |
| 5 | Durability: Surviving a Crash | [05_durability_surviving_a_crash.md](6.1%20-%20Transactions%20and%20ACID/05_durability_surviving_a_crash.md) |

### Concurrency Control

| # | Topic | File |
|---|-------|------|
| 1 | Why Concurrency Control is Needed? | [01_why_concurrency_control_is_needed.md](6.2%20-%20Concurrency%20Control/01_why_concurrency_control_is_needed.md) |
| 2 | Concurrency Problems | [02_concurrency_problems.md](6.2%20-%20Concurrency%20Control/02_concurrency_problems.md) |
| 3 | Locking | [03_locking.md](6.2%20-%20Concurrency%20Control/03_locking.md) |
| 4 | Isolation Levels | [04_isolation_levels.md](6.2%20-%20Concurrency%20Control/04_isolation_levels.md) |
| 5 | Deadlocks | [05_deadlocks.md](6.2%20-%20Concurrency%20Control/05_deadlocks.md) |
| 6 | Serializability | [06_serializability.md](6.2%20-%20Concurrency%20Control/06_serializability.md) |

### Recovery

| # | Topic | File |
|---|-------|------|
| 1 | Database Failures | [01_database_failures.md](6.3%20-%20Recovery/01_database_failures.md) |
| 2 | Write-Ahead Logging (WAL) | [02_writeahead_logging.md](6.3%20-%20Recovery/02_writeahead_logging.md) |
| 3 | Checkpoints: Bounding How Far Back Recovery Must Go | [03_checkpoints_bounding_how_far_back_recovery_must_go.md](6.3%20-%20Recovery/03_checkpoints_bounding_how_far_back_recovery_must_go.md) |
| 4 | Undo and Redo: How a Database Rolls Back and Replays | [04_undo_and_redo_how_a_database_rolls_back_and_replay.md](6.3%20-%20Recovery/04_undo_and_redo_how_a_database_rolls_back_and_replay.md) |
| 5 | Transactions in Application Code | [05_transactions_in_application_code.md](6.3%20-%20Recovery/05_transactions_in_application_code.md) |

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples under natural headings, runnable SQL examples embedded via OneCompiler, and a closing **Conclusion**. No emojis, no em dashes, no forward or backward references to other units or chapters.

_Status: all 16 lessons authored and reviewed._

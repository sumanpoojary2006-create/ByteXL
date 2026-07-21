# Unit 12: Exception Handling

**Semester 1: Python Fundamentals**

Write robust programs that anticipate and recover from failure.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | What Are Errors? Syntax vs. Runtime vs. Logic | [01_what_are_errors_syntax_vs_runtime_vs_logic.md](01_what_are_errors_syntax_vs_runtime_vs_logic.md) |
| 2 | Reading a Traceback Bottom-Up | [02_reading_a_traceback_bottomup.md](02_reading_a_traceback_bottomup.md) |
| 3 | try and except | [03_try_and_except.md](03_try_and_except.md) |
| 4 | Handling Multiple and Specific Exceptions | [04_handling_multiple_and_specific_exceptions.md](04_handling_multiple_and_specific_exceptions.md) |
| 5 | else and finally | [05_else_and_finally.md](05_else_and_finally.md) |
| 6 | Raising Exceptions with raise | [06_raising_exceptions_with_raise.md](06_raising_exceptions_with_raise.md) |
| 7 | Creating Custom Exceptions | [07_creating_custom_exceptions.md](07_creating_custom_exceptions.md) |
| 8 | Validating Input Defensively | [08_validating_input_defensively.md](08_validating_input_defensively.md) |
| 9 | Errors as Part of Robust Program Design | [09_errors_as_part_of_robust_program_design.md](09_errors_as_part_of_robust_program_design.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples and situation-based questions under natural headings, a concept-scoped illustration, and a closing **Conclusion**. Plain-English explanations are preferred; Python code is kept simple and interactive. No emojis, no em dashes.

Lessons continue Asha's thread from Unit 3: her signup form that could reject bad input but never re-ask or survive a bad conversion. This unit closes that gap, moving from telling errors apart, to reading a traceback, to `try`/`except`, multiple and specific exception types, `else`/`finally`, raising her own exceptions, naming her own exception types, and finally combining a loop with `try`/`except` into the complete defensive validation pattern the control flow unit promised was coming. The closing lesson steps back to the design question of when to fail gracefully versus fail loudly.

_Status: lesson content authored for all 9 topics, all code blocks verified to run correctly and match documented output, including intentional error demonstrations._

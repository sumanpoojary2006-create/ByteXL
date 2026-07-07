# Unit 13: Debugging

**Semester 1: Python Fundamentals**

Find and fix bugs systematically: the most practical real-world skill.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | The Debugging Mindset: Errors Are Normal | [01_the_debugging_mindset_errors_are_normal.md](01_the_debugging_mindset_errors_are_normal.md) |
| 2 | Print Debugging and Reading Output | [02_print_debugging_and_reading_output.md](02_print_debugging_and_reading_output.md) |
| 3 | Using assert for Sanity Checks | [03_using_assert_for_sanity_checks.md](03_using_assert_for_sanity_checks.md) |
| 4 | The Python Debugger (pdb / breakpoints) | [04_the_python_debugger.md](04_the_python_debugger.md) |
| 5 | Stepping, Inspecting Variables, and the Call Stack | [05_stepping_inspecting_variables_and_the_call_stack.md](05_stepping_inspecting_variables_and_the_call_stack.md) |
| 6 | Logging Basics: logging vs print | [06_logging_basics_logging_vs_print.md](06_logging_basics_logging_vs_print.md) |
| 7 | Isolating a Minimal Failing Case | [07_isolating_a_minimal_failing_case.md](07_isolating_a_minimal_failing_case.md) |
| 8 | Rubber-Duck Debugging and Asking Good Questions | [08_rubberduck_debugging_and_asking_good_questions.md](08_rubberduck_debugging_and_asking_good_questions.md) |
| 9 | AI-Assisted Debugging (Used Responsibly) | [09_aiassisted_debugging.md](09_aiassisted_debugging.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples and situation-based questions under natural headings, a concept-scoped illustration, and a closing **Conclusion**. Plain-English explanations are preferred; Python code is kept simple and interactive. No emojis, no em dashes.

Lessons follow Zara, a first-year debugging her first multi-file class project (an RSVP tracker split across an `Attendee` class, an `Event` class, and a CSV loader) the night before a deadline: reframing a crash from personal failure to plain information, tracing values with deliberate print statements, stating assumptions with `assert`, pausing and stepping through a live program with `breakpoint()` and `pdb`, following the call stack across nested calls, replacing scattered prints with leveled `logging`, isolating a minimal failing case, explaining the problem out loud before asking for help, and finally using an AI assistant responsibly, verifying any suggested fix the same way she would verify her own code. Because this unit follows exception handling, `try`/`except` is available and used where it genuinely fits, alongside every debugging tool introduced here.

_Status: lesson content authored for all 9 topics, all runnable code blocks verified to run correctly (interactive `breakpoint()`/`pdb` transcripts shown as illustrative terminal sessions), closing Semester 1's full lesson content._

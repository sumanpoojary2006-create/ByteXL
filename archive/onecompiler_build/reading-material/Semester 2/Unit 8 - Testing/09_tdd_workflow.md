## Introduction

Sam's team lead makes a suggestion that sounds backwards: "Write the test before the function." Sam's instinct is that you cannot test code that does not exist yet. His lead explains that this is exactly the point: writing the test first forces you to design the function's interface before implementing it, and the failing test shows exactly what needs to be built.

This practice is called test-driven development (TDD). The workflow is three steps, run in a tight loop: Red (write a failing test), Green (write the minimum code to make it pass), Refactor (clean up the code while keeping the test green).

![A cycle diagram showing three phases: Red (test fails, shown with a red indicator), Green (test passes with minimal code, shown in green), and Refactor (code is cleaned up, test stays green)](images/09_tdd_workflow.png)

## The Red-Green-Refactor Cycle

**Red**: write a test for the function you want to build. Run it. It fails because the function does not exist yet. The failure is not a problem -- it is the goal of this step. A test that fails for the right reason confirms your test is correct.

**Green**: write the simplest code that makes the test pass. Do not optimize. Do not handle edge cases that are not yet tested. Just make it green.

**Refactor**: now that you have a passing test as a safety net, clean up the implementation. Extract duplication, rename variables, simplify logic. The test confirms you have not broken anything.

Repeat.

## A TDD Session: Building a Reservation System

**Step 1 -- Red**: Write a test for a function that does not yet exist.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiIyB0ZXN0cy90ZXN0X3Jlc2VydmF0aW9ucy5weVxuaW1wb3J0IHB5dGVzdFxuZnJvbSBsaWJyYXJ5LnJlc2VydmF0aW9ucyBpbXBvcnQgUmVzZXJ2YXRpb25RdWV1ZVxuXG5kZWYgdGVzdF9lbXB0eV9xdWV1ZV9oYXNfemVyb19sZW5ndGgoKTpcbiAgICBxID0gUmVzZXJ2YXRpb25RdWV1ZSgpXG4gICAgYXNzZXJ0IGxlbihxKSA9PSAwIn0"
 width="100%"
></iframe>

Run `pytest`. It fails with `ModuleNotFoundError: No module named 'library.reservations'`. That is the expected red state.

**Step 2 -- Green**: Write the minimum code to pass the test.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiIyBsaWJyYXJ5L3Jlc2VydmF0aW9ucy5weVxuY2xhc3MgUmVzZXJ2YXRpb25RdWV1ZTpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHNlbGYuX3F1ZXVlID0gW11cblxuICAgIGRlZiBfX2xlbl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gbGVuKHNlbGYuX3F1ZXVlKSJ9"
 width="100%"
></iframe>

Run `pytest`. The test passes. Green.

**Step 3 -- Refactor**: Nothing to clean up yet. Move to the next test.

---

**Step 4 -- Red**: Add a test for enqueuing a reservation.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZGVmIHRlc3RfYWRkX3Jlc2VydmF0aW9uX2luY3JlYXNlc19sZW5ndGgoKTpcbiAgICBxID0gUmVzZXJ2YXRpb25RdWV1ZSgpXG4gICAgcS5hZGQoXCJQMDAxXCIsIFwiOTc4LTAwMVwiKVxuICAgIGFzc2VydCBsZW4ocSkgPT0gMVxuXG5kZWYgdGVzdF9hZGRfdHdvX3Jlc2VydmF0aW9ucygpOlxuICAgIHEgPSBSZXNlcnZhdGlvblF1ZXVlKClcbiAgICBxLmFkZChcIlAwMDFcIiwgXCI5NzgtMDAxXCIpXG4gICAgcS5hZGQoXCJQMDAyXCIsIFwiOTc4LTAwMVwiKVxuICAgIGFzc2VydCBsZW4ocSkgPT0gMiJ9"
 width="100%"
></iframe>

Both tests fail. Green the first one:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIGFkZChzZWxmLCBwYXRyb25faWQsIGlzYm4pOlxuICAgIHNlbGYuX3F1ZXVlLmFwcGVuZCh7XCJwYXRyb25faWRcIjogcGF0cm9uX2lkLCBcImlzYm5cIjogaXNibn0pIn0"
 width="100%"
></iframe>

Run `pytest`. Both tests now pass.

---

**Step 5 -- Red**: Test next-in-queue retrieval.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZGVmIHRlc3RfbmV4dF9wYXRyb25faXNfZmlyc3RfYWRkZWQoKTpcbiAgICBxID0gUmVzZXJ2YXRpb25RdWV1ZSgpXG4gICAgcS5hZGQoXCJQMDAxXCIsIFwiOTc4LTAwMVwiKVxuICAgIHEuYWRkKFwiUDAwMlwiLCBcIjk3OC0wMDFcIilcbiAgICBhc3NlcnQgcS5uZXh0X3BhdHJvbigpID09IFwiUDAwMVwiXG5cbmRlZiB0ZXN0X25leHRfcGF0cm9uX29uX2VtcHR5X3JhaXNlcygpOlxuICAgIHEgPSBSZXNlcnZhdGlvblF1ZXVlKClcbiAgICB3aXRoIHB5dGVzdC5yYWlzZXMoSW5kZXhFcnJvciwgbWF0Y2g9XCJubyByZXNlcnZhdGlvbnNcIik6XG4gICAgICAgIHEubmV4dF9wYXRyb24oKSJ9"
 width="100%"
></iframe>

**Step 6 -- Green**:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X3RkZF93b3JrZmxvdyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZGVmIG5leHRfcGF0cm9uKHNlbGYpOlxuICAgIGlmIG5vdCBzZWxmLl9xdWV1ZTpcbiAgICAgICAgcmFpc2UgSW5kZXhFcnJvcihcIm5vIHJlc2VydmF0aW9uc1wiKVxuICAgIHJldHVybiBzZWxmLl9xdWV1ZVswXVtcInBhdHJvbl9pZFwiXSJ9"
 width="100%"
></iframe>

Tests pass.

**Step 7 -- Refactor**: Change `self._queue` to a `collections.deque` for O(1) access from both ends, then verify all tests still pass.

## Why TDD Helps Design

TDD naturally produces functions with clean interfaces:

- You write the test from the perspective of the caller, which forces you to think about the API before the implementation.
- You cannot write a test for a function that is hard to call, so TDD creates pressure toward smaller, focused functions.
- Every function you write has tests from the start, so coverage stays high automatically.

## When TDD Is and Is Not Appropriate

TDD works well for: business logic with clear inputs and outputs (fine calculations, queuing, validation), algorithmic functions, anything where the specification is clear.

TDD is harder for: UI code, exploratory prototypes where the requirements are unclear, integration code that wires together external systems.

## TDD Workflow at a Glance

| Phase | Goal |
|---|---|
| Red | Write a failing test that describes what you want |
| Green | Write the minimum code to make it pass |
| Refactor | Clean up with the test as a safety net |
| Repeat | Next test, next cycle |

## Your Turn

Build a `WaitList` class using TDD. Start with these tests in order (add one at a time, make it pass before adding the next):

1. `test_empty_waitlist_length` -- `len(WaitList())` is 0
2. `test_add_patron_to_waitlist` -- after `wl.add("P001")`, length is 1
3. `test_serve_removes_first_added` -- `wl.serve()` returns the patron added first (FIFO)
4. `test_serve_decreases_length` -- length drops by 1 after `wl.serve()`
5. `test_serve_empty_raises` -- `wl.serve()` raises `IndexError` on empty list

Work one test at a time. Do not write code that is not yet required by a test.

## Conclusion

TDD writes tests before code, using the Red-Green-Refactor cycle to drive implementation from the outside in. It produces functions with clean, testable interfaces and keeps coverage high by construction. It is not always the right approach for exploratory work, but for any well-defined piece of business logic, it is the most reliable path to code that works correctly from the start. Unit 9 moves from testing to code quality: type hints, linters, formatters, and pre-commit hooks that catch problems before the tests even run.

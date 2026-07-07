## Introduction

Sam's `notify_patron` function sends an email through an external SMTP server. When he tries to test it, the test actually sends an email to the patron's real address. Running the test suite fifty times a day means fifty spam emails to real people, plus a failing test every time the SMTP server is down for maintenance.

The solution is mocking: replacing the real external dependency with a controlled fake during testing. The fake behaves exactly as the real thing when told to, and records what calls were made to it, allowing the test to verify behavior without touching the external system.

![A test shown with two paths from notify_patron: one path going to the real SMTP server (crossed out), and one path going to a mock that records calls and returns a fake response](images/07_mocking_patching.png)

## unittest.mock.MagicMock

Python's standard library includes `unittest.mock`. `MagicMock` is the core object: it accepts any attribute access or method call without raising an error, and records what was done to it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-001-5df7991aa0.html"
 width="100%"
></iframe>

## patch: Replace at the Call Site

`unittest.mock.patch` temporarily replaces a name with a `MagicMock` for the duration of a test. The replacement is scoped: it reverts to the real object after the test exits.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-002-b742854357.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-003-6b955d7205.html"
 width="100%"
></iframe>

The critical rule: patch where the name is *used*, not where it is defined. The function uses `smtplib.SMTP` as `library.notifications.smtplib.SMTP`, so that is what you patch.

## patch as a Decorator

`@patch` as a decorator is cleaner than the `with` form for test methods:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-004-693c383367.html"
 width="100%"
></iframe>

The patched object is passed as the last argument to the test function.

## pytest-mock: A Cleaner pytest Integration

The `pytest-mock` plugin provides a `mocker` fixture that wraps `unittest.mock` with a cleaner API:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-005-b6cfbdc10c.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-006-9e141b1c7d.html"
 width="100%"
></iframe>

`mocker.patch` automatically reverts after the test; no `with` block or decorator needed.

## Mock Assertions

Mocks provide built-in assertion methods:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-007-f894f0ac2e.html"
 width="100%"
></iframe>

## What to Mock and What Not to

Mock external dependencies: network calls, database I/O, file system writes in slow tests, time (for deterministic date-sensitive tests). Do not mock the code you are actually testing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-008-b39506704a.html"
 width="100%"
></iframe>

## Mocking and Patching at a Glance

| Tool | What it does |
|---|---|
| `MagicMock()` | Fake object that accepts any call and records it |
| `mock.return_value = x` | Control what the mock returns |
| `patch("module.Name")` | Replace a name temporarily during the test |
| `mock.assert_called_once_with(args)` | Verify the mock was called with specific args |
| `mocker.patch(...)` | pytest-mock fixture version of patch |

## Your Turn

Write a test for a function `send_overdue_notices(overdue_records, notifier)` where `notifier` is a callable that sends the notification. Use a `MagicMock` as the notifier and verify it was called once per overdue record, with the correct patron ID:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-07-mocking-and-patching-009-a92c8d485b.html"
 width="100%"
></iframe>

## Conclusion

Mocking replaces real external dependencies with controlled fakes, making tests fast, deterministic, and free of side effects. `MagicMock` is the fake object; `patch` targets the name where it is used in the module under test. Mock assertions verify that the code interacted with its dependencies in the expected way. The next lesson covers coverage: measuring how much of the code is actually being exercised by the test suite.

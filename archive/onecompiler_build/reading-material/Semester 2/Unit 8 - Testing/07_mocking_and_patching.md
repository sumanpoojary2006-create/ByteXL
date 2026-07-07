## Introduction

Sam's `notify_patron` function sends an email through an external SMTP server. When he tries to test it, the test actually sends an email to the patron's real address. Running the test suite fifty times a day means fifty spam emails to real people, plus a failing test every time the SMTP server is down for maintenance.

The solution is mocking: replacing the real external dependency with a controlled fake during testing. The fake behaves exactly as the real thing when told to, and records what calls were made to it, allowing the test to verify behavior without touching the external system.

![A test shown with two paths from notify_patron: one path going to the real SMTP server (crossed out), and one path going to a mock that records calls and returns a fake response](images/07_mocking_patching.png)

## unittest.mock.MagicMock

Python's standard library includes `unittest.mock`. `MagicMock` is the core object: it accepts any attribute access or method call without raising an error, and records what was done to it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIHVuaXR0ZXN0Lm1vY2sgaW1wb3J0IE1hZ2ljTW9ja1xuXG4jIE1hZ2ljTW9jayBhY2NlcHRzIGFueSBjYWxsXG5zbXRwID0gTWFnaWNNb2NrKClcbnNtdHAuc2VuZG1haWwoXCJmcm9tQGxpYi5vcmdcIiwgXCJwYXRyb25AbWFpbC5jb21cIiwgXCJZb3VyIGJvb2sgaXMgZHVlXCIpXG5cbiMgSW5zcGVjdCB3aGF0IHdhcyBjYWxsZWRcbnByaW50KHNtdHAuc2VuZG1haWwuY2FsbGVkKSAgICAgICAgICAjIFRydWVcbnByaW50KHNtdHAuc2VuZG1haWwuY2FsbF9jb3VudCkgICAgICAjIDFcbnByaW50KHNtdHAuc2VuZG1haWwuY2FsbF9hcmdzKSAgICAgICAjIGNhbGwoJ2Zyb21AbGliLm9yZycsICdwYXRyb25AbWFpbC5jb20nLCAnLi4uJylcblxuIyBDb250cm9sIHRoZSByZXR1cm4gdmFsdWVcbnNtdHAubG9naW4ucmV0dXJuX3ZhbHVlID0gVHJ1ZVxucmVzdWx0ID0gc210cC5sb2dpbihcInVzZXJcIiwgXCJwYXNzXCIpXG5wcmludChyZXN1bHQpICAgIyBUcnVlIn0"
 width="100%"
></iframe>

## patch: Replace at the Call Site

`unittest.mock.patch` temporarily replaces a name with a `MagicMock` for the duration of a test. The replacement is scoped: it reverts to the real object after the test exits.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiIjIGxpYnJhcnkvbm90aWZpY2F0aW9ucy5weVxuaW1wb3J0IHNtdHBsaWJcblxuZGVmIG5vdGlmeV9wYXRyb24ocGF0cm9uX2VtYWlsLCBtZXNzYWdlKTpcbiAgICB3aXRoIHNtdHBsaWIuU01UUChcInNtdHAubGlicmFyeS5vcmdcIiwgNTg3KSBhcyBzbXRwOlxuICAgICAgICBzbXRwLmxvZ2luKFwibGlicmFyeVwiLCBcInNlY3JldFwiKVxuICAgICAgICBzbXRwLnNlbmRtYWlsKFwibGlicmFyeUBsaWJyYXJ5Lm9yZ1wiLCBwYXRyb25fZW1haWwsIG1lc3NhZ2UpXG4gICAgICAgIHJldHVybiBUcnVlIn0"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIHRlc3RzL3Rlc3Rfbm90aWZpY2F0aW9ucy5weVxuZnJvbSB1bml0dGVzdC5tb2NrIGltcG9ydCBwYXRjaCwgTWFnaWNNb2NrXG5cbmRlZiB0ZXN0X25vdGlmeV9wYXRyb25fc2VuZHNfZW1haWwoKTpcbiAgICB3aXRoIHBhdGNoKFwibGlicmFyeS5ub3RpZmljYXRpb25zLnNtdHBsaWIuU01UUFwiKSBhcyBtb2NrX3NtdHBfY2xhc3M6XG4gICAgICAgICMgbW9ja19zbXRwX2NsYXNzIGlzIHRoZSBwYXRjaGVkIFNNVFAgY2xhc3NcbiAgICAgICAgIyBtb2NrX3NtdHBfY2xhc3MoKSBpcyB0aGUgaW5zdGFuY2UgcmV0dXJuZWQgYnkgJ3dpdGggc210cGxpYi5TTVRQKC4uLiknXG4gICAgICAgIG1vY2tfaW5zdGFuY2UgPSBNYWdpY01vY2soKVxuICAgICAgICBtb2NrX3NtdHBfY2xhc3MucmV0dXJuX3ZhbHVlLl9fZW50ZXJfXyA9IE1hZ2ljTW9jayhyZXR1cm5fdmFsdWU9bW9ja19pbnN0YW5jZSlcbiAgICAgICAgbW9ja19zbXRwX2NsYXNzLnJldHVybl92YWx1ZS5fX2V4aXRfXyA9IE1hZ2ljTW9jayhyZXR1cm5fdmFsdWU9RmFsc2UpXG5cbiAgICAgICAgcmVzdWx0ID0gbm90aWZ5X3BhdHJvbihcInBhdHJvbkBtYWlsLmNvbVwiLCBcIllvdXIgYm9vayBpcyBkdWVcIilcblxuICAgICAgICBhc3NlcnQgcmVzdWx0IGlzIFRydWVcbiAgICAgICAgbW9ja19pbnN0YW5jZS5sb2dpbi5hc3NlcnRfY2FsbGVkX29uY2Vfd2l0aChcImxpYnJhcnlcIiwgXCJzZWNyZXRcIilcbiAgICAgICAgbW9ja19pbnN0YW5jZS5zZW5kbWFpbC5hc3NlcnRfY2FsbGVkX29uY2UoKSJ9"
 width="100%"
></iframe>

The critical rule: patch where the name is *used*, not where it is defined. The function uses `smtplib.SMTP` as `library.notifications.smtplib.SMTP`, so that is what you patch.

## patch as a Decorator

`@patch` as a decorator is cleaner than the `with` form for test methods:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIHVuaXR0ZXN0Lm1vY2sgaW1wb3J0IHBhdGNoXG5cbkBwYXRjaChcImxpYnJhcnkubm90aWZpY2F0aW9ucy5zbXRwbGliLlNNVFBcIilcbmRlZiB0ZXN0X25vdGlmeV9zZW5kc190b19jb3JyZWN0X2FkZHJlc3MobW9ja19zbXRwX2NsYXNzKTpcbiAgICBtb2NrX2luc3RhbmNlID0gbW9ja19zbXRwX2NsYXNzLnJldHVybl92YWx1ZS5fX2VudGVyX18ucmV0dXJuX3ZhbHVlXG5cbiAgICBub3RpZnlfcGF0cm9uKFwiYWxpY2VAbWFpbC5jb21cIiwgXCJPdmVyZHVlIG5vdGljZVwiKVxuXG4gICAgYXJncywgXyA9IG1vY2tfaW5zdGFuY2Uuc2VuZG1haWwuY2FsbF9hcmdzXG4gICAgYXNzZXJ0IGFyZ3NbMV0gPT0gXCJhbGljZUBtYWlsLmNvbVwiICAgIyBzZWNvbmQgYXJnIGlzIHRoZSByZWNpcGllbnQifQ"
 width="100%"
></iframe>

The patched object is passed as the last argument to the test function.

## pytest-mock: A Cleaner pytest Integration

The `pytest-mock` plugin provides a `mocker` fixture that wraps `unittest.mock` with a cleaner API:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgNSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDUuc2giLCJjb2RlIjoicGlwIGluc3RhbGwgcHl0ZXN0LW1vY2sifQ"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJkZWYgdGVzdF9ub3RpZnlfd2l0aF9tb2NrZXIobW9ja2VyKTpcbiAgICBtb2NrX3NtdHAgPSBtb2NrZXIucGF0Y2goXCJsaWJyYXJ5Lm5vdGlmaWNhdGlvbnMuc210cGxpYi5TTVRQXCIpXG4gICAgaW5zdGFuY2UgPSBtb2NrX3NtdHAucmV0dXJuX3ZhbHVlLl9fZW50ZXJfXy5yZXR1cm5fdmFsdWVcblxuICAgIG5vdGlmeV9wYXRyb24oXCJhbGljZUBtYWlsLmNvbVwiLCBcIk92ZXJkdWUgbm90aWNlXCIpXG5cbiAgICBpbnN0YW5jZS5zZW5kbWFpbC5hc3NlcnRfY2FsbGVkX29uY2UoKSJ9"
 width="100%"
></iframe>

`mocker.patch` automatically reverts after the test; no `with` block or decorator needed.

## Mock Assertions

Mocks provide built-in assertion methods:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJtb2NrLmFzc2VydF9jYWxsZWQoKSAgICAgICAgICAgICAgICAgICAgIyB3YXMgY2FsbGVkIGF0IGxlYXN0IG9uY2Vcbm1vY2suYXNzZXJ0X2NhbGxlZF9vbmNlKCkgICAgICAgICAgICAgICMgd2FzIGNhbGxlZCBleGFjdGx5IG9uY2Vcbm1vY2suYXNzZXJ0X2NhbGxlZF93aXRoKGFyZzEsIGFyZzIpICAgICMgbGFzdCBjYWxsIHVzZWQgdGhlc2UgYXJnc1xubW9jay5hc3NlcnRfY2FsbGVkX29uY2Vfd2l0aChhcmcxKSAgICAgIyBjYWxsZWQgZXhhY3RseSBvbmNlIHdpdGggdGhlc2UgYXJnc1xubW9jay5hc3NlcnRfbm90X2NhbGxlZCgpICAgICAgICAgICAgICAgIyBuZXZlciBjYWxsZWQifQ"
 width="100%"
></iframe>

## What to Mock and What Not to

Mock external dependencies: network calls, database I/O, file system writes in slow tests, time (for deterministic date-sensitive tests). Do not mock the code you are actually testing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgOCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwOC5weSIsImNvZGUiOiIjIEdPT0Q6IG1vY2sgdGhlIGV4dGVybmFsIGVtYWlsIHNlbmRlclxuQHBhdGNoKFwibGlicmFyeS5ub3RpZmljYXRpb25zLnNtdHBsaWIuU01UUFwiKVxuZGVmIHRlc3Rfbm90aWZ5KG1vY2tfc210cCk6IC4uLlxuXG4jIEJBRDogbW9ja2luZyB0aGUgdGhpbmcgeW91J3JlIHRlc3RpbmcgZGVmZWF0cyB0aGUgcHVycG9zZVxud2l0aCBwYXRjaChcImxpYnJhcnkuY2F0YWxvZy5DYXRhbG9nLmFkZFwiKSBhcyBtb2NrX2FkZDpcbiAgICBjYXRhbG9nLmFkZChib29rKSAgICMgeW91J3JlIHRlc3Rpbmcgbm90aGluZ1xuICAgIG1vY2tfYWRkLmFzc2VydF9jYWxsZWRfb25jZSgpICAgIyB0aGlzIG9ubHkgdGVzdHMgdGhhdCBtb2NrIHdhcyBjYWxsZWQifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X21vY2tpbmdfYW5kX3BhdGNoaW5nIGNvZGUgOSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwOS5weSIsImNvZGUiOiJmcm9tIHVuaXR0ZXN0Lm1vY2sgaW1wb3J0IE1hZ2ljTW9ja1xuXG5kZWYgc2VuZF9vdmVyZHVlX25vdGljZXMob3ZlcmR1ZV9yZWNvcmRzLCBub3RpZmllcik6XG4gICAgZm9yIHJlY29yZCBpbiBvdmVyZHVlX3JlY29yZHM6XG4gICAgICAgIG5vdGlmaWVyKHJlY29yZFtcInBhdHJvbl9pZFwiXSwgZlwiWW91ciBib29rIGlzIHtyZWNvcmRbJ2RheXNfb3ZlcmR1ZSddfSBkYXlzIG92ZXJkdWUuXCIpXG5cbmRlZiB0ZXN0X3NlbmRzX29uZV9ub3RpY2VfcGVyX3JlY29yZCgpOlxuICAgIG1vY2tfbm90aWZpZXIgPSBNYWdpY01vY2soKVxuICAgIHJlY29yZHMgPSBbXG4gICAgICAgIHtcInBhdHJvbl9pZFwiOiBcIlAwMDFcIiwgXCJkYXlzX292ZXJkdWVcIjogM30sXG4gICAgICAgIHtcInBhdHJvbl9pZFwiOiBcIlAwMDJcIiwgXCJkYXlzX292ZXJkdWVcIjogN30sXG4gICAgXVxuICAgIHNlbmRfb3ZlcmR1ZV9ub3RpY2VzKHJlY29yZHMsIG1vY2tfbm90aWZpZXIpXG5cbiAgICBhc3NlcnQgbW9ja19ub3RpZmllci5jYWxsX2NvdW50ID09IDJcbiAgICBtb2NrX25vdGlmaWVyLmFzc2VydF9hbnlfY2FsbChcIlAwMDFcIiwgXCJZb3VyIGJvb2sgaXMgMyBkYXlzIG92ZXJkdWUuXCIpXG4gICAgbW9ja19ub3RpZmllci5hc3NlcnRfYW55X2NhbGwoXCJQMDAyXCIsIFwiWW91ciBib29rIGlzIDcgZGF5cyBvdmVyZHVlLlwiKSJ9"
 width="100%"
></iframe>

## Conclusion

Mocking replaces real external dependencies with controlled fakes, making tests fast, deterministic, and free of side effects. `MagicMock` is the fake object; `patch` targets the name where it is used in the module under test. Mock assertions verify that the code interacted with its dependencies in the expected way. The next lesson covers coverage: measuring how much of the code is actually being exercised by the test suite.

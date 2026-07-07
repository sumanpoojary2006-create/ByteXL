## Introduction

Raj can now run `ruff`, `black`, and `mypy` individually. The problem is that developers forget to run them before committing. Style issues still reach the shared repository and show up in CI failures, which are slower to catch and more disruptive to fix than catching them locally.

Git hooks solve this: they are scripts that Git runs automatically at specific points in the workflow. A `pre-commit` hook runs before every commit. If the hook fails (exits with a non-zero code), Git cancels the commit. The developer sees the failure immediately, fixes it, and commits again.

![A git commit timeline with a hook shown as a gate between staging and the commit: if the hook passes, the commit happens; if it fails, the commit is aborted and the developer sees an error](images/05_git_hooks_intro.png)

## Where Git Hooks Live

Git hooks are shell scripts stored in `.git/hooks/`. Git creates sample hooks with a `.sample` extension when you run `git init`. To activate a hook, remove the `.sample` extension and make the file executable.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDEiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAxLnNoIiwiY29kZSI6ImxzIC5naXQvaG9va3MvXG4jIGFwcGx5cGF0Y2gtbXNnLnNhbXBsZSAgcHJlLWNvbW1pdC5zYW1wbGUgIHByZS1wdXNoLnNhbXBsZSAgLi4uIn0"
 width="100%"
></iframe>

The most commonly used hooks:
- `pre-commit`: runs before a commit is created
- `commit-msg`: validates the commit message format
- `pre-push`: runs before a push to a remote
- `post-merge`: runs after a merge completes (e.g., to install new dependencies)

## A Simple pre-commit Hook

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDIiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAyLnNoIiwiY29kZSI6IiMgLmdpdC9ob29rcy9wcmUtY29tbWl0XG4jIS9iaW4vc2hcbiMgUnVuIHJ1ZmYgbGludGVyOyBpZiBpdCBmYWlscywgYWJvcnQgdGhlIGNvbW1pdFxuXG5ydWZmIGNoZWNrIC5cbmV4aXQgJD8gICAjIHBhc3MgdGhyb3VnaCBydWZmJ3MgZXhpdCBjb2RlIn0"
 width="100%"
></iframe>

Make it executable:
<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDMiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAzLnNoIiwiY29kZSI6ImNobW9kICt4IC5naXQvaG9va3MvcHJlLWNvbW1pdCJ9"
 width="100%"
></iframe>

Now every `git commit` runs `ruff check .` first. If `ruff` finds any violations, it exits with code 1, Git sees the failure, and the commit is aborted.

## A Hook That Checks and Auto-Fixes

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDQiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA0LnNoIiwiY29kZSI6IiMhL2Jpbi9zaFxuIyBBdXRvLWZpeCB3aXRoIHJ1ZmYsIGF1dG8tZm9ybWF0IHdpdGggYmxhY2ssIHRoZW4gcmUtc3RhZ2UgdGhlIGNoYW5nZXNcblxucnVmZiBjaGVjayAtLWZpeCAuICYmIGJsYWNrIC5cblxuIyBSZS1zdGFnZSB0aGUgbW9kaWZpZWQgZmlsZXMgc28gdGhlIGNoYW5nZXMgYXJlIGluY2x1ZGVkIGluIHRoZSBjb21taXRcbmdpdCBhZGQgLXVcblxuIyBFeGl0IDAgdG8gYWxsb3cgdGhlIGNvbW1pdCB0byBwcm9jZWVkXG5leGl0IDAifQ"
 width="100%"
></iframe>

This hook runs `ruff --fix` and `black`, re-stages the files, and lets the commit proceed. The developer does not need to manually fix and re-commit.

## Limitations of Manual Hooks

Manual hooks have two problems:

1. They live in `.git/hooks/`, which is not version-controlled. Every developer who clones the repository must set up hooks themselves. If the team grows to ten people, all ten must remember to install and update the hooks.

2. Different developers can configure different hooks, leading to inconsistency.

The `pre-commit` framework (next lesson) solves both problems by version-controlling the hook configuration and managing hook installation automatically.

## Hook Types Reference

| Hook | When it runs |
|---|---|
| `pre-commit` | Before a commit is created (after staging) |
| `commit-msg` | After the commit message is written, before commit |
| `pre-push` | Before pushing to a remote |
| `post-commit` | After a commit is created (cannot abort) |
| `post-merge` | After a merge finishes |
| `pre-rebase` | Before a rebase starts |

## Bypassing Hooks (and When Not To)

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDUiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA1LnNoIiwiY29kZSI6ImdpdCBjb21taXQgLS1uby12ZXJpZnkgICAjIHNraXAgYWxsIGhvb2tzIGZvciB0aGlzIGNvbW1pdCJ9"
 width="100%"
></iframe>

`--no-verify` is available but should be used only for genuine emergencies (hot-fix in an incident, debugging the hook itself). Normalizing its use defeats the purpose of having hooks.

## Git Hooks at a Glance

| Concept | What it means |
|---|---|
| Hook location | `.git/hooks/` (not version-controlled) |
| Activation | Remove `.sample` extension, make executable |
| `pre-commit` | Most important: runs before every commit |
| Exit code 0 | Hook passes, commit proceeds |
| Exit code non-zero | Hook fails, commit aborted |
| `--no-verify` | Skip hooks (use sparingly) |

## Your Turn

Create a `pre-commit` hook in your library project that:
1. Runs `ruff check .` and exits 1 if there are violations
2. Runs `black --check .` and exits 1 if formatting is needed

Test it by introducing a deliberate style violation (an unused import, a line over 88 characters) and confirming that `git commit` is blocked. Then fix the violation and confirm the commit succeeds.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dpdF9ob29rc19pbnRybyBjb2RlIDYiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA2LnNoIiwiY29kZSI6IiMhL2Jpbi9zaFxucnVmZiBjaGVjayAuIHx8IGV4aXQgMVxuYmxhY2sgLS1jaGVjayAuIHx8IGV4aXQgMVxuZXhpdCAwIn0"
 width="100%"
></iframe>

## Conclusion

Git hooks are shell scripts that run at specific points in the Git workflow. `pre-commit` hooks enforce quality gates before code enters the repository. They are powerful but require every developer to install them manually, since `.git/hooks/` is not version-controlled. The next lesson introduces the `pre-commit` framework, which solves this by defining hooks in a committed configuration file that manages itself.

## Introduction

Priya's CLI works correctly, but librarians complain that they cannot remember the options, the error messages do not explain what is wrong, and the import command gives no feedback during a 20-minute run. A CLI that works is not the same as a CLI that is enjoyable to use. This lesson covers the UX principles that separate professional tools from fragile scripts.

![A terminal window showing four UX improvements: a progress bar during a long operation, colored output distinguishing success (green) and error (red), a --dry-run option, and a friendly --help message with examples](images/07_ux_best_practices.png)

## Principle 1: Give Feedback for Long Operations

A command that runs for 20 seconds with no output looks frozen. Provide progress:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-001-739388b9fb.html"
 width="100%"
></iframe>

## Principle 2: Use Color Meaningfully

- Green for success
- Yellow for warnings or dry-run messages
- Red for errors

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-002-1c41c0c030.html"
 width="100%"
></iframe>

Check `typer.get_terminal_size()` or use `NO_COLOR` environment variable respecting (typer does this automatically) for scripts that pipe output.

## Principle 3: Provide a --dry-run Mode

Any command that modifies data should have a `--dry-run` flag that shows what would happen without actually doing it:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-003-51fbf77136.html"
 width="100%"
></iframe>

## Principle 4: Clear, Actionable Error Messages

The best error message says what was wrong, why it is wrong, and what the user can do:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-004-9b0d9761e3.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-005-9af647ae66.html"
 width="100%"
></iframe>

## Principle 5: Add --verbose and --quiet Flags

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-006-750af9e70c.html"
 width="100%"
></iframe>

## Principle 6: Confirm Dangerous Operations

For operations that cannot be undone, ask for confirmation before proceeding:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-07-ux-best-practices-007-03857a31fd.html"
 width="100%"
></iframe>

## CLI UX at a Glance

| Practice | Why it matters |
|---|---|
| Progress bar for long ops | Tells users the program is working |
| Meaningful color | Visual hierarchy; errors stand out |
| `--dry-run` mode | Safe to explore before committing |
| Actionable error messages | User knows what to fix |
| `--verbose` / `--quiet` | Adaptable to scripting and interactive use |
| Confirm before destructive ops | Prevents accidental data loss |

## Your Turn

Add two improvements to any command you have built:
1. A progress bar using `typer.progressbar` for an operation with many items
2. A confirmation prompt for any destructive operation using `typer.confirm`

Test that `--force` bypasses the confirmation for scripted use.

## Conclusion

A CLI that works is not enough. The best CLIs give feedback during long operations, use color meaningfully, offer dry-run modes, write clear error messages, and confirm before deleting data. These practices make the difference between a tool that users trust and one they avoid. Unit 13 moves to the persistence layer that most CLI tools depend on: database interaction with Python.

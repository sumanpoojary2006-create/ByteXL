## Introduction

Priya's CLI works correctly, but librarians complain that they cannot remember the options, the error messages do not explain what is wrong, and the import command gives no feedback during a 20-minute run. A CLI that works is not the same as a CLI that is enjoyable to use. This lesson covers the UX principles that separate professional tools from fragile scripts.

![A terminal window showing four UX improvements: a progress bar during a long operation, colored output distinguishing success (green) and error (red), a --dry-run option, and a friendly --help message with examples](images/07_ux_best_practices.png)

## Principle 1: Give Feedback for Long Operations

A command that runs for 20 seconds with no output looks frozen. Provide progress:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgdHlwZXJcbmltcG9ydCB0aW1lXG5cbmFwcCA9IHR5cGVyLlR5cGVyKClcblxuQGFwcC5jb21tYW5kKClcbmRlZiBpbXBvcnRfYm9va3MoZmlsZTogc3RyLCBicmFuY2g6IHN0ciA9IFwibWFpblwiKTpcbiAgICBcIlwiXCJJbXBvcnQgYm9va3MgZnJvbSBhIENTViBmaWxlLlwiXCJcIlxuICAgIHJlY29yZHMgPSBsb2FkX2NzdihmaWxlKSAgICMgcXVpY2s6IGp1c3QgcmVhZGluZyB0aGUgZmlsZVxuICAgIHR5cGVyLmVjaG8oZlwiRm91bmQge2xlbihyZWNvcmRzKX0gcmVjb3Jkcy4gSW1wb3J0aW5nIGludG8gJ3ticmFuY2h9Jy4uLlwiKVxuXG4gICAgd2l0aCB0eXBlci5wcm9ncmVzc2JhcihyZWNvcmRzLCBsYWJlbD1cIkltcG9ydGluZ1wiKSBhcyBwcm9ncmVzczpcbiAgICAgICAgZm9yIHJlY29yZCBpbiBwcm9ncmVzczpcbiAgICAgICAgICAgIGltcG9ydF9yZWNvcmQocmVjb3JkLCBicmFuY2gpXG4gICAgICAgICAgICB0aW1lLnNsZWVwKDAuMDEpICAgIyBzaW11bGF0ZSB3b3JrXG5cbiAgICB0eXBlci5lY2hvKHR5cGVyLnN0eWxlKGZcIkRvbmUuIHtsZW4ocmVjb3Jkcyl9IHJlY29yZHMgaW1wb3J0ZWQuXCIsIGZnPXR5cGVyLmNvbG9ycy5HUkVFTikpIn0"
 width="100%"
></iframe>

## Principle 2: Use Color Meaningfully

- Green for success
- Yellow for warnings or dry-run messages
- Red for errors

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiIjIFN1Y2Nlc3M6XG50eXBlci5lY2hvKHR5cGVyLnN0eWxlKFwiSW1wb3J0IGNvbXBsZXRlOiAyLDAwMCByZWNvcmRzXCIsIGZnPXR5cGVyLmNvbG9ycy5HUkVFTikpXG5cbiMgV2FybmluZzpcbnR5cGVyLmVjaG8odHlwZXIuc3R5bGUoXCJXYXJuaW5nOiA1IHJlY29yZHMgc2tpcHBlZCAoZHVwbGljYXRlIElTQk4pXCIsIGZnPXR5cGVyLmNvbG9ycy5ZRUxMT1cpKVxuXG4jIEVycm9yOlxudHlwZXIuZWNobyh0eXBlci5zdHlsZShmXCJFcnJvcjoge21lc3NhZ2V9XCIsIGZnPXR5cGVyLmNvbG9ycy5SRUQpLCBlcnI9VHJ1ZSkifQ"
 width="100%"
></iframe>

Check `typer.get_terminal_size()` or use `NO_COLOR` environment variable respecting (typer does this automatically) for scripts that pipe output.

## Principle 3: Provide a --dry-run Mode

Any command that modifies data should have a `--dry-run` flag that shows what would happen without actually doing it:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJAYXBwLmNvbW1hbmQoKVxuZGVmIGltcG9ydF9ib29rcyhcbiAgICBmaWxlOiBzdHIsXG4gICAgYnJhbmNoOiBzdHIgPSBcIm1haW5cIixcbiAgICBkcnlfcnVuOiBib29sID0gdHlwZXIuT3B0aW9uKEZhbHNlLCBcIi0tZHJ5LXJ1blwiLCBoZWxwPVwiU2hvdyB3aGF0IHdvdWxkIGJlIGltcG9ydGVkXCIpLFxuKTpcbiAgICByZWNvcmRzID0gbG9hZF9jc3YoZmlsZSlcbiAgICBpZiBkcnlfcnVuOlxuICAgICAgICB0eXBlci5lY2hvKHR5cGVyLnN0eWxlKFwiW0RSWSBSVU5dIFdvdWxkIGltcG9ydDpcIiwgZmc9dHlwZXIuY29sb3JzLllFTExPVykpXG4gICAgICAgIGZvciByIGluIHJlY29yZHNbOjVdOlxuICAgICAgICAgICAgdHlwZXIuZWNobyhmXCIgIHtyWydpc2JuJ119OiB7clsndGl0bGUnXX1cIilcbiAgICAgICAgaWYgbGVuKHJlY29yZHMpID4gNTpcbiAgICAgICAgICAgIHR5cGVyLmVjaG8oZlwiICAuLi4gYW5kIHtsZW4ocmVjb3JkcykgLSA1fSBtb3JlXCIpXG4gICAgICAgIHJldHVyblxuXG4gICAgIyBBY3R1YWwgaW1wb3J0XG4gICAgZm9yIHJlY29yZCBpbiByZWNvcmRzOlxuICAgICAgICBpbXBvcnRfcmVjb3JkKHJlY29yZCwgYnJhbmNoKVxuICAgIHR5cGVyLmVjaG8oZlwiSW1wb3J0ZWQge2xlbihyZWNvcmRzKX0gcmVjb3JkcyBpbnRvICd7YnJhbmNofSdcIikifQ"
 width="100%"
></iframe>

## Principle 4: Clear, Actionable Error Messages

The best error message says what was wrong, why it is wrong, and what the user can do:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIEJhZDpcbiMgRXJyb3I6IGludmFsaWQgYXJndW1lbnRcblxuIyBHb29kOlxuIyBFcnJvcjogLS1icmFuY2ggJ25vcnRod2VzdCcgaXMgbm90IGEgdmFsaWQgYnJhbmNoLlxuIyBWYWxpZCBicmFuY2hlczogbWFpbiwgZWFzdCwgd2VzdCwgbm9ydGgsIHNvdXRoXG4jIFJ1biAnbGlicmFyeS1jbGkgYnJhbmNoZXMnIHRvIGxpc3QgYWxsIGF2YWlsYWJsZSBicmFuY2hlcy4ifQ"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJWQUxJRF9CUkFOQ0hFUyA9IFtcIm1haW5cIiwgXCJlYXN0XCIsIFwid2VzdFwiLCBcIm5vcnRoXCIsIFwic291dGhcIl1cblxuZGVmIHZhbGlkYXRlX2JyYW5jaChicmFuY2g6IHN0cikgLT4gc3RyOlxuICAgIGlmIGJyYW5jaCBub3QgaW4gVkFMSURfQlJBTkNIRVM6XG4gICAgICAgIHR5cGVyLmVjaG8oXG4gICAgICAgICAgICBmXCJFcnJvcjogJ3ticmFuY2h9JyBpcyBub3QgYSB2YWxpZCBicmFuY2guXFxuXCJcbiAgICAgICAgICAgIGZcIlZhbGlkIGJyYW5jaGVzOiB7JywgJy5qb2luKFZBTElEX0JSQU5DSEVTKX1cIixcbiAgICAgICAgICAgIGVycj1UcnVlXG4gICAgICAgIClcbiAgICAgICAgcmFpc2UgdHlwZXIuRXhpdChjb2RlPTEpXG4gICAgcmV0dXJuIGJyYW5jaCJ9"
 width="100%"
></iframe>

## Principle 5: Add --verbose and --quiet Flags

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJmcm9tIGVudW0gaW1wb3J0IEVudW1cblxuY2xhc3MgTG9nTGV2ZWwoc3RyLCBFbnVtKTpcbiAgICBxdWlldCA9IFwicXVpZXRcIlxuICAgIG5vcm1hbCA9IFwibm9ybWFsXCJcbiAgICB2ZXJib3NlID0gXCJ2ZXJib3NlXCJcblxuQGFwcC5jb21tYW5kKClcbmRlZiBpbXBvcnRfYm9va3MoXG4gICAgZmlsZTogc3RyLFxuICAgIGxvZ19sZXZlbDogTG9nTGV2ZWwgPSB0eXBlci5PcHRpb24oTG9nTGV2ZWwubm9ybWFsLCBcIi0tbG9nLWxldmVsXCIpLFxuKTpcbiAgICBpZiBsb2dfbGV2ZWwgPT0gTG9nTGV2ZWwudmVyYm9zZTpcbiAgICAgICAgdHlwZXIuZWNobyhmXCJMb2FkaW5nIGZpbGU6IHtmaWxlfVwiKVxuICAgIHJlY29yZHMgPSBsb2FkX2NzdihmaWxlKVxuICAgIGlmIGxvZ19sZXZlbCAhPSBMb2dMZXZlbC5xdWlldDpcbiAgICAgICAgdHlwZXIuZWNobyhmXCJJbXBvcnRpbmcge2xlbihyZWNvcmRzKX0gcmVjb3Jkcy4uLlwiKVxuICAgIGZvciByZWNvcmQgaW4gcmVjb3JkczpcbiAgICAgICAgaW1wb3J0X3JlY29yZChyZWNvcmQpXG4gICAgICAgIGlmIGxvZ19sZXZlbCA9PSBMb2dMZXZlbC52ZXJib3NlOlxuICAgICAgICAgICAgdHlwZXIuZWNobyhmXCIgIEltcG9ydGVkOiB7cmVjb3JkWydpc2JuJ119XCIpIn0"
 width="100%"
></iframe>

## Principle 6: Confirm Dangerous Operations

For operations that cannot be undone, ask for confirmation before proceeding:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3V4X2Jlc3RfcHJhY3RpY2VzIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJAYXBwLmNvbW1hbmQoKVxuZGVmIGRlbGV0ZV9icmFuY2goYnJhbmNoOiBzdHIsIGZvcmNlOiBib29sID0gdHlwZXIuT3B0aW9uKEZhbHNlLCBcIi0tZm9yY2VcIikpOlxuICAgIFwiXCJcIkRlbGV0ZSBhbGwgcmVjb3JkcyBmb3IgYSBicmFuY2guIElSUkVWRVJTSUJMRS5cIlwiXCJcbiAgICBpZiBub3QgZm9yY2U6XG4gICAgICAgIGNvbmZpcm1lZCA9IHR5cGVyLmNvbmZpcm0oXG4gICAgICAgICAgICBmXCJEZWxldGUgQUxMIHJlY29yZHMgZm9yIGJyYW5jaCAne2JyYW5jaH0nPyBUaGlzIGNhbm5vdCBiZSB1bmRvbmUuXCJcbiAgICAgICAgKVxuICAgICAgICBpZiBub3QgY29uZmlybWVkOlxuICAgICAgICAgICAgdHlwZXIuZWNobyhcIkFib3J0ZWQuXCIpXG4gICAgICAgICAgICByYWlzZSB0eXBlci5FeGl0KClcblxuICAgICMgUHJvY2VlZCB3aXRoIGRlbGV0aW9uXG4gICAgdHlwZXIuZWNobyhmXCJEZWxldGVkIGJyYW5jaDoge2JyYW5jaH1cIikifQ"
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

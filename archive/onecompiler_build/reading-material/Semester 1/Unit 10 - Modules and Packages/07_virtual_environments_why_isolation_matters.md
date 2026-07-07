## Introduction

Naveen's hostel project needs version 2 of a package he installed with `pip install`. A different project he is helping a friend with, on the very same laptop, depends on version 1 of that exact same package, and upgrading it for one project quietly breaks the other. Both projects share the one Python installation on his machine, and `pip install` by default installs into that one shared place, which means every project on his laptop is fighting over the same set of package versions whether they want to or not.

The fix is to give each project its own private, isolated set of installed packages, so installing or upgrading something for one project can never affect any other. That isolated space is called a **virtual environment**, and Python's built-in tool for creating one is `venv`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/07_isolated_virtual_environments.png)

## The Problem, Concretely

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDEiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAxLnNoIiwiY29kZSI6InBpcCBpbnN0YWxsIHNvbWVfbGlicmFyeT09Mi4wICAgICMgZm9yIHRoZSBob3N0ZWwgcHJvamVjdFxuIyAuLi4gbGF0ZXIsIGZvciB0aGUgZnJpZW5kJ3MgcHJvamVjdCAuLi5cbnBpcCBpbnN0YWxsIHNvbWVfbGlicmFyeT09MS4wICAgICMgZG93bmdyYWRlcyBpdCBldmVyeXdoZXJlLCBicmVha2luZyB0aGUgaG9zdGVsIHByb2plY3QifQ"
 width="100%"
></iframe>

With one shared, global Python installation, there is only ever one installed version of `some_library` at a time, no matter how many separate projects are relying on it. The second install does not add a second version alongside the first; it replaces it.

## Creating a Virtual Environment

`venv`, a module included with Python itself, creates a private folder holding its own separate copy of Python and its own separate space for installed packages.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDIiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAyLnNoIiwiY29kZSI6InB5dGhvbiAtbSB2ZW52IC52ZW52In0"
 width="100%"
></iframe>

This creates a new folder named `.venv` inside your project, containing everything that environment needs to run independently of your system's global Python.

## Activating an Environment

Creating the environment is not enough on its own; you need to **activate** it, which tells your terminal to use that environment's Python and packages instead of the global ones, for the rest of that terminal session.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDMiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAzLnNoIiwiY29kZSI6IiMgT24gbWFjT1Mgb3IgTGludXhcbnNvdXJjZSAudmVudi9iaW4vYWN0aXZhdGVcblxuIyBPbiBXaW5kb3dzXG4udmVudlxcU2NyaXB0c1xcYWN0aXZhdGUifQ"
 width="100%"
></iframe>

Once activated, your terminal prompt usually changes to show the environment's name, a visual reminder that you are now working inside this isolated space. Any `pip install` you run from here installs only into `.venv`, completely separate from your system's global packages, and separate from any other project's own virtual environment.

## Installing Inside an Active Environment

With the environment activated, `pip` behaves exactly as you already know, except everything it installs stays contained.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDQiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA0LnNoIiwiY29kZSI6InBpcCBpbnN0YWxsIHNvbWVfbGlicmFyeSJ9"
 width="100%"
></iframe>

This installs into `.venv`, leaving your global Python, and every other project's own environment, entirely untouched.

## Deactivating

When you are done working on this particular project, `deactivate` returns your terminal to the global Python.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDUiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA1LnNoIiwiY29kZSI6ImRlYWN0aXZhdGUifQ"
 width="100%"
></iframe>

## One Environment Per Project

The strong convention, and the entire point of this lesson, is one virtual environment per project, never shared between unrelated projects. Naveen's hostel project gets its own `.venv`, with its own version of `some_library`, and his friend's project gets a completely separate one, with whatever version it actually needs, and the two simply never interfere with each other again.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/07_venv_project_isolation.png)


## Virtual Environments at a Glance

| Step | Command | Effect |
|---|---|---|
| Create | `python -m venv .venv` | Builds a new, isolated environment folder |
| Activate | `source .venv/bin/activate` (Mac/Linux) | Switches your terminal to use that environment |
| Install inside it | `pip install package_name` | Installs only into the active environment |
| Deactivate | `deactivate` | Returns to the global Python |

## Why .venv Usually Should Not Be Shared or Uploaded

A virtual environment folder can be large, and it is entirely reconstructable from a simple list of what was installed, which is exactly the subject of the final lesson of this unit. Project folders almost always exclude `.venv` from version control, sharing only the instructions to recreate it, rather than the environment folder itself.

## Your Turn: Plan an Isolated Setup

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X3ZpcnR1YWxfZW52aXJvbm1lbnRzX3doeV9pc29sYXRpb25fbWF0dGVycyBjb2RlIDYiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA2LnNoIiwiY29kZSI6IiMgSW4geW91ciBwcm9qZWN0IGZvbGRlcjpcbnB5dGhvbiAtbSB2ZW52IC52ZW52XG5zb3VyY2UgLnZlbnYvYmluL2FjdGl2YXRlICAgICAgIyBvciAudmVudlxcU2NyaXB0c1xcYWN0aXZhdGUgb24gV2luZG93c1xucGlwIGluc3RhbGwgcmVxdWVzdHNcbnB5dGhvbiBteV9zY3JpcHQucHlcbmRlYWN0aXZhdGUifQ"
 width="100%"
></iframe>

If you have a real terminal available, walk through these five lines yourself, noticing how your prompt changes after activation, and confirming `pip list` shows a clean, separate environment compared to your global Python.

## Conclusion

A virtual environment, created with `python -m venv .venv` and switched on with `activate`, gives each project its own private, isolated copy of installed packages, so that upgrading or installing something for one project can never silently break another sharing the same machine. The convention is one environment per project, deactivated and left behind whenever you switch contexts. Python's built-in `venv` solves this reliably; the next lesson introduces a newer, dramatically faster tool that handles the exact same job, called `uv`.

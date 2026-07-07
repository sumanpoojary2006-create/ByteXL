## Introduction

Two projects on Dev's machine need different versions of the same library. The library catalog uses `typer 0.12` but an older project needs `typer 0.9`. Installing both globally breaks one of them. Every Python developer eventually hits this conflict.

Virtual environments solve it by giving each project its own isolated Python installation. The `uv` tool manages them far faster than `pip` and adds lockfile-based reproducibility that makes "works on my machine" a thing of the past.

![Three isolated circles (projects) each containing their own Python version and dependency set, with arrows showing no overlap between them](images/03_virtual_environments_and_uv.png)

## What a Virtual Environment Is

```python
import sys
import os

# A virtual environment is a directory tree:
venv_structure = {
    ".venv/": {
        "bin/":     "python, pip, and installed scripts",
        "lib/":     "installed packages (site-packages/)",
        "include/": "header files for C extensions",
        "pyvenv.cfg": "metadata (base python path, version)",
    }
}

print("Virtual environment structure:")
for key, content in venv_structure.items():
    print(f"  {key}")
    if isinstance(content, dict):
        for subkey, description in content.items():
            print(f"    {subkey:<15} # {description}")

print()
print("When .venv is active:")
print(f"  sys.executable would point to .venv/bin/python")
print(f"  Packages install into .venv/lib/ only")
print(f"  Other projects are unaffected")
```

## Creating a Virtual Environment

```python
# Show what the commands do
commands = [
    ("python -m venv .venv",          "Create a virtual environment in .venv/"),
    ("source .venv/bin/activate",     "Activate it (adds .venv/bin to PATH)"),
    ("pip install -e '.[dev]'",       "Install the project + dev dependencies"),
    ("deactivate",                    "Deactivate (restore original PATH)"),
]

print("Virtual environment workflow:")
for cmd, description in commands:
    print(f"  $ {cmd}")
    print(f"    # {description}")
    print()

# What 'activate' actually does to PATH
print("Before activate: PATH searches /usr/bin first")
print("After activate:  PATH searches .venv/bin first")
print("So 'python' -> .venv/bin/python, not /usr/bin/python3")
```

## Why uv Instead of pip + venv

```python
# Speed and reproducibility comparison
comparison = [
    ("Tool",           "pip + venv",     "uv"),
    ("Create venv",    "~0.5s",          "~0.05s (10x faster)"),
    ("Install deps",   "seconds-minutes","sub-second for most projects"),
    ("Lockfile",       "pip freeze only","uv.lock (cross-platform)"),
    ("Python version", "system Python",  "uv python install 3.12"),
    ("Config file",    "requirements.txt","pyproject.toml (same file)"),
]

header, *rows = comparison
print(f"{'Feature':<20} {header[1]:<25} {header[2]}")
print("-" * 65)
for feature, pip_val, uv_val in rows:
    print(f"{feature:<20} {pip_val:<25} {uv_val}")
```

## uv Workflow

```python
# uv commands and what they do
uv_commands = [
    ("uv venv",                    "Create .venv in current directory"),
    ("uv sync",                    "Install deps from pyproject.toml + uv.lock"),
    ("uv add typer",               "Add typer to [project.dependencies]"),
    ("uv add --dev pytest",        "Add pytest to [tool.uv.dev-dependencies]"),
    ("uv remove requests",         "Remove a dependency"),
    ("uv run pytest",              "Run command inside the virtual environment"),
    ("uv python install 3.12",     "Download and install Python 3.12"),
    ("uv python pin 3.12",         "Pin this project to Python 3.12"),
    ("uv lock",                    "Regenerate uv.lock without installing"),
]

print("Common uv commands:")
for cmd, description in uv_commands:
    print(f"  $ {cmd:<35} # {description}")
```

## The uv.lock File

```python
# uv.lock pins every transitive dependency to an exact version
# Ensures everyone on the team gets identical installations

lock_concept = {
    "pyproject.toml": "what you want (>=3.11, typer>=0.12)",
    "uv.lock":        "what you get (typer==0.12.3, click==8.1.7, ...)",
}

print("Two files, two purposes:")
for filename, purpose in lock_concept.items():
    print(f"  {filename:<20}: {purpose}")

print()
print("Rule: commit BOTH files to git")
print("  pyproject.toml -> version ranges for flexibility")
print("  uv.lock        -> exact versions for reproducibility")
print()

# Show what a minimal lock entry looks like conceptually
lock_entry = {
    "package": "typer",
    "version": "0.12.3",
    "source":  "registry",
    "requires": ["click>=7.1.1", "typing-extensions>=3.7.4.3"],
    "hash": "sha256:abc123...",
}

print("A lock file entry captures:")
for key, value in lock_entry.items():
    print(f"  {key}: {value}")
```

## Reproducible Environments in CI

```python
# How the lock file makes CI reliable
ci_workflow_steps = [
    "1. Developer runs 'uv add somelib'",
    "   -> pyproject.toml updated: somelib>=1.2",
    "   -> uv.lock updated: somelib==1.2.5 + all transitive deps pinned",
    "",
    "2. Developer commits both files",
    "",
    "3. CI runs 'uv sync'",
    "   -> reads uv.lock",
    "   -> installs exactly somelib==1.2.5",
    "   -> every CI run, every developer, every machine: identical",
    "",
    "4. Without a lockfile (pip freeze):",
    "   -> next week somelib releases 1.3.0 with a breaking change",
    "   -> 'pip install somelib>=1.2' installs 1.3.0",
    "   -> CI breaks -- but only on new runs, not old ones",
    "   -> classic 'works on my machine' scenario",
]

for step in ci_workflow_steps:
    print(step)
```

## Virtual Environments and uv at a Glance

| Concept | pip + venv | uv |
|---|---|---|
| Create environment | `python -m venv .venv` | `uv venv` |
| Install project | `pip install -e '.[dev]'` | `uv sync` |
| Add dependency | Edit toml + `pip install` | `uv add pkg` |
| Lockfile | `pip freeze > requirements.txt` | `uv.lock` (auto) |
| Speed | Baseline | 10-100x faster |

## Your Turn

Create a virtual environment for a small project using `python -m venv .venv`, activate it, and check which Python executable is used by running `which python` (macOS/Linux) or `where python` (Windows). Then deactivate it and check again. Confirm the path changes on activation.

## Conclusion

Virtual environments isolate project dependencies so projects with conflicting requirements coexist on the same machine. `uv` is a modern replacement for pip that creates environments in milliseconds, manages lockfiles automatically, and can install Python itself. The next lesson covers building distributable packages: wheels and source distributions.

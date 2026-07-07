## Introduction

Nia's `metric-utils` folder now has the right shape. What it does not have is a way to install itself. When her teammate runs `pip install .`, pip prints a polite error about missing metadata. Pip needs to know the name of the project, its version, what Python versions it supports, and which tool should build it. All of that lives in a single file at the project root: `pyproject.toml`.

This lesson writes that file from scratch and explains the one part every author gets wrong at least once: the build backend.

![A pyproject.toml file at the root of the metric-utils project, with arrows pointing to sections for build-system, project metadata, and tool configuration](images/02_pyprojecttoml_and_build_backends.png)

## What `pyproject.toml` Replaces

Before 2016, a Python project needed a `setup.py`, sometimes a `setup.cfg`, a `requirements.txt`, and often a `MANIFEST.in`. Different tools read different files. `pyproject.toml` was introduced by PEP 518 and PEP 621 to be the single source of truth. Modern projects use only this one file:

```python
files_replaced = {
    "setup.py":         "project metadata now lives in [project]",
    "setup.cfg":        "tool config now lives in [tool.<name>]",
    "requirements.txt": "dependencies now live in [project] dependencies",
    "MANIFEST.in":      "included files now come from the build backend",
}

for old, new in files_replaced.items():
    print(f"{old:18s} -> {new}")
```

## A Minimal `pyproject.toml`

Here is the smallest working file for `metric-utils`. Nia saves this at the project root:

```toml
# pyproject.toml

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "metric-utils"
version = "0.1.0"
description = "Small rolling-statistics helpers for time-series data."
readme = "README.md"
requires-python = ">=3.10"
authors = [{ name = "Nia Okafor", email = "nia@example.com" }]
license = { text = "MIT" }
dependencies = [
    "numpy>=1.24",
]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.4"]

[project.scripts]
metric-utils = "metric_utils.cli:main"
```

Three blocks matter here: `[build-system]` picks a build backend, `[project]` describes the package, and `[project.scripts]` maps a command-line name to a Python function so users get a `metric-utils` command after installing.

## What a Build Backend Actually Does

A **build backend** is the program that reads `pyproject.toml`, packages the code in `src/`, and produces the two file formats pip understands: a wheel (`.whl`) and a source distribution (`.tar.gz`). Pip itself is not a build backend. It calls whichever backend the file names in `[build-system]`.

```python
backends = {
    "hatchling":     "modern default, minimal config, great for pure-Python",
    "setuptools":    "the classic, still supported, more configuration knobs",
    "flit-core":     "very small, ideal for single-module libraries",
    "poetry-core":   "used when the project is managed by Poetry",
    "pdm-backend":   "used when the project is managed by PDM",
}

for name, note in backends.items():
    print(f"{name:14s} -> {note}")
```

For a first-time author, `hatchling` is the recommended choice. It reads `[project]` directly, needs no extra `[tool.hatch]` section for a simple library, and has clear error messages when something is off.

## The `[project]` Section, Field by Field

Every field in `[project]` is defined by PEP 621, so the same names work no matter which backend you pick:

```python
fields = [
    ("name",            "the pip-installable name (dashes allowed)"),
    ("version",         "the released version string"),
    ("description",     "one-line summary shown on PyPI"),
    ("readme",          "path to the long description file"),
    ("requires-python", "which Python versions the package supports"),
    ("authors",         "list of name and email pairs"),
    ("license",         "an SPDX identifier or a text field"),
    ("dependencies",    "packages that must be installed with this one"),
    ("optional-dependencies", "extras like 'dev' or 'docs' for opt-in installs"),
    ("scripts",         "CLI commands the package should register"),
]

for name, note in fields:
    print(f"{name:24s} -> {note}")
```

## Tool Config Lives Here Too

Any tool that supports `pyproject.toml` reads its own section named `[tool.<name>]`. This keeps the whole project configured in one file:

```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
```

When a new developer joins the team, they open one file and see the entire toolchain at a glance.

## Verifying the File

The fastest way to catch a broken `pyproject.toml` is to install the project locally in editable mode:

```console
pip install -e .
```

If the metadata is invalid, pip refuses immediately with a clear message. If it succeeds, Python can now import the package from anywhere and the `metric-utils` command is on the shell path.

## `pyproject.toml` at a Glance

| Section | Purpose |
|---|---|
| `[build-system]` | which backend builds the package |
| `[project]` | metadata: name, version, dependencies |
| `[project.optional-dependencies]` | extras like `dev`, `docs`, `test` |
| `[project.scripts]` | maps CLI names to Python functions |
| `[tool.<name>]` | configuration for tools like ruff, pytest, mypy |

## Your Turn

Write a `pyproject.toml` for a small package called `text-cleaner` that has one dependency on `regex`, a dev extra with `pytest`, a script called `clean-text` mapped to `text_cleaner.cli:main`, and uses `hatchling` as the backend. Run `pip install -e .` to confirm it works.

## Conclusion

`pyproject.toml` is the single file that turns a folder of Python code into a real project. `[build-system]` chooses the tool that packages it, `[project]` describes it to users and to PyPI, and `[tool.<name>]` sections keep the rest of the toolchain in the same place. With metadata declared, the next lesson brings in `uv` to manage the environments and dependency versions the file promises.

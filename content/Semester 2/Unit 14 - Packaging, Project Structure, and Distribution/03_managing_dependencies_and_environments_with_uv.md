## Introduction

Nia's `pyproject.toml` promises numpy will be installed with the package. On her laptop, that promise is kept by a `venv` she set up months ago. Her teammate has numpy too, but a different major version. Their build server has no numpy at all. Three machines, three versions, three sets of behavior. Nothing in the current setup fixes that.

What the project needs is a single tool that creates the virtual environment, installs the exact dependency versions declared, and locks those versions so every machine agrees. That tool is `uv`.

![Three developer machines each running uv sync from the same pyproject.toml and uv.lock, all ending with identical environments](images/03_managing_dependencies_and_environments_with_uv.png)

## What `uv` Is

`uv` is a Python package and project manager written in Rust. It replaces a stack of older tools with one command: it creates virtual environments, installs dependencies, resolves version conflicts, and produces a lockfile. It also runs commands inside the project's environment without needing `source .venv/bin/activate`.

```python
# What each command does in one line

commands = {
    "uv init":       "create a new project scaffold",
    "uv add":        "add a dependency to pyproject.toml and install it",
    "uv remove":     "remove a dependency",
    "uv sync":       "install exactly what the lockfile says",
    "uv lock":       "refresh the lockfile from pyproject.toml",
    "uv run":        "run a command inside the project environment",
    "uv pip":        "a drop-in replacement for pip that is much faster",
}

for name, note in commands.items():
    print(f"{name:12s} -> {note}")
```

## Installing `uv`

`uv` is a single binary. On macOS and Linux:

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows PowerShell:

```console
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Once installed, `uv --version` prints the version and no further Python setup is required to use it.

## Adding a Dependency

Nia opens `metric-utils` and adds numpy the `uv` way:

```console
uv add "numpy>=1.24"
```

Three things happen. `uv` records `numpy>=1.24` in `[project] dependencies` of `pyproject.toml`. It creates `.venv/` on the first run if it does not exist. It writes an entry into `uv.lock` pinning the exact numpy version and the versions of every package numpy depends on. The next teammate who runs `uv sync` gets the same numpy, down to the patch.

## Dev Dependencies and Extras

Test frameworks and linters should not ship to end users. `uv` stores them separately:

```console
uv add --dev pytest ruff
```

This puts them under `[dependency-groups] dev` in `pyproject.toml` (a modern PEP 735 group) and installs them into the local `.venv/`. When someone runs `uv sync` in production without dev tools, they get numpy only. When a developer runs `uv sync --group dev`, they get numpy, pytest, and ruff.

Older projects use the `[project.optional-dependencies]` mechanism from lesson 2. `uv` supports both; groups are the preferred choice for tools that only run during development.

## The Lockfile

`uv.lock` is the single most important file for reproducibility:

```python
# What lives in uv.lock

lock_contents = [
    ("exact versions",   "numpy 1.26.4, not just 'numpy>=1.24'"),
    ("all transitives",  "every package numpy depends on, and their versions"),
    ("hashes",           "cryptographic hashes so installs cannot be tampered with"),
    ("platform info",    "which markers apply on Linux, macOS, Windows"),
]

for name, note in lock_contents:
    print(f"{name:16s} -> {note}")
```

Commit `uv.lock` to git alongside `pyproject.toml`. Every teammate, every build server, every deploy uses `uv sync` to reproduce that exact environment. The old "works on my machine" problem is gone by construction.

## Running Commands Without Activating

Activation scripts are easy to forget. `uv run` puts the environment on the path for one command:

```console
uv run pytest
uv run python -m metric_utils
uv run ruff check src/
```

Each of those uses the project's `.venv/` even from a fresh shell. No `source .venv/bin/activate` step is required.

## Refreshing Dependencies

When Nia wants newer versions inside the ranges declared in `pyproject.toml`:

```console
uv lock --upgrade
uv sync
```

`uv lock --upgrade` produces a fresh lockfile with the latest allowed versions. `uv sync` applies it. She commits both files together and the update is reviewable in a single pull request.

## `uv` at a Glance

| Command | What it does |
|---|---|
| `uv add <pkg>` | add a runtime dependency |
| `uv add --dev <pkg>` | add a development-only dependency |
| `uv remove <pkg>` | remove a dependency |
| `uv sync` | install exactly what `uv.lock` records |
| `uv lock --upgrade` | rebuild `uv.lock` with newer allowed versions |
| `uv run <cmd>` | run a command inside the project environment |
| `uv.lock` | the file committed to git for reproducibility |

## Your Turn

In the `metric-utils` project, run `uv add "numpy>=1.24"` and `uv add --dev pytest ruff`. Confirm that `.venv/` was created, that `uv.lock` was written, and that `uv run pytest` works even from a brand-new shell where the venv was never activated. Then delete `.venv/` and run `uv sync`; the environment should come back identical.

## Conclusion

`uv` gives the project one command for every stage of dependency management: `add` to declare, `lock` to freeze, `sync` to install, and `run` to execute. The lockfile turns "the same package versions" from a hope into a guarantee. With reproducible environments in place, the next lesson turns the source in `src/` into the two files pip actually consumes: a wheel and a source distribution.

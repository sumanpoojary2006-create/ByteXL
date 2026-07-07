## Introduction

Nia has spent six months building a small library at work called `metric-utils`. It computes rolling averages, percentiles, and a few custom stats her team needs. Everything sits in one folder next to a `main.py`, a couple of `test_*.py` files, and a `requirements.txt`. It works on her laptop. It breaks on her teammate's laptop, breaks again on the build server, and passes tests only when she is standing next to them.

The issue is not the code. The issue is layout. Before a project can be installed, published, or trusted, its files must sit in a shape that Python and its tools recognize. This lesson gives that shape a name and shows why professionals use it.

![A messy flat folder of Python files on the left, transformed into a clean src-layout project on the right with pyproject.toml at the root](images/01_professional_project_layout.png)

## The src Layout

The most reliable structure for an installable Python project is called the **src layout**. Source code lives inside a folder called `src/`, tests live in a sibling `tests/`, and configuration files sit at the top:

```python
# Recommended project layout for metric-utils

layout = {
    "metric-utils/": {
        "src/": {
            "metric_utils/": {
                "__init__.py":   "makes metric_utils a package",
                "rolling.py":    "rolling-average functions",
                "percentiles.py":"percentile helpers",
                "cli.py":        "command-line entry point",
            }
        },
        "tests/": {
            "__init__.py":       "makes tests a package",
            "test_rolling.py":   "tests for rolling.py",
            "test_percentiles.py":"tests for percentiles.py",
        },
        "pyproject.toml":        "single source of truth for the project",
        "README.md":             "user-facing description",
        ".gitignore":            "files git should ignore",
    }
}

def show(tree, indent=0):
    for name, value in tree.items():
        print("  " * indent + name)
        if isinstance(value, dict):
            show(value, indent + 1)
        else:
            print("  " * (indent + 1) + f"# {value}")

show(layout)
```

Notice the folder name uses a dash (`metric-utils`) but the package name inside `src/` uses an underscore (`metric_utils`). Python cannot import a dash. This is one of the first rules the layout enforces.

## Why Not Keep Everything at the Root?

Nia's flat layout looked like this:

```
metric-utils/
    rolling.py
    percentiles.py
    cli.py
    test_rolling.py
    requirements.txt
```

That structure passes tests on her machine because Python adds the current directory to `sys.path` when she runs `pytest`. On the build server, tests import a version of the code that was never installed, or worse, no version at all. The `src` layout blocks that shortcut on purpose:

```python
# Two structures compared

flat_layout = {
    "problem_1": "tests find code by accident (current directory on sys.path)",
    "problem_2": "installed package can shadow the source you are editing",
    "problem_3": "no clean line between source and project metadata",
}

src_layout = {
    "benefit_1": "tests must import the installed package, matching real users",
    "benefit_2": "source code and project files are visually separated",
    "benefit_3": "packaging tools know exactly where to look",
}

for label, note in flat_layout.items():
    print(f"flat  {label}: {note}")
print()
for label, note in src_layout.items():
    print(f"src   {label}: {note}")
```

Because the `src` folder is not on `sys.path` by default, tests only pass if the package was properly installed with something like `pip install -e .`. That single constraint catches most packaging mistakes before a user ever sees them.

## The Role of `__init__.py`

A folder becomes a Python **package** the moment it contains an `__init__.py` file. Without it, you have a folder of scripts. With it, you have something importable:

```python
# src/metric_utils/__init__.py

from .rolling import rolling_mean, rolling_median
from .percentiles import percentile

__version__ = "0.1.0"
__all__ = ["rolling_mean", "rolling_median", "percentile"]
```

Three things are happening here. The relative imports (`from .rolling import ...`) expose the package's top-level API so users can write `from metric_utils import rolling_mean` instead of `from metric_utils.rolling import rolling_mean`. `__version__` gives the package a version string that other tools can read. `__all__` declares the public API and hides everything else from wildcard imports.

## Tests Belong Outside `src/`

New authors sometimes place tests inside `src/metric_utils/tests/`. That ships the tests to end users, which they do not need, and it complicates the import path. A sibling `tests/` folder at the project root is the standard:

```python
# Where does each file go?

placements = [
    ("Application code",         "src/metric_utils/"),
    ("Test files",               "tests/"),
    ("Project metadata",         "pyproject.toml at the root"),
    ("Documentation",            "README.md, docs/ at the root"),
    ("Automation config",        ".pre-commit-config.yaml, .github/ at the root"),
]

for kind, place in placements:
    print(f"{kind:22s} -> {place}")
```

## Professional Project Layout at a Glance

| Item | Location | Purpose |
|---|---|---|
| `src/<package>/` | inside `src/` | the code users install |
| `__init__.py` | every package folder | marks the folder as a package |
| `tests/` | at the project root | not installed, run by developers |
| `pyproject.toml` | at the project root | one place for metadata and config |
| `README.md` | at the project root | first thing a new user reads |

## Your Turn

Draw the directory tree for a project called `weather-tools` with two sub-packages: `weather_tools.forecast` and `weather_tools.stations`. Include `__init__.py` files, a `tests/` folder, and `pyproject.toml`. Then answer in one sentence why moving the source into `src/` prevents a whole category of import bugs.

## Conclusion

The `src` layout is not a stylistic preference. It is a structural rule that separates source from project files, forces tests to use the installed package, and gives every packaging tool a predictable place to look. With the shape in place, the next lesson fills the empty `pyproject.toml` and turns this folder into a real distributable project.

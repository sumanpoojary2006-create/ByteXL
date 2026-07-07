## Introduction

Dev types `pip install .` in the project root. pip looks for a file named `pyproject.toml` that tells it what the project is called, what Python version it requires, which third-party packages it depends on, and where the source code lives. Without that file, pip has nothing to read and the install fails.

`pyproject.toml` replaced the older `setup.py` and `setup.cfg` files. It is the single source of truth for every tool in the project: the package manager, the linter, the formatter, and the test runner all read from it.

![A pyproject.toml file in the center with arrows pointing outward to pip, ruff, black, mypy, and pytest -- all reading their configuration from the same file](images/02_pyproject_toml.png)

## Minimal pyproject.toml

```python
# Represent the minimal pyproject.toml as Python data
# (In a real project this is a TOML file, not Python)

minimal_config = {
    "build-system": {
        "requires": ["hatchling"],
        "build-backend": "hatchling.build",
    },
    "project": {
        "name": "library-system",
        "version": "0.1.0",
        "requires-python": ">=3.11",
        "dependencies": [],
    }
}

print("Minimal pyproject.toml sections:")
for section, content in minimal_config.items():
    print(f"\n[{section}]")
    for key, value in content.items():
        print(f"  {key} = {repr(value)}")
```

The real file looks like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "library-system"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
```

## Adding Metadata and Dependencies

```python
# Full project metadata
metadata = {
    "name": "library-system",
    "version": "0.1.0",
    "description": "A command-line library catalog management tool",
    "authors": [{"name": "Dev Patel", "email": "dev@example.com"}],
    "license": {"text": "MIT"},
    "requires-python": ">=3.11",
    "dependencies": [
        "typer>=0.12",
        "rich>=13.0",
    ],
}

print("Project metadata:")
for key, value in metadata.items():
    print(f"  {key}: {value}")

print()
print("Runtime dependencies:")
for dep in metadata["dependencies"]:
    name, version = dep.split(">=")
    print(f"  {name.strip():<15} requires version >= {version.strip()}")
```

## Optional Dependency Groups

```python
# Optional extras separate runtime from development dependencies
extras = {
    "dev": [
        "pytest>=8.0",
        "pytest-cov>=5.0",
        "ruff>=0.4",
        "black>=24.0",
        "mypy>=1.9",
    ],
    "docs": [
        "mkdocs>=1.5",
        "mkdocs-material>=9.5",
    ],
}

print("Optional dependency groups:")
for group, deps in extras.items():
    print(f"\n[project.optional-dependencies.{group}]")
    for dep in deps:
        print(f"  {dep}")

print()
print("Install command:")
print("  pip install -e .          # runtime only")
print("  pip install -e '.[dev]'   # runtime + dev tools")
print("  pip install -e '.[dev,docs]'  # everything")
```

## Tool Configuration Sections

```python
# Tools read their config from [tool.TOOLNAME] sections
tool_configs = {
    "ruff": {
        "line-length": 88,
        "select": ["E", "W", "F", "I", "N", "UP"],
        "ignore": ["E501"],
    },
    "black": {
        "line-length": 88,
        "target-version": ["py311", "py312"],
    },
    "mypy": {
        "python_version": "3.11",
        "strict": True,
        "ignore_missing_imports": True,
    },
    "pytest.ini_options": {
        "testpaths": ["tests"],
        "addopts": "--cov=library --cov-report=term-missing",
    },
}

print("Tool configuration sections in pyproject.toml:")
for tool, config in tool_configs.items():
    print(f"\n[tool.{tool}]")
    for key, value in config.items():
        print(f"  {key} = {repr(value)}")
```

## Specifying the Package Location (src layout)

```python
# Tell hatchling (or setuptools) where the source lives
hatch_config = {
    "build": {
        "packages": ["src/library"]
    }
}

setuptools_config = {
    "package-dir": {"": "src"},
    "packages": {"find": {"where": ["src"]}},
}

print("hatchling (recommended):")
print("  [tool.hatch.build.targets.wheel]")
print("  packages = ['src/library']")

print()
print("setuptools alternative:")
print("  [tool.setuptools.packages.find]")
print("  where = ['src']")

print()
print("Both tell the build tool: 'the library package is in src/'")
print("Without this, pip install would not find the package")
```

## Versioning Strategies

```python
# Semantic versioning: MAJOR.MINOR.PATCH
def parse_version(version_str):
    parts = version_str.split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    return {"major": major, "minor": minor, "patch": patch}

versions = [
    ("0.1.0", "Initial release -- not yet stable"),
    ("0.2.0", "Added CLI commands -- backwards compatible new feature"),
    ("0.2.1", "Fixed ISBN validation bug -- patch"),
    ("1.0.0", "Stable public API -- major milestone"),
    ("2.0.0", "Breaking change: removed old API methods"),
]

print(f"{'Version':<10} {'Type':<12} {'Meaning'}")
print("-" * 60)
for version, description in versions:
    parts = parse_version(version)
    if parts["major"] == 0:
        vtype = "pre-stable"
    elif "patch" in description:
        vtype = "patch"
    elif "Breaking" in description:
        vtype = "major"
    else:
        vtype = "minor"
    print(f"{version:<10} {vtype:<12} {description}")
```

## pyproject.toml at a Glance

| Section | Purpose |
|---|---|
| `[build-system]` | Which build tool to use (hatchling, setuptools) |
| `[project]` | Package name, version, dependencies, metadata |
| `[project.optional-dependencies]` | Extra install groups like `[dev]`, `[docs]` |
| `[project.scripts]` | CLI entry points |
| `[tool.ruff]` | ruff linter configuration |
| `[tool.black]` | black formatter configuration |
| `[tool.mypy]` | mypy type checker configuration |
| `[tool.pytest.ini_options]` | pytest configuration |

## Your Turn

Write out (as text) a `pyproject.toml` for a package called `bookworm` that:
- Requires Python 3.11+
- Depends on `typer>=0.12` at runtime
- Has a `[dev]` extras group with `pytest` and `ruff`
- Sets ruff's line length to 100

Then write the pip command that would install `bookworm` in editable mode with dev dependencies.

## Conclusion

`pyproject.toml` is the single configuration file for a modern Python project: package metadata, dependencies, extras groups, and tool configuration all live here. The `[build-system]` section tells pip which build backend to use. Tool sections keep all project configuration in one file and out of scattered `.cfg` and `.ini` files. The next lesson covers `uv`, a faster alternative to pip for dependency management.

## Introduction

Dev wants to share the library system with other libraries in the region. He could zip the source folder and email it, but the recipient would have to figure out dependencies, file paths, and import structures themselves. A proper Python package installs with a single command, resolves dependencies automatically, and appears in the recipient's Python environment like any other library.

This lesson covers building a wheel, testing the installation locally, and publishing to PyPI.

![The packaging pipeline: source code -> build creates a .whl file -> test install from local file -> publish to PyPI -> anyone can pip install](images/04_building_and_publishing.png)

## What a Wheel Is

```python
# A wheel (.whl) is a zip archive with a specific structure
# Python can install it without a build step

wheel_facts = {
    "Extension":     ".whl (actually a renamed .zip file)",
    "Naming":        "library_system-0.1.0-py3-none-any.whl",
    "Name parts":    "package-version-pythonver-abi-platform",
    "Contents":      "source files + metadata (no build step on install)",
    "vs sdist":      "sdist (.tar.gz) contains source; wheel is pre-built",
    "Install speed": "wheel installs faster: no compilation step",
}

print("What a wheel file is:")
for fact, description in wheel_facts.items():
    print(f"  {fact:<15}: {description}")

# Wheel name decoding
wheel_name = "library_system-0.1.0-py3-none-any.whl"
parts = wheel_name.replace(".whl", "").split("-")
labels = ["Package", "Version", "Python", "ABI", "Platform"]
print(f"\nDecoding: {wheel_name}")
for label, part in zip(labels, parts):
    print(f"  {label:<10}: {part}")
```

## The Build Step

```python
# Show what 'python -m build' or 'uv build' produces
import os

def simulate_build_output():
    dist_contents = [
        "dist/",
        "  library_system-0.1.0.tar.gz   # source distribution",
        "  library_system-0.1.0-py3-none-any.whl  # wheel",
    ]
    print("After 'python -m build' or 'uv build':")
    for line in dist_contents:
        print(" ", line)

simulate_build_output()

print()
print("What happens during build:")
steps = [
    "1. Reads pyproject.toml for metadata",
    "2. Collects source files from src/library/",
    "3. Writes METADATA file inside the wheel",
    "4. Creates the .whl zip archive",
    "5. Creates the .tar.gz source archive",
]
for step in steps:
    print(" ", step)
```

## Installing and Testing Locally

```python
# Before publishing, test the wheel on the same machine

install_steps = [
    ("Build",              "uv build",                              "Creates dist/*.whl"),
    ("Install local",      "pip install dist/library_system*.whl",  "Install from file"),
    ("Verify installed",   "pip show library-system",               "Check metadata"),
    ("Test import",        "python -c 'import library; print(library.__version__)'", "Confirm importable"),
    ("Test CLI",           "library-system --help",                 "Check entry point"),
    ("Uninstall",          "pip uninstall library-system",          "Clean up"),
]

print("Local install and test workflow:")
for label, command, description in install_steps:
    print(f"\n  [{label}]")
    print(f"    $ {command}")
    print(f"    # {description}")
```

## What PyPI Is

```python
# PyPI: the Python Package Index
pypi_facts = {
    "URL":           "https://pypi.org",
    "Size":          "600,000+ packages (as of 2024)",
    "Install":       "pip install package-name reads from PyPI by default",
    "Test PyPI":     "https://test.pypi.org -- safe sandbox for practice uploads",
    "Authentication":"API tokens (never use username/password in scripts)",
    "Upload tool":   "twine or uv publish",
}

print("Python Package Index (PyPI):")
for key, value in pypi_facts.items():
    print(f"  {key:<16}: {value}")

print()
print("Workflow summary:")
workflow = [
    "1. Create account on test.pypi.org (free)",
    "2. Generate an API token in account settings",
    "3. Store token in ~/.pypirc or as TWINE_PASSWORD env var",
    "4. Build: uv build",
    "5. Upload to Test PyPI: twine upload --repository testpypi dist/*",
    "6. Install from Test PyPI: pip install --index-url https://test.pypi.org/simple/ library-system",
    "7. Verify everything works",
    "8. Upload to real PyPI: twine upload dist/*",
]
for step in workflow:
    print(f"  {step}")
```

## Semantic Versioning in Practice

```python
# Decide version bump type based on the change

changes = [
    ("Added --verbose flag to CLI",                    "0.1.0", "0.1.1", "patch"),
    ("Fixed crash on empty ISBN field",                "0.1.1", "0.1.2", "patch"),
    ("Added export-to-csv command",                    "0.1.2", "0.2.0", "minor"),
    ("Added PostgreSQL support",                       "0.2.0", "0.3.0", "minor"),
    ("Renamed 'add-book' command to 'catalog add'",    "0.3.0", "1.0.0", "major (breaking)"),
    ("Fixed typo in error message",                    "1.0.0", "1.0.1", "patch"),
]

print(f"{'Change':<47} {'Before':<8} {'After':<8} {'Bump'}")
print("-" * 75)
for change, before, after, bump in changes:
    print(f"{change:<47} {before:<8} {after:<8} {bump}")

print()
print("Rule: never break 1.x.x users with a 1.x.y release")
print("Rule: 0.x.y versions can break any time (pre-stable)")
```

## Checking the Published Package

```python
# After uploading, verify the package is findable and installable

verification = {
    "pip search":        "pip index versions library-system",
    "pip info":          "pip show library-system",
    "install from pypi": "pip install library-system",
    "import check":      "python -c 'import library; print(library.__version__)'",
    "uninstall":         "pip uninstall library-system",
}

print("Post-publish verification checklist:")
for step, command in verification.items():
    print(f"  [{step}]")
    print(f"    $ {command}")
    print()
```

## Building and Publishing at a Glance

| Step | Command | Tool |
|---|---|---|
| Build wheel + sdist | `uv build` or `python -m build` | `build` / `uv` |
| Test install locally | `pip install dist/*.whl` | `pip` |
| Upload to Test PyPI | `twine upload --repository testpypi dist/*` | `twine` |
| Upload to PyPI | `twine upload dist/*` | `twine` |
| Install from PyPI | `pip install library-system` | `pip` |

## Your Turn

Without actually publishing, write out the full sequence of terminal commands you would run to:
1. Build the library-system package
2. Install it into a fresh virtual environment
3. Test that `import library` works
4. Uninstall it

Then write the `twine` command you would use to upload to Test PyPI (not the real PyPI) as a safe practice step.

## Conclusion

A wheel is a pre-built zip archive that `pip` installs without any build step. `uv build` or `python -m build` creates it from `pyproject.toml`. Test installations locally before publishing. PyPI is the public index; Test PyPI is the sandbox. Semantic versioning signals to users what kind of change each release contains. The next lesson covers writing documentation that makes the package easy for others to use.

## Introduction

Nia's `metric-utils` project installs cleanly with `uv sync`. Her teammate can install it from the git clone. What she cannot yet do is send a single file to a colleague in another team and say "install this." For that, the project needs to be **built** into distribution artifacts: a wheel and a source distribution. These are the two file formats pip and PyPI understand, and every published Python package on the planet ships in at least one of them.

This lesson builds both, opens them, and shows what each contains.

![A pyproject.toml source project on the left, a build tool in the middle, and two output files on the right: a .whl wheel and a .tar.gz source distribution](images/04_building_wheels_and_source_distributions.png)

## Two Formats, One Purpose

A distribution is just a package delivered as a file. Python defines two:

```python
formats = {
    "wheel (.whl)":  "prebuilt, ready to install, fast",
    "sdist (.tar.gz)": "the source code plus metadata, must build before install",
}

for name, note in formats.items():
    print(f"{name:18s} -> {note}")
```

A wheel is what pip prefers because installation is a straight copy of files. An sdist is a safety net: if a wheel is not available for the user's platform or Python version, pip falls back to building one from the sdist on the spot.

## Building With `python -m build`

The standard tool is `build`. It is a small wrapper that calls whichever backend `pyproject.toml` declares and writes the results into a `dist/` folder:

```console
uv run python -m build
```

If `build` is not installed yet:

```console
uv add --dev build
```

The output, on Nia's project, looks like:

```
Successfully built metric_utils-0.1.0.tar.gz and metric_utils-0.1.0-py3-none-any.whl
```

Two files, both under `dist/`. Both are ready to install with pip.

## Anatomy of a Wheel

A wheel is a zip file with a specific name pattern. The pieces of the filename carry meaning:

```python
# metric_utils-0.1.0-py3-none-any.whl

pieces = [
    ("metric_utils",  "the importable package name (underscores)"),
    ("0.1.0",         "the version"),
    ("py3",           "any Python 3 interpreter"),
    ("none",          "no ABI restrictions (pure Python)"),
    ("any",           "any operating system"),
]

for value, meaning in pieces:
    print(f"{value:14s} -> {meaning}")
```

Pure Python wheels use `py3-none-any` and install on every platform. Packages with compiled C extensions produce multiple wheels, one for each platform tag (`macosx_11_0_arm64`, `manylinux2014_x86_64`, and so on). pip picks the one matching the user's system.

Inside, a wheel is just a zip:

```console
unzip -l dist/metric_utils-0.1.0-py3-none-any.whl
```

You will see the `metric_utils/` code, a `metric_utils-0.1.0.dist-info/` folder with metadata (name, version, license, dependencies), and a `RECORD` file listing every file plus its hash.

## Anatomy of a Source Distribution

An sdist is a gzipped tarball of the source needed to build a wheel. It contains `pyproject.toml`, `src/`, `README.md`, and enough files to reproduce the wheel with `python -m build`.

```console
tar -tzf dist/metric_utils-0.1.0.tar.gz
```

Sdists exist so users on unusual platforms or Python versions can build the package themselves, and so historians can trace exactly which source produced a given release. PyPI accepts both formats and stores both alongside the release.

## Installing the Built Artifact

The whole point of building is to make the artifact installable anywhere pip runs:

```console
pip install dist/metric_utils-0.1.0-py3-none-any.whl
```

That file could have been emailed, copied to a USB stick, or downloaded from an internal server. Once pip has it, the package is installed the same way a PyPI release would be. The wheel is portable in every sense that matters.

## Checking Before Publishing

Before pushing artifacts to PyPI, run one quick check to catch metadata mistakes:

```console
uv run python -m twine check dist/*
```

`twine check` warns about broken README rendering (PyPI expects reStructuredText or Markdown with a declared content type) and missing metadata fields. Fixing these locally is much cheaper than yanking a broken release.

## A Clean Rebuild

Nia should delete the previous `dist/` before every build so old wheels from earlier versions do not accumulate:

```console
rm -rf dist/ build/ src/*.egg-info
uv run python -m build
```

Some workflows automate this with a Makefile or a `justfile` command. The rule is the same: the `dist/` folder should contain only the artifacts for the version currently being released.

## Build Artifacts at a Glance

| Artifact | Extension | Contents | Speed to install |
|---|---|---|---|
| Wheel | `.whl` | prebuilt files, ready to copy | fast |
| Source distribution | `.tar.gz` | source, requires a build step | slower |
| Metadata folder | `.dist-info/` inside wheel | name, version, dependencies, RECORD | not installed alone |

## Your Turn

In the `metric-utils` project, run `uv run python -m build`. Confirm that `dist/` now contains both a `.whl` and a `.tar.gz`. Unzip the wheel and locate the `METADATA` file inside `.dist-info/`. Then create a fresh throwaway virtual environment and run `pip install dist/metric_utils-0.1.0-py3-none-any.whl`; confirm that `python -c "import metric_utils; print(metric_utils.__version__)"` prints `0.1.0`.

## Conclusion

Building a package produces two files: a wheel for fast installs and a source distribution as a safety net. Both live under `dist/`, both are signed by their filename tags, and both can be installed with a single `pip install`. With the artifacts in hand, the next lesson decides what version number to stamp on the next one.

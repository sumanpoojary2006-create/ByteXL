## Introduction

Naveen finally hands his hostel project over to next year's committee, the same handover the functions unit left him preparing for, except this time the problem is not unclear code, it is missing packages. The new committee clones his project folder, tries to run it, and Python immediately complains that `requests` is not installed. Naveen remembers installing it himself, months ago, into his own `venv`, a folder he never shared because virtual environments, as the earlier lesson explained, are not meant to be passed around directly. The new committee has no way of knowing what to install, or which versions, just by looking at his code.

What Naveen actually needed to hand over was not the environment itself, but a clear, exact list of what it contained, so anyone, anywhere, could rebuild an identical environment in moments. That list is conventionally called a **requirements file**, and it is the key to a genuinely **reproducible setup**.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/09_requirements_file_reproducibility.png)

## Generating a Requirements File

`pip` can inspect everything currently installed in your active environment and write it out to a plain text file, conventionally named `requirements.txt`.

```console
pip freeze > requirements.txt
```

`pip freeze` lists every installed package together with its exact version, and the `>` redirects that output into a file instead of just printing it to the screen.

```
requests==2.31.0
```

A `requirements.txt` like this is a precise, shareable snapshot: not just "this project needs requests," but "this project was built and tested against requests version 2.31.0 specifically."

## Recreating an Environment From a Requirements File

Anyone with this file, on any machine, can recreate the exact same set of packages with a single command, run inside their own freshly created virtual environment.

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`pip install -r requirements.txt` reads the file and installs every listed package at its listed version, in one step, which is exactly what Naveen should have committed alongside his code from the very beginning.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/09_requirements_install_recreate.png)


## What Belongs in Version Control

| Should Be Shared | Should Not Be Shared |
|---|---|
| Your actual code (`.py` files) | The `.venv` folder itself |
| `requirements.txt` | Your personal cache of downloaded packages |
| Project documentation | Anything machine-specific to your own laptop |

The `.venv` folder is large, entirely reconstructable, and often contains paths specific to your own machine; sharing `requirements.txt` instead lets every collaborator rebuild their own clean, correct environment locally.

## The uv Equivalent

If a project uses `uv` instead, dependency tracking happens automatically as you `uv add` packages, recorded in project files (commonly `pyproject.toml`, alongside a lock file) rather than a hand-generated `requirements.txt`. A fresh collaborator with `uv` installed can typically recreate the entire environment with a single command.

```console
uv sync
```

This reads the project's recorded dependencies and rebuilds a matching environment in one step, the `uv`-native equivalent of `pip install -r requirements.txt`, simply driven by the project's own dependency files instead of a separate, manually generated list.

## Reproducibility at a Glance

| Tool | Record Dependencies With | Recreate an Environment With |
|---|---|---|
| pip + venv | `pip freeze > requirements.txt` | `pip install -r requirements.txt` |
| uv | Automatic, via `uv add` | `uv sync` |

## Why This Matters Beyond One Hostel Project

Reproducibility is not just a courtesy to the next person; it protects you too. Six months from now, on a new laptop, or after your own `.venv` is accidentally deleted, a `requirements.txt` (or its `uv` equivalent) is the difference between rebuilding your exact working setup in one command and trying to remember every package you ever happened to install along the way.

## Your Turn: Plan a Reproducible Handover

```console
# Before handing off a project:
pip freeze > requirements.txt

# Whoever receives it:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

If you have a real project with a few installed packages, generate its `requirements.txt` for real, inspect what it actually lists, and confirm a fresh `venv` can install from it cleanly.

## Conclusion

A `requirements.txt` file, generated with `pip freeze` and consumed with `pip install -r requirements.txt`, turns "it works on my machine" into "it works on any machine," by recording the exact packages and versions a project depends on, separately from the project's actual code. `uv`-based projects track the same information automatically and rebuild it with `uv sync`. Across this entire unit, you have learned to organise code into modules, group modules into packages, install other people's published work with `pip`, isolate every project's dependencies with `venv` or `uv`, and now hand a finished project to someone else with confidence that it will actually run. That confidence, that your code travels intact to someone else's machine, is the real, practical payoff of everything this unit covered.

## Introduction

Naveen wants his receipts to print with a little color and a clean border in the terminal, the kind of polish the standard library's plain `print()` was never designed to give him. Somewhere out there, someone has almost certainly already written and shared exactly this kind of tool. He does not need to build it from scratch, and he does not need to copy code from a webpage into his own files by hand either. He needs a way to download someone else's finished package and use it in his own project, exactly the way he uses `math` or `random`.

That is exactly what `pip`, Python's package installer, is for, pulling ready-made packages from **PyPI**, the Python Package Index, the public library where the wider Python community shares its work.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/06_pip_install_from_pypi.png)

## What PyPI Actually Is

PyPI, short for the Python Package Index, is a public, online catalogue of Python packages that anyone can publish to and anyone can install from. The standard library modules from earlier in this unit ship with Python itself; PyPI packages do not, and need an explicit install step before they can be imported.

## Installing a Package With pip

`pip` is run from your terminal, not from inside a Python script, and the basic command is `pip install` followed by the package's name.

```console
pip install requests
```

This downloads the `requests` package, a hugely popular tool for talking to web pages and APIs, and makes it available to `import` in any script run with that same Python installation.

## Using What You Installed

Once installed, a third-party package is imported exactly like a standard library module; Python does not distinguish between the two once the install step is done.

```text
import requests

response = requests.get("https://example.com")
print(response.status_code)    # 200, if the page is reachable
```

The only real difference from `import math` is the invisible step that happened before this code ever ran: `requests` had to be installed first, while `math` was simply already there.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/06_pip_install_then_import.png)


## Checking What Is Installed

`pip` can also report on what is already available in your current environment.

```console
pip list
pip show requests
```

`pip list` prints every installed package, and `pip show requests` prints details about one specific package: its version, where it came from, and what it depends on.

## Uninstalling a Package

Removing something you no longer need follows the same pattern.

```console
pip uninstall requests
```

## pip Commands at a Glance

| Command | Effect |
|---|---|
| `pip install package_name` | Downloads and installs a package from PyPI |
| `pip list` | Lists every package currently installed |
| `pip show package_name` | Shows details about one installed package |
| `pip uninstall package_name` | Removes an installed package |

## A Question Worth Asking Before Installing Anything

Not every problem needs a third-party package. Before reaching for `pip install`, it is worth checking whether the standard library already covers the job, since a standard library module needs no install step, no version to manage, and no risk of going unmaintained. Reach for PyPI once you have confirmed the standard library genuinely does not cover what you need.

## Your Turn: Check Whether a Package Is Actually Installed

`pip show` from the terminal is one way to confirm a package is available, but a script can ask the exact same question of its own environment, using `importlib.util.find_spec`, which looks for a package without actually importing it.

```python
import importlib.util

for package_name in ("json", "receipt_colorizer"):
    found = importlib.util.find_spec(package_name) is not None
    print(f"{package_name}: {'installed' if found else 'not installed'}")
```

```text
json: installed
receipt_colorizer: not installed
```

`json` reports as installed because it ships with the standard library, present in every Python environment with no `pip install` ever required. `receipt_colorizer` is a made-up package name, standing in for any third-party package nobody has installed yet, so it reports as not installed. Running `pip install some_real_package_name` in a real terminal, then rerunning this exact check there, is what flips a package from `not installed` to `installed`, which is the whole job `pip` does.

## Conclusion

`pip` is Python's package installer, used from the terminal to download packages published on PyPI, the public Python Package Index, with `pip install package_name` as the core command, alongside `pip list`, `pip show`, and `pip uninstall` for managing what is already there. Once installed, a third-party package imports exactly like any standard library module. Installing packages globally onto your machine works, but it quietly risks one project's needs conflicting with another's, which is exactly the problem the next lesson, on virtual environments, exists to solve.

## Introduction

Naveen wants his receipts to print with a little color and a clean border in the terminal, the kind of polish the standard library's plain `print()` was never designed to give him. Somewhere out there, someone has almost certainly already written and shared exactly this kind of tool. He does not need to build it from scratch, and he does not need to copy code from a webpage into his own files by hand either. He needs a way to download someone else's finished package and use it in his own project, exactly the way he uses `math` or `random`.

That is exactly what `pip`, Python's package installer, is for, pulling ready-made packages from **PyPI**, the Python Package Index, the public library where the wider Python community shares its work.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/06_pip_install_from_pypi.png)

## What PyPI Actually Is

PyPI, short for the Python Package Index, is a public, online catalogue of Python packages that anyone can publish to and anyone can install from. The standard library modules from earlier in this unit ship with Python itself; PyPI packages do not, and need an explicit install step before they can be imported.

## Installing a Package With pip

`pip` is run from your terminal, not from inside a Python script, and the basic command is `pip install` followed by the package's name.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-06-pip-and-installing-thirdparty-packa-001-0197b56434.html"
 width="100%"
></iframe>

This downloads the `requests` package, a hugely popular tool for talking to web pages and APIs, and makes it available to `import` in any script run with that same Python installation.

## Using What You Installed

Once installed, a third-party package is imported exactly like a standard library module; Python does not distinguish between the two once the install step is done.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-06-pip-and-installing-thirdparty-packa-002-172ca6437c.html"
 width="100%"
></iframe>

The only real difference from `import math` is the invisible step that happened before this code ever ran: `requests` had to be installed first, while `math` was simply already there.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/06_pip_install_then_import.png)


## Checking What Is Installed

`pip` can also report on what is already available in your current environment.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-06-pip-and-installing-thirdparty-packa-003-192167ee3c.html"
 width="100%"
></iframe>

`pip list` prints every installed package, and `pip show requests` prints details about one specific package: its version, where it came from, and what it depends on.

## Uninstalling a Package

Removing something you no longer need follows the same pattern.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-06-pip-and-installing-thirdparty-packa-004-ca50899341.html"
 width="100%"
></iframe>

## pip Commands at a Glance

| Command | Effect |
|---|---|
| `pip install package_name` | Downloads and installs a package from PyPI |
| `pip list` | Lists every package currently installed |
| `pip show package_name` | Shows details about one installed package |
| `pip uninstall package_name` | Removes an installed package |

## A Question Worth Asking Before Installing Anything

Not every problem needs a third-party package. Before reaching for `pip install`, it is worth checking whether the standard library already covers the job, since a standard library module needs no install step, no version to manage, and no risk of going unmaintained. Reach for PyPI once you have confirmed the standard library genuinely does not cover what you need.

## Your Turn: Plan an Install

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-06-pip-and-installing-thirdparty-packa-005-0ff7a5c63c.html"
 width="100%"
></iframe>

If you have a real Python environment available, actually run `pip install requests` in your terminal, then write and run a tiny script that imports it and prints `requests.__version__` to confirm the install worked.

## Conclusion

`pip` is Python's package installer, used from the terminal to download packages published on PyPI, the public Python Package Index, with `pip install package_name` as the core command, alongside `pip list`, `pip show`, and `pip uninstall` for managing what is already there. Once installed, a third-party package imports exactly like any standard library module. Installing packages globally onto your machine works, but it quietly risks one project's needs conflicting with another's, which is exactly the problem the next lesson, on virtual environments, exists to solve.

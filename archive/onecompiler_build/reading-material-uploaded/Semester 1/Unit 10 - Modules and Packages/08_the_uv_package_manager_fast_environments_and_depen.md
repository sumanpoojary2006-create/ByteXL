## Introduction

Naveen has gotten used to the small wait every time he creates a fresh `venv` and installs a handful of packages into it: not painfully slow, but slow enough that he notices, especially when he is setting up a new laptop or starting a brand new project from scratch and has to repeat the whole ritual. A newer tool in the Python ecosystem, called **uv**, does exactly the same jobs as `venv` and `pip`, virtual environments and package installation, but built from the ground up to be dramatically faster, while staying compatible with the same project files you already understand.

This lesson covers `uv` as a modern, faster alternative to the tools from the last two lessons, not a different idea, the same idea, executed quicker.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/08_uv_speed_comparison.png)

## Installing uv Itself

`uv` is installed once on your machine, separately from any particular project, typically with a single command from its official installation instructions (which vary by operating system, so it is worth checking the current command rather than memorising one that may change).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-001-5e6ee0fabd.html"
 width="100%"
></iframe>

Once installed, `uv` is available as a command in your terminal, the same way `pip` and `python` are.

## Creating an Environment With uv

Where `venv` needed `python -m venv .venv`, `uv` does the equivalent with its own command, noticeably faster.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-002-f580553273.html"
 width="100%"
></iframe>

This creates an isolated environment in your project, exactly serving the same purpose as the `.venv` folder from the previous lesson: a private space for this project's installed packages, separate from your global Python and from any other project.

## Installing Packages With uv

`uv` provides its own install command, a faster drop-in replacement for the equivalent `pip install`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-003-96e01ab5a5.html"
 width="100%"
></iframe>

This installs `requests` into the active `uv`-managed environment, the same outcome as `pip install requests` inside an activated `venv`, just resolved and downloaded considerably faster, which becomes very noticeable once a project depends on more than a handful of packages.

## Running a Script With uv

`uv` also offers a convenient way to run a script using its managed environment directly, without a separate manual activation step.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-004-a476d7a93d.html"
 width="100%"
></iframe>

This runs `my_script.py` using the project's isolated environment, automatically, in one command.

## Managing Project Dependencies With uv

Beyond replacing individual `venv` and `pip` commands, `uv` can manage a project's entire list of dependencies for you, adding a new package and recording it in one step.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-005-616a491575.html"
 width="100%"
></iframe>

This both installs `requests` and records it as a dependency of your project, keeping that record automatically up to date as you add more packages, a job that previously needed a separate, manual step, covered properly in the next, final lesson of this unit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/08_uv_sync_lockfile.png)


## venv + pip vs uv at a Glance

| Job | venv + pip | uv |
|---|---|---|
| Create an isolated environment | `python -m venv .venv` | `uv venv` |
| Install a package | `pip install requests` (after activating) | `uv pip install requests` |
| Run a script in the environment | Activate first, then `python script.py` | `uv run script.py` |
| Add and record a dependency | A separate manual step | `uv add requests` |
| Speed | Reliable, but noticeably slower | Built specifically for speed |

## Why Learn Both

`venv` and `pip` come bundled with Python itself, work everywhere Python does, and are what you are guaranteed to find on any machine with Python installed, including ones you do not control. `uv` is a separate, additional install, faster and more convenient once it is set up, but not something you can assume is already present everywhere. Knowing both means you are never stuck, regardless of which tool a particular project, tutorial, or machine happens to expect.

## Your Turn: Plan a uv-Based Setup

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-08-the-uv-package-manager-fast-environ-006-fc190fe19d.html"
 width="100%"
></iframe>

Compare this three-line flow against the five-line `venv` and `pip` flow from the previous lesson; both reach the exact same destination, an isolated environment with `requests` available, just by a different, faster road.

## Conclusion

`uv` is a modern package and environment manager that performs the same core jobs as `venv` and `pip`, isolating a project's packages and installing what it needs, but executes them noticeably faster, and additionally offers `uv run` to execute scripts directly inside the managed environment and `uv add` to install and record a dependency in one step. Both the older standard-library approach and `uv` are worth recognising, since real projects you encounter will use either one. The final lesson of this unit covers what `uv add` was quietly already doing for you: keeping a clear, shareable record of exactly which packages a project depends on.

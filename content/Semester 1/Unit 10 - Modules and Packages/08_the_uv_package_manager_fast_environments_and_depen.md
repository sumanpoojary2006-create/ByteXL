## Introduction

The last two lessons covered two separate tools doing three separate jobs: `pip` installs packages, and `venv` creates the isolated environment that keeps one project's installed packages from colliding with another's. Both work, both ship with Python, and both are worth knowing. But using them means running several individual commands, each with its own small startup cost, every single time you set up a project.

**What uv is**: a single command-line tool, built by a company called Astral and written in Rust, that does everything `venv` and `pip` do, and also installs Python itself when needed, all from one program.

**Why uv exists**: Naveen has gotten used to the small wait every time he creates a fresh `venv` and installs a handful of packages into it, not painfully slow, but slow enough that he notices, especially when he is setting up a new laptop or starting a brand new project from scratch and has to repeat the whole ritual. `uv` exists to remove that friction. It is not a different idea from the tools in the last two lessons; it is the same three jobs, creating an isolated environment, installing packages, and managing a project's dependencies, done by one noticeably faster tool instead of several separate ones.

**Where uv is used**: anywhere you would otherwise reach for `venv` and `pip` together, from a quick throwaway script to a full multi-package project you intend to share with teammates. It has become popular on projects that install many packages, or where a team wants every developer's environment to install identically, since the speed and the exact-version locking described later in this lesson matter most at that scale.

This lesson covers `uv` as a modern, faster alternative to the tools from the last two lessons, not a different idea, the same idea, executed quicker.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/08_uv_speed_comparison.png)

## Installing uv Itself

`uv` is installed once on your machine, separately from any particular project, typically with a single command from its official installation instructions (which vary by operating system, so it is worth checking the current command rather than memorising one that may change).

```console
# Example installer command (check uv's own documentation for the current one)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once installed, `uv` is available as a command in your terminal, the same way `pip` and `python` are.

## Creating an Environment With uv

Where `venv` needed `python -m venv .venv`, `uv` does the equivalent with its own command, noticeably faster.

```console
uv venv
```

This creates an isolated environment in your project, exactly serving the same purpose as the `.venv` folder from the previous lesson: a private space for this project's installed packages, separate from your global Python and from any other project.

## Installing Packages With uv

`uv` provides its own install command, a faster drop-in replacement for the equivalent `pip install`.

```console
uv pip install requests
```

This installs `requests` into the active `uv`-managed environment, the same outcome as `pip install requests` inside an activated `venv`, just resolved and downloaded considerably faster, which becomes very noticeable once a project depends on more than a handful of packages.

## Running a Script With uv

`uv` also offers a convenient way to run a script using its managed environment directly, without a separate manual activation step.

```console
uv run my_script.py
```

This runs `my_script.py` using the project's isolated environment, automatically, in one command.

## Managing Python Versions With uv

So far, `uv` has been standing in for `venv` and `pip`, both of which assume Python itself is already installed. `uv` goes one step further and can install and manage Python versions too, so a machine with no Python at all, or the wrong version of it, is no longer a blocker.

```console
uv python install 3.12    # download and install a specific Python version
uv python list            # see every Python version uv knows about, installed or not
uv python find            # report which installed Python version uv would currently use
uv python pin 3.12        # lock this project to Python 3.12 specifically
uv python uninstall 3.10  # remove a Python version uv installed
```

`uv python pin` writes the chosen version into a small project file so that everyone working on the project, and `uv` itself, agrees on exactly which Python version this project runs against, the same way `requirements.txt` pins package versions rather than leaving them to chance.

A pinned or explicitly requested version also works per script run, without needing to repin the whole project first.

```console
uv run --python 3.12 my_script.py
```

This runs `my_script.py` under Python 3.12 specifically for that one command, useful for quickly checking whether code behaves the same on a version other than the one currently pinned.

## Managing Projects With uv

Beyond individual environment and Python-version commands, `uv` can manage an entire project, its dependencies, and their exact versions, starting from nothing.

```console
uv init hostel_tracker
```

`uv init` creates a new project folder, `hostel_tracker`, already containing a small starter `main.py` and a `pyproject.toml`, the standard Python file that records a project's name, its dependencies, and its metadata in one place.

```console
uv add requests
```

Run from inside the project, `uv add` installs `requests` into the project's environment and records it as a dependency directly inside `pyproject.toml`, keeping that record automatically up to date every time you add another package.

```console
uv remove requests
```

`uv remove` does the reverse: it uninstalls the package from the environment and deletes its entry from `pyproject.toml`, so the recorded dependency list never drifts from what is actually installed.

```console
uv lock
```

`uv lock` writes a separate file, `uv.lock`, pinning the exact resolved version of every dependency, and every dependency of those dependencies, down to the last detail. Where `pyproject.toml` says "this project needs `requests`," `uv.lock` says "and that resolved to exactly `requests==2.31.0`, with these exact supporting packages," so a teammate installing from the lock file gets a byte-for-byte identical set of packages, not just a compatible one.

```text pyproject.toml
[project]
name = "hostel-tracker"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
]
```

This is roughly what `pyproject.toml` looks like after `uv init` followed by `uv add requests`: a plain, readable text file, the same one a teammate opens to see at a glance what the project is called, which Python version it expects, and what it depends on, all without running a single command.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/08_uv_sync_lockfile.png)


## venv + pip vs uv at a Glance

| Job | venv + pip | uv |
|---|---|---|
| Create an isolated environment | `python -m venv .venv` | `uv venv` |
| Install a package | `pip install requests` (after activating) | `uv pip install requests` |
| Run a script in the environment | Activate first, then `python script.py` | `uv run script.py` |
| Add and record a dependency | A separate manual step | `uv add requests` |
| Remove a recorded dependency | A separate manual step | `uv remove requests` |
| Pin exact resolved versions | Not built in | `uv lock` |
| Manage Python versions themselves | Not built in | `uv python install / list / pin` |
| Speed | Reliable, but noticeably slower | Built specifically for speed |

## Why Learn Both

`venv` and `pip` come bundled with Python itself, work everywhere Python does, and are what you are guaranteed to find on any machine with Python installed, including ones you do not control. `uv` is a separate, additional install, faster and more convenient once it is set up, but not something you can assume is already present everywhere. Knowing both means you are never stuck, regardless of which tool a particular project, tutorial, or machine happens to expect.

## Your Turn: Plan a uv-Based Setup

```console
# Starting a brand new project, with uv installed:
uv init hostel_tracker
cd hostel_tracker
uv python pin 3.12
uv add requests
uv lock
uv run main.py
```

Compare this against the multi-step `venv` and `pip` flow from the previous lesson, where creating the folder, pinning a Python version, installing a package, and recording it were all separate, manual pieces; here, `uv` handles the project scaffold, the pinned Python version, the installed package, and its locked-down version, in five short commands.

## Conclusion

`uv` is a modern package and environment manager that performs the same core jobs as `venv` and `pip`, isolating a project's packages and installing what it needs, but executes them noticeably faster, and goes further still with `uv run` to execute scripts directly inside the managed environment, `uv python` to install and pin Python versions themselves, and `uv init`, `uv add`, `uv remove`, and `uv lock` to scaffold a project and keep its `pyproject.toml` and `uv.lock` files an exact, trustworthy record of what it depends on. Both the older standard-library approach and `uv` are worth recognising, since real projects you encounter will use either one. The final lesson of this unit builds directly on `pyproject.toml` and `uv.lock`, covering how a project, whichever tool built it, hands its exact dependency list to the next person who needs to run it.

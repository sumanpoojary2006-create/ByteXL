## Introduction

Naveen's hostel project needs version 2 of a package he installed with `pip install`. A different project he is helping a friend with, on the very same laptop, depends on version 1 of that exact same package, and upgrading it for one project quietly breaks the other. Both projects share the one Python installation on his machine, and `pip install` by default installs into that one shared place, which means every project on his laptop is fighting over the same set of package versions whether they want to or not.

The fix is to give each project its own private, isolated set of installed packages, so installing or upgrading something for one project can never affect any other. That isolated space is called a **virtual environment**, and Python's built-in tool for creating one is `venv`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/07_isolated_virtual_environments.png)

## The Problem, Concretely

```console
pip install some_library==2.0    # for the hostel project
# ... later, for the friend's project ...
pip install some_library==1.0    # downgrades it everywhere, breaking the hostel project
```

With one shared, global Python installation, there is only ever one installed version of `some_library` at a time, no matter how many separate projects are relying on it. The second install does not add a second version alongside the first; it replaces it.

## Creating a Virtual Environment

`venv`, a module included with Python itself, creates a private folder holding its own separate copy of Python and its own separate space for installed packages.

```console
python -m venv .venv
```

This creates a new folder named `.venv` inside your project, containing everything that environment needs to run independently of your system's global Python.

## Activating an Environment

Creating the environment is not enough on its own; you need to **activate** it, which tells your terminal to use that environment's Python and packages instead of the global ones, for the rest of that terminal session.

```console
# On macOS or Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

Once activated, your terminal prompt usually changes to show the environment's name, a visual reminder that you are now working inside this isolated space. Any `pip install` you run from here installs only into `.venv`, completely separate from your system's global packages, and separate from any other project's own virtual environment.

## Installing Inside an Active Environment

With the environment activated, `pip` behaves exactly as you already know, except everything it installs stays contained.

```console
pip install some_library
```

This installs into `.venv`, leaving your global Python, and every other project's own environment, entirely untouched.

## Deactivating

When you are done working on this particular project, `deactivate` returns your terminal to the global Python.

```console
deactivate
```

## One Environment Per Project

The strong convention, and the entire point of this lesson, is one virtual environment per project, never shared between unrelated projects. Naveen's hostel project gets its own `.venv`, with its own version of `some_library`, and his friend's project gets a completely separate one, with whatever version it actually needs, and the two simply never interfere with each other again.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/07_venv_project_isolation.png)


## Virtual Environments at a Glance

| Step | Command | Effect |
|---|---|---|
| Create | `python -m venv .venv` | Builds a new, isolated environment folder |
| Activate | `source .venv/bin/activate` (Mac/Linux) | Switches your terminal to use that environment |
| Install inside it | `pip install package_name` | Installs only into the active environment |
| Deactivate | `deactivate` | Returns to the global Python |

## Why .venv Usually Should Not Be Shared or Uploaded

A virtual environment folder can be large, and it is entirely reconstructable from a simple list of what was installed, which is exactly the subject of the final lesson of this unit. Project folders almost always exclude `.venv` from version control, sharing only the instructions to recreate it, rather than the environment folder itself.

## Your Turn: Plan an Isolated Setup

```console
# In your project folder:
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\activate on Windows
pip install requests
python my_script.py
deactivate
```

If you have a real terminal available, walk through these five lines yourself, noticing how your prompt changes after activation, and confirming `pip list` shows a clean, separate environment compared to your global Python.

## Conclusion

A virtual environment, created with `python -m venv .venv` and switched on with `activate`, gives each project its own private, isolated copy of installed packages, so that upgrading or installing something for one project can never silently break another sharing the same machine. The convention is one environment per project, deactivated and left behind whenever you switch contexts. Python's built-in `venv` solves this reliably; the next lesson introduces a newer, dramatically faster tool that handles the exact same job, called `uv`.

# Unit 10: Modules and Packages

**Semester 1: Python Fundamentals**

Organize, reuse, and manage code and dependencies the real-world way.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | Why Modules: Organizing and Reusing Code | [01_why_modules_organizing_and_reusing_code.md](01_why_modules_organizing_and_reusing_code.md) |
| 2 | import, from-import, and Aliases | [02_import_fromimport_and_aliases.md](02_import_fromimport_and_aliases.md) |
| 3 | Touring the Standard Library (math, random, datetime, os) | [03_touring_the_standard_library.md](03_touring_the_standard_library.md) |
| 4 | Creating Your Own Module | [04_creating_your_own_module.md](04_creating_your_own_module.md) |
| 5 | Packages and __init__.py | [05_packages_and_initpy.md](05_packages_and_initpy.md) |
| 6 | pip and Installing Third-Party Packages (PyPI) | [06_pip_and_installing_thirdparty_packages.md](06_pip_and_installing_thirdparty_packages.md) |
| 7 | Virtual Environments: Why Isolation Matters (venv) | [07_virtual_environments_why_isolation_matters.md](07_virtual_environments_why_isolation_matters.md) |
| 8 | The uv Package Manager: Fast Environments and Dependencies | [08_the_uv_package_manager_fast_environments_and_depen.md](08_the_uv_package_manager_fast_environments_and_depen.md) |
| 9 | requirements and Reproducible Setups | [09_requirements_and_reproducible_setups.md](09_requirements_and_reproducible_setups.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples and situation-based questions under natural headings, a concept-scoped illustration, and a closing **Conclusion**. Plain-English explanations are preferred; Python code is kept simple and interactive. No emojis, no em dashes.

Lessons continue Naveen's thread from Unit 8: his one bloated script splits into focused modules, gets toured through the standard library, becomes his own importable `billing.py`, groups into a `tools` package, pulls in a third-party package via pip, gets isolated per-project with venv and then uv, and finally ships with a reproducible `requirements.txt` handover.

_Status: lesson content authored for all 9 topics. Lessons 6-9 (pip, venv, uv, requirements) are primarily terminal/CLI-driven; their illustrative Python snippets were verified where runnable standalone, and shell commands were checked against correct, current syntax._

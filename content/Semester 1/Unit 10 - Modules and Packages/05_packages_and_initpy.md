## Introduction

Naveen's one `billing.py` module has been joined by `formatting.py`, `trip_planner.py`, and `raffle.py`, and his project folder now has four loose module files sitting side by side at the top level, alongside `main.py`. Four feels manageable, but he can already see where this is going: a dozen modules scattered flat in one folder is really just last lesson's "one giant file" problem, one level up. He wants to group his related modules the same way folders on a computer group related files, with `billing.py` and `formatting.py` living together inside something like a `tools` folder.

That grouping of related modules into a folder is called a **package**, and Python needs exactly one small extra file inside that folder to recognise it as one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/05_modules_grouping_into_package.png)

## A Package Is a Folder of Modules

A package is a folder containing related module files, plus one special file named `__init__.py`, which can be completely empty. Its mere presence is what tells Python "treat this folder as an importable package," rather than just an ordinary folder.

```
my_project/
    main.py
    tools/
        __init__.py
        billing.py
        formatting.py
```

`tools` is now a package, because it contains `__init__.py`. `billing.py` and `formatting.py` are modules living inside that package.

## Importing From a Package

Reaching a function inside a package's module chains the names together with dots, following the folder structure exactly.

```python file=tools/__init__.py
```

```python file=tools/billing.py
def split_cost(total, people):
    return total / people
```

```python with=tools/__init__.py,tools/billing.py
# main.py
from tools import billing

print(billing.split_cost(1200, 4))    # 300.0
```

Or reach all the way to a specific function in one line, exactly the `from ... import` form from two lessons ago, simply with a longer path in front of it.

```python with=tools/__init__.py,tools/billing.py
from tools.billing import split_cost

print(split_cost(1200, 4))    # 300.0
```

Either style works; the choice between them follows the same trade-off from the import lesson, a module-qualified name avoids any ambiguity, while a direct function import reads a little shorter.

## __init__.py Can Do More Than Sit Empty

An empty `__init__.py` is enough to make a folder a package, but it can also contain code that runs the moment the package itself is first imported, often used to make a package's most commonly used functions available directly from the package name itself, without the inner module name. Suppose Naveen bundles his cost-splitting logic into a second package, `shop`, with the function itself living in `shop/billing.py`.

```python file=shop/billing.py
def split_cost(total, people):
    return total / people
```

Instead of sitting empty, `shop/__init__.py` re-exports `split_cost` with a single line, so callers never have to name the inner `billing` module at all.

```python file=shop/__init__.py
from .billing import split_cost
```

With that one line in place, `main.py` can reach `split_cost` directly from `shop`, without separately naming `billing`.

```python with=shop/billing.py,shop/__init__.py
# main.py
from shop import split_cost

print(split_cost(1200, 4))    # 300.0
```

The leading dot in `from .billing import split_cost` means "from a module in this same package," a detail you only need inside a package's own files, never from outside it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/05_init_package_door.png)


## Why Bother With This Extra Structure?

| Without a Package | With a Package |
|---|---|
| All modules sit flat in one folder | Related modules are grouped under one clear name |
| A growing project becomes one cluttered folder | Folders mirror the natural categories of your project |
| No natural place for "the public functions of this group" | `__init__.py` can curate exactly what is meant to be used from outside |

This matters more as a project grows. A handful of scripts rarely need packages at all; a real, multi-feature project almost always benefits from grouping its modules this way.

## Packages at a Glance

| Concept | What It Is |
|---|---|
| Module | A single `.py` file |
| Package | A folder containing modules, marked with `__init__.py` |
| `__init__.py` | Can be empty, or can re-export names for shorter imports |
| Importing from a package | `from package import module` or `from package.module import name` |

## Your Turn: Picture a Package Layout

```
fest_project/
    main.py
    tools/
        __init__.py
        registration.py
        merch.py
```

```python file=tools/__init__.py
```

```python file=tools/registration.py
def is_unique(attendee_id, seen):
    return attendee_id not in seen
```

```python with=tools/__init__.py,tools/registration.py
# main.py
from tools import registration

seen_ids = {"A101"}
print(registration.is_unique("A101", seen_ids))    # False
print(registration.is_unique("A102", seen_ids))    # True
```

If you have a real project folder, build this exact structure and confirm the import works precisely as shown.

## Conclusion

A package is a folder of related modules, made importable by the presence of an `__init__.py` file, which can be empty or can re-export names to shorten how a package's contents are reached from outside it. Importing from a package chains names with dots, following the folder structure: `from package import module`, or directly to a function with `from package.module import name`. Modules organise functions within a project; packages organise modules across a growing one. The next lesson turns to code other people have already packaged for you, and how to bring it into your own project with `pip`.

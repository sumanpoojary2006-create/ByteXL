## Introduction

Naveen's one `billing.py` module has been joined by `formatting.py`, `trip_planner.py`, and `raffle.py`, and his project folder now has four loose module files sitting side by side at the top level, alongside `main.py`. Four feels manageable, but he can already see where this is going: a dozen modules scattered flat in one folder is really just last lesson's "one giant file" problem, one level up. He wants to group his related modules the same way folders on a computer group related files, with `billing.py` and `formatting.py` living together inside something like a `tools` folder.

That grouping of related modules into a folder is called a **package**, and Python needs exactly one small extra file inside that folder to recognise it as one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/05_modules_grouping_into_package.png)

## A Package Is a Folder of Modules

A package is a folder containing related module files, plus one special file named `__init__.py`, which can be completely empty. Its mere presence is what tells Python "treat this folder as an importable package," rather than just an ordinary folder.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6Im15X3Byb2plY3QvXG4gICAgbWFpbi5weVxuICAgIHRvb2xzL1xuICAgICAgICBfX2luaXRfXy5weVxuICAgICAgICBiaWxsaW5nLnB5XG4gICAgICAgIGZvcm1hdHRpbmcucHkifQ"
 width="100%"
></iframe>

`tools` is now a package, because it contains `__init__.py`. `billing.py` and `formatting.py` are modules living inside that package.

## Importing From a Package

Reaching a function inside a package's module chains the names together with dots, following the folder structure exactly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IiMgbWFpbi5weVxuZnJvbSB0b29scyBpbXBvcnQgYmlsbGluZ1xuXG5wcmludChiaWxsaW5nLnNwbGl0X2Nvc3QoMTIwMCwgNCkpICAgICMgMzAwLjAifQ"
 width="100%"
></iframe>

Or reach all the way to a specific function in one line, exactly the `from ... import` form from two lessons ago, simply with a longer path in front of it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImZyb20gdG9vbHMuYmlsbGluZyBpbXBvcnQgc3BsaXRfY29zdFxuXG5wcmludChzcGxpdF9jb3N0KDEyMDAsIDQpKSAgICAjIDMwMC4wIn0"
 width="100%"
></iframe>

Either style works; the choice between them follows the same trade-off from the import lesson, a module-qualified name avoids any ambiguity, while a direct function import reads a little shorter.

## __init__.py Can Do More Than Sit Empty

An empty `__init__.py` is enough to make a folder a package, but it can also contain code that runs the moment the package itself is first imported, often used to make a package's most commonly used functions available directly from the package name itself, without the inner module name.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IiMgdG9vbHMvX19pbml0X18ucHlcbmZyb20gLmJpbGxpbmcgaW1wb3J0IHNwbGl0X2Nvc3QifQ"
 width="100%"
></iframe>

With this written into `__init__.py`, Naveen's `main.py` can now reach `split_cost` directly from `tools`, without separately naming `billing` at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgbWFpbi5weVxuZnJvbSB0b29scyBpbXBvcnQgc3BsaXRfY29zdFxuXG5wcmludChzcGxpdF9jb3N0KDEyMDAsIDQpKSAgICAjIDMwMC4wIn0"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImZlc3RfcHJvamVjdC9cbiAgICBtYWluLnB5XG4gICAgdG9vbHMvXG4gICAgICAgIF9faW5pdF9fLnB5XG4gICAgICAgIHJlZ2lzdHJhdGlvbi5weVxuICAgICAgICBtZXJjaC5weSJ9"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3BhY2thZ2VzX2FuZF9pbml0cHkgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6IiMgdG9vbHMvcmVnaXN0cmF0aW9uLnB5XG5kZWYgaXNfdW5pcXVlKGF0dGVuZGVlX2lkLCBzZWVuKTpcbiAgICByZXR1cm4gYXR0ZW5kZWVfaWQgbm90IGluIHNlZW5cblxuIyBtYWluLnB5XG5mcm9tIHRvb2xzIGltcG9ydCByZWdpc3RyYXRpb25cblxuc2Vlbl9pZHMgPSB7XCJBMTAxXCJ9XG5wcmludChyZWdpc3RyYXRpb24uaXNfdW5pcXVlKFwiQTEwMVwiLCBzZWVuX2lkcykpICAgICMgRmFsc2VcbnByaW50KHJlZ2lzdHJhdGlvbi5pc191bmlxdWUoXCJBMTAyXCIsIHNlZW5faWRzKSkgICAgIyBUcnVlIn0"
 width="100%"
></iframe>

If you have a real project folder, build this exact structure and confirm the import works precisely as shown.

## Conclusion

A package is a folder of related modules, made importable by the presence of an `__init__.py` file, which can be empty or can re-export names to shorten how a package's contents are reached from outside it. Importing from a package chains names with dots, following the folder structure: `from package import module`, or directly to a function with `from package.module import name`. Modules organise functions within a project; packages organise modules across a growing one. The next lesson turns to code other people have already packaged for you, and how to bring it into your own project with `pip`.

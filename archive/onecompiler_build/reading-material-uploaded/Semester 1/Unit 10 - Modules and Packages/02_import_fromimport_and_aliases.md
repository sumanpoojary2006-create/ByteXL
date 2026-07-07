## Introduction

Naveen has used `import` casually for units now, typing `import random` or `import math` without ever stopping to learn the actual rules behind it. Now that he is about to split his own giant script into proper modules, the details suddenly matter: should he write `billing.split_cost(...)` every time, or can he just write `split_cost(...)` directly? What happens if two different modules both happen to define a function with the same name? And what is that `as` keyword doing in code he has seen online?

This lesson covers the three forms of `import` you will use constantly: a plain `import`, a `from ... import` that reaches directly inside a module, and an alias with `as` that gives an imported name a shorter or clearer label.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/02_three_import_styles.png)

## Plain import: Bringing in the Whole Module

A plain `import` brings in the entire module, and every name inside it must be reached through the module's own name, with a dot.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-001-8c1fab3402.html"
 width="100%"
></iframe>

Writing `math.sqrt` rather than just `sqrt` is not extra typing for no reason. It keeps every imported name clearly labeled with where it came from, which matters enormously once a script imports several modules that might otherwise define overlapping names.

## from ... import: Reaching Directly Inside

`from module import name` brings one specific name directly into your script, letting you use it without the module prefix at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-002-0d1067dbb0.html"
 width="100%"
></iframe>

This reads slightly cleaner for code that uses `sqrt` constantly, but it comes at a real cost: if two different modules both export something called `sqrt`, importing both this way creates a genuine naming collision, and whichever import ran second silently wins, with no warning at all.

## Aliasing With as: Renaming on the Way In

The `as` keyword renames an imported module or name, usually to something shorter, or to avoid a clash with a name you are already using.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-003-94419dc1b1.html"
 width="100%"
></iframe>

`as` works with `from ... import` too.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-004-9c5ce9ae62.html"
 width="100%"
></iframe>

This is purely a local convenience inside your own script; it does not change anything about the `math` module itself, only the name you have chosen to refer to it by from this point onward.

## Why Real Code Often Prefers the Plain Form

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-005-afefebb2bd.html"
 width="100%"
></iframe>

If both `billing.py` and `receipts.py` happen to define a function called `format`, the plain `import billing` and `import receipts` keep both perfectly usable side by side, because the module name in front of the dot always disambiguates which one you mean. `from billing import format` followed by `from receipts import format` would have the second import silently overwrite the first, an easy, hard-to-notice mistake in a larger project.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/02_namespace_import_styles.png)


## Import Styles at a Glance

| Style | Syntax | Usage After Importing | Risk |
|---|---|---|---|
| Plain import | `import math` | `math.sqrt(16)` | None; always unambiguous |
| from-import | `from math import sqrt` | `sqrt(16)` | Can silently clash with another `sqrt` |
| Aliased import | `import math as m` | `m.sqrt(16)` | None; just a chosen shorter name |
| Aliased from-import | `from math import sqrt as square_root` | `square_root(16)` | Same clash risk as plain from-import, renamed away |

## Your Turn: Try All Three Styles

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-02-import-fromimport-and-aliases-006-d16821f82b.html"
 width="100%"
></iframe>

Run this a few times and notice the random results change each time, while the import style itself never affects what `random` actually does, only how you refer to it afterward.

## Conclusion

A plain `import module` keeps every name safely behind a `module.` prefix, `from module import name` reaches a name directly but risks a silent clash with another import of the same name, and `as` renames whatever you import, for brevity or to dodge a collision. Reach for the plain form by default in anything beyond a quick script, and reserve `from ... import` for names you are certain are safe and used constantly. With the syntax settled, the next lesson tours a handful of standard library modules genuinely worth knowing well.

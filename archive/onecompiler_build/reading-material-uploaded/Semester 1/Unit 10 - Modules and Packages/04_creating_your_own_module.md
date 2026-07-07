## Introduction

Naveen is finally ready to do what the first lesson of this unit only previewed: actually pull his bill-splitting functions out of his giant script and into their own proper module, then import them from somewhere else. There is no special command to "create a module." There is no new syntax at all, in fact. The entire trick is simply saving a `.py` file in the right place and importing it by its filename, without the `.py` extension.

This lesson walks through that, file by file, exactly the way Naveen would do it on his own laptop.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/04_two_files_same_folder.png)

## Step One: Write the Module File

Naveen creates a new file named `billing.py`, in the same folder as his main script, containing only the functions that belong together.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-04-creating-your-own-module-001-64a5a39efb.html"
 width="100%"
></iframe>

This file does nothing on its own when it is run directly; it simply defines two functions and stops. That is exactly the point. A module's job is to be imported, not to be the main script itself.

## Step Two: Import It From Another File

In a second file, `main.py`, saved in that very same folder, Naveen imports `billing` exactly the way he would import `math` or `random`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-04-creating-your-own-module-002-3fab051308.html"
 width="100%"
></iframe>

Notice the module name used in `import billing` is just `billing`, the filename with the `.py` removed, and every function inside it is reached through `billing.` exactly as `math.sqrt` reached a function inside `math`.

## The Folder Layout That Makes This Work

```
my_project/
    billing.py
    main.py
```

Python looks for a module being imported in the same folder as the script doing the importing, among a few other places. As long as `billing.py` and `main.py` sit side by side like this, `import billing` inside `main.py` finds it without any extra configuration.

## A Module Can Be Run Directly, Too

Because a module is just a `.py` file, nothing stops you from running it on its own as well, separately from importing it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-04-creating-your-own-module-003-2742df7f7c.html"
 width="100%"
></iframe>

The catch is that this `print` line would also run every single time `billing` is imported from anywhere else, which is rarely what you actually want from a module meant to be reused quietly. The next lesson on packages, and good practice generally, favours keeping a module's top level limited to definitions, saving any "run this directly" code for the script that does the importing.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/04_name_main_guard.png)


## Naming Your Module File

A module's name follows the exact same snake_case convention as a variable or function: lower case words, separated by underscores, descriptive of what it contains. `billing.py`, `trip_planner.py`, and `receipt_formatter.py` are all reasonable; a module named `stuff.py` documents nothing about what it actually holds.

## Creating a Module at a Glance

| Step | What Happens |
|---|---|
| Save functions in a `.py` file | That file is now a module, automatically |
| Place it beside the importing script | Python can find it with a plain `import module_name` |
| Import it | `import billing` |
| Use its contents | `billing.function_name(...)`, exactly like `math.sqrt` |

## Your Turn: Picture Your Own Module

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-04-creating-your-own-module-004-54e9754e71.html"
 width="100%"
></iframe>

If you have a real project folder to try this in, save the two halves as two actual files exactly as commented above, and run `main.py` to see the import work for real.

## Conclusion

Creating your own module takes no special syntax at all: save a `.py` file containing functions (or other definitions), place it in the same folder as the script that needs it, and import it by its filename, without the `.py` extension, exactly the way you import any standard library module. Keep a module's top level limited mostly to definitions, since any other code runs every time the module is imported, not just when you intend it to. With one module under control, the next lesson covers organising several related modules together into a single package.

## Introduction

Meera is putting together a price list to post for her handmade shop, but the numbers will not sit still: one price crowds right up against its item name, another trails off at a different distance, and one shows three decimal places where it should show two. She reworks it so every item name lines up on the left and every price sits in a neat column on the right, each rounded to exactly two decimals, and the list suddenly looks like a proper menu instead of a jumble. Back in the data-types unit you met f-strings as a clean way to drop variables into text, but they can do much more than that. With a little extra notation, an f-string can round a number to two decimals, line figures up into neat columns, and turn raw values into output that looks like a real report rather than a jumble. This lesson takes the f-string from useful to genuinely polished. None of the methods from earlier lessons can line up a column of prices on their own; formatting is the missing piece that turns correct numbers into a readable list.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/07_formatting_aligned_table.png)

## A Quick Recap

An f-string is a string with the letter `f` before the opening quote, and anything inside curly braces is replaced by its value.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-001-1289d69fc5.html"
 width="100%"
></iframe>

That much you know. The new idea is that you can add a formatting instruction after a colon inside the braces, to control exactly how a value appears.

## Formatting Numbers

The most common need is controlling decimal places, especially for money. A colon followed by `.2f` means "show this as a number with two decimal places".

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-002-eacbfadc24.html"
 width="100%"
></iframe>

You can also add a comma to group thousands, which makes large numbers readable, and use a percent sign for proportions:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-003-6ed40cb47f.html"
 width="100%"
></iframe>

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/07_format_specifier_dashboard.png)


## Lining Things Up Into Columns

Here is where output starts to look professional. You can set a minimum width and an alignment, so values form tidy columns. A number after the colon sets the width, while `<`, `>`, and `^` mean left, right, and centre.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-004-97e61ac4a1.html"
 width="100%"
></iframe>

This prints a small aligned table, with item names pushed to the left in a 10-wide column and prices pushed to the right in an 8-wide column, so the numbers line up cleanly underneath each other. This is exactly the transformation that turned Meera's crowded, uneven price list into something that reads like a proper menu.

## You May See Older Styles

In other people's code you might meet two older ways of formatting, the `.format()` method and the `%` operator. They still work, but f-strings are newer, faster, and far easier to read, so they are the recommended choice today. It is enough to recognise the old styles when you see them and to reach for f-strings yourself.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-005-050f729547.html"
 width="100%"
></iframe>

All three lines print the exact same sentence, which is exactly the point: the underlying idea, dropping a value into a template, never changed, only the syntax did, and f-strings simply won out as the clearest way to write it.

## Format Specifiers at a Glance

| Specifier | Effect | Example |
|---|---|---|
| `:.2f` | Two decimal places | `f"{49.5:.2f}"` is `"49.50"` |
| `:,` | Comma as a thousands separator | `f"{1000000:,}"` is `"1,000,000"` |
| `:.1%` | Shown as a percentage | `f"{0.873:.1%}"` is `"87.3%"` |
| `:<10` | Left-aligned, minimum width 10 | Pads with spaces on the right |
| `:>10` | Right-aligned, minimum width 10 | Pads with spaces on the left |
| `:^10` | Centred, minimum width 10 | Pads with spaces on both sides |

## Your Turn: A Small Price List

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-07-string-formatting-and-fstrings-006-1c4cb65539.html"
 width="100%"
></iframe>

Enter a couple of items and notice how the names align on the left and the prices align on the right with two decimals, no matter how long or short each entry is. That alignment is what separates a rough printout from a readable report.

## Conclusion

An f-string can do far more than insert a value: a colon followed by a format specifier controls the output, with `.2f` for decimals, `,` for thousands separators, `%` for percentages, and a width plus `<`, `>`, or `^` for alignment into columns. These tools turn raw numbers into clean, professional output. Prefer f-strings over the older `.format()` and `%` styles, and your programs will not only compute correctly but also present their results clearly. Formatting controls how a finished value appears on screen; the next lesson controls something a level deeper, the raw line breaks and quote marks inside the text itself.

## Introduction

The fest runs for two days, and Tara has a clean set of unique attendee IDs for each one. Now the questions get more interesting. How many people came on both days? How many came only on day one, and never showed up again? How many distinct people attended across the whole fest, counted just once each even if they came twice? Scanning through two separate lists by eye to answer these would be slow and error-prone.

Sets answer all three questions in a single line each, because comparing sets is something Python builds in directly. These comparisons are called **set operations**, and they read almost exactly like the questions Tara is actually asking.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/02_two_day_attendee_overlap.png)

## Union: Everyone, Counted Once

The union of two sets combines them into one, with every value appearing only once even if it was in both.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-02-set-operations-001-4e9217d5fd.html"
 width="100%"
></iframe>

The `|` operator reads as "or": a value belongs to the union if it was in day1, or day2, or both. The same result comes from `day1.union(day2)`, written as a method instead of a symbol; both forms are common, and it is worth recognising either. As with any set, do not expect the printed order to match the order shown here exactly.

## Intersection: Only the Overlap

The intersection keeps only the values present in both sets, exactly answering "who came on both days."

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-02-set-operations-002-d70c79608b.html"
 width="100%"
></iframe>

The `&` operator reads as "and." Only A103 and A104 appear in both `day1` and `day2`, so only those two survive. `day1.intersection(day2)` does the same thing.

## Difference: In One, Not the Other

The difference keeps values that are in the first set but not the second, and order matters here, unlike with union and intersection.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-02-set-operations-003-9b6341e3d7.html"
 width="100%"
></iframe>

`day1 - day2` answers "who came on day one and never returned", while `day2 - day1` answers the opposite question, "who only showed up on day two." Swapping the order swaps the answer entirely, so always read a difference as "this set, minus whatever the other set already covers."

## Symmetric Difference: In Exactly One, Not Both

Sometimes you want everyone who attended exactly one day, excluding the people who came to both. That is the symmetric difference.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-02-set-operations-004-18b5993004.html"
 width="100%"
></iframe>

The `^` operator keeps values that are in either set but not in both at once, which is the union minus the intersection in one step.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/02_set_operation_outputs.png)


## Set Operations at a Glance

| Operation | Symbol | Method | Meaning |
|---|---|---|---|
| Union | `\|` | `.union()` | In either set, counted once |
| Intersection | `&` | `.intersection()` | In both sets |
| Difference | `-` | `.difference()` | In the first set, not the second |
| Symmetric difference | `^` | `.symmetric_difference()` | In exactly one set, not both |

## Your Turn: Compare Two Days

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-02-set-operations-005-c25edb151b.html"
 width="100%"
></iframe>

Enter two overlapping lists of IDs and watch all four questions answered instantly from the same two sets, no manual comparison required.

## Conclusion

Sets compare cleanly with `|` for union, `&` for intersection, `-` for difference, and `^` for symmetric difference, turning questions like "who attended both, either, or only one" into single, readable lines. Sets are excellent at tracking who or what is present, but they cannot attach extra information to each value, such as a price or a score. For that, you need a structure that pairs every value with something else, which is exactly what the next lesson, dictionaries, introduces.

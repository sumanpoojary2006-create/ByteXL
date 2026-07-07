## Introduction

Tara is on gate duty for the college fest, scanning each attendee's wristband as they walk in. The scanner logs an ID every single time it beeps, and people being people, a few wander out for a smoke and scan back in, while one nervous fresher scans the same wristband three times just to be sure it worked. By the end of the day Tara does not want a log of every beep. She wants to know one thing: how many different people actually came in.

A list would dutifully keep every duplicate beep, because a list remembers everything exactly as it happened. What Tara actually needs is a collection that automatically throws away repeats and only ever keeps one copy of each value. That is exactly what Python's **set** is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/01_unique_attendee_scans.png)

## Creating a Set

A set is written with curly braces, holding values separated by commas, just like a list but with no guaranteed order.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-001-79ad34767d.html"
 width="100%"
></iframe>

Notice the duplicates vanish on their own. Python keeps only one copy of each value, automatically, with no extra code from Tara at all. The order shown when you print a set is not the order you typed it in, and it is not guaranteed to stay the same between runs, because a set does not track position the way a list does. Run the line above yourself and you may well see the same three IDs printed in a different order, which is expected, not a mistake.

## An Empty Set Needs set(), Not { }

Be careful with empty sets. Curly braces with nothing inside, `{}`, create an empty dictionary, not an empty set, because dictionaries (which you will meet in a later lesson) also use curly braces. To make a genuinely empty set, call `set()` directly.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-002-4e256b1ccb.html"
 width="100%"
></iframe>

## No Indexing, Because There Is No Order

Try to reach into a set with a position, the way you would a list, and Python refuses.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-003-d58fbb0e0b.html"
 width="100%"
></iframe>

This raises a `TypeError`, because a set has no first item, no last item, no position 0. It only has membership: a value is either in the set, or it is not. That single idea, membership rather than position, is the whole point of a set.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/01_set_no_duplicates_unordered.png)


## Checking Membership: in

Asking "is this value already in here" is instant and natural with a set, using the `in` operator you already know from lists and strings.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-004-328ce16c2d.html"
 width="100%"
></iframe>

This is the exact check Tara's scanner runs silently every time a wristband beeps: has this ID already been logged today, or is it a genuinely new attendee? Checking membership in a set is also typically much faster than checking membership in a long list, because Python organises a set internally for quick lookups rather than scanning item by item.

## Building a Set From a List

A common, practical move is turning an existing list, duplicates and all, into a set, instantly deduplicating it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-005-fe73e13d3a.html"
 width="100%"
></iframe>

This one line is exactly how Tara turns a noisy log of every beep into the one number she actually needs: the count of distinct people who walked through the gate.

## Sets at a Glance

| Feature | List | Set |
|---|---|---|
| Brackets | `[ ]` | `{ }` or `set()` |
| Duplicate values | Kept | Automatically removed |
| Order | Preserved | Not guaranteed |
| Indexing with `[0]` | Yes | No |
| Fast membership check with `in` | Slower on long lists | Fast |

## Your Turn: Deduplicate a Scan Log

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-01-sets-uniqueness-and-creation-006-c9d310d0e0.html"
 width="100%"
></iframe>

Enter the same ID more than once on purpose and watch the unique count refuse to budge, no matter how many times that one ID is scanned.

## Conclusion

A set is an unordered collection of unique values, written in curly braces, that automatically drops duplicates and offers fast membership checks with `in`, but gives up indexing and positional order entirely. Converting a list to a set with `set(some_list)` is the quickest way to deduplicate real data. Knowing whether one value is in a set is useful on its own, but the real power appears once you start comparing two sets against each other, which is exactly where the next lesson goes.

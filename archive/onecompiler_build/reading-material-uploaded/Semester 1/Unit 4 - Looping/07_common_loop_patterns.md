## Introduction

After the class fest, Kabir sits down with the sign-up sheet and notices that every little task he needs to do is really the same handful of moves wearing a different label. He counts how many classmates actually showed up. He adds up the total money collected. He finds the single highest scorer in the games. He searches the list for one particular name. Different questions, the same few moves repeated.

Once you have written a handful of loops, you start to notice that the same few shapes keep returning: counting how many things match, adding values up, finding the largest or smallest, searching for a particular item. These are the common loop patterns, and they are worth learning by name, because almost every loop problem you meet is one of them, or a small combination of them. Kabir did not invent four separate strategies for his sign-up sheet; he reused the same handful of moves on four different questions, which is precisely the habit this lesson wants to build in you. Recognise the pattern and the code almost writes itself.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5ngqj/07_count_and_sum_sheet.png)
## The Counting Pattern

To count how many items meet a condition, set a counter to zero before the loop and add one each time the condition is true.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-4-looping-07-common-loop-patterns-001-ee24c3e899.html"
 width="100%"
></iframe>

The counter starts at 0 and rises only for even numbers, ending at 3. You used this exact shape to count vowels earlier; the pattern is the same whatever you are counting.

## The Sum and Average Pattern

To total a group of numbers, keep a running sum that starts at zero and grows on each pass. An average is simply that sum divided by how many numbers there were.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-4-looping-07-common-loop-patterns-002-ddde1a915d.html"
 width="100%"
></iframe>

The `total` accumulates to 100, and dividing by the count gives the average of 25. Notice `len()` tells you how many items the list holds, saving you from counting them yourself.

## The Min and Max Pattern

To find the largest or smallest value, hold a "best so far" and update it whenever you meet something better. This is the highest-marks idea from earlier units, now a named pattern.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-4-looping-07-common-loop-patterns-003-2feb2e69e5.html"
 width="100%"
></iframe>

Start by assuming the first item is the largest, then let any bigger value take its place. By the end, `largest` holds the true maximum, here 88. It is the exact same "best so far" habit Kabir used to find the top scorer on his sign-up sheet, just renamed into code.

## The Search Pattern

To find whether something exists, loop and stop early with `break` when you find it, using a flag to remember the result.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-4-looping-07-common-loop-patterns-004-b15ed65fe6.html"
 width="100%"
></iframe>

The flag `found` starts false and flips to true only if the target appears. The `break` stops the search the moment it succeeds.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5ngqj/07_max_and_search_flag.png)

## The Four Patterns at a Glance

| Pattern | Starting Value | What Happens Each Pass | Example Result |
|---|---|---|---|
| Count | `0` | Add 1 when the condition is true | Number of even values |
| Sum / Average | `0` | Add the value | Total, then total divided by count |
| Min / Max | First item | Replace if a better value appears | The largest value seen |
| Search | `False` flag | Flip to `True` and `break` on a match | Found or not found |

## Your Turn: Average of Entered Numbers

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-4-looping-07-common-loop-patterns-005-b576cacf93.html"
 width="100%"
></iframe>

This combines patterns: a sentinel loop to gather numbers, a running sum, a count, and a guard against dividing by zero. Enter a few numbers and then "done" to see the average. Real programs are often just these simple patterns stitched together.

## Conclusion

Most loops are one of a few familiar patterns: counting matches, summing values, tracking a running minimum or maximum, and searching with a flag and a `break`. Each has a simple skeleton, set up a variable before the loop and update it inside. Learn to recognise which pattern a problem needs, and writing the loop becomes a matter of filling in a shape you already know, rather than inventing logic from scratch. The last lesson of this unit turns to the two mistakes most likely to trip you up while writing any of these patterns for the first time.

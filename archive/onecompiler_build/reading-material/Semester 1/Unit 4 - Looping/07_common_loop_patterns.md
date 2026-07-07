## Introduction

After the class fest, Kabir sits down with the sign-up sheet and notices that every little task he needs to do is really the same handful of moves wearing a different label. He counts how many classmates actually showed up. He adds up the total money collected. He finds the single highest scorer in the games. He searches the list for one particular name. Different questions, the same few moves repeated.

Once you have written a handful of loops, you start to notice that the same few shapes keep returning: counting how many things match, adding values up, finding the largest or smallest, searching for a particular item. These are the common loop patterns, and they are worth learning by name, because almost every loop problem you meet is one of them, or a small combination of them. Kabir did not invent four separate strategies for his sign-up sheet; he reused the same handful of moves on four different questions, which is precisely the habit this lesson wants to build in you. Recognise the pattern and the code almost writes itself.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5ngqj/07_count_and_sum_sheet.png)
## The Counting Pattern

To count how many items meet a condition, set a counter to zero before the loop and add one each time the condition is true.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NvbW1vbl9sb29wX3BhdHRlcm5zIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJudW1iZXJzID0gWzQsIDksIDIsIDcsIDYsIDFdXG5ldmVucyA9IDBcbmZvciBuIGluIG51bWJlcnM6XG4gICAgaWYgbiAlIDIgPT0gMDpcbiAgICAgICAgZXZlbnMgPSBldmVucyArIDFcbnByaW50KFwiRXZlbiBudW1iZXJzOlwiLCBldmVucykifQ"
 width="100%"
></iframe>

The counter starts at 0 and rises only for even numbers, ending at 3. You used this exact shape to count vowels earlier; the pattern is the same whatever you are counting.

## The Sum and Average Pattern

To total a group of numbers, keep a running sum that starts at zero and grows on each pass. An average is simply that sum divided by how many numbers there were.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NvbW1vbl9sb29wX3BhdHRlcm5zIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJudW1iZXJzID0gWzEwLCAyMCwgMzAsIDQwXVxudG90YWwgPSAwXG5mb3IgbiBpbiBudW1iZXJzOlxuICAgIHRvdGFsID0gdG90YWwgKyBuXG5wcmludChcIlN1bTpcIiwgdG90YWwpXG5wcmludChcIkF2ZXJhZ2U6XCIsIHRvdGFsIC8gbGVuKG51bWJlcnMpKSJ9"
 width="100%"
></iframe>

The `total` accumulates to 100, and dividing by the count gives the average of 25. Notice `len()` tells you how many items the list holds, saving you from counting them yourself.

## The Min and Max Pattern

To find the largest or smallest value, hold a "best so far" and update it whenever you meet something better. This is the highest-marks idea from earlier units, now a named pattern.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NvbW1vbl9sb29wX3BhdHRlcm5zIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJudW1iZXJzID0gWzQyLCAxNywgODgsIDIzXVxubGFyZ2VzdCA9IG51bWJlcnNbMF1cbmZvciBuIGluIG51bWJlcnM6XG4gICAgaWYgbiA-IGxhcmdlc3Q6XG4gICAgICAgIGxhcmdlc3QgPSBuXG5wcmludChcIkxhcmdlc3Q6XCIsIGxhcmdlc3QpIn0"
 width="100%"
></iframe>

Start by assuming the first item is the largest, then let any bigger value take its place. By the end, `largest` holds the true maximum, here 88. It is the exact same "best so far" habit Kabir used to find the top scorer on his sign-up sheet, just renamed into code.

## The Search Pattern

To find whether something exists, loop and stop early with `break` when you find it, using a flag to remember the result.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NvbW1vbl9sb29wX3BhdHRlcm5zIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJudW1iZXJzID0gWzMsIDgsIDUsIDldXG50YXJnZXQgPSA1XG5mb3VuZCA9IEZhbHNlXG5mb3IgbiBpbiBudW1iZXJzOlxuICAgIGlmIG4gPT0gdGFyZ2V0OlxuICAgICAgICBmb3VuZCA9IFRydWVcbiAgICAgICAgYnJlYWtcbnByaW50KFwiRm91bmQhXCIgaWYgZm91bmQgZWxzZSBcIk5vdCBmb3VuZC5cIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NvbW1vbl9sb29wX3BhdHRlcm5zIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJ0b3RhbCA9IDBcbmNvdW50ID0gMFxud2hpbGUgVHJ1ZTpcbiAgICBlbnRyeSA9IGlucHV0KFwiRW50ZXIgYSBudW1iZXIgKG9yICdkb25lJyk6IFwiKVxuICAgIGlmIGVudHJ5ID09IFwiZG9uZVwiOlxuICAgICAgICBicmVha1xuICAgIHRvdGFsID0gdG90YWwgKyBpbnQoZW50cnkpXG4gICAgY291bnQgPSBjb3VudCArIDFcblxuaWYgY291bnQgPiAwOlxuICAgIHByaW50KFwiQXZlcmFnZTpcIiwgdG90YWwgLyBjb3VudClcbmVsc2U6XG4gICAgcHJpbnQoXCJObyBudW1iZXJzIGVudGVyZWQuXCIpIn0"
 width="100%"
></iframe>

This combines patterns: a sentinel loop to gather numbers, a running sum, a count, and a guard against dividing by zero. Enter a few numbers and then "done" to see the average. Real programs are often just these simple patterns stitched together.

## Conclusion

Most loops are one of a few familiar patterns: counting matches, summing values, tracking a running minimum or maximum, and searching with a flag and a `break`. Each has a simple skeleton, set up a variable before the loop and update it inside. Learn to recognise which pattern a problem needs, and writing the loop becomes a matter of filling in a shape you already know, rather than inventing logic from scratch. The last lesson of this unit turns to the two mistakes most likely to trip you up while writing any of these patterns for the first time.

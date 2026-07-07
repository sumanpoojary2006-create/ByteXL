## Introduction

Kabir is at the hostel gym working through his daily set of ten push-ups, counting each one under his breath: one, two, three. This time there is no guessing and no waiting for a signal. He knows the exact count before he even starts, so he just works through them in order and stops cleanly the moment he hits the last one.

That is the situation a `while` loop is clumsy for and a different tool handles cleanly. A `while` loop would technically work for ten push-ups too, but it would force Kabir's program to manage its own counter and remember to update it, extra bookkeeping for a job where the count was never really in doubt. Very often you know the repetitions in advance: print each of the 12 months, repeat a calculation 10 times, step through the numbers 1 to 100. For these counted repetitions, the `for` loop is cleaner and safer, because the counting is handled for you. Its constant companion is `range()`, a tool that produces sequences of numbers to loop over.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5kfd6/03_for_range_stepping_stones.png)
## The for Loop

A `for` loop takes each value from a sequence, one at a time, and runs its block with that value.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zvcl9sb29wc19hbmRfcmFuZ2UgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImZvciBudW1iZXIgaW4gcmFuZ2UoNSk6XG4gICAgcHJpbnQobnVtYmVyKSJ9"
 width="100%"
></iframe>

This prints 0, 1, 2, 3, 4. The variable `number` automatically takes the next value on each pass, and the loop ends when the sequence runs out. There is no counter to set up and no condition to update by hand, which means there is no way to accidentally forget the step and loop forever. The `for` loop does the bookkeeping for you.

## Understanding range()

The `range()` function generates a sequence of numbers, and it comes in three forms.

## range() Forms at a Glance

| Form | Produces | Example |
|---|---|---|
| `range(stop)` | 0 up to, but not including, stop | `range(5)` gives 0, 1, 2, 3, 4 |
| `range(start, stop)` | start up to, but not including, stop | `range(1, 6)` gives 1, 2, 3, 4, 5 |
| `range(start, stop, step)` | start up to stop, counting in jumps | `range(0, 10, 2)` gives 0, 2, 4, 6, 8 |

The detail that surprises everyone at first is that the stop value is never included. This is why `range(1, 6)` stops at 5, not 6. Keep that in mind and a whole category of "one too few" or "one too many" bugs simply disappears, the same kind of miscount that would leave Kabir stopping his push-ups one rep short without ever noticing why.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5kfd6/03_range_start_stop_step.png)


## for or while: Which One?

So how do you choose? Reach for a `for` loop when you know the number of repetitions or you want to visit every item in a sequence, which is most of the time. Reach for a `while` loop when you must keep going until a condition changes and the count is unknown, such as re-asking for input. When either could work, the `for` loop is usually safer, because it cannot become infinite.

## Your Turn: A Multiplication Table

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zvcl9sb29wc19hbmRfcmFuZ2UgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Im51bWJlciA9IGludChpbnB1dChcIlNob3cgdGhlIHRhYmxlIG9mOiBcIikpXG5mb3IgaSBpbiByYW5nZSgxLCAxMSk6XG4gICAgcHJpbnQoZlwie251bWJlcn0geCB7aX0gPSB7bnVtYmVyICogaX1cIikifQ"
 width="100%"
></iframe>

Enter 7 and watch the full table from 7 x 1 to 7 x 10 print in ten neat lines. The `range(1, 11)` gives the numbers 1 through 10, and the loop variable `i` steps through each one. You wrote the multiply-and-print instruction once, and the loop produced the whole table.

## Conclusion

A `for` loop runs its block once for each value in a sequence, making it the natural choice for counted repetition and for visiting every item. Its partner `range()` builds number sequences in three forms, start, stop, and step, and always stops just before the stop value. Because the loop handles the counting itself, it is both cleaner and safer than a hand-managed `while`. When you know how many times, or you have a sequence to walk through, `for` is the tool. So far every `for` loop has stepped through numbers; the next lesson shows it stepping through names and letters just as naturally.

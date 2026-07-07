## Introduction

Kabir is back in his hostel room trying to get onto the wifi, typing the password in again and again. Wrong, try again. Wrong, try again. He has no idea how many attempts it will take, maybe the next one, maybe the tenth, so he just keeps going, watching the little wifi icon, ready to stop the instant it connects. There is no fixed count to plan around here, only a condition to keep checking.

That is exactly the shape of plenty of real tasks: you keep asking for a password until the user gets it right, a game keeps running until the player chooses to quit, you keep adding items to a cart until the customer is done. In all of these, you cannot say in advance how many times to loop; you only know the condition that should keep it going. Kabir does not know if the wifi will connect on attempt two or attempt twelve, and a program in his position would face the same uncertainty. This is exactly what the `while` loop is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5k4ef/02_while_until_correct.png)
## Repeat While a Condition Holds

A `while` loop checks a condition before each pass. As long as the condition is true, it runs its block again. The moment the condition becomes false, the loop stops.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3doaWxlX2xvb3BzX2NvdW50ZXJzX2FuZF9zZW50aW5lbHMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNvdW50ID0gMVxud2hpbGUgY291bnQgPD0gNTpcbiAgICBwcmludChjb3VudClcbiAgICBjb3VudCA9IGNvdW50ICsgMSJ9"
 width="100%"
></iframe>

Read it as "while count is 5 or less, print it and then increase it." The loop prints 1 through 5 and then stops, because `count` has reached 6 and the condition is finally false. Like every block in Python, the condition line ends with a colon and the repeated lines are indented.

## The Counter Pattern

That example shows the most common shape of a `while` loop, the counter pattern, which has three essential parts: set up a counter before the loop, test it in the condition, and update it inside the loop.

Miss that last part and you have a problem. What do you think happens if you forget the line `count = count + 1`?

The counter stays at 1 forever, the condition `count <= 5` is always true, and the loop never stops. This is called an infinite loop, and it is the classic `while` loop mistake. You will study how to avoid it carefully in a later lesson; for now, remember the rule: something inside the loop must move you closer to the condition becoming false, the way each wifi attempt at least brings Kabir one try closer to either the right password or giving up and asking the warden for it.

## The Sentinel Pattern

The other common shape does not count at all. Instead it repeats until a special signal value, called a sentinel, tells it to stop. This is perfect for "keep going until the user is done."

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3doaWxlX2xvb3BzX2NvdW50ZXJzX2FuZF9zZW50aW5lbHMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNvbW1hbmQgPSBcIlwiXG53aGlsZSBjb21tYW5kICE9IFwicXVpdFwiOlxuICAgIGNvbW1hbmQgPSBpbnB1dChcIlR5cGUgYSBjb21tYW5kIChvciAncXVpdCcgdG8gc3RvcCk6IFwiKVxuICAgIHByaW50KFwiWW91IHR5cGVkOlwiLCBjb21tYW5kKVxucHJpbnQoXCJHb29kYnllIVwiKSJ9"
 width="100%"
></iframe>

The loop keeps reading commands and only stops when the user types "quit". Notice this is exactly the kind of "keep asking" behaviour that simple conditions could not do in the last unit. The loop is what finally lets a program insist on what it needs.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5k4ef/02_sentinel_quit_signal.png)

## Counter vs Sentinel at a Glance

| Pattern | Stops When | Example |
|---|---|---|
| Counter | A counter reaches a target value | Print 1 through 5 |
| Sentinel | A special signal value appears | Keep going until the user types "quit" |

## Your Turn: Ask Until Correct

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3doaWxlX2xvb3BzX2NvdW50ZXJzX2FuZF9zZW50aW5lbHMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InBhc3N3b3JkID0gXCJcIlxud2hpbGUgcGFzc3dvcmQgIT0gXCJvcGVuMTIzXCI6XG4gICAgcGFzc3dvcmQgPSBpbnB1dChcIkVudGVyIHRoZSBwYXNzd29yZDogXCIpXG5wcmludChcIkFjY2VzcyBncmFudGVkIVwiKSJ9"
 width="100%"
></iframe>

Run it and type a few wrong passwords. The loop refuses to move on until you enter "open123", then it lets you through. This re-asking pattern, impossible with conditions alone, is one of the most practical uses of a `while` loop.

## Conclusion

A `while` loop repeats its block as long as a condition stays true, which makes it the right choice when you do not know the number of repetitions in advance. Use the counter pattern when you are stepping toward a limit, always updating the counter inside the loop so it can eventually stop, and use the sentinel pattern when you want to repeat until a special value appears. Above all, make sure each pass moves you closer to ending, or the loop will run forever. Not every repeated task is this open-ended, though, and Kabir's next chore, a fixed set of gym reps, shows the cleaner tool for when the count really is known up front.

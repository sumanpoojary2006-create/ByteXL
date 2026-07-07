## Introduction

Give two students the same assignment, "write a program that tells a student whether they passed," and watch what happens in the first thirty seconds.

The first student's fingers hit the keyboard immediately. They type a bit, get confused, delete it, try again, and twenty minutes later they are surrounded by half finished work and rising frustration. The second student does something that looks almost lazy: they sit back, stare at the ceiling, and think. They jot a few notes on paper. Then, calmly, they solve the whole thing in one clean pass.

The difference between them is not talent or typing speed. It is that the second student had a **plan** before they had a single instruction. And here is the uncomfortable truth this lesson is built on: most bugs are not coding errors at all. They are thinking errors that a few minutes of planning would have caught.

## The Question Most Beginners Skip

So what was the second student actually doing while staring at the ceiling? They were asking four quiet questions before touching the keyboard:

- What do I have? (the inputs) Three subject marks.
- What do I want? (the output) The word "Pass" or "Fail".
- What is the rule? (the logic) An average of 40 or more means pass.
- What are the steps? Read the marks, find the average, compare it to 40, show the result.

In about two minutes the entire solution existed, on paper, in plain language. Building it then became the easy part, because it was just following a plan that already worked.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t2hgunm/04_two_students_plan_vs_dive_in.png)

The principle is short enough to memorise: **understand first, plan second, build third.**

## A Four-Stage Rhythm You Can Trust

This is not a trick. It is a method as old as problem solving itself, often credited to the mathematician George Polya, and it moves through four stages in order.

| Stage | What You Do | Pass/Fail Example |
|---|---|---|
| 1. Understand | Restate the problem in your own words; pin down the inputs, outputs, and rules | Three marks in, "Pass" or "Fail" out, the rule is average of 40 or more |
| 2. Plan | Outline the steps; think through examples and tricky cases | Read marks, find average, compare to 40, show result |
| 3. Carry Out | Turn each planned step into instructions, one at a time | Only this stage touches the keyboard |
| 4. Look Back | Test the result, especially with unusual inputs, and improve it | Check marks of exactly 40, or all zeros |

Stages one and two happen in your head and on paper. Only stage three touches the keyboard. If you cannot explain your plan in plain language, the problem is not yet understood, and that is your signal to return to stage one rather than type harder.

## Writing the Plan in Plain Words

For the pass or fail task, the finished plan looks like this, with no programming required:

1. Read the three subject marks.
2. Add them and divide by three to get the average.
3. If the average is 40 or more, the result is "Pass". Otherwise it is "Fail".
4. Show the result.

That is a complete, testable solution expressed entirely in English. When you finally learn the Python for it later in this unit, you will simply be translating these four lines, not inventing anything new.

## The Stage Everyone Wants to Skip

Here is where it gets interesting. Suppose your plan works for marks of 50, 30, and 46. The average is roughly 42, so it prints "Pass". Done, right?

A careful student asks one more question: what about the awkward inputs? Experienced problem solvers keep a short mental checklist of these "awkward input" categories, because the same handful of categories catches almost every hidden bug:

- **The boundary itself:** a value sitting exactly on the pass mark, such as 40, 40, 40.
- **The empty or zero case:** all marks recorded as zero.
- **The unexpected negative:** a mark mistyped as -5.
- **The unusually large value:** a mark of 1,000 typed by mistake instead of 100.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t2hgunm/04_checking_awkward_inputs.png)

Walk the plan through marks of 40, 40, and 40. The average is exactly 40, and because the rule says "40 or more", it correctly counts as a pass. All zeros correctly fails. Those few seconds of checking boundary cases during the "look back" stage are exactly how professionals catch the subtle bugs that would otherwise embarrass them later. Skipping this stage is how wrong solutions get delivered with full confidence, and at a large enough scale, "we forgot to check one edge case" is exactly how real banking apps and hospital scheduling systems end up in the news for the wrong reasons.

## Conclusion

A problem well understood is already half solved, so resist the itch to start building. Understand, plan, carry out, then look back, checking your boundary, zero, negative, and unusually large cases before you trust the result. Treat the keyboard as the last tool you reach for rather than the first. This same habit pays off everywhere, from coding interviews that reward clear thinking aloud, to real projects where the plan becomes the design document, to the moment you are stuck on a bug and the fastest cure is simply to understand the problem again.

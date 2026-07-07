## Introduction

It is well past midnight, Zara's bug is finally understood, the CSV loader really was forgetting to call `int()` on one column, and she has one more tool available that this entire unit has been quietly preparing her to use well: an AI coding assistant. It can plausibly fix this in seconds. The real risk is not using one, it is using one badly, pasting an error with no context, accepting whatever code comes back without reading it, and walking away having fixed a symptom while learning nothing about the actual cause, ready to hit the exact same bug again next week.

This closing lesson is about using an AI assistant the way Zara used the rubber duck and the strong question from the last lesson: as a genuine collaborator in a process she still leads and understands, not as a replacement for understanding it at all.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/09_ai_assisted_debugging_responsibly.png)

## Give It the Strong Question, Not the Weak One

Everything the previous lesson identified as a strong question for a human is exactly what makes an AI assistant's answer reliable instead of a generic guess: the exact error message, a minimal reproduction, what you expected, and your own theory so far.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2FpYXNzaXN0ZWRfZGVidWdnaW5nIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFdlYWsgcHJvbXB0OiBcImZpeCBteSBjb2RlXCIgKyB0aGUgZW50aXJlIGZvdXItZmlsZSBwcm9qZWN0IHBhc3RlZCBpblxuXG4jIFN0cm9uZyBwcm9tcHQ6IHRoZSBleGFjdCBlcnJvciwgdGhlIG1pbmltYWwgcmVwcm9kdWN0aW9uIGZyb20gdHdvIGxlc3NvbnMgYWdvLFxuIyB3aGF0IHlvdSBleHBlY3RlZCwgYW5kIHlvdXIgb3duIHRoZW9yeTpcbiMgXCJ0b3RhbF9yc3ZwcygpIHJhaXNlcyBUeXBlRXJyb3I6IHVuc3VwcG9ydGVkIG9wZXJhbmQgdHlwZShzKSBmb3IgKzogJ2ludCcgYW5kICdzdHInLlxuIyAgTWluaW1hbCBjYXNlOiBjb3VudHMgPSBbMiwgJzMnXTsgc3VtKGNvdW50cykuXG4jICBJIGV4cGVjdGVkIGV2ZXJ5IHZhbHVlIHRvIGFscmVhZHkgYmUgYW4gaW50LiBJIHN1c3BlY3QgbXkgQ1NWIGxvYWRlclxuIyAgaXNuJ3QgY29udmVydGluZyBvbmUgY29sdW1uIHdpdGggaW50KCkuIENhbiB5b3UgY29uZmlybSBhbmQgc3VnZ2VzdCBhIGZpeD9cIiJ9"
 width="100%"
></iframe>

A vague prompt invites a vague, possibly irrelevant answer. A specific one, built from work Zara already did herself, gets a specific, checkable one.

## Always Read and Understand a Suggested Fix Before Using It

The single most important habit in this entire lesson: never paste in a suggested fix you do not yet understand. If an AI assistant suggests this change to the CSV loader, the job is to read it and confirm it actually addresses the real cause, not just to trust it because it looks plausible.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2FpYXNzaXN0ZWRfZGVidWdnaW5nIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJkZWYgbG9hZF9hdHRlbmRlZXMocm93cyk6XG4gICAgYXR0ZW5kZWVzID0gW11cbiAgICBmb3IgbmFtZSwgcmF3X2NvdW50IGluIHJvd3M6XG4gICAgICAgIGNvdW50ID0gaW50KHJhd19jb3VudCkgICAgIyB0aGUgc3VnZ2VzdGVkIGZpeDogY29udmVydCBleHBsaWNpdGx5IGhlcmVcbiAgICAgICAgYXR0ZW5kZWVzLmFwcGVuZCgobmFtZSwgY291bnQpKVxuICAgIHJldHVybiBhdHRlbmRlZXNcblxucm93cyA9IFsoXCJaYXJhXCIsIFwiMlwiKSwgKFwiTGluXCIsIFwiM1wiKV1cbnByaW50KGxvYWRfYXR0ZW5kZWVzKHJvd3MpKSJ9"
 width="100%"
></iframe>

Reading this, Zara can confirm it directly matches her own diagnosis from the rubber-duck lesson: the loader was leaving `raw_count` as a string, and this line converts it explicitly. Because she understood the cause first, she can verify the fix actually addresses it, rather than just hoping it does.

## Verify the Fix the Same Way You Verify Your Own Code

A suggested fix deserves exactly the same scrutiny as code Zara wrote herself: rerun the original failing case, and confirm the original error is actually gone, not just trust that it looks reasonable.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2FpYXNzaXN0ZWRfZGVidWdnaW5nIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWYgdG90YWxfcnN2cHMoYXR0ZW5kZWVzKTpcbiAgICByZXR1cm4gc3VtKGNvdW50IGZvciBfbmFtZSwgY291bnQgaW4gYXR0ZW5kZWVzKVxuXG5maXhlZF9hdHRlbmRlZXMgPSBsb2FkX2F0dGVuZGVlcyhbKFwiWmFyYVwiLCBcIjJcIiksIChcIkxpblwiLCBcIjNcIildKVxucHJpbnQodG90YWxfcnN2cHMoZml4ZWRfYXR0ZW5kZWVzKSkgICAgIyA1LCB0aGUgYnVnIGlzIGdlbnVpbmVseSBnb25lIn0"
 width="100%"
></iframe>

This step matters because a suggested fix can look correct, use sensible-sounding variable names, and still be subtly wrong, fixing a slightly different problem than the one you actually have. Running it against your own minimal failing case from two lessons ago is the same discipline this entire unit has built toward: trust what you can verify, not what merely looks plausible.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/09_ai_suggestion_verify_tests.png)

*Treat an AI suggestion like any other possible fix: read it, test it, and explain why it works before trusting it.*

## What an AI Assistant Is Genuinely Good For, and What It Is Not

It is genuinely useful for explaining an unfamiliar error message, suggesting where to look first, or drafting a fix you then read and verify yourself. It is a poor substitute for understanding your own program's logic well enough to know whether a suggestion actually makes sense, the same understanding every other tool in this unit, print debugging, `assert`, the debugger, and minimization, was built to develop directly in you.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2FpYXNzaXN0ZWRfZGVidWdnaW5nIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIEdvb2QgdXNlOiBcImV4cGxhaW4gd2hhdCB0aGlzIHRyYWNlYmFjayBtZWFuc1wiIC0-IHlvdSBzdGlsbCB2ZXJpZnkgdGhlIGV4cGxhbmF0aW9uXG4jIEdvb2QgdXNlOiBcImhlcmUncyBteSBtaW5pbWFsIGZhaWxpbmcgY2FzZSBhbmQgbXkgdGhlb3J5LCBkb2VzIHRoaXMgZml4IG1ha2Ugc2Vuc2U_XCJcbiMgUmlza3kgdXNlOiBwYXN0aW5nIGEgZml4IGluIGltbWVkaWF0ZWx5LCB3aXRoIG5vIHJlYWRpbmcsIG5vIHVuZGVyc3RhbmRpbmcsIG5vIHJlcnVuIn0"
 width="100%"
></iframe>

## AI-Assisted Debugging at a Glance

| Habit | Why It Matters |
|---|---|
| Give it the strong question: error, minimal case, expectation, theory | Specific input produces specific, checkable answers |
| Read and understand any suggested fix before using it | A plausible-looking fix can still be wrong, or fix the wrong thing |
| Rerun your own minimal failing case afterward | Confirms the actual bug is gone, not just that the code looks different |
| Use it to build understanding, not to replace it | The goal is debugging this bug and recognizing the next one yourself |

## Your Turn: Write the Strong Prompt

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2FpYXNzaXN0ZWRfZGVidWdnaW5nIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgYXZlcmFnZV9yYXRpbmcocmF0aW5ncyk6XG4gICAgcmV0dXJuIHN1bShyYXRpbmdzKSAvIGxlbihyYXRpbmdzKVxuXG5wcmludChhdmVyYWdlX3JhdGluZyhbXSkpICAgICMgZXJyb3IhIn0"
 width="100%"
></iframe>

Write the strong prompt you would give an AI assistant for this bug, including the exact error, a minimal reproduction, what you expected, and your own theory. Then, imagining a suggested fix comes back, write down exactly how you would verify it actually works before trusting it.

## Conclusion

An AI assistant is most useful when given the same strong question, the exact error, a minimal reproduction, your expectation, and your own theory, that this unit's earlier lessons already taught you to build, and any fix it suggests deserves the same reading, understanding, and rerun-against-your-own-failing-case verification you would give code you wrote yourself. Across this entire unit, Zara moved from panicking at a crash to reading it calmly, from scattered prints to deliberate ones, from guessing to stating assumptions with `assert`, from guessing again to pausing and stepping through a live program, from noisy prints to leveled logging, from a tangled project to a minimal failing case, from silent confusion to a clearly stated question, and finally to using every tool available, AI included, with understanding leading the way rather than following behind it. That is debugging as a real, transferable skill, and it is also where this semester's foundation in Python comes to a close.

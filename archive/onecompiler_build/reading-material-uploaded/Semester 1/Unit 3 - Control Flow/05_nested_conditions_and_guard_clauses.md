## Introduction

Asha taps a movie in a streaming app on her phone, and the app makes two checks in order. First it checks she is logged in, and only then does it check whether her subscription is still active. If she is not logged in, it never even bothers checking the subscription, it just sends her to the login screen, because there was no point going further. That is a decision living inside another decision, and programmers call it nesting. Nesting is powerful, but stacked too deep, check inside check inside check, it becomes a tangle that is hard to follow.

Notice that the subscription check was never even reached when the login check failed; one decision was genuinely sitting inside the protection of another. This lesson shows how to keep such logic flat and readable.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hhawj/05_pyramid_of_doom.png)

## A Decision Inside a Decision

You nest by placing an `if` inside the block of another `if`. The inner decision is reached only when the outer condition is true.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-05-nested-conditions-and-guard-clauses-001-1e3cfeee23.html"
 width="100%"
></iframe>

Read the indentation carefully. The balance check sits one level further in, because it only happens after the PIN is accepted. With a wrong PIN, Python never even looks at the balance, which matches how a real ATM behaves.

## The Pyramid of Doom

Nesting is fine one or two levels deep. The trouble begins when a decision sits inside a decision inside a decision, marching further and further to the right.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-05-nested-conditions-and-guard-clauses-002-a9865dfecc.html"
 width="100%"
></iframe>

Code like this is hard to read, hard to change, and easy to get wrong, which is why programmers nickname it the pyramid of doom. Each extra level pushes the real action further to the right and forces a reader to hold every outer condition in their head just to understand the one buried line at the bottom. The good news is that most deep nesting can be flattened.

## Flattening the Logic

One way is to combine conditions that must all be true into a single `if` using `and`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-05-nested-conditions-and-guard-clauses-003-7aa2831738.html"
 width="100%"
></iframe>

Another way is the guard clause: deal with the failure cases first and get them out of the way, leaving the main logic clean and barely indented.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-05-nested-conditions-and-guard-clauses-004-80b8f7cff3.html"
 width="100%"
></iframe>

Here each problem is handled up front, and the successful path is the last, simplest branch. This reads top to bottom like a checklist rather than a pyramid. When you reach functions in a later unit, you will be able to make guard clauses even cleaner by stopping early, but the idea, handle the bad cases first, is already yours to use.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hhawj/05_guard_clauses_flat_checklist.png)

## Nested Conditions at a Glance

| Approach | Readability | Use When |
|---|---|---|
| Nested `if` | Gets messy past 2-3 levels | Each check genuinely depends on the one before it |
| Combine with `and` | Clean for a single pass/fail outcome | Every condition must be true together, with no separate messages needed |
| Guard clauses | Clean even with several checks | Each failing case needs its own message |

## Your Turn: Loan Eligibility

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-05-nested-conditions-and-guard-clauses-005-71520c63d6.html"
 width="100%"
></iframe>

Try a few combinations. Notice that this flat version checks each disqualifying condition in turn and only approves at the end. Compare it in your head with the deeply nested version it replaces, and you will feel why flatter is easier to follow.

## Conclusion

Nested conditions let one decision depend on another, which is natural when a later check only matters after an earlier one passes. But deep nesting quickly becomes a hard-to-read pyramid. Keep it shallow by combining conditions with `and`, or by writing guard clauses that handle the failing cases first and leave the main path clean. Readable decision logic is not a luxury, it is how you avoid bugs you cannot see. So far every condition has been a clear comparison; the next lesson looks at a different, menu-shaped kind of decision, and the one after that asks what Python actually considers true or false when there is no comparison at all.

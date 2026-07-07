## Introduction

The trip is two days away, and Dev has the full itinerary sitting in front of him: a list of fixed day-and-plan tuples, a packing list, a snack list, a seating chart. None of this data is useful sitting still. He needs to walk through the itinerary morning by morning and read each plan aloud at the class briefing, and he wants to do it without typing `itinerary[0]`, then `itinerary[1]`, then `itinerary[2]` by hand like it is still the very first lesson of this unit.

You already know the `for` loop from the looping unit, and you have been quietly using it on lists and tuples throughout this one. This final lesson pulls those threads together properly, showing the small set of patterns that make looping over lists and tuples clean, readable, and complete.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/08_itinerary_walkthrough.png)

## The Basic Walk-Through

A plain `for` loop visits every item of a list or tuple in order, with no indexing required at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2l0ZXJhdGluZ19vdmVyX2xpc3RzX2FuZF90dXBsZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InBhY2tpbmdfbGlzdCA9IFtcIndhdGVyIGJvdHRsZVwiLCBcImNoYXJnZXJcIiwgXCJJRCBjYXJkXCIsIFwicmFpbmNvYXRcIl1cbmZvciBpdGVtIGluIHBhY2tpbmdfbGlzdDpcbiAgICBwcmludChcIlBhY2s6XCIsIGl0ZW0pIn0"
 width="100%"
></iframe>

This reads exactly as "for each item in the packing list, print it", and it works identically whether the collection is a list or a tuple, since both are ordered sequences a `for` loop can step through directly.

## When You Also Need the Position: enumerate()

Sometimes the position matters as much as the value, for example when numbering each day of the itinerary. `enumerate` hands you both the index and the item together.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2l0ZXJhdGluZ19vdmVyX2xpc3RzX2FuZF90dXBsZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Iml0aW5lcmFyeSA9IFtcIlRyYXZlbCBhbmQgY2hlY2staW5cIiwgXCJXYXRlcmZhbGwgdHJla1wiLCBcIkJlYWNoIGFuZCBkZXBhcnR1cmVcIl1cbmZvciBkYXksIHBsYW4gaW4gZW51bWVyYXRlKGl0aW5lcmFyeSwgc3RhcnQ9MSk6XG4gICAgcHJpbnQoZlwiRGF5IHtkYXl9OiB7cGxhbn1cIikifQ"
 width="100%"
></iframe>

The `start=1` makes the numbering begin at 1 instead of 0, which reads far more naturally for a human audience than starting from zero would.

## Unpacking Tuples Inside a Loop

When a list holds tuples, you can unpack each tuple directly in the loop header, naming its parts instead of indexing into them one by one.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2l0ZXJhdGluZ19vdmVyX2xpc3RzX2FuZF90dXBsZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InN0b3BzID0gW1xuICAgIChcIlJlc29ydFwiLCAxNS4yOTkzLCA3NC4xMjQwKSxcbiAgICAoXCJEdWRoc2FnYXIgRmFsbHNcIiwgMTUuMzE0NCwgNzQuMzE0NCksXG5dXG5mb3IgbmFtZSwgbGF0LCBsb25nIGluIHN0b3BzOlxuICAgIHByaW50KGZcIntuYW1lfSBpcyBhdCAoe2xhdH0sIHtsb25nfSlcIikifQ"
 width="100%"
></iframe>

Each pass automatically unpacks the current tuple into `name`, `lat`, and `long`, exactly the packing-and-unpacking idea from earlier in this unit, now happening once per loop pass.

## Looping Over Two Lists Together: zip()

Occasionally you have two separate, related lists, such as student names and their seat numbers, and you want to walk through both together. `zip` pairs them up, position by position.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2l0ZXJhdGluZ19vdmVyX2xpc3RzX2FuZF90dXBsZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6Im5hbWVzID0gW1wiQXNoYVwiLCBcIlJhdmlcIiwgXCJNZWVyYVwiXVxuc2VhdHMgPSBbMSwgMiwgM11cbmZvciBuYW1lLCBzZWF0IGluIHppcChuYW1lcywgc2VhdHMpOlxuICAgIHByaW50KGZcIntuYW1lfSBpcyBpbiBzZWF0IHtzZWF0fVwiKSJ9"
 width="100%"
></iframe>

`zip` stops as soon as the shorter list runs out, so it is safest when both lists are meant to be the same length, which is exactly true of names lined up against their assigned seats.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/08_enumerate_zip_unpacks.png)


## Looping Patterns at a Glance

| Goal | Pattern |
|---|---|
| Visit every value | `for item in collection:` |
| Visit value and position | `for index, item in enumerate(collection):` |
| Visit each tuple's parts directly | `for a, b, c in list_of_tuples:` |
| Walk two lists together | `for a, b in zip(list1, list2):` |

## Your Turn: Read Out the Itinerary

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2l0ZXJhdGluZ19vdmVyX2xpc3RzX2FuZF90dXBsZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6Iml0aW5lcmFyeSA9IFtcbiAgICAoXCJEYXkgMVwiLCBcIlRyYXZlbCBhbmQgY2hlY2staW5cIiksXG4gICAgKFwiRGF5IDJcIiwgXCJXYXRlcmZhbGwgdHJla1wiKSxcbiAgICAoXCJEYXkgM1wiLCBcIkJlYWNoIGFuZCBkZXBhcnR1cmVcIiksXG5dXG5cbmZvciBkYXksIHBsYW4gaW4gaXRpbmVyYXJ5OlxuICAgIHByaW50KGZcIntkYXl9OiB7cGxhbn1cIilcblxucHJpbnQoXCJcXG4tLS0gTnVtYmVyZWQgdmVyc2lvbiAtLS1cIilcbmZvciBudW1iZXIsIChkYXksIHBsYW4pIGluIGVudW1lcmF0ZShpdGluZXJhcnksIHN0YXJ0PTEpOlxuICAgIHByaW50KGZcIntudW1iZXJ9LiB7ZGF5fSAtIHtwbGFufVwiKSJ9"
 width="100%"
></iframe>

Notice the second loop unpacks a tuple from inside an `enumerate` call, combining two patterns from this lesson at once, exactly the kind of small combination real itineraries end up needing.

## Conclusion

A plain `for` loop steps through a list or tuple directly; `enumerate` adds the position when you need it; unpacking inside the loop header reads tuple parts by name instead of by index; and `zip` walks two related lists together, position by position. Across this entire unit you have learned to hold data in order, change it, organise it, filter it, lock it, group it, nest it, and now walk through it cleanly. Lists and tuples, together with the loops you already knew, are the backbone of almost every real program you will write from here on.

## Introduction

The bus playlist for the trip has ballooned into forty songs by the time everyone has added their pick, dumped into the list in whatever order people happened to suggest them. At one point Dev wants the whole list flipped so the newest additions play first instead of last, without disturbing that original running order everywhere else. He wants to know how many times "one more song" requests have piled up for a particular track, and exactly where a specific track sits in the list. Then he wants it alphabetised, permanently in one place, but also just previewed in order somewhere else without disturbing the actual playing order. None of this needs a new playlist built from scratch. It needs the list reorganised.

Beyond adding and removing items, lists come with a set of methods for exactly this kind of organising: reversing, counting, locating, and sorting. This lesson is about putting an already-built list into the shape you actually want.

**Definition:** `Lists` carry built-in organising tools: `reverse()` and `sort()` rearrange in place and return nothing, `reversed()` and `sorted()` hand back a new view while leaving the original untouched, and `count()` and `index()` answer "how many" and "where".

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/03_playlist_sorting.png)

## Reversing in Place: reverse()

The `reverse` method flips the current order of a list in place, without sorting it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbxgm" 
 width="100%"
></iframe>

This is not the same as sorting backwards; it simply turns the list around exactly as it stands, which is exactly what Dev wants when he decides the newest playlist additions should play first. Like `sort()`, `reverse()` changes the original list directly and returns nothing, so `queue = queue.reverse()` is the same classic mistake in a new outfit, quietly leaving `queue` holding `None`.

## Reversing Without Changing the Original: reversed()

Sometimes Dev wants to glance at the playlist backwards, newest-first, without actually disturbing the order it plays in for everyone else. The built-in function `reversed()` (a function, not a method, so it does not use a dot) hands back a reverse iterator over the list, usually wrapped in `list()` to actually see it, leaving the original list exactly as it was.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbxsm" 
 width="100%"
></iframe>

`reversed()` and `reverse()` relate exactly the way `sorted()` and `sort()` do further down this lesson: the method changes the list itself, and the built-in function hands back a new view while leaving the original untouched.

## Counting Occurrences: count()

`count` tells you how many times a value appears anywhere in the list.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwby8n" 
 width="100%"
></iframe>

This answers "one more song" the way Dev actually needs it answered: not by scanning the list himself, but by asking the list directly how many times a particular request has piled up.

## Locating a Value: index()

`index` tells you the position of a value's first appearance in the list.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbynr" 
 width="100%"
></iframe>

If the value passed to `index` is not in the list at all, Python raises a `ValueError`, the same caution that applied to `remove` in the last lesson, so checking with `in` first is good practice whenever you are not certain the value is there.

## Sorting in Place: sort()

The `sort` method rearranges a list into ascending order, directly, with no new list created.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbyy7" 
 width="100%"
></iframe>

Numbers sort the same way, smallest to largest. To sort the other way round, pass `reverse=True`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbz9f" 
 width="100%"
></iframe>

Like `append`, `sort` changes the original list and returns nothing, so writing `playlist = playlist.sort()` is a classic mistake that quietly throws the list away and leaves `playlist` holding `None`.

## Sorting Without Changing the Original: sorted()

Sometimes you want a sorted view without disturbing the original order. The built-in function `sorted()` (notice it is a function, not a method, so it does not use a dot) returns a brand new sorted list and leaves the original exactly as it was.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbzmt" 
 width="100%"
></iframe>

Reach for `sort()` when you are happy to permanently reorder the list itself, and reach for `sorted()` when you need the original order preserved for something else later.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/03_sort_vs_sorted.png)

## List Organising Tools at a Glance

| Tool | Changes Original? | Returns |
|---|---|---|
| `list.reverse()` | Yes, in place | Nothing (`None`) |
| `reversed(list)` | No | A reverse iterator (wrap in `list()` to see it) |
| `list.count(value)` | No | How many times `value` appears |
| `list.index(value)` | No | The position of `value`'s first appearance |
| `list.sort()` | Yes, in place | Nothing (`None`) |
| `sorted(list)` | No | A brand new sorted list |

## Your Turn: Organise the Playlist

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44vrwbzxt" 
 width="100%"
></iframe>

Enter four song titles and watch the same small list get summarised three different ways, organised and reorganised without ever being rebuilt from nothing.

## Conclusion

Lists carry built-in organising tools: `reverse()` and `sort()` rearrange in place and return nothing, `reversed()` and `sorted()` hand back a new view while leaving the original untouched, and `count()` and `index()` answer "how many" and "where". Choosing between the in-place method and its built-in counterpart comes down to one question, for both reversing and sorting: do you still need the original order for anything else? Reversing, counting, locating, and sorting all work on values you already have; the next lesson shows how to build a whole new, filtered list out of an existing one in a single line.

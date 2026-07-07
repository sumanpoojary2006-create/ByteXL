## Introduction

The bus playlist for the trip has ballooned into forty songs by the time everyone has added their pick, dumped into the list in whatever order people happened to suggest them. Dev wants it alphabetised so people can find their own song quickly, he wants to know how many times "one more song" requests have piled up for a particular track, and at one point he wants the whole list flipped so the newest additions play first instead of last. None of this needs a new playlist built from scratch. It needs the list reorganised.

Beyond adding and removing items, lists come with a set of methods for exactly this kind of organising: sorting, reversing, counting, and locating. This lesson is about putting an already-built list into the shape you actually want.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/03_playlist_sorting.png)

## Sorting in Place: sort()

The `sort` method rearranges a list into ascending order, directly, with no new list created.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoicGxheWxpc3QgPSBbXCJTYXBwaGlyZVwiLCBcIkFudGhlbVwiLCBcIkNhbG0gVGlkZVwiLCBcIkJhc3NsaW5lXCJdXG5wbGF5bGlzdC5zb3J0KClcbnByaW50KHBsYXlsaXN0KSAgICAjIFsnQW50aGVtJywgJ0Jhc3NsaW5lJywgJ0NhbG0gVGlkZScsICdTYXBwaGlyZSddIn0"
 width="100%"
></iframe>

Numbers sort the same way, smallest to largest. To sort the other way round, pass `reverse=True`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoic2NvcmVzID0gWzcyLCA5NSwgNjAsIDg4XVxuc2NvcmVzLnNvcnQocmV2ZXJzZT1UcnVlKVxucHJpbnQoc2NvcmVzKSAgICAjIFs5NSwgODgsIDcyLCA2MF0ifQ"
 width="100%"
></iframe>

Like `append`, `sort` changes the original list and returns nothing, so writing `playlist = playlist.sort()` is a classic mistake that quietly throws the list away and leaves `playlist` holding `None`.

## Sorting Without Changing the Original: sorted()

Sometimes you want a sorted view without disturbing the original order. The built-in function `sorted()` (notice it is a function, not a method, so it does not use a dot) returns a brand new sorted list and leaves the original exactly as it was.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoicGxheWxpc3QgPSBbXCJTYXBwaGlyZVwiLCBcIkFudGhlbVwiLCBcIkNhbG0gVGlkZVwiLCBcIkJhc3NsaW5lXCJdXG5vcmRlcmVkID0gc29ydGVkKHBsYXlsaXN0KVxucHJpbnQob3JkZXJlZCkgICAgICAjIFsnQW50aGVtJywgJ0Jhc3NsaW5lJywgJ0NhbG0gVGlkZScsICdTYXBwaGlyZSddXG5wcmludChwbGF5bGlzdCkgICAgICAjIFsnU2FwcGhpcmUnLCAnQW50aGVtJywgJ0NhbG0gVGlkZScsICdCYXNzbGluZSddIC0gdW5jaGFuZ2VkIn0"
 width="100%"
></iframe>

Reach for `sort()` when you are happy to permanently reorder the list itself, and reach for `sorted()` when you need the original order preserved for something else later.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/03_sort_vs_sorted.png)


## Reversing: reverse()

The `reverse` method flips the current order of a list in place, without sorting it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoicXVldWUgPSBbXCJBc2hhXCIsIFwiUmF2aVwiLCBcIk1lZXJhXCJdXG5xdWV1ZS5yZXZlcnNlKClcbnByaW50KHF1ZXVlKSAgICAjIFsnTWVlcmEnLCAnUmF2aScsICdBc2hhJ10ifQ"
 width="100%"
></iframe>

This is not the same as sorting backwards; it simply turns the list around exactly as it stands, which is exactly what Dev wants when he decides the newest playlist additions should play first.

## Counting and Locating: count() and index()

`count` tells you how many times a value appears, and `index` tells you the position of its first appearance.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoicmVxdWVzdHMgPSBbXCJBbnRoZW1cIiwgXCJCYXNzbGluZVwiLCBcIkFudGhlbVwiLCBcIkNhbG0gVGlkZVwiLCBcIkFudGhlbVwiXVxucHJpbnQocmVxdWVzdHMuY291bnQoXCJBbnRoZW1cIikpICAgICMgM1xucHJpbnQocmVxdWVzdHMuaW5kZXgoXCJDYWxtIFRpZGVcIikpICMgMyJ9"
 width="100%"
></iframe>

If the value passed to `index` is not in the list at all, Python raises a `ValueError`, the same caution that applied to `remove` in the last lesson, so checking with `in` first is good practice whenever you are not certain the value is there.

## sort() vs sorted() at a Glance

| Tool | Changes Original? | Returns |
|---|---|---|
| `list.sort()` | Yes, in place | Nothing (`None`) |
| `sorted(list)` | No | A brand new sorted list |
| `list.reverse()` | Yes, in place | Nothing (`None`) |

## Your Turn: Organise the Playlist

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2xpc3RfbWV0aG9kc19hbmRfc29ydGluZyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoicGxheWxpc3QgPSBbXVxuZm9yIF8gaW4gcmFuZ2UoNCk6XG4gICAgcGxheWxpc3QuYXBwZW5kKGlucHV0KFwiQWRkIGEgc29uZyB0aXRsZTogXCIpKVxuXG5wcmludChcIk9yaWdpbmFsIG9yZGVyOlwiLCBwbGF5bGlzdClcbnByaW50KFwiQWxwaGFiZXRpY2FsOlwiLCBzb3J0ZWQocGxheWxpc3QpKVxuXG5wbGF5bGlzdC5yZXZlcnNlKClcbnByaW50KFwiUmV2ZXJzZWQ6XCIsIHBsYXlsaXN0KSJ9"
 width="100%"
></iframe>

Enter four song titles and watch the same small list get summarised three different ways, organised and reorganised without ever being rebuilt from nothing.

## Conclusion

Lists carry built-in organising tools: `sort()` and `reverse()` rearrange in place and return nothing, `sorted()` hands back a new sorted list while leaving the original untouched, and `count()` and `index()` answer "how many" and "where". Choosing between `sort()` and `sorted()` comes down to one question: do you still need the original order for anything else? Sorting and counting work on values you already have; the next lesson shows how to build a whole new, filtered list out of an existing one in a single line.

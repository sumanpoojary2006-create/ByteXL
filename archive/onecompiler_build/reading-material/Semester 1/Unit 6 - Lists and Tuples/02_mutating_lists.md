## Introduction

Dev's snack list was never going to stay still for long. The moment he shares it in the class group, replies start pouring in: someone wants to add chips, someone else says scrap the biscuits because two people are bringing their own, and one friend insists his snack be the very first thing in the bag so it does not get crushed. Dev keeps editing the same list, again and again, right up until the bus leaves.

With a string, this constant back-and-forth would be impossible, because strings are immutable and every small change forces you to build an entirely new one. A list is different. A list is **mutable**, which means you can add, remove, and rearrange its contents in place, without ever having to rebuild it from scratch. This lesson is about exactly that power.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/02_snack_list_editing.png)

## Adding an Item to the End: append

The `append` method adds one new item to the end of a list, in place, with no need to create a new list or store a result.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJzbmFja3MgPSBbXCJjaGlwc1wiLCBcImJpc2N1aXRzXCJdXG5zbmFja3MuYXBwZW5kKFwianVpY2UgYm94ZXNcIilcbnByaW50KHNuYWNrcykgICAgIyBbJ2NoaXBzJywgJ2Jpc2N1aXRzJywgJ2p1aWNlIGJveGVzJ10ifQ"
 width="100%"
></iframe>

Notice there is no `snacks = snacks.append(...)` here. Unlike a string method, `append` changes the list directly and returns nothing useful, which is the first sign that lists behave differently from the immutable values you have used so far.

## Adding an Item at a Chosen Spot: insert

Sometimes the new item cannot simply go at the end. `insert` takes a position and a value, and slides the value into that exact spot, pushing everything after it one step along.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJzbmFja3MuaW5zZXJ0KDAsIFwiZnJ1aXRcIilcbnByaW50KHNuYWNrcykgICAgIyBbJ2ZydWl0JywgJ2NoaXBzJywgJ2Jpc2N1aXRzJywgJ2p1aWNlIGJveGVzJ10ifQ"
 width="100%"
></iframe>

This is exactly how Dev honours his friend's request to have a snack placed first, without retyping the whole list or losing the order of everything already there.

## Taking an Item Out: remove and pop

`remove` deletes the first item that matches the value you give it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJzbmFja3MucmVtb3ZlKFwiYmlzY3VpdHNcIilcbnByaW50KHNuYWNrcykgICAgIyBbJ2ZydWl0JywgJ2NoaXBzJywgJ2p1aWNlIGJveGVzJ10ifQ"
 width="100%"
></iframe>

If the value is not in the list at all, `remove` raises a `ValueError`, so it is worth checking with `in` first if you are not certain the item exists. `pop`, by contrast, removes an item by position rather than by value, and hands it back to you as it goes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJsYXN0X2l0ZW0gPSBzbmFja3MucG9wKClcbnByaW50KGxhc3RfaXRlbSkgICAgIyBqdWljZSBib3hlc1xucHJpbnQoc25hY2tzKSAgICAgICAgIyBbJ2ZydWl0JywgJ2NoaXBzJ10ifQ"
 width="100%"
></iframe>

Called with no argument, `pop` removes and returns the last item, which is handy whenever you want to take something off a list and actually use the value you just removed, rather than simply discarding it.

## Lists Are Shared, Not Copied, by Default

Here is a subtle trap worth meeting early. Assigning a list to a second variable name does not make a separate copy; it makes a second label pointing at the very same list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJvZmZpY2lhbF9saXN0ID0gc25hY2tzXG5vZmZpY2lhbF9saXN0LmFwcGVuZChcIndhdGVyXCIpXG5wcmludChzbmFja3MpICAgICMgWydmcnVpdCcsICdjaGlwcycsICd3YXRlciddIC0gY2hhbmdlZCB0b28hIn0"
 width="100%"
></iframe>

Because `official_list` and `snacks` point at the same list in memory, changing one changes what the other sees. If Dev truly wants an independent copy to edit separately, he needs `snacks.copy()` or `list(snacks)`, not a plain assignment.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/02_list_alias_copy_warning.png)


## Mutating Methods at a Glance

| Method | Effect | Returns |
|---|---|---|
| `.append(value)` | Adds one item to the end | Nothing |
| `.insert(index, value)` | Inserts an item at a position | Nothing |
| `.remove(value)` | Deletes the first matching item | Nothing |
| `.pop()` | Removes and returns the last item | The removed item |
| `.pop(index)` | Removes and returns the item at a position | The removed item |

## Your Turn: Build a Snack List Live

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX211dGF0aW5nX2xpc3RzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJzbmFja3MgPSBbXVxuc25hY2tzLmFwcGVuZChpbnB1dChcIkZpcnN0IHNuYWNrOiBcIikpXG5zbmFja3MuYXBwZW5kKGlucHV0KFwiU2Vjb25kIHNuYWNrOiBcIikpXG5zbmFja3MuaW5zZXJ0KDAsIGlucHV0KFwiU25hY2sgdG8gcHV0IGZpcnN0OiBcIikpXG5wcmludChcIkZpbmFsIHNuYWNrIGxpc3Q6XCIsIHNuYWNrcylcblxucmVtb3ZlX2l0ZW0gPSBpbnB1dChcIkFueSBzbmFjayB0byByZW1vdmU6IFwiKVxuaWYgcmVtb3ZlX2l0ZW0gaW4gc25hY2tzOlxuICAgIHNuYWNrcy5yZW1vdmUocmVtb3ZlX2l0ZW0pXG5wcmludChcIkFmdGVyIHJlbW92aW5nOlwiLCBzbmFja3MpIn0"
 width="100%"
></iframe>

Build a small list from scratch and watch it grow, reorder, and shrink, all on the very same list, never a fresh one.

## Conclusion

Lists are mutable: `append` adds to the end, `insert` adds at a chosen position, `remove` deletes by value, and `pop` removes by position while handing the removed item back to you. Remember that assigning a list to a new name shares the same list rather than copying it, so use `.copy()` when you genuinely need an independent version. Now that you can change a list freely, the next lesson looks at the built-in methods that organise it, especially sorting it into a sensible order.

## Introduction

Dev's snack list was never going to stay still for long. The moment he shares it in the class group, replies start pouring in: someone wants to add chips, someone else says scrap the biscuits because two people are bringing their own, and one friend insists his snack be the very first thing in the bag so it does not get crushed. Dev keeps editing the same list, again and again, right up until the bus leaves.

With a string, this constant back-and-forth would be impossible, because strings are immutable and every small change forces you to build an entirely new one. A list is different. A list is **mutable**, which means you can add, remove, and rearrange its contents in place, without ever having to rebuild it from scratch. This lesson is about exactly that power.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/02_snack_list_editing.png)

## Adding an Item to the End: append

The `append` method adds one new item to the end of a list, in place, with no need to create a new list or store a result.

```python
snacks = ["chips", "biscuits"]
snacks.append("juice boxes")
print(snacks)    # ['chips', 'biscuits', 'juice boxes']
```

Notice there is no `snacks = snacks.append(...)` here. Unlike a string method, `append` changes the list directly and returns nothing useful, which is the first sign that lists behave differently from the immutable values you have used so far.

## Adding an Item at a Chosen Spot: insert

Sometimes the new item cannot simply go at the end. `insert` takes a position and a value, and slides the value into that exact spot, pushing everything after it one step along.

```python
snacks = ["chips", "biscuits", "juice boxes"]
snacks.insert(0, "fruit")
print(snacks)    # ['fruit', 'chips', 'biscuits', 'juice boxes']
```

This is exactly how Dev honours his friend's request to have a snack placed first, without retyping the whole list or losing the order of everything already there.

## Taking an Item Out: remove and pop

`remove` deletes the first item that matches the value you give it.

```python
snacks = ["fruit", "chips", "biscuits", "juice boxes"]
snacks.remove("biscuits")
print(snacks)    # ['fruit', 'chips', 'juice boxes']
```

If the value is not in the list at all, `remove` raises a `ValueError`, so it is worth checking with `in` first if you are not certain the item exists. `pop`, by contrast, removes an item by position rather than by value, and hands it back to you as it goes.

```python
snacks = ["fruit", "chips", "juice boxes"]
last_item = snacks.pop()
print(last_item)    # juice boxes
print(snacks)        # ['fruit', 'chips']
```

Called with no argument, `pop` removes and returns the last item, which is handy whenever you want to take something off a list and actually use the value you just removed, rather than simply discarding it.

## Lists Are Shared, Not Copied, by Default

Here is a subtle trap worth meeting early. Assigning a list to a second variable name does not make a separate copy; it makes a second label pointing at the very same list.

```python
snacks = ["fruit", "chips"]
official_list = snacks
official_list.append("water")
print(snacks)    # ['fruit', 'chips', 'water'] - changed too!
```

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

```python
snacks = []
snacks.append(input("First snack: "))
snacks.append(input("Second snack: "))
snacks.insert(0, input("Snack to put first: "))
print("Final snack list:", snacks)

remove_item = input("Any snack to remove: ")
if remove_item in snacks:
    snacks.remove(remove_item)
print("After removing:", snacks)
```

Build a small list from scratch and watch it grow, reorder, and shrink, all on the very same list, never a fresh one.

## Conclusion

Lists are mutable: `append` adds to the end, `insert` adds at a chosen position, `remove` deletes by value, and `pop` removes by position while handing the removed item back to you. Remember that assigning a list to a new name shares the same list rather than copying it, so use `.copy()` when you genuinely need an independent version. Now that you can change a list freely, the next lesson looks at the built-in methods that organise it, especially sorting it into a sensible order.

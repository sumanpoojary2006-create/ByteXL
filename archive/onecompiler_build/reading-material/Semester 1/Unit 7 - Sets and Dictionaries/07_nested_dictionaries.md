## Introduction

The merch stall was never the only stall at the fest. There is also the food stall and the games stall, and the committee wants one combined report covering all three: every stall, every item it sells, and that item's price. A single flat dictionary cannot hold this on its own, because "T-shirt" might mean one thing at the merch stall and nothing at all at the food stall. Tara needs to say "food stall, then within that, samosa" and land on one exact price, the same row-then-column shape you met with nested lists.

The structure that captures this is a **nested dictionary**: a dictionary whose values are themselves dictionaries. It is the natural way to represent anything organised into named groups, each holding its own key-value data.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/07_fest_stalls_nested_report.png)

## A Dictionary Whose Values Are Dictionaries

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImZlc3Rfc3RhbGxzID0ge1xuICAgIFwiTWVyY2hcIjoge1wiVC1zaGlydFwiOiAzNTAsIFwiTXVnXCI6IDE1MH0sXG4gICAgXCJGb29kXCI6IHtcIlNhbW9zYVwiOiAzMCwgXCJDb2xkIERyaW5rXCI6IDQwfSxcbiAgICBcIkdhbWVzXCI6IHtcIlJpbmcgVG9zc1wiOiAyMCwgXCJEYXJ0XCI6IDI1fSxcbn0ifQ"
 width="100%"
></iframe>

Here the outer dictionary's keys are stall names, and each value is itself a complete dictionary of that stall's items and prices. Printing `fest_stalls` shows the whole structure, braces within braces, mirroring stalls within a fest.

## Reaching One Value: Double Key Lookup

To reach one specific price, you look up twice: once for the outer dictionary, the stall, and once for the inner dictionary, the item within that stall.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InByaW50KGZlc3Rfc3RhbGxzW1wiRm9vZFwiXSkgICAgICAgICAgICAgIyB7J1NhbW9zYSc6IDMwLCAnQ29sZCBEcmluayc6IDQwfVxucHJpbnQoZmVzdF9zdGFsbHNbXCJGb29kXCJdW1wiU2Ftb3NhXCJdKSAgICMgMzBcbnByaW50KGZlc3Rfc3RhbGxzW1wiR2FtZXNcIl1bXCJEYXJ0XCJdKSAgICAjIDI1In0"
 width="100%"
></iframe>

Read `fest_stalls["Food"]["Samosa"]` from left to right: "go to the Food stall, then within that stall, look up Samosa." This is exactly the stall-then-item lookup the combined report needs, with no ambiguity about which stall's samosa price you are reading.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/07_nested_dict_key_path.png)


## Changing One Nested Value

Because dictionaries are mutable, you can update one value deep inside the structure directly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImZlc3Rfc3RhbGxzW1wiRm9vZFwiXVtcIlNhbW9zYVwiXSA9IDM1XG5wcmludChmZXN0X3N0YWxsc1tcIkZvb2RcIl0pICAgICMgeydTYW1vc2EnOiAzNSwgJ0NvbGQgRHJpbmsnOiA0MH0ifQ"
 width="100%"
></iframe>

Only that one price changes. Every other stall, and every other item within the Food stall, is untouched, exactly the kind of precise, surgical update you want when one price rises and nothing else should.

## Adding a Whole New Stall

Adding a brand new stall is just adding a new key whose value happens to be an entire dictionary.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImZlc3Rfc3RhbGxzW1wiQm9va3NcIl0gPSB7XCJOb3ZlbFwiOiAxMjAsIFwiQ29taWNcIjogNjB9XG5wcmludChmZXN0X3N0YWxscy5rZXlzKCkpICAgICMgZGljdF9rZXlzKFsnTWVyY2gnLCAnRm9vZCcsICdHYW1lcycsICdCb29rcyddKSJ9"
 width="100%"
></iframe>

## Looping Through a Nested Dictionary

A nested loop, just like the one used for nested lists, is the natural way to visit every item across every stall.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImZvciBzdGFsbCwgaXRlbXMgaW4gZmVzdF9zdGFsbHMuaXRlbXMoKTpcbiAgICBwcmludChmXCItLS0ge3N0YWxsfSAtLS1cIilcbiAgICBmb3IgaXRlbSwgcHJpY2UgaW4gaXRlbXMuaXRlbXMoKTpcbiAgICAgICAgcHJpbnQoZlwiICB7aXRlbX06IHtwcmljZX1cIikifQ"
 width="100%"
></iframe>

The outer loop walks through each stall, and the inner loop walks through that stall's own items, exactly matching the two-level shape of the data. This is the loop that finally produces the full, combined fest report Tara was asked for.

## Nested Dictionary Lookups at a Glance

| Expression | Meaning |
|---|---|
| `fest_stalls["Food"]` | The whole inner dictionary for one stall |
| `fest_stalls["Food"]["Samosa"]` | One specific price |
| `fest_stalls["Food"]["Samosa"] = 35` | Update one specific price |
| `fest_stalls["Books"] = {...}` | Add an entire new stall at once |
| `for stall, items in fest_stalls.items(): for item, price in items.items():` | Visit every item across every stall |

## Your Turn: Build a Two-Stall Report

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9kaWN0aW9uYXJpZXMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6InN0YWxscyA9IHt9XG5mb3Igc3RhbGxfbmFtZSBpbiBbXCJNZXJjaFwiLCBcIkZvb2RcIl06XG4gICAgaXRlbXMgPSB7fVxuICAgIGZvciBfIGluIHJhbmdlKDIpOlxuICAgICAgICBuYW1lID0gaW5wdXQoZlwie3N0YWxsX25hbWV9IGl0ZW0gbmFtZTogXCIpXG4gICAgICAgIHByaWNlID0gZmxvYXQoaW5wdXQoZlwie25hbWV9IHByaWNlOiBcIikpXG4gICAgICAgIGl0ZW1zW25hbWVdID0gcHJpY2VcbiAgICBzdGFsbHNbc3RhbGxfbmFtZV0gPSBpdGVtc1xuXG5mb3Igc3RhbGwsIGl0ZW1zIGluIHN0YWxscy5pdGVtcygpOlxuICAgIHByaW50KGZcIi0tLSB7c3RhbGx9IC0tLVwiKVxuICAgIGZvciBpdGVtLCBwcmljZSBpbiBpdGVtcy5pdGVtcygpOlxuICAgICAgICBwcmludChmXCIgIHtpdGVtfToge3ByaWNlfVwiKSJ9"
 width="100%"
></iframe>

Build a small two-stall structure from your own input, then watch the nested loop print it back out, organised exactly the way it was entered.

## Conclusion

A nested dictionary is a dictionary whose values are themselves dictionaries, the natural shape for data organised into named groups, reached with two key lookups: `data[group][item]`. Visiting every value pairs with a nested loop, one level of loop for each level of nesting, the same idea you already used for nested lists. You can now group, sort, filter, and grid key-value data at any depth the fest can throw at you; the final lesson of this unit steps back to decide which structure, list, tuple, set, or dictionary, actually fits a given job.

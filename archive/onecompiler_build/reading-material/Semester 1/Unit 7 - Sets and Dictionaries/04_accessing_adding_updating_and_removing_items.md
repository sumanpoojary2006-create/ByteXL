## Introduction

The merch stall is never still for long. A new shipment of caps arrives partway through the day, so a brand new item needs adding to the price list. The badge price gets revised down to clear stock, so an existing value needs updating. The last mug sells, so the whole entry needs to disappear rather than sit there pointing at stock that no longer exists. Tara is doing to her price dictionary exactly what she once did to a list: changing it freely, in place, while the stall is open.

Dictionaries are mutable just like lists, and this lesson covers the small set of operations that add, change, and remove key-value pairs without ever needing to rebuild the whole dictionary from scratch.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/04_stall_dictionary_editing.png)

## Adding a New Key

Assign to a key that does not exist yet, and Python creates it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwcmljZXMgPSB7XCJULXNoaXJ0XCI6IDM1MCwgXCJNdWdcIjogMTUwLCBcIkJhZGdlXCI6IDUwfVxucHJpY2VzW1wiQ2FwXCJdID0gMjAwXG5wcmludChwcmljZXMpICAgICMgeydULXNoaXJ0JzogMzUwLCAnTXVnJzogMTUwLCAnQmFkZ2UnOiA1MCwgJ0NhcCc6IDIwMH0ifQ"
 width="100%"
></iframe>

There is no separate "add" method to remember here; the square-bracket assignment itself decides whether it is adding or changing, based on one simple rule covered next.

## Updating an Existing Key

Assign to a key that already exists, and Python overwrites its value instead of creating a duplicate.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJwcmljZXNbXCJCYWRnZVwiXSA9IDMwXG5wcmludChwcmljZXNbXCJCYWRnZVwiXSkgICAgIyAzMCJ9"
 width="100%"
></iframe>

The same `dictionary[key] = value` line either adds or updates, and the only thing that decides which one happens is whether that key was already present. This is worth sitting with for a moment: dictionaries never hold two entries with the same key, so an assignment to an existing key can only ever mean "replace the old value."

## Removing a Key: del and pop

The `del` keyword removes a key-value pair outright, with nothing handed back.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWwgcHJpY2VzW1wiTXVnXCJdXG5wcmludChwcmljZXMpICAgICMgTXVnIGlzIGdvbmUgZW50aXJlbHkifQ"
 width="100%"
></iframe>

`pop`, just like with lists, removes the entry and returns its value, which is handy when you want to use the removed value on your way out.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJzb2xkX291dF9wcmljZSA9IHByaWNlcy5wb3AoXCJDYXBcIilcbnByaW50KHNvbGRfb3V0X3ByaWNlKSAgICAjIDIwMFxucHJpbnQocHJpY2VzKSAgICAgICAgICAgICAjIENhcCBpcyBnb25lLCAyMDAgd2FzIGhhbmRlZCBiYWNrIn0"
 width="100%"
></iframe>

Both `del` and `pop` raise a `KeyError` if the key does not exist, so it is good practice to check with `in` first whenever you are not certain the key is there.

## Safe Lookups With get()

The `get` method looks up a key without ever raising an error, returning `None`, or a default value you choose, if the key is missing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJwcmludChwcmljZXMuZ2V0KFwiTXVnXCIpKSAgICAgICAgICAgICAjIE5vbmUsIHNpbmNlIE11ZyB3YXMgcmVtb3ZlZFxucHJpbnQocHJpY2VzLmdldChcIk11Z1wiLCAwKSkgICAgICAgICAgIyAwLCB0aGUgY2hvc2VuIGRlZmF1bHQgaW5zdGVhZCBvZiBhIGNyYXNoIn0"
 width="100%"
></iframe>

This is often nicer than an `if key in dictionary:` check followed by a lookup, because `get` does both jobs, look up and fall back safely, in one call.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/04_get_vs_keyerror.png)


## Dictionary Editing at a Glance

| Action | Code | Notes |
|---|---|---|
| Add a new key | `d[key] = value` | Creates the entry if the key was missing |
| Update an existing key | `d[key] = value` | Same syntax, overwrites the old value |
| Remove a key | `del d[key]` | Raises `KeyError` if missing |
| Remove and return a value | `d.pop(key)` | Raises `KeyError` if missing |
| Look up safely | `d.get(key, default)` | Never raises an error |

## Your Turn: Manage the Stall Live

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2FjY2Vzc2luZ19hZGRpbmdfdXBkYXRpbmdfYW5kX3JlbW92aW5nX2l0ZW1zIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJzdG9jayA9IHtcIlQtc2hpcnRcIjogMjAsIFwiTXVnXCI6IDE1fVxuXG5zdG9ja1tcIkJhZGdlXCJdID0gNDBcbnByaW50KFwiQWZ0ZXIgYWRkaW5nIEJhZGdlOlwiLCBzdG9jaylcblxuc3RvY2tbXCJNdWdcIl0gPSBzdG9ja1tcIk11Z1wiXSAtIDFcbnByaW50KFwiQWZ0ZXIgb25lIG11ZyBzb2xkOlwiLCBzdG9jaylcblxuaWYgXCJULXNoaXJ0XCIgaW4gc3RvY2sgYW5kIHN0b2NrW1wiVC1zaGlydFwiXSA9PSAwOlxuICAgIGRlbCBzdG9ja1tcIlQtc2hpcnRcIl1cblxucHJpbnQoXCJTdG9jayBjaGVjayBmb3IgQ2FwOlwiLCBzdG9jay5nZXQoXCJDYXBcIiwgXCJub3Qgc3RvY2tlZFwiKSkifQ"
 width="100%"
></iframe>

Notice the safe `get` call at the end never risks crashing on a key that was never added in the first place.

## Conclusion

Dictionaries are mutable: assigning to a key either adds it or updates it depending on whether it already exists, `del` and `pop` remove a key with `pop` handing back the removed value, and `get` looks up a key safely with a fallback default. With a stall's worth of items changing all day, the next lesson covers how to walk through the whole dictionary cleanly for an end-of-day report.

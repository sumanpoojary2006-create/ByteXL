## Introduction

The fest has closed for the day, and Tara needs to write up a quick stall report: every item she sold, alongside its price, printed out one line at a time for the treasurer. Looking up one price by one key, the way the last two lessons worked, will not do here. She needs to walk through the entire dictionary, every key and every value, in one pass.

You already know the `for` loop walks through lists and tuples directly. Dictionaries can be looped over too, but because every entry is actually a pair, Python gives you three related ways to do it, depending on whether you want the keys, the values, or both together.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/05_end_of_day_report_loop.png)

## Looping Over Keys

By default, looping directly over a dictionary visits its keys, one at a time.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InByaWNlcyA9IHtcIlQtc2hpcnRcIjogMzUwLCBcIk11Z1wiOiAxNTAsIFwiQmFkZ2VcIjogNTB9XG5mb3IgaXRlbSBpbiBwcmljZXM6XG4gICAgcHJpbnQoaXRlbSkifQ"
 width="100%"
></iframe>

This prints just the item names: T-shirt, Mug, Badge. To also use the price inside the loop, you would have to look it up yourself with `prices[item]`, which works, but there is a cleaner way for when you need both.

## Looping Over Values: .values()

When you only care about the values and not which key they belong to, `.values()` hands you just those.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImZvciBwcmljZSBpbiBwcmljZXMudmFsdWVzKCk6XG4gICAgcHJpbnQocHJpY2UpIn0"
 width="100%"
></iframe>

This is perfect for a quick total: summing every price without caring which item it belonged to.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InRvdGFsX3ZhbHVlID0gc3VtKHByaWNlcy52YWx1ZXMoKSlcbnByaW50KFwiVG90YWwgY2F0YWxvZ3VlIHZhbHVlOlwiLCB0b3RhbF92YWx1ZSkifQ"
 width="100%"
></iframe>

## Looping Over Both at Once: .items()

Most real reporting needs the key and the value together, and `.items()` gives you exactly that, as a pair you can unpack directly in the loop header.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImZvciBpdGVtLCBwcmljZSBpbiBwcmljZXMuaXRlbXMoKTpcbiAgICBwcmludChmXCJ7aXRlbX06IHtwcmljZX1cIikifQ"
 width="100%"
></iframe>

Read this exactly like the tuple-unpacking loops from the lists and tuples unit, because that is precisely what is happening: each entry comes out as an `(item, price)` pair, and the loop header unpacks it on the spot. This is the line Tara actually uses to write her end-of-day report.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/05_dict_keys_values_items.png)


## Keys, Values, and Items at a Glance

| Want | Use | Example Loop |
|---|---|---|
| Just the keys | `for key in d:` or `for key in d.keys():` | `for item in prices:` |
| Just the values | `for value in d.values():` | `for price in prices.values():` |
| Both together | `for key, value in d.items():` | `for item, price in prices.items():` |

`d.keys()` and looping over `d` directly do the same thing; the explicit `.keys()` is mostly used for readability or when you need to pass the keys somewhere else, such as into `sorted()`.

## A Practical Combination: Sorted Reporting

Combine `.items()` with `sorted()` from the lists and tuples unit, and you get a report in a sensible order rather than whatever order the dictionary happens to hold.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImZvciBpdGVtLCBwcmljZSBpbiBzb3J0ZWQocHJpY2VzLml0ZW1zKCkpOlxuICAgIHByaW50KGZcIntpdGVtfToge3ByaWNlfVwiKSJ9"
 width="100%"
></iframe>

`sorted()` on a list of pairs sorts by the first element of each pair by default, which here means alphabetically by item name, exactly the tidy order a report should read in.

## Your Turn: Write the End-of-Day Report

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2l0ZXJhdGluZ19kaWN0aW9uYXJpZXMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6InN0b2NrID0ge1wiVC1zaGlydFwiOiAxMiwgXCJNdWdcIjogOCwgXCJCYWRnZVwiOiAyNX1cblxucHJpbnQoXCItLS0gRW5kIG9mIERheSBSZXBvcnQgLS0tXCIpXG5mb3IgaXRlbSwgY291bnQgaW4gc29ydGVkKHN0b2NrLml0ZW1zKCkpOlxuICAgIHByaW50KGZcIntpdGVtfToge2NvdW50fSBzb2xkXCIpXG5cbnByaW50KFwiVG90YWwgaXRlbXMgc29sZDpcIiwgc3VtKHN0b2NrLnZhbHVlcygpKSkifQ"
 width="100%"
></iframe>

This single small script reads every entry, sorts it for readability, and totals the values, three different jobs from the same three loop tools.

## Conclusion

Looping over a dictionary directly visits its keys, `.values()` visits just the values, and `.items()` visits both as unpackable pairs, the tool reached for most often in real reporting. Combine `.items()` with `sorted()` whenever the order matters. You can now read the whole dictionary cleanly; the next lesson shows how to build a brand new dictionary, filtered or transformed, in a single line.

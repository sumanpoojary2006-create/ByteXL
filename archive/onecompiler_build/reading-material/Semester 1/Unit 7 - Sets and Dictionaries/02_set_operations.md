## Introduction

The fest runs for two days, and Tara has a clean set of unique attendee IDs for each one. Now the questions get more interesting. How many people came on both days? How many came only on day one, and never showed up again? How many distinct people attended across the whole fest, counted just once each even if they came twice? Scanning through two separate lists by eye to answer these would be slow and error-prone.

Sets answer all three questions in a single line each, because comparing sets is something Python builds in directly. These comparisons are called **set operations**, and they read almost exactly like the questions Tara is actually asking.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/02_two_day_attendee_overlap.png)

## Union: Everyone, Counted Once

The union of two sets combines them into one, with every value appearing only once even if it was in both.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3NldF9vcGVyYXRpb25zIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJkYXkxID0ge1wiQTEwMVwiLCBcIkExMDJcIiwgXCJBMTAzXCIsIFwiQTEwNFwifVxuZGF5MiA9IHtcIkExMDNcIiwgXCJBMTA0XCIsIFwiQTEwNVwifVxuXG5hbGxfYXR0ZW5kZWVzID0gZGF5MSB8IGRheTJcbnByaW50KGFsbF9hdHRlbmRlZXMpICAgICMgYWxsIGZpdmUgSURzLCBBMTAxIHRocm91Z2ggQTEwNSwgb3JkZXIgbm90IGd1YXJhbnRlZWQifQ"
 width="100%"
></iframe>

The `|` operator reads as "or": a value belongs to the union if it was in day1, or day2, or both. The same result comes from `day1.union(day2)`, written as a method instead of a symbol; both forms are common, and it is worth recognising either. As with any set, do not expect the printed order to match the order shown here exactly.

## Intersection: Only the Overlap

The intersection keeps only the values present in both sets, exactly answering "who came on both days."

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3NldF9vcGVyYXRpb25zIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJib3RoX2RheXMgPSBkYXkxICYgZGF5MlxucHJpbnQoYm90aF9kYXlzKSAgICAjIEExMDMgYW5kIEExMDQsIG9yZGVyIG5vdCBndWFyYW50ZWVkIn0"
 width="100%"
></iframe>

The `&` operator reads as "and." Only A103 and A104 appear in both `day1` and `day2`, so only those two survive. `day1.intersection(day2)` does the same thing.

## Difference: In One, Not the Other

The difference keeps values that are in the first set but not the second, and order matters here, unlike with union and intersection.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3NldF9vcGVyYXRpb25zIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJvbmx5X2RheTEgPSBkYXkxIC0gZGF5MlxucHJpbnQob25seV9kYXkxKSAgICAjIEExMDEgYW5kIEExMDIsIG9yZGVyIG5vdCBndWFyYW50ZWVkXG5cbm9ubHlfZGF5MiA9IGRheTIgLSBkYXkxXG5wcmludChvbmx5X2RheTIpICAgICMgeydBMTA1J30ifQ"
 width="100%"
></iframe>

`day1 - day2` answers "who came on day one and never returned", while `day2 - day1` answers the opposite question, "who only showed up on day two." Swapping the order swaps the answer entirely, so always read a difference as "this set, minus whatever the other set already covers."

## Symmetric Difference: In Exactly One, Not Both

Sometimes you want everyone who attended exactly one day, excluding the people who came to both. That is the symmetric difference.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3NldF9vcGVyYXRpb25zIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJleGFjdGx5X29uZV9kYXkgPSBkYXkxIF4gZGF5MlxucHJpbnQoZXhhY3RseV9vbmVfZGF5KSAgICAjIEExMDEsIEExMDIsIGFuZCBBMTA1LCBvcmRlciBub3QgZ3VhcmFudGVlZCJ9"
 width="100%"
></iframe>

The `^` operator keeps values that are in either set but not in both at once, which is the union minus the intersection in one step.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/02_set_operation_outputs.png)


## Set Operations at a Glance

| Operation | Symbol | Method | Meaning |
|---|---|---|---|
| Union | `\|` | `.union()` | In either set, counted once |
| Intersection | `&` | `.intersection()` | In both sets |
| Difference | `-` | `.difference()` | In the first set, not the second |
| Symmetric difference | `^` | `.symmetric_difference()` | In exactly one set, not both |

## Your Turn: Compare Two Days

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3NldF9vcGVyYXRpb25zIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkYXkxID0gc2V0KGlucHV0KFwiRGF5IDEgYXR0ZW5kZWUgSURzLCBzcGFjZSBzZXBhcmF0ZWQ6IFwiKS5zcGxpdCgpKVxuZGF5MiA9IHNldChpbnB1dChcIkRheSAyIGF0dGVuZGVlIElEcywgc3BhY2Ugc2VwYXJhdGVkOiBcIikuc3BsaXQoKSlcblxucHJpbnQoXCJDYW1lIGJvdGggZGF5czpcIiwgZGF5MSAmIGRheTIpXG5wcmludChcIk9ubHkgZGF5IDE6XCIsIGRheTEgLSBkYXkyKVxucHJpbnQoXCJPbmx5IGRheSAyOlwiLCBkYXkyIC0gZGF5MSlcbnByaW50KFwiVG90YWwgdW5pcXVlIGF0dGVuZGVlczpcIiwgbGVuKGRheTEgfCBkYXkyKSkifQ"
 width="100%"
></iframe>

Enter two overlapping lists of IDs and watch all four questions answered instantly from the same two sets, no manual comparison required.

## Conclusion

Sets compare cleanly with `|` for union, `&` for intersection, `-` for difference, and `^` for symmetric difference, turning questions like "who attended both, either, or only one" into single, readable lines. Sets are excellent at tracking who or what is present, but they cannot attach extra information to each value, such as a price or a score. For that, you need a structure that pairs every value with something else, which is exactly what the next lesson, dictionaries, introduces.

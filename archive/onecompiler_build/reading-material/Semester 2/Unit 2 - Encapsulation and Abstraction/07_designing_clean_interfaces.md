## Introduction

Priya is ready to put everything in this unit together. She has encapsulated state with properties, defined a formal interface with an ABC, and written concrete classes that implement it. But there is a final, practical question her tech lead poses: "How do you know if the interface you designed is actually clean?" He means: what is the difference between an interface that makes code easier to write and one that just adds boilerplate?

This lesson synthesizes the unit into concrete design principles, shows the full shape of a well-designed component, and highlights the most common mistakes that make interfaces harder rather than easier to use.

![](images/07_designing_clean_interfaces.png)

## Principle 1: Expose What Callers Need, Nothing More

A clean interface has no public methods or properties that callers are not supposed to use. Every public name is a commitment: once published, callers will depend on it, and changing or removing it becomes a breaking change.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Rlc2lnbmluZ19jbGVhbl9pbnRlcmZhY2VzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIGFiYyBpbXBvcnQgQUJDLCBhYnN0cmFjdG1ldGhvZFxuXG5jbGFzcyBOb3RpZmllcihBQkMpOlxuICAgIEBhYnN0cmFjdG1ldGhvZFxuICAgIGRlZiBzZW5kKHNlbGYsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgICAgICBcIlwiXCJTZW5kIGEgbm90aWZpY2F0aW9uLiBjb250YWN0IGFuZCBtZXNzYWdlIGFyZSBzdHJpbmdzLlwiXCJcIlxuXG4gICAgIyBzZW5kX2JhdGNoIGlzIGEgY29udmVuaWVuY2UgbWV0aG9kIGNhbGxlcnMgbWF5IHdhbnRcbiAgICBkZWYgc2VuZF9iYXRjaChzZWxmLCBjb250YWN0cywgbWVzc2FnZSk6XG4gICAgICAgIGZvciBjb250YWN0IGluIGNvbnRhY3RzOlxuICAgICAgICAgICAgc2VsZi5zZW5kKGNvbnRhY3QsIG1lc3NhZ2UpXG5cbiAgICAjIF92YWxpZGF0ZSBpcyBpbnRlcm5hbCwgZG8gbm90IGV4cG9zZSBpdFxuICAgIGRlZiBfdmFsaWRhdGUoc2VsZiwgY29udGFjdCwgbWVzc2FnZSk6XG4gICAgICAgIGlmIG5vdCBjb250YWN0OlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcImNvbnRhY3QgY2Fubm90IGJlIGVtcHR5XCIpXG4gICAgICAgIGlmIG5vdCBtZXNzYWdlOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcIm1lc3NhZ2UgY2Fubm90IGJlIGVtcHR5XCIpIn0"
 width="100%"
></iframe>

The public interface is two methods: `send` and `send_batch`. The validation helper is prefixed with `_` to signal it is internal. Callers never need to call `_validate` directly; the class calls it as needed inside `send`.

## Principle 2: Make It Hard to Use Incorrectly

A well-designed interface should be harder to misuse than to use correctly. This is achieved through type checking in setters, sensible defaults, and validation at the entry point.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Rlc2lnbmluZ19jbGVhbl9pbnRlcmZhY2VzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzPTEpOlxuICAgICAgICBpZiBub3QgaXNpbnN0YW5jZSh0aXRsZSwgc3RyKSBvciBub3QgdGl0bGUuc3RyaXAoKTpcbiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJ0aXRsZSBtdXN0IGJlIGEgbm9uLWVtcHR5IHN0cmluZ1wiKVxuICAgICAgICBpZiBub3QgaXNpbnN0YW5jZShjb3BpZXMsIGludCkgb3IgY29waWVzIDwgMDpcbiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJjb3BpZXMgbXVzdCBiZSBhIG5vbi1uZWdhdGl2ZSBpbnRlZ2VyXCIpXG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZS5zdHJpcCgpXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBAcHJvcGVydHlcbiAgICBkZWYgY29waWVzKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5fY29waWVzXG5cbiAgICBAY29waWVzLnNldHRlclxuICAgIGRlZiBjb3BpZXMoc2VsZiwgdmFsdWUpOlxuICAgICAgICBpZiBub3QgaXNpbnN0YW5jZSh2YWx1ZSwgaW50KSBvciB2YWx1ZSA8IDA6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKFwiY29waWVzIG11c3QgYmUgYSBub24tbmVnYXRpdmUgaW50ZWdlclwiKVxuICAgICAgICBzZWxmLl9jb3BpZXMgPSB2YWx1ZSJ9"
 width="100%"
></iframe>

Validation in `__init__` and the setter means an invalid `Book` object simply cannot exist. Callers do not need to remember to validate; the class takes care of it for them.

## Principle 3: Keep Interfaces Narrow and Focused

An interface that declares 12 abstract methods is a burden: every concrete subclass must implement all 12, even if it only needs 3. Good interface design splits a large interface into smaller, more focused ones.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Rlc2lnbmluZ19jbGVhbl9pbnRlcmZhY2VzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIE9uZSBsYXJnZSBpbnRlcmZhY2UgKGhhcmQgdG8gaW1wbGVtZW50KTpcbmNsYXNzIEZ1bGxMaWJyYXJ5U2VydmljZShBQkMpOlxuICAgIEBhYnN0cmFjdG1ldGhvZFxuICAgIGRlZiBzZW5kX25vdGlmaWNhdGlvbihzZWxmLCBjb250YWN0LCBtZXNzYWdlKTogLi4uXG4gICAgQGFic3RyYWN0bWV0aG9kXG4gICAgZGVmIGV4cG9ydF9jYXRhbG9nKHNlbGYsIGZpbGVuYW1lKTogLi4uXG4gICAgQGFic3RyYWN0bWV0aG9kXG4gICAgZGVmIGdlbmVyYXRlX3JlcG9ydChzZWxmLCBwZXJpb2QpOiAuLi5cbiAgICBAYWJzdHJhY3RtZXRob2RcbiAgICBkZWYgaGFuZGxlX3BheW1lbnQoc2VsZiwgYW1vdW50KTogLi4uXG5cbiMgQmV0dGVyOiB0aHJlZSBmb2N1c2VkIGludGVyZmFjZXNcbmNsYXNzIE5vdGlmaWVyKEFCQyk6XG4gICAgQGFic3RyYWN0bWV0aG9kXG4gICAgZGVmIHNlbmQoc2VsZiwgY29udGFjdCwgbWVzc2FnZSk6IC4uLlxuXG5jbGFzcyBFeHBvcnRlcihBQkMpOlxuICAgIEBhYnN0cmFjdG1ldGhvZFxuICAgIGRlZiBleHBvcnQoc2VsZiwgZGF0YSwgZmlsZW5hbWUpOiAuLi5cblxuY2xhc3MgUGF5bWVudEhhbmRsZXIoQUJDKTpcbiAgICBAYWJzdHJhY3RtZXRob2RcbiAgICBkZWYgY2hhcmdlKHNlbGYsIGFtb3VudCwgYWNjb3VudCk6IC4uLiJ9"
 width="100%"
></iframe>

A class that needs to send notifications and export data can inherit from both `Notifier` and `Exporter` without being forced to implement payment handling it will never use.

## Putting It Together: A Complete Component

Here is what the full `Book`-and-`Notifier` design looks like when all the lessons of this unit are applied together:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Rlc2lnbmluZ19jbGVhbl9pbnRlcmZhY2VzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIGFiYyBpbXBvcnQgQUJDLCBhYnN0cmFjdG1ldGhvZFxuXG5jbGFzcyBOb3RpZmllcihBQkMpOlxuICAgIEBhYnN0cmFjdG1ldGhvZFxuICAgIGRlZiBzZW5kKHNlbGYsIGNvbnRhY3QsIG1lc3NhZ2UpOlxuICAgICAgICBcIlwiXCJTZW5kIG9uZSBtZXNzYWdlIHRvIG9uZSBjb250YWN0LlwiXCJcIlxuXG4gICAgZGVmIHNlbmRfYmF0Y2goc2VsZiwgY29udGFjdHMsIG1lc3NhZ2UpOlxuICAgICAgICBmb3IgYyBpbiBjb250YWN0czpcbiAgICAgICAgICAgIHNlbGYuc2VuZChjLCBtZXNzYWdlKVxuXG5jbGFzcyBFbWFpbE5vdGlmaWVyKE5vdGlmaWVyKTpcbiAgICBkZWYgc2VuZChzZWxmLCBjb250YWN0LCBtZXNzYWdlKTpcbiAgICAgICAgcHJpbnQoZlwiW0VNQUlMXSBUbzoge2NvbnRhY3R9IHwge21lc3NhZ2V9XCIpXG5cbmNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBjb3BpZXM9MSk6XG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZVxuICAgICAgICBzZWxmLmlzYm4gPSBpc2JuXG4gICAgICAgIHNlbGYuX2NvcGllcyA9IGNvcGllc1xuXG4gICAgQHByb3BlcnR5XG4gICAgZGVmIGNvcGllcyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllc1xuXG4gICAgQGNvcGllcy5zZXR0ZXJcbiAgICBkZWYgY29waWVzKHNlbGYsIHZhbHVlKTpcbiAgICAgICAgaWYgdmFsdWUgPCAwOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcImNvcGllcyBjYW5ub3QgYmUgbmVnYXRpdmVcIilcbiAgICAgICAgc2VsZi5fY29waWVzID0gdmFsdWVcblxuICAgIGRlZiBjaGVja19vdXQoc2VsZik6XG4gICAgICAgIGlmIHNlbGYuX2NvcGllcyA8IDE6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIk5vIGNvcGllcyBvZiAne3NlbGYudGl0bGV9JyBhdmFpbGFibGVcIilcbiAgICAgICAgc2VsZi5fY29waWVzIC09IDFcblxuICAgIGRlZiByZXR1cm5fY29weShzZWxmKTpcbiAgICAgICAgc2VsZi5fY29waWVzICs9IDFcblxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIkJvb2soe3NlbGYudGl0bGUhcn0sIGNvcGllcz17c2VsZi5fY29waWVzfSlcIiJ9"
 width="100%"
></iframe>

## Clean Interfaces at a Glance

| Principle | What it looks like in code |
|---|---|
| Expose only what callers need | Keep helpers and internals prefixed with `_` |
| Make misuse hard | Validate in `__init__` and setters, raise on invalid input |
| Keep interfaces narrow | One ABC per responsibility, not one ABC for everything |
| Separate interface from implementation | ABCs define what; concrete classes define how |
| Document the contract | Abstract method docstrings describe what callers can expect |

## Your Turn

Design a clean `PaymentProcessor` ABC and two concrete implementations: `CreditCardProcessor` and `UPIProcessor`. The interface should have one abstract method: `charge(amount, account_id)` that returns `True` on success and `False` on failure. Add a concrete `charge_with_retry(amount, account_id, attempts=3)` method on the ABC that calls `charge` in a loop up to `attempts` times, returning `True` on first success or `False` if all attempts fail. Test both implementations and confirm the retry logic works without modification to either concrete class.

## Conclusion

A clean interface exposes exactly what callers need and nothing more, validates input at every entry point so invalid objects cannot exist, and splits responsibilities into narrow, focused ABCs rather than one sprawling contract. This unit covered the full arc: from the raw `Book` class with an open attribute that anyone could set to a validated, property-controlled object, and from informal duck typing to a formal ABC that catches missing implementations at instantiation time. Unit 3 builds on this foundation by exploring what happens when one class inherits from another: how constructor chains work, how methods override each other, and how multiple classes can share and extend behavior through inheritance.

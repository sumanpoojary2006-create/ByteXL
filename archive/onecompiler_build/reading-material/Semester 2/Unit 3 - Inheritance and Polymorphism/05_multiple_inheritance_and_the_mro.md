## Introduction

Dev needs an `AudioBook` that is simultaneously a `LibraryItem` (with a title and ISBN) and also a `DigitalMedia` object (with a file size and download capability). It is naturally both things at once. Python allows a class to inherit from more than one parent, and this is called **multiple inheritance**.

Multiple inheritance is powerful but introduces a question that simpler inheritance does not have: if both parent classes define the same method, which version does Python use? The answer depends on a rule called the **Method Resolution Order** (MRO), and understanding it prevents a whole category of subtle bugs.

![](images/05_multiple_inheritance_mro.png)

## Multiple Inheritance Syntax

The syntax is straightforward: list both parent classes in the parentheses.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBMaWJyYXJ5SXRlbTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4pOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuXG4gICAgZGVmIGRpc3BsYXlfaW5mbyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIntzZWxmLnRpdGxlfSAoSVNCTjoge3NlbGYuaXNibn0pXCJcblxuY2xhc3MgRGlnaXRhbE1lZGlhOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBmaWxlX3NpemVfbWIpOlxuICAgICAgICBzZWxmLmZpbGVfc2l6ZV9tYiA9IGZpbGVfc2l6ZV9tYlxuXG4gICAgZGVmIGRvd25sb2FkKHNlbGYpOlxuICAgICAgICByZXR1cm4gZlwiRG93bmxvYWRpbmcge3NlbGYuZmlsZV9zaXplX21ifSBNQlwiXG5cbmNsYXNzIEF1ZGlvQm9vayhMaWJyYXJ5SXRlbSwgRGlnaXRhbE1lZGlhKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4sIGZpbGVfc2l6ZV9tYiwgbmFycmF0b3IpOlxuICAgICAgICBMaWJyYXJ5SXRlbS5fX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibilcbiAgICAgICAgRGlnaXRhbE1lZGlhLl9faW5pdF9fKHNlbGYsIGZpbGVfc2l6ZV9tYilcbiAgICAgICAgc2VsZi5uYXJyYXRvciA9IG5hcnJhdG9yXG5cbmFiID0gQXVkaW9Cb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDI1MC41LCBcIlNjb3R0IEJyaWNrXCIpXG5wcmludChhYi5kaXNwbGF5X2luZm8oKSkgICAjIER1bmUgKElTQk46IDk3OC0wNDQxMDEzNTkzKSAtLSBmcm9tIExpYnJhcnlJdGVtXG5wcmludChhYi5kb3dubG9hZCgpKSAgICAgICAjIERvd25sb2FkaW5nIDI1MC41IE1CIC0tIGZyb20gRGlnaXRhbE1lZGlhXG5wcmludChhYi5uYXJyYXRvcikgICAgICAgICAjIFNjb3R0IEJyaWNrIn0"
 width="100%"
></iframe>

Here the two parents have no methods in common, so there is no conflict. The real complexity appears when both parents define the same method name.

## The Diamond Problem and the MRO

The classic conflict in multiple inheritance is called the **diamond problem**. Imagine this hierarchy:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiIgICAgIEJhc2VcbiAgICAvICAgIFxcXG4gIExlZnQgICBSaWdodFxuICAgIFxcICAgIC9cbiAgICAgQ2hpbGQifQ"
 width="100%"
></iframe>

Both `Left` and `Right` inherit from `Base` and override a method. When `Child` calls that method, which version runs: `Left`'s or `Right`'s?

Python's answer is the **Method Resolution Order** (MRO): a deterministic, linearized ordering of the class hierarchy calculated using the **C3 linearization algorithm**. In simple terms, Python checks classes in the order: the class itself, then left-to-right through parents, following a rule that ensures no class appears before another class it inherits from.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJjbGFzcyBCYXNlOlxuICAgIGRlZiBkZXNjcmliZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiQmFzZVwiXG5cbmNsYXNzIExlZnQoQmFzZSk6XG4gICAgZGVmIGRlc2NyaWJlKHNlbGYpOlxuICAgICAgICByZXR1cm4gXCJMZWZ0XCJcblxuY2xhc3MgUmlnaHQoQmFzZSk6XG4gICAgZGVmIGRlc2NyaWJlKHNlbGYpOlxuICAgICAgICByZXR1cm4gXCJSaWdodFwiXG5cbmNsYXNzIENoaWxkKExlZnQsIFJpZ2h0KTpcbiAgICBwYXNzXG5cbmMgPSBDaGlsZCgpXG5wcmludChjLmRlc2NyaWJlKCkpICAgICAgICMgTGVmdCAtLSBmb2xsb3dzIE1STzogQ2hpbGQgLT4gTGVmdCAtPiBSaWdodCAtPiBCYXNlXG5wcmludChDaGlsZC5fX21yb19fKSAgICAgICMgKDxjbGFzcyAnQ2hpbGQnPiwgPGNsYXNzICdMZWZ0Jz4sIDxjbGFzcyAnUmlnaHQnPiwgPGNsYXNzICdCYXNlJz4sIDxjbGFzcyAnb2JqZWN0Jz4pIn0"
 width="100%"
></iframe>

Python found `describe` in `Left` and used it. The MRO tells you the exact order Python searches. You can inspect it any time with `ClassName.__mro__` or `ClassName.mro()`.

## super() Follows the MRO

When you use `super()` in multiple inheritance, Python does not call the direct parent. It calls the *next class in the MRO*. This is how `super()` stays correct in complex hierarchies: each class calls `super()`, Python picks the right next class, and every `__init__` in the chain runs exactly once.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBCYXNlOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgcHJpbnQoXCJCYXNlLl9faW5pdF9fXCIpXG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKVxuXG5jbGFzcyBMZWZ0KEJhc2UpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgcHJpbnQoXCJMZWZ0Ll9faW5pdF9fXCIpXG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKSAgICAjIGdvZXMgdG8gUmlnaHQsIG5vdCBCYXNlXG5cbmNsYXNzIFJpZ2h0KEJhc2UpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgcHJpbnQoXCJSaWdodC5fX2luaXRfX1wiKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKCkgICAgIyBnb2VzIHRvIEJhc2VcblxuY2xhc3MgQ2hpbGQoTGVmdCwgUmlnaHQpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmKTpcbiAgICAgICAgcHJpbnQoXCJDaGlsZC5fX2luaXRfX1wiKVxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKCkgICAgIyBnb2VzIHRvIExlZnRcblxuQ2hpbGQoKVxuIyBDaGlsZC5fX2luaXRfX1xuIyBMZWZ0Ll9faW5pdF9fXG4jIFJpZ2h0Ll9faW5pdF9fXG4jIEJhc2UuX19pbml0X18ifQ"
 width="100%"
></iframe>

Every `__init__` ran exactly once, in MRO order, because each one calls `super()`. If any level skipped `super().__init__()`, everything after it in the MRO would be silently skipped.

## When to Use Multiple Inheritance

Multiple inheritance is appropriate when an object genuinely has two independent, orthogonal roles: a `SearchableMixin`, a `LoggableMixin`, or a `SerializableMixin` that adds behavior orthogonally to a domain class. Mixins, classes that add specific capabilities without being primary base classes, are the most common and well-justified use of multiple inheritance.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBMb2dnYWJsZU1peGluOlxuICAgIGRlZiBsb2coc2VsZiwgbWVzc2FnZSk6XG4gICAgICAgIHByaW50KGZcIlt7c2VsZi5fX2NsYXNzX18uX19uYW1lX199XSB7bWVzc2FnZX1cIilcblxuY2xhc3MgQm9vayhMaWJyYXJ5SXRlbSwgTG9nZ2FibGVNaXhpbik6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBjb3BpZXMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKHRpdGxlLCBpc2JuKVxuICAgICAgICBzZWxmLmNvcGllcyA9IGNvcGllc1xuXG4gICAgZGVmIGNoZWNrX291dChzZWxmKTpcbiAgICAgICAgaWYgc2VsZi5jb3BpZXMgPCAxOlxuICAgICAgICAgICAgc2VsZi5sb2coXCJDaGVja291dCBmYWlsZWQ6IG5vIGNvcGllcyBhdmFpbGFibGVcIilcbiAgICAgICAgICAgIHJldHVybiBGYWxzZVxuICAgICAgICBzZWxmLmNvcGllcyAtPSAxXG4gICAgICAgIHNlbGYubG9nKGZcIkNoZWNrZWQgb3V0LiBSZW1haW5pbmc6IHtzZWxmLmNvcGllc31cIilcbiAgICAgICAgcmV0dXJuIFRydWVcblxuYiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMSlcbmIuY2hlY2tfb3V0KCkgICAjIFtCb29rXSBDaGVja2VkIG91dC4gUmVtYWluaW5nOiAwXG5iLmNoZWNrX291dCgpICAgIyBbQm9va10gQ2hlY2tvdXQgZmFpbGVkOiBubyBjb3BpZXMgYXZhaWxhYmxlIn0"
 width="100%"
></iframe>

## Multiple Inheritance and MRO at a Glance

| Concept | What it means |
|---|---|
| Multiple inheritance | `class Child(A, B):` inherits from both |
| Diamond problem | Same method in two parents; which version runs? |
| MRO | Python's linearized search order; always deterministic |
| `__mro__` | Inspect the resolution order of any class |
| `super()` in MI | Follows the MRO, not just the direct parent |
| Mixins | Common, safe use of multiple inheritance for orthogonal capabilities |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcGxlX2luaGVyaXRhbmNlX2FuZF90aGVfbXJvIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJjbGFzcyBUaW1lc3RhbXBNaXhpbjpcbiAgICBkZWYgY3JlYXRlZF9hdF9sYWJlbChzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiQ3JlYXRlZDogMjAyNC0wMS0wMVwiICAgIyBzaW1wbGlmaWVkXG5cbmNsYXNzIFRhZ2dhYmxlTWl4aW46XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLnRhZ3MgPSBbXVxuXG4gICAgZGVmIGFkZF90YWcoc2VsZiwgdGFnKTpcbiAgICAgICAgc2VsZi50YWdzLmFwcGVuZCh0YWcpXG5cbiAgICBkZWYgdGFnX2xpc3Qoc2VsZik6XG4gICAgICAgIHJldHVybiBcIiwgXCIuam9pbihzZWxmLnRhZ3MpXG5cbmNsYXNzIEFydGljbGUoVGltZXN0YW1wTWl4aW4sIFRhZ2dhYmxlTWl4aW4pOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSk6XG4gICAgICAgIHN1cGVyKCkuX19pbml0X18oKSAgICMgdHJpZ2dlcnMgVGFnZ2FibGVNaXhpbi5fX2luaXRfXyB2aWEgTVJPXG4gICAgICAgIHNlbGYudGl0bGUgPSB0aXRsZSJ9"
 width="100%"
></iframe>

Create an `Article`, add two tags, and print `created_at_label()`, `tag_list()`, and `Article.__mro__`. Then explain in your own words why calling `super().__init__()` in `Article` rather than `TaggableMixin.__init__(self)` directly is the correct approach when using mixins.

## Conclusion

Multiple inheritance lets a class inherit from two or more parents. When method names collide, Python resolves the conflict using the Method Resolution Order (MRO), a deterministic linearization visible via `ClassName.__mro__`. Using `super()` at every level of a multiple-inheritance hierarchy ensures all `__init__` methods run exactly once. The cleanest and most common use of multiple inheritance is mixin classes, which add specific capabilities orthogonally to a main domain class. The next lesson asks a harder design question: when is inheritance the wrong tool, and when should you use composition instead?

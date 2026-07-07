## Introduction

Meera is writing the bio for her page, and she wants it laid out nicely: the greeting on its own line, the next line indented a little, and a short quoted phrase from a happy customer included with its quotation marks intact. She presses Enter to drop text onto a new line and Tab to indent, and types the quote carefully so the quotation marks sit inside the text without ending it early. How do you put a line break inside a string, when pressing Enter would just end your line of code? How do you include a quotation mark when quotes already mark the start and end of the string? Python solves these with escape sequences, special codes that begin with a backslash, and with triple-quoted strings for text that spans many lines. These are the tools for shaping how text is laid out. Formatting in the last lesson controlled how a single value looked; this lesson controls the structure of the text around it, the line breaks, the indents, and the quote marks Meera needs sitting safely inside her bio.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/08_escape_multiline.png)

## The Backslash and Escape Sequences

Inside a string, a backslash gives the next character a special meaning. The most useful escape sequences are a small handful worth memorising.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2VzY2FwZV9zZXF1ZW5jZXNfYW5kX211bHRpbGluZV9zdHJpbmdzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwcmludChcIkxpbmUgb25lXFxuTGluZSB0d29cIilcbnByaW50KFwiTmFtZTpcXHRBc2hhXCIpXG5wcmludChcIlNoZSBzYWlkIFxcXCJoZWxsb1xcXCJcIilcbnByaW50KFwiQSBiYWNrc2xhc2g6IFxcXFxcIikifQ"
 width="100%"
></iframe>

Here `\n` inserts a new line, so "Line one" and "Line two" print on separate lines. `\t` inserts a tab, useful for spacing out columns. `\"` lets you place a double quote inside a double-quoted string without ending it. And because the backslash is special, `\\` is how you print a single literal backslash.

## Multi-line Strings With Triple Quotes

When you have several lines of text, peppering them with `\n` gets ugly. Triple quotes, either three double quotes or three single quotes, let you write text exactly as it should appear, line breaks and all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2VzY2FwZV9zZXF1ZW5jZXNfYW5kX211bHRpbGluZV9zdHJpbmdzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJtZXNzYWdlID0gXCJcIlwiRGVhciBzdHVkZW50LFxuXG5XZWxjb21lIHRvIHRoZSBQeXRob24gY291cnNlLlxuV2UgaG9wZSB5b3UgZW5qb3kgaXQuXG5cblJlZ2FyZHMsXG5UaGUgVGVhbVwiXCJcIlxucHJpbnQobWVzc2FnZSkifQ"
 width="100%"
></iframe>

Everything between the triple quotes is preserved, including the blank lines, so the layout you type is the layout you get. This is perfect for emails, reports, and any block of formatted text, and for exactly the kind of multi-line bio Meera wanted to write without littering it with `\n` after every sentence.

## Raw Strings, Briefly

Occasionally the backslash gets in your way, for example in a Windows file path like "C:\new\table", where `\n` and `\t` would be misread as escape codes. Putting the letter `r` before the string turns off escaping, treating every backslash literally.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2VzY2FwZV9zZXF1ZW5jZXNfYW5kX211bHRpbGluZV9zdHJpbmdzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJwYXRoID0gclwiQzpcXG5ld1xcdGFibGVcIlxucHJpbnQocGF0aCkgICAgIyBDOlxcbmV3XFx0YWJsZSJ9"
 width="100%"
></iframe>

You will meet raw strings again in a later semester when you study pattern matching, where they are especially handy.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/08_raw_string_backslash.png)


## Escape Sequences at a Glance

| Sequence | Meaning | Example |
|---|---|---|
| `\n` | New line | `"a\nb"` prints as two lines |
| `\t` | Tab | `"a\tb"` inserts a tab between a and b |
| `\"` | A literal double quote inside a double-quoted string | `"She said \"hi\""` |
| `\\` | A literal backslash | `"\\"` prints as `\` |
| `r"..."` | Raw string, every backslash taken literally | `r"C:\new"` prints as `C:\new` |
| `"""..."""` | Triple-quoted, multi-line text exactly as typed | Preserves every line break and blank line |

## Your Turn: A Formatted Receipt

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2VzY2FwZV9zZXF1ZW5jZXNfYW5kX211bHRpbGluZV9zdHJpbmdzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJzaG9wID0gaW5wdXQoXCJTaG9wIG5hbWU6IFwiKVxuaXRlbSA9IGlucHV0KFwiSXRlbTogXCIpXG5wcmljZSA9IGlucHV0KFwiUHJpY2U6IFwiKVxucHJpbnQoZlwie3Nob3B9XFxuLS0tLS0tLS0tLS0tLS0tLS0tLS1cXG5JdGVtOlxcdHtpdGVtfVxcblByaWNlOlxcdHtwcmljZX1cIikifQ"
 width="100%"
></iframe>

Run it and watch the `\n` codes break the output into separate lines and the `\t` codes align the labels. You built a small, tidy receipt purely by controlling where the line breaks and tabs fall.

## Conclusion

Escape sequences are backslash codes that shape text, with `\n` for a new line, `\t` for a tab, `\"` for a quote inside quotes, and `\\` for a literal backslash. Triple-quoted strings let you write multi-line text exactly as it should appear, and a raw string with an `r` prefix turns escaping off when you need backslashes taken literally. With these, you control not just what your text says but how it is laid out on the screen. Every tool in this unit, from indexing to formatting to layout, finally comes together in the last lesson, where Meera puts the whole toolkit to work cleaning up a real inbox of messy entries.

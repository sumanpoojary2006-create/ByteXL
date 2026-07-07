## Introduction

Asel types `python app.py` and her script runs. She has done this hundreds of times without thinking twice about it. But Rahul's question from the previous lesson is still sitting with her: what is actually happening in those few milliseconds between the command and the first line of output?

The answer involves a piece of software called an **interpreter**, and understanding it changes the way you read error messages, think about performance, and reason about code that behaves in unexpected ways. This lesson pulls back the curtain.

![](images/02_interpreter_pipeline.png)

## Python Is Not Compiled the Way C Is

When you run a C program, a compiler translates your source code into machine instructions once, producing a binary that the CPU executes directly. Python works differently: a program called the **interpreter** reads your source file, translates it internally, and executes it, all in one process, every time you run it.

The most widely used Python interpreter is called **CPython** (it is written in C), and it is almost certainly what you have installed. There are others, such as PyPy and Jython, but CPython is the reference implementation and the one this unit focuses on.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2hvd19weXRob25fcnVuc195b3VyX2NvZGVfdGhlX2ludGVycHJldGVyIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5wcmludChzeXMuaW1wbGVtZW50YXRpb24ubmFtZSkgICAjIGNweXRob25cbnByaW50KHN5cy52ZXJzaW9uKSAgICAgICAgICAgICAgICAjIDMueC54IC4uLiJ9"
 width="100%"
></iframe>

Understanding that CPython is a piece of software, not an abstract thing called "Python," clarifies a lot of confusion. When people say "Python is slow" they usually mean CPython's interpreter loop is slower than native machine code for certain workloads. The language itself does not have a speed; its implementations do.

## The Four Stages Inside the Interpreter

When CPython runs `python app.py`, it works through four stages before any of your logic executes:

**1. Lexing** (tokenization) reads your source file character by character and groups characters into meaningful tokens: keywords like `def`, names like `my_function`, operators like `+`, and literals like `"hello"`.

**2. Parsing** takes those tokens and builds an **Abstract Syntax Tree** (AST), a tree-shaped data structure that represents the grammatical structure of your program. At this stage Python catches `SyntaxError`.

**3. Compilation** walks the AST and produces **bytecode**, a compact sequence of simple instructions designed for CPython's virtual machine to execute efficiently. This step is fast and happens automatically; you never call it manually.

**4. Execution** runs the bytecode instruction by instruction in CPython's evaluation loop. This is the stage where your variables are created, your functions are called, and your `print()` output appears.

## Inspecting the AST

Python exposes its own AST through the `ast` module. You can parse a string of source code and print the tree:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2hvd19weXRob25fcnVuc195b3VyX2NvZGVfdGhlX2ludGVycHJldGVyIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgYXN0XG5cbnNvdXJjZSA9IFwieCA9IDEgKyAyXCJcbnRyZWUgPSBhc3QucGFyc2Uoc291cmNlKVxucHJpbnQoYXN0LmR1bXAodHJlZSwgaW5kZW50PTIpKSJ9"
 width="100%"
></iframe>

The output is verbose but readable: you can see a `Module` containing an `Assign` node, which holds a `BinOp` (binary operation) adding two `Constant` nodes. This is the exact data structure CPython's compiler receives as input. You will rarely work with it directly, but knowing it exists explains how tools like linters, formatters, and IDEs understand your code without running it.

## Why This Matters in Practice

Understanding the interpreter's pipeline gives you three practical advantages.

First, SyntaxError is caught at the *parse* stage, before any code runs. That is why an error on line 50 stops even line 1 from executing: the file is parsed in full before execution begins.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2hvd19weXRob25fcnVuc195b3VyX2NvZGVfdGhlX2ludGVycHJldGVyIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIFRoaXMgZmlsZSB3b3VsZCBmYWlsIGVudGlyZWx5IGF0IHBhcnNlIHRpbWU6XG4jIGRlZiBicm9rZW4oOiAgICAjIFN5bnRheEVycm9yXG4jICAgICBwYXNzIn0"
 width="100%"
></iframe>

Second, NameError and TypeError are runtime errors caught during *execution*. The interpreter did not know the problem existed until it reached that instruction.

Third, certain optimizations (like constant folding) happen at compile time. Python computes `1 + 2` as `3` at compile time rather than adding at runtime, which is why simple arithmetic in tight loops is faster than it looks.

## The Interpreter at a Glance

| Stage | Input | Output | Where errors appear |
|---|---|---|---|
| Lexing | Source characters | Token stream | (rarely surfaces directly) |
| Parsing | Tokens | Abstract Syntax Tree | `SyntaxError` |
| Compilation | AST | Bytecode | (rarely surfaces directly) |
| Execution | Bytecode | Program output | `NameError`, `TypeError`, etc. |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2hvd19weXRob25fcnVuc195b3VyX2NvZGVfdGhlX2ludGVycHJldGVyIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgYXN0XG5cbnNvdXJjZSA9IFwiXCJcIlxuZGVmIGFkZChhLCBiKTpcbiAgICByZXR1cm4gYSArIGJcblxucmVzdWx0ID0gYWRkKDMsIDQpXG5cIlwiXCJcblxudHJlZSA9IGFzdC5wYXJzZShzb3VyY2UpXG5wcmludChhc3QuZHVtcCh0cmVlLCBpbmRlbnQ9MikpIn0"
 width="100%"
></iframe>

Run this and identify in the output: the `FunctionDef` node for `add`, and the `Call` node for `add(3, 4)`. Then change `add(3, 4)` to `add(3, "hello")` and note that the AST is identical: there is no type error at parse time because Python types are only known at execution.

## Conclusion

Every Python script travels through lexing, parsing, compilation, and execution before producing a single line of output. SyntaxErrors appear early; runtime errors appear only when execution reaches the problematic instruction. The compilation stage produces bytecode, not machine code, and that bytecode is the actual language CPython runs. The next lesson goes deeper into bytecode itself, showing what those instructions look like and how you can read them with a built-in module called `dis`.

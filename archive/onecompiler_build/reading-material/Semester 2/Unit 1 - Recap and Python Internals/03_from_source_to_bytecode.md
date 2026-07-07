## Introduction

Asel spent ten minutes staring at the output of `ast.dump()` from the last lesson, and she finds it genuinely fascinating. But Rahul tells her the AST is only a halfway point. After the AST comes a translation step that produces something much closer to what actually runs, something called **bytecode**, and it turns out Python lets you read it.

This lesson cracks open bytecode with Python's `dis` module (short for "disassembler"), which shows exactly what instructions CPython executes for any function or block of code. Reading bytecode is not something you will do every day, but doing it once changes how precisely you think about what Python is doing on your behalf.

![](images/03_source_to_bytecode_pipeline.png)

## What Bytecode Actually Is

Bytecode is a compact, portable sequence of simple instructions designed for CPython's virtual machine to execute efficiently. It is not machine code (x86, ARM, or otherwise); it is an intermediate format understood only by CPython's internal evaluation loop. This is intentional: the same `.pyc` file runs on any operating system because bytecode is platform-neutral, and CPython handles the platform-specific work underneath.

Each instruction is one byte for the operation code (opcode) plus one byte for an argument. Because opcodes are simple and fixed-size, CPython's evaluation loop can run through them quickly, which is most of what determines Python's execution speed.

## Reading Bytecode with dis

The `dis` module disassembles any function into human-readable bytecode:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgZGlzXG5cbmRlZiBhZGQoYSwgYik6XG4gICAgcmV0dXJuIGEgKyBiXG5cbmRpcy5kaXMoYWRkKSJ9"
 width="100%"
></iframe>

The output looks like:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiIgIDIgICAgICAgICAgIDAgUkVTVU1FICAgICAgICAgICAgICAgICAgIDBcblxuICAzICAgICAgICAgICAyIExPQURfRkFTVCAgICAgICAgICAgICAgICAwIChhKVxuICAgICAgICAgICAgICA0IExPQURfRkFTVCAgICAgICAgICAgICAgICAxIChiKVxuICAgICAgICAgICAgICA2IEJJTkFSWV9PUCAgICAgICAgICAgICAgIDAgKCspXG4gICAgICAgICAgICAgMTAgUkVUVVJOX1ZBTFVFIn0"
 width="100%"
></iframe>

Read each line as: *offset in bytes* | *source line number* | *opcode* | *argument*. `LOAD_FAST` pushes a local variable onto a small internal stack. `BINARY_OP` pops two values, adds them, and pushes the result. `RETURN_VALUE` pops the top of the stack and returns it to the caller.

## A Slightly Richer Example

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgZGlzXG5cbmRlZiBncmVldChuYW1lKTpcbiAgICBtZXNzYWdlID0gXCJIZWxsbywgXCIgKyBuYW1lXG4gICAgcmV0dXJuIG1lc3NhZ2VcblxuZGlzLmRpcyhncmVldCkifQ"
 width="100%"
></iframe>

Now you see a `STORE_FAST` instruction for the local variable `message`, and a `LOAD_CONST` for the string literal `"Hello, "`. Constants known at compile time are stored in the function's `co_consts` tuple and loaded by index rather than looked up by name, which makes them slightly faster than variables.

You can inspect these code-object attributes directly:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJwcmludChncmVldC5fX2NvZGVfXy5jb19jb25zdHMpICAgICMgKCdIZWxsbywgJywpIC0tIHRoZSBzdHJpbmcgbGl0ZXJhbFxucHJpbnQoZ3JlZXQuX19jb2RlX18uY29fdmFybmFtZXMpICAjICgnbmFtZScsICdtZXNzYWdlJykgLS0gbG9jYWwgdmFyaWFibGUgbmFtZXMifQ"
 width="100%"
></iframe>

These attributes live on every function's `__code__` object, which is the compiled bytecode container Python creates when it processes a `def` statement.

## Constant Folding: One Compile-Time Optimization

CPython can compute certain expressions at compile time rather than at runtime. This is called **constant folding**.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgZGlzXG5cbmRlZiBleHBlbnNpdmVfbG9va2luZygpOlxuICAgIHJldHVybiA2MCAqIDYwICogMjQgKiA3ICAgICMgb25lIHdlZWsgaW4gc2Vjb25kc1xuXG5kaXMuZGlzKGV4cGVuc2l2ZV9sb29raW5nKSJ9"
 width="100%"
></iframe>

Instead of seeing three `BINARY_OP` instructions at runtime, you see a single `LOAD_CONST` with the precomputed result `604800`. Python recognized that all operands are known constants, computed the result during compilation, and stored only the answer. The runtime never performs the multiplication.

This is a small but real optimization, and it illustrates the general principle: the compiler is not just translating, it is also doing useful work.

## What the dis Module Reveals About Your Code

Reading bytecode is most useful for three things. First, verifying that an optimization you wrote actually matters: if two versions of a function produce identical bytecode, any performance difference you measure is noise, not signal. Second, understanding why certain patterns have the overhead they do: a list comprehension has a `BUILD_LIST` and an inner loop in bytecode, which makes it easy to see it is not free. Third, satisfying curiosity when Python does something surprising and you cannot figure out why from the source code alone.

## Bytecode at a Glance

| Concept | What it is |
|---|---|
| Bytecode | Platform-neutral instructions for CPython's virtual machine |
| Opcode | A one-byte code naming a simple operation (LOAD, STORE, BINARY_OP...) |
| `dis.dis()` | Disassembles any function or code block into readable bytecode |
| `__code__` | The code object on every function; holds bytecode, constants, variable names |
| Constant folding | Compiler precomputes expressions whose operands are all constants |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2Zyb21fc291cmNlX3RvX2J5dGVjb2RlIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgZGlzXG5cbmRlZiB3aXRoX2xvb3AoaXRlbXMpOlxuICAgIHRvdGFsID0gMFxuICAgIGZvciBpdGVtIGluIGl0ZW1zOlxuICAgICAgICB0b3RhbCArPSBpdGVtXG4gICAgcmV0dXJuIHRvdGFsXG5cbmRlZiB3aXRoX3N1bShpdGVtcyk6XG4gICAgcmV0dXJuIHN1bShpdGVtcylcblxuZGlzLmRpcyh3aXRoX2xvb3ApXG5wcmludChcIi0tLVwiKVxuZGlzLmRpcyh3aXRoX3N1bSkifQ"
 width="100%"
></iframe>

Run this and count the number of instructions each version produces. Then explain in one sentence why `with_sum` has fewer bytecode instructions: the work has moved into a built-in C function (`sum`) rather than being expressed as explicit Python loop opcodes.

## Conclusion

Python compiles your source code into bytecode at the compilation stage, and that bytecode is what CPython actually runs. The `dis` module lets you read it, revealing optimizations like constant folding and showing exactly how much work each Python expression becomes at the instruction level. The next lesson covers what Python does with this bytecode after compilation: whether it is reused from a cache or recompiled fresh, and where that cache lives.

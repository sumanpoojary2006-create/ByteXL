## Introduction

You have learned what programming is, how to think in steps, and why Python is a great first language. There is only one thing left before you are officially a programmer: actually getting Python onto a computer and making it do something. This is the moment the idea stops being theory and becomes real.

But first, a small story that explains a choice you will make constantly.

## Two Doors Into the Same Language

Imagine you have a quick, throwaway question: what is 1234 times 5678? You do not want to create a file, name it, and save it. You just want the answer now. For that, you open Python's interactive shell, called the **REPL**, type the calculation, and the answer appears instantly.

Now imagine something different: a fee calculator you will want to run again next week, and the week after. You do not want to retype it every time. For that, you write your instructions in a **script file**, a saved file you can run whenever you like.

Same Python, two different doors.

| Tool | Best For | Is It Saved? |
|---|---|---|
| REPL | A quick, throwaway question you want answered right now | No, it disappears once you close it |
| Script file | Anything you will want to run again, today or next month | Yes, saved to a file you can reopen and rerun |

Knowing which door to open for the moment is a small but genuinely professional habit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t2hky6v/09_repl_vs_script_doors.png)

## What You Actually Need

Setting up need not be intimidating. Three pieces, and you are ready:

- **The Python interpreter**, the program that runs your code. Install Python version 3 (3.10 or newer) from python.org.
- **A place to write code.** Thonny is perfect for beginners because it is simple and includes a visual debugger. VS Code and PyCharm are professional editors you can grow into later.
- **A way to run it**, which is the REPL for quick tries, or a Run button for scripts.

And if even installing feels like too much on day one, there is a shortcut. Browser based runners let you write and run real Python instantly, with nothing to install. Start there if you like, and set up your own machine once the ideas feel comfortable.

## Your First Real Program

Let us write something small. Type these three lines and run them:

```python
name = "Asha"
print("Hello,", name)
print("Welcome to Python!")
```

Run it, and the program greets Asha by name. The first line stores some text in a place called `name`, and `print` shows messages on screen. Change "Asha" to your own name and run it again. You have just written and run a real Python program.

## Making It Respond to You

That program always greets the same fixed name, because the name is written directly into the code. A small change makes it greet whoever runs it instead:

```python
name = input("What is your name? ")
print("Hello,", name)
print("Welcome to Python!")
```

Now the program pauses and waits for you. Type your own name, press Enter, and it greets you by name. The `input` part collects something typed by whoever is running the program. One thing worth filing away for later: whatever you type into `input`, Python always hands it back as plain text, even if you type a number. The next unit, on data types, shows you why that small fact matters and how to convert that text into a real number when you need to calculate with it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t2hky6v/09_input_waits_for_you.png)

## A Question That Reveals How Code Really Runs

Here is a deceptively simple puzzle. Look at these three lines and ask yourself: which one shows nothing at all on the screen?

```python
print("Welcome!")
score = 10 + 5
print("Your score is", score)
```

The first line prints "Welcome!". The third prints "Your score is 15". But the middle line, where score is set to 10 plus 5, displays nothing.

Why? Because storing a value is processing, not output. The computer dutifully works out 15 and remembers it, but it has no reason to announce it. Only `print` puts something on screen. Understanding this early saves you from a classic beginner panic, "my program ran but I see nothing", which almost always means there was no `print`.

## The Little Mistakes Everyone Makes First

Your first errors are coming, and that is completely normal.

| Mistake | What You'll See | The Fix |
|---|---|---|
| Forgetting quotes around text | Python treats your words as a command, not a message | Wrap text in quotes: `"like this"` |
| A missing bracket or quotation mark | The line simply will not run | Check that every opening symbol has a matching closing one |
| Expecting the REPL to save your work | Your code is gone once you close it | Use a saved script for anything you want to keep |
| Using the wrong command for your system | "command not found" in the terminal | Try `python3` if plain `python` does not work |
| A stray space at the start of a normal line | Python reports an indentation error | Remove leading spaces unless you intend a block |

None of these mean you are bad at this. They mean you are a programmer now, reading error messages like everyone else.

## Conclusion

You are no longer someone who has only read about code. You have run it. Reach for the REPL when you want a quick, throwaway answer, and a saved script when you want to keep and reuse a program. Lean on `print` as your window into what your code is doing, and remember that `input` always hands you back text, a detail the next unit builds on directly. Treat each error message as a clue rather than a verdict. With Python set up and your first interactive program working, you are ready to start learning the language itself, beginning with data types and operators in the next unit.

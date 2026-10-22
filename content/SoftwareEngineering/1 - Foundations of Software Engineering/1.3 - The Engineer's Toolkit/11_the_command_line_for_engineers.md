## Introduction

Three weeks into the job, Ananya's phone buzzed during lunch. Students were reporting failed payments. Vikram sent her a short message: "Log into the staging server and tell me how many payment failures happened today."

She connected to the server and found a black screen with a blinking cursor. There were no windows, no icons, and no mouse pointer. She did know one thing, which was that the answer was in a log file, a plain text file in which the application records everything it does. She just did not know how to look inside it, let alone count the failures in a file with thousands of lines.

That afternoon Vikram taught her the commands below. By evening she could answer the question in a single line. The command line stops looking intimidating once you realise it is a small vocabulary of commands that can be combined.

**Definition:** The command line is a text interface to the operating system in which you type commands, each doing one small job, and combine them with pipes and redirection to automate tasks and work on machines that have no graphical interface.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_the_command_line_for_engineers.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya faces a dark terminal window with a blinking cursor while a stream of glowing log lines flows past, and Vikram points to a short pipeline of three connected command blocks.

ON-IMAGE TEXT: show a short bold title "The Command Line for Engineers" plus only these few labels, large and legible: Terminal, Logs, Pipes. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Engineers Use the Command Line

- **Servers usually have no graphical interface**, so the terminal is the only way in.
- **It is fast and repeatable.** A command typed once can be saved in a script and run a thousand times.
- **Tools are built for it.** Git, package managers, test runners, and containers are all driven from the command line.
- **Commands combine.** The output of one command can feed another, so small tools become powerful together.

## Moving Around and Managing Files

```bash
pwd                      # print the current directory
ls                       # list files here
ls -l                    # list with sizes and dates
cd projects              # move into the directory called projects
cd ..                    # move up one directory
mkdir notes              # make a new directory
touch todo.txt           # create an empty file
cp todo.txt backup.txt   # copy a file
mv backup.txt old.txt    # move or rename a file
rm old.txt               # delete a file (there is no recycle bin)
```

Be careful with `rm`: it deletes immediately and permanently. Always check the file name before pressing Enter.

## Looking Inside Files

```bash
cat app.log              # print the whole file
head -n 3 app.log        # first 3 lines
tail -n 3 app.log        # last 3 lines
tail -f app.log          # keep showing new lines as they arrive (Ctrl+C to stop)
less app.log             # scroll through a long file (press q to quit)
```

## Searching and Counting

Suppose `app.log` contains these six lines:

```text
2026-03-02 12:01:10 INFO order placed id=101
2026-03-02 12:01:14 ERROR payment failed id=101
2026-03-02 12:02:03 INFO order placed id=102
2026-03-02 12:02:09 INFO payment ok id=102
2026-03-02 12:03:40 ERROR payment failed id=103
2026-03-02 12:04:55 ERROR menu timeout
```

```bash
grep "payment failed" app.log        # show only matching lines
grep -c ERROR app.log                # count matching lines (prints 3)
wc -l app.log                        # count lines in the file (prints 6 app.log)
```

## Pipes: Connecting Commands

The pipe symbol `|` sends the output of one command into the next. This is the single most useful idea on the command line, because it lets you build answers from small steps.

```bash
grep "payment failed" app.log | wc -l
```

`grep` selects the matching lines, and `wc -l` counts them. The result is `2`, which is exactly the answer Ananya needed. A longer example counts how many log lines there are at each severity level:

```bash
cut -d' ' -f3 app.log | sort | uniq -c
```

`cut` takes the third space-separated column (the level), `sort` groups identical values, and `uniq -c` counts each group. The output is:

```text
      3 ERROR
      3 INFO
```

<!--
IMAGE PROMPT  ->  generate as images/02_pipe_pipeline.png   (16:9 explanatory diagram, place here)

A horizontal pipeline of three glowing pipe segments: app.log (file icon) flowing into grep payment failed (filter funnel), then into wc -l (counter), ending in a large number 2.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Redirection: Saving Output

```bash
grep ERROR app.log > errors.txt       # write matches to a file (overwrites)
echo "checked at noon" >> notes.txt   # append to the end of a file
```

## Getting Help

```bash
grep --help        # a short summary of options
man grep           # the full manual page (press q to quit)
```

Experienced engineers look things up constantly. Knowing that a command exists and how to read its manual matters far more than memorising every option.

## Your Turn: Write the Command

Using the six-line `app.log` above, write a command for each task and predict its output.

1. Show only the lines containing the word `ERROR`.
2. Count how many lines contain `order placed`.
3. Save the lines containing `id=101` into a file named `order101.txt`.

For task 1, `grep ERROR app.log` prints the three error lines. For task 2, `grep "order placed" app.log | wc -l` prints `2`. For task 3, `grep "id=101" app.log > order101.txt` creates the file with two lines, and prints nothing on screen because the output was redirected.

## Conclusion

The command line is a text interface to the operating system in which you type commands, each doing one small job, and combine them with pipes and redirection to automate tasks and work on machines that have no graphical interface. A small vocabulary goes a long way.

Ananya could now find the answer to Vikram's question, but finding that payments failed leads straight to the next challenge: working out why. For that she will have to read code she did not write, which is the subject of the final lesson of this unit.

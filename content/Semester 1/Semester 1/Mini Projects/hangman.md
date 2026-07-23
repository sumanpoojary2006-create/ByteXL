## Background

Hangman is a word-guessing game where the player guesses letters one at a time to reveal a hidden word. Guess too many wrong letters and you lose. It is a classic game that exercises string indexing, list tracking, and loop control — and it is satisfying to build because the result is something you can actually play.

## What You Will Build

A CLI Hangman game where the program picks a random word and the player guesses letters. The player gets 6 wrong guesses before losing.

## Learning Objectives

By the end of this project, you will be able to:
- Index and rebuild strings to show revealed vs. hidden letters
- Track guessed letters in a collection and test membership
- Control a game loop bounded by a wrong-guess budget
- Validate single-character alphabetic input

**Difficulty:** Intermediate · **Estimated time:** 2 hours

## Tasks

### Task 1: The Hidden Word

1. Create a list of at least 15 words — choose any theme you like (animals, cities, programming terms, cricket players).
2. Pick one word randomly using `random.choice()`.
3. Display the word as underscores, one per letter:
   ```
   Word: _ _ _ _ _ _
   ```
4. When the player guesses a correct letter, reveal it in the right position(s). Keep underscores for unguessed letters.

### Task 2: The Game Loop

1. Give the player 6 wrong guesses. In each turn:
   - Show the current state of the word
   - Show which letters have been guessed already
   - Show how many wrong guesses remain
   - Ask for a letter

2. If the guessed letter is in the word, reveal it. If not, subtract one wrong guess.

3. The game ends when:
   - The player reveals all letters (win), or
   - The player runs out of wrong guesses (lose — reveal the full word)

### Task 3: Input Validation

1. If the player enters more than one character, ask again.
2. If the player enters a letter they have already guessed, tell them and ask again — do not count it as a wrong guess.
3. If the player enters a number or symbol, ask again.

## Sample Run

```
===== Hangman =====
Word: _ _ _ _ _ _
Guessed: (none)
Wrong guesses left: 6
Guess a letter: p
Good guess!

Word: p _ _ _ _ _
Guessed: p
Wrong guesses left: 6
Guess a letter: z
Nope — 'z' is not in the word.

Word: p _ _ _ _ _
Guessed: p, z
Wrong guesses left: 5
Guess a letter: 3
Please enter a single letter (a–z).
...
You won! The word was: python
```

**Answer these questions after completing all tasks:**
- You store guessed letters in a list. When the player guesses a letter, how do you check if it is already in the list? Would a set work better here — why or why not?
- Your word display shows underscores and revealed letters. Walk through your code for the word "python" when the player has guessed "p" and "t" — what does the display show, and does your code produce it correctly?
- What happens when the word contains a repeated letter like "apple"? If the player guesses "p", do both p's get revealed at once? Test this case.

## Deliverables & Rubric

Submit your `.py` file along with written answers to the reflection questions above.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Word masking and correct reveal of guessed letters (incl. repeats) | 4 |
| Game loop with wrong-guess budget and win/lose detection | 2 |
| Input validation (length, already-guessed, non-letters) | 2 |
| Code readability & organization | 1 |
| Reflection questions answered thoughtfully | 1 |
| **Total** | **10** |

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)

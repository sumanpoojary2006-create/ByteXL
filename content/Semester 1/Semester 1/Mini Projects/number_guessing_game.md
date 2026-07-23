## Background

The computer picks a random number and you have to guess it. Simple idea — but building it correctly requires you to handle user input, branching logic, and loop control together for the first time. This project is your first complete Python program that does something interactive.

## What You Will Build

A CLI game where the computer picks a secret number between 1 and 100 and the player has 7 attempts to guess it. After each guess, the game says whether the guess is too high, too low, or correct.

## Learning Objectives

By the end of this project, you will be able to:
- Generate a secret value with `random.randint()`
- Combine a loop with `if`/`elif`/`else` to drive interactive branching
- Validate user input and reject bad values without consuming an attempt
- Structure a replayable game with an outer play-again loop

**Difficulty:** Beginner · **Estimated time:** 1–1.5 hours

## Tasks

### Task 1: The Basic Game

1. Use `random.randint(1, 100)` to pick a secret number at the start of the game.
2. Give the player 7 attempts. In each attempt:
   - Ask the player to enter a guess
   - Tell them if the guess is too high, too low, or correct
   - Show how many attempts remain
3. If the player guesses correctly, congratulate them and show how many attempts they used.
4. If all 7 attempts are used up without a correct guess, reveal the secret number.

### Task 2: Input Validation

1. If the player enters something that is not a number, display an error message and ask again. Do not count it as an attempt.
2. If the player enters a number outside 1–100, tell them the valid range and ask again. Do not count it as an attempt.

### Task 3: Play Again

1. After the game ends, ask the player: "Play again? (yes/no)"
2. If yes, start a new game with a new random number.
3. If no, say goodbye and exit.

## Sample Run

```
===== Number Guessing Game =====
I'm thinking of a number between 1 and 100.
You have 7 attempts.

Attempt 1/7 — Enter your guess: 50
Too high! Attempts remaining: 6
Attempt 2/7 — Enter your guess: abc
That's not a number. Try again.
Attempt 2/7 — Enter your guess: 25
Too low! Attempts remaining: 5
Attempt 3/7 — Enter your guess: 37
Correct! You got it in 3 attempts.

Play again? (yes/no): no
Goodbye!
```

**Answer these questions after completing all tasks:**
- What happens if the player enters "abc" instead of a number? Did your program crash the first time you tried this, and what did you add to fix it?
- If the player types "YES" or "Yes" instead of "yes" for the play again prompt, does your program handle it? Fix it if not.
- Try playing the game yourself. With 7 attempts, is it easy or hard to guess a number between 1 and 100? What strategy did you use?

## Deliverables & Rubric

Submit your `.py` file along with written answers to the reflection questions above.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Core game works: secret number, 7 attempts, high/low/correct feedback | 4 |
| Play-again loop starts a fresh game correctly | 2 |
| Input validation (non-numbers and out-of-range) without wasting an attempt | 2 |
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

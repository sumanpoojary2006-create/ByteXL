# Mini Project 1: Number Guessing Game

## Background

The computer picks a random number and you have to guess it. Simple idea — but building it correctly requires you to handle user input, branching logic, and loop control together for the first time. This project is your first complete Python program that does something interactive.

## What You Will Build

A CLI game where the computer picks a secret number between 1 and 100 and the player has 7 attempts to guess it. After each guess, the game says whether the guess is too high, too low, or correct.

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

**Answer these questions after completing all tasks:**
- What happens if the player enters "abc" instead of a number? Did your program crash the first time you tried this, and what did you add to fix it?
- If the player types "YES" or "Yes" instead of "yes" for the play again prompt, does your program handle it? Fix it if not.
- Try playing the game yourself. With 7 attempts, is it easy or hard to guess a number between 1 and 100? What strategy did you use?

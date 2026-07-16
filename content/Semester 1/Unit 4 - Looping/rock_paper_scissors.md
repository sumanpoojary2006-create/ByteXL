# Mini Project 2: Rock, Paper & Scissors

## Background

Rock, Paper & Scissors is a classic two-player game — except here, one of the players is your program. The computer picks randomly, you pick by typing, and the program decides who wins. It sounds simple, but getting the win logic right and keeping score across multiple rounds is a good exercise in loops and conditions.

## What You Will Build

A CLI game where the player competes against the computer in Rock, Paper & Scissors. The game runs for multiple rounds, keeps score, and announces the overall winner at the end.

## Tasks

### Task 1: One Round

1. Ask the player to enter their choice: Rock, Paper, or Scissors.
2. Use `random.choice()` to pick the computer's choice.
3. Display both choices.
4. Decide and display the round result — who won, or if it was a draw.

### Task 2: Multiple Rounds

1. Ask the player how many rounds they want to play (e.g. best of 3, best of 5).
2. Loop through that many rounds, showing the score after each one.
3. At the end, display the final score and announce the overall winner.

   Example after 3 rounds:
   ```
   Final Score — You: 2 | Computer: 1
   You win the game!
   ```

### Task 3: Input Validation

1. If the player enters anything other than Rock, Paper, or Scissors, tell them the valid options and ask again.
2. Make the input case-insensitive — "rock", "ROCK", and "Rock" should all be accepted.

**Answer these questions after completing all tasks:**
- Write out the six possible win/loss combinations (Rock beats Scissors, Scissors beats Paper, etc.). How many `if-elif` conditions did you need to cover all of them?
- What does your program do if the player enters the number of rounds as 0 or a negative number? Try it and fix it if it behaves unexpectedly.
- Play 10 rounds against the computer. Does the computer feel random, or does it seem to favour one choice? Why is this expected?

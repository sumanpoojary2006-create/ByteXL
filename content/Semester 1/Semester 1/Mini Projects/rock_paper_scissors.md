## Background

Rock, Paper & Scissors is a classic two-player game — except here, one of the players is your program. The computer picks randomly, you pick by typing, and the program decides who wins. It sounds simple, but getting the win logic right and keeping score across multiple rounds is a good exercise in loops and conditions.

## What You Will Build

A CLI game where the player competes against the computer in Rock, Paper & Scissors. The game runs for multiple rounds, keeps score, and announces the overall winner at the end.

## Learning Objectives

By the end of this project, you will be able to:
- Model game rules with conditional logic
- Use `random.choice()` to pick the computer's move
- Track and report a score across multiple rounds with a loop
- Normalize and validate user input (case-insensitive)

**Difficulty:** Beginner · **Estimated time:** 1–1.5 hours

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

## Sample Run

```
===== Rock, Paper & Scissors =====
How many rounds? 3

Round 1 — Rock, Paper or Scissors? rock
You: Rock | Computer: Scissors
You win the round!
Score — You: 1 | Computer: 0

Round 2 — Rock, Paper or Scissors? PAPER
You: Paper | Computer: Paper
Draw!
Score — You: 1 | Computer: 0

Round 3 — Rock, Paper or Scissors? banana
Invalid choice. Enter Rock, Paper or Scissors.
Round 3 — Rock, Paper or Scissors? scissors
You: Scissors | Computer: Paper
You win the round!

Final Score — You: 2 | Computer: 0
You win the game!
```

**Answer these questions after completing all tasks:**
- Write out the six possible win/loss combinations (Rock beats Scissors, Scissors beats Paper, etc.). How many `if-elif` conditions did you need to cover all of them?
- What does your program do if the player enters the number of rounds as 0 or a negative number? Try it and fix it if it behaves unexpectedly.
- Play 10 rounds against the computer. Does the computer feel random, or does it seem to favour one choice? Why is this expected?

## Deliverables & Rubric

Submit your `.py` file along with written answers to the reflection questions above.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Single-round logic: choices shown, winner/draw decided correctly | 4 |
| Multi-round play with running score and final winner | 2 |
| Input validation and case-insensitive choices | 2 |
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

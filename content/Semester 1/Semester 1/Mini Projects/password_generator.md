## Background

Weak passwords are one of the most common security risks. A good password is long, random, and contains a mix of letters, numbers, and symbols. Building a password generator is a great way to practise string manipulation — you are working with characters, building strings piece by piece, and applying logic to control what goes into the final result.

## What You Will Build

A CLI tool that generates a random password based on the user's preferences — length and which character types to include.

## Learning Objectives

By the end of this project, you will be able to:
- Build strings from character pools using `string` constants
- Use `random.choice()` to assemble randomized output
- Conditionally include character sets based on user input
- Derive a simple rating from the composition of the result

**Difficulty:** Beginner–Intermediate · **Estimated time:** 1.5 hours

## Tasks

### Task 1: Generate a Basic Password

1. Ask the user how long they want the password to be.
2. Generate a random password of that length using lowercase letters only, using `random.choice()` and the `string.ascii_lowercase` constant.
3. Display the generated password.

### Task 2: Character Type Options

1. Ask the user which character types to include:
   - Uppercase letters (Y/N)
   - Numbers (Y/N)
   - Symbols (Y/N) — use `string.punctuation` for the symbol pool

2. Build a character pool from the user's choices combined with lowercase letters (always included).

3. Generate the password by picking randomly from this pool.

4. If the user says N to everything and only lowercase is available, generate the password with lowercase only — do not crash.

### Task 3: Strength Indicator

1. After generating the password, display a strength rating based on these rules:
   - Only one character type → Weak
   - Two character types → Moderate
   - Three or more character types → Strong

2. Display the password and its strength:
   ```
   Generated Password : aB3$kpL9
   Strength           : Strong
   ```

3. Ask the user if they want to generate another password with the same settings. If yes, generate a new one. If no, exit.

## Sample Run

```
===== Password Generator =====
Password length: 8
Include uppercase letters? (Y/N): Y
Include numbers? (Y/N): Y
Include symbols? (Y/N): N

Generated Password : aB3kpLd9
Strength           : Strong

Generate another with the same settings? (Y/N): N
```

**Answer these questions after completing all tasks:**
- Your character pool is a string built by joining the selected character types. What happens if the user selects all options and requests a password of length 1 — can all four character types appear? Is that possible?
- Try generating 5 passwords with the same settings. Are they all different? What would it mean if two identical passwords were generated, and how likely is that?
- A password of length 4 with only lowercase letters is rated "Weak" and a password of length 20 with only lowercase is also rated "Weak." Is your strength rating fair? What else could you add to make it more accurate?

## Deliverables & Rubric

Submit your `.py` file along with written answers to the reflection questions above.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Basic and configurable password generation from the chosen pool | 4 |
| Strength indicator matches the character-type rules | 2 |
| Handles edge cases (all options declined, generate-again loop) | 2 |
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

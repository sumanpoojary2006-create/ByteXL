# Capstone Project: Cricket Score Tracker

## Background

Ball-by-ball cricket commentary is something every Indian student has followed on Cricbuzz or ESPNcricinfo. CricTrack is a command-line cricket score tracker for local and college matches. It records deliveries ball by ball, computes run rates and required rates, tracks individual batting and bowling performances, and generates a full scorecard at the end of the innings.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, each one adding a layer of functionality on top of the last.

## Stages

### Stage 1: Record a Single Over

1. Ask the scorer to enter match details:
   - Team 1 name
   - Team 2 name
   - Number of overs per innings (e.g. 20 for T20)

2. Simulate one over: prompt for each of the 6 deliveries. For each ball, accept:
   - Runs scored (0-6)
   - Delivery type: Normal (N), Wide (W), No Ball (B), Wicket (K)

3. Wides and no-balls add 1 extra run and require an additional delivery in the over.

4. After the over, display the over summary:
   ```
   Over 1: 2 1 W 4 0 K 1
   Runs: 9  |  Wickets: 1  |  Extras: 1 (W)
   ```

**Answer these questions after completing Stage 1:**
- A wide delivery requires an extra ball. How does your loop handle this — does the over end at 6 legal deliveries or at 6 total deliveries? Test with an over that has 3 wides.
- You accept runs as an integer between 0 and 6. A legitimate boundary can score 4 or 6. What invalid inputs does your current validation not catch — for example, what happens if the user enters 5?

### Stage 2: Full Innings with a Live Scoreboard

1. Extend to a full innings: loop over all overs until the team is all out (10 wickets) or overs are complete.

2. Track for the batting team:
   - Total runs, total wickets, total overs faced
   - Extras breakdown: wides, no-balls

3. After each over, display a live scoreboard:
   ```
   ===========================
   CSE-A: 67/3 (8.0 overs)
   CRR: 8.38 | Required: N/A
   ===========================
   ```

4. At the end of the innings, display the full innings total.

**Answer these questions after completing Stage 2:**
- Current run rate (CRR) is total runs / overs bowled. What happens to this calculation on the first ball of the first over, before any complete overs have been bowled — does it crash or give a wrong answer?
- "All out" means 10 wickets. But a team has 11 players, meaning the 11th batsman has no partner. Your innings should end when the 10th wicket falls. Does your loop terminate correctly at exactly 10 wickets?

### Stage 3: Organise with Functions and Add Scorecards

1. Refactor your code so each operation is a dedicated function:
   - `play_over(match_state)` — runs one over and updates the innings
   - `get_scoreboard(match_state)` — returns a formatted live score line
   - `record_batsman_ball(batsmen, name, runs, is_boundary)` — updates one batsman's stats
   - `record_bowler_ball(bowlers, name, runs, delivery_type)` — updates one bowler's stats

2. Track individual batsman performance in a dictionary keyed by name:
   - Runs scored, balls faced, fours, sixes
   - Dismissal type: not out, bowled, caught, run out, LBW

3. Track individual bowler performance in a dictionary keyed by name:
   - Overs bowled (in X.Y format where Y is legal balls), runs conceded, wickets taken, economy rate

4. At the end of the innings, display a batting scorecard followed by a bowling scorecard in standard cricket format:
   ```
   BATTING
   Name              R    B   4s  6s   SR    How Out
   R. Sharma        45   32    5   2  140.6  Caught
   V. Kohli          0    1    0   0    0.0  Bowled
   ...

   BOWLING
   Name           O    M    R    W   Econ
   M. Shami     4.0    0   28    2    7.0
   ...
   ```

**Answer these questions after completing Stage 3:**
- Strike rate is (runs / balls faced) x 100. What do you display for a batsman who scored 0 from 0 balls — they were run out without facing a delivery?
- Economy rate is (runs conceded / overs bowled). Overs bowled for a bowler who bowled 3.4 overs (3 complete overs and 4 balls) is not 3.4 — it is 3 + 4/6 = 3.67. Does your economy rate calculation use 3.4 or 3.67?
- After refactoring into functions, did your main loop get shorter or longer? What moved out of it, and what does that tell you about why functions exist?

### Stage 4: Second Innings and Match Result

1. After the first innings, swap teams for the second innings. The second team now has a target to chase.

2. Track required run rate (RRR) = runs remaining / overs remaining. Update and display after each over.

3. At the end of the match, determine and display the result:
   - If the chasing team reaches the target: "CSE-B won by N wickets"
   - If the bowling team defends: "CSE-A won by N runs"
   - If scores are tied: "Match Tied"

4. Display a full match summary with both scorecards.

**Answer these questions after completing Stage 4:**
- "Won by N wickets" means the chasing team had N wickets in hand when they crossed the target. How do you compute N from your tracked data?
- Required run rate becomes undefined in the last over's last ball — you need 6 off 0.1 overs. Does your RRR calculation handle the final delivery gracefully?

### Stage 5: Redesign with Classes

1. Create a `Batsman` class with attributes `name`, `runs`, `balls`, `fours`, `sixes`, `dismissal` and methods `face_ball(runs, boundary_type)`, `get_out(dismissal_type)`, `strike_rate()`, `__str__`.

2. Create a `Bowler` class with attributes `name`, `overs`, `legal_balls`, `runs_conceded`, `wickets` and methods `bowl_ball(runs, delivery_type)`, `economy()`, `__str__`.

3. Create an `Innings` class with attributes `batting_team`, `bowling_team`, `target`, `batsmen`, `bowlers`, `total_runs`, `wickets`, `extras` and methods `record_ball(runs, delivery_type, bowler_name, batsman_name)`, `current_run_rate()`, `required_run_rate()`, `scorecard()`.

4. Create a `Match` class that holds two `Innings` objects and determines the result.

5. Rewrite the main loop to use a `Match` instance. The loop should only call `Match` and `Innings` methods — no scorekeeping logic inside it.

**Answer these questions after completing Stage 5:**
- `Innings.record_ball()` updates runs, wickets, the current batsman, and the current bowler all in one call. How many objects change state with each ball? List them all.
- After the refactor, where does the "innings is over" check live — in `Innings.record_ball()`, in the `Match` class, or in the main loop? Which location makes the logic clearest, and did you move any logic out of the main loop to get there?

### Stage 6: Make It Robust, Persistent, and Bug-Free

**Exception Handling:**

1. Wrap all file operations in `try-except` blocks. Handle `FileNotFoundError`, `PermissionError`, and `json.JSONDecodeError` separately with a distinct message for each.

2. Add a custom exception `ScoreTrackingError` with two subclasses: `InvalidDeliveryError` (raised when runs are outside 0-6 or the delivery type is not one of N/W/B/K) and `InningsCompleteError` (raised if a ball is recorded after 10 wickets have fallen or all overs are bowled). Raise these inside `Innings.record_ball()` and catch them in the main loop.

3. Save completed match scorecards to `match_history.json`. Each saved match should include both innings' scorecards and the result.

4. Add a **Match History** option: displays a list of saved matches with date, teams, and result.

**Debugging:**

The following three bugs are planted. Find and fix each one. For each, write two sentences: what the bug was and what a scorer would have experienced because of it.

**Bug 1:**
```python
def economy(self):
    return self.runs_conceded / self.overs
    # self.overs is stored as legal_balls / 6
    # but legal_balls is an integer
    # 10 legal balls / 6 = 1 in integer division, not 1.67
```

**Bug 2:**
```python
def current_run_rate(self):
    return self.total_runs / self.overs_completed
    # crashes at the start of the innings before any over is complete
```

**Bug 3:**
```python
def determine_result(self):
    if self.innings2.total_runs >= self.innings1.total_runs:
        print(f"{self.innings2.batting_team} won by "
              f"{10 - self.innings2.wickets} wickets")
    # target is first innings score + 1
    # reaching exactly the first innings total is a tie, not a win
```

**Answer these questions after completing Stage 6:**
- Bug 1 uses integer division accidentally. This is a very common Python 2 to Python 3 migration bug. In Python 3, when does `/` give integer division and when does it not?
- Bug 3 means a tie is declared as a win for the chasing team. Write a specific scorecard scenario (two exact numbers) where this bug would incorrectly announce a winner.
- You now have both validation loops (Stage 1) and a custom exception hierarchy (Stage 6) guarding against bad deliveries. Which one catches a bad input first, and why do you need both instead of just one?

## The Complete Picture

When all six stages are complete, CricTrack:

- Records ball-by-ball deliveries including wides, no-balls, and wickets
- Tracks individual batting and bowling performances
- Computes and displays current and required run rates after each over
- Generates full batting and bowling scorecards in standard format
- Determines match results with wickets-in-hand or runs margin
- Raises and handles a custom exception hierarchy for invalid deliveries
- Saves match history across sessions in JSON
- Uses a clean four-class OOP design
- Has three realistic bugs identified and fixed

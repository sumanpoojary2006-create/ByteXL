## Introduction

A small firm in Kochi is installing alarm systems in apartments, and Tanvi, who writes the controller software, is having an argument with the salesman about when the siren should sound.

The salesman says it is obvious. The alarm goes off if the system is armed and something happens. Tanvi asks what counts as something happening. Motion in the hall, he says, or the front door opening. And if the resident enters the code on the keypad? Then obviously not.

So Tanvi writes: the alarm sounds when the system is armed, and either motion is detected or the door is open, and the correct code has not been entered. The salesman reads it back and agrees. Two weeks later a customer's alarm goes off in an empty flat, at three in the morning, with the system disarmed.

Nobody lied and nobody was careless. English is simply not precise enough to specify a condition with four moving parts, because words like "and" and "or" do not fix how the parts group together. What Tanvi needed was a notation where a statement means exactly one thing and where every possible situation can be checked mechanically. That notation is **propositional logic**.

**Definition:** `Propositional logic` is a formal language in which each `proposition` is a statement that is either true or false, and complex statements are built from simpler ones using `logical operators` whose meaning is fixed completely by a `truth table`.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_introduction.png)

## Propositions

A `proposition` is a statement that is definitely true or definitely false, with no third option and no dependence on who is asking.

- "The system is armed" is a proposition. At any moment it is one or the other.
- "Motion is detected in the hall" is a proposition.
- "Is the door open?" is not a proposition. Questions have no truth value.
- "Arm the system" is not a proposition. Commands have no truth value.
- "This alarm is too loud" is not a proposition in any useful sense, because its truth depends on who is listening.

Each proposition gets a short symbol or name, and from then on the logic does not care what it means. This is the source of both the power and the limitation of the whole system: the machinery works identically whether the names refer to alarms, to blood tests, or to nothing at all.

![Visual explanation of propositions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_propositions.png)

## The Five Operators

Complex statements are built with five operators, and each is defined entirely by what it does to truth values.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operator</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Read as</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">True exactly when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>NOT</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">not P</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P is false</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>AND</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P and Q</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">both are true</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>OR</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P or Q</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">at least one is true, including both</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>IMPLIES</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">if P then Q</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P is false, or Q is true</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>IF AND ONLY IF</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P exactly when Q</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">both have the same truth value</td>
    </tr>
  </tbody>
</table>

Two rows deserve a warning, because both differ from ordinary speech.

**OR includes both.** Asked "tea or coffee", a person means one. In logic, "motion or door open" is true when both happen. This is inclusive or, and when the exclusive meaning is wanted it must be built explicitly.

**IMPLIES is stranger than it looks**, and it is treated separately below because it causes more confusion than everything else combined.

![Visual explanation of propositional operators](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_propositional_operators.png)

## Reading a Specification as a Truth Table

Tanvi's statement, written properly, is: armed AND (motion OR door open). The parentheses are not decoration; they are the entire content of the argument she had with the salesman.

A `truth table` lists every possible combination of truth values and what the formula evaluates to in each. With three propositions there are eight combinations, and checking all eight is checking every situation that can ever arise.

Reading the code below: `truth_table` is a general printer that works for any formula, and `alarm` is Tanvi's specification written as one line of Python. The key idea is that a logical formula becomes an ordinary function, so evaluating it in every situation is just a loop.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjgf5" 
 width="100%"
></iframe>

```
armed | motion | door_open | alarm sounds
-----------------------------------------
False | False  | False     | False
False | False  | True      | False
False | True   | False     | False
False | True   | True      | False
True  | False  | False     | False
True  | False  | True      | True
True  | True   | False     | True
True  | True   | True      | True
```

Eight rows, and the specification is now unambiguous.

| In the code | What it does |
| --- | --- |
| `product([False, True], repeat=3)` | Generates all 2³ = 8 combinations, in a fixed order |
| `dict(zip(names, values))` | Turns one combination into named arguments |
| `formula(**assignment)` | Calls the formula with those names, so any formula works |
| `armed and (motion or door_open)` | The specification itself, brackets and all |

Every row where `armed` is False gives False, which is what "armed and anything" must produce. Of the four armed rows, three sound the alarm and one does not, the one where nothing happened.

This is the property that makes propositional logic useful for specification. **A formula over n propositions has exactly 2 to the power n possible situations, and all of them can be checked.** No customer can present a case that is not already a row in the table. The argument between Tanvi and the salesman was unresolvable in English and takes eight lines to settle here.

![Visual explanation of reading a specification as a truth table](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_reading_a_specification_as_a_truth_table.png)

## Implication, and Why Everyone Gets It Wrong

The `IMPLIES` operator is worth its own section because its definition is genuinely counter-intuitive on first meeting.

"If P then Q" is defined as false in exactly one case: P true and Q false. In every other case it is true. Which means that if P is false, the whole statement is true regardless of Q.

Take "if the door is opened while armed, the siren sounds". Suppose the door is never opened. Is the statement true? Logic says yes, and this feels wrong, because nothing was tested. The reasoning behind the convention is that an implication is a promise, and a promise is broken only by the one case where its condition was met and its consequence failed. If the door was never opened, the promise was never broken, so it stands. This is called **vacuous truth**, and it is a convention adopted because it makes the logic work cleanly, not a discovery about how promises really behave.

Two errors follow from misreading implication, and both are common enough to have names.

- **Affirming the consequent.** From "if armed and the door opens, the siren sounds" plus "the siren is sounding", concluding that the door opened. Invalid. The motion sensor could have triggered it.
- **Denying the antecedent.** From the same rule plus "the door did not open", concluding the siren is silent. Also invalid, for the same reason.

What *is* valid is the contrapositive: from "if P then Q", you may conclude "if not Q then not P". If the siren is silent, then it is not the case that the system was armed and the door opened. That one is watertight, and the code below confirms it mechanically.

![Visual explanation of implication truth table](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_implication_truth_table_context_v4.png)

## Tautologies, Contradictions, and Equivalence

Once every formula can be evaluated in every situation, formulas sort themselves into three kinds, and two formulas can be compared exactly.

Reading the code below: `all_results` evaluates a formula in every situation and returns the whole column of answers. Everything else is built on that one idea, including the equivalence test, which turns out to be a single `==`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjgs4" 
 width="100%"
></iframe>

```
armed or not armed               -> tautology (always true)
armed and not armed              -> contradiction (never true)
armed and motion                 -> contingency (depends on the values)
if armed and motion then armed   -> tautology (always true)

De Morgan: not(m or d) == (not m) and (not d)            equivalent
Tempting error: not(m or d) == (not m) or (not d)        NOT equivalent
Contrapositive: (m implies d) == (not d implies not m)   equivalent
Converse error: (m implies d) == (d implies m)           NOT equivalent
```

Several things in that output matter.

A **tautology** is true in every situation, which means it carries no information about the world but does record something guaranteed by the structure of the statement. The fourth one, "if armed and motion then armed", is a tautology, and that is precisely what makes it a valid rule of reasoning: it can never lead from truth to falsehood.

A **contradiction** is true in no situation, and finding one in a specification means the specification demands something impossible.

Two formulas are **logically equivalent** when their columns match in every row, which means either can be substituted for the other anywhere. De Morgan's law is the everyday one: "neither motion nor door" is the same as "no motion and no door". Notice that the tempting variant, changing AND to OR, is not equivalent, and this is the single most common mistake made when negating a condition in code.

Notice how little machinery any of this needed.

| In the code | What it decides | How |
| --- | --- | --- |
| `all(results)` | Tautology | True in every row |
| `not any(results)` | Contradiction | False in every row |
| neither | Contingency | Some rows true, some false |
| `all_results(left) == all_results(right)` | Equivalence | The two columns are identical |

The last row is the one to appreciate. `equivalent` does not reason, prove, or manipulate symbols. It evaluates both formulas in all four situations and compares two Python lists with `==`. **Exhaustive checking replaces argument entirely**, and that is the practical gift of a finite truth table.

![Visual explanation of tautologies, contradictions, and equivalence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_tautologies_contradictions_and_equivalence_simple_v2.png)

## Where Propositional Logic Runs Out

Before the exercise, it is worth being clear about the ceiling, because it arrives quickly.

Tanvi's building has forty flats, each with a motion sensor. She wants to say: if any armed flat detects motion, alert the guard. Propositional logic cannot say "any armed flat". It has no way to talk about flats as things, or about a property holding across a collection. She would have to write forty separate propositions and combine all forty with OR, and then write it again when a forty-first flat is added.

The other ceiling is arithmetic. Sixteen propositions produce 65,536 rows, and thirty produce over a billion. Exhaustive checking is a wonderful tool that stops working sooner than people expect.

![Visual explanation of where propositional logic runs out](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_where_propositional_logic_runs_out.png)

## Your Turn

Return to Tanvi's three-in-the-morning failure. Her specification was "armed AND (motion OR door open) AND NOT code entered". The version that reached the customer's flat had lost a pair of brackets.

Before running this, predict how many of the sixteen situations the two versions disagree on.

Reading the code below: two functions holding what Tanvi meant and what shipped. Read them side by side; the only difference is where the brackets are, and one of them has none. The loop then checks all sixteen situations and prints every disagreement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjh3t" 
 width="100%"
></iframe>

```
Rows where the two versions disagree: 6 of 16

  armed=False, motion=False, door_open=True, code_entered=False
    specified says False, code says True
  armed=False, motion=False, door_open=True, code_entered=True
    specified says False, code says True
  armed=False, motion=True, door_open=True, code_entered=False
    specified says False, code says True
  armed=False, motion=True, door_open=True, code_entered=True
    specified says False, code says True
  armed=True, motion=False, door_open=True, code_entered=True
    specified says False, code says True
  armed=True, motion=True, door_open=True, code_entered=True
    specified says False, code says True
```

Read the first disagreement carefully. The system is **not armed**, and the code sounds the siren anyway, because `and` binds tighter than `or`, so the shipped formula reduces to "either the armed conditions hold, or the door is simply open". Rows five and six are worse in a different way: the resident has entered the correct code and the siren sounds regardless.

Six of sixteen situations wrong, from one missing pair of brackets, found in a fraction of a second by an exhaustive check that no amount of reading the code aloud would have produced reliably.

Now extend it. Add a fifth proposition for a panic button that must sound the siren whatever else is true, including when the system is disarmed. Write the corrected specification, and then verify two things exhaustively rather than by inspection: that pressing the panic button always sounds the siren, and that not pressing it leaves all sixteen original rows exactly as the correct specification had them. If your second check fails, your panic button has quietly changed the behaviour of the ordinary cases, which is the kind of fault that ships.

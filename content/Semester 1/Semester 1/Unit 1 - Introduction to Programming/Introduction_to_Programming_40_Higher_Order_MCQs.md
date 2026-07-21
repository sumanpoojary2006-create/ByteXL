# Unit 1: Introduction to Programming - 40 Higher-Order MCQs

## Assessment design

- Scope: all nine Unit 1 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led decision making, tracing, testing, design review, and practical application
- Student expectation: reason from the stated requirement or trace before selecting an answer

---

## Questions

### 1. Instructions for a literal fee-calculation assistant

**Difficulty:** Foundational

A college asks a computer to prepare admission receipts. The draft instruction says:

> Work out the correct fee after tax and scholarship, then make a good receipt.

The computer cannot use unstated common sense. Which replacement is most suitable for the computer to follow repeatedly?

A. Prepare each receipt as quickly as possible and avoid mistakes  
B. Read the student's details, calculate a fair amount, and print it neatly  
C. Read the base fee and approved scholarship, calculate `base fee + 18% tax - scholarship`, then print the student's name and calculated amount  
D. Ask an experienced clerk to decide how every receipt should be calculated

### 2. Turning one clerk's method into automation

**Difficulty:** Intermediate

A clerk can manually prepare one accurate receipt in two minutes. The college needs 5,000 receipts governed by the same rules. Which proposal captures the programming approach most effectively?

A. Express the receipt rules once as clear, ordered instructions and let the computer execute them for every student  
B. Ask the clerk to memorise the rules so each receipt becomes slightly faster  
C. Scan one completed receipt 5,000 times, even though every student's values differ  
D. Buy a faster printer without describing how each amount should be calculated

### 3. From operating a feature to creating one

**Difficulty:** Foundational

Four interns describe their work on a shopping application. Which intern is programming rather than only using existing software?

A. Meera taps “Add to Cart” to buy a notebook  
B. Faisal changes his delivery address through the settings screen  
C. Kavya exports her order history using the existing Download button  
D. Arjun defines the ordered instructions that validate an item, update the cart total, and show the new quantity when “Add to Cart” is tapped

### 4. A medicine dispenser that must respect order

**Difficulty:** Intermediate

An automated pharmacy cabinet must dispense medicine only for a valid prescription. Which sequence is both complete enough for the stated task and safely ordered?

A. Dispense medicine → read prescription → confirm patient  
B. Read patient ID → read prescription → verify patient and prescription → select prescribed medicine → dispense it  
C. Select any available medicine → check whether the patient wants it → dispense  
D. Read patient ID → dispense medicine → verify the prescription later

### 5. Separating a taxi fare system into IPO

**Difficulty:** Foundational

A taxi application receives the travelled distance and price per kilometre, calculates the fare, and displays the amount due. Which IPO description matches the system?

A. Input: calculated fare; Processing: display it; Output: distance and rate  
B. Input: distance and rate; Processing: multiply them; Output: fare due  
C. Input: multiplication; Processing: fare due; Output: distance  
D. Input: passenger name only; Processing: save the name; Output: distance

### 6. A backup with no person at the keyboard

**Difficulty:** Foundational

A backup application begins automatically every night at 2:00 AM. No user clicks a button. In the IPO model, which event acts as the input that starts this run?

A. The completion message shown after the backup  
B. The CPU performing the copy  
C. The copied files stored at the destination  
D. The scheduled 2:00 AM trigger

### 7. A perfect formula receives unreliable data

**Difficulty:** Intermediate

A parcel service uses a tested formula to calculate delivery charges from weight. One scale sends `650` for a 650-gram parcel, while a faulty scale sends `6500`. The software confidently charges ten times too much. Which intervention addresses the real weakness in this situation?

A. Validate whether the incoming weight is plausible before applying the correct formula  
B. Replace the output screen because it displayed the charge accurately  
C. Make the CPU repeat the same calculation twice  
D. Move the charge calculation from processing into output

### 8. Notes that disappear after a power failure

**Difficulty:** Foundational

A note-taking program keeps a new paragraph available while the program is open, but the paragraph disappears after a power failure because the user never saved it. Which explanation best fits the computer components introduced in the unit?

A. The paragraph was stored permanently by the CPU  
B. The keyboard deleted the paragraph when power stopped  
C. The paragraph existed only in RAM, and it was never written to long-term storage  
D. The screen was responsible for remembering the paragraph

### 9. Following an ATM request through the hardware

**Difficulty:** Foundational

An ATM receives a PIN, checks it, shows an approval message, and records the completed transaction for future visits. Which component mapping is accurate?

A. Screen checks the PIN; CPU stores the permanent record; keypad shows approval  
B. Keypad supplies input; CPU performs the check; screen supplies output; storage keeps the lasting record  
C. Storage reads the PIN; RAM dispenses cash; keypad performs the comparison  
D. CPU supplies the PIN; screen processes it; storage displays approval

### 10. Splitting a hospital appointment system

**Difficulty:** Intermediate

A team is overwhelmed by the instruction “build a hospital appointment system.” Which first breakdown demonstrates useful decomposition?

A. Separate patient registration, doctor availability, appointment booking, cancellation, and reminders into smaller problems  
B. Choose the colour of every screen before identifying what the system must do  
C. Treat the entire system as one task so no component is considered separately  
D. Write the final program immediately and discover the required features later

### 11. Three campus documents share one shape

**Difficulty:** Intermediate

A college separately prints fee receipts, ID cards, and course certificates. A developer notices that each task reads one student record, fills a template, and produces one personalised document. Which decision makes the best use of that observation?

A. Ignore the shared steps because the documents have different names  
B. Merge every document into one identical design  
C. Ask students to create all three documents manually  
D. Design one reusable record-to-template process and apply the appropriate template in each case

### 12. Choosing details for a delivery-time estimate

**Difficulty:** Intermediate

A team is modelling the estimated arrival time for a food order. Which set retains the essential details while removing irrelevant noise?

A. Customer's wallpaper, rider's shirt colour, and restaurant logo  
B. Customer's favourite cuisine, phone model, and profile photo  
C. Distance, current traffic, preparation time, and rider availability  
D. Every detail stored about the customer, restaurant, and rider

### 13. When abstraction removes something essential

**Difficulty:** Advanced

A clinic scheduler keeps doctor name, patient name, and appointment date, but removes appointment duration to “simplify” the model. Later it assigns two patients to the same doctor at overlapping times. Which review conclusion is strongest?

A. The model needs more decorative patient information  
B. The abstraction removed a detail required to determine whether time slots overlap  
C. Decomposition should never be used with scheduling problems  
D. Pattern recognition caused the scheduler to forget the date

### 14. Redesigning a festival registration workflow

**Difficulty:** Advanced

A festival team currently maintains separate handwritten processes for workshop entry, meal coupons, and certificate collection. A new plan splits registration into smaller services, recognises that all three services verify the same student ID, and excludes clothing colour from the data model. Which assessment of the plan is accurate?

A. It uses abstraction only  
B. It uses decomposition and ignores pattern recognition  
C. It uses pattern recognition but keeps every irrelevant detail  
D. It combines decomposition, pattern recognition, and abstraction

### 15. Tracking the highest score seen so far

**Difficulty:** Intermediate

A scholarship team reviews scores in this order: `72, 88, 65, 90, 77`. Its paper trace records the “highest so far” after each score is considered. Which trace should the reviewer accept?

A. `72, 88, 88, 90, 90`  
B. `72, 88, 65, 90, 77`  
C. `90, 90, 90, 90, 90`  
D. `72, 72, 72, 72, 72`

### 16. “Make search fast” is not yet a clear requirement

**Difficulty:** Intermediate

A client asks a team to “make the student search fast,” but does not state how many records exist, what users search by, or what response time is acceptable. Which action belongs first in a disciplined problem-solving approach?

A. Build the search screen and decide the rules afterward  
B. Select Python because implementation always comes first  
C. Restate the problem with the client and clarify inputs, expected output, constraints, and the meaning of “fast”  
D. Test a finished solution against random values

### 17. The useful pause before implementation

**Difficulty:** Intermediate

Two students understand a pass/fail requirement. One starts typing immediately. The other lists the inputs, average calculation, threshold decision, and displayed result before opening an editor. In the four-stage rhythm, which stage is the second student performing?

A. Look back  
B. Plan  
C. Carry out  
D. Installation

### 18. Testing the exact scholarship boundary

**Difficulty:** Advanced

A scholarship is awarded when the average is **75 or more**. The solution works for averages of 74 and 90. The team can add one test specifically to determine whether the boundary wording was translated correctly. Which test has the highest value?

A. Average `0`  
B. Average `1000`  
C. Average `76`  
D. Average `75`

### 19. A compact test set for a ticket limit

**Difficulty:** Intermediate

A booking plan should accept requests from 1 through 6 tickets. Which compact test set best exercises the ordinary case, both valid boundaries, and invalid values immediately outside them?

A. `0, 1, 3, 6, 7`  
B. `2, 3, 4, 5, 6`  
C. `1, 1, 1, 1, 1`  
D. `-100, 100, 1000, 10000`

### 20. The undefined “best student” report

**Difficulty:** Advanced

A requirement says, “Read all student records and display the best student.” The records contain marks, attendance, project score, and sports points. A developer chooses the highest marks without consulting anyone. Which response would have prevented the largest risk?

A. Write the output screen before reading any records  
B. Assume “best” always means the first record  
C. Return to understanding and clarify the selection rule before planning the solution  
D. Add every field together even though no weighting rule was supplied

### 21. “Arrange the deliveries properly”

**Difficulty:** Intermediate

A route algorithm contains this step:

> Arrange all deliveries properly before starting.

Two drivers interpret “properly” differently. Which property of a reliable algorithm is missing most clearly?

A. Input  
B. Output  
C. Finiteness  
D. Definiteness

### 22. A customer-support process with no guaranteed ending

**Difficulty:** Advanced

A draft procedure says:

1. Ask the customer whether they are satisfied.
2. If not, say “We will improve.”
3. Return to step 1.

No action changes the customer's situation and no maximum number of attempts is defined. Which algorithm requirement is most directly threatened?

A. Effectiveness, because speaking is impossible  
B. Finiteness, because the procedure has no guaranteed stopping point  
C. Input, because the customer gives an answer  
D. Output, because the procedure displays a message

### 23. One plan implemented in two languages

**Difficulty:** Foundational

A team writes one language-independent procedure for finding the largest of three numbers. Priya implements it in Python and Joel implements it in Java. Which description correctly relates their work?

A. They share one algorithm but have two programs expressed in different languages  
B. They have two unrelated algorithms because the syntax differs  
C. The Python file is an algorithm, while the Java file is a program  
D. Only compiled languages can express an algorithm

### 24. Tracing a largest-value algorithm

**Difficulty:** Intermediate

A quality inspector applies these instructions to measurements `12`, `27`, and `19`:

1. Treat the first measurement as the largest.
2. Replace the stored largest if the second is bigger.
3. Replace the stored largest if the third is bigger.
4. Report the stored value.

Which report follows the procedure faithfully?

A. `12`, because the first value is stored first  
B. `19`, because it is considered last  
C. `27`, because it replaces `12` and is not replaced by `19`  
D. `58`, because all measurements should be added

### 25. Two correct contact searches at different scales

**Difficulty:** Advanced

A phone contains 20 contacts today but may contain 20,000 next year. Method 1 checks every name from the top. Method 2 uses the alphabetic index to jump to the correct letter before scanning. Both eventually find the correct contact. Which engineering judgment is most appropriate?

A. Method 1 is the only algorithm because it checks every item  
B. Method 2 is incorrect because it skips unrelated letters  
C. The methods must take the same time because both are correct  
D. Both are correct algorithms, but Method 2 is likely more efficient as the list grows

### 26. An ATM sequence forgets the card

**Difficulty:** Intermediate

An ATM withdrawal procedure validates the PIN, checks the balance, dispenses cash, updates the balance, and ends. The requirement also states that the card must always be returned. Which review note should block release?

A. The procedure is ambiguous because “cash” has no meaning  
B. The procedure is incomplete because a required card-return step is missing  
C. The procedure is infinite because it updates the balance  
D. The procedure has no processing because it uses a PIN

### 27. A whiteboard plan that the computer cannot execute

**Difficulty:** Foundational

A team writes this during a design meeting:

```text
READ marks
COMPUTE average
IF average >= 40 THEN
    PRINT "Pass"
ELSE
    PRINT "Fail"
END IF
```

The logic is clear to everyone, but double-clicking the text does not run it. Which explanation fits its purpose?

A. It is invalid because decisions cannot be written before code  
B. It is a flowchart without arrows  
C. It is pseudocode for humans to review and later translate into a programming language  
D. It is a Python program missing only a file name

### 28. Repairing the order of an average calculation

**Difficulty:** Intermediate

A draft solution tries to calculate `average` before receiving any marks. Which pseudocode revision puts the work in a usable order?

A.

```text
BEGIN
    READ mark1, mark2, mark3
    SET average = (mark1 + mark2 + mark3) / 3
    PRINT average
END
```

B.

```text
BEGIN
    PRINT average
    READ mark1, mark2, mark3
END
```

C.

```text
BEGIN
    SET average = (mark1 + mark2 + mark3) / 3
    READ mark1, mark2, mark3
END
```

D.

```text
BEGIN
    READ average
    PRINT mark1, mark2, mark3
END
```

### 29. Shipping a parcel at the free-delivery boundary

**Difficulty:** Advanced

A delivery team reviews this pseudocode:

```text
BEGIN
    READ order_total
    IF order_total >= 500 THEN
        SET delivery_fee = 0
    ELSE
        SET delivery_fee = 50
    END IF
    PRINT delivery_fee
END
```

A customer's order total is exactly ₹500. Which trace belongs in the review record?

A. The fee is ₹50 because only totals above ₹500 qualify  
B. Both fees are assigned because both branches run  
C. No fee is shown because pseudocode cannot contain numbers  
D. The condition is satisfied, the first branch assigns ₹0, and ₹0 is displayed

### 30. A rejection message placed outside its branch

**Difficulty:** Intermediate

A login design is intended to show `"Try again"` only when the PIN is incorrect:

```text
IF pin_is_correct THEN
    PRINT "Welcome"
PRINT "Try again"
END IF
```

Which revised layout communicates the intended branch membership clearly?

A.

```text
IF pin_is_correct THEN
PRINT "Welcome"
PRINT "Try again"
END IF
```

B.

```text
IF pin_is_correct THEN
    PRINT "Welcome"
ELSE
    PRINT "Try again"
END IF
```

C.

```text
PRINT "Try again"
IF pin_is_correct THEN
    PRINT "Welcome"
END IF
```

D.

```text
IF pin_is_correct THEN
    PRINT "Try again"
ELSE
    PRINT "Welcome"
END IF
```

### 31. Explaining a refund workflow to store managers

**Difficulty:** Intermediate

A refund workflow contains several approval decisions, a path back for missing documents, and an audience of non-technical store managers. Which artefact is best suited to the meeting?

A. Executable Python with no diagram  
B. A long paragraph with every branch embedded in sentences  
C. A flowchart showing decisions, labelled paths, and the return arrow  
D. A screenshot of the final refund screen

### 32. Assigning shapes to a pass/fail chart

**Difficulty:** Foundational

A chart must read marks, calculate an average, decide whether the average is at least 40, and display Pass or Fail. Which shape assignment follows standard flowchart meaning?

A. Read marks: parallelogram; calculate average: rectangle; threshold question: diamond; display result: parallelogram  
B. Read marks: diamond; calculate average: oval; threshold question: rectangle; display result: arrow  
C. Read marks: rectangle; calculate average: parallelogram; threshold question: oval; display result: diamond  
D. Use rectangles for every step because the arrows already show direction

### 33. A decision diamond with two anonymous exits

**Difficulty:** Intermediate

A railway turnstile flowchart has a diamond labelled `Ticket valid?`. Its two outgoing arrows are not labelled, so a reader cannot tell which path opens the gate. Which correction makes the chart unambiguous?

A. Remove one outgoing arrow  
B. Replace the diamond with a process rectangle  
C. Put both outcomes on one arrow  
D. Label the outgoing paths `Yes` and `No` and connect each to its corresponding action

### 34. Two failed logins followed by success

**Difficulty:** Advanced

A login flowchart starts with `tries = 0`. After each wrong password it adds 1. If `tries < 3`, it returns to read another password; otherwise it locks the account. A user enters two wrong passwords and then the correct password. Which path summary matches the chart?

A. The account locks after the second failure because only two retries are allowed  
B. The chart loops after each of the first two failures, then follows the success path and grants access with `tries = 2`  
C. The success is ignored because any earlier failure forces the lock path  
D. The chart never stops because every backward arrow is infinite

### 35. Drafting a mostly sequential calculation

**Difficulty:** Intermediate

A developer needs to sketch a short salary calculation, edit its steps quickly, and discuss it with another developer. It has one simple sequence and no complicated web of branches. Which choice best fits this moment?

A. Build the full graphical interface first  
B. Draw a large flowchart even though the path never branches  
C. Write concise pseudocode, then trace and translate it later  
D. Avoid planning because sequential problems cannot contain mistakes

### 36. A first language that does not hide the idea

**Difficulty:** Intermediate

A teaching team wants beginners to focus on problem-solving rather than extensive punctuation and boilerplate, while still learning a language used in automation, data, web systems, and AI. Which justification best supports Python?

A. Its readable syntax reduces ceremony, while its ecosystem and general-purpose use keep it relevant beyond the classroom  
B. Python guarantees that beginners will never encounter errors  
C. Python is the fastest possible language for every kind of software  
D. Python requires no interpreter or runtime

### 37. Choosing a language for a tiny real-time controller

**Difficulty:** Advanced

A team is building a tiny embedded controller with extremely limited memory and strict real-time performance requirements. Another team is building a data-analysis prototype. Which recommendation reflects the trade-off described in the unit?

A. Python must be selected for both because readable languages are always fastest  
B. A compiled language must be selected for both because Python has no real-world uses  
C. Language choice never depends on the task  
D. Python is a strong fit for the data prototype, while a lower-level compiled language may better suit the constrained controller

### 38. A calculation needed only once

**Difficulty:** Foundational

A student wants to calculate `1234 × 5678` once and does not need to keep the work. Which Python workspace is the most appropriate choice?

A. A saved package containing several files  
B. A permanent script that must be reopened next semester  
C. The REPL, because it gives an immediate answer and the session need not be saved  
D. A flowchart, because flowcharts execute calculations

### 39. A script runs but reveals only its greeting

**Difficulty:** Intermediate

A beginner runs this saved script:

```python
print("Welcome")
score = 10 + 5
```

The learner expected to see both `Welcome` and `15`. Which support response explains the observed screen most accurately?

A. The calculation never occurs because assignment is not processing  
B. `Welcome` appears, and `15` is stored but not displayed because no `print` instruction outputs `score`  
C. Python automatically displays every stored value in a script  
D. The script must be moved into the REPL before assignment can work

### 40. An age entered as text behaves like text

**Difficulty:** Advanced

A welcome kiosk contains:

```python
age = input("Age: ")
print(age + age)
```

A visitor types `20`. The designer expected `40`, but the screen shows `2020`. Which change plan is based on the correct explanation?

A. Recognise that `input` supplied the text `"20"`; convert it to a numeric value before performing addition  
B. Replace `print` because it turns every number into repeated text  
C. Run the same file from the REPL because scripts cannot add numbers  
D. Save the input in storage before using it so RAM can calculate correctly

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | C | Foundational | It supplies explicit inputs, an unambiguous calculation, an ordered action, and a defined output rather than asking the computer to use judgment. |
| 2 | A | Intermediate | Programming captures the rules once as executable instructions so the machine can apply the same logic reliably at scale. |
| 3 | D | Foundational | Defining the behavior behind the button is writing software; the other interns are operating features someone else already built. |
| 4 | B | Intermediate | It gathers and verifies the required information before selecting and dispensing the prescribed medicine. |
| 5 | B | Foundational | Distance and rate enter the program, multiplication transforms them, and the fare is the result returned to the user. |
| 6 | D | Foundational | Input can be a scheduled trigger; it does not require a person typing or clicking. |
| 7 | A | Intermediate | Correct processing cannot rescue a faulty weight. Checking the input addresses the garbage-in, garbage-out problem. |
| 8 | C | Foundational | RAM holds active data temporarily and loses it when power ends; only deliberately saved data survives in storage. |
| 9 | B | Foundational | The keypad is an input device, the CPU processes, the screen outputs, and storage preserves the transaction. |
| 10 | A | Intermediate | Decomposition makes the large system manageable by identifying coherent smaller problems. |
| 11 | D | Intermediate | The shared record-to-document pattern can be solved once and reused with different templates. |
| 12 | C | Intermediate | Those variables materially affect arrival time; the other choices retain irrelevant personal or visual details. |
| 13 | B | Advanced | Duration is essential to checking overlap. Abstraction simplifies only by removing details that do not affect the solution. |
| 14 | D | Advanced | The plan splits the workflow, reuses a repeated ID check, and removes an irrelevant attribute. |
| 15 | A | Intermediate | The stored maximum progresses from 72 to 88, stays 88 for 65, becomes 90, and stays 90 for 77. |
| 16 | C | Intermediate | The team must understand and clarify the problem before planning or implementation can be reliable. |
| 17 | B | Intermediate | Listing the intended steps after understanding the requirement is the planning stage. |
| 18 | D | Advanced | Testing exactly 75 distinguishes an inclusive `75 or more` rule from an incorrect strict-above-75 rule. |
| 19 | A | Intermediate | It covers a typical valid value, both valid endpoints, and the closest invalid values below and above the range. |
| 20 | C | Advanced | “Best” is ambiguous because several competing measures exist; the selection rule must be clarified during understanding. |
| 21 | D | Intermediate | “Properly” allows different interpretations, violating definiteness. |
| 22 | B | Advanced | Nothing guarantees that satisfaction will change or limits retries, so termination is not guaranteed. |
| 23 | A | Foundational | The algorithm is the language-independent plan; each language-specific implementation is a program. |
| 24 | C | Intermediate | The stored largest changes from 12 to 27 and remains 27 because 19 is smaller. |
| 25 | D | Advanced | Correctness and efficiency are separate. Both can find the contact, while indexed access avoids unnecessary checks at scale. |
| 26 | B | Intermediate | Returning the card is an explicit requirement, so omitting it makes the instruction sequence incomplete. |
| 27 | C | Foundational | Pseudocode communicates structured logic to people without needing the exact syntax a computer requires. |
| 28 | A | Intermediate | The marks must be received before the average can be computed and shown. |
| 29 | D | Advanced | The inclusive comparison is true at exactly ₹500, so the zero-fee branch runs and that value is displayed. |
| 30 | B | Intermediate | The `ELSE` branch and indentation attach the retry message only to the incorrect-PIN outcome. |
| 31 | C | Intermediate | A flowchart makes branches, loops, and return paths visible to technical and non-technical readers. |
| 32 | A | Foundational | Parallelograms represent input/output, rectangles represent processing, and diamonds represent decisions. |
| 33 | D | Intermediate | A decision needs labelled outcomes so readers can connect each result to the correct next action. |
| 34 | B | Advanced | After two failures, `tries` is 2 and the chart permits another attempt; the correct third entry follows the success path. |
| 35 | C | Intermediate | Pseudocode is quick to draft and edit when the purpose is to reason about mostly sequential logic before implementation. |
| 36 | A | Intermediate | Python combines low syntactic ceremony and readability with a large ecosystem and broad professional use. |
| 37 | D | Advanced | Python fits rapid data work, while highly constrained real-time systems may benefit from a compiled, lower-level language. |
| 38 | C | Foundational | The REPL is intended for immediate, disposable experiments and calculations. |
| 39 | B | Intermediate | Assignment performs and stores the calculation, but only `print` sends a value to the screen in a script. |
| 40 | A | Advanced | `input()` returns a string, so `+` joins `"20"` and `"20"`; numeric addition requires conversion first. |

## Topic coverage

| Unit 1 topic | Question numbers |
|---|---|
| What programming is and why it matters | 1–4 |
| Inputs, processing, outputs, and computer components | 5–9 |
| Computational thinking | 10–15 |
| Problem-solving approach | 16–20 |
| Algorithms | 21–26 |
| Pseudocode | 27–30, 35 |
| Flowcharts | 31–34 |
| Why Python | 36–37 |
| Python setup, REPL, scripts, `print`, and `input` | 38–40 |

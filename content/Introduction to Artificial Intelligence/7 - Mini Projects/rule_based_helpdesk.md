## Background

A college puts a chatbot on its website. It answers "how do I apply for a bonafide certificate" instantly and correctly, and then fails on "my warden says I need proof that I'm studying here", which is the same request in different words. That failure is not sloppy engineering. It is the signature of one specific way of building AI, and recognising the signature tells you almost everything about how a system was made.

The fastest way to understand why learning-based AI exists is to build the thing it replaced, measure exactly where it breaks, and be able to say what would have to change. That is more useful than being told rules are brittle, because you will have the number.

## What You Will Build

A rule-based helpdesk assistant for a college, plus a test harness that measures its coverage against realistic student questions and reports precisely how it fails.

## Learning Objectives

By the end of this project, you will be able to:
- Separate a knowledge base from the inference procedure that uses it
- Explain why a rule fires on a message it was never intended for
- Measure brittleness as a number rather than describing it as a quality
- Apply the four characteristics of an AI system to something you built yourself
- Decide which parts of a system may never be probabilistic

**Difficulty:** Beginner · **Estimated time:** 2 hours

**Before you start.** This is the first project in the course and Unit 1 contains no code, so the scaffolding below is given to you. Copy it into your file as it stands. Your work begins at Task 1 step 3, and everything the project assesses is written by you.

```python
# Given. Each rule is an identifier, a set of trigger words, and a reply.
# A rule fires when EVERY word in its trigger appears in the message.
RULES = [
    ("R1", {"bonafide"},            "Bonafide certificate: academic office, window 3."),
    ("R2", {"proof", "study"},      "Bonafide certificate: academic office, window 3."),
    ("R3", {"fee", "last", "date"}, "Fee deadline: 15th of the month."),
    ("R4", {"hostel", "leave"},     "Hostel leave form: warden's office."),
    ("R5", {"transcript"},          "Transcripts: apply online, seven working days."),
]
FALLBACK = "Sorry, I did not understand that. Please rephrase your question."

# Given. Lowercases the message, splits on spaces, strips punctuation,
# and returns the words as a set.
def tokenise(text):
    return {w.strip(".,!?'") for w in text.lower().split()}
```

## Tasks

### Task 1: The Engine

1. Read the two given structures until you can state, in one sentence each, what `RULES` holds and what `tokenise` returns.

2. Add one rule of your own to `RULES`, for a request the college would plausibly receive.

3. Write a `respond(message)` function. Tokenise the message, then find the first rule whose trigger words are all present. Return two things: the identifier of the rule that fired and its reply. When nothing matches, return `None` and `FALLBACK`.

4. Keep your matching logic separate from the rules themselves. Somebody should be able to add a rule without reading your code.

### Task 2: Measure the Brittleness

1. Build a test set of at least ten messages. For each one, record which rule *should* handle it. Include several paraphrases that mean the same thing as a rule's trigger but do not use its exact words, and include at least one message that contains a trigger's words while meaning something completely different.

2. Run every test message through `respond()` and classify the outcome as one of three things: the correct rule fired, no rule fired when one should have, or the wrong rule fired.

3. Print a table with one row per message and a summary line giving the coverage as a percentage.

4. The third outcome is the interesting one. Make sure your test set contains a message like "the hostel warden is on leave, who signs my form" so you can see a rule fire on a request it has nothing to do with.

### Task 3: Classify What You Built

Answer these in a short written section, in your own words, referring to the numbers your harness produced:

1. Work through the four characteristics of an AI system. Which does your helpdesk show, and which does it not? Be specific about why.

2. Your system fails loudly, saying it did not understand. A learning-based system would fail quietly with a plausible wrong answer. For a college helpdesk, which failure would you rather have, and why?

3. Suppose the college replaces your rules with a learned model that handles every paraphrase correctly. Name one responsibility you would keep in a rule layer regardless, and state why a model that is right 99 percent of the time is unacceptable for it.

## Sample Run

```
RULE-BASED HELPDESK: coverage test

student message                                         fired  expected  verdict
----------------------------------------------------------------------------------------
How do I get a bonafide certificate?                       R1        R1  correct
I need proof of study for my passport                      R2        R2  correct
My warden says I need proof that I am studying here      None        R2  MISSED (fallback)
Where do I get a letter saying I study here?             None        R2  MISSED (fallback)
What is the last date for fee payment?                     R3        R3  correct
When are fees due?                                       None        R3  MISSED (fallback)
I want to apply for hostel leave                           R4        R4  correct
The hostel warden is on leave, who signs my form?          R4      None  WRONG RULE
How long does a transcript take?                           R5        R5  correct
Can I get my marksheet posted to me?                     None        R5  MISSED (fallback)

correct 5/10   missed 4   wrong rule 1
coverage 50 percent
```

Your exact numbers will differ, because your rules and test messages are your own. What should not differ is the shape: a respectable score on messages that use the trigger words, several misses on paraphrases, and at least one rule firing on something it was never meant for.

**Answer these questions after completing all tasks:**
- Your rule for hostel leave fires on "the hostel warden is on leave". Adding more words to the trigger would fix this one message. Write the next message that would break your improved rule, and say what that tells you about fixing brittleness by adding rules.
- Count how many rules you would need to reach 90 percent coverage on your test set. Then estimate how many you would need for the two hundred questions a real college helpdesk receives. What happens to your ability to predict what the system will do?
- Your engine returns the first matching rule. Two rules could match the same message. What does your code do in that case, and is that a decision you made deliberately or one the code made for you?

## Deliverables & Rubric

Submit your `.py` file, the printed output of your coverage test, and your written answers to Task 3 and the reflection questions.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| `respond()` returns the firing rule and reply, with a working fallback | 2 |
| Test set includes paraphrases and at least one misfiring message | 2 |
| Harness classifies all three outcomes and reports coverage | 2 |
| Four characteristics applied correctly to the student's own system | 2 |
| Written answers show a defensible position on failure modes | 1 |
| Code readability and organisation | 1 |
| **Total** | **10** |

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)

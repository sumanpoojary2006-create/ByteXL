"""Reference solution, Unit 1 mini project: rule-based helpdesk and its limits."""

RULES = [
    ("R1", {"bonafide"},            "Bonafide certificate: academic office, window 3."),
    ("R2", {"proof", "study"},      "Bonafide certificate: academic office, window 3."),
    ("R3", {"fee", "last", "date"}, "Fee deadline: 15th of the month."),
    ("R4", {"hostel", "leave"},     "Hostel leave form: warden's office."),
    ("R5", {"transcript"},          "Transcripts: apply online, seven working days."),
]
FALLBACK = "Sorry, I did not understand that. Please rephrase your question."


def tokenise(text):
    return {w.strip(".,!?'") for w in text.lower().split()}


def respond(message):
    """Return (rule_id, reply). Fires the first rule whose words are all present."""
    words = tokenise(message)
    for rule_id, trigger, reply in RULES:
        if trigger <= words:
            return rule_id, reply
    return None, FALLBACK


# Each entry is (what the student types, the rule that SHOULD handle it).
TESTS = [
    ("How do I get a bonafide certificate?",              "R1"),
    ("I need proof of study for my passport",             "R2"),
    ("My warden says I need proof that I am studying here","R2"),
    ("Where do I get a letter saying I study here?",      "R2"),
    ("What is the last date for fee payment?",            "R3"),
    ("When are fees due?",                                "R3"),
    ("I want to apply for hostel leave",                  "R4"),
    ("The hostel warden is on leave, who signs my form?", None),
    ("How long does a transcript take?",                  "R5"),
    ("Can I get my marksheet posted to me?",              "R5"),
]

print("RULE-BASED HELPDESK: coverage test")
print()
print(f"{'student message':<54} {'fired':>6} {'expected':>9}  verdict")
print("-" * 88)
correct = missed = wrong = 0
for message, expected in TESTS:
    fired, _ = respond(message)
    if fired == expected:
        verdict = "correct"; correct += 1
    elif fired is None:
        verdict = "MISSED (fallback)"; missed += 1
    else:
        verdict = "WRONG RULE"; wrong += 1
    print(f"{message[:54]:<54} {str(fired):>6} {str(expected):>9}  {verdict}")

total = len(TESTS)
print()
print(f"correct {correct}/{total}   missed {missed}   wrong rule {wrong}")
print(f"coverage {100 * correct / total:.0f} percent")

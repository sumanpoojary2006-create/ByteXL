"""Reference solution, Unit 3 mini project: clinic triage expert system."""

RULES = [
    ("R1", {"fever", "cough"},                      "respiratory_infection"),
    ("R2", {"respiratory_infection", "breathless"}, "chest_review_needed"),
    ("R3", {"fever", "rash"},                       "possible_dengue"),
    ("R4", {"possible_dengue", "low_platelets"},    "urgent_referral"),
    ("R5", {"chest_review_needed", "over_60"},      "urgent_referral"),
    ("R6", {"headache", "stiff_neck"},              "urgent_referral"),
    ("R7", {"respiratory_infection"},               "prescribe_rest"),
    ("R8", {"fever", "joint_pain"},                 "possible_dengue"),
    ("R9", {"dehydrated", "vomiting"},              "fluids_needed"),
]
OBSERVABLE = {"fever", "cough", "breathless", "rash", "low_platelets", "headache",
              "stiff_neck", "over_60", "joint_pain", "dehydrated", "vomiting"}

# Ground truth about this patient. Forward chaining needs all of it recorded
# up front; backward chaining discovers what it needs as it goes.
PATIENT = {"fever": True, "cough": True, "breathless": True, "over_60": True,
           "rash": False, "low_platelets": False, "headache": False,
           "stiff_neck": False, "joint_pain": False, "dehydrated": False,
           "vomiting": False}


def forward_chain(known):
    facts, fired = set(known), []
    changed = True
    while changed:
        changed = False
        for rid, conds, concl in RULES:
            if conds <= facts and concl not in facts:
                facts.add(concl); fired.append(rid); changed = True
    return facts, fired


def backward_chain(goal, asked, seen=None):
    seen = seen or set()
    if goal in OBSERVABLE:
        if goal not in asked:
            asked.append(goal)          # a question put to the nurse
        return PATIENT[goal]
    if goal in seen:
        return False
    seen = seen | {goal}
    for rid, conds, concl in RULES:
        if concl == goal and all(backward_chain(c, asked, seen) for c in sorted(conds)):
            return True
    return False


print("CLINIC TRIAGE: two ways to reach the same conclusion")
print(f"Rule base: {len(RULES)} rules over {len(OBSERVABLE)} observable signs")
print()

# Forward chaining is data-driven: the nurse must record everything first,
# because the engine cannot know in advance which signs will matter.
recorded = {s for s, present in PATIENT.items() if present}
facts, fired = forward_chain(recorded)
derived = sorted(facts - recorded)
print("FORWARD CHAINING, one goal (is this urgent?)")
print(f"   signs the nurse must record  {len(OBSERVABLE)}")
print(f"   rules fired                  {len(fired)}  ({', '.join(fired)})")
print(f"   conclusions derived          {len(derived)}  ({', '.join(derived)})")
print(f"   urgent?                      {'urgent_referral' in facts}")
print()

asked = []
proved = backward_chain("urgent_referral", asked)
print("BACKWARD CHAINING, same goal")
print(f"   questions asked              {len(asked)}  ({', '.join(asked)})")
print(f"   urgent?                      {proved}")
print()

GOALS = ["urgent_referral", "prescribe_rest", "fluids_needed", "chest_review_needed"]
total = 0
for g in GOALS:
    a = []
    backward_chain(g, a)
    total += len(a)
print(f"BACKWARD CHAINING, all {len(GOALS)} goals separately")
print(f"   questions asked across the four passes  {total}")
print()
print(f"One goal:   backward asks {len(asked)}, forward needs {len(OBSERVABLE)}. Backward wins.")
print(f"Four goals: backward asks {total}, forward still needs {len(OBSERVABLE)}. The advantage has gone.")
print("The more goals tested against the same facts, the better forward chaining looks.")

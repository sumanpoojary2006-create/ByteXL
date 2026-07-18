"""Build the benchmark-quality Unit 4 - Looping MCQ workbook.

Question content is stored in ``unit4_questions.json`` and is grounded only in
the Unit 4 reading materials. Set 1 contains 10 course MCQs; Set 2 contains 30
assessment MCQs. The answer field is 1..4 (A=1, B=2, C=3, D=4).
"""

import json
import os
import shutil
from collections import Counter

import openpyxl


TEMPLATE = "content/Question Bank/Template/questions-mcq-template.xlsx"
OUT_DIR = "content/Question Bank/MCQ/Python/Unit 4 - Looping"
OUT_FILE = os.path.join(OUT_DIR, "Unit 4 - Looping - MCQ.xlsx")
DATA_FILE = os.path.join(OUT_DIR, "unit4_questions.json")
SHEET_NAME = "Python - MCQ - 4"

LETTER_TO_NUMBER = {"A": 1, "B": 2, "C": 3, "D": 4}
SCORE = {"easy": 5, "medium": 8, "hard": 10}
HEADERS = [
    "title", "description", "explanation", "score", "status", "difficulty",
    "bloomTaxonomy", "tags", "subjects", "topics", "subTopics", "companies",
    "option1", "option2", "option3", "option4", "answer",
]


def load_questions():
    with open(DATA_FILE, encoding="utf-8") as source:
        questions = json.load(source)

    required = {
        "set", "difficulty", "bloom", "subtopic", "description",
        "explanation", "options", "answer",
    }
    assert len(questions) == 40, f"expected 40 questions, got {len(questions)}"
    assert all(set(item) == required for item in questions)
    assert all(item["difficulty"] in SCORE for item in questions)
    assert all(item["bloom"] in {"understand", "apply", "analyze"} for item in questions)
    assert all(item["answer"] in LETTER_TO_NUMBER for item in questions)
    assert all(len(item["options"]) == 4 for item in questions)
    assert all(len(set(item["options"])) == 4 for item in questions)
    assert all(item["description"].strip() and item["explanation"].strip() for item in questions)
    return questions


def validate_bank(questions):
    answer_tally = Counter(item["answer"] for item in questions)
    assert answer_tally == Counter({letter: 10 for letter in "ABCD"}), answer_tally

    set_tally = Counter(item["set"] for item in questions)
    assert set_tally == Counter({1: 10, 2: 30}), set_tally

    set1_answers = Counter(item["answer"] for item in questions[:10])
    assert sorted(set1_answers.values()) == [2, 2, 3, 3], set1_answers

    max_run = run = 1
    for previous, current in zip(questions, questions[1:]):
        run = run + 1 if previous["answer"] == current["answer"] else 1
        max_run = max(max_run, run)
    assert max_run <= 2, f"answer letter repeats {max_run} times consecutively"

    descriptions = [item["description"] for item in questions]
    assert len(descriptions) == len(set(descriptions)), "duplicate description found"

    for index, item in enumerate(questions, start=1):
        correct = item["options"][LETTER_TO_NUMBER[item["answer"]] - 1]
        assert correct.strip(), f"empty correct option at question {index}"

    return answer_tally, max_run


def build_rows(questions):
    counters = {1: 0, 2: 0}
    rows = []
    for item in questions:
        set_number = item["set"]
        counters[set_number] += 1
        options = item["options"]
        rows.append([
            f"Python - MCQ - 4.{set_number}.{counters[set_number]}",
            item["description"],
            item["explanation"],
            SCORE[item["difficulty"]],
            "published",
            item["difficulty"],
            item["bloom"],
            f"python - Set {set_number}",
            "python",
            "looping",
            item["subtopic"],
            None,
            options[0], options[1], options[2], options[3],
            LETTER_TO_NUMBER[item["answer"]],
        ])
    return rows


questions = load_questions()
answer_tally, max_run = validate_bank(questions)
rows = build_rows(questions)

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(TEMPLATE, OUT_FILE)
workbook = openpyxl.load_workbook(OUT_FILE)
worksheet = workbook.active
worksheet.title = SHEET_NAME
worksheet.delete_rows(2, worksheet.max_row)
for row in rows:
    worksheet.append(row)
for table in worksheet.tables.values():
    table.ref = f"A1:Q{len(rows) + 1}"
workbook.save(OUT_FILE)

check = openpyxl.load_workbook(OUT_FILE, read_only=True)[SHEET_NAME]
saved_rows = list(check.iter_rows(values_only=True))
assert list(saved_rows[0]) == HEADERS
assert len(saved_rows) == 41

print("Saved:", OUT_FILE)
print("Questions:", len(rows))
print("Answer distribution:", dict(sorted(answer_tally.items())))
print("Maximum consecutive answer run:", max_run)
print("Difficulty mix:", dict(Counter(item["difficulty"] for item in questions)))
print("Subtopic mix:", dict(Counter(item["subtopic"] for item in questions)))
print("Validation passed.")

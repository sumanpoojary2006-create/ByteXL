"""Build the benchmark-quality Unit 1 MCQ workbook from canonical JSON."""

import json
import os
import shutil
from collections import Counter

import openpyxl


TEMPLATE = "content/Question Bank/Template/questions-mcq-template.xlsx"
OUT_DIR = "content/Question Bank/MCQ/Python/Unit 1 - Introduction to Programming"
OUT_FILE = os.path.join(OUT_DIR, "Unit 1 - Introduction to Programming - MCQ.xlsx")
DATA_FILE = os.path.join(OUT_DIR, "unit1_questions.json")
SHEET_NAME = "Python - MCQ - 1"
UNIT = 1
TOPIC = "introduction-to-programming"

LETTER_TO_NUMBER = {"A": 1, "B": 2, "C": 3, "D": 4}
SCORE = {"easy": 5, "medium": 8, "hard": 10}
HEADERS = [
    "title", "description", "explanation", "score", "status", "difficulty",
    "bloomTaxonomy", "tags", "subjects", "topics", "subTopics", "companies",
    "option1", "option2", "option3", "option4", "answer",
]


def load_and_validate():
    with open(DATA_FILE, encoding="utf-8") as source:
        questions = json.load(source)
    assert len(questions) == 40
    assert Counter(item["answer"] for item in questions) == Counter({letter: 10 for letter in "ABCD"})
    assert Counter(item["set"] for item in questions) == Counter({1: 10, 2: 30})
    assert sorted(Counter(item["answer"] for item in questions[:10]).values()) == [2, 2, 3, 3]
    run = best = 1
    for previous, current in zip(questions, questions[1:]):
        run = run + 1 if previous["answer"] == current["answer"] else 1
        best = max(best, run)
    assert best <= 2
    assert all(item["difficulty"] in SCORE for item in questions)
    assert all(item["bloom"] in {"remember", "understand", "apply", "analyze"} for item in questions)
    assert all(len(item["options"]) == 4 and len(set(item["options"])) == 4 for item in questions)
    return questions


def build_rows(questions):
    counters = {1: 0, 2: 0}
    rows = []
    for item in questions:
        counters[item["set"]] += 1
        rows.append([
            f"Python - MCQ - {UNIT}.{item['set']}.{counters[item['set']]}",
            item["description"], item["explanation"], SCORE[item["difficulty"]],
            "published", item["difficulty"], item["bloom"],
            f"python - Set {item['set']}", "python", TOPIC, item["subtopic"], None,
            *item["options"], LETTER_TO_NUMBER[item["answer"]],
        ])
    return rows


questions = load_and_validate()
rows = build_rows(questions)
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(TEMPLATE, OUT_FILE)
workbook = openpyxl.load_workbook(OUT_FILE)
worksheet = workbook.active
worksheet.title = SHEET_NAME
worksheet.delete_rows(2, worksheet.max_row)
for row in rows:
    worksheet.append(row)
workbook.save(OUT_FILE)
print("Saved:", OUT_FILE)
print("Questions:", len(rows))
print("Answer distribution:", dict(Counter(item["answer"] for item in questions)))

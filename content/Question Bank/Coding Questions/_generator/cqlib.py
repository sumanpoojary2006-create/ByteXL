"""Shared library for building ByteXL coding-question xlsx files.

Design principle: the question author supplies the reference `solution` and the
raw testcase *inputs*.  The build step EXECUTES the solution to compute each
expected output, so testcases are correct by construction and every solution is
verified to run before it lands in the workbook.
"""

import subprocess
import sys
import textwrap
import openpyxl

# Exact column order used by the ByteXL coding-question uploader.
# Standard is 7 testcases per question (2 open + 5 hidden, enforced by the
# uploader's "public testcases (first N)" setting, not by any xlsx column).
NUM_TESTCASES = 7

TESTCASE_HEADERS = [
    f"testcase{i}_{field}"
    for i in range(1, NUM_TESTCASES + 1)
    for field in ("input", "output")
]

HEADERS = [
    "title", "description", "explanation", "score", "status", "difficulty",
    "bloomTaxonomy", "tags", "subjects", "topics", "subTopics", "companies",
    "codingType", "language", "supportAllLanguages", "enablePartialScore",
    "ignoreCase", *TESTCASE_HEADERS,
    "preloadCode_python", "solution_python", "hints",
]

DEFAULT_CONSTRAINTS = [
    "All numeric inputs are valid numbers in the ranges implied by the examples.",
    "Every value must be printed exactly as shown in the output format, with no "
    "extra text added or removed.",
]


def run_solution(code, stdin_text):
    """Run `code` with `stdin_text` on stdin; return stripped stdout.

    Raises RuntimeError if the program errors so bad solutions never ship.
    """
    proc = subprocess.run(
        [sys.executable, "-c", code],
        input=stdin_text,
        capture_output=True, text=True, timeout=15,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"solution crashed (rc={proc.returncode})\n"
            f"--- stdin ---\n{stdin_text}\n--- stderr ---\n{proc.stderr}"
        )
    # ByteXL compares trailing-newline-insensitively; strip trailing whitespace
    # per line and drop trailing blank lines.
    lines = proc.stdout.split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(line.rstrip() for line in lines)


def make_description(prose, input_lines, sample_output, constraints=None):
    """Assemble the markdown description block used by every question."""
    parts = [prose.strip(), "", "### Input Format"]
    for line in input_lines:
        parts.append(f"- {line}")
    parts += ["", "### Output Format", "```", sample_output, "```", "",
              "### Constraints"]
    for c in (constraints or DEFAULT_CONSTRAINTS):
        parts.append(f"- {c}")
    return "\n".join(parts)


def build_workbook(questions, out_path, *, defaults=None):
    """Validate + execute every question, then write the xlsx.

    `questions` is a list of dicts with keys:
      title, prose, difficulty, topics, subTopics, inputs (list of 3 strings),
      solution, and optional input_lines / constraints / score / hints / tags /
      explanation.
    """
    defaults = defaults or {}
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(HEADERS)

    report = []
    for q in questions:
        code = textwrap.dedent(q["solution"]).strip("\n")
        inputs = q["inputs"]
        assert len(inputs) == NUM_TESTCASES, (
            f"{q['title']}: need exactly {NUM_TESTCASES} testcases, got {len(inputs)}"
        )
        outputs = [run_solution(code, inp) for inp in inputs]

        desc = q.get("description") or make_description(
            q["prose"], q["input_lines"], outputs[0], q.get("constraints"),
        )
        row = {
            "title": q["title"],
            "description": desc,
            "explanation": q.get("explanation", ""),
            "score": q.get("score", 5),
            "status": "Published",
            "difficulty": q["difficulty"],
            "bloomTaxonomy": q.get("bloomTaxonomy", ""),
            "tags": q.get("tags", ""),
            "subjects": q.get("subjects", defaults.get("subjects", "python-fundamentals")),
            "topics": q["topics"],
            "subTopics": q["subTopics"],
            "companies": "",
            "codingType": "Programming",
            "language": "Python",
            "supportAllLanguages": False,
            "enablePartialScore": True,
            "ignoreCase": q.get("ignoreCase", True),
            **{
                f"testcase{i}_{field}": value
                for i, (inp, out) in enumerate(zip(inputs, outputs), start=1)
                for field, value in (("input", inp), ("output", out))
            },
            "preloadCode_python": q.get("preloadCode_python", ""),
            "solution_python": code,
            "hints": q.get("hints", ""),
        }
        ws.append([row[h] for h in HEADERS])
        report.append((q["title"], q["difficulty"], outputs[0].replace("\n", " | ")))

    wb.save(out_path)
    return report


def main(questions, out_path, *, defaults=None):
    """Convenience entry point: build, print a summary, verify counts."""
    from collections import Counter
    report = build_workbook(questions, out_path, defaults=defaults)
    diff = Counter(d for _, d, _ in report)
    print(f"Wrote {len(report)} questions -> {out_path}")
    print(f"  difficulty split: {dict(diff)}")
    for title, d, out in report:
        print(f"  [{d:6}] {title:42} -> {out[:50]}")
    return report

"""Question-bank business intelligence.

Reduces the ByteXL question bank, the archive vault and the test list into a
single compact fact table the browser can pivot without another round trip.

The upstream reads are slow and large (``/api/questions`` alone is ~245 MB and
takes about a minute), so a snapshot is built once and cached on disk. Every
metric the dashboard shows is derived client-side from the fact table, which
keeps filters instant and lets the Content Lead roster stay editable without a
redeploy.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any, Iterable, Optional

SNAPSHOT_PATH = Path(
    os.getenv("ANALYTICS_SNAPSHOT_PATH", Path(__file__).parent / ".analytics-snapshot.json")
)
# A short cache keeps normal page loads fast while making upstream changes appear
# on an open dashboard within a few minutes. The Refresh data button bypasses it.
SNAPSHOT_TTL_SECONDS = int(os.getenv("ANALYTICS_SNAPSHOT_TTL", str(5 * 60)))

QUESTION_TYPES = ["multipleChoice", "coding", "descriptive"]
DIFFICULTIES = ["easy", "medium", "hard", "unspecified"]

# Free-text difficulty entered by hand upstream. Anything unmapped becomes
# "unspecified" rather than silently inflating a real bucket.
DIFFICULTY_ALIASES = {
    "easy": "easy",
    "easu": "easy",
    "rudimentary": "easy",
    "medium": "medium",
    "meidum": "medium",
    "moderate": "medium",
    "conceptual": "medium",
    "hard": "hard",
    "difficult": "hard",
}

# Company names are typed per question, so the same employer arrives in several
# spellings. Values that mean "no company" are dropped instead of normalized.
COMPANY_ALIASES = {
    "cts": "Cognizant",
    "cognizant": "Cognizant",
    "tcs": "TCS",
    "techmahindra": "Tech Mahindra",
    "tech mahindra": "Tech Mahindra",
    "tech-mahindra": "Tech Mahindra",
    "microscoft": "Microsoft",
    "microsoft": "Microsoft",
    "infosys": "Infosys",
    "wipro": "Wipro",
    "accenture": "Accenture",
    "capgemini": "Capgemini",
    "deloitte": "Deloitte",
    "hcl": "HCL",
    "hexaware": "Hexaware",
    "lti-mindtree": "LTIMindtree",
    "ltimindtree": "LTIMindtree",
    "nokia": "Nokia",
    "amazon": "Amazon",
    "google": "Google",
    "ibm": "IBM",
    "oracle": "Oracle",
    "bytexl": "byteXL",
    "aws": "AWS",
    "azure": "Azure",
}
COMPANY_NON_VALUES = {
    "na", "n/a", "-", "--", "", "general", "none", "advanced", "nil", "nan",
    # Placeholder values left behind by bulk uploads and the sample sheet.
    "sample", "sample-company", "test", "string", "abc", "xyz", "company",
}

# Ordered rules: the first pattern that matches a subject wins, so specific course
# subjects are tested before the broad institution catch-all. Questions carrying no
# subject at all get their own bucket rather than joining "Other", because 34% of the
# bank is in that state and it is a data-quality number, not a track.
TRACK_RULES: list[tuple[str, str]] = [
    (r"^\(no-subject\)$", "Unassigned Subject"),
    (r"(company-specific)", "Company-Specific Prep"),
    (r"^tactical", "Tactical Drills"),
    (r"(algorithm|data-structure|^dsa$|competitive)", "DSA & Problem Solving"),
    (r"(machine-learning|natural-language|exploratory-data|generative-ai|artificial-intelligence|intro-to-ai|deep-learning|^dl$|data-science|data-engineering|data-visualization|excel|power-?bi|tableau|analytics|streamlit)", "Data, AI & Analytics"),
    (r"(web-development|frontend|backend|node|react|angular|full-?stack|javascript|^html|^css|mongodb|mean-stack|mern)", "Web & Backend"),
    (r"(cloud|security|devops|aws|azure|^az\d|^ai900|^dp\d|^sc\d|^ms\d)", "Cloud & Security"),
    (r"(rdbms|dbms|sql|database)", "Databases"),
    (r"(operating-system|computer-network|computer-fundamental|cs-fundamental|computer-organization|software-engineering|software-testing)", "CS Core & Engineering"),
    (r"(c-programming|cpp|c\+\+|python|java|oops|object-oriented|programming|pseudocode)", "Programming Fundamentals"),
    (r"(verbal|english|communication|career-readiness|aptitude|reasoning|product-thinking|design-thinking|psychometric|soft-skill)", "Aptitude & Communication"),
    (r"(custom-course|st-mary|jntuk|adityau|university|college|-course$)", "Institution Custom"),
]
TRACK_FALLBACK = "Other / Unclassified"

# The eight Content Leads are the roster confirmed by the content manager; everyone
# else authoring in the bank is a Platform Support Engineer, with the manager and the
# system account called out so they don't distort the curated-vs-uploaded split. The
# dashboard exposes this as an editable roster, so a team change is corrected in the
# UI rather than in code.
DEFAULT_ROLES = {
    "Akila Rengarajan": "lead",
    "Anshul Kumar": "lead",
    "Badal Kumar": "lead",
    "Suman Poojary": "lead",
    "Priya Sharma": "lead",
    "Darsh Nath Segal": "lead",
    "Jai Gupta": "lead",
    "Shashwat Tripathi": "lead",
    "Smaranjit Ghose": "manager",
    "Rohith Kokkirala": "support",
    "Mahesh K": "support",
    "Sravanth Kumar  Chintalacheruvu": "support",
    "Prabhakar Chitikela": "support",
    "Prasanth Y": "support",
    "Kondakavuri Pavani": "support",
    "Karunakar Pothuganti": "support",
    "Karthik Divi": "support",
    "Ayush Walekar": "support",
    "Jai Bytexl": "support",
    "Super Admin": "system",
    "Reshma": "support",
    "Pavani K": "support",
    "Maheedhar K": "support",
    "MEGHANA KAVALA": "support",
    "Mrunalini Kulkarni": "support",
    "Ruchira": "support",
    "Shahbaj Alam": "support",
}

MOCK_TAG_RE = re.compile(r"mock[\s_-]*test|mocktest", re.IGNORECASE)
PLACEHOLDER_TAXONOMY = {"sample-topic", "sample-subtopic", "sample-subject", "string", "test"}


def norm_difficulty(raw: Any) -> str:
    key = str(raw or "").strip().lower()
    return DIFFICULTY_ALIASES.get(key, "unspecified")


def norm_company(raw: Any) -> Optional[str]:
    key = str(raw or "").strip()
    if key.lower() in COMPANY_NON_VALUES:
        return None
    return COMPANY_ALIASES.get(key.lower(), key)


def track_for_subject(subject: str) -> str:
    """Map a free-text subject onto a track.

    Subjects are typed by hand upstream and mix separators ("Software Testing"
    vs "software-testing"), so separators are normalized to hyphens before the
    patterns run.
    """
    key = str(subject or "").strip().lower()
    if not key:
        return TRACK_FALLBACK
    key = re.sub(r"[\s_]+", "-", key)
    for pattern, track in TRACK_RULES:
        if re.search(pattern, key):
            return track
    return TRACK_FALLBACK


def _first(values: Any, default: str = "") -> str:
    """The primary taxonomy value, ignoring upstream placeholder entries.

    Questions carry list-valued subjects/topics but are authored against one
    subject in practice (118 of 123k have a second). Placeholders like
    "sample-topic" are dropped so they don't masquerade as a real topic.
    """
    if not isinstance(values, list):
        return default
    for value in values:
        text = str(value or "").strip()
        if text and text.lower() not in PLACEHOLDER_TAXONOMY:
            return text
    return default


class Interner:
    """Assigns each distinct string a stable index for columnar encoding."""

    def __init__(self) -> None:
        self.values: list[str] = []
        self._index: dict[str, int] = {}

    def add(self, value: str) -> int:
        if value not in self._index:
            self._index[value] = len(self.values)
            self.values.append(value)
        return self._index[value]


def build_fact_table(
    live: Iterable[dict[str, Any]],
    vault: Iterable[dict[str, Any]],
    tests: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Reduce the three upstream payloads to one dictionary-encoded fact table."""
    authors = Interner()
    subjects = Interner()
    topics = Interner()
    companies = Interner()
    months = Interner()

    cols: dict[str, list[int]] = {k: [] for k in ("cm", "am", "ty", "df", "au", "su", "tp", "co", "mk", "ex", "st")}

    def ingest(question: dict[str, Any], archived: bool) -> None:
        created = str(question.get("created") or "")[:7]
        if not created:
            return
        subject = _first(question.get("subjects"), "(no subject)")
        company_values = [c for c in (norm_company(c) for c in (question.get("companies") or [])) if c]
        tags = [str(t) for t in (question.get("tags") or [])]
        is_mock = bool(company_values) or subject == "company-specific" or any(MOCK_TAG_RE.search(t) for t in tags)
        archived_month = str(question.get("_archived_at") or "")[:7]

        cols["cm"].append(months.add(created))
        cols["am"].append(months.add(archived_month) if archived_month else -1)
        qtype = question.get("type")
        cols["ty"].append(QUESTION_TYPES.index(qtype) if qtype in QUESTION_TYPES else 0)
        cols["df"].append(DIFFICULTIES.index(norm_difficulty(question.get("difficulty"))))
        cols["au"].append(authors.add(str((question.get("createdBy") or {}).get("name") or "(unattributed)")))
        cols["su"].append(subjects.add(subject))
        cols["tp"].append(topics.add(_first(question.get("topics"), "(no topic)")))
        cols["co"].append(companies.add(company_values[0]) if company_values else -1)
        cols["mk"].append(1 if is_mock else 0)
        cols["ex"].append(1 if str(question.get("explanation") or "").strip() else 0)
        cols["st"].append(1 if archived else 0)

    for question in live:
        ingest(question, archived=False)
    for question in vault:
        ingest(question, archived=True)

    return {
        "dims": {
            "authors": authors.values,
            "subjects": subjects.values,
            "topics": topics.values,
            "companies": companies.values,
            "months": months.values,
            "types": QUESTION_TYPES,
            "difficulties": DIFFICULTIES,
        },
        "cols": cols,
        "tracks": {s: track_for_subject(s) for s in subjects.values},
        "roles": DEFAULT_ROLES,
        "tests": summarize_tests(tests),
        "counts": {"live": sum(1 for v in cols["st"] if v == 0), "archived": sum(cols["st"])},
    }


def summarize_tests(tests: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Per-test rows for the assessment coverage panels.

    Kept as rows rather than pre-aggregated counts so the dashboard can filter
    them by month and intent alongside the question metrics.
    """
    rows = []
    for test in tests:
        tags = [str(t) for t in (test.get("tags") or [])]
        title = str(test.get("title") or "")
        blob = f"{title} {' '.join(tags)}"
        companies = sorted({
            c for c in (norm_company(m) for m in re.findall(
                r"\b(TCS|NQT|Accenture|Infosys|Wipro|Capgemini|Deloitte|Cognizant|CTS|Tech[\s-]?Mahindra|HCL|Hexaware|Amazon|Google|Microsoft|IBM|Oracle|LTI[\s-]?Mindtree|Nokia)\b",
                blob, re.IGNORECASE)) if c
        })
        standardized = test.get("testIntent") == "standardizedAssessment" or any(
            "standardi" in t.lower() for t in tags
        )
        rows.append({
            "id": test.get("_id"),
            "title": title,
            "month": str(test.get("created") or "")[:7],
            "intent": test.get("testIntent") or "unset",
            "questions": test.get("questionsCount") or 0,
            "author": (test.get("createdBy") or {}).get("name") or "(unattributed)",
            "tags": tags,
            "companies": companies,
            "standardized": standardized,
            "mock": bool(MOCK_TAG_RE.search(blob)) or bool(companies),
            "subject": subject_from_test_title(title),
        })
    return {"rows": rows}


def subject_from_test_title(title: str) -> str:
    """The course a standardized assessment covers, read off its title.

    Tests carry no subject field, but standardized ones are named
    "<Course> - Assessment <n>" or "Standardized Assessment - <Course> - <unit>".
    """
    text = str(title or "").strip()
    text = re.sub(r"^standardi[sz]ed assessments?\s*[-–:]\s*", "", text, flags=re.IGNORECASE)
    parts = re.split(r"\s*[-–]\s*", text)
    head = parts[0] if parts else text
    head = re.sub(r"\s*\(v\d+\)\s*$", "", head).strip()
    head = re.sub(r"\s+(assessment|mock test|test|quiz)\s*\d*$", "", head, flags=re.IGNORECASE).strip()
    return head or "(untitled)"


def load_snapshot(fetch_items, force: bool = False) -> dict[str, Any]:
    """Return the cached fact table, rebuilding it when stale or forced.

    ``fetch_items`` takes an API path and returns an iterable of records — a
    list or a lazy generator. Injecting it keeps this module free of the
    server's auth and HTTP concerns, and lets the server stream a 245 MB
    response instead of materializing it.
    """
    if not force and SNAPSHOT_PATH.exists():
        age = time.time() - SNAPSHOT_PATH.stat().st_mtime
        if age < SNAPSHOT_TTL_SECONDS:
            try:
                snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
                snapshot["cached"] = True
                snapshot["ageSeconds"] = int(age)
                return snapshot
            except (ValueError, OSError):
                pass  # Unreadable cache is a rebuild, not an error.

    started = time.time()
    # Consumed lazily and in order inside build_fact_table, so at most one bulk
    # response is open at a time. Do not wrap these in list().
    snapshot = build_fact_table(
        fetch_items("/api/questions"),
        fetch_items("/api/questions-vault"),
        fetch_items("/api/tests?builderListView=true"),
    )
    snapshot["generatedAt"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    snapshot["buildSeconds"] = round(time.time() - started, 1)
    snapshot["cached"] = False
    snapshot["ageSeconds"] = 0

    try:
        SNAPSHOT_PATH.write_text(json.dumps(snapshot, separators=(",", ":")), encoding="utf-8")
    except OSError:
        pass  # A read-only deploy still serves the freshly built snapshot.
    return snapshot

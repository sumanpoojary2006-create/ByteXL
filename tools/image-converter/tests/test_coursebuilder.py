import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import coursebuilder


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #

DONOR_ID = "prod1"


def tree(*pages):
    """One donor product with a single section holding ``pages``."""
    return {
        DONOR_ID: {
            "title": "Modern Python Programming",
            "contentSections": [
                {
                    "_id": "sec1",
                    "title": "Strings",
                    "contentPages": [{"_id": pid, "title": title} for pid, title in pages],
                }
            ],
        }
    }


def blueprint(*topics):
    return {
        "slug": "demo",
        "title": "Demo Course",
        "description": "Tactical Course",
        "sources": [{"productId": DONOR_ID, "title": "Modern Python Programming"}],
        "units": [
            {
                "number": 1,
                "title": "Basics",
                "courseOutcome": "CO1",
                "hours": 8,
                "chapters": [{"number": "1.1", "title": "Working with Strings", "topics": list(topics)}],
            }
        ],
    }


def pinned(title, page_id, page_title):
    return {
        "title": title,
        "source": {
            "productId": DONOR_ID,
            "productTitle": "Modern Python Programming",
            "sectionTitle": "Strings",
            "pageId": page_id,
            "pageTitle": page_title,
        },
    }


def stats(**pages):
    return {
        page_id: {"words": words, "images": 1, "codeBlocks": 2, "ok": True}
        for page_id, words in pages.items()
    }


def only_topic(plan):
    return plan["units"][0]["chapters"][0]["topics"][0]


# --------------------------------------------------------------------------- #
# Title folding and section flattening
# --------------------------------------------------------------------------- #

def test_normalize_title_folds_punctuation_and_backticks():
    assert coursebuilder.normalize_title("`str.split()` & Joining") == "str split and joining"
    assert coursebuilder.normalize_title("Type Conversion (Casting) and type()") == \
        coursebuilder.normalize_title("type conversion casting and type")


def test_section_title_carries_unit_and_chapter():
    unit = {"number": 5, "title": "Files and OOP"}
    chapter = {"number": "5.2", "title": "Modules and Packages"}
    assert coursebuilder.section_title(unit, chapter) == "5.2 - Modules and Packages"


def test_section_title_falls_back_to_the_unit_number():
    assert coursebuilder.section_title({"number": 3}, {"title": "Strings"}) == "3 - Strings"


# --------------------------------------------------------------------------- #
# Source resolution
# --------------------------------------------------------------------------- #

def test_pinned_page_resolves_by_id():
    index = coursebuilder.index_donor_pages(tree(("p1", "Indexing and slicing")))
    entry, status, detail = coursebuilder.resolve_source(
        {"productId": DONOR_ID, "pageId": "p1", "pageTitle": "Indexing and slicing"}, index
    )
    assert status == coursebuilder.STATUS_REUSE
    assert entry["pageId"] == "p1"
    assert detail == ""


def test_renamed_page_id_heals_through_the_recorded_title():
    """A donor page that was recreated keeps its title but loses its id."""
    index = coursebuilder.index_donor_pages(tree(("p9", "Indexing and slicing")))
    entry, status, detail = coursebuilder.resolve_source(
        {"productId": DONOR_ID, "pageId": "p1", "pageTitle": "Indexing and slicing"}, index
    )
    assert status == coursebuilder.STATUS_MOVED
    assert entry["pageId"] == "p9"
    assert "p1" in detail and "p9" in detail


def test_missing_page_with_no_title_match_is_reported_not_guessed():
    index = coursebuilder.index_donor_pages(tree(("p9", "Something else")))
    entry, status, detail = coursebuilder.resolve_source(
        {"productId": DONOR_ID, "pageId": "p1", "pageTitle": "Indexing and slicing"}, index
    )
    assert entry is None
    assert status == coursebuilder.STATUS_MISSING
    assert "Indexing and slicing" in detail


def test_ambiguous_title_match_refuses_to_pick_one():
    index = coursebuilder.index_donor_pages(
        tree(("p8", "Indexing and slicing"), ("p9", "Indexing and slicing"))
    )
    entry, status, detail = coursebuilder.resolve_source(
        {"productId": DONOR_ID, "pageId": "p1", "pageTitle": "Indexing and slicing"}, index
    )
    assert entry is None
    assert status == coursebuilder.STATUS_MISSING
    assert "ambiguous" in detail


def test_unloaded_donor_product_is_missing_rather_than_a_crash():
    index = coursebuilder.index_donor_pages(tree(("p1", "Indexing and slicing")))
    entry, status, detail = coursebuilder.resolve_source(
        {"productId": "nope", "pageId": "p1"}, index
    )
    assert entry is None
    assert status == coursebuilder.STATUS_MISSING
    assert "nope" in detail


# --------------------------------------------------------------------------- #
# Plan
# --------------------------------------------------------------------------- #

def test_plan_reuses_a_healthy_donor_and_reports_its_metrics():
    plan = coursebuilder.build_plan(
        blueprint(pinned("String Indexing and Slice Operations", "p1", "Indexing and slicing")),
        tree(("p1", "Indexing and slicing")),
        stats(p1=833),
    )
    topic = only_topic(plan)
    assert topic["status"] == coursebuilder.STATUS_REUSE
    assert topic["sectionTitle"] == "1.1 - Working with Strings"
    assert topic["source"]["pageTitle"] == "Indexing and slicing"
    assert topic["stats"]["words"] == 833
    assert plan["totals"]["reuse"] == 1
    assert plan["totals"]["reusedWords"] == 833
    assert plan["canCreate"] is True


def test_thin_donor_is_flagged_but_does_not_block():
    plan = coursebuilder.build_plan(
        blueprint(pinned("Method Overloading and Overriding", "p1", "Overloading")),
        tree(("p1", "Overloading")),
        stats(p1=207),
    )
    topic = only_topic(plan)
    assert topic["status"] == coursebuilder.STATUS_THIN
    assert "207 words" in topic["detail"]
    assert plan["totals"]["thin"] == 1
    assert plan["canCreate"] is True


def test_author_new_topic_becomes_a_gap_and_still_allows_creation():
    plan = coursebuilder.build_plan(
        blueprint({"title": "Pass by Object Reference", "authorNew": True, "note": "Nothing covers it"}),
        tree(("p1", "Indexing and slicing")),
        stats(p1=833),
    )
    topic = only_topic(plan)
    assert topic["status"] == coursebuilder.STATUS_AUTHOR
    assert topic["source"] is None
    assert plan["gaps"] == [
        {
            "position": 1,
            "title": "Pass by Object Reference",
            "sectionTitle": "1.1 - Working with Strings",
            "note": "Nothing covers it",
        }
    ]
    assert plan["canCreate"] is True


def test_unresolvable_pin_blocks_creation():
    plan = coursebuilder.build_plan(
        blueprint(pinned("String Indexing", "gone", "Vanished")),
        tree(("p1", "Indexing and slicing")),
        stats(p1=833),
    )
    assert only_topic(plan)["status"] == coursebuilder.STATUS_MISSING
    assert plan["totals"]["missing"] == 1
    assert plan["canCreate"] is False
    assert plan["blockers"][0]["title"] == "String Indexing"


def test_donor_that_could_not_be_read_blocks_rather_than_shipping_empty():
    """The upload path once blanked 16 lessons; an unreadable donor must stop here."""
    plan = coursebuilder.build_plan(
        blueprint(pinned("String Indexing", "p1", "Indexing and slicing")),
        tree(("p1", "Indexing and slicing")),
        {"p1": {"ok": False, "error": "502 Bad Gateway", "words": 0}},
    )
    assert only_topic(plan)["status"] == coursebuilder.STATUS_MISSING
    assert plan["canCreate"] is False


def test_a_donor_used_twice_is_called_out_on_the_second_topic():
    plan = coursebuilder.build_plan(
        blueprint(
            pinned("Creating Strings", "p1", "Indexing and slicing"),
            pinned("Slice Operations", "p1", "Indexing and slicing"),
        ),
        tree(("p1", "Indexing and slicing")),
        stats(p1=833),
    )
    first, second = plan["units"][0]["chapters"][0]["topics"]
    assert first["detail"] == ""
    assert "already fills 'Creating Strings'" in second["detail"]


def test_totals_and_coverage_count_every_reusable_status():
    plan = coursebuilder.build_plan(
        blueprint(
            pinned("A", "p1", "One"),
            pinned("B", "p2", "Two"),
            {"title": "C", "authorNew": True, "note": "gap"},
            {"title": "D", "authorNew": True, "note": "gap"},
        ),
        tree(("p1", "One"), ("p2", "Two")),
        stats(p1=800, p2=200),
    )
    totals = plan["totals"]
    assert (totals["topics"], totals["reuse"], totals["thin"], totals["author"]) == (4, 1, 1, 2)
    assert totals["coverage"] == 0.5
    assert plan["sources"][0]["used"] == 2


def test_empty_blueprint_cannot_be_created():
    plan = coursebuilder.build_plan(
        {"slug": "empty", "title": "Empty", "sources": [], "units": []}, {}, {}
    )
    assert plan["totals"]["topics"] == 0
    assert plan["totals"]["coverage"] == 0.0
    assert plan["canCreate"] is False


# --------------------------------------------------------------------------- #
# Creation helpers
# --------------------------------------------------------------------------- #

def test_creation_steps_follow_blueprint_order():
    plan = coursebuilder.build_plan(
        blueprint(
            pinned("A", "p1", "One"),
            {"title": "B", "authorNew": True, "note": "gap"},
        ),
        tree(("p1", "One")),
        stats(p1=800),
    )
    steps = coursebuilder.creation_steps(plan)
    assert steps == [
        {
            "sectionTitle": "1.1 - Working with Strings",
            "topics": [
                {"title": "A", "sourcePageId": "p1", "authorNew": False},
                {"title": "B", "sourcePageId": None, "authorNew": True},
            ],
        }
    ]


def test_placeholder_markdown_names_the_topic_and_the_reason():
    body = coursebuilder.placeholder_markdown(
        "Command Line Arguments with sys.argv", {"title": "NHCE - Python"}, "No page covers sys.argv"
    )
    assert body.startswith("# Command Line Arguments with sys.argv")
    assert "has not been written yet" in body
    assert "No page covers sys.argv" in body
    assert "NHCE - Python" in body


def test_measure_markdown_counts_images_and_code_fences():
    measured = coursebuilder.measure_markdown("# T\n![a](x)\n```py\nprint(1)\n```\nsome words here")
    assert measured["images"] == 1
    assert measured["codeBlocks"] == 1
    assert measured["words"] == 9


def test_measure_markdown_tolerates_a_missing_body():
    assert coursebuilder.measure_markdown(None) == {
        "words": 0, "chars": 0, "images": 0, "codeBlocks": 0
    }


# --------------------------------------------------------------------------- #
# Page stats caching
# --------------------------------------------------------------------------- #

def test_collect_page_stats_reads_each_page_once(tmp_path, monkeypatch):
    monkeypatch.setattr(coursebuilder, "PAGE_CACHE_PATH", tmp_path / "cache.json")
    calls = []

    def fetch(page_id):
        calls.append(page_id)
        return {"title": page_id, "markdown": "word " * 500}

    result = coursebuilder.collect_page_stats(["p1", "p1", "p2", ""], fetch, now=1000.0)
    assert calls == ["p1", "p2"]
    assert result["p1"]["words"] == 500

    # A second call inside the TTL is served from the file written above.
    calls.clear()
    again = coursebuilder.collect_page_stats(["p1", "p2"], fetch, now=1000.0 + 60)
    assert calls == []
    assert again["p1"]["words"] == 500


def test_collect_page_stats_refetches_once_the_cache_expires(tmp_path, monkeypatch):
    monkeypatch.setattr(coursebuilder, "PAGE_CACHE_PATH", tmp_path / "cache.json")
    calls = []

    def fetch(page_id):
        calls.append(page_id)
        return {"markdown": "word " * 10}

    coursebuilder.collect_page_stats(["p1"], fetch, now=0.0)
    coursebuilder.collect_page_stats(["p1"], fetch, now=coursebuilder.PAGE_CACHE_TTL_SECONDS + 1)
    assert calls == ["p1", "p1"]


def test_a_failing_page_read_is_recorded_rather_than_raised(tmp_path, monkeypatch):
    monkeypatch.setattr(coursebuilder, "PAGE_CACHE_PATH", tmp_path / "cache.json")

    def fetch(page_id):
        raise RuntimeError("404 Topic not found")

    result = coursebuilder.collect_page_stats(["p1"], fetch, now=0.0)
    assert result["p1"]["ok"] is False
    assert "404" in result["p1"]["error"]


# --------------------------------------------------------------------------- #
# Blueprints on disk
# --------------------------------------------------------------------------- #

def test_load_blueprint_rejects_a_traversing_slug():
    with pytest.raises(FileNotFoundError):
        coursebuilder.load_blueprint("../../server")


def test_load_blueprint_rejects_an_empty_slug():
    with pytest.raises(FileNotFoundError):
        coursebuilder.load_blueprint("")


def test_installed_blueprints_are_listed_with_their_counts():
    summaries = {item["slug"]: item for item in coursebuilder.list_blueprints()}
    assert "nhce-python" in summaries
    nhce = summaries["nhce-python"]
    assert nhce["courseCode"] == "25CSE144"
    assert (nhce["units"], nhce["chapters"], nhce["topics"]) == (5, 19, 89)


@pytest.mark.parametrize("slug", ["nhce-python", "nhce-python-lab"])
def test_shipped_blueprints_are_well_formed(slug):
    """Every topic must carry a title and either a full pin or an explained gap."""
    bp = coursebuilder.load_blueprint(slug)
    assert bp["slug"] == slug
    seen_sections = set()
    for unit in bp["units"]:
        for chapter in unit["chapters"]:
            section = coursebuilder.section_title(unit, chapter)
            assert section not in seen_sections, f"duplicate section {section}"
            seen_sections.add(section)
            assert chapter["topics"], f"{section} has no topics"
            for topic in chapter["topics"]:
                assert topic.get("title")
                if topic.get("authorNew"):
                    assert topic.get("note"), f"{topic['title']} is a gap with no explanation"
                else:
                    source = topic["source"]
                    assert source["productId"] and source["pageId"] and source["pageTitle"]


def test_nhce_blueprint_pins_only_declared_donor_products():
    bp = coursebuilder.load_blueprint("nhce-python")
    declared = {source["productId"] for source in bp["sources"]}
    used = {
        topic["source"]["productId"]
        for unit in bp["units"]
        for chapter in unit["chapters"]
        for topic in chapter["topics"]
        if topic.get("source")
    }
    assert used <= declared


def test_nhce_blueprint_covers_all_five_syllabus_modules_in_order():
    bp = coursebuilder.load_blueprint("nhce-python")
    assert [unit["number"] for unit in bp["units"]] == [1, 2, 3, 4, 5]
    assert [unit["title"] for unit in bp["units"]] == [
        "Basics of Python",
        "Loops, Control Statements and Functions",
        "Strings and Exception Handling",
        "List, Set, Dictionary and Tuple",
        "Files and Object-Oriented Programming",
    ]
    assert all(unit["hours"] == 8 for unit in bp["units"])


def test_nhce_lab_blueprint_is_entirely_unwritten():
    """The lab manual does not exist anywhere yet; the plan must say so."""
    bp = coursebuilder.load_blueprint("nhce-python-lab")
    topics = [t for u in bp["units"] for c in u["chapters"] for t in c["topics"]]
    assert bp["sources"] == []
    assert all(topic.get("authorNew") for topic in topics)
    assert len(topics) == 14

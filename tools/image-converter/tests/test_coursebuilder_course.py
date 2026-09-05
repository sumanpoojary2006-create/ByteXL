"""The platform Course Builder object (``/api/courses``), distinct from the
reading-material product tested in ``test_coursebuilder.py``.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import coursebuilder


def blueprint(*units):
    return {"slug": "demo", "title": "Demo", "units": list(units)}


def unit(number, title, *chapters):
    return {"number": number, "title": title, "chapters": list(chapters)}


def chapter(number, title, *topic_titles, course_chapter=None):
    ch = {"number": number, "title": title,
          "topics": [{"title": t} for t in topic_titles]}
    if course_chapter is not None:
        ch["courseChapter"] = course_chapter
    return ch


def reading(reading_id="R1", title="Demo Course", *sections):
    return {"_id": reading_id, "title": title, "contentSections": list(sections)}


def section(title, *pages):
    return {"title": title, "contentPages": [{"_id": pid, "title": t} for pid, t in pages]}


def counting_ids():
    n = [0]
    def make():
        n[0] += 1
        return f"id{n[0]}"
    return make


# --------------------------------------------------------------------------- #
# slugify / URL building
# --------------------------------------------------------------------------- #

def test_slugify_matches_live_bytexl_examples():
    """Every case here is a real lesson title checked against the URL the
    platform actually stores for it."""
    cases = {
        "Type Conversion (Casting) and type()": "type-conversion-casting-and-type",
        "Comparison (Relational) Operators": "comparison-relational-operators",
        "Match-case: Python's switch-style Structure": "match-case-python-s-switch-style-structure",
        "How Computers Work: Inputs, Processing, and Outputs (IPO)":
            "how-computers-work-inputs-processing-and-outputs-ipo",
        "Args and kwargs": "args-and-kwargs",
        # Underscores are word characters to ByteXL, not separators.
        "Python Variable_ Namespace and Scoping": "python-variable_-namespace-and-scoping",
        # A leading separator keeps its hyphen; only the trailing one is dropped.
        " Branching and Merging": "-branching-and-merging",
    }
    for text, expected in cases.items():
        assert coursebuilder.slugify(text) == expected, text


def test_slugify_preserves_dunders_in_python_titles():
    """Folding ``__init__`` to ``init`` yields a URL that resolves to nothing."""
    assert coursebuilder.slugify("Packages and __init__.py") == "packages-and-__init__-py"
    assert coursebuilder.slugify("Initializing Objects: the __init__ Constructor") == \
        "initializing-objects-the-__init__-constructor"


def test_slugify_collapses_runs_and_strips_only_the_trailing_hyphen():
    assert coursebuilder.slugify("  Hello,,  World!!  ") == "-hello-world"
    assert coursebuilder.slugify("Trailing punctuation...") == "trailing-punctuation"
    assert coursebuilder.slugify("") == ""
    assert coursebuilder.slugify(None) == ""


def test_reading_material_url_shape():
    url = coursebuilder.reading_material_url(
        "44zu958mx", "NHCE - Problem Solving Using Python", "p1",
        "1.1 - Algorithms and Flowcharts", "Algorithms: Designing Step-by-Step Logic",
    )
    assert url == (
        "https://app.bytexl.ai/reading/44zu958mx/nhce-problem-solving-using-python/"
        "p1/1-1-algorithms-and-flowcharts/algorithms-designing-step-by-step-logic"
    )


# --------------------------------------------------------------------------- #
# blueprint_skeleton
# --------------------------------------------------------------------------- #

def test_blueprint_skeleton_carries_titles_and_section_names_only():
    bp = blueprint(unit(1, "Basics", chapter("1.1", "Strings", "Indexing", "Slicing")))
    skeleton = coursebuilder.blueprint_skeleton(bp)
    assert skeleton == {
        "units": [{
            "number": 1, "title": "Basics",
            "chapters": [{
                "sectionTitle": "1.1 - Strings", "title": "Strings",
                "courseChapter": "Strings",
                "topics": [{"title": "Indexing"}, {"title": "Slicing"}],
            }],
        }]
    }


def test_a_chapter_without_an_explicit_course_chapter_keeps_its_own_title():
    bp = blueprint(unit(1, "Basics", chapter("1.1", "Working with Strings", "Indexing")))
    skeleton = coursebuilder.blueprint_skeleton(bp)
    assert skeleton["units"][0]["chapters"][0]["courseChapter"] == "Working with Strings"


# --------------------------------------------------------------------------- #
# build_course_structure
# --------------------------------------------------------------------------- #

def test_every_topic_with_a_matching_page_becomes_a_subtopic():
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.1", "Strings", "Indexing and slicing")))
    )
    tree = reading("R1", "Demo", section("1.1 - Strings", ("p1", "Indexing and slicing")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())

    assert result["totals"] == {"modules": 1, "topics": 1, "subTopics": 1, "excluded": 0}
    module = result["modules"][0]
    assert module["title"] == "Unit 1 - Basics"
    topic = module["topics"][0]
    assert topic["title"] == "Strings"
    sub = topic["subTopics"][0]
    assert sub["title"] == "Indexing and slicing"
    assert sub["topicType"] == "readingMaterial"
    assert sub["data"] == (
        "https://app.bytexl.ai/reading/R1/demo/p1/1-1-strings/indexing-and-slicing"
    )
    assert sub["time"] == 0


def test_a_topic_with_no_matching_page_is_excluded_not_stubbed():
    """This is how a topic left out at reading-material creation time (skipAuthorNew)
    disappears from the course too, without any special-casing here."""
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.1", "Functions",
                                             "Creating a Function", "Pass by Object Reference")))
    )
    tree = reading("R1", "Demo", section("1.1 - Functions", ("p1", "Creating a Function")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())

    assert result["totals"]["subTopics"] == 1
    assert result["totals"]["excluded"] == 1
    assert result["excluded"] == [{"sectionTitle": "1.1 - Functions", "title": "Pass by Object Reference"}]


def test_a_chapter_that_loses_every_topic_produces_no_empty_module_topic():
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.1", "Nothing Written", "Ghost Topic")))
    )
    tree = reading("R1", "Demo", section("1.1 - Nothing Written"))  # no pages at all
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())

    assert result["modules"] == []
    assert result["totals"] == {"modules": 0, "topics": 0, "subTopics": 0, "excluded": 1}


def test_a_unit_that_loses_every_chapter_produces_no_empty_module():
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Empty Unit", chapter("1.1", "Empty Chapter", "Ghost")))
    )
    tree = reading("R1", "Demo", section("1.1 - Empty Chapter"))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["modules"] == []


def test_section_lookup_is_keyed_by_the_exact_section_title():
    """A page that exists in the reading material under a *different* section
    than the blueprint expects must not match -- titles can collide across
    chapters (e.g. two 'Introduction' pages), so cross-section matching would
    silently link the wrong lesson."""
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.2", "Elements", "Introduction")))
    )
    tree = reading("R1", "Demo", section("1.1 - Other Chapter", ("p1", "Introduction")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["totals"]["subTopics"] == 0
    assert result["excluded"] == [{"sectionTitle": "1.2 - Elements", "title": "Introduction"}]


def test_title_matching_is_case_and_punctuation_insensitive():
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.1", "Ops", "Type Conversion (Casting) and type()")))
    )
    tree = reading("R1", "Demo", section("1.1 - Ops", ("p1", "type conversion casting and type")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["totals"]["subTopics"] == 1


def test_module_topic_and_subtopic_each_get_an_assigned_id():
    skeleton = coursebuilder.blueprint_skeleton(
        blueprint(unit(1, "Basics", chapter("1.1", "Strings", "Indexing")))
    )
    tree = reading("R1", "Demo", section("1.1 - Strings", ("p1", "Indexing")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    module = result["modules"][0]
    topic = module["topics"][0]
    sub = topic["subTopics"][0]
    assert {module["_id"], topic["_id"], sub["_id"]} == {"id1", "id2", "id3"}


def test_chapters_sharing_a_course_chapter_merge_into_one_in_blueprint_order():
    """Two reading-material chapters, one client-facing chapter, lessons contiguous."""
    skeleton = coursebuilder.blueprint_skeleton(blueprint(unit(
        1, "Basics",
        chapter("1.1", "Algorithms and Flowcharts", "Algorithms", "Flowcharts",
                course_chapter="Introduction to Python"),
        chapter("1.2", "Elements of Python", "Keywords", "Numbers",
                course_chapter="Introduction to Python"),
    )))
    tree = reading(
        "R1", "Demo",
        section("1.1 - Algorithms and Flowcharts", ("p1", "Algorithms"), ("p2", "Flowcharts")),
        section("1.2 - Elements of Python", ("p3", "Keywords"), ("p4", "Numbers")),
    )
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())

    assert result["totals"] == {"modules": 1, "topics": 1, "subTopics": 4, "excluded": 0}
    topic = result["modules"][0]["topics"][0]
    assert topic["title"] == "Introduction to Python"
    assert [s["title"] for s in topic["subTopics"]] == \
        ["Algorithms", "Flowcharts", "Keywords", "Numbers"]


def test_merged_lessons_keep_the_url_of_their_own_reading_section():
    """Merging is presentational -- each link must still point at the section the
    lesson actually lives in, not at the merged chapter's name."""
    skeleton = coursebuilder.blueprint_skeleton(blueprint(unit(
        5, "Files and OOP",
        chapter("5.1", "File Handling", "Reading Text Files", course_chapter="File Handling"),
        chapter("5.2", "Modules and Packages", "Creating Your Own Module",
                course_chapter="File Handling"),
    )))
    tree = reading(
        "R1", "Demo",
        section("5.1 - File Handling", ("p1", "Reading Text Files")),
        section("5.2 - Modules and Packages", ("p2", "Creating Your Own Module")),
    )
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    subs = result["modules"][0]["topics"][0]["subTopics"]
    assert subs[0]["data"].endswith("/p1/5-1-file-handling/reading-text-files")
    assert subs[1]["data"].endswith("/p2/5-2-modules-and-packages/creating-your-own-module")


def test_the_same_course_chapter_name_in_different_units_does_not_merge_across_units():
    skeleton = coursebuilder.blueprint_skeleton(blueprint(
        unit(1, "Basics", chapter("1.1", "Intro", "A", course_chapter="Shared")),
        unit(2, "More", chapter("2.1", "Intro", "B", course_chapter="Shared")),
    ))
    tree = reading("R1", "Demo",
                   section("1.1 - Intro", ("p1", "A")),
                   section("2.1 - Intro", ("p2", "B")))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["totals"]["modules"] == 2
    assert result["totals"]["topics"] == 2


def test_a_merged_chapter_survives_one_half_being_entirely_unwritten():
    skeleton = coursebuilder.blueprint_skeleton(blueprint(unit(
        1, "Basics",
        chapter("1.1", "Written", "Real Lesson", course_chapter="Merged"),
        chapter("1.2", "Unwritten", "Ghost", course_chapter="Merged"),
    )))
    tree = reading("R1", "Demo",
                   section("1.1 - Written", ("p1", "Real Lesson")),
                   section("1.2 - Unwritten"))
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["totals"] == {"modules": 1, "topics": 1, "subTopics": 1, "excluded": 1}
    assert result["modules"][0]["topics"][0]["title"] == "Merged"


def donor_blueprint(*units, extras=None):
    bp = {"slug": "demo", "title": "Demo", "sources": [{"productId": DONOR_ID}], "units": list(units)}
    if extras:
        bp["courseExtras"] = extras
    return bp


DONOR_ID = "prod1"


def donor_tree(*pages):
    return {DONOR_ID: {"title": "Donor Course", "contentSections": [
        {"_id": "s1", "title": "Donor Section",
         "contentPages": [{"_id": pid, "title": t} for pid, t in pages]}]}}


def pin(title, page_id, page_title):
    return {"title": title, "source": {
        "productId": DONOR_ID, "pageId": page_id, "pageTitle": page_title,
        "sectionTitle": "Donor Section"}}


# --------------------------------------------------------------------------- #
# Labs and other hand-attached items
# --------------------------------------------------------------------------- #

def test_declared_labs_are_appended_after_the_chapter_readings():
    bp = donor_blueprint(
        unit(1, "Basics", chapter("1.1", "Operators", course_chapter="Operators and Expressions")),
        extras={"1|Operators and Expressions": [
            {"title": "Lab - Operators", "topicType": "challenge", "data": "44x58dat2"}]},
    )
    bp["units"][0]["chapters"][0]["topics"] = [pin("Arithmetic Operators", "p1", "Arithmetic")]
    result = coursebuilder.build_course_from_donors(
        bp, donor_tree(("p1", "Arithmetic")), counting_ids())

    subs = result["modules"][0]["topics"][0]["subTopics"]
    assert [s["title"] for s in subs] == ["Arithmetic Operators", "Lab - Operators"]
    lab = subs[-1]
    assert lab["topicType"] == "challenge"
    assert lab["data"] == "44x58dat2"       # a bare test id, not a URL
    assert lab["time"] == 0
    assert result["totals"]["extras"] == 1
    assert result["totals"]["lessons"] == 1


def test_a_lab_declared_for_a_chapter_that_produced_nothing_is_not_emitted():
    bp = donor_blueprint(
        unit(1, "Basics", chapter("1.1", "Ghost", course_chapter="Ghost")),
        extras={"1|Ghost": [{"title": "Lab - Ghost", "topicType": "challenge", "data": "x"}]},
    )
    bp["units"][0]["chapters"][0]["topics"] = [{"title": "Unwritten", "authorNew": True, "note": "n"}]
    result = coursebuilder.build_course_from_donors(bp, donor_tree(), counting_ids())
    assert result["modules"] == []


def test_extras_are_keyed_by_unit_so_repeated_chapter_names_do_not_collide():
    bp = donor_blueprint(
        unit(1, "One", chapter("1.1", "Shared", course_chapter="Shared")),
        unit(2, "Two", chapter("2.1", "Shared", course_chapter="Shared")),
        extras={"2|Shared": [{"title": "Lab - Only Unit 2", "topicType": "challenge", "data": "d"}]},
    )
    bp["units"][0]["chapters"][0]["topics"] = [pin("A", "p1", "A")]
    bp["units"][1]["chapters"][0]["topics"] = [pin("B", "p2", "B")]
    result = coursebuilder.build_course_from_donors(
        bp, donor_tree(("p1", "A"), ("p2", "B")), counting_ids())
    assert [s["title"] for s in result["modules"][0]["topics"][0]["subTopics"]] == ["A"]
    assert [s["title"] for s in result["modules"][1]["topics"][0]["subTopics"]] == \
        ["B", "Lab - Only Unit 2"]


# --------------------------------------------------------------------------- #
# carry_over_manual_items — the regression that lost a set of labs
# --------------------------------------------------------------------------- #

def built(chapter_title, *subs):
    return [{"_id": "m", "title": "Unit 1 - X", "topics": [
        {"_id": "t", "title": chapter_title, "subTopics": list(subs)}]}]


def reading_sub(title, data):
    return {"_id": "r", "title": title, "topicType": "readingMaterial", "data": data}


def lab_sub(title, data):
    return {"_id": "l", "title": title, "topicType": "challenge", "data": data}


def test_a_hand_added_lab_survives_a_rebuild():
    modules = built("Operators", reading_sub("Arithmetic", "u1"))
    existing = built("Operators", reading_sub("Arithmetic", "old-url"),
                     lab_sub("Lab - Operators", "44x58dat2"))
    report = coursebuilder.carry_over_manual_items(modules, existing)

    subs = modules[0]["topics"][0]["subTopics"]
    assert [s["title"] for s in subs] == ["Arithmetic", "Lab - Operators"]
    assert report["carried"][0]["title"] == "Lab - Operators"
    assert report["orphaned"] == []


def test_stale_reading_links_are_not_carried_over():
    """Reading links are rebuilt from the blueprint, so an old one is stale."""
    modules = built("Operators", reading_sub("Arithmetic", "new-url"))
    existing = built("Operators", reading_sub("Arithmetic", "old-url"))
    report = coursebuilder.carry_over_manual_items(modules, existing)
    assert len(modules[0]["topics"][0]["subTopics"]) == 1
    assert modules[0]["topics"][0]["subTopics"][0]["data"] == "new-url"
    assert report["carried"] == []


def test_a_lab_the_blueprint_now_declares_is_not_duplicated():
    modules = built("Operators", reading_sub("Arithmetic", "u1"),
                    lab_sub("Lab - Operators", "44x58dat2"))
    existing = built("Operators", lab_sub("Lab - Operators", "44x58dat2"))
    report = coursebuilder.carry_over_manual_items(modules, existing)
    assert len(modules[0]["topics"][0]["subTopics"]) == 2
    assert report["carried"] == []


def test_an_item_the_blueprint_moved_to_a_merged_chapter_is_not_stranded():
    """Merging 'Tuples' into 'Lists and Tuples' relocates the quiz the blueprint
    owns. Keying ownership on chapter+asset would strand it and block the write."""
    modules = built("Lists and Tuples", reading_sub("Creating a List", "u1"),
                    lab_sub("Quiz - Lists and Tuples", "44x5avd42"))
    existing = built("Tuples", lab_sub("Quiz - Lists and Tuples", "44x5avd42"))
    report = coursebuilder.carry_over_manual_items(modules, existing)
    assert report == {"carried": [], "orphaned": []}
    assert len(modules[0]["topics"][0]["subTopics"]) == 2


def test_an_item_whose_chapter_disappeared_is_reported_not_dropped():
    """A chapter merge or rename must not silently strand hand-added work."""
    modules = built("Operators and Expressions", reading_sub("Arithmetic", "u1"))
    existing = built("Input, Output and Comments", lab_sub("Lab - IO", "zzz"))
    report = coursebuilder.carry_over_manual_items(modules, existing)
    assert report["carried"] == []
    assert report["orphaned"] == [{
        "chapter": "Input, Output and Comments", "title": "Lab - IO",
        "topicType": "challenge", "data": "zzz",
    }]
    assert len(modules[0]["topics"][0]["subTopics"]) == 1


def test_quizzes_and_projects_are_carried_too_not_just_labs():
    modules = built("Strings", reading_sub("Indexing", "u1"))
    existing = built("Strings", lab_sub("Quiz - Strings", "q1"),
                     {"_id": "p", "title": "Project", "topicType": "project", "data": "pr1"})
    report = coursebuilder.carry_over_manual_items(modules, existing)
    assert [s["title"] for s in modules[0]["topics"][0]["subTopics"]] == \
        ["Indexing", "Quiz - Strings", "Project"]
    assert len(report["carried"]) == 2


def test_carrying_over_an_empty_existing_course_is_a_no_op():
    modules = built("Strings", reading_sub("Indexing", "u1"))
    report = coursebuilder.carry_over_manual_items(modules, [])
    assert report == {"carried": [], "orphaned": []}
    assert len(modules[0]["topics"][0]["subTopics"]) == 1


def test_nhce_blueprint_uses_the_purpose_built_new_horizon_labs():
    """NHCE has its own authored labs. Modern Python's generic 10-question labs
    are a different asset and must not stand in for them."""
    extras = coursebuilder.load_blueprint("nhce-python")["courseExtras"]
    labs = {item["data"] for items in extras.values() for item in items
            if item["title"].startswith("Lab - ")}
    assert labs == {"44zuk3n9m", "44zuk525b", "44zwvkyjj"}

    modern_python_generic_labs = {
        "44x58dat2", "44x58ex27", "44x58jppu", "44x58t5rv", "44x58yh69",
        "44x593udj", "44x599cmm", "44x59cq22", "44x59fpfv", "44x59kvjf",
    }
    used = {item["data"] for items in extras.values() for item in items}
    assert not (used & modern_python_generic_labs)


def test_nhce_blueprint_places_the_reused_python_foundations_quizzes():
    extras = coursebuilder.load_blueprint("nhce-python")["courseExtras"]
    quizzes = {
        key: [i["data"] for i in items if i["title"].startswith("Quiz - ")]
        for key, items in extras.items()
    }
    assert {k: v for k, v in quizzes.items() if v} == {
        "1|Introduction to Python": ["44x5af7x9"],
        "1|Operators and Expressions": ["44x5aj9zz"],
        "2|Control Statements": ["44x5amxrf"],
        "2|Loops": ["44x5aqq4y"],
        "2|Functions": ["44x5b2ugw"],
        "3|Strings": ["44x5aswnz"],
        "3|Assertion and Exception Handling": ["44x5bd2kw"],
        "4|Lists and Tuples": ["44x5avd42"],
        "4|Sets and Dictionaries": ["44x5ayqrw"],
        # NHCE merges Modules and Packages into File Handling, so both apply.
        "5|File Handling": ["44x5bb3vg", "44x5c263v"],
        "5|Object-Oriented Programming": ["44x5cknfd"],
    }
    # No NHCE chapter covers debugging, so that quiz stays out.
    assert "44x5bf4zw" not in {i["data"] for items in extras.values() for i in items}


def test_a_quiz_precedes_the_lab_in_any_chapter_that_has_both():
    extras = coursebuilder.load_blueprint("nhce-python")["courseExtras"]
    for key, items in extras.items():
        kinds = [i["title"].split(" - ")[0] for i in items]
        if "Quiz" in kinds and "Lab" in kinds:
            assert kinds.index("Quiz") < kinds.index("Lab"), key


def test_every_nhce_extra_is_well_formed_and_lands_in_a_real_chapter():
    bp = coursebuilder.load_blueprint("nhce-python")
    extras = bp["courseExtras"]
    for key, items in extras.items():
        unit_number, _ = key.split("|", 1)
        assert unit_number.isdigit()
        for item in items:
            assert item["topicType"] == "challenge"
            assert item["title"].startswith(("Lab - ", "Quiz - "))
            assert item["data"]
    built_chapters = {
        f"{u['number']}|{c.get('courseChapter') or c['title']}"
        for u in bp["units"] for c in u["chapters"]
    }
    assert set(extras) <= built_chapters
    # Nothing may be attached twice.
    used = [i["data"] for items in extras.values() for i in items]
    assert len(used) == len(set(used))
    # Every lab must land in a chapter the blueprint actually builds.
    built_chapters = {
        f"{u['number']}|{c.get('courseChapter') or c['title']}"
        for u in bp["units"] for c in u["chapters"]
    }
    assert set(extras) <= built_chapters


def test_nhce_blueprint_merges_to_the_thirteen_agreed_course_chapters():
    """The client-facing shape signed off on: 19 reading chapters, 13 course chapters."""
    bp = coursebuilder.load_blueprint("nhce-python")
    merged = []
    for unit in bp["units"]:
        seen = []
        for ch in unit["chapters"]:
            name = ch["courseChapter"]
            if name not in seen:
                seen.append(name)
        merged.append((unit["number"], seen))

    assert merged == [
        (1, ["Introduction to Python", "Operators and Expressions"]),
        (2, ["Control Statements", "Loops", "Functions"]),
        (3, ["Strings", "Assertion and Exception Handling"]),
        (4, ["Lists and Tuples", "Sets and Dictionaries"]),
        (5, ["File Handling", "Object-Oriented Programming"]),
    ]
    assert sum(len(names) for _, names in merged) == 11
    assert sum(len(u["chapters"]) for u in bp["units"]) == 19


def test_nhce_course_carries_the_reused_faqs():
    bp = coursebuilder.load_blueprint("nhce-python")
    faqs = bp["courseFaqs"]
    assert len(faqs) == 5
    for faq in faqs:
        assert faq["question"].endswith("?")
        assert len(faq["answer"].split()) >= 15


def test_nhce_course_description_is_client_facing_not_the_internal_note():
    bp = coursebuilder.load_blueprint("nhce-python")
    assert bp["description"].startswith("Tactical Course for")
    assert 60 <= len(bp["courseDescription"].split()) <= 95
    assert "Tactical" not in bp["courseDescription"]
    assert "25CSE144" not in bp["courseDescription"]


def test_multi_chapter_multi_unit_structure_matches_positionally_by_title():
    skeleton = coursebuilder.blueprint_skeleton(blueprint(
        unit(1, "Basics", chapter("1.1", "Strings", "Indexing", "Slicing")),
        unit(2, "Control Flow", chapter("2.1", "Loops", "for Loops", "while Loops")),
    ))
    tree = reading(
        "R1", "Demo",
        section("1.1 - Strings", ("p1", "Indexing"), ("p2", "Slicing")),
        section("2.1 - Loops", ("p3", "for Loops"), ("p4", "while Loops")),
    )
    result = coursebuilder.build_course_structure(skeleton, tree, counting_ids())
    assert result["totals"] == {"modules": 2, "topics": 2, "subTopics": 4, "excluded": 0}
    assert [m["title"] for m in result["modules"]] == ["Unit 1 - Basics", "Unit 2 - Control Flow"]

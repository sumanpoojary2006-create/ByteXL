import importlib.util
import sys
import unittest
from pathlib import Path

ANALYTICS_PATH = Path(__file__).parents[1] / "analytics.py"
SPEC = importlib.util.spec_from_file_location("question_bank_analytics", ANALYTICS_PATH)
analytics = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = analytics
SPEC.loader.exec_module(analytics)


def question(**overrides):
    base = {
        "_id": "q1",
        "created": "2026-07-14T09:00:00.000Z",
        "type": "multipleChoice",
        "difficulty": "medium",
        "createdBy": {"_id": "u1", "name": "Priya Sharma"},
        "subjects": ["python"],
        "topics": ["file-handling"],
        "tags": [],
        "companies": [],
        "explanation": "because",
    }
    base.update(overrides)
    return base


class DifficultyTests(unittest.TestCase):
    def test_case_and_spelling_variants_collapse_onto_one_bucket(self):
        for raw in ("Medium", "medium", " MEDIUM ", "Meidum", "Moderate"):
            self.assertEqual(analytics.norm_difficulty(raw), "medium", raw)

    def test_an_unrecognised_value_is_unspecified_rather_than_guessed(self):
        # Silently folding junk into a real bucket would inflate that bucket.
        self.assertEqual(analytics.norm_difficulty("banana"), "unspecified")
        self.assertEqual(analytics.norm_difficulty(None), "unspecified")

    def test_rudimentary_counts_as_easy(self):
        self.assertEqual(analytics.norm_difficulty("rudimentary"), "easy")


class CompanyTests(unittest.TestCase):
    def test_spellings_of_one_employer_merge(self):
        for raw in ("tcs", "TCS", " TCS "):
            self.assertEqual(analytics.norm_company(raw), "TCS")
        self.assertEqual(analytics.norm_company("microscoft"), "Microsoft")
        self.assertEqual(analytics.norm_company("CTS"), "Cognizant")

    def test_placeholders_are_dropped_not_counted_as_a_company(self):
        for raw in ("NA", "N/A", "-", "General", "sample", ""):
            self.assertIsNone(analytics.norm_company(raw), raw)

    def test_an_unknown_company_is_kept_verbatim(self):
        self.assertEqual(analytics.norm_company("Freshworks"), "Freshworks")


class TrackTests(unittest.TestCase):
    def test_subjects_map_onto_their_skill_family(self):
        cases = {
            "c-programming": "Programming Fundamentals",
            "python": "Programming Fundamentals",
            "algorithm-design": "DSA & Problem Solving",
            "dsa": "DSA & Problem Solving",
            "machine-learning": "Data, AI & Analytics",
            "rdbms": "Databases",
            "web-application-security": "Cloud & Security",
            "company-specific": "Company-Specific Prep",
            "tactical": "Tactical Drills",
        }
        for subject, track in cases.items():
            self.assertEqual(analytics.track_for_subject(subject), track, subject)

    def test_separator_style_does_not_change_the_track(self):
        # Subjects are typed by hand, so "Software Testing" and "software-testing"
        # both occur and must land in the same track.
        self.assertEqual(
            analytics.track_for_subject("Software Testing"),
            analytics.track_for_subject("software-testing"),
        )

    def test_missing_subject_is_its_own_bucket_not_other(self):
        # It is a data-quality number, so it must not hide inside a real track.
        self.assertEqual(analytics.track_for_subject("(no subject)"), "Unassigned Subject")

    def test_an_unmatched_subject_falls_back(self):
        self.assertEqual(analytics.track_for_subject("basket-weaving"), analytics.TRACK_FALLBACK)


class FactTableTests(unittest.TestCase):
    def test_creation_and_archive_events_are_encoded_by_iso_week(self):
        table = analytics.build_fact_table(
            [], [question(_archived_at="2026-08-09T18:00:00Z")], []
        )
        weeks = table["dims"]["weeks"]
        self.assertEqual(weeks[table["cols"]["cw"][0]], "2026-07-13")
        self.assertEqual(weeks[table["cols"]["aw"][0]], "2026-08-03")
        self.assertEqual(table["schemaVersion"], analytics.SNAPSHOT_SCHEMA_VERSION)

    def test_live_and_archived_questions_share_one_table(self):
        table = analytics.build_fact_table(
            [question(_id="a")],
            [question(_id="b", _archived_at="2026-08-02T00:00:00Z")],
            [],
        )
        self.assertEqual(table["counts"], {"live": 1, "archived": 1})
        self.assertEqual(table["cols"]["st"], [0, 1])

    def test_an_archived_question_still_counts_in_its_creation_month(self):
        # Archival is a separate event; production in July must not vanish
        # because the question was archived in August.
        table = analytics.build_fact_table(
            [], [question(created="2026-07-01T00:00:00Z", _archived_at="2026-08-09T00:00:00Z")], []
        )
        months = table["dims"]["months"]
        self.assertEqual(months[table["cols"]["cm"][0]], "2026-07")
        self.assertEqual(months[table["cols"]["am"][0]], "2026-08")

    def test_a_question_that_was_never_archived_has_no_archive_month(self):
        table = analytics.build_fact_table([question()], [], [])
        self.assertEqual(table["cols"]["am"], [-1])
        self.assertEqual(table["cols"]["aw"], [-1])

    def test_a_question_with_no_creation_date_is_skipped(self):
        # Every month-based metric would otherwise silently gain a phantom row.
        table = analytics.build_fact_table([question(created=None)], [], [])
        self.assertEqual(table["counts"]["live"], 0)

    def test_placeholder_taxonomy_does_not_masquerade_as_a_real_topic(self):
        table = analytics.build_fact_table(
            [question(subjects=["sample-subject"], topics=["sample-topic"])], [], []
        )
        self.assertEqual(table["dims"]["subjects"][table["cols"]["su"][0]], "(no subject)")
        self.assertEqual(table["dims"]["topics"][table["cols"]["tp"][0]], "(no topic)")

    def test_a_second_real_subject_is_used_when_the_first_is_a_placeholder(self):
        table = analytics.build_fact_table(
            [question(subjects=["sample-subject", "python"])], [], []
        )
        self.assertEqual(table["dims"]["subjects"][table["cols"]["su"][0]], "python")

    def test_company_tag_mock_and_subject_all_flag_a_company_question(self):
        by_company = analytics.build_fact_table([question(companies=["tcs"])], [], [])
        by_tag = analytics.build_fact_table([question(tags=["hcl-mocktest-3"])], [], [])
        by_subject = analytics.build_fact_table([question(subjects=["company-specific"])], [], [])
        plain = analytics.build_fact_table([question()], [], [])
        self.assertEqual(by_company["cols"]["mk"], [1])
        self.assertEqual(by_tag["cols"]["mk"], [1])
        self.assertEqual(by_subject["cols"]["mk"], [1])
        self.assertEqual(plain["cols"]["mk"], [0])

    def test_a_placeholder_company_does_not_create_a_company_dimension_entry(self):
        table = analytics.build_fact_table([question(companies=["NA"])], [], [])
        self.assertEqual(table["dims"]["companies"], [])
        self.assertEqual(table["cols"]["co"], [-1])

    def test_an_unknown_question_type_does_not_break_the_encoding(self):
        table = analytics.build_fact_table([question(type="somethingNew")], [], [])
        self.assertEqual(table["cols"]["ty"], [0])

    def test_an_unattributed_question_still_gets_an_author_slot(self):
        table = analytics.build_fact_table([question(createdBy=None)], [], [])
        self.assertEqual(table["dims"]["authors"], ["(unattributed)"])


class SnapshotSourceTests(unittest.TestCase):
    def test_lazy_generators_are_consumed_not_discarded(self):
        # The server streams a 245 MB response, so the fetcher hands back
        # generators. An isinstance(..., list) guard here would silently
        # produce an empty bank.
        def fetch(path):
            if path == "/api/questions":
                return (question(_id="live") for _ in range(3))
            if path == "/api/questions-vault":
                return (question(_id="gone", _archived_at="2026-08-01T00:00:00Z") for _ in range(2))
            return iter([{"title": "Python - Assessment 1", "testIntent": "standardizedAssessment"}])

        snapshot = analytics.load_snapshot(fetch, force=True)
        self.assertEqual(snapshot["counts"], {"live": 3, "archived": 2})
        self.assertEqual(len(snapshot["tests"]["rows"]), 1)

    def test_only_one_bulk_source_is_open_at_a_time(self):
        # Holding all three 245 MB reads open at once would defeat streaming.
        open_paths = []

        def fetch(path):
            def gen():
                open_paths.append(path)
                self.assertEqual(len(open_paths), len(set(open_paths)))
                self.assertEqual(open_paths[-1], path)
                yield question()
                open_paths.remove(path)
            return gen()

        analytics.load_snapshot(fetch, force=True)
        self.assertEqual(open_paths, [])

    def setUp(self):
        # Keep the real cache file out of the way of these forced rebuilds.
        self._real_path = analytics.SNAPSHOT_PATH
        analytics.SNAPSHOT_PATH = Path(__file__).parent / ".test-snapshot.json"

    def tearDown(self):
        analytics.SNAPSHOT_PATH.unlink(missing_ok=True)
        analytics.SNAPSHOT_PATH = self._real_path


class TestSummaryTests(unittest.TestCase):
    def test_intent_or_tag_marks_a_standardized_assessment(self):
        rows = analytics.summarize_tests([
            {"title": "A", "testIntent": "standardizedAssessment"},
            {"title": "B", "tags": ["Standardized Assessments"]},
            {"title": "C", "testIntent": "quiz"},
        ])["rows"]
        self.assertEqual([r["standardized"] for r in rows], [True, True, False])

    def test_the_course_is_read_off_the_test_title(self):
        cases = {
            "Cloud Security (v1) - Assessment 11": "Cloud Security",
            "Introduction to AI - Assessment 3": "Introduction to AI",
            "Standardized Assessment - Java Foundations - Methods": "Java Foundations",
            "Python Assessment - 7": "Python",
        }
        for title, subject in cases.items():
            self.assertEqual(analytics.subject_from_test_title(title), subject, title)

    def test_a_company_named_in_the_title_or_tags_marks_a_mock_test(self):
        rows = analytics.summarize_tests([
            {"title": "TCS NQT Mock Test 4"},
            {"title": "Weekly quiz", "tags": ["ACCENTURE"]},
            {"title": "Unit 3 practice"},
        ])["rows"]
        self.assertEqual([r["mock"] for r in rows], [True, True, False])
        self.assertIn("TCS", rows[0]["companies"])


if __name__ == "__main__":
    unittest.main()

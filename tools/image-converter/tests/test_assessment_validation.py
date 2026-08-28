import asyncio
import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from fastapi import HTTPException
import requests


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("assessment_validation_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class AssessmentValidationTests(unittest.TestCase):
    @patch.object(server.requests, "post")
    @patch.object(server, "auth_headers", return_value={"Authorization": "Bearer test"})
    def test_server_error_uses_local_validation_fallback(self, _auth_headers, post):
        response = Mock(status_code=500)
        error = requests.HTTPError("500 Server Error", response=response)
        response.raise_for_status.side_effect = error
        post.return_value = response
        questions = [{"title": "Question 1"}, {"title": "Question 2"}]

        result = asyncio.run(server.assessment_validate({"questions": questions}))

        self.assertEqual(result["validationMode"], "local-fallback")
        self.assertEqual(result["result"], [{"errors": []}, {"errors": []}])
        self.assertIn("temporarily unavailable", result["warning"])

    @patch.object(server.requests, "post")
    @patch.object(server, "auth_headers", return_value={"Authorization": "Bearer test"})
    def test_auth_error_does_not_bypass_validation(self, _auth_headers, post):
        response = Mock(status_code=401)
        error = requests.HTTPError("401 Client Error", response=response)
        response.raise_for_status.side_effect = error
        post.return_value = response

        with self.assertRaises(HTTPException) as raised:
            asyncio.run(server.assessment_validate({"questions": [{"title": "Question"}]}))

        self.assertEqual(raised.exception.status_code, 502)
        self.assertIn("validation failed", raised.exception.detail)

    @patch.object(server, "bytexl_post", return_value=[{"_id": "question-1"}])
    def test_upload_uses_batch_import_endpoint_for_all_question_types(self, bytexl_post):
        questions = [
            {"title": "Question 1", "type": "multipleChoice"},
            {"title": "Question 2", "type": "coding"},
        ]

        result = asyncio.run(server.assessment_upload({"questions": questions}))

        bytexl_post.assert_called_once_with("/api/questions/batch", questions)
        self.assertEqual(result["result"], [{"_id": "question-1", "uploadAction": "created"}])

    @patch.object(server, "bytexl_get")
    @patch.object(server, "bytexl_post")
    def test_archived_duplicate_is_restored_and_updated_in_place(self, bytexl_post, bytexl_get):
        question = {
            "title": "Question 1",
            "type": "multipleChoice",
            "status": "published",
            "topics": ["new-topic"],
        }
        bytexl_post.side_effect = [
            [{"status": "failed", "message": "Duplicate: question: id: existing-1"}],
            {"status": "success"},
            {"status": "success", "data": {"_id": "existing-1"}},
        ]
        bytexl_get.return_value = {
            "status": "success",
            "data": {
                "_id": "existing-1",
                "title": "Question 1",
                "status": "archived",
                "topics": ["old-topic"],
                "created": "preserved",
            },
        }

        result = asyncio.run(server.assessment_upload({"questions": [question]}))

        bytexl_get.assert_called_once_with("/api/questions/_edit/existing-1")
        self.assertEqual(bytexl_post.call_args_list[1].args, ("/api/questions-vault/restore/existing-1", {}))
        update_path, update_payload = bytexl_post.call_args_list[2].args
        self.assertEqual(update_path, "/api/questions")
        self.assertEqual(update_payload["_id"], "existing-1")
        self.assertEqual(update_payload["topics"], ["new-topic"])
        self.assertEqual(update_payload["created"], "preserved")
        self.assertEqual(result["result"][0]["uploadAction"], "updated")

    @patch.object(server, "bytexl_get")
    @patch.object(server, "bytexl_post")
    def test_duplicate_with_other_validation_error_is_not_updated(self, bytexl_post, bytexl_get):
        failure = {
            "status": "failed",
            "message": "Duplicate: question: id: existing-1, Invalid: subjects: Unknown not found",
        }
        bytexl_post.return_value = [failure]

        result = asyncio.run(server.assessment_upload({"questions": [{"title": "Question 1"}]}))

        bytexl_get.assert_not_called()
        self.assertEqual(result["result"], [failure])

    @patch.object(server, "validate_questions_with_bytexl")
    def test_coding_validation_uses_upstream_batch_validator(self, validate_questions):
        questions = [{"title": "Coding Question", "type": "coding"}]
        validate_questions.return_value = ([{"errors": []}], None)

        result = asyncio.run(server.assessment_validate({"type": "coding", "questions": questions}))

        validate_questions.assert_called_once_with(questions)
        self.assertEqual(result["validationMode"], "bytexl")
        self.assertEqual(result["result"], [{"errors": []}])

    @patch.object(server, "validate_questions_with_bytexl")
    def test_duplicate_validation_error_becomes_update_candidate(self, validate_questions):
        questions = [{"title": "Existing coding question", "type": "coding"}]
        validate_questions.return_value = (
            [
                {
                    "errors": [
                        {
                            "code": "Duplicate",
                            "field": "question",
                            "message": "id: existing-1",
                        }
                    ]
                }
            ],
            None,
        )

        result = asyncio.run(server.assessment_validate({"type": "coding", "questions": questions}))

        self.assertEqual(result["result"][0]["errors"], [])
        self.assertEqual(result["result"][0]["duplicateQuestionId"], "existing-1")
        self.assertEqual(result["result"][0]["uploadAction"], "update")

    @patch.object(server, "validate_questions_with_bytexl")
    def test_non_duplicate_validation_errors_still_block_upload(self, validate_questions):
        questions = [{"title": "Invalid question", "type": "coding"}]
        invalid = {"code": "Invalid", "field": "subjects", "message": "Unknown subject"}
        validate_questions.return_value = ([{"errors": [invalid]}], None)

        result = asyncio.run(server.assessment_validate({"type": "coding", "questions": questions}))

        self.assertEqual(result["result"][0]["errors"], [invalid])

    @patch.object(server, "bytexl_get")
    def test_update_validation_requires_question_id_without_calling_bytexl(self, bytexl_get):
        result = asyncio.run(
            server.assessment_update_validate(
                {"questions": [{"title": "Question 1", "type": "multipleChoice"}]}
            )
        )

        bytexl_get.assert_not_called()
        self.assertEqual(result["created"], 0)
        self.assertIn("questionId is required", result["result"][0]["errors"][0])

    @patch.object(server, "bytexl_get")
    def test_update_validation_resolves_id_and_reports_description_change(self, bytexl_get):
        existing = {
            "_id": "existing-1",
            "title": "Question 1",
            "type": "multipleChoice",
            "description": "Old description",
            "status": "published",
        }
        bytexl_get.return_value = {"status": "success", "data": existing}
        question = {
            "questionId": "existing-1",
            "title": "Question 1",
            "type": "multipleChoice",
            "description": "```python\nprint('new')\n```",
        }

        result = asyncio.run(server.assessment_update_validate({"questions": [question]}))

        bytexl_get.assert_called_once_with("/api/questions/_edit/existing-1")
        row = result["result"][0]
        self.assertEqual(row["uploadAction"], "update")
        self.assertEqual(row["changedFields"], ["description"])
        self.assertEqual(row["errors"], [])
        self.assertTrue(row["expectedRevision"])
        self.assertEqual(result["created"], 0)

    @patch.object(server, "bytexl_post")
    @patch.object(server, "bytexl_get")
    def test_update_endpoint_preserves_id_and_markdown_without_batch_create(self, bytexl_get, bytexl_post):
        existing = {
            "_id": "existing-1",
            "title": "Question 1",
            "type": "multipleChoice",
            "description": "Old description",
            "status": "published",
            "created": "preserved",
        }
        bytexl_get.return_value = {"status": "success", "data": existing}
        bytexl_post.return_value = {"status": "success", "data": {"_id": "existing-1"}}
        markdown = "Before\n\n```python\nprint('new')\n```\n\nAfter"
        question = {
            "questionId": "existing-1",
            "expectedRevision": server.assessment_question_revision(existing),
            "title": "Question 1",
            "type": "multipleChoice",
            "description": markdown,
        }

        result = asyncio.run(server.assessment_update({"confirm": True, "questions": [question]}))

        bytexl_post.assert_called_once()
        update_path, update_payload = bytexl_post.call_args.args
        self.assertEqual(update_path, "/api/questions")
        self.assertEqual(update_payload["_id"], "existing-1")
        self.assertEqual(update_payload["description"], markdown)
        self.assertEqual(update_payload["created"], "preserved")
        self.assertEqual(result["result"][0]["uploadAction"], "updated")
        self.assertEqual(result["created"], 0)

    @patch.object(server, "bytexl_post")
    @patch.object(server, "bytexl_get")
    def test_update_endpoint_blocks_stale_revision(self, bytexl_get, bytexl_post):
        existing = {
            "_id": "existing-1",
            "title": "Question 1",
            "type": "multipleChoice",
            "description": "Current",
            "status": "published",
        }
        bytexl_get.return_value = {"status": "success", "data": existing}
        question = {
            "questionId": "existing-1",
            "expectedRevision": "stale",
            "title": "Question 1",
            "type": "multipleChoice",
            "description": "New",
        }

        result = asyncio.run(server.assessment_update({"confirm": True, "questions": [question]}))

        bytexl_post.assert_not_called()
        self.assertEqual(result["result"][0]["status"], "conflict")
        self.assertEqual(result["created"], 0)

    def test_update_endpoint_requires_explicit_confirmation(self):
        with self.assertRaises(HTTPException) as raised:
            asyncio.run(server.assessment_update({"questions": [{"questionId": "existing-1"}]}))

        self.assertEqual(raised.exception.status_code, 400)
        self.assertIn("confirm", raised.exception.detail)

    def test_candidates_group_by_course_and_unit_and_sort_by_order(self):
        questions = [
            {"_id": "q1", "title": "AI - MCQ 3.2.2", "tags": "Set 2"},
            {"_id": "q2", "title": "AI - MCQ 3.2.1", "tags": "Set 2"},
            {"_id": "q3", "title": "AI - Coding Question 3.2.3", "tags": ["ai", "Set 2"]},
            {"_id": "q4", "title": "AI - MCQ 1.1.1", "tags": "Set 1"},
            {"_id": "q5", "title": "Not a structured title", "tags": "Set 2"},
        ]

        result = server.set_two_assessment_candidates(questions, [])

        self.assertEqual(result["setTwoQuestionCount"], 4)
        self.assertEqual(result["structuredQuestionCount"], 3)
        self.assertEqual(result["unstructuredQuestionCount"], 1)
        self.assertEqual(len(result["candidates"]), 1)
        candidate = result["candidates"][0]
        self.assertEqual(candidate["course"], "AI")
        self.assertEqual(candidate["unit"], 3)
        self.assertEqual(candidate["title"], "AI - Assessment 3")
        self.assertEqual(candidate["questionIds"], ["q2", "q1", "q3"])
        self.assertTrue(candidate["ready"])
        self.assertIsNone(candidate["existingTest"])
        self.assertEqual(candidate["duration"], 60)

    def test_candidates_flag_duplicate_order_and_existing_test(self):
        questions = [
            {"_id": "q1", "title": "AI - MCQ 2.2.1", "tags": "Set 2"},
            {"_id": "q2", "title": "AI - MCQ 2.2.1", "tags": "Set 2"},
        ]
        tests = [{"_id": "test-9", "title": "AI - Assessment 2"}]

        result = server.set_two_assessment_candidates(questions, tests)

        candidate = result["candidates"][0]
        self.assertFalse(candidate["ready"])
        self.assertIn("Duplicate question numbers: 1", candidate["issues"][0])
        self.assertEqual(candidate["existingTest"]["_id"], "test-9")
        self.assertEqual(result["existingCount"], 1)
        self.assertEqual(result["readyCount"], 0)

    def test_candidates_match_existing_test_with_version_tag(self):
        questions = [{"_id": "q1", "title": "System Design - MCQ 1.2.1", "tags": "Set 2"}]
        tests = [{"_id": "test-1", "title": "System Design (v1) – Assessment 1"}]

        result = server.set_two_assessment_candidates(questions, tests)

        candidate = result["candidates"][0]
        self.assertEqual(candidate["existingTest"]["_id"], "test-1")
        self.assertEqual(result["existingCount"], 1)
        self.assertEqual(result["readyCount"], 0)

    @patch.object(server, "bytexl_get")
    def test_candidates_match_existing_test_by_question_ids_when_titles_differ(self, bytexl_get):
        questions = [{"_id": "q1", "title": "Introduction to Artificial Intelligence - MCQ 6.2.1", "tags": "Set 2"}]
        tests = [
            {
                "_id": "test-77",
                "title": "Introduction to AI - Assessment 6",
                "testIntent": "standardizedAssessment",
                "questionsCount": 1,
            }
        ]
        bytexl_get.return_value = {"data": {"questions": [{"_id": "q1"}]}}

        result = server.set_two_assessment_candidates(questions, tests)

        candidate = result["candidates"][0]
        self.assertEqual(candidate["existingTest"]["_id"], "test-77")
        bytexl_get.assert_called_once_with("/api/tests/test-77")

    @patch.object(server, "bytexl_get")
    def test_candidates_stay_ready_when_question_ids_do_not_match(self, bytexl_get):
        questions = [{"_id": "q1", "title": "New Course - MCQ 1.2.1", "tags": "Set 2"}]
        tests = [{"_id": "test-1", "title": "Unrelated Test", "testIntent": "standardizedAssessment", "questionsCount": 1}]
        bytexl_get.return_value = {"data": {"questions": [{"_id": "different-question"}]}}

        result = server.set_two_assessment_candidates(questions, tests)

        candidate = result["candidates"][0]
        self.assertIsNone(candidate["existingTest"])
        self.assertTrue(candidate["ready"])

    @patch.object(server, "bytexl_get")
    def test_question_id_fallback_skips_non_standardized_and_mismatched_counts(self, bytexl_get):
        questions = [{"_id": "q1", "title": "New Course - MCQ 1.2.1", "tags": "Set 2"}]
        tests = [
            {"_id": "test-1", "title": "Other", "testIntent": "practice", "questionsCount": 1},
            {"_id": "test-2", "title": "Other2", "testIntent": "standardizedAssessment", "questionsCount": 5},
        ]

        result = server.set_two_assessment_candidates(questions, tests)

        bytexl_get.assert_not_called()
        self.assertIsNone(result["candidates"][0]["existingTest"])

    @patch.object(server, "published_test_items", return_value=[])
    @patch.object(server, "published_question_items")
    def test_candidates_endpoint_returns_discovery(self, published_questions, _published_tests):
        published_questions.return_value = [{"_id": "q1", "title": "AI - MCQ 1.2.1", "tags": "Set 2"}]

        result = asyncio.run(server.test_assessment_candidates())

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["candidateCount"], 1)

    @patch.object(server, "bytexl_post")
    @patch.object(server, "published_test_items", return_value=[])
    @patch.object(server, "published_question_items")
    def test_create_builds_standardized_test_for_selected_group(
        self, published_questions, _published_tests, bytexl_post
    ):
        published_questions.return_value = [
            {"_id": "q1", "title": "AI - MCQ 1.2.2", "tags": "Set 2"},
            {"_id": "q2", "title": "AI - MCQ 1.2.1", "tags": "Set 2"},
        ]
        bytexl_post.return_value = {"_id": "test-1", "title": "AI - Assessment 1"}
        group_key = server.set_two_group_key("AI", 1)

        result = asyncio.run(server.test_assessment_create({"confirm": True, "groupKeys": [group_key]}))

        bytexl_post.assert_called_once()
        path, test_payload = bytexl_post.call_args.args
        self.assertEqual(path, "/api/tests")
        self.assertEqual(test_payload["questions"], ["q2", "q1"])
        self.assertEqual(test_payload["testIntent"], "standardizedAssessment")
        self.assertEqual(test_payload["timeLimit"], 30)
        self.assertEqual(result["createdCount"], 1)
        self.assertEqual(result["failedCount"], 0)
        self.assertIn("/tests/_edit/test-1/ai-assessment-1", result["results"][0]["editUrl"])

    @patch.object(server, "bytexl_post")
    @patch.object(server, "published_test_items", return_value=[])
    @patch.object(server, "published_question_items")
    def test_create_applies_title_and_duration_overrides(
        self, published_questions, _published_tests, bytexl_post
    ):
        published_questions.return_value = [{"_id": "q1", "title": "AI - MCQ 1.2.1", "tags": "Set 2"}]
        bytexl_post.return_value = {"_id": "test-1", "title": "Custom Title"}
        group_key = server.set_two_group_key("AI", 1)

        result = asyncio.run(
            server.test_assessment_create(
                {
                    "confirm": True,
                    "groupKeys": [group_key],
                    "overrides": {group_key: {"title": "  Custom Title  ", "duration": 45}},
                }
            )
        )

        path, test_payload = bytexl_post.call_args.args
        self.assertEqual(test_payload["title"], "Custom Title")
        self.assertEqual(test_payload["timeLimit"], 45)
        self.assertEqual(result["results"][0]["title"], "Custom Title")

    @patch.object(server, "published_test_items", return_value=[])
    @patch.object(server, "published_question_items")
    def test_create_rejects_blank_title_override(self, published_questions, _published_tests):
        published_questions.return_value = [{"_id": "q1", "title": "AI - MCQ 1.2.1", "tags": "Set 2"}]
        group_key = server.set_two_group_key("AI", 1)

        with self.assertRaises(HTTPException) as raised:
            asyncio.run(
                server.test_assessment_create(
                    {"confirm": True, "groupKeys": [group_key], "overrides": {group_key: {"title": "   "}}}
                )
            )

        self.assertEqual(raised.exception.status_code, 400)

    @patch.object(server, "published_test_items", return_value=[])
    @patch.object(server, "published_question_items")
    def test_create_rejects_out_of_range_duration_override(self, published_questions, _published_tests):
        published_questions.return_value = [{"_id": "q1", "title": "AI - MCQ 1.2.1", "tags": "Set 2"}]
        group_key = server.set_two_group_key("AI", 1)

        with self.assertRaises(HTTPException) as raised:
            asyncio.run(
                server.test_assessment_create(
                    {"confirm": True, "groupKeys": [group_key], "overrides": {group_key: {"duration": 5000}}}
                )
            )

        self.assertEqual(raised.exception.status_code, 400)

    @patch.object(server, "published_test_items", return_value=[{"_id": "test-9", "title": "AI - Assessment 1"}])
    @patch.object(server, "published_question_items")
    def test_create_rejects_group_that_already_has_a_test(self, published_questions, _published_tests):
        published_questions.return_value = [{"_id": "q1", "title": "AI - MCQ 1.2.1", "tags": "Set 2"}]
        group_key = server.set_two_group_key("AI", 1)

        with self.assertRaises(HTTPException) as raised:
            asyncio.run(server.test_assessment_create({"confirm": True, "groupKeys": [group_key]}))

        self.assertEqual(raised.exception.status_code, 409)

    def test_create_requires_confirmation(self):
        with self.assertRaises(HTTPException) as raised:
            asyncio.run(server.test_assessment_create({"groupKeys": ["anything"]}))

        self.assertEqual(raised.exception.status_code, 400)
        self.assertIn("confirm", raised.exception.detail)

    def test_create_rejects_empty_group_selection(self):
        with self.assertRaises(HTTPException) as raised:
            asyncio.run(server.test_assessment_create({"confirm": True, "groupKeys": []}))

        self.assertEqual(raised.exception.status_code, 400)


if __name__ == "__main__":
    unittest.main()

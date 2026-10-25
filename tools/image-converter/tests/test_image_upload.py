import asyncio
import importlib.util
import inspect
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch

from fastapi import HTTPException
import requests


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("image_upload_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class ImageUploadTests(unittest.TestCase):
    def test_frontend_wakes_backend_and_retries_editor_requests(self):
        html = SERVER_PATH.with_name("index.html").read_text(encoding="utf-8")

        self.assertIn("const API_WAKE_ATTEMPTS = 5", html)
        self.assertIn('await wakeBackendApi("editor service")', html)
        self.assertIn("attempt <= ONECOMPILER_REQUEST_ATTEMPTS", html)
        self.assertIn("r.status !== 429 && r.status < 500", html)
        self.assertIn("if (apiWakePromise) return apiWakePromise", html)

    def test_onecompiler_workspace_runs_in_fastapi_thread_pool(self):
        self.assertFalse(inspect.iscoroutinefunction(server.create_onecompiler_workspace))

    @patch.object(server.sys, "stdlib_module_names", set(), create=True)
    @patch.object(server, "onecompiler_save", return_value={"_id": "editor123"})
    def test_onecompiler_workspace_returns_reusable_editor_links(self, save):
        result = server.create_onecompiler_workspace(
            {
                "language": "python",
                "title": "Fast editor",
                "filename": "main.py",
                "code": "print('ready')",
                "sourceFile": "unit/topic.md",
                "snippetId": "unit-topic-001",
            }
        )

        self.assertEqual(result["codeId"], "editor123")
        self.assertEqual(result["embedUrl"], "https://onecompiler.com/embed/python/editor123")
        self.assertEqual(save.call_count, 1)

    def test_sorted_creation_days_fill_only_equal_date_ranges(self):
        question_ids = [f"q{i}" for i in range(12)]
        source_days = {
            **{f"q{i}": "2026-10-15" for i in range(4)},
            **{f"q{i}": "2026-10-14" for i in range(4, 9)},
            **{f"q{i}": "2026-10-12" for i in range(9, 12)},
        }

        days = server.resolve_sorted_creation_days(
            question_ids,
            lambda ids: {question_id: source_days[question_id] for question_id in ids},
        )

        self.assertEqual(days, [source_days[question_id] for question_id in question_ids])

    def test_sorted_creation_days_reject_out_of_order_feed(self):
        source_days = {"new": "2026-10-15", "old": "2026-10-12", "wrong": "2026-10-16"}
        with self.assertRaisesRegex(RuntimeError, "not ordered newest first"):
            server.resolve_sorted_creation_days(
                ["new", "old", "wrong"],
                lambda ids: {question_id: source_days[question_id] for question_id in ids},
            )

    def test_content_addressed_names_prevent_same_basename_collision(self):
        first = server.content_addressed_image_name("01_intro.png", b"cloud evolution")
        second = server.content_addressed_image_name("01_intro.png", b"identity workflow")

        self.assertNotEqual(first, second)
        self.assertTrue(first.startswith("01_intro-"))
        self.assertTrue(first.endswith(".png"))

    def test_content_addressed_name_is_stable_for_identical_bytes(self):
        first = server.content_addressed_image_name("01_intro.webp", b"same image")
        second = server.content_addressed_image_name("01_intro.webp", b"same image")

        self.assertEqual(first, second)

    @patch.object(server, "get_upload_token", return_value="test-token")
    @patch.object(server, "upload_to_s3", return_value="https://cdn.example/image.png")
    def test_upload_endpoint_replaces_repeated_basename_before_s3(self, upload_to_s3, _get_token):
        file = server.UploadFile(filename="01_intro.png", file=io.BytesIO(b"cloud evolution"))

        result = asyncio.run(server.upload_image(file, "Introduction to Cloud Computing"))

        uploaded_name, uploaded_bytes, subtype = upload_to_s3.call_args.args
        self.assertRegex(uploaded_name, r"^01_intro-[0-9a-f]{16}\.png$")
        self.assertEqual(uploaded_bytes, b"cloud evolution")
        self.assertEqual(subtype, "introduction-to-cloud-computing")
        self.assertEqual(result, {"status": "success", "url": "https://cdn.example/image.png"})

    def test_legacy_bytexl_host_is_normalized_without_losing_path(self):
        self.assertEqual(
            server.canonical_bytexl_url("https://bytexl.app/api/upload/s3"),
            "https://app.bytexl.ai/api/upload/s3",
        )
        self.assertEqual(
            server.canonical_bytexl_url("https://app.bytexl.ai/api/upload/s3"),
            "https://app.bytexl.ai/api/upload/s3",
        )

    @patch.object(server, "get_upload_token", return_value="test-token")
    @patch.object(server.requests, "post")
    def test_upload_posts_directly_to_current_host(self, post, _get_token):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"status": "success", "url": "https://cdn.example/image.png"}
        post.return_value = response

        url = server.upload_to_s3("image.png", b"png", "unit-1")

        self.assertEqual(url, "https://cdn.example/image.png")
        self.assertEqual(post.call_args.args[0], "https://app.bytexl.ai/api/upload/s3")

    @patch.object(server, "get_upload_token", return_value="test-token")
    @patch.object(server.requests, "post")
    def test_upload_surfaces_upstream_error(self, post, _get_token):
        response = Mock(status_code=500, text="Invalid token")
        response.raise_for_status.side_effect = requests.HTTPError(
            "500 Server Error", response=response
        )
        post.return_value = response

        with self.assertRaises(HTTPException) as raised:
            server.upload_to_s3("image.png", b"png", "unit-1")

        self.assertEqual(raised.exception.status_code, 502)
        self.assertIn("Invalid token", raised.exception.detail)

    @patch.object(server.time, "sleep")
    @patch.object(server.requests, "get")
    @patch.object(server, "get_content_token", return_value="content-token")
    def test_id_request_retries_and_uses_content_token(self, _token, get, sleep):
        failed = Mock()
        failed.raise_for_status.side_effect = requests.RequestException("temporary failure")
        succeeded = Mock()
        succeeded.raise_for_status.return_value = None
        succeeded.json.return_value = {"id": "12abc3def"}
        get.side_effect = [failed, succeeded]

        self.assertEqual(server.get_bytexl_id(), "12abc3def")
        self.assertEqual(get.call_count, 2)
        self.assertEqual(
            get.call_args_list,
            [
                call(
                    f"{server.BYTEXL_API_BASE}/api/getId",
                    headers={"Authorization": "Bearer content-token"},
                    timeout=30,
                ),
                call(
                    f"{server.BYTEXL_API_BASE}/api/getId",
                    headers={"Authorization": "Bearer content-token"},
                    timeout=30,
                ),
            ],
        )
        sleep.assert_called_once_with(0.25)

    @patch.object(server.time, "sleep")
    @patch.object(server.requests, "get")
    @patch.object(server, "get_content_token", return_value="")
    def test_id_request_reports_final_status_after_retries(self, _token, get, sleep):
        response = Mock(status_code=503)
        failed = Mock()
        failed.raise_for_status.side_effect = requests.HTTPError(
            "unavailable", response=response
        )
        get.return_value = failed

        with self.assertRaises(HTTPException) as raised:
            server.get_bytexl_id()

        self.assertEqual(raised.exception.status_code, 502)
        self.assertEqual(
            raised.exception.detail,
            "Could not create a ByteXL id after 3 attempts: ByteXL returned HTTP 503",
        )
        self.assertEqual(get.call_count, 3)

    @patch.object(server.time, "sleep")
    @patch.object(server.requests, "get")
    @patch.object(server, "get_content_token", return_value="content-token")
    def test_bulk_read_retries_a_transient_502_before_streaming(self, _token, get, sleep):
        # ByteXL's edge has returned a bare 502 on /api/questions-vault in
        # production; this must recover rather than aborting the whole build.
        failed = Mock(status_code=502)
        failed.raise_for_status.side_effect = requests.HTTPError(
            "502 Server Error: Bad Gateway", response=Mock(status_code=502)
        )
        succeeded = Mock()
        succeeded.raise_for_status.return_value = None
        succeeded.raw = io.BytesIO(b'[{"_id":"q1"}]')
        get.side_effect = [failed, succeeded]

        items = list(server.bytexl_stream_large("/api/questions-vault"))

        self.assertEqual(items, [{"_id": "q1"}])
        self.assertEqual(get.call_count, 2)
        sleep.assert_called_once_with(2)

    @patch.object(server.time, "sleep")
    @patch.object(server.requests, "get")
    @patch.object(server, "get_content_token", return_value="content-token")
    def test_bulk_read_reports_final_status_after_exhausting_retries(self, _token, get, sleep):
        response = Mock(status_code=502)
        failed = Mock(status_code=502)
        failed.raise_for_status.side_effect = requests.HTTPError("Bad Gateway", response=response)
        get.return_value = failed

        with self.assertRaises(HTTPException) as raised:
            list(server.bytexl_stream_large("/api/questions-vault"))

        self.assertEqual(raised.exception.status_code, 502)
        self.assertIn("after 3 attempts", raised.exception.detail)
        self.assertIn("HTTP 502", raised.exception.detail)
        self.assertEqual(get.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(2), call(4)])

    @patch.object(server.time, "sleep")
    @patch.object(server.requests, "get")
    @patch.object(server, "get_content_token", return_value="content-token")
    def test_question_bulk_read_uses_compact_feed(self, _token, get, sleep):
        summary = Mock()
        summary.raise_for_status.return_value = None
        summary.raw = io.BytesIO(b'[{"_id":"q1"}]')
        get.return_value = summary

        items = list(server.bytexl_stream_large("/api/questions"))

        self.assertEqual(items, [{"_id": "q1", "_analytics_summary_only": True}])
        self.assertIn("summaryScreen=true", get.call_args.args[0])
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()

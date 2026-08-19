import asyncio
import importlib.util
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
        self.assertEqual(sleep.call_args_list, [call(0.25), call(0.5)])


if __name__ == "__main__":
    unittest.main()

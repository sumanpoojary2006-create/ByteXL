import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from fastapi import HTTPException
import requests


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("image_upload_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class ImageUploadTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

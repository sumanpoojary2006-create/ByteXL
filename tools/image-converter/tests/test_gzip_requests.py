import asyncio
import gzip
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from starlette.requests import Request
from starlette.responses import JSONResponse


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("gzip_request_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class GzipRequestTests(unittest.TestCase):
    @staticmethod
    def run_middleware(body, headers):
        messages = []
        request_delivered = False

        async def receive():
            nonlocal request_delivered
            if request_delivered:
                return {"type": "http.request", "body": b"", "more_body": False}
            request_delivered = True
            return {"type": "http.request", "body": body, "more_body": False}

        async def send(message):
            messages.append(message)

        async def downstream(scope, receive_next, send_next):
            payload = await Request(scope, receive_next).json()
            await JSONResponse({"received": payload})(scope, receive_next, send_next)

        scope = {
            "type": "http",
            "asgi": {"version": "3.0"},
            "http_version": "1.1",
            "method": "POST",
            "scheme": "https",
            "path": "/preview-product-upload",
            "raw_path": b"/preview-product-upload",
            "query_string": b"",
            "root_path": "",
            "headers": [(name.lower().encode(), value.encode()) for name, value in headers.items()],
            "client": ("test", 123),
            "server": ("test", 443),
        }
        asyncio.run(server.GZipRequestMiddleware(downstream)(scope, receive, send))
        status = next(message["status"] for message in messages if message["type"] == "http.response.start")
        response_body = b"".join(
            message.get("body", b"") for message in messages if message["type"] == "http.response.body"
        )
        return status, json.loads(response_body)

    def test_gzip_helper_round_trips_json(self):
        raw = json.dumps({"files": [{"path": "Unit 1/01_intro.md", "markdown": "Hello"}]}).encode()

        self.assertEqual(server.decompress_gzip_json_body(gzip.compress(raw)), raw)

    def test_invalid_gzip_request_returns_json_error(self):
        status, response = self.run_middleware(
            b"not gzip",
            {"Content-Type": "application/json", "Content-Encoding": "gzip"},
        )

        self.assertEqual(status, 400)
        self.assertEqual(response, {"detail": "Invalid compressed request body"})

    def test_rejected_gzip_body_still_carries_cors_headers(self):
        """Without CORS wrapping the decoder the browser sees "Failed to fetch"."""
        from fastapi.testclient import TestClient

        origin = "https://image-converter-pi-rouge.vercel.app"
        with TestClient(server.app) as client:
            response = client.post(
                "/preview-product-upload",
                content=b"not gzip",
                headers={
                    "Content-Type": "application/json",
                    "Content-Encoding": "gzip",
                    "Origin": origin,
                },
            )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Invalid compressed request body"})
        self.assertEqual(response.headers.get("access-control-allow-origin"), origin)

    def test_middleware_delivers_gzipped_json_to_the_application(self):
        payload = {
            "readingId": "reading-1",
            "files": [{"path": "Unit 1/01_intro.md", "markdown": "Hello"}],
        }
        status, response = self.run_middleware(
            gzip.compress(json.dumps(payload).encode()),
            {
                "Content-Type": "application/json",
                "Content-Encoding": "gzip",
            },
        )

        self.assertEqual(status, 200)
        self.assertEqual(response, {"received": payload})


if __name__ == "__main__":
    unittest.main()

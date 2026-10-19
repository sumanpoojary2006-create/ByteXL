"""OneCompiler silently drops snippets with IPv4 literals or dotted-host URLs.

The save call still answers 200 with an id (and an error in `stderr`), so the lesson ends up with
an embed that shows "Not Found". These tests pin the rule the converter uses to keep such blocks
static.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import server  # noqa: E402


class RejectedLiteralTests(unittest.TestCase):
    def test_dotted_quad_is_rejected(self):
        self.assertEqual(server.onecompiler_rejected_literals('packet = {"source": "203.0.113.9"}'), ["ip-address"])

    def test_cidr_prefix_is_rejected_too(self):
        self.assertEqual(server.onecompiler_rejected_literals('net = "10.0.0.0/8"'), ["ip-address"])

    def test_url_with_dotted_host_is_rejected(self):
        self.assertEqual(server.onecompiler_rejected_literals('print("https://shop.example.com/cart")'), ["url"])

    def test_both_are_reported(self):
        found = server.onecompiler_rejected_literals('x = "http://a.example.org"\ny = "1.2.3.4"')
        self.assertEqual(sorted(found), ["ip-address", "url"])

    def test_plain_code_is_fine(self):
        for code in ['print("hello")', 'x = "3.12"', 'host = "example.com"', 'url = "https://localhost"',
                     'v = "1.2.3"', 'mac = "aa:bb:cc:dd:ee:ff"']:
            self.assertEqual(server.onecompiler_rejected_literals(code), [], code)

    def test_extra_files_are_checked_with_the_main_file(self):
        self.assertEqual(server.onecompiler_rejected_literals("print(1)", 'ip = "8.8.8.8"'), ["ip-address"])


if __name__ == "__main__":
    unittest.main()

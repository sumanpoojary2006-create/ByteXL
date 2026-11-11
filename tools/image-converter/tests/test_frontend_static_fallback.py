import unittest
from pathlib import Path


INDEX_PATH = Path(__file__).parents[1] / "index.html"


class FrontendStaticFallbackTests(unittest.TestCase):
    def test_sandbox_rejection_keeps_the_block_static_and_continues(self):
        html = INDEX_PATH.read_text(encoding="utf-8")

        self.assertIn("if (!error?.oneCompilerStaticBlock) throw error", html)
        self.assertIn('reason:error.staticReason || "onecompiler-rejected-static"', html)
        self.assertIn("continue;\n      }\n      convertedBlocks++;", html)

    def test_only_explicit_static_block_responses_are_recoverable(self):
        html = INDEX_PATH.read_text(encoding="utf-8")

        self.assertIn('r.status === 400', html)
        self.assertIn("must stay\\s+(?:a\\s+)?static code block", html)
        self.assertIn("error.oneCompilerStaticBlock = true", html)
        self.assertNotIn("r.status >= 400", html)

    def test_missing_package_reason_is_preserved_for_the_report(self):
        html = INDEX_PATH.read_text(encoding="utf-8")

        self.assertIn("function oneCompilerStaticReason(detail)", html)
        self.assertIn("missing-package:${match[1]", html)


if __name__ == "__main__":
    unittest.main()

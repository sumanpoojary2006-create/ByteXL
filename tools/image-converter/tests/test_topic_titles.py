import importlib.util
import asyncio
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("image_converter_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class TopicTitleTests(unittest.TestCase):
    def test_readme_title_preserves_punctuation_symbols_and_long_text(self):
        files = [
            {
                "path": "README.md",
                "markdown": (
                    "| # | File | Topic |\n"
                    "|---|---|---|\n"
                    "| 1 | [lesson](1.4%20-%20Relational%20Algebra/02_selection.md) "
                    "| Selection (σ) and Projection (π) |\n"
                    "| 2 | [lesson](2.1/01_entities.md) | "
                    "Entities, Attributes, and Relationships: Modelling the Real World |\n"
                ),
            },
            {"path": "1.4 - Relational Algebra/02_selection.md", "markdown": "body"},
            {"path": "2.1/01_entities.md", "markdown": "body"},
        ]

        records = server.markdown_records(files)

        records_by_path = {record["path"]: record for record in records}
        self.assertEqual(
            records_by_path["1.4 - Relational Algebra/02_selection.md"]["topicTitle"],
            "Selection (σ) and Projection (π)",
        )
        self.assertEqual(
            records_by_path["2.1/01_entities.md"]["topicTitle"],
            "Entities, Attributes, and Relationships: Modelling the Real World",
        )

    @patch.object(server, "save_content")
    @patch.object(server, "save_content_page")
    @patch.object(server, "fetch_content_page")
    @patch.object(server, "fetch_content")
    def test_existing_topic_title_is_published_on_update(
        self, fetch_content, fetch_page, save_page, save_content
    ):
        fetch_content.return_value = {
            "_id": "reading-1",
            "title": "DBMS",
            "contentSections": [
                {
                    "_id": "section-1",
                    "title": "1.4 - Relational Algebra",
                    "contentPages": [
                        {"_id": "page-1", "title": "Selection", "publishStatus": "published"}
                    ],
                }
            ],
        }
        fetch_page.return_value = {
            "_id": "page-1",
            "title": "Selection",
            "markdown": "old",
            "publishStatus": "published",
        }
        save_page.side_effect = lambda page: dict(page)
        save_content.side_effect = lambda content: dict(content)
        files = [
            {
                "path": "README.md",
                "markdown": (
                    "| # | File | Topic |\n|---|---|---|\n"
                    "| 1 | [lesson](1.4%20-%20Relational%20Algebra/02_selection.md) "
                    "| Selection (σ) and Projection (π) |\n"
                ),
            },
            {"path": "1.4 - Relational Algebra/02_selection.md", "markdown": "new"},
        ]

        result = asyncio.run(
            server.upload_to_product(
                {
                    "confirm": True,
                    "readingId": "reading-1",
                    "files": files,
                    "createMissing": False,
                    "replaceAll": False,
                }
            )
        )

        self.assertEqual(result["updatedTopics"], 1)
        published_page = save_page.call_args.args[0]
        self.assertEqual(published_page["title"], "Selection (σ) and Projection (π)")
        self.assertEqual(published_page["markdown"], "new")


if __name__ == "__main__":
    unittest.main()

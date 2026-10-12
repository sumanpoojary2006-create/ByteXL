import asyncio
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SERVER_PATH = Path(__file__).parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("analytics_endpoint_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = server
SPEC.loader.exec_module(server)


class AnalyticsEndpointTests(unittest.TestCase):
    @patch.object(server, "analytics_refresh_status", return_value=(True, None))
    @patch.object(server, "start_analytics_refresh", return_value=True)
    @patch.object(server.analytics, "read_snapshot", return_value=None)
    def test_cold_start_returns_building_without_waiting_for_upstream(
        self, read_snapshot, start_refresh, refresh_status
    ):
        response = asyncio.run(server.analytics_snapshot())

        self.assertEqual(response.status_code, 202)
        self.assertEqual(json.loads(response.body), {
            "status": "building",
            "refreshing": True,
            "message": "The first question-bank snapshot is being built.",
        })
        start_refresh.assert_called_once_with(force_retry=False)

    @patch.object(server, "analytics_refresh_status", return_value=(True, None))
    @patch.object(server, "start_analytics_refresh", return_value=True)
    @patch.object(server.analytics, "read_snapshot")
    def test_stale_snapshot_is_served_while_one_refresh_runs(
        self, read_snapshot, start_refresh, refresh_status
    ):
        read_snapshot.return_value = {
            "schemaVersion": server.analytics.SNAPSHOT_SCHEMA_VERSION,
            "ageSeconds": server.analytics.SNAPSHOT_TTL_SECONDS + 1,
            "counts": {"live": 10, "archived": 2},
        }

        response = asyncio.run(server.analytics_snapshot())

        self.assertEqual(response["counts"], {"live": 10, "archived": 2})
        self.assertTrue(response["refreshing"])
        start_refresh.assert_called_once_with(force_retry=False)

    @patch.object(server, "analytics_refresh_status", return_value=(False, None))
    @patch.object(server, "start_analytics_refresh")
    @patch.object(server.analytics, "read_snapshot")
    def test_fresh_snapshot_does_not_start_another_refresh(
        self, read_snapshot, start_refresh, refresh_status
    ):
        read_snapshot.return_value = {
            "schemaVersion": server.analytics.SNAPSHOT_SCHEMA_VERSION,
            "ageSeconds": 5,
            "counts": {"live": 10, "archived": 2},
        }

        response = asyncio.run(server.analytics_snapshot())

        self.assertFalse(response["refreshing"])
        start_refresh.assert_not_called()


if __name__ == "__main__":
    unittest.main()

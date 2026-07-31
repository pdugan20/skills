#!/usr/bin/env python3
"""Tests for the analyze-ui-video frame extraction helper."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "analyze-ui-video" / "scripts" / "video_frames.py"


def load_script(test: unittest.TestCase):
    test.assertTrue(SCRIPT.is_file(), f"missing portable helper: {SCRIPT}")
    spec = importlib.util.spec_from_file_location("analyze_ui_video_frames", SCRIPT)
    test.assertIsNotNone(spec)
    test.assertIsNotNone(spec.loader)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AnalyzeUIVideoTests(unittest.TestCase):
    def test_observed_fps_prefers_average_over_nominal_rate(self) -> None:
        module = load_script(self)
        stream = {
            "avg_frame_rate": "274800/4621",
            "r_frame_rate": "120/1",
            "nb_frames": "916",
        }

        fps = module.observed_fps(stream, duration=15.403333)

        self.assertAlmostEqual(fps, 59.467648, places=5)

    def test_observed_fps_falls_back_to_decoded_frame_count(self) -> None:
        module = load_script(self)
        stream = {
            "avg_frame_rate": "0/0",
            "r_frame_rate": "120/1",
            "nb_frames": "300",
        }

        fps = module.observed_fps(stream, duration=10.0)

        self.assertEqual(fps, 30.0)

    def test_overview_rate_caps_the_number_of_frames(self) -> None:
        module = load_script(self)

        fps = module.overview_fps(duration=15.403333, source_fps=59.467648, max_frames=30)
        manifest = module.sample_manifest(start=0.0, duration=15.403333, fps=fps, cols=6)

        self.assertEqual(len(manifest), 30)
        self.assertAlmostEqual(manifest[-1]["timestamp"], 14.889888, places=5)

    def test_manifest_maps_grid_cells_to_absolute_timestamps(self) -> None:
        module = load_script(self)

        manifest = module.sample_manifest(start=2.5, duration=1.0, fps=10.0, cols=4)

        self.assertEqual(len(manifest), 10)
        self.assertEqual(
            manifest[5],
            {"index": 5, "row": 2, "column": 2, "timestamp": 3.0},
        )

    def test_crop_rejects_regions_outside_the_source_frame(self) -> None:
        module = load_script(self)

        with self.assertRaisesRegex(ValueError, "outside the 1206x2622 frame"):
            module.parse_crop("900:800:400:0", width=1206, height=2622)


if __name__ == "__main__":
    unittest.main()

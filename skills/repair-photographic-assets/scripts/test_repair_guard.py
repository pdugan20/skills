import copy
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from repair_guard import InvalidRepair, check_composite, check_invocation, file_hash, preflight


class RepairChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.master = Image.new("RGBA", (12, 10), (100, 110, 120, 255))
        self.master.putpixel((0, 0), (30, 40, 50, 0))
        self.master.save(self.root / "master.png")
        self.mask = Image.new("L", self.master.size, 0)
        self.mask.putpixel((5, 4), 255)
        self.mask.putpixel((6, 4), 30)  # The feather is permitted too.
        self.mask.save(self.root / "mask.png")
        self.master.crop((3, 2, 9, 7)).save(self.root / "target.png")
        self.plan = {
            "schema": 1,
            "master": {**self.record("master.png"), "size": [12, 10]},
            "mask": self.record("mask.png"),
            "target": {**self.record("target.png"), "box": [3, 2, 6, 5]},
            "references": [self.record("master.png")],
            "diagnosis": "Damage exists in the source photograph.",
            "source_comparison": "Earlier source inspected; keep the registered master.",
            "boundary_review": "Inspected mask including feather, inside the local crop.",
            "prompt": "Image 1 is the local edit target. Image 2 is reference only.",
            "candidate_path": "candidate.png",
            "preserve_alpha": True,
        }
        self.path = self.root / "repair.json"
        self.save()

    def record(self, name):
        return {"path": name, "sha256": file_hash(self.root / name)}

    def save(self):
        self.path.write_text(json.dumps(self.plan))

    def rejected(self, text):
        return self.assertRaisesRegex(InvalidRepair, text)

    def test_valid_crop_and_exact_invocation(self):
        receipt = preflight(self.path)
        self.assertEqual(receipt["allowed_pixels"], 2)
        self.assertEqual(receipt["protected_pixels"], 118)
        self.assertFalse(receipt["tool_args"]["transparent_background"])
        check_invocation(self.path, receipt["tool_args"])

    def test_missing_diagnosis_or_review_is_rejected(self):
        for field in ("diagnosis", "source_comparison", "boundary_review"):
            with self.subTest(field=field):
                plan = copy.deepcopy(self.plan)
                plan.pop(field)
                self.path.write_text(json.dumps(plan))
                with self.rejected(f"Missing {field}"):
                    preflight(self.path)

    def test_master_file_changed_after_preparation(self):
        changed = self.master.copy()
        changed.putpixel((4, 4), (0, 0, 0, 255))
        changed.save(self.root / "master.png")
        with self.rejected("Input changed"):
            preflight(self.path)

    def test_whole_sprite_target_is_rejected(self):
        self.master.save(self.root / "target.png")
        self.plan["target"] = {**self.record("target.png"), "box": [0, 0, 12, 10]}
        self.save()
        with self.rejected("whole product"):
            preflight(self.path)

    def test_changed_crop_rejected_even_with_updated_file_hash(self):
        with Image.open(self.root / "target.png") as image:
            crop = image.copy()
        crop.putpixel((1, 1), (255, 0, 0, 255))
        crop.save(self.root / "target.png")
        self.plan["target"]["sha256"] = file_hash(self.root / "target.png")
        self.save()
        with self.rejected("unchanged crop"):
            preflight(self.path)

    def test_empty_and_whole_masks_rejected(self):
        for shade, message in ((0, "no repair pixels"), (255, "protect some pixels")):
            Image.new("L", self.master.size, shade).save(self.root / "mask.png")
            self.plan["mask"] = self.record("mask.png")
            self.save()
            with self.rejected(message):
                preflight(self.path)

    def test_feather_outside_crop_rejected(self):
        self.mask.putpixel((10, 4), 1)
        self.mask.save(self.root / "mask.png")
        self.plan["mask"] = self.record("mask.png")
        self.save()
        with self.rejected("entire permitted mask"):
            preflight(self.path)

    def test_source_destination_and_reused_candidate_rejected(self):
        self.plan["candidate_path"] = "master.png"
        self.save()
        with self.rejected("replace a source"):
            preflight(self.path)
        self.plan["candidate_path"] = "candidate.png"
        self.master.save(self.root / "candidate.png")
        self.save()
        with self.rejected("already exists"):
            preflight(self.path)

    def test_tool_changes_rejected(self):
        args = preflight(self.path)["tool_args"]
        for key, value in (("prompt", "Only edit the logo, trust me"),
                           ("referenced_image_paths", [str(self.root / "master.png")]),
                           ("transparent_background", True),
                           ("num_last_images_to_include", 1)):
            with self.subTest(key=key):
                with self.rejected("inputs differ"):
                    check_invocation(self.path, {**args, key: value})

    def test_correct_masked_composite_including_feather_accepted(self):
        result = self.master.copy()
        result.putpixel((5, 4), (200, 200, 200, 255))
        result.putpixel((6, 4), (111, 112, 113, 255))
        result.save(self.root / "candidate.png")
        receipt = check_composite(self.path, self.root / "candidate.png")
        self.assertEqual(receipt["changed_protected_pixels"], 0)
        self.assertEqual(receipt["protected_pixels_checked"], 118)

    def test_unrelated_rgb_and_alpha_changes_rejected(self):
        for color in ((0, 110, 120, 255), (100, 110, 120, 0)):
            result = self.master.copy()
            result.putpixel((9, 9), color)
            result.save(self.root / "composite.png")
            with self.rejected("1 protected RGBA pixels"):
                check_composite(self.path, self.root / "composite.png")

    def test_hidden_transparent_rgb_is_protected(self):
        result = self.master.copy()
        result.putpixel((0, 0), (31, 40, 50, 0))
        result.save(self.root / "composite.png")
        with self.rejected("protected RGBA pixels"):
            check_composite(self.path, self.root / "composite.png")

    def test_alpha_in_allowed_region_requires_declared_permission(self):
        result = self.master.copy()
        result.putpixel((5, 4), (100, 110, 120, 0))
        result.save(self.root / "composite.png")
        with self.rejected("preserve_alpha"):
            check_composite(self.path, self.root / "composite.png")
        self.plan["preserve_alpha"] = False
        self.save()
        check_composite(self.path, self.root / "composite.png")

    def test_master_cannot_be_verified_as_a_separate_composite(self):
        with self.rejected("separate composite"):
            check_composite(self.path, self.root / "master.png")


if __name__ == "__main__":
    unittest.main()

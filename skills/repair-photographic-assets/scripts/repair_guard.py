#!/usr/bin/env python3
"""Read-only checks for bounded photographic repairs. Requires Pillow.

This validates files and pixels, not authorization, taste, or visual review.
It never generates, composites, or replaces an image.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = 16_777_216


class InvalidRepair(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidRepair(message)


def file_hash(path):
    require(path.is_file(), f"Missing file: {path}")
    require(path.stat().st_size <= 64 * 1024 * 1024, "Repair input exceeds 64 MiB")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_file(record, base):
    require(isinstance(record, dict), "Expected a file record")
    path = (base / record["path"]).resolve()
    require(file_hash(path) == record["sha256"], f"Input changed: {path}")
    return path


def png(path, mode=None):
    with Image.open(path) as image:
        require(image.format == "PNG", f"Expected a lossless PNG: {path}")
        require(image.width * image.height <= Image.MAX_IMAGE_PIXELS,
                "Repair input exceeds 16 megapixels")
        require(getattr(image, "n_frames", 1) == 1, "Animated inputs are unsupported")
        if mode:
            require(image.mode == mode, f"Expected {mode} image: {path}")
        return image.copy()


def preflight(plan_path, candidate_may_exist=False):
    plan_path = Path(plan_path).resolve()
    require(plan_path.stat().st_size <= 65536, "Repair record exceeds 64 KiB")
    plan = json.loads(plan_path.read_text())
    require(plan.get("schema") == 1, "Unsupported repair record schema")
    for field in ("diagnosis", "source_comparison", "boundary_review", "prompt"):
        require(isinstance(plan.get(field), str) and plan[field].strip(),
                f"Missing {field}; preparation must precede generation")
    require(isinstance(plan.get("preserve_alpha"), bool), "Declare preserve_alpha")
    base = plan_path.parent
    master_path = checked_file(plan["master"], base)
    mask_path = checked_file(plan["mask"], base)
    target_path = checked_file(plan["target"], base)
    require(len({master_path, mask_path, target_path}) == 3,
            "Master, mask and local target must be separate files")
    master = png(master_path).convert("RGBA")
    require(list(master.size) == plan["master"]["size"], "Master dimensions changed")
    mask = png(mask_path, "L")
    require(mask.size == master.size, "Mask must use master coordinates")
    bbox = mask.getbbox()
    require(bbox is not None, "Mask permits no repair pixels")
    coverage = mask.tobytes()
    require(0 in coverage, "Mask must protect some pixels")
    box = plan["target"]["box"]
    require(isinstance(box, list) and len(box) == 4 and
            all(type(value) is int for value in box), "Crop box must contain four integers")
    x, y, w, h = box
    require(x >= 0 and y >= 0 and w > 0 and h > 0 and
            x + w <= master.width and y + h <= master.height,
            "Crop is outside the master")
    require(w * h < master.width * master.height,
            "Prompt-only repair cannot use the whole product as its edit target")
    require(x <= bbox[0] and y <= bbox[1] and x + w >= bbox[2] and y + h >= bbox[3],
            "Crop does not contain the entire permitted mask, including feather")
    target = png(target_path).convert("RGBA")
    require(target.size == (w, h), "Crop dimensions do not match its registration")
    require(target.tobytes() == master.crop((x, y, x + w, y + h)).tobytes(),
            "Local target is not an unchanged crop of the master")
    references = plan.get("references", [])
    require(isinstance(references, list) and len(references) <= 4,
            "Expected at most four reference files")
    reference_paths = [checked_file(record, base) for record in references]
    for path in reference_paths:
        png(path)
    candidate = (base / plan["candidate_path"]).resolve()
    require(candidate not in {master_path, mask_path, target_path, *reference_paths},
            "Candidate destination would replace a source")
    require(candidate_may_exist or not candidate.exists(), "Candidate destination already exists")
    marker = f"\nRepair preflight: {plan_path}"
    tool_args = {
        "prompt": plan["prompt"] + marker,
        "referenced_image_paths": [str(target_path), *map(str, reference_paths)],
        "transparent_background": target.getchannel("A").getextrema()[0] < 255,
    }
    return {
        "plan_path": str(plan_path), "plan_sha256": file_hash(plan_path),
        "master_path": str(master_path), "master_sha256": file_hash(master_path),
        "mask_path": str(mask_path), "target_path": str(target_path),
        "allowed_pixels": sum(value > 0 for value in coverage),
        "protected_pixels": sum(value == 0 for value in coverage),
        "tool_args": tool_args, "plan": plan,
    }


def check_invocation(plan_path, arguments):
    receipt = preflight(plan_path)
    actual = {key: value for key, value in arguments.items() if value is not None}
    require(actual == receipt["tool_args"],
            "Image tool inputs differ from the validated repair record")
    return receipt


def check_composite(plan_path, composite_path):
    receipt = preflight(plan_path, candidate_may_exist=True)
    composite_path = Path(composite_path).resolve()
    require(composite_path != Path(receipt["master_path"]),
            "Validate a separate composite before replacing the master")
    master = png(Path(receipt["master_path"])).convert("RGBA")
    composite = png(composite_path).convert("RGBA")
    require(master.size == composite.size, "Composite dimensions changed")
    before, after = master.tobytes(), composite.tobytes()
    mask = png(Path(receipt["mask_path"]), "L").tobytes()
    changed_protected = 0
    first = None
    for pixel, permitted in enumerate(mask):
        offset = pixel * 4
        if permitted == 0 and before[offset:offset + 4] != after[offset:offset + 4]:
            changed_protected += 1
            if first is None:
                first = (pixel % master.width, pixel // master.width)
    require(changed_protected == 0,
            f"Composite changed {changed_protected} protected RGBA pixels; first at {first}")
    if receipt["plan"]["preserve_alpha"]:
        require(master.getchannel("A").tobytes() == composite.getchannel("A").tobytes(),
                "Composite changed alpha despite preserve_alpha")
    return {"composite_path": str(composite_path),
            "composite_sha256": file_hash(composite_path),
            "protected_pixels_checked": receipt["protected_pixels"],
            "changed_protected_pixels": 0,
            "visual_acceptance": "not established by this check"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("preflight", "invocation", "composite"))
    parser.add_argument("plan")
    parser.add_argument("input", nargs="?")
    args = parser.parse_args()
    try:
        if args.mode == "preflight":
            result = preflight(args.plan)
            result.pop("plan")
        elif args.mode == "invocation":
            require(args.input is not None, "Provide image-tool arguments JSON")
            result = check_invocation(args.plan, json.loads(Path(args.input).read_text()))
            result.pop("plan")
        else:
            require(args.input is not None, "Provide the lossless composite PNG")
            result = check_composite(args.plan, args.input)
        print(json.dumps(result, indent=2))
    except (InvalidRepair, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Repair rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

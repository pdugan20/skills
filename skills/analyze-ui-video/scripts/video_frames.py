#!/usr/bin/env python3
"""Probe a UI recording or turn a time window into a contact sheet and manifest."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


TILE_BACKGROUND = "0x222222"
DEFAULT_COLUMNS = 6
DEFAULT_MAX_WIDTH = 2400
DEFAULT_OVERVIEW_FRAMES = 30


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_video_tools() -> None:
    missing = [tool for tool in ("ffmpeg", "ffprobe") if shutil.which(tool) is None]
    if missing:
        die(f"missing {', '.join(missing)}; install ffmpeg and try again")


def fraction_value(value: object) -> float | None:
    if not isinstance(value, str) or value in {"", "N/A", "0/0"}:
        return None
    try:
        result = float(Fraction(value))
    except (ValueError, ZeroDivisionError):
        return None
    return result if result > 0 else None


def observed_fps(stream: dict[str, object], duration: float) -> float:
    """Prefer the observed average rate over a container's nominal rate."""
    average = fraction_value(stream.get("avg_frame_rate"))
    if average is not None:
        return average

    frame_count = stream.get("nb_frames")
    if duration > 0 and isinstance(frame_count, str) and frame_count.isdigit():
        decoded_average = int(frame_count) / duration
        if decoded_average > 0:
            return decoded_average

    nominal = fraction_value(stream.get("r_frame_rate"))
    if nominal is not None:
        return nominal
    raise ValueError("video stream does not expose a usable frame rate")


def probe_stream(recording: Path) -> dict[str, object]:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,r_frame_rate,avg_frame_rate,nb_frames:format=duration",
            "-of",
            "json",
            str(recording),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    streams = payload.get("streams", [])
    if not streams:
        raise ValueError("recording has no video stream")
    stream = streams[0]
    duration = float(payload["format"]["duration"])
    average = observed_fps(stream, duration)
    nominal = fraction_value(stream.get("r_frame_rate"))
    frame_count = stream.get("nb_frames")
    return {
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "duration": duration,
        "observed_fps": average,
        "nominal_fps": nominal,
        "frame_count": int(frame_count)
        if isinstance(frame_count, str) and frame_count.isdigit()
        else None,
    }


def parse_crop(spec: str, width: int, height: int) -> tuple[int, int, int, int]:
    try:
        crop_width, crop_height, x, y = (int(part) for part in spec.split(":"))
    except ValueError as error:
        raise ValueError(f"crop must be W:H:X:Y (got {spec!r})") from error
    if crop_width <= 0 or crop_height <= 0 or x < 0 or y < 0:
        raise ValueError("crop dimensions must be positive and coordinates non-negative")
    if x + crop_width > width or y + crop_height > height:
        raise ValueError(f"crop {spec} falls outside the {width}x{height} frame")
    return crop_width, crop_height, x, y


def clamp_window(start: float, duration: float, source_duration: float) -> float:
    if start < 0 or start >= source_duration:
        raise ValueError(f"start must be within the {source_duration:.3f}s recording")
    if duration <= 0:
        raise ValueError("duration must be greater than zero")
    return min(duration, source_duration - start)


def overview_fps(duration: float, source_fps: float, max_frames: int) -> float:
    if duration <= 0 or source_fps <= 0 or max_frames <= 0:
        raise ValueError("duration, source_fps, and max_frames must be positive")
    return min(source_fps, max_frames / duration)


def sample_manifest(
    start: float,
    duration: float,
    fps: float,
    cols: int,
) -> list[dict[str, int | float]]:
    if duration <= 0 or fps <= 0 or cols <= 0:
        raise ValueError("duration, fps, and columns must be positive")
    frame_count = max(1, math.ceil((duration * fps) - 1e-9))
    return [
        {
            "index": index,
            "row": (index // cols) + 1,
            "column": (index % cols) + 1,
            "timestamp": round(start + (index / fps), 6),
        }
        for index in range(frame_count)
    ]


def manifest_path(output: Path) -> Path:
    return output.with_suffix(".json")


def write_manifest(output: Path, payload: dict[str, object]) -> Path:
    path = manifest_path(output)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def run_probe(
    recording: Path,
    output: Path,
    start: float,
    source: dict[str, object],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-ss",
            str(start),
            "-i",
            str(recording),
            "-frames:v",
            "1",
            str(output),
        ],
        check=True,
    )
    sidecar = write_manifest(
        output,
        {
            "mode": "probe",
            "source": source,
            "timestamp": round(start, 6),
            "output": output.name,
        },
    )
    print_source(source)
    print(f"probe t={start:.3f}s -> {output}\nmanifest -> {sidecar}")


def run_sheet(
    recording: Path,
    output: Path,
    crop: tuple[int, int, int, int] | None,
    start: float,
    duration: float,
    fps: float,
    cols: int,
    max_width: int,
    source: dict[str, object],
    mode: str,
) -> None:
    source_width = int(source["width"])
    source_height = int(source["height"])
    crop_width, crop_height, crop_x, crop_y = crop or (
        source_width,
        source_height,
        0,
        0,
    )
    cells = sample_manifest(start=start, duration=duration, fps=fps, cols=cols)
    rows = math.ceil(len(cells) / cols)

    cell_width = min(crop_width, max_width // cols)
    cell_height = max(2, round(crop_height * cell_width / crop_width))
    cell_width = max(2, cell_width - (cell_width % 2))
    cell_height = max(2, cell_height - (cell_height % 2))

    filters = (
        f"crop={crop_width}:{crop_height}:{crop_x}:{crop_y},"
        f"fps={fps:.12g},"
        f"scale={cell_width}:{cell_height},"
        f"tile={cols}x{rows}:margin=2:padding=2:color={TILE_BACKGROUND}"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-ss",
            str(start),
            "-t",
            str(duration),
            "-i",
            str(recording),
            "-vf",
            filters,
            "-frames:v",
            "1",
            str(output),
        ],
        check=True,
    )
    sidecar = write_manifest(
        output,
        {
            "mode": mode,
            "source": source,
            "window": {
                "start": round(start, 6),
                "duration": round(duration, 6),
                "end": round(start + duration, 6),
            },
            "sample_fps": fps,
            "crop": {
                "width": crop_width,
                "height": crop_height,
                "x": crop_x,
                "y": crop_y,
            },
            "grid": {"columns": cols, "rows": rows},
            "cells": cells,
            "output": output.name,
        },
    )
    print_source(source)
    print(
        f"{mode} -> {output}\n"
        f"{len(cells)} cells at {fps:.3f}fps, "
        f"t={start:.3f}s..{start + duration:.3f}s, {cols}x{rows} grid\n"
        f"manifest -> {sidecar}\n"
        "Read cells row-major; use the manifest for absolute timestamps."
    )


def print_source(source: dict[str, object]) -> None:
    nominal = source.get("nominal_fps")
    nominal_text = f", nominal {float(nominal):.3f}fps" if nominal is not None else ""
    print(
        f"{source['width']}x{source['height']}, {source['duration']:.3f}s, "
        f"observed {source['observed_fps']:.3f}fps{nominal_text}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recording", type=Path, help="local screen recording")
    parser.add_argument("-o", "--out", type=Path, default=Path("contact-sheet.png"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--probe", action="store_true", help="write one full-resolution frame")
    mode.add_argument(
        "--overview",
        action="store_true",
        help="sheet the selected window in at most --max-frames cells",
    )
    parser.add_argument("--crop", help="region as W:H:X:Y in source pixels")
    parser.add_argument("--start", type=float, default=0.0, help="start time in seconds")
    parser.add_argument("--duration", type=float, help="window duration in seconds")
    parser.add_argument("--fps", type=float, help="detail sampling rate")
    parser.add_argument("--cols", type=int, default=DEFAULT_COLUMNS)
    parser.add_argument("--max-width", type=int, default=DEFAULT_MAX_WIDTH)
    parser.add_argument("--max-frames", type=int, default=DEFAULT_OVERVIEW_FRAMES)
    args = parser.parse_args()

    require_video_tools()
    if not args.recording.is_file():
        die(f"no such recording: {args.recording}")
    if args.out.suffix.lower() != ".png":
        die("output must use a .png extension")
    if args.cols <= 0 or args.max_width <= 0 or args.max_frames <= 0:
        die("columns, max width, and max frames must be positive")

    try:
        source = probe_stream(args.recording)
        if args.probe:
            if args.start < 0 or args.start >= float(source["duration"]):
                raise ValueError(f"start must be within the {source['duration']:.3f}s recording")
            run_probe(args.recording, args.out, args.start, source)
            return

        requested_duration = args.duration
        if requested_duration is None:
            requested_duration = (
                float(source["duration"]) - args.start if args.overview else 1.0
            )
        duration = clamp_window(args.start, requested_duration, float(source["duration"]))
        if args.fps is not None and args.fps <= 0:
            raise ValueError("fps must be greater than zero")
        fps = (
            overview_fps(duration, float(source["observed_fps"]), args.max_frames)
            if args.overview
            else args.fps or float(source["observed_fps"])
        )
        run_sheet(
            recording=args.recording,
            output=args.out,
            crop=parse_crop(args.crop, int(source["width"]), int(source["height"]))
            if args.crop
            else None,
            start=args.start,
            duration=duration,
            fps=fps,
            cols=args.cols,
            max_width=args.max_width,
            source=source,
            mode="overview" if args.overview else "detail",
        )
    except (ValueError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        die(str(error))


if __name__ == "__main__":
    main()

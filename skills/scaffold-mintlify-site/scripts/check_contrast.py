#!/usr/bin/env python3
"""Calculate the WCAG contrast ratio between two hexadecimal colors."""

from __future__ import annotations

import argparse
import re


HEX_COLOR = re.compile(r"^#?(?P<value>[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def parse_color(value: str) -> tuple[int, int, int]:
    match = HEX_COLOR.fullmatch(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(f"invalid hexadecimal color: {value}")
    digits = match.group("value")
    if len(digits) == 3:
        digits = "".join(character * 2 for character in digits)
    return tuple(int(digits[index : index + 2], 16) for index in (0, 2, 4))


def relative_luminance(color: tuple[int, int, int]) -> float:
    channels = []
    for value in color:
        normalized = value / 255
        channels.append(
            normalized / 12.92
            if normalized <= 0.04045
            else ((normalized + 0.055) / 1.055) ** 2.4
        )
    red, green, blue = channels
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(first: tuple[int, int, int], second: tuple[int, int, int]) -> float:
    lighter, darker = sorted(
        (relative_luminance(first), relative_luminance(second)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("foreground", type=parse_color)
    parser.add_argument("background", type=parse_color)
    args = parser.parse_args()
    ratio = contrast_ratio(args.foreground, args.background)
    normal = "pass" if ratio >= 4.5 else "fail"
    large = "pass" if ratio >= 3 else "fail"
    print(f"{ratio:.2f}:1 (AA normal text: {normal}; AA large text: {large})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

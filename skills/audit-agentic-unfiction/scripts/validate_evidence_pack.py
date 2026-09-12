#!/usr/bin/env python3
"""Validate mechanical integrity of an agentic-unfiction evidence packet.

This checks paths and image containers without reading or printing story content.
Human review must still decide whether a screenshot proves the claimed behavior.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".webp", ".jpg", ".jpeg", ".gif", ".svg"}


def detected_format(path: Path) -> str | None:
    data = path.read_bytes()[:512]
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "gif"
    if len(data) >= 12 and data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "webp"
    stripped = data.lstrip()
    if stripped.startswith(b"<svg") or (stripped.startswith(b"<?xml") and b"<svg" in stripped):
        return "svg"
    return None


def expected_format(path: Path) -> str | None:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return "jpeg"
    if suffix in IMAGE_EXTENSIONS:
        return suffix[1:]
    return None


def inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_local(root: Path, notes: Path, value: str) -> Path | None:
    clean = value.strip().split("#", 1)[0].split("?", 1)[0]
    if not clean or clean.startswith(("http://", "https://")):
        return None
    options = [notes.parent / clean, root / clean]
    for option in options:
        resolved = option.resolve()
        if inside(root, resolved) and resolved.exists():
            return resolved
    return options[0].resolve()


def note_targets(text: str) -> list[str]:
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    code_paths = re.findall(r"`([^`\n]*evidence/[^`\n]+)`", text)
    return links + code_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a versioned visual evidence packet")
    parser.add_argument("--root", required=True, type=Path, help="Candidate or experiment root")
    parser.add_argument("--notes", type=Path, help="Evidence manifest/notes Markdown")
    parser.add_argument(
        "--required-current",
        action="append",
        default=[],
        help="Root-relative current-candidate evidence path; repeat as needed",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    image_count = 0
    referenced_count = 0

    if not root.is_dir():
        print(f"HOLD: evidence root not found: {root}", file=sys.stderr)
        return 2

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        image_count += 1
        expected = expected_format(path)
        actual = detected_format(path)
        rel = path.relative_to(root)
        if actual is None:
            errors.append(f"unrecognized image bytes: {rel}")
        elif actual != expected:
            errors.append(f"image extension/magic mismatch: {rel} says {expected}, bytes are {actual}")

    for value in args.required_current:
        candidate = (root / value).resolve()
        if not inside(root, candidate):
            errors.append(f"required-current path escapes root: {value}")
            continue
        if "pre-revision" in {part.lower() for part in candidate.parts}:
            errors.append(f"required-current path is pre-revision evidence: {value}")
        if not candidate.is_file():
            errors.append(f"required-current evidence missing: {value}")

    if args.notes:
        notes = args.notes.resolve()
        if not notes.is_file():
            errors.append(f"evidence notes not found: {notes}")
        else:
            text = notes.read_text(encoding="utf-8")
            if "_(parent)_" in text:
                errors.append("evidence notes contain _(parent)_ placeholder")
            for value in note_targets(text):
                target = resolve_local(root, notes, value)
                if target is None:
                    continue
                referenced_count += 1
                if not inside(root, target):
                    errors.append(f"evidence-notes path escapes root: {value}")
                elif not target.exists():
                    errors.append(f"evidence-notes path does not resolve: {value}")
                if "pre-revision" in value.lower():
                    line = next((line for line in text.splitlines() if value in line), "")
                    if not re.search(r"pre-revision|regression|obsolete", line, re.IGNORECASE):
                        errors.append(f"pre-revision evidence is not labeled as regression context: {value}")

    if errors:
        print(f"HOLD: {len(errors)} evidence-pack error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("PASS: evidence-pack mechanical validation")
    print(f"images={image_count}")
    print(f"referenced_paths={referenced_count}")
    print(f"required_current={len(args.required_current)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

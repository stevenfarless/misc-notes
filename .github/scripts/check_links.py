#!/usr/bin/env python3
"""Validate repository-local Markdown links, image paths, and heading fragments."""
from __future__ import annotations

import os
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_DIRS = {
    ".git", ".github", "_site", "node_modules", "vendor", "__pycache__"
}
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript", "vbscript"}
MARKDOWN_LINK = re.compile(
    r'!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))'
)
REFERENCE_LINK = re.compile(r'^\s*\[(?!\^)[^\]]+\]:\s*(?:<([^>]+)>|(\S+))', re.MULTILINE)
HTML_ATTRIBUTE = re.compile(
    r'\b(?:href|src)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.IGNORECASE
)
HEADING = re.compile(r'^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$')
EXPLICIT_ID = re.compile(r'\s+\{#([^}]+)\}\s*$')
HTML_ID = re.compile(r'\bid\s*=\s*(?:"([^"]+)"|\'([^\']+)\'|([^\s>]+))', re.IGNORECASE)


def markdown_files() -> list[Path]:
    files = []
    for current, directories, names in os.walk(ROOT):
        directories[:] = sorted(
            name for name in directories
            if name not in EXCLUDED_DIRS and not name.startswith(".")
        )
        for name in names:
            if name.lower().endswith(".md"):
                files.append(Path(current, name))
    return sorted(files)


def heading_slug(text: str) -> str:
    text = re.sub(r'<[^>]*>', "", text)
    text = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[*_~\x60]', "", text)
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(
        char for char in text
        if not unicodedata.combining(char)
        and (char.isalpha() or char.isdigit() or char.isspace() or char in "_-")
    )
    return re.sub(r"\s", "-", text.strip())


def strip_code(source: str) -> str:
    lines = []
    in_fence = False
    fence_char = ""
    fence_size = 0
    for line in source.splitlines():
        marker = re.match(r"^\s{0,3}(\x60{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if not in_fence:
                in_fence, fence_char, fence_size = True, token[0], len(token)
            elif token[0] == fence_char and len(token) >= fence_size:
                in_fence = False
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def anchors_for(path: Path) -> set[str]:
    source = strip_code(path.read_text(encoding="utf-8"))
    anchors: set[str] = set()
    used: set[str] = set()
    for line in source.splitlines():
        match = HEADING.match(line)
        if match:
            raw = match.group(2)
            explicit = EXPLICIT_ID.search(raw)
            base = explicit.group(1) if explicit else heading_slug(raw)
            anchor = base
            suffix = 0
            while anchor in used:
                suffix += 1
                anchor = f"{base}-{suffix}"
            used.add(anchor)
            anchors.add(anchor)
        for attr in HTML_ID.finditer(line):
            anchors.add(next(value for value in attr.groups() if value))
    return anchors


def destinations(source: str):
    source = strip_code(source)
    for match in MARKDOWN_LINK.finditer(source):
        yield next(value for value in match.groups() if value)
    for match in REFERENCE_LINK.finditer(source):
        yield next(value for value in match.groups() if value)
    for match in HTML_ATTRIBUTE.finditer(source):
        yield next(value for value in match.groups() if value)


def resolve_target(source_file: Path, destination: str):
    destination = destination.strip()
    if not destination or destination.startswith("#"):
        return source_file, unquote(destination[1:]) if destination.startswith("#") else ""
    parsed = urlsplit(destination)
    if parsed.scheme.lower() in SKIP_SCHEMES or parsed.netloc:
        return None, ""
    raw_path = unquote(parsed.path)
    if not raw_path:
        target = source_file
    elif raw_path.startswith("/"):
        target = ROOT / raw_path.lstrip("/")
    else:
        target = source_file.parent / raw_path
    target = Path(os.path.normpath(target))
    if target.is_dir():
        for index_name in ("index.md", "README.md", "index.html"):
            candidate = target / index_name
            if candidate.is_file():
                target = candidate
                break
    elif not target.suffix:
        for suffix in (".md", "/index.md"):
            candidate = Path(str(target) + suffix)
            if candidate.is_file():
                target = candidate
                break
    return target, unquote(parsed.fragment)


def main() -> int:
    files = markdown_files()
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}

    for source_file in files:
        source = source_file.read_text(encoding="utf-8")
        for destination in destinations(source):
            target, fragment = resolve_target(source_file, destination)
            if target is None:
                continue
            if not target.is_file():
                errors.append(
                    f"{source_file.relative_to(ROOT)}: missing local target {destination!r}"
                )
                continue
            if fragment and target.suffix.lower() == ".md":
                if target not in anchor_cache:
                    anchor_cache[target] = anchors_for(target)
                if fragment not in anchor_cache[target]:
                    errors.append(
                        f"{source_file.relative_to(ROOT)}: missing fragment "
                        f"#{fragment} in {target.relative_to(ROOT)}"
                    )

    if errors:
        print(f"Found {len(errors)} broken local reference(s):")
        for error in errors[:100]:
            print(f"  - {error}")
        if len(errors) > 100:
            print(f"  ... and {len(errors) - 100} more")
        return 1

    print(f"Validated local links, assets, and heading fragments across {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Prepare a clean GitHub Pages directory from the Markdown notebook."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "_site"
EXCLUDED_DIRS = {".git", ".github", "_site", "node_modules", "vendor"}
EXCLUDED_FILES = {".gitignore"}

def main():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for item in ROOT.iterdir():
        if item.name in EXCLUDED_DIRS or item.name in EXCLUDED_FILES:
            continue
        destination = OUTPUT / item.name
        if item.is_dir():
            shutil.copytree(
                item,
                destination,
                ignore=shutil.ignore_patterns(
                    ".git", ".github", "_site", "node_modules", "vendor", "__pycache__"
                ),
            )
        elif item.is_file():
            shutil.copy2(item, destination)
    if not (OUTPUT / "index.html").is_file():
        raise SystemExit("index.html was not copied into the Pages output.")
    if not (OUTPUT / "articles.json").is_file():
        raise SystemExit("articles.json was not generated before the Pages build.")
    print(f"Prepared GitHub Pages site in {OUTPUT}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate the browser reader's file manifest using only the Python standard library."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_DIRS = {".git", ".github", "_layouts", "_includes", "_site", "vendor", "node_modules"}
EXCLUDED_FILES = {"README.md", "TAGS.md"}


def collect_articles():
    articles = []
    for current, directories, filenames in os.walk(ROOT):
        directories[:] = sorted(
            name for name in directories
            if name not in EXCLUDED_DIRS and not name.startswith(".")
        )
        for filename in filenames:
            if filename.lower().endswith(".md") and filename not in EXCLUDED_FILES:
                path = Path(current, filename)
                relative = path.relative_to(ROOT).as_posix()
                articles.append({"path": relative})
    return sorted(articles, key=lambda item: item["path"].casefold())


def main():
    output = ROOT / "articles.json"
    output.write_text(
        json.dumps({"articles": collect_articles()}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {output.name} with {len(collect_articles())} Markdown files.")


if __name__ == "__main__":
    main()

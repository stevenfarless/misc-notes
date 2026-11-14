#!/usr/bin/env python3
"""Regression tests for the repository-local link validator."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from check_links import anchors_for, destinations, heading_slug, strip_code


class LinkValidatorTests(unittest.TestCase):
    def test_footnote_definitions_are_not_reference_links(self):
        source = """[^1]: National Association of Example Authors.
[book]: references/book.md
[read it](references/other.md)
"""
        self.assertEqual(
            list(destinations(source)),
            ["references/other.md", "references/book.md"],
        )

    def test_reference_definitions_and_inline_links_are_found(self):
        source = """[guide]: <docs/guide.md> "Guide"
![diagram](images/diagram.svg)
"""
        self.assertEqual(
            list(destinations(source)),
            ["images/diagram.svg", "docs/guide.md"],
        )

    def test_code_fences_are_ignored(self):
        source = """[real](real.md)
```markdown
[fake](missing.md)
[^2]: missing.md
```
"""
        self.assertEqual(list(destinations(source)), ["real.md"])

    def test_heading_slug_removes_punctuation_and_normalizes_unicode(self):
        self.assertEqual(heading_slug("Café: A *Test*!"), "cafe-a-test")

    def test_duplicate_heading_anchors_receive_numeric_suffixes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "notes.md"
            path.write_text("## Repeated Heading\n## Repeated Heading\n", encoding="utf-8")
            self.assertEqual(
                anchors_for(path),
                {"repeated-heading", "repeated-heading-1"},
            )

    def test_explicit_html_ids_are_collected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "notes.md"
            path.write_text('<div id="custom-anchor"></div>\n', encoding="utf-8")
            self.assertEqual(anchors_for(path), {"custom-anchor"})


if __name__ == "__main__":
    unittest.main()

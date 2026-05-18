import os
import re
from urllib.parse import quote

REPO_BASE_URL = "https://github.com/stevenfarless/misc-notes/blob/main"
IGNORE = {".git", ".github", "README.md", "TAGS.md"}


def collect_md_files(root="."):
    """Walk the repo and return a list of relative .md file paths."""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip ignored dirs in-place
        dirnames[:] = [d for d in dirnames if d not in IGNORE]
        for fname in filenames:
            if fname.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, fname), root)
                # Normalise to forward slashes
                rel = rel.replace(os.sep, "/")
                if rel not in IGNORE:
                    md_files.append(rel)
    return sorted(md_files)


def extract_tags(filepath):
    """Return the list of tags from a file's YAML front matter, or []."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (IOError, OSError):
        return []

    # Must start with ---
    if not content.startswith("---"):
        return []

    end = content.find("---", 3)
    if end == -1:
        return []

    front_matter = content[3:end]

    # Match: tags: [a, b, c]  or  tags:\n  - a\n  - b
    # Inline array
    inline = re.search(r"^tags:\s*\[([^\]]+)\]", front_matter, re.MULTILINE)
    if inline:
        raw = inline.group(1)
        tags = [t.strip().strip('"\"') for t in raw.split(",") if t.strip()]
        return tags

    # Block list
    block = re.search(r"^tags:\s*\n((?:[ \t]+-[^\n]+\n?)+)", front_matter, re.MULTILINE)
    if block:
        lines = block.group(1).splitlines()
        tags = [re.sub(r"^[ \t]+-\s*", "", l).strip() for l in lines if l.strip()]
        return tags

    return []


def build_tag_index(root="."):
    """Return {tag: [rel_path, ...]} sorted by tag."""
    index = {}
    for rel in collect_md_files(root):
        tags = extract_tags(rel)
        for tag in tags:
            index.setdefault(tag, []).append(rel)
    return dict(sorted(index.items()))


def render_table(index):
    """Render the tag index as a Markdown table."""
    rows = []
    rows.append("| Tag | Files |")
    rows.append("|-----|-------|")
    for tag, files in index.items():
        file_links = []
        for f in sorted(files):
            name = os.path.splitext(os.path.basename(f))[0]
            encoded = quote(f, safe="/")
            url = f"{REPO_BASE_URL}/{encoded}"
            file_links.append(f"[{name}]({url})")
        rows.append(f"| `{tag}` | {', '.join(file_links)} |")
    return "\n".join(rows)


def main():
    index = build_tag_index()
    table = render_table(index)
    count = len(index)

    content = f"""# Tag Index

> Auto-generated on every push to `main`. Do not edit by hand.
> **{count} tags** across all notes.

{table}
"""

    with open("TAGS.md", "w", encoding="utf-8") as f:
        f.write(content)

    print(f"TAGS.md written with {count} tags.")


if __name__ == "__main__":
    main()

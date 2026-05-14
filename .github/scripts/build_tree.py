import os
import re
from urllib.parse import quote

REPO_BASE_URL = "https://github.com/stevenfarless/misc-notes/blob/main"

IGNORE = {".git", ".github", "README.md"}


def build_tree(root=".", depth=0, rel_path=""):
    lines = []
    entries = sorted(
        [e for e in os.listdir(root) if e not in IGNORE],
        key=lambda e: (os.path.isfile(os.path.join(root, e)), e.lower()),
    )
    indent = "  " * depth
    for entry in entries:
        full_path = os.path.join(root, entry)
        entry_rel = f"{rel_path}/{entry}" if rel_path else entry
        encoded_rel = quote(entry_rel, safe="/")
        if os.path.isdir(full_path):
            lines.append(f"{indent}- **{entry}/**")
            lines.extend(build_tree(full_path, depth + 1, entry_rel))
        else:
            url = f"{REPO_BASE_URL}/{encoded_rel}"
            name = os.path.splitext(entry)[0]
            lines.append(f"{indent}  - [{name}]({url})")
    return lines


def main():
    tree_lines = build_tree()
    tree_block = "\n".join(tree_lines)
    new_section = f"<!-- TREE_START -->\n{tree_block}\n<!-- TREE_END -->"

    with open("README.md", "r") as f:
        content = f.read()

    updated = re.sub(
        r"<!-- TREE_START -->.*?<!-- TREE_END -->",
        new_section,
        content,
        flags=re.DOTALL,
    )

    with open("README.md", "w") as f:
        f.write(updated)

    print("README updated.")


if __name__ == "__main__":
    main()

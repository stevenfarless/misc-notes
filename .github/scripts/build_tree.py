import os
import re

REPO_BASE_URL = "https://github.com/stevenfarless/misc-notes/blob/main"
TREE_BASE_URL = "https://github.com/stevenfarless/misc-notes/tree/main"

IGNORE = {".git", ".github", "README.md"}


def build_tree(root=".", prefix="", rel_path=""):
    lines = []
    entries = sorted(
        [e for e in os.listdir(root) if e not in IGNORE],
        key=lambda e: (os.path.isfile(os.path.join(root, e)), e.lower()),
    )
    for i, entry in enumerate(entries):
        full_path = os.path.join(root, entry)
        entry_rel = f"{rel_path}/{entry}" if rel_path else entry
        connector = "└──" if i == len(entries) - 1 else "├──"
        extension = "    " if i == len(entries) - 1 else "│   "
        if os.path.isdir(full_path):
            url = f"{TREE_BASE_URL}/{entry_rel}"
            lines.append(f"{prefix}{connector} [{entry}/]({url})")
            lines.extend(build_tree(full_path, prefix + extension, entry_rel))
        else:
            url = f"{REPO_BASE_URL}/{entry_rel}"
            name = os.path.splitext(entry)[0]
            lines.append(f"{prefix}{connector} [{name}]({url})")
    return lines


def main():
    tree_lines = build_tree()
    tree_block = "\n".join(tree_lines)
    new_section = f"<!-- TREE_START -->\n```\n{tree_block}\n```\n<!-- TREE_END -->"

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

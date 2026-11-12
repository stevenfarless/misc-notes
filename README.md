---
title: Miscellaneous Notes
---

# misc-notes

Research notebook for theological and comparative-religion studies. Debate documents present the strongest cases for competing positions, critiques, rebuttals, and the questions on which disagreements turn.

## Local reader

The repository includes a browser-based Markdown reader. It uses the original `.md` files directly. It does not generate duplicate HTML articles and requires no installation, package manager, local server, or internet connection.

**To use it:**

1. Download the repository and extract the folder.
2. Open `index.html` in a current browser.
3. Select **Choose repository folder** and choose the extracted repository folder.
4. The index scans its subfolders, reads each Markdown file, and builds the catalog automatically.
5. Select a study to read its rendered Markdown. Use **Rescan folder** after adding or editing files.

The folder selection is required by browser security rules. A page opened from disk cannot inspect surrounding folders until the user explicitly selects one. The browser reads the selected files locally.

The folder picker uses the browser's directory-upload support. Current Chrome, Edge, and Firefox desktop releases support this workflow. If folder selection is unavailable in another browser, use one of those browsers.

## GitHub Pages

The same index works when hosted on GitHub Pages. A GitHub Actions workflow scans the repository whenever changes are pushed to `main` and updates `articles.json`. The index reads that manifest and loads the original Markdown files from the site. The manifest contains file paths only, not article content.

New Markdown files are discovered automatically when added anywhere outside excluded repository and build folders. A title and tags in YAML front matter improve the catalog display. Files without front matter receive a title derived from their filename.

## Document structure

Debate files generally use YAML front matter with `title`, `tags`, and `related` fields, followed by a table of contents, definitions, arguments, critiques, rebuttals, and selected bibliography.

Example:

```yaml
---
title: Calvinism vs. Arminianism
tags: [soteriology, grace, election, free-will, predestination]
related:
  - theology/anthropology/monism-vs-dualism.md
---
```

Use canonical tags listed in [TAGS.md](TAGS.md). The tag index and README file tree are generated automatically by GitHub Actions.

---

## File Tree

<!-- TREE_START -->
<!-- TREE_END -->

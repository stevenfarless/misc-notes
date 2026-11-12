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
- **religions/**
    - [islam-vs-christianity](https://github.com/stevenfarless/misc-notes/blob/main/religions/islam-vs-christianity.md)
    - [judaism-vs-christianity-messianic-prophecy](https://github.com/stevenfarless/misc-notes/blob/main/religions/judaism-vs-christianity-messianic-prophecy.md)
- **theology/**
  - **anthropology/**
      - [colorblind-equality-vs-race-conscious-justice](https://github.com/stevenfarless/misc-notes/blob/main/theology/anthropology/colorblind-equality-vs-race-conscious-justice.md)
      - [monism-vs-dualism](https://github.com/stevenfarless/misc-notes/blob/main/theology/anthropology/monism-vs-dualism.md)
  - **bibliology/**
      - [deuterocanon-include-vs-exclude](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/deuterocanon-include-vs-exclude.md)
      - [majority-text-vs-critical-text](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/majority-text-vs-critical-text.md)
      - [plenary-vs-limited-inerrancy](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/plenary-vs-limited-inerrancy.md)
      - [textus-receptus-vs-critical-text](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/textus-receptus-vs-critical-text.md)
  - **christology/**
      - [chalcedonian-christology-vs-kenotic-christology](https://github.com/stevenfarless/misc-notes/blob/main/theology/christology/chalcedonian-christology-vs-kenotic-christology.md)
  - **church-history/**
      - [was-the-reformation-necessary](https://github.com/stevenfarless/misc-notes/blob/main/theology/church-history/was-the-reformation-necessary.md)
  - **ecclesiology/**
      - [egalitarianism-vs-complementarianism](https://github.com/stevenfarless/misc-notes/blob/main/theology/ecclesiology/egalitarianism-vs-complementarianism.md)
  - **eschatology/**
      - [conscious-intermediate-state-vs-soul-sleep](https://github.com/stevenfarless/misc-notes/blob/main/theology/eschatology/conscious-intermediate-state-vs-soul-sleep.md)
      - [eternal-conscious-torment-vs-annihilation](https://github.com/stevenfarless/misc-notes/blob/main/theology/eschatology/eternal-conscious-torment-vs-annihilation.md)
  - **hermeneutics/**
      - [dispensationalism-vs-covenant-theology](https://github.com/stevenfarless/misc-notes/blob/main/theology/hermeneutics/dispensationalism-vs-covenant-theology.md)
      - [lgh-vs-canonical-theological](https://github.com/stevenfarless/misc-notes/blob/main/theology/hermeneutics/lgh-vs-canonical-theological.md)
  - **pneumatology/**
      - [case-for-cessationism](https://github.com/stevenfarless/misc-notes/blob/main/theology/pneumatology/case-for-cessationism.txt)
      - [cessationism-vs-continuationism](https://github.com/stevenfarless/misc-notes/blob/main/theology/pneumatology/cessationism-vs-continuationism.md)
  - **soteriology/**
      - [calvinism-vs-arminianism](https://github.com/stevenfarless/misc-notes/blob/main/theology/soteriology/calvinism-vs-arminianism.md)
  - **theology-proper/**
      - [classical-theism-vs-open-theism](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/classical-theism-vs-open-theism.md)
      - [eternal-functional-subordination-vs-classical-trinitarian-relations](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/eternal-functional-subordination-vs-classical-trinitarian-relations.md)
      - [theism-vs-atheism](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/theism-vs-atheism.md)
- **topic-studies/**
    - [cannibalism_in_the_bible](https://github.com/stevenfarless/misc-notes/blob/main/topic-studies/cannibalism_in_the_bible.md)
  - [.gitignore](https://github.com/stevenfarless/misc-notes/blob/main/.gitignore)
  - [.nojekyll](https://github.com/stevenfarless/misc-notes/blob/main/.nojekyll)
  - [articles](https://github.com/stevenfarless/misc-notes/blob/main/articles.json)
  - [index](https://github.com/stevenfarless/misc-notes/blob/main/index.html)
  - [TAGS](https://github.com/stevenfarless/misc-notes/blob/main/TAGS.md)
<!-- TREE_END -->

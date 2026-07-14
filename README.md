# misc-notes

Research notebook for theological and comparative-religion debate notes. Each file maps a live doctrinal dispute in a bilateral format: strongest case for each position, internal critiques, rebuttals, and a "three actual hinges" section identifying the irreducible points of disagreement.

---

## Document Structure

Every debate file follows the same structure:

1. **YAML front matter**: `title`, `tags`, and `related` fields
2. **Table of Contents**: internal anchor links
3. **Domain & Evidence**: what both sides agree on and what evidence counts
4. **Key Definitions**: each position's definition of disputed terms, plus the opposing critique
5. **Foundational Assumptions**: what each side is taking for granted
6. **Position A: Strongest Case**: syllogistic arguments with critiques and rebuttals
7. **Position B: Strongest Case**: same format
8. **The Three Actual Hinges**: the irreducible points where the debate lives or dies
9. **Selected Bibliography**: primary and secondary sources, collapsed by default

---

## YAML Front Matter

Every file uses three fields:

```yaml
---
title: Calvinism vs Arminianism
tags: [soteriology, grace, election, free-will, predestination]
related:
  - theology/Anthropology/Monism vs Dualism.md
---
```

| Field | Purpose |
|---|---|
| `title` | Matches the filename exactly, no period after "vs", no appended subtitles |
| `tags` | One or more canonical tags from the list below |
| `related` | Repo-relative paths to files where the outcome of one debate directly constrains the other. Do not add loosely thematic links. |

---

## Canonical Tag List

<details>
<summary>Use only these tags. Add new ones here before using them in a file.</summary>

| Tag | Covers |
|---|---|
| `anthropology` | Human nature, body-soul composition, imago Dei |
| `annihilationism` | Final destruction of the wicked; subset of conditional immortality |
| `apologetics` | Cross-tradition or cross-worldview debate |
| `atheism` | Arguments for and against the existence of God |
| `bibliology` | Scripture: inspiration, inerrancy, canon, authority |
| `calvinism` | Reformed soteriology: TULIP, covenant, election |
| `cessationism` | View that sign gifts ceased with the apostolic era |
| `christology` | Doctrine of Christ's person: two natures, incarnation, kenosis |
| `church-history` | Historical theology, ecclesiastical development |
| `complementarianism` | Male-only eldership/headship in church and home |
| `conditional-immortality` | Immortality as a gift of God, not an inherent property of the soul |
| `continuationism` | View that sign gifts continue in the post-apostolic church |
| `covenant-theology` | Hermeneutical framework organizing Scripture around covenants |
| `dispensationalism` | Hermeneutical framework organizing Scripture around distinct dispensations |
| `dualism` | View that humans have a distinct immaterial soul capable of surviving death |
| `ecclesiology` | Doctrine of the church: structure, offices, sacraments |
| `egalitarianism` | Mutual submission in church and home; no gender-based office restriction |
| `election` | Divine selection of individuals or groups for salvation |
| `eschatology` | Last things: death, resurrection, judgment, final state |
| `free-will` | Human capacity for libertarian or compatibilist choice |
| `grace` | Doctrines of divine favor in salvation |
| `hermeneutics` | Principles and methods of biblical interpretation |
| `inerrancy` | Whether Scripture is without error in all or some of its assertions |
| `inspiration` | Mechanism and scope of divine authorship of Scripture |
| `intermediate-state` | Condition of persons between death and resurrection |
| `islam` | Islamic theology, Qur'an, prophetology |
| `monism` | View that humans are a psychosomatic unity without a separable soul |
| `open-theism` | View that God does not have exhaustive foreknowledge of free choices |
| `physicalism` | Subset of monism: mental life constituted by physical processes |
| `pneumatology` | Doctrine of the Holy Spirit |
| `predestination` | Divine determination of the eternal destiny of persons |
| `reformation` | 16th-century Protestant reform movement and its theological claims |
| `religion` | Cross-traditional or world-religion comparison |
| `revelation` | Divine self-disclosure through Scripture, Christ, or general means |
| `soul` | Immaterial constituent of the human person |
| `soteriology` | Doctrine of salvation: grace, faith, atonement, justification |
| `tawhid` | Islamic doctrine of strict divine unity |
| `theology` | General theological method or systematic theology |
| `theology-proper` | Doctrine of God: attributes, Trinity, divine action |
| `theism` | Belief in the existence of a personal God |
| `trinity` | Doctrine of God as one being in three persons |

</details>

---

## File Tree

The tree below is auto-regenerated on every push to `main` by `.github/workflows/update-readme.yml`.

<!-- TREE_START -->
- **religions/**
    - [islam-vs-christianity](https://github.com/stevenfarless/misc-notes/blob/main/religions/islam-vs-christianity.md)
    - [judaism-vs-christianity-messianic-prophecy](https://github.com/stevenfarless/misc-notes/blob/main/religions/judaism-vs-christianity-messianic-prophecy.md)
- **theology/**
  - **anthropology/**
      - [monism-vs-dualism](https://github.com/stevenfarless/misc-notes/blob/main/theology/anthropology/monism-vs-dualism.md)
  - **bibliology/**
      - [deuterocanon-include-vs-exclude](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/deuterocanon-include-vs-exclude.md)
      - [plenary-vs-limited-inerrancy](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/plenary-vs-limited-inerrancy.md)
      - [Textus Receptus vs Critical Text](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/Textus%20Receptus%20vs%20Critical%20Text.md)
      - [textus-receptus-vs-critical-text](https://github.com/stevenfarless/misc-notes/blob/main/theology/bibliology/textus-receptus-vs-critical-text.md)
  - **christology/**
      - [chalcedonian-christology-vs-kenotic-christology](https://github.com/stevenfarless/misc-notes/blob/main/theology/christology/chalcedonian-christology-vs-kenotic-christology.md)
  - **church-history/**
      - [was-the-reformation-necessary](https://github.com/stevenfarless/misc-notes/blob/main/theology/church-history/was-the-reformation-necessary.md)
  - **ecclesiology/**
      - [egalitarianism-vs-complementarianism](https://github.com/stevenfarless/misc-notes/blob/main/theology/ecclesiology/egalitarianism-vs-complementarianism.md)
  - **eschatology/**
      - [eternal-conscious-torment-vs-annihilation](https://github.com/stevenfarless/misc-notes/blob/main/theology/eschatology/eternal-conscious-torment-vs-annihilation.md)
  - **hermeneutics/**
      - [dispensationalism-vs-covenant-theology](https://github.com/stevenfarless/misc-notes/blob/main/theology/hermeneutics/dispensationalism-vs-covenant-theology.md)
      - [lgh-vs-canonical-theological](https://github.com/stevenfarless/misc-notes/blob/main/theology/hermeneutics/lgh-vs-canonical-theological.md)
  - **pneumatology/**
      - [cessationism-vs-continuationism](https://github.com/stevenfarless/misc-notes/blob/main/theology/pneumatology/cessationism-vs-continuationism.md)
  - **soteriology/**
      - [calvinism-vs-arminianism](https://github.com/stevenfarless/misc-notes/blob/main/theology/soteriology/calvinism-vs-arminianism.md)
  - **theology-proper/**
      - [classical-theism-vs-open-theism](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/classical-theism-vs-open-theism.md)
      - [eternal-functional-subordination-vs-classical-trinitarian-relations](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/eternal-functional-subordination-vs-classical-trinitarian-relations.md)
      - [theism-vs-atheism](https://github.com/stevenfarless/misc-notes/blob/main/theology/theology-proper/theism-vs-atheism.md)
  - [TAGS](https://github.com/stevenfarless/misc-notes/blob/main/TAGS.md)
<!-- TREE_END -->

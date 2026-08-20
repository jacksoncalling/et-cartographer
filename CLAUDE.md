# THE CARTOGRAPHER — Project Context

> Load this at the start of every session. Start here, not with the phase history.

---

## What This Is

**The Cartographer** is a droppable, ICM-style folder that turns an AI into a
cartographer for a socio-technical ecosystem. Point it at a real body of work
(documents, a registry, a repo, a vault) and it leaves a **walkable map**: a
catalog, one typed card per object, the live/leftover/ghost status of each, and
the gaps (named-but-unwired ghosts, and unbridged clusters) made visible. The
later reader is often a cold model.

Built for two audiences:
- **The Cartographer contest (Cliff Notes / ICM).** The submission is the folder
  plus a worked example on a real territory.
- **AGIT (Aachen tech transfer).** A reuse: the technology manager's map of the
  Einstein Telescope Euregio campaign, and a wedge for re-contact.

**Worked territory:** the Einstein Telescope campaign to be hosted in the Euregio
Meuse-Rhine (DE / BE / NL).
**Published artifact:** https://claude.ai/code/artifact/a1e73ced-ee6b-4fb0-afd5-4905e4061bce

---

## Current State — Updated 2026-08-20

### What's working
- **Complete cartographer folder.** Method files (`identity`, `rules`,
  `discovery`, `examples`, `README`), `reference/` (`card-types`,
  `gap-heuristics`, `reference-frames`), `tools/` (`gap-scan.py`,
  `build-artifact.py`, `template.html`), and `map/` (41 object notes + `Catalog`
  + `North Star`).
- **Worked ET Euregio map, second pass done.** 41 objects including the engagement
  layer (ET-InnoNet is a real hub) and 7 ghosts. Built from public sources only.
- **Gap engine works and is consistent.** `gap-scan.py` computes betweenness +
  modularity on the object graph (navigation nodes excluded); numbers match
  `build-artifact.py`. The financing-vehicle ghost ranks #2 by betweenness
  (237 vs Interreg 295) — the load-bearing absence.
- **Published walkable artifact** (private): catalog-left, one-card-center,
  network toggle. Fully rebuildable from `map/`.
- **`reference-frames.md` de-biased.** The yardstick is built per run from the
  user's frameworks + two deeply-researched analogues, not a canned list.
  `discovery.md` carries the reference-frame step and the anti-shallow rule.

### Known issues / debt
- **Artifact language is insider** ("ghost", "betweenness 237.3"). Needs a
  plain-language legend for cold readers.
- **Template header is hardcoded ET** (title / subtitle / footer). Reuse needs a
  3-line edit; documented in README ("Reuse on a new territory").
- **Map carries fingerprints of our conversation.** A fresh source-only run is
  warranted, especially re-testing the AI-coordination ghost against real analogues.
- `examples.md` is a pre-second-pass snapshot (fewer objects than live `map/`);
  fine as a teaching sample.

### What's next
1. **Push to GitHub + submit the contest** (repo link + 2–3 sentence blurb +
   artifact link). Initial commit is done; add a remote and push.
2. **German AGIT version**: first-person "how I would approach this as a
   technology manager," plain framing, the map, then where I would dig next and
   who I would contact.
3. **Fresh source-only run** to strip conversational bias, plus a plain-language
   legend layer on the artifact.

---

## Stack

| Layer | Technology |
|-------|-----------|
| The cartographer | A folder of markdown (identity / rules / discovery / reference), read by an AI agent |
| Map output | One markdown note per object under `map/objects/`, `[[wikilinks]]` for movements, simple YAML frontmatter |
| Gap engine | Pure-Python graph theory, no dependencies: Brandes betweenness + greedy-modularity communities |
| Artifact | Self-contained HTML (inline CSS/JS, seeded force layout), generated from `map/` |
| Agent | Claude, acting as the cartographer per the folder's instructions |

---

## Architecture: folder as architecture

The folder IS the agent's operating instructions. Each file does one job.

- `identity.md` — who the cartographer is, the territory it walks, the reader (may be a model).
- `rules.md` — the anti-fabrication law, live/leftover/ghost marking, the two gaps, the research trigger, the refusals.
- `discovery.md` — the run protocol (8 steps: scope, gather, build the reference frame, shelve, wire, hunt gaps, write, iterate).
- `reference/card-types.md` — the closed set of 6 nouns, the canonical movements, the walk order, the naming collisions.
- `reference/gap-heuristics.md` — the by-hand gap scan and the computed tool, and how to read them.
- `reference/reference-frames.md` — how to build the absence yardstick per run (never canned).
- `map/` — the OUTPUT of a run: `Catalog.md` (front door), `North Star.md` (meta), `objects/` (the cards).
- `tools/` — `gap-scan.py` (report), `build-artifact.py` + `template.html` (the HTML).

---

## The object-note schema (map/objects/*.md)

```
---
type: Actor | Capability | Shared Resource | Instrument | Decision | Jurisdiction | Ghost | Tension | Gradient
status: live | leftover | ghost | pending
kind: <optional, e.g. "national research funder">
hub: <optional, e.g. "engagement">
---
# Label

One prose paragraph (the description). Links to neighbours as [[wikilinks]].

Typed movements as prose: Holds [[X]] · funded-by [[Y]] ...

- Hits: what moves if this changes.
- Does not hit: the obvious wrong neighbour.
```

The graph: nodes = object notes; edges = resolved `[[wikilinks]]`. Navigation nodes
(`Catalog`, `North Star`) are **excluded** from the graph, in both tools.

---

## Key File Paths

| What | Where |
|---|---|
| Method (the cartographer) | `identity.md`, `rules.md`, `discovery.md`, `README.md`, `examples.md` |
| Reference | `reference/card-types.md`, `reference/gap-heuristics.md`, `reference/reference-frames.md` |
| Map output | `map/Catalog.md`, `map/North Star.md`, `map/objects/*.md` |
| Gap report | `tools/gap-scan.py` |
| Artifact build | `tools/build-artifact.py` (parser + graph), `tools/template.html` (page) |
| Published page | `et-cartographer.html` (generated; do not hand-edit) |

---

## How to run

```bash
# recompute the gap report from the current map
python tools/gap-scan.py

# rebuild the walkable HTML from the current map
python tools/build-artifact.py
# then republish et-cartographer.html via the Artifact tool (same URL)

# preview locally (JS runs only when served, not as a file:// snapshot)
python -m http.server 8137     # then open http://localhost:8137/et-cartographer.html
```

---

## Patterns & Gotchas

- **Nav nodes are excluded from the graph, not just the report.** The `Catalog`
  links to everything; leaving it in the graph makes it an artificial mega-hub and
  distorts every betweenness score. Both tools drop `type: meta` / `role:
  front-door` nodes before computing.
- **Two ghost flavors.** Named-but-unwired (a label with no real edges) and
  required-but-absent (a link the chain needs that appears nowhere). Both are marked,
  never deleted, and each carries a research question.
- **The reference frame is earned, never canned.** Build it per run from the user's
  named frameworks + two deeply-researched analogues (their model, their successes
  AND failures), matched to the territory's shape and scale. A dimension with no
  source is a bias; drop it.
- **Generate files with Write or Python, never shell heredocs.** This Bash
  environment breaks on apostrophes and `<<'EOF'` delimiters in the command body.
  Authoring markdown/HTML via the Write tool, or emitting files from a Python
  script, avoids the quoting trap entirely.
- **The artifact is data-driven.** Never hand-edit `et-cartographer.html`. Change
  `map/` (or `template.html`), then rerun `build-artifact.py`.
- **Hero copy is dynamic.** The artifact reads the top real hub and the top ghost
  from the data, so re-running discovery keeps the headline true.
- **Reuse needs a different map, not a different cartographer.** Swap `map/`, edit
  three ET-specific lines in `template.html`, rerun the tools.

---

## Phase History (compressed)

| Phase | What happened |
|---|---|
| Design | Chose territory (ET Euregio), merged our + Gemini's grammar, set the 6-noun card model, live/leftover/ghost, hits/does-not-hit. |
| First map | Built `map/` (33 objects) from the public ET-Förder-Navigator corpus + ET-EMR sources. Cited cards, one ghost, one tension, a correction log. |
| Gap engine | Added `gap-scan.py` (betweenness + modularity), `gap-heuristics.md`, `reference-frames.md`. Ghost-with-high-betweenness became the signature finding. |
| Artifact | Built the walkable HTML (catalog + card + network toggle), published private. |
| Second pass | Added the engagement layer + 5 required-but-absent ghosts (41 objects); reshaped the graph; de-biased `reference-frames.md`. |

---

## Workflow Rules (for Claude)

- **Start every session** by reading this file and the Current State section.
- **The map is the output, the folder is the method.** To change the map, run
  discovery and edit `map/`; do not edit the artifact directly.
- **Keep the two tools consistent** (`gap-scan.py` and `build-artifact.py` compute
  the same object graph). If you change one graph-construction rule, change both.
- **Cite source for every card; mark verified vs open; never fill a silence with a
  guess.** The file wins over the card.
- **Do not commit or push without Max asking.** Writing-mechanics: no em-dashes in
  anything client-facing.

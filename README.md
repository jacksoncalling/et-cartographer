# The Cartographer

A droppable folder that turns an AI into a cartographer for a socio-technical
ecosystem. Point it at a real body of work and it leaves a **map a cold reader can
wander without reading the whole thing**: a catalog, typed cards on demand, and the
gaps (ghosts and missing links) made visible.

The later reader is often a model with no memory. That is who this is built for.

## What to feed it

A body of work that is still in force, about an ecosystem someone will act on:

- a corpus of documents, interviews, or notes;
- a registry or database (a funding list, a company map, a project list);
- governance texts, MOUs, tenders.

Point it at the body of work. Do **not** paste the whole thing into the chat. The
cartographer reads the source to build the map; it does not copy the source into
the reader's lap.

## How to use it

1. Drop this folder into a Claude project.
2. Point the AI at the body of work (a path, a set of links, a corpus).
3. The AI becomes the cartographer. It produces a **catalog** (the front door) and
   writes one card per object into an `objects/` folder, each citing its source.
4. You, or the next model, walk it by the one rule below.

`examples.md` shows the whole shape in miniature: a catalog plus a few cards plus
the gaps, for the Einstein Telescope ecosystem. A real run scales that into a
catalog file plus an `objects/` folder of one-card-per-file.

## THE ONE RULE (how a cold model should walk)

> **Load the catalog, then one card, then stop. Never load the whole objects
> folder.**

Ask one question. The catalog points you to one card in two hops. Open that card:
what the thing is, why it's shaped that way, whether it's live / leftover / ghost,
and what it hits and does not hit. Then stop. If you catch yourself loading
everything, you are eating the tree, which is the one thing this folder exists to
prevent.

## What each file does

| File | Job |
|---|---|
| `identity.md` | Who the cartographer is, what it walks, who the later reader is |
| `rules.md` | How it maps: the anti-fabrication law, marking, the two gaps, the research trigger, the refusals |
| `discovery.md` | The run protocol: what to point it at, and the steps from sources to map |
| `reference/card-types.md` | The closed set of 6 nouns, the movements, the walk order, the naming collisions |
| `reference/gap-heuristics.md` | How to find gaps: the by-hand scan and the computed tool |
| `reference/reference-frames.md` | The yardsticks absence is measured against (the blind-spot checklist) |
| `examples.md` | One worked map of a real territory: catalog, cards, a ghost, a tension, a correction log |
| `map/` | Output of a run: `Catalog.md`, `North Star.md`, and `objects/` (one card per object) |
| `tools/gap-scan.py` | The gap scan: ranks nodes by how many paths run through them (a measure called betweenness), groups them into clusters, and flags the ghosts that sit on the most paths, the missing things the structure leans on. A lightweight take on the InfraNodus method. |
| `tools/build-artifact.py` + `tools/template.html` | Render `map/` into the walkable HTML cartography |
| `et-cartographer.html` | The published walkable map, rebuilt by `build-artifact.py` |
| `README.md` | This file |

## Reuse on a new territory

The method is general; only the `map/` and a few labels are ET-specific.

1. Run discovery (`discovery.md`) on the new body of work. Replace `map/objects/`
   with the new cards, and rewrite `map/Catalog.md` and `map/North Star.md`.
2. In `tools/template.html`, edit three ET-specific lines: the `<h1>`, the `.sub`
   subtitle, and the footer sources line.
3. Run `python tools/build-artifact.py`, then `python tools/gap-scan.py`. The
   centrality, clusters and ghost ranking recompute from the new `map/`.

Everything else (identity, rules, reference, the tools' logic) carries over
unchanged. A run against a different territory needs a different map, not a
different cartographer.

## What you get back

- A **catalog** you can enter from cold.
- **Cards** that cite source and end with Hits / Does not hit.
- **Ghosts** marked (named-but-unwired objects), so no reader implements a wish.
- **Structural gaps** named (live clusters with no link between them).
- **Research questions** where the sources are silent, instead of invented answers.

## What it will refuse

- To hand you the whole source (that's a photocopy, not a map).
- To list everything (that's an auditor).
- To explain why something failed (that's a diagnostician).
- To fill a silence with a guess (that's fabrication).

If the output is a story of how things go, a pile of everything wrong, a cause of a
failure, or a nicer-prose copy of the source, it is not a map. Send it back.

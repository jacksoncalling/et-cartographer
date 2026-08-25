# The Cartographer

A droppable folder that turns an AI into a cartographer for a real body of work. Point
it at a repo, a vault, a funding registry, a set of discovery calls, and it leaves a
**map a cold reader can wander without reading the whole thing**: a catalog at the
front, one typed card per object on demand, and the gaps (the ghosts and the missing
links) made visible.

The later reader is often a model with no memory. That is who this is built for, and
saying so is not the lesser answer. It is the real one.

## Three worked territories

One grammar, three kinds of reader. Start with the first.

- **Einstein Telescope, the Euregio map** (41 objects, ecosystem lens). **Start here.**
  A tri-border campaign (DE / BE / NL) to host a gravitational-wave observatory, mapped
  from public sources. The later reader is a cold model joining the coordination work.
  The sharpest finding is a load-bearing absence: the financing vehicle everyone
  references but no one has built.
  [Walk it.](https://claude.ai/code/artifact/a1e73ced-ee6b-4fb0-afd5-4905e4061bce)
- **OpenEvidence** (56 objects, Business Model Canvas lens). A company's own three-sided
  model (doctors use it free, pharma pays to reach them), mapped from public sources.
  The reader is anyone who needs the model and its tensions fast, without reading a
  stack of analyst notes.
  [Walk it.](https://claude.ai/code/artifact/02572122-e3bd-4af6-8605-4f14087a111e)
- **A rope-access firm** (21 objects, consulting-client lens). A 16-person industrial
  firm's operating model, mapped from two discovery conversations. The reader is the
  consultant, or the owner who wants to step back without the business breaking. The
  finding is a judgment bottleneck living in two people's heads.
  [Walk it.](https://claude.ai/code/artifact/5b1e7fa6-84a5-4989-9944-fea7ad2ac16f)

The method was **blind-tested**. Re-run cold on the ET territory from public sources,
under the same folder, it independently reproduced the load-bearing financing-vehicle
ghost. The map is not a lucky read; the method finds it.

## What to feed it

A body of work that is still in force, about something someone will act on or change:

- a corpus of documents, interviews, or notes;
- a registry or database (a funding list, a company map, a project list);
- a repo, a vault, governance texts, MOUs, tenders, discovery calls.

Point it at the body of work. Do **not** paste the whole thing into the chat. The
cartographer reads the source to build the map. It does not copy the source into the
reader's lap.

## How to use it

1. Drop this folder into a Claude project.
2. Point the AI at the body of work (a path, a set of links, a corpus).
3. The AI becomes the cartographer and runs the two passes: Pass 1 (`discovery.md`)
   builds an inventory of the nouns and a reference-frame yardstick; Pass 2
   (`cartography.md`) wires them, confirms the ghosts, hunts the gaps, and writes a
   **catalog** (the front door) plus one card per object into an `objects/` folder,
   each citing its source.
4. You, or the next model, walk it by the one rule below.

`examples.md` shows the whole shape in miniature: a catalog plus a few cards plus the
gaps. A real run scales that into a catalog file plus an `objects/` folder of
one-card-per-file, as in the three territories above.

## THE ONE RULE (how a cold model should walk)

> **Load the catalog, then one card, then stop. Never load the whole objects folder.**

Ask one question. The catalog points you to one card in two hops. Open that card: what
the thing is, why it is shaped that way, whether it is live, pending, leftover, or
ghost, and what it hits and does not hit. Then stop. If you catch yourself loading
everything, you are eating the tree, which is the one thing this folder exists to
prevent.

## What each file does

| File | Job |
|---|---|
| `identity.md` | Who the cartographer is, what it walks, who the later reader is |
| `rules.md` | How it maps: the anti-fabrication law, live / pending / leftover / ghost marking, the two gaps, the research trigger, the refusals |
| `discovery.md` | Pass 1 of the run: the exploratory read; build the inventory of nouns and the reference-frame yardstick; write `Inventory.md` |
| `cartography.md` | Pass 2 of the run: wire the nouns, confirm ghosts, hunt gaps (two methods), write the catalog, cards, and evaluative layer |
| `reference/card-types.md` | The closed set of 6 nouns, the movements, the walk order, the naming collisions |
| `reference/discovery-lenses.md` | The deck of reading models; how to classify a territory and assemble a lens mix |
| `reference/gap-heuristics.md` | How to find gaps: the by-hand scan and the computed tool |
| `reference/reference-frames.md` | The yardstick absence is measured against, earned fresh per run |
| `reference/glossary.md` | The lookup surface: every term in a line or two, pointing to the file that owns it |
| `examples.md` | One worked map in miniature: catalog, a few cards, a ghost, a tension, a correction log |
| `map/`, `map-openevidence/`, `map-stonemasters/` | The three run outputs: `Inventory.md`, `Catalog.md`, `North Star.md`, and `objects/` |
| `tools/gap-scan.py` | The gap scan: ranks nodes by how many paths run through them (betweenness), groups them into clusters, and flags the ghosts that sit on the most paths. A lightweight take on the InfraNodus idea. Takes a map folder as its argument. |
| `tools/build-artifact.py` | Renders one map folder into the walkable HTML. Reads `<map>/build.json` for the template skin, the output name, and the shelf rules. Takes the map folder as its argument. |
| `tools/template*.html` | The visual skins, one per territory |
| `output/` | The generated HTML artifacts (do not hand-edit; rebuild from `map/`) |

## Reuse on a new territory

The method is general. Only the map and its build config are territory-specific.

1. Run the two passes (`discovery.md` then `cartography.md`) on the new body of work.
   Write the cards into a new folder, for example `map-yourterritory/`, with its
   `Catalog.md`, `North Star.md`, and `objects/`.
2. Add a `build.json` to that folder: the template skin, the output filename, and the
   shelf rules. Copy an existing `build.json` and adjust the shelves to your territory.
3. Reuse a template skin, or clone one and swap its header lines.
4. Run `python tools/build-artifact.py map-yourterritory` and
   `python tools/gap-scan.py map-yourterritory`. The reach tiers, clusters, and ghost
   ranking recompute from the new map.

Everything else (identity, rules, discovery, cartography, reference, the tools' logic)
carries over unchanged. A run against a different territory needs a different map, not
a different cartographer and not a different builder.

## What you get back

- A **catalog** you can enter from cold.
- **Cards** that cite their source and end with Hits / Does not hit.
- **Ghosts** marked (named but unwired), so no reader implements a wish.
- **Structural gaps** named (live clusters with no link between them).
- **Research questions** where the sources are silent, instead of invented answers.

## What it will refuse

- To hand you the whole source (that is a photocopy, not a map).
- To list everything (that is an auditor).
- To explain why something failed (that is a diagnostician).
- To fill a silence with a guess (that is fabrication).

If the output is a story of how things go, a pile of everything wrong, a cause of a
failure, or a nicer-prose copy of the source, it is not a map. Send it back.

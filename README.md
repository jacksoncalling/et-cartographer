# The Cartographer

Retrieval-augmented generation reads a pile of text and averages its way to the next
likely word. It has no idea what connects to what. A knowledge graph does. An ontology
makes a body of work **traversable**, so an agent, or a person, can walk from one thing
to the next and see what depends on what. That traversability is the depth a flat
retrieval cannot reach.

The Cartographer builds that graph from a real body of work and leaves it as a
**walkable map**: a catalog at the front, one typed card per object on demand, the
live / pending / leftover / ghost status of each, and the gaps made visible. Not a flat
street map that says A links to B, but a map with relief, one that shows the valley
between A and B, what it costs to cross, and why the ground is shaped that way. That
relief is richer context, for a cold model and for a human both.

It is built in **ICM** (Interpretable Context Methodology), which replaces orchestration
code with structure. The workspace is a library. The catalog is small and stable: it
points at everything and stores almost nothing. One model walks the building, and the
question decides which shelf gets walked to. The Cartographer is the ICM form that maps
a body of work as a graph rather than a list. The catalog is the front door, the cards
are the shelves, and the typed movements between them are the map.

**Watch the walkthrough:** https://youtu.be/OtkM18P1GeE

## The three maps (how this grew)

It began as a question: could an ecosystem come more alive as a map than as a table of
its active members? A list of names tells you who is in the room. A map tells you who
holds what, what moves if you touch one thing, and what everyone references but no one
has actually built.

- **Einstein Telescope, the Euregio map** (41 objects, ecosystem lens). **Start here.**
  A tri-border campaign (DE / BE / NL) to host a gravitational-wave observatory, mapped
  from public sources. The sharpest finding is a load-bearing absence: the financing
  vehicle everyone references and no one has built.
  [Walk it.](https://claude.ai/code/artifact/a1e73ced-ee6b-4fb0-afd5-4905e4061bce)
- **OpenEvidence** (56 objects, Business Model Canvas lens). Once the map worked, we
  pointed it at a complex AI-product ecosystem: doctors use it free, pharma pays to
  reach them. The map holds the three-sided model and the tensions the headline numbers
  hide.
  [Walk it.](https://claude.ai/code/artifact/02572122-e3bd-4af6-8605-4f14087a111e)
- **A rope-access firm** (21 objects, consulting-client lens). Then a different
  question: could we map a customer's world as we engage with them on a consulting gig?
  Built from two discovery conversations, the map surfaced a judgment bottleneck living
  in two people's heads, an insight that came from reading the map, not from sitting in
  the calls.
  [Walk it.](https://claude.ai/code/artifact/5b1e7fa6-84a5-4989-9944-fea7ad2ac16f)

The insights kept arriving from the same place: reading the map, and watching what the
discovery phase surfaced. To give the graph depth, we mapped the **tensions** in each
field, the forces pulling against each other that a list of entities can never show.

The method was blind-tested. Re-run cold on the ET territory from public sources, under
the same folder, it independently reproduced the load-bearing financing-vehicle ghost.
The map is not a lucky read; the method finds it.

## How to use it

1. Drop this folder into a Claude project.
2. Point the AI at a body of work (a path, a set of links, a corpus, a set of calls).
3. The AI becomes the cartographer and runs two passes. Pass 1 (`discovery.md`) builds
   an inventory of the nouns and a reference-frame yardstick. Pass 2 (`cartography.md`)
   wires them, confirms the ghosts, hunts the gaps, and writes a catalog plus one card
   per object, each citing its source.
4. You, or the next model, walk it by the one rule below.

`examples.md` shows the whole shape in miniature. A real run scales that into a catalog
plus an `objects/` folder of one-card-per-file, as in the three maps above.

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
| `discovery.md` | Pass 1: the exploratory read; build the inventory of nouns and the reference-frame yardstick; write `Inventory.md` |
| `cartography.md` | Pass 2: wire the nouns, confirm ghosts, hunt gaps (two methods), write the catalog, cards, and evaluative layer |
| `reference/card-types.md` | The closed set of 6 nouns, the movements, the walk order, the naming collisions |
| `reference/discovery-lenses.md` | The deck of reading models; how to classify a territory and assemble a lens mix |
| `reference/gap-heuristics.md` | How to find gaps: the by-hand scan and the computed tool |
| `reference/reference-frames.md` | The yardstick absence is measured against, earned fresh per run |
| `reference/glossary.md` | The lookup surface: every term in a line or two, pointing to the file that owns it |
| `examples.md` | One worked map in miniature: catalog, a few cards, a ghost, a tension, a correction log |
| `map/`, `map-openevidence/`, `map-stonemasters/` | The three run outputs: `Inventory.md`, `Catalog.md`, `North Star.md`, and `objects/` |
| `tools/gap-scan.py` | The gap scan: ranks nodes by how many paths run through them (betweenness), groups them into clusters, and flags the ghosts that sit on the most paths. A lightweight take on the InfraNodus idea. Takes a map folder as its argument. |
| `tools/build-artifact.py` | Renders one map folder into the walkable HTML. Reads `<map>/build.json` for the template skin, the output name, and the shelf rules. Takes the map folder as its argument. |
| `output/` | The generated HTML artifacts (do not hand-edit; rebuild from the map) |

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
carries over unchanged. A run against a different territory needs a different map, not a
different cartographer and not a different builder.

## What it will refuse

- To hand you the whole source (that is a photocopy, not a map).
- To list everything (that is an auditor).
- To explain why something failed (that is a diagnostician).
- To fill a silence with a guess (that is fabrication).

If the output is a story of how things go, a pile of everything wrong, a cause of a
failure, or a nicer-prose copy of the source, it is not a map. Send it back.

## Built on

- **ICM (Interpretable Context Methodology)**, Van Clief and McDermott. Folder as
  architecture, the catalog-then-card discipline, the walk test.
  [Paper](https://arxiv.org/abs/2603.16021) and [Clief Notes](https://www.skool.com/cliefnotes).
- **Simone Cicero (Boundaryless).** The ecosystem-mapping vocabulary: entities, the VRIO
  liveness test for a capability, the Platform Design Toolkit lens.
- **Bonnitta Roy.** Her thinking on evaluative AI and topology mapping: reading the
  tensions and the contact pressure in a field that a map of entities alone cannot show.
- **Michel Bauwens.** The commons and federation vocabulary for naming governance gaps.
- **InfraNodus** (Dmitry Paranyushkin). The north-star behaviour: surface the structural
  gap, do not tour the text. This is the cheap, source-anchored version of that idea.
- **Terroir.** The evaluative layer (tensions, gradients) and the rule that the structure
  detects while the model only voices, and never invents. (Joshua Baker)
- The growing body of work around **graph engineering**, the larger current this rides.

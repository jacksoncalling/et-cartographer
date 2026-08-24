# Glossary — the cartographer's terms

> A lookup surface, not a re-spec. Each entry is one or two lines and points to the
> file that carries the full treatment. When a term is defined at length elsewhere,
> that file wins.

## Two planes (read this first)

The map has two planes, and most confusion comes from mixing them.

- **The objects.** The six nouns (Actor, Capability, Shared Resource, Instrument,
  Decision, Jurisdiction) and the typed movements between them. This is the wiring.
- **The evaluative field (the relief).** Tensions and gradients. Not nouns, not
  edges. A separate plane that carries what shapes the form and what a move actually
  costs. In Terroir, the source of this grammar, these live in their own arrays
  (`tensions`, `evaluativeSignals`), apart from nodes and relationships. Same split
  here: the field is detected from the structure and voiced by the model, never
  invented. See `identity.md`, "Why the map carries relief."

---

## Terms

**Actor.** One of the six nouns. An entity that can hold a capability, receive funds,
sign an instrument, or make a decision. Full spec: `card-types.md`.

**Body of work (territory).** The real, in-force material the cartographer walks: a
repo, a vault, a registry, a corpus, a set of PDFs. Something someone will change,
not a post-mortem. See `identity.md`.

**Cartographer.** The folder-as-agent: the method that walks a body of work and leaves
a walkable map. Not a diagnostician, a tour guide, an auditor, or a second spec.
`identity.md`.

**Cartography (Pass 2).** The second pass of a run: wire the nouns, confirm the ghosts,
hunt the gaps, write the map. `cartography.md`.

**Card.** One object note under `objects/`. Exactly one noun, cites its source, ends in
Hits / Does not hit. The map's unit. `card-types.md`.

**Catalog.** The front door. Small on purpose: it points, it stores almost nothing.
Shelves by hub, two hops to any card. A navigation node, excluded from the graph.

**Centrality (betweenness).** How many shortest paths run through a node, the tool's
measure of a true broker (usually not the most-linked node, and usually not the
technology). A ghost high on it is a load-bearing absence. `gap-heuristics.md`,
`tools/gap-scan.py`.

**Correction log.** The running record of where a card was wrong and the source
corrected it. The file wins over the card. `rules.md`, `examples.md`.

**Degree tripwire.** A Pass 2 reading check: a noun marked live that wires to nothing,
or to one thing only, is the structure flagging a ghost. Find the real movement in a
source, or confirm the ghost. Do not force a link to save it. Lineage: Terroir's
node-zone reading (emergent / attracted / integrated, by edge count). `cartography.md`.

**Discovery (Pass 1).** The first pass of a run: scope, gather, build the reference
frame, shelve, and write `Inventory.md`. Inventory before cards. `discovery.md`.

**Evaluative layer (the relief).** The plane the nouns sit in: tensions and gradients.
See "Two planes" above and `identity.md`. Lineage: Terroir's evaluative field.

**External reference-frame gap.** A gap found by looking outward: what a comparable
analogue carries that this territory lacks. Yields a required-but-absent ghost. The
InfraNodus move. `cartography.md` move 6, `gap-heuristics.md`.

**Ghost.** A name with no wiring: referenced in the body of work, but no source gives
it a holder, an instrument, an authority, or a money path. A tripwire, not a lie:
marked, never deleted. Two flavors:
- **Named-but-unwired** (the core flavor): a label present in the sources with no real
  edges. Confirmed in Pass 2 after wiring. `rules.md`.
- **Required-but-absent:** a link the live chain needs that appears in no source. Found
  in the Pass 2 reference-frame gap hunt. `gap-heuristics.md`.

**Ghost-candidate.** A Pass 1 provisional mark: a name with no substance in the source.
Not yet confirmed; Pass 2 wiring decides whether it becomes a confirmed ghost.
`discovery.md`.

**Ghost capability.** A capability that is valuable but held by no one. The VRIO
"Organized" check: a capability is live only if an actor actually holds and can
exercise it. "Everyone says the region can do X" is not "an actor holds X." Lineage:
Cicero / Boundaryless. `rules.md`.

**Gradient.** An evaluative marker: a directional pressure with a cost and a threshold
(direction, what it trades off, the tipping point it approaches). One of the two
relief markers. Lineage: Terroir's evaluative signal (direction, strength, temporal
horizon). `card-types.md`.

**Hits / Does not hit.** The required last line of every card. Hits: the objects that
move if you change this one. Does not hit: the obvious wrong neighbour, the word
everyone reaches for that this change does not touch. Without it, a card is a glossary
entry, not a map. `rules.md`, `card-types.md`.

**Hub (shelf).** A catalog grouping a noun is filed under, drawn from the lens and the
territory, not a fixed list (ET shelved by governance / funding / engagement; a Business
Model Canvas run by audience / core / revenue). A shelf is where a reader finds a card,
not a graph edge: edges come only from typed movements, so shelving wires a noun to
nothing. `emergent` is the honest home for a noun that fits no shelf, used only when
none applies. Lineage: Terroir's attractors, with a deliberate divergence: Terroir made
the hub a real node so every node kept a connection; here shelving creates no edge, and
a ghost is never shelved to look connected.

**Instrument.** One of the six nouns. A formal device that binds or enables (contract,
MOU, grant, permit, zoning, tax arrangement, treaty). Carries binding strength and
money-routing. `card-types.md`.

**Internal structural gap.** A gap found by looking inward: two live clusters with no
movement between them. `tools/gap-scan.py` surfaces it. `cartography.md` move 6,
`rules.md` ("the two gaps").

**Inventory.md.** What Pass 1 writes into the run's map folder: the run header, the
source log, the reference frame, and the noun inventory with provisional marks. No
cards, no catalog. The checkpoint Pass 2 consumes. `discovery.md`.

**Jurisdiction.** One of the six nouns. A territorial or legal authority envelope: whose
law, whose tax, whose permit applies. `card-types.md`.

**Later reader.** Who the map is for: often a cold model with no memory, sometimes a new
person. Same map, same job. Saying the reader is a model is the real answer, not the
lesser one. `identity.md`.

**Leftover.** A marking: was live, still referenced, no longer load-bearing. Honest
residue, marked so no one treats it as current. `rules.md`.

**Lens.** A reading grammar: how to read the territory, the questions and the working
vocabulary to hunt with. Generates questions, never verdicts, which is why the deck can
be canned. Assembled per run into a mix (open / deepen / converge). `discovery-lenses.md`.

**Live.** A marking: named in a current source and wired (a holder, an instrument, an
authority, or money actually routing). `rules.md`.

**Movement (edge).** A typed relationship between nouns. Closed set: holds,
binds / enables, governs, routes-funds-to, depends-on, decides / supersedes,
contested-by. Only typed movements are edges; a mention in a description is not.
`card-types.md`.

**Naming collision.** A word that means different things in this territory (Node,
Commitment, Federation, Host, Grant). The collisions are written down in
`card-types.md`; that file is authoritative for them.

**North Star.** The map's meta note: what the map is really about. A navigation node,
excluded from the graph.

**Noun.** An object that earns a card: exactly one of the six types, and named in a
source. If a candidate is a relationship it is a movement; a directional pressure, a
gradient; a live conflict, a tension; a wish with no holder, a ghost. `rules.md`,
`card-types.md`.

**The one rule.** How a cold reader walks: load the catalog, then one card, then stop.
Never the whole `objects/` folder. `README.md`, `rules.md`.

**Pass.** One of the two halves of a run: Pass 1 Discovery, Pass 2 Cartography. One
agent, one session, one folder. A checkpoint (`Inventory.md`) passes between them inside
the run. Not a pipeline: nothing is handed to another folder or agent. `discovery.md`,
`cartography.md`.

**Pending.** One of the four marks. A forthcoming object, named in a source as coming
or in preparation, not yet wired, but on a credible sourced path to becoming live (a
bidbook in preparation; a decision on a set track but not yet made). Distinct from a
ghost (no sourced path) and from leftover (was once live). This is the canonical fourth
mark; "candidate" is retired as a status and kept only as the ET domain term (a
candidate site). `rules.md`.

**Reference frame (yardstick).** How to judge absence: the dimensions a complete version
of this territory should carry, built per run from the user's frameworks plus two
studied analogues (their model, their successes and their failures). Generates verdicts,
so it is earned fresh every run, never canned. `reference-frames.md`.

**Relief.** See Evaluative layer. The 3D terrain a flat catalog cannot show, the reason
the map carries tensions and gradients. `identity.md`.

**Shared Resource.** One of the six nouns. The heavy commons multiple actors use: the
instrument itself, the site, pooled funds, shared data. `card-types.md`.

**Tension.** An evaluative marker: a structural conflict, both sides live now, neither
fully satisfiable, and solving everything else would not dissolve it. One of the two
relief markers. Lineage: Terroir's tension marker (related nodes, resolution status).
`card-types.md`.

**The two gaps.** The map's product, not the cards. The ghost (a node present by name,
absent in wiring) and the structural gap (two live clusters with no edge). Naming the
gap is the job; prescribing the fix is a diagnostician's job, out of scope. `rules.md`.

**UNVERIFIED / research question.** How a silence is recorded: `UNVERIFIED - research:
<question>`, never a guess. An absence is a finding, not a blank to fill. `rules.md`.

---

## Housekeeping note (resolved 2026-08-24)

The marking scheme is four marks: **live / pending / leftover / ghost** (`rules.md`).
Earlier drafts also used **candidate** for a forthcoming object; that is now folded into
**pending**, and "candidate" is kept only as the ET domain term (a candidate site). The
map cards already matched this: they carry `pending`, never `candidate`, as a status.

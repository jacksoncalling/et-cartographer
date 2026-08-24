# Cartography — Pass 2 of the run (wire, confirm, hunt, write)

Pass 2 of the two-pass run. It reads the `Inventory.md` that Pass 1 (`discovery.md`)
wrote into the run's map folder, and turns that honest pile of nouns into the
walkable map. Same agent, same session, same folder. `Inventory.md` is a checkpoint
consumed inside the run, not a handoff to another agent or folder. The map is the
product.

**Precondition:** `Inventory.md` exists for this run: the noun inventory, the
provisional live / pending / leftover / ghost-candidate marks, and the reference frame. If it
does not, you are still in Pass 1. Go back to `discovery.md`.

## The Pass 2 moves

5. **Wire.** Connect the nouns with the canonical movements in
   `reference/card-types.md` (holds, binds / enables, governs, routes-funds-to,
   depends-on, decides / supersedes, contested-by). Only typed movements are edges; a
   mention in a description is not an edge. Then apply the **degree tripwire**: a noun
   the inventory marked live but that wires to nothing, or to one thing only, is the
   structure flagging a ghost. Do not force a link to save it. Either find the real
   movement in a source, or confirm it as a **named-but-unwired ghost**. This is where
   a ghost-candidate from Pass 1 becomes a confirmed ghost, on evidence.
6. **Hunt gaps, two methods, side by side.** A gap is not found one way. Run both, and
   keep them distinct:
   - **Internal structural gap** (looks inward, at the wiring). Run
     `tools/gap-scan.py` on the map folder. It ranks nouns by how many paths run
     through them (betweenness), groups them into clusters (modularity), and surfaces
     two live clusters with no edge between them. The gap is a missing bridge *inside*
     the territory.
   - **External reference-frame gap** (looks outward, at the yardstick). Take the
     reference frame Pass 1 built and lay this territory against the analogues. Where a
     comparable project carries something this one lacks, classify the absence before
     you call it a gap:
     - **Commodity absence.** The missing piece is well-evolved and everyone in this
       class has it (a financing vehicle, an IP framework). The finding is "adopt the
       known pattern," a **required-but-absent ghost**.
     - **Genesis absence.** No analogue has a settled answer, because the territory is
       on the frontier. The finding is "research required," not a deficiency. This is
       why ET carries so much research: a cross-border financing vehicle for a
       three-country build is genuinely uncharted, not a missing best practice.
     Same yardstick, two verdicts. Calling an absence a ghost when it is really genesis
     scores the territory against a template and hides where the real innovation is.
     This is the InfraNodus move, find what the territory never listed by measuring it
     against ones that did, and let the evolution axis (Wardley, in the lens deck) say
     whether the absence is a missing commodity or an open frontier.
   Write every gap as `UNVERIFIED - research: <question>`, never as an answer.
7. **Write the map.** Produce, in the run's map folder:
   - `Catalog.md`, the front door. Small on purpose. It points, it stores almost
     nothing. Shelves by hub, two hops to any card.
   - one card per noun under `objects/`, each citing its source, each ending in
     **Hits / Does not hit**. Follow the walk order in `reference/card-types.md`.
   - the **evaluative layer**, the relief (see `identity.md`, "Why the map carries
     relief"): tensions (a structural conflict, both sides live now) and gradients (a
     directional pressure with a cost and a threshold). These are detected from the
     structure and voiced by the model. They are never invented.
   - `North Star.md` (what the map is really about) and a **correction log**.
8. **Iterate.** New artifacts arrive; re-run from the pass they touch. If a card and a
   source disagree, the source wins and the card is corrected, logged in the
   correction log.

## The discipline (carried from `rules.md`)

- Cite a source for every card. No source, no card. The file wins over the card.
- A ghost is marked, never deleted. A silence is a research question, never a guess.
- Catalog, then one card, then stop. Never load the whole `objects/` folder. If the
  output slurps the shelves, tours the week, lists everything wrong, or names why
  something failed, it is not a map. Send it back.

## Where the example lives

`examples.md` is one completed run of both passes, shown as its output shape: a
catalog, a few cards, a ghost, a tension, a correction log. Read it to see the shape,
not to copy its contents. Your territory will have different nouns, different ghosts,
and a different north star.

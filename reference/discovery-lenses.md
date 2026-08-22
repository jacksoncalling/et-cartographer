# Discovery Lenses — the catalogue of reading models

> A lens is a **reading grammar**: a way to orient the inquiry before you gather.
> It tells you what kind of thing you are looking at, what question structures the
> read, and what working vocabulary to hunt with. Point the cartographer at a body
> of work with no lens and it latches onto whatever word is loudest in the prompt
> or the first source, and the read wanders. A lens is a commitment device. It
> pre-commits the nouns so a stray word cannot hijack the map.
>
> This file is the catalogue. It is meant to grow. Add your own models with the
> drop-in template at the bottom.

---

## Three things that are easy to confuse

Keep these separate. They do different jobs at different steps of a run.

| | What it is | What it produces | Where it fires |
|---|---|---|---|
| **Lens** (this file) | how to *read* the territory | the questions and the working vocabulary | step 1 (scope) and step 4 (shelve) |
| **Card type** (`card-types.md`) | how to *type* what you find | the closed noun set every object is filed under | step 4 (shelve) and step 7 (write) |
| **Reference frame** (`reference-frames.md`) | how to *judge absence* | the yardstick that makes a gap a fact, not an opinion | step 3 and step 6 (hunt gaps) |

The important line: **a lens generates questions, a reference frame generates
verdicts.** That is why this catalogue is allowed to be pre-built and canned, while
the reference frame must be earned fresh every run. Asking "who are the customer
segments?" commits you to nothing about the territory. Claiming "they are missing a
financing vehicle" is a verdict, and a verdict has to be grounded in evidence, not
in a model you picked off a shelf.

## The lens serves the user, not the other way around

Most runs start with the user bringing their own material (transcripts, code, PDFs,
a registry) and already knowing what they want mapped. **Their question rules the
run.** The lens is chosen to fit that question and to give structure to what they
brought. It does two jobs:

1. **Structure the material you were handed.** The lens vocabulary is the checklist
   you shelve the user's artifacts against, so nothing salient is dropped and
   nothing loud is over-weighted.
2. **Guide external depth.** The same vocabulary tells you what to go research
   beyond the material, so the map gains depth the user could not see from inside.

When the user is explicit about scope, external discovery *deepens* the map
(analogues, missing pieces, the wider field). It does not re-scope the territory.
The cartographer adds depth; it does not overrule the person who brought the work.

## Compose a mix, do not just pick

A territory rarely fits one model cleanly, and understanding a genuinely tangled one
does not happen in a single pass. Borrowing from Stanford d.school's design-thinking
mixtape: this catalogue is the **deck**, and a run assembles a short **mix**, an
ordered route you play through the deck for this particular territory. The order is
the point. You open the space with one lens, then go deeper with another, then
converge. Selection is what you take; sequence is how understanding unfolds.

Assemble the mix in step 1, giving each lens a **role** and a one-line reason:

- **Open** — the lens that first exposes the shape of the territory and names its
  main entities. Often an ecosystem or component lens, something wide.
- **Deepen** — a lens that goes into the part the opening lens flagged as the core.
  A venture opened with the Platform Design Toolkit might be deepened on its
  central actor with the Business Model Canvas.
- **Converge** — an optional third lens that sharpens the thing the map is really
  about: the contested language (ontology), the job being served (JTBD), the
  bottleneck (data-flow).

Discipline on the mix:

- **A mix of one is a valid mix.** When the user brought a well-understood territory
  and a clear question, one lens played straight through is correct. Do not stack
  lenses to look thorough.
- **Cap it at three.** More than open / deepen / converge turns the map into soup. If
  you feel the pull for a fourth, the territory is probably two territories, and you
  should say so instead of extending the mix.
- **Every track on the mix earns its reason.** A lens with no role and no reason
  behind it is drift waiting to happen. That one-line justification is what keeps a
  canned deck honest.

The mix is not the design-thinking phase model. Design thinking runs empathise to
ideate to prototype, a divergent arc toward a *solution*. The cartographer is
diagnostic, not generative: it maps a body of work that already exists. What transfers
from the mixtape is the composability and the sequence, not the solutioning arc. The
phases the mix moves through are the cartographer's own discovery moves (open,
deepen, converge over the same territory), not d.school's.

---

## Categories

The catalogue is organised by the challenge's own three tracks. Most territories
sit mainly in one, and borrow a secondary lens from another.

- **Technical** — a system, a codebase, an architecture, a pipeline. The mental
  model lives in the structure.
- **Business** — a venture, a market, a platform, an ecosystem. The mental model
  lives in who exchanges what value with whom.
- **Creator** — a body of creative or intellectual work, a knowledge corpus, a
  personal system, an audience. The mental model lives in the through-line and who
  it serves.

Classifying is the first move of step 1: which track, and what shape and scale
(a solo creator's vault is not a cross-border megaproject).

---

## Quick-scan table

Read this table, pick, then read the one or two full entries you chose. Do not read
every entry; that is the same discipline as loading the catalog then one card.

| Lens | Category | Territory shape | The question it forces |
|---|---|---|---|
| Business Model Canvas | Business | a venture, one organisation making and capturing value | who is served, with what value, paid for how? |
| Platform Design Toolkit | Business | a many-sided platform or ecosystem of interacting parties | who are the entities, and what does the platform let them exchange? |
| Wardley Mapping | Business | a value chain of capabilities serving a user need, pieces evolving | what does the user need, and how mature is each capability serving it? |
| Theory of Constraints | Business | a flow or chain capped by one bottleneck | where is the one constraint, and is everything subordinated to it? |
| Three Economies | Business | an org or platform balancing efficiency and distinctiveness | which economy (differentiation / scale / scope) is each part running on? |
| Component / dependency model (C4) | Technical | a system or codebase with parts that call each other | what are the parts, the boundaries, and what depends on what? |
| Domain-Driven Design context map | Technical | a codebase whose meaning splits across teams or modules | where are the bounded contexts, and how do they translate at the seams? |
| Data-flow / pipeline | Technical | anything that moves and transforms data end to end | where does data enter, what transforms it, where does it rest or leave? |
| Jobs-to-be-Done (demand-side) | Creator | a product, service or body of work helping someone make progress | what job is this hired to do, and what forces drive the switch? |
| Ontology / concept map | Creator | a knowledge corpus, research vault, or set of documents | what are the concepts and how are they related? |
| Body-of-work map | Creator | a portfolio, a catalogue of content, an oeuvre | what is the through-line, and who is each piece for? |

---

## Full entries

Each entry follows the same schema so the agent can reason across them: the
originator, the territory shape, the question it forces, the working vocabulary to
hunt with, how that vocabulary types into `card-types.md`, what it pairs with, and
when not to use it.

### Business Model Canvas
*Osterwalder & Pigneur.*

- **Territory shape.** A single venture that makes and captures value. Best when the
  unit of analysis is one organisation, not a whole market.
- **The question it forces.** Who is served, with what value, delivered how, paid
  for how, at what cost?
- **Working vocabulary.** Customer segments, value propositions, channels, customer
  relationships, revenue streams, key resources, key activities, key partners, cost
  structure.
- **Types into card-types.** Segments and partners become Actors. Key resources
  become Capabilities or Shared Resources. Revenue streams and cost structure read
  as Gradients (directional pressures) or as Instruments where a contract carries
  the money. A pricing or access choice is a Decision.
- **Pairs well with.** Platform Design Toolkit (when one of the segments is really a
  second side of a platform); Jobs-to-be-Done (to sharpen the value proposition).
- **Do not use when.** The territory is a multi-sided ecosystem where value flows
  between parties the venture only mediates. The canvas will flatten that into
  "segments" and hide the real structure. Use the platform lens instead.

### Platform Design Toolkit
*Simone Cicero.*

- **Territory shape.** A many-sided platform or an ecosystem of interacting parties
  where value is exchanged between participants, not just sold by one firm.
- **The question it forces.** Who are the entities in the ecosystem, what does each
  want, and what exchanges does the platform enable between them?
- **Working vocabulary.** Ecosystem entities and their roles (peer producers, peer
  consumers, partners), the platform's value propositions to each, the transactions
  and channels, the enabling and empowering services, the learning loops.
- **Types into card-types.** Entities and roles become Actors. Enabling services
  become Capabilities or Shared Resources. Transactions that are formalised become
  Instruments; the exchange logic itself often surfaces a Tension (two sides pulling
  against each other) or a Gradient.
- **Pairs well with.** Business Model Canvas (for the platform-owner's own capture);
  Wardley (to see which ecosystem services are commoditising).
- **Do not use when.** There is really only one side and one seller. Forcing an
  ecosystem frame onto a linear business invents participants that are not there.

### Wardley Mapping
*Simon Wardley.*

- **Territory shape.** A value chain of capabilities that serve a user need, whose
  pieces sit at different stages of maturity and where positioning and movement
  matter. Use it to understand the user need and the chain of capabilities a supply
  chain must provide to answer it.
- **The question it forces.** What does the user need, what chain of capabilities
  serves that need, and how evolved (genesis to commodity) is each one?
- **Working vocabulary.** User need, value chain, capabilities and components,
  evolution stages (genesis, custom-built, product, commodity), movement and inertia.
- **Types into card-types.** Capabilities and components become Capabilities or Shared
  Resources. Evolution and movement read as Gradients (a directional pressure with a
  cost and a threshold). Strategic plays are Decisions. A capability the chain needs
  that no one supplies is a Ghost.
- **Pairs well with.** Business Model Canvas (what the venture captures on top of the
  chain); component/dependency model (the technical realisation of the chain); Theory
  of Constraints (which link in the chain actually caps throughput).
- **Do not use when.** The territory has no meaningful evolution axis, or you have no
  evidence for where pieces sit on it. A guessed evolution stage is a bias dressed as
  a map.

### Theory of Constraints
*Eliyahu Goldratt.*

- **Territory shape.** A system whose output is capped by one binding constraint: a
  pipeline, a supply chain, an organisation's delivery flow, any chain of dependent
  steps with a bottleneck.
- **The question it forces.** Where is the one constraint that limits the throughput
  of the whole system, and is everything else subordinated to it or fighting it?
- **Working vocabulary.** Throughput, the constraint (bottleneck), the five focusing
  steps (identify, exploit, subordinate, elevate, repeat), buffers, subordination,
  inventory and operating expense, local versus global optima.
- **Types into card-types.** Flow stations are Capabilities or Shared Resources. The
  constraint reads as a Gradient (a directional pressure with a threshold) and usually
  surfaces a Tension (local efficiency pulling against global throughput). A focusing
  step taken is a Decision. A bottleneck everyone names but no one has measured is a
  Ghost.
- **Pairs well with.** Data-flow / pipeline (the structural flow the constraint sits
  in); Wardley (whether the constraint is worth elevating or is merely evolving to
  commodity); Three Economies (the grinding gears often sit right on the constraint).
- **Do not use when.** The territory is not a flow with a throughput to maximise. A
  body of ideas or a portfolio has no bottleneck in this sense, and forcing one
  invents a false chokepoint.

### Three Economies
*Jabe Bloom.*

- **Territory shape.** An organisation or platform trying to be efficient and
  distinctive at once, where you need to read which economic logic each part is really
  optimising for and where those logics grind against each other.
- **The question it forces.** Which of the three economies is each part running on:
  differentiation (value from being unique), scale (value from cheaper reproduction of
  the same), or scope (value from reuse), and where do they conflict?
- **Working vocabulary.** Differentiation, scale, scope; consumables (used up, access
  controlled) versus reusables (things that gain value in reuse); the "grinding gears"
  of differentiation against scale; scope as the "clutch" and the platform that
  isolates the two; adoption and reuse as the measure of scope.
- **Types into card-types.** Each economy reads as a Gradient (a directional pressure
  with a cost). The differentiation-versus-scale opposition is a textbook Tension. A
  scope platform (the reusable substrate) is a Shared Resource. A reusable asset
  everyone cites that nothing actually reuses is a Ghost.
- **Pairs well with.** Platform Design Toolkit (scope economies are platform
  economies); Wardley (scale maps to commoditising components, differentiation to
  genesis); Theory of Constraints (the grinding gears often sit on the constraint).
- **Do not use when.** The territory is a single-logic operation with no live tension
  between efficiency and distinctiveness. The three-economy read manufactures a
  conflict that is not there.

### Component / dependency model (C4)
*Simon Brown's C4, or any module-dependency view.*

- **Territory shape.** A system or codebase whose parts call, contain, or depend on
  each other. The mental model is in the structure.
- **The question it forces.** What are the parts, where are the boundaries, and what
  depends on what?
- **Working vocabulary.** Systems, containers, components, code; dependencies,
  interfaces, boundaries; the level of zoom you are reading at.
- **Types into card-types.** Components and services become Capabilities (a capacity
  tied to a holder). The runtime or shared datastore is a Shared Resource. A
  dependency is a movement (`depends-on`). An architectural choice already made is a
  Decision. A boundary that everyone assumes but nothing enforces is a Ghost.
- **Pairs well with.** Domain-Driven Design context map (meaning at the seams);
  data-flow (what actually moves through the parts).
- **Do not use when.** The question is about meaning, ownership, or language rather
  than call structure. Two components can be cleanly separated in code and hopelessly
  entangled in meaning. Reach for the context map.

### Domain-Driven Design context map
*Eric Evans.*

- **Territory shape.** A codebase or organisation whose meaning splits across teams
  or modules, where the same word means different things in different places.
- **The question it forces.** Where are the bounded contexts, what is the language
  inside each, and how do they translate (or fail to) at the seams?
- **Working vocabulary.** Bounded contexts, ubiquitous language, aggregates, context
  map relationships (shared kernel, customer-supplier, conformist, anticorruption
  layer, separate ways).
- **Types into card-types.** Each bounded context is an Actor or a Jurisdiction (a
  meaning-authority envelope). A translation layer is an Instrument or a Capability.
  A word that means two things across a seam is a naming collision, which
  `card-types.md` requires you to write down. An unowned context is a Ghost.
- **Pairs well with.** Component/dependency model (the structural view under the
  meaning view); ontology/concept map (for the language itself).
- **Do not use when.** The system is small enough to hold in one head, or has one
  clear language throughout. The context-map machinery will manufacture seams that do
  not exist.

### Data-flow / pipeline
*A classic dataflow view.*

- **Territory shape.** Anything whose essence is moving and transforming data or
  material end to end: an ETL pipeline, an ML training flow, a supply chain.
- **The question it forces.** Where does data enter, what transforms it in what
  order, and where does it rest or leave?
- **Working vocabulary.** Sources, transforms, stores, sinks; the flow between them;
  batch versus stream; where state accumulates.
- **Types into card-types.** Stores are Shared Resources. Transforms are Capabilities.
  The flow is the `depends-on` movement. A stage everyone assumes runs but nothing
  actually triggers is a Ghost. A backlog or bottleneck is a Gradient.
- **Pairs well with.** Component/dependency model (what hosts the stages); DDD
  context map (whose meaning each store carries).
- **Do not use when.** The territory is not fundamentally a flow. Forcing a pipeline
  onto a web of mutual dependencies imposes a false linearity.

### Jobs-to-be-Done (demand-side)
*Bob Moesta, with Clayton Christensen.*

- **Territory shape.** A product, service, or body of work whose point is to help
  someone make progress. Strong for a creator or a venture working out who and what
  the work is really for, read from the demand side.
- **The question it forces.** What job is someone hiring this to do, in what struggling
  moment, and what forces push them toward the switch and hold them back from it?
- **Working vocabulary.** The job (functional, emotional, social), the struggling
  moment, the timeline of the switch (first thought to hiring), and the four forces of
  progress: push of the current situation, pull of the new solution, anxiety about the
  new, habit of the present. Hiring and firing moments.
- **Types into card-types.** The person doing the hiring is an Actor. The job and the
  progress sought read as a Gradient (a pull toward something, at a cost). A competing
  solution, the thing being fired, is another Actor or Capability. The moment of
  switching is a Decision. The four forces surface as Tensions (push and pull against
  anxiety and habit).
- **Pairs well with.** Business Model Canvas (a sharp job becomes a value
  proposition); body-of-work map (which pieces serve which job).
- **Do not use when.** You have no contact with the actual people and would be
  inventing their jobs. A made-up job is the cartographer's bias wearing a customer's
  clothes.

### Ontology / concept map
*A knowledge-graph or concept-map view.*

- **Territory shape.** A knowledge corpus, a research vault, a set of documents, a
  field of ideas. The mental model is a web of concepts.
- **The question it forces.** What are the concepts, how are they related, and where
  are the clusters and the bridges between them?
- **Working vocabulary.** Concepts, relations (is-a, part-of, causes, contradicts),
  categories, clusters, bridging concepts, orphans.
- **Types into card-types.** A concept-as-thing can be a Capability or a Shared
  Resource; a category is a Jurisdiction (an envelope other concepts fall under). A
  relation is a movement. A concept everyone cites with no definition anywhere is a
  Ghost. A clash between two framings is a Tension.
- **Pairs well with.** DDD context map (when the corpus is also a system); body-of-work
  map (when the concepts are someone's oeuvre).
- **Do not use when.** The territory is really about people and exchange, not ideas.
  An ontology of an ecosystem hides the actors and their transactions.

### Body-of-work map
*A portfolio / oeuvre view, creator-native.*

- **Territory shape.** A creator's catalogue: a body of writing, talks, products,
  releases, a portfolio. The mental model is a through-line across many pieces.
- **The question it forces.** What is the through-line connecting the work, who is
  each piece for, and what is present, repeated, or conspicuously missing?
- **Working vocabulary.** Pieces, themes, the through-line, audiences, phases or eras,
  formats, the recurring move, the gap in the catalogue.
- **Types into card-types.** Each piece and each audience is an Actor or a Capability.
  A recurring theme is a Gradient or a Shared Resource. A promised-but-never-made
  piece, the book everyone expects and it does not exist, is a Ghost. A pull between
  two audiences is a Tension.
- **Pairs well with.** Jobs-to-be-Done (who each piece serves); ontology (the ideas
  running through the work).
- **Do not use when.** There is no body yet, only a single piece or a plan. Map what
  exists, not what is hoped for.

---

## How to add a lens

The catalogue is meant to grow. To add one, keep the entry schema exact so the agent
can reason across all of them, and add a row to the quick-scan table. A lens earns a
place only if it forces a genuinely different question than the ones already here.
Two lenses that ask the same question are one lens.

```
### <Lens name>
*<originator or source>.*

- **Territory shape.** <when the territory looks like this>
- **The question it forces.** <one line>
- **Working vocabulary.** <its nouns, what to hunt for>
- **Types into card-types.** <how its nouns map into the closed set in card-types.md>
- **Pairs well with.** <composition hints>
- **Do not use when.** <the anti-pattern that makes this lens lie>
```

Two rules for a good addition:

1. **A lens generates questions, never verdicts.** If your candidate asserts what the
   territory contains rather than asking, it is a reference frame, and it belongs in
   `reference-frames.md` where it has to be earned, not here where it is canned.
2. **Name the anti-pattern.** The "Do not use when" line is the most valuable part.
   A lens without a stated failure mode will get applied everywhere and flatten
   territories it does not fit.

---

## Relationship to the reference frame

A lens and a reference frame can come from the same model. The Platform Design
Toolkit, for instance, is a lens here (it structures the read) and can also feed
`reference-frames.md` as one of the user's own named frameworks (it suggests
dimensions a healthy platform carries). That is fine, as long as the two jobs stay
separate: use it to ask questions in step 1, and only let it make absence claims in
step 6 after those claims are grounded against real analogues. Same model, two
disciplines. The lens is where you look. The frame is what you are allowed to say is
missing.

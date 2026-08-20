# Discovery — how to run the cartographer on a body of work

This is the run protocol. It is deliberately general. The worked example in
`examples.md` is one territory (the Einstein Telescope ecosystem), but the moves
below apply to any body of work: a repo, an Obsidian vault, a client delivery
folder, a set of grant PDFs, an organisation's public artifacts.

## What you are actually mapping

Not "the domain." You are mapping the **mental model a body of work expresses**:
the operative model held by whoever produced these artifacts. The map shows its
shape, and, more valuably, its holes. What is present, what is wired, and what has
a name but no substance.

## What to point it at (source types)

Feed it artifacts, not summaries. Any of:

- **Websites** - landing pages, "about", partner/ecosystem pages, directories.
- **PDFs** - grant applications, reports, research papers, bidbooks, white papers.
- **Markdown / docs** - notes, wikis, READMEs, specs.
- **Code / repos** - source files, module layouts, configs (the mental model of a
  system is in its structure).
- **Registries / spreadsheets** - member lists, supplier maps, asset inventories.
- **News / newsletters** - because transparency-over-time is itself a signal of
  how a project keeps its ecosystem informed.
- **Events / workshops / education** - listings show how the ecosystem is kept
  active and who is being cultivated.
- **Transcripts** - interviews, talks, meeting notes.

Point the cartographer at these. Do **not** paste them wholesale into the chat.
The cartographer reads sources to build the map; it never copies the source into
the reader's lap.

## The run, step by step

1. **Scope.** Name three things in one line each: the territory, the later reader
   (say if it is a model), and the question the map must let them answer.
2. **Gather.** Find and pull the artifacts. This includes searching and scraping
   the web for what is out there, not only reading what you were handed. Log every
   source with a link and a date. (This is a run-time act the AI performs; the
   folder instructs it, it does not scrape by itself.)
3. **Build the reference frame.** Before anything can be called a gap, build the
   yardstick per `reference/reference-frames.md`. Two sources, both cited:
   (a) **ask the user** which models or frameworks they use for this domain; and
   (b) research at least **two comparable analogues**, matched to this territory's
   shape and scale (a corner shop is not measured against CERN). For each analogue,
   go deep: what model did they use, what is documented about their successes AND
   their failures, what dimensions did they carry. Naming a reference without
   studying how it works and where it broke does not count. The dimensions a
   complete model should carry are read off this evidence, never from your own head
   or the user's offhand remarks. (For an ET-scale run, two analogues might be
   Virgo and an ERIC-style multinational infrastructure, plus the EU guidance for
   multi-country collaborations.)
4. **Shelve.** Extract entities. Assign each to a hub (`domain`, `capability`,
   `governance`, `funding`, `engagement`, `emergent`). Type each against the
   closed noun set in `reference/card-types.md`. Mark each **live / leftover /
   ghost**.
5. **Wire.** Connect entities with canonical movements. A card that connects to
   nothing is a suspect; either find its link or mark it emergent.
6. **Hunt gaps.** Run both scans in `reference/gap-heuristics.md`: the by-hand
   scan against the reference frame you built in step 3, and the computed
   `tools/gap-scan.py` (real hubs, clusters, load-bearing ghosts). Write each gap
   as `UNVERIFIED - research: <question>`.
7. **Write the map.** Produce `map/catalog.md` (the front door), one card per
   object under `map/objects/`, the evaluative layer (tensions, gradients, north
   star), and a correction log. Follow the walk order in `card-types.md`.
8. **Iterate.** New artifacts arrive; re-run. If a card and a source disagree, the
   source wins and the card is corrected, logged in the correction log.

## The discipline (carried from `rules.md`)

- Cite a source for every card. No source, no card.
- Mark verified vs open. A ghost is marked, never deleted.
- Never fill a silence with a guess. A silence is a research question.
- Load the catalog, then one card, then stop. Never load the whole `objects/` folder.

## Where the example lives

`examples.md` is one completed run of this protocol. Read it to see the shape of
the output, not to copy its contents. Your territory will have different nouns,
different ghosts, and a different north star.

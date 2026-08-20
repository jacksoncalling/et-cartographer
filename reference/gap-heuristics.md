# Gap Heuristics — how the cartographer pokes holes

The map's value is not the cards. It is what the cards make visible: what is
missing, what is unwired, what should connect and does not. Gaps are found two
ways, and both belong in a run.

---

## A. By hand (the interpretable scan)

Walk the catalog and run three scans. No maths required.

1. **Absent-hub scan.** For each hub a complete model of this territory would
   carry (see `reference-frames.md`), ask: is this region populated at all? An
   empty or missing hub is a blind spot. (For ET: no risk/security hub, no
   horizon hub, no economics hub.) Flag it against the reference, never as a
   verdict. It may be genuinely absent, or non-public. Mark it a research
   question.
2. **Required-but-absent scan.** For each live node, ask: what would it depend
   on to actually work, that appears nowhere? That missing link is a ghost of the
   "required-but-absent" flavor (the cross-border financing vehicle; a shared IP
   framework).
3. **Missing-bridge scan.** For each pair of live clusters, ask: should these
   connect, and do they? Two real worlds with no edge between them is a
   structural gap (the funding world and the governance world, thinly bridged).

Every gap found this way is written as `UNVERIFIED - research: <question>`, per
the research trigger in `rules.md`. Naming the gap is the job. Prescribing the
fix is not.

---

## B. By machine (`tools/gap-scan.py`)

The same three moves, computed. This is the cheap version of InfraNodus:
standard graph theory over the `[[wikilinks]]` in `map/`, no heavy libraries.

Run it:

    python tools/gap-scan.py

It reports four things:

- **Real hubs — betweenness centrality.** The nodes most shortest paths run
  through. These are the true brokers, which are usually NOT the nodes with the
  most links, and usually NOT the technology. (For ET the top three were a
  governance body, a tension, and a decision. The physics sat at the bottom.)
- **Load-bearing absence — ghosts ranked by betweenness.** A ghost high on this
  list is a missing thing the whole structure leans on. This is the sharpest
  output the tool produces. (The financing-vehicle ghost outscored every funder
  and every lab. The sovereign-zone ghost scored zero: a floating wish, not a
  load-bearing hole. The metric tells them apart.)
- **Clusters — greedy modularity.** The natural worlds in the graph, detected
  from structure, not from the hub labels we assigned. Where the detected
  clusters disagree with the designed hubs, look closer.
- **Structural gaps — weakly connected cluster pairs.** Distant worlds that
  barely touch. When none appear, the clusters that exist are bridged, and the
  seam between them (and any ghost sitting on it) is the thing to examine.

---

## Reading the two together

By-hand finds gaps against a reference frame (what *should* be here). By-machine
finds gaps in the wiring that is here (what leans on what, what fails to
connect). A blind spot the reference predicts AND the graph confirms as
load-bearing is the highest-value finding on the map.

---

## Calibration (wire first, tune later)

The algorithms are correct out of the box. These knobs are set by looking at
results on a real map, never in advance:

- **Cluster resolution.** Modularity merges small communities (a known resolution
  limit). Add a resolution parameter only if you need finer worlds than the run
  returns.
- **Gap threshold.** "One edge or fewer between clusters" is a starting
  definition. Calibrate against a second real map so you are not overfitting to
  one graph.
- **Link weighting.** Every relationship currently counts equally. Weight
  movement types (`funds` over `informs`) only with domain judgment, after you
  have seen unweighted results.

None of these block wiring the tool up. They are the second pass, run against a
second map.

# -*- coding: utf-8 -*-
"""
gap-scan.py  --  the cheap InfraNodus for a cartographer map.

Runs on a map/ folder of the cartographer format (one note per object, links
written as [[wikilinks]], simple YAML frontmatter with type/status).

It reports:
  1. REAL HUBS      - betweenness centrality (navigation nodes excluded).
                      These are the true brokers, the load-bearing nodes.
  2. LOAD-BEARING   - ghost nodes ranked by betweenness. A ghost with high
     ABSENCE          centrality is a missing thing the whole structure leans on.
  3. CLUSTERS       - greedy-modularity communities (the natural worlds).
  4. STRUCTURAL     - cluster pairs that barely connect (the missing mycelium).
     GAPS

The algorithms are standard and need no tuning to be correct. The calibration
knobs (cluster resolution, gap threshold, link weighting) are meant to be set
AFTER looking at results on a real map, not in advance.

Usage:
    python gap-scan.py [path-to-map-folder]
Defaults to ../map relative to this file.
"""
import os, re, sys
from collections import deque, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
MAP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "map")

# ---- load notes ------------------------------------------------------------
files = []
for root, _, fs in os.walk(MAP):
    for f in fs:
        if f.endswith(".md"):
            files.append(os.path.join(root, f))
if not files:
    sys.exit("No .md notes found under: " + os.path.abspath(MAP))

name = lambda p: os.path.splitext(os.path.basename(p))[0]

def frontmatter(txt):
    fm = {}
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        if end != -1:
            for line in txt[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip().lower()] = v.strip().lower()
    return fm

raw = {name(p): open(p, encoding="utf-8").read() for p in files}
meta = {n: frontmatter(t) for n, t in raw.items()}

def is_nav(n):
    fm = meta.get(n, {})
    return fm.get("type") == "meta" or fm.get("role") == "front-door"
def is_ghost(n):
    return meta.get(n, {}).get("status") == "ghost"

# The object graph: navigation nodes (catalog, north star) are excluded from the
# graph itself, not just from the report. A table-of-contents node that links to
# everything would otherwise absorb the paths and distort every score.
nodes = set(n for n in raw if not is_nav(n))
adj = defaultdict(set)
link_re = re.compile(r"\[\[([^\]|#]+)")

def movements_zone(txt):
    """Extract the typed-movements zone of a card, where [[wikilinks]] are
    structural edges. Skips frontmatter, title, description paragraph, and
    stops before Hits/Does-not-hit/Source lines. This mirrors the Terroir
    principle: only canonical typed relationships count as graph edges."""
    body = txt
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        if end != -1: body = txt[end+4:]
    lines = body.splitlines()
    past_title = False
    past_desc = False
    blank_after_desc = False
    zone = []
    for line in lines:
        s = line.strip()
        if not past_title:
            if s.startswith("# "): past_title = True
            continue
        if not past_desc:
            if not s: past_desc = True
            continue
        sl = s.lower()
        if sl.startswith("- hits:") or sl.startswith("- does not hit:"):
            break
        if sl.startswith("source:"):
            break
        if s: zone.append(line)
    return "\n".join(zone)

for s, txt in raw.items():
    if is_nav(s): continue
    mzone = movements_zone(txt)
    for m in link_re.findall(mzone):
        t = m.strip()
        if t != s and t in nodes:
            adj[s].add(t); adj[t].add(s)
for n in nodes:
    adj[n]

# ---- betweenness (Brandes) -------------------------------------------------
def brandes(adj):
    CB = {v: 0.0 for v in adj}
    for s in adj:
        S = []; P = {w: [] for w in adj}; sig = {w: 0 for w in adj}; sig[s] = 1
        d = {w: -1 for w in adj}; d[s] = 0; Q = deque([s])
        while Q:
            v = Q.popleft(); S.append(v)
            for w in adj[v]:
                if d[w] < 0: d[w] = d[v] + 1; Q.append(w)
                if d[w] == d[v] + 1: sig[w] += sig[v]; P[w].append(v)
        dl = {w: 0.0 for w in adj}
        while S:
            w = S.pop()
            for v in P[w]: dl[v] += (sig[v] / sig[w]) * (1 + dl[w])
            if w != s: CB[w] += dl[w]
    for v in CB: CB[v] /= 2.0
    return CB

# ---- greedy modularity communities -----------------------------------------
def communities(adj):
    m = sum(len(v) for v in adj) // 2
    if m == 0: return {n: i for i, n in enumerate(adj)}
    cof = {n: n for n in adj}; members = {n: {n} for n in adj}
    degc = {n: len(adj[n]) for n in adj}
    def lij(a, b):
        return sum(1 for x in members[a] for y in adj[x] if cof[y] == b)
    improved = True
    while improved:
        improved = False; best = None; bestdq = 1e-9
        pairs = set()
        for x in adj:
            for y in adj[x]:
                a, b = cof[x], cof[y]
                if a != b: pairs.add(tuple(sorted((a, b))))
        for (a, b) in pairs:
            dq = lij(a, b) / m - (degc[a] * degc[b]) / (2 * m * m)
            if dq > bestdq: bestdq = dq; best = (a, b)
        if best:
            a, b = best; members[a] |= members[b]
            for n in members[b]: cof[n] = a
            degc[a] += degc[b]; del members[b]; del degc[b]; improved = True
    return cof

bet = brandes(adj)
cof = communities(adj)
comm = defaultdict(list)
for n, c in cof.items(): comm[c].append(n)
clusters = [sorted(v) for _, v in sorted(comm.items(), key=lambda kv: -len(kv[1]))]
cid = {n: i for i, c in enumerate(clusters) for n in c}

# ---- report ----------------------------------------------------------------
edges = sum(len(v) for v in adj.values()) // 2
print(f"map: {os.path.abspath(MAP)}")
print(f"nodes: {len(nodes)}   edges: {edges}\n")

print("=== REAL HUBS (betweenness; navigation nodes excluded) ===")
for n, v in sorted(bet.items(), key=lambda kv: -kv[1]):
    if is_nav(n) or v <= 0: continue
    print(f"  {v:7.1f}  {n}" + ("   [GHOST]" if is_ghost(n) else ""))

print("\n=== LOAD-BEARING ABSENCE (ghosts ranked by betweenness) ===")
gh = sorted([(bet[n], n) for n in nodes if is_ghost(n)], reverse=True)
if gh:
    for v, n in gh:
        print(f"  {v:7.1f}  {n}")
    print("  (a ghost high on this list is a missing thing the structure leans on)")
else:
    print("  (no ghost nodes in this map)")

print("\n=== CLUSTERS (greedy modularity) ===")
for i, c in enumerate(clusters):
    body = ", ".join(x for x in c if not is_nav(x))
    if body: print(f"  C{i} ({len(c)}): {body}")

print("\n=== STRUCTURAL GAPS (cluster pairs with <=1 connecting edge) ===")
pair = defaultdict(int)
for a in adj:
    for b in adj[a]:
        if a < b and cid[a] != cid[b]:
            pair[tuple(sorted((cid[a], cid[b])))] += 1
found = False
for i in range(len(clusters)):
    for j in range(i + 1, len(clusters)):
        if len(clusters[i]) < 2 or len(clusters[j]) < 2: continue
        if pair.get((i, j), 0) <= 1:
            found = True
            ri = [x for x in clusters[i] if not is_nav(x)][:2]
            rj = [x for x in clusters[j] if not is_nav(x)][:2]
            print(f"  C{i} <-> C{j}: {pair.get((i,j),0)} edge  ({', '.join(ri)}... vs {', '.join(rj)}...)")
if not found:
    print("  none: the clusters that exist are bridged. The seam between them")
    print("  (and any ghost sitting on it) is where to look next.")

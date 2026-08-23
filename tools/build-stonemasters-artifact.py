# -*- coding: utf-8 -*-
"""Build the walkable HTML cartography from the map-stonemasters/ notes.
Parses notes, computes betweenness + modularity on the OBJECT graph
(navigation nodes excluded), injects the data into template-stonemasters.html."""
import os, re, json
from collections import deque, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(HERE, "..", "map-stonemasters")
TEMPLATE = os.path.join(HERE, "template-stonemasters.html")
OUT = os.path.join(HERE, "..", "output", "stonemasters-cartographer.html")
EXCLUDE = {"Catalog", "North Star"}

name = lambda p: os.path.splitext(os.path.basename(p))[0]

def read(p): return open(p, encoding="utf-8").read()

def split_fm(txt):
    fm = {}
    body = txt
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        if end != -1:
            for line in txt[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip().lower()] = v.strip()
            body = txt[end+4:]
    return fm, body

LINK = re.compile(r"\[\[([^\]|#]+)")
def clean(s): return s.replace("[[", "").replace("]]", "").strip()

def parse_body(body):
    lines = body.splitlines()
    title = None; i = 0
    for idx, l in enumerate(lines):
        if l.startswith("# "): title = l[2:].strip(); i = idx+1; break
    while i < len(lines) and not lines[i].strip(): i += 1
    desc = []
    while i < len(lines) and lines[i].strip():
        desc.append(lines[i].strip()); i += 1
    hits = miss = None
    for l in lines:
        s = l.strip()
        if s.lower().startswith("- hits:"): hits = clean(s.split(":", 1)[1])
        elif s.lower().startswith("- does not hit:"): miss = clean(s.split(":", 1)[1])
    return title, clean(" ".join(desc)), hits, miss

def movements_zone(body):
    lines = body.splitlines()
    past_title = False; past_desc = False; zone = []
    for line in lines:
        s = line.strip()
        if not past_title:
            if s.startswith("# "): past_title = True
            continue
        if not past_desc:
            if not s: past_desc = True
            continue
        sl = s.lower()
        if sl.startswith("- hits:") or sl.startswith("- does not hit:"): break
        if sl.startswith("source:"): break
        if s: zone.append(line)
    return "\n".join(zone)

# ---- load ----
files = []
for root, _, fs in os.walk(MAP):
    for f in fs:
        if f.endswith(".md"): files.append(os.path.join(root, f))
allnodes = set(name(p) for p in files)
records = {}
north_star = ""
for p in files:
    nid = name(p)
    fm, body = split_fm(read(p))
    title, desc, hits, miss = parse_body(body)
    if nid == "North Star": north_star = desc
    if nid in EXCLUDE: continue
    connects = []
    mzone = movements_zone(body)
    for m in LINK.findall(mzone):
        t = m.strip()
        if t != nid and t in allnodes and t not in EXCLUDE and t not in connects:
            connects.append(t)
    records[nid] = dict(id=nid, label=nid, type=fm.get("type", "Object"),
                        status=fm.get("status", "live").lower(), kind=fm.get("kind", ""),
                        hub=fm.get("hub", ""),
                        desc=desc, hits=hits, doesNotHit=miss, connects=connects)

# ---- graph (object nodes only) ----
adj = defaultdict(set)
for nid, r in records.items():
    for t in r["connects"]:
        if t in records:
            adj[nid].add(t); adj[t].add(nid)
for nid in records: adj[nid]

def brandes(adj):
    CB = {v: 0.0 for v in adj}
    for s in adj:
        S=[]; P={w:[] for w in adj}; sig={w:0 for w in adj}; sig[s]=1
        d={w:-1 for w in adj}; d[s]=0; Q=deque([s])
        while Q:
            v=Q.popleft(); S.append(v)
            for w in adj[v]:
                if d[w]<0: d[w]=d[v]+1; Q.append(w)
                if d[w]==d[v]+1: sig[w]+=sig[v]; P[w].append(v)
        dl={w:0.0 for w in adj}
        while S:
            w=S.pop()
            for v in P[w]: dl[v]+=(sig[v]/sig[w])*(1+dl[w])
            if w!=s: CB[w]+=dl[w]
    for v in CB: CB[v]/=2.0
    return CB

def communities(adj):
    m=sum(len(v) for v in adj)//2
    if m==0: return {n:0 for n in adj}
    cof={n:n for n in adj}; members={n:{n} for n in adj}; degc={n:len(adj[n]) for n in adj}
    def lij(a,b): return sum(1 for x in members[a] for y in adj[x] if cof[y]==b)
    improved=True
    while improved:
        improved=False; best=None; bestdq=1e-9
        pairs=set()
        for x in adj:
            for y in adj[x]:
                a,b=cof[x],cof[y]
                if a!=b: pairs.add(tuple(sorted((a,b))))
        for (a,b) in pairs:
            dq=lij(a,b)/m-(degc[a]*degc[b])/(2*m*m)
            if dq>bestdq: bestdq=dq; best=(a,b)
        if best:
            a,b=best; members[a]|=members[b]
            for n in members[b]: cof[n]=a
            degc[a]+=degc[b]; del members[b]; del degc[b]; improved=True
    return cof

bet = brandes(adj)
cof = communities(adj)
comm = defaultdict(list)
for n, c in cof.items(): comm[c].append(n)
ranked = sorted(comm.values(), key=lambda v: -len(v))
big = set(ranked[0]) if ranked else set()

def shelf(typ, status, kind, hub):
    t = typ.lower()
    if status == "ghost": return "Ghosts"
    if t in ("tension", "gradient"): return "Evaluative"
    if t == "decision": return "Decisions"
    if t == "shared resource": return "Shared resources"
    if t == "capability": return "Capabilities"
    if t == "actor": return "People & parties"
    return "Emergent"

# hero = most central ghost
ghosts = [(bet[n], n) for n, r in records.items() if r["status"] == "ghost"]
hero_bet, hero_id = max(ghosts) if ghosts else max((bet[n], n) for n in records)

nodes = []
for nid, r in records.items():
    r = dict(r)
    r["bet"] = round(bet.get(nid, 0.0), 1)
    r["cluster"] = 0 if nid in big else 1
    r["shelf"] = shelf(r["type"], r["status"], r["kind"], r.get("hub", ""))
    r["alert"] = (nid == hero_id)
    nodes.append(r)

edges = []
seen = set()
for a in adj:
    for b in adj[a]:
        k = tuple(sorted((a, b)))
        if k not in seen: seen.add(k); edges.append([k[0], k[1]])

real = [(bet[n], n) for n, r in records.items() if r["status"] != "ghost"]
top_bet, top_id = max(real) if real else (0.0, "")
DATA = dict(nodes=nodes, edges=edges,
            hero=dict(id=hero_id, label=hero_id, bet=round(hero_bet, 1)),
            topReal=dict(id=top_id, label=top_id, bet=round(top_bet, 1)),
            northStar=north_star)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
tpl = read(TEMPLATE)
html = tpl.replace("/*__DATA__*/", "const DATA = " + json.dumps(DATA, ensure_ascii=False) + ";")
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", os.path.abspath(OUT))
print("nodes", len(nodes), "edges", len(edges), "clusters", len(ranked))
print("hero:", hero_id, hero_bet)
print("top betweenness:")
for n, v in sorted(((r["bet"], r["id"]) for r in nodes), reverse=True)[:8]:
    print("  ", n, v)

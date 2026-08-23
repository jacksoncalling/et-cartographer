"""
Generate the OpenEvidence cartographer map -- business model lens.
Run from the ET-Cartographer root: python tools/build-openevidence-map.py
"""
import os

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "map-openevidence")
OBJ = os.path.join(ROOT, "objects")
os.makedirs(OBJ, exist_ok=True)

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ── CATALOG ──────────────────────────────────────────────────────────────────

write(os.path.join(ROOT, "Catalog.md"), """\
---
type: meta
role: front-door
---
# OpenEvidence -- Catalog

A cartographer's map of the OpenEvidence business model ecosystem, built from
public sources (announcements, Sacra research, press, academic preprints) as of
August 2026.

Territory: one AI company, its three-sided business model (clinicians / pharma /
health systems), its technical architecture, its capital structure, and the
strategic decisions that shaped it.

Core insight: doctors are the audience. Pharma is the payer. The free tool for
physicians is the distribution strategy, not the product. The product is
high-intent, NPI-verified prescriber attention sold to pharmaceutical companies
at CPMs 10-100x consumer platforms.

---

## Customer Segments
- [[Clinician Segment]] -- 760K NPI-verified US prescribers, free access
- [[Pharma Advertiser Segment]] -- the paying customer, primary revenue source
- [[Enterprise Health Systems]] -- institutional contracts, second revenue stream

## Value Propositions
- [[Clinician Value Proposition]] -- free, cited, HIPAA-safe evidence at point of care
- [[Pharma Value Proposition]] -- highest-intent physician ad inventory in existence
- [[Health System Value Proposition]] -- EHR-embedded workflow and documentation support

## Revenue Streams
- [[Pharma Advertising Revenue]] -- CPM $70-$1,000+, $150M ARR (2025), 90% gross margin
- [[Enterprise SaaS Revenue]] -- per-seat pricing, 5-10x ARPU vs ad model
- [[CME Credit Platform]] -- continuing education, launched April 2025
- [[Open Vista Suite]] -- pharma commercial layer, future stream (not yet live)

## Key Activities
- [[Corpus Curation]] -- 35M papers, licensed medical society content
- [[Model Training Pipeline]] -- RAG plus LoRA fine-tuning cycle
- [[Enterprise Sales and Integration]] -- EHR embedding, health system contracts
- [[Pharma Ad Sales]] -- direct sales to pharmaceutical companies

## Key Resources
- [[Medical Literature Corpus]] -- 35M papers with licensed society imprimatur
- [[NPI-Verified Prescriber Network]] -- the audience pharma pays to reach
- [[Medical Society Network]] -- content moat (NEJM, AMA, NCCN, ACC and 9 more)
- [[RAG and LoRA Architecture]] -- the technical method

## Key Partners
- [[Baseten]] -- inference infrastructure (billions of calls per week)
- [[Epic and Cerner]] -- EHR distribution channels
- [[Veeva Systems]] -- Open Vista pharma commercial co-development
- [[Tandem Health]] -- prior authorization workflow

## Channels
- [[NPI Self-Serve Onboarding]] -- instant, frictionless, NPI-gated
- [[EHR Embedding]] -- Epic and Cerner app marketplaces
- [[CME Credit Platform]] -- recurring engagement mechanism

## Customer Relationships
- [[Clinician Relationship]] -- free, self-serve, no churn pressure, CME sticky
- [[Pharma Relationship]] -- direct ad sales, precision targeting platform
- [[Health System Relationship]] -- enterprise contracts, IT integration

## Cost Structure
- [[Infrastructure and Inference Cost]] -- Baseten, billions of calls per week
- [[Content Licensing Cost]] -- medical society partnership fees
- [[Team and Operations]] -- ~120+ employees, 33% engineering, 18% sales

## Decisions
- [[Free Clinician Access Decision]] -- the go-to-market foundation
- [[Medical Society First-Mover Deals]] -- the content moat built before competitors
- [[EU-UK Withdrawal]] -- April 2026, regulatory exit
- [[Medical Superintelligence Framing]] -- Series D positioning ($12B valuation)

## Jurisdiction
- [[HIPAA]] -- US privacy compliance, required for clinical use
- [[EU AI Act and MDR]] -- the regulatory frame that triggered the EU exit

## Competitive Context
- [[Doximity]] -- the incumbent physician network, also monetizes pharma attention

## Ghosts
- [[European Clinician Access]] -- was real until April 2026, now absent
- [[Patient-Facing Interface]] -- named in vision, no product
- [[Organic Revenue Visibility]] -- $100M+ ARR confirmed, but source breakdown not public

## Tensions
- [[Audience-Customer Split]] -- doctors use it, pharma pays; misaligned incentives possible
- [[Accuracy Gap]] -- 100% USMLE vs less than 45% on complex subspecialty scenarios
- [[Regulatory Framing Conflict]] -- superintelligence narrative vs high-risk classification
- [[Investor-Customer Duality]] -- Mayo Clinic as both funder and deployment site

## Gradient
- [[Search to Agentic Automation]] -- the product direction of travel
""")

# ── NORTH STAR ────────────────────────────────────────────────────────────────

write(os.path.join(ROOT, "North Star.md"), """\
---
type: meta
role: orientation
---
# North Star

**The model in one sentence:** OpenEvidence gives doctors a free, best-in-class
clinical search tool; uses that to build a verified, NPI-confirmed audience of
760,000 US prescribers; then sells pharmaceutical companies the most precisely
targeted, highest-intent physician ad inventory that has ever existed -- at CPMs
10-100x consumer platforms -- generating $150M ARR at 90% gross margins with a
team of roughly 120 people.

**The historical analogue:** Epocrates (free drug reference tool for physicians,
pharma pays for access) -- but rebuilt with AI, at 40x the scale, with 90% gross
margins. Epocrates sold to athenahealth for $293M in 2013. OpenEvidence is valued
at $12B.

**The structural hub:** [[NPI-Verified Prescriber Network]] is the node everything
else radiates from. It is simultaneously what pharma pays for, what clinicians are
part of, and what makes the [[Pharma Advertising Revenue]] defensible. Lose it
(regulatory pressure, competitor offering), and the revenue model unravels.

**The load-bearing tension:** [[Audience-Customer Split]]. Pharma is the payer.
Doctors are the audience. Those two groups have partially conflicting interests --
pharma wants brand messages at prescribing moments; doctors want unbiased evidence.
OpenEvidence's structural answer is corpus quality and citation grounding (if the
evidence says brand X, that is editorial, not advertising). Whether that answer
holds at scale, under [[Accuracy Gap]] conditions, as the agentic layer grows, is
the live question.

**The most central ghost:** [[Organic Revenue Visibility]]. Revenue is confirmed
($100M+ by Nadler, $150M by Sacra) but the split between pharma advertising,
enterprise SaaS, and CME is not public. Understanding which stream is growing
fastest shapes whether [[Open Vista Suite]] is an acceleration or a pivot.

**What this map cannot yet answer:**
- Exact revenue split across three streams.
- Whether pharma advertising CPMs hold as the prescriber base scales.
- Whether the agentification gradient ([[Search to Agentic Automation]]) changes
  the [[Audience-Customer Split]] tension materially.

Sources: Sacra research, Fierce Healthcare, CNBC, BusinessWire, medRxiv (Nov 2025),
The Lancet Regional Health (2026), Baseten case study, Forbes, Getlatka.
""")

# ── CUSTOMER SEGMENTS ─────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Clinician Segment.md"), """\
---
type: Actor
subtype: user segment (non-paying)
status: live
hub: audience
---
# Clinician Segment

760,000 NPI-verified US prescribers using OpenEvidence, plus residents, nurses,
and other healthcare professionals. 40%+ of all US physicians use it daily.
65,000 new clinician registrations per month. Free access, no subscription,
NPI verification at signup. The clinician segment is not the revenue source --
it is the audience that creates the [[Pharma Advertising Revenue]]. Primary
specialties: primary care, internal medicine, emergency medicine, family medicine,
psychiatry (highest query volumes). Usage: clinical questions at point of care,
drug interactions, rare disease lookup, protocol checking, and increasingly
visit documentation via [[Clinical Documentation Capability]].

Served-by [[Clinician Value Proposition]] · onboarded-via [[NPI Self-Serve Onboarding]] ·
maintained-via [[CME Credit Platform]] and [[EHR Embedding]] ·
part-of [[NPI-Verified Prescriber Network]] ·
governed-by [[HIPAA]] · valued-by [[Pharma Advertiser Segment]]

- Hits: clinical decision quality, time-to-answer, documentation burden.
- Does not hit: OpenEvidence's revenue directly; the value flows through the
  [[Pharma Advertiser Segment]] relationship.
""")

write(os.path.join(OBJ, "Pharma Advertiser Segment.md"), """\
---
type: Actor
subtype: customer segment (paying)
status: live
hub: revenue
---
# Pharma Advertiser Segment

Pharmaceutical and medical device companies that pay to reach the [[Clinician
Segment]] through OpenEvidence's advertising platform. The primary revenue
customer. US digital pharma ad spending runs $20-25 billion annually;
OpenEvidence captures a slice at CPMs of $70-$1,000+ (vs $5-15 on consumer
platforms) because the inventory is unique: verified physician identity (NPI),
at the exact moment of clinical decision-making that may inform a prescribing
choice. No consumer platform can offer this. The audience is not scrolling a
feed -- they are actively researching a treatment option.

Pays-for [[Pharma Advertising Revenue]] · reaches [[Clinician Segment]] via
[[Pharma Value Proposition]] · part-of [[Pharma Ad Sales]] commercial relationship ·
future-served-by [[Open Vista Suite]]

- Hits: drug brand awareness, prescribing behavior at point of clinical research.
- Does not hit: patient outcomes directly; the pharma message reaches the clinician,
  not the patient.
""")

write(os.path.join(OBJ, "Enterprise Health Systems.md"), """\
---
type: Actor
subtype: customer segment (paying, institutional)
status: live
---
# Enterprise Health Systems

Hospitals and health systems that deploy OpenEvidence enterprise-wide via
[[EHR Embedding]] and pay per-seat contracts through [[Enterprise SaaS Revenue]].
Key deployments: Mount Sinai (7 hospitals, March 2026), Sutter Health (February
2026), Cedars-Sinai (May 2026 -- most advanced: live patient EHR data piped
into evidence queries). Mayo Clinic is both a deployment target and an investor
in [[VC Investor Coalition]] -- creating the [[Investor-Customer Duality]] tension.
Revenue per seat is estimated at 5-10x the per-user ARPU from the ad-supported
individual model.

Pays-for [[Enterprise SaaS Revenue]] · served-by [[Health System Value Proposition]] ·
integrates-via [[EHR Embedding]] · using [[FHIR Standard]] ·
held by [[Investor-Customer Duality]] in Mayo's case

- Hits: clinical workflow efficiency, documentation burden, evidence access at scale.
- Does not hit: the pharma advertising layer; enterprise contracts are a separate
  commercial relationship from the [[Pharma Advertiser Segment]] revenue.
""")

# ── VALUE PROPOSITIONS ────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Clinician Value Proposition.md"), """\
---
type: Capability
subtype: value proposition
status: live
---
# Clinician Value Proposition

What OpenEvidence offers the clinician: free, instant, cited answers to clinical
questions grounded in 35 million peer-reviewed papers ([[Medical Literature Corpus]]),
HIPAA-compliant, with no subscription required. The value stack has deepened over
time: point-of-care evidence (the original), then CME credit (physician has to earn
it anyway, now earnable passively through use), then visit documentation
([[Clinical Documentation Capability]]), then EHR-embedded workflow ([[EHR Embedding]]).
Each layer increases the switching cost without increasing the price. The
competition is UpToDate (expensive subscription), Doximity GPT (convenient but
shallower corpus), and general LLMs (no clinical grounding, no citations, not
HIPAA-safe). OpenEvidence's answer to each: free, deeper, and compliant.

Delivered-to [[Clinician Segment]] · anchored-by [[Medical Literature Corpus]] ·
differentiated-by [[Medical Society Network]] partnerships ·
deepened-by [[CME Credit Platform]] and [[Clinical Documentation Capability]]

- Hits: adoption speed, retention, NPI-verified audience size.
- Does not hit: revenue directly -- the clinician pays nothing.
""")

write(os.path.join(OBJ, "Pharma Value Proposition.md"), """\
---
type: Capability
subtype: value proposition
status: live
---
# Pharma Value Proposition

What OpenEvidence sells to pharmaceutical companies: access to 760,000 NPI-verified
US prescribers at the precise moment they are researching a clinical question that
may directly inform a prescribing decision. CPMs of $70-$1,000+ (vs $5-15 on
consumer social platforms) because the signal quality is incomparably higher --
verified identity, verified profession, verified intent. No consumer platform
offers NPI-level verification. No professional network offers the clinical intent
signal (a physician is not just browsing; they are making or preparing a clinical
decision). The combination is unique. The structural parallel is paid search
advertising: you pay more because the user is at the bottom of the funnel. Here,
the funnel is a prescribing decision.

Delivered-to [[Pharma Advertiser Segment]] · enabled-by [[NPI-Verified Prescriber Network]] ·
sold-via [[Pharma Ad Sales]] · generates [[Pharma Advertising Revenue]]

- Hits: drug brand exposure at maximum prescribing intent.
- Does not hit: patient awareness -- this is HCP-targeted, not DTC.
""")

write(os.path.join(OBJ, "Health System Value Proposition.md"), """\
---
type: Capability
subtype: value proposition
status: live
---
# Health System Value Proposition

What OpenEvidence offers enterprise health systems: clinical decision support
embedded inside existing EHR workflows (Epic, Cerner), reducing documentation
burden through [[Clinical Documentation Capability]], and providing population-level
insight into how their clinicians research clinical decisions. The most advanced
deployment (Cedars-Sinai) passes live patient EHR context (comorbidities,
medications, allergies) into the evidence query, personalizing the answer to
the individual patient at point of care. For the health system, this is
operationalized evidence-based medicine -- not a tool clinicians use separately,
but a capability embedded where clinical decisions already happen.

Delivered-to [[Enterprise Health Systems]] · enabled-by [[EHR Embedding]] ·
deepened-by [[Clinical Documentation Capability]] · priced-via [[Enterprise SaaS Revenue]]

- Hits: workflow stickiness, documentation compliance, clinical quality metrics.
- Does not hit: the pharma revenue stream -- enterprise contracts are clean of
  pharma advertising in the EHR-embedded context.
""")

# ── REVENUE STREAMS ───────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Pharma Advertising Revenue.md"), """\
---
type: Capability
subtype: revenue stream
status: live
hub: primary revenue
---
# Pharma Advertising Revenue

The core current revenue engine. Pharmaceutical companies pay to display targeted
messages to the [[NPI-Verified Prescriber Network]] via the [[Pharma Value
Proposition]]. CPMs range from $70 to $1,000+ depending on specialty, drug
category, and targeting precision (vs $5-15 on consumer social platforms).
Estimated ARPU: $124 per active prescriber. Sacra estimates $150M ARR in 2025,
up 1,803% from $7.9M in 2024. Daniel Nadler confirmed $100M+ to CNBC. Gross
margins: ~90%. The ad is served during the brief moment the AI generates an
answer -- a loading-screen model that converts wait time into impression time.
At 20 million clinical consultations per month (January 2026), the impression
inventory is substantial and growing.

Generated-by [[Pharma Advertiser Segment]] via [[Pharma Value Proposition]] ·
sold-through [[Pharma Ad Sales]] · enabled-by [[NPI-Verified Prescriber Network]] ·
in-tension-with [[Audience-Customer Split]]

- Hits: OpenEvidence P&L directly; 90% gross margin makes this extremely capital-
  efficient at scale.
- Does not hit: clinician experience directly (ads are served during generation,
  not inside the clinical answer).
""")

write(os.path.join(OBJ, "Enterprise SaaS Revenue.md"), """\
---
type: Capability
subtype: revenue stream
status: live
---
# Enterprise SaaS Revenue

Per-seat enterprise pricing for health systems that deploy OpenEvidence
organisation-wide. Estimated at 5-10x ARPU versus the ad-supported individual
model. Deployments confirmed: Mount Sinai (7 hospitals), Sutter Health, Cedars-Sinai.
Enterprise contracts include IT integration ([[EHR Embedding]]), support, and
potentially custom protocol overlays (Cedars-Sinai model). Exact pricing is not
publicly disclosed. The enterprise model creates switching costs (EHR integration,
workflow dependencies) that the free individual model does not.

Generated-by [[Enterprise Health Systems]] · sold-via [[Enterprise Sales and Integration]] ·
enabled-by [[EHR Embedding]] · complements [[Pharma Advertising Revenue]]

- Hits: revenue stability, contract predictability, switching cost moat.
- Does not hit: the 40%+ of individual physicians who use the free product outside
  an enterprise contract; those users generate [[Pharma Advertising Revenue]].
""")

write(os.path.join(OBJ, "CME Credit Platform.md"), """\
---
type: Capability
subtype: revenue stream / retention mechanism
status: live
---
# CME Credit Platform

Launched April 2025. Physicians, nurse practitioners, and physician associates
in the US are required to earn continuing medical education (CME) credits to
maintain licensure -- typically 25-50 hours per year. OpenEvidence offers free
CME credit for NPI-verified healthcare professionals, earned through platform use.
Dual strategic function: (1) a retention mechanism -- physicians return to earn
required credits, increasing session frequency and therefore ad inventory;
(2) a revenue stream -- CME modules can be sponsored by pharmaceutical companies,
or physicians can pay for certified CME tracks. The model mirrors the pharma
advertising logic: physician has to do something (earn CME) anyway; OpenEvidence
makes it happen through their platform; pharma pays for the attendance.

Retains [[Clinician Segment]] · increases inventory for [[Pharma Advertising Revenue]] ·
potentially-sponsored-by [[Pharma Advertiser Segment]] ·
accessed-via [[NPI Self-Serve Onboarding]]

- Hits: session frequency, physician stickiness, time-on-platform.
- Does not hit: new user acquisition; CME is a retention tool, not an acquisition tool.
""")

write(os.path.join(OBJ, "Open Vista Suite.md"), """\
---
type: Capability
subtype: revenue stream (future)
status: pending
---
# Open Vista Suite

The future commercial product line, co-developed with [[Veeva Systems]]: a pharma-
facing suite connecting physicians to clinical trials, supporting drug discovery,
and improving therapy adoption. Expected to launch in 2026; no reported revenue
as of April 2026. This is the third leg of the revenue model -- moving beyond
advertising (pharma pays to be seen at prescribing moment) and enterprise SaaS
(health systems pay for workflow integration) into pharma commercial intelligence
(pharma pays to understand and influence the prescribing pipeline). If it lands,
it converts OpenEvidence from an ad platform into a pharma commercial data layer --
a meaningfully higher valuation multiple.

Co-developed-with [[Veeva Systems]] · expands [[Pharma Advertiser Segment]] relationship ·
deeper than [[Pharma Advertising Revenue]] (data and workflow, not just impressions) ·
expected-to-resolve [[Organic Revenue Visibility]] ghost partially

- Hits: OpenEvidence's path from ad platform to pharma intelligence platform.
- Does not hit: anything a clinician experiences; this is a pharma-facing product.
""")

# ── KEY ACTIVITIES ────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Corpus Curation.md"), """\
---
type: Capability
subtype: key activity
status: live
---
# Corpus Curation

Maintaining, licensing, and continuously updating the [[Medical Literature Corpus]]
(35 million peer-reviewed papers). This is the activity that produces the
defensible moat: content from the [[Medical Society Network]] carries institutional
credibility that generic scraped corpora do not. Key sub-activities: negotiating
and renewing society content licenses (NEJM, AMA, and 10+ specialty bodies),
ingesting new publications, maintaining citation metadata, and ensuring every
answer is grounded (traceable to a timestamped source). The corpus is also the
input to the [[Model Training Pipeline]] -- better curated sources produce better
synthetic training data.

Produces [[Medical Literature Corpus]] · anchors [[Medical Society Network]] deals ·
feeds [[Model Training Pipeline]] · grounds [[Clinician Value Proposition]]

- Hits: answer quality, citation reliability, regulatory defensibility.
- Does not hit: the advertising platform or enterprise sales.
""")

write(os.path.join(OBJ, "Model Training Pipeline.md"), """\
---
type: Capability
subtype: key activity
status: live
---
# Model Training Pipeline

The continuously improving AI training cycle: RAG retrieves relevant passages
from [[Medical Literature Corpus]]; LoRA adapters fine-tune specialist models
on medical subdomains; improved models generate higher-quality synthetic training
data for the next cycle. The flywheel means OpenEvidence's models improve
automatically as clinical query volume grows -- each of the 20 million monthly
consultations provides signal for the next fine-tuning round. Infrastructure
provided by [[Baseten]] (Multi-cloud Capacity Management, Baseten Embeddings
Inference, Baseten Training). The technical method is [[RAG and LoRA Architecture]].

Produces and improves [[RAG and LoRA Architecture]] · runs-on [[Baseten]] ·
trains-from [[Medical Literature Corpus]] · validated-by [[USMLE Benchmark]]

- Hits: model accuracy, hallucination rate, subspecialty coverage.
- Does not hit: the commercial relationships -- this is engineering, not sales.
""")

write(os.path.join(OBJ, "Enterprise Sales and Integration.md"), """\
---
type: Capability
subtype: key activity
status: live
---
# Enterprise Sales and Integration

The commercial and technical activity of winning and deploying enterprise health
system contracts. Sales team approaches hospital systems; technical team
implements [[EHR Embedding]] via FHIR APIs into Epic or Cerner; ongoing support
maintains the integration. The Cedars-Sinai deployment is the most technically
advanced: live patient EHR data (comorbidities, medications, allergies) is piped
into literature queries in real time. Each enterprise deployment increases lock-in
(workflow dependency), generates [[Enterprise SaaS Revenue]], and adds another
beacon of credibility for the next enterprise prospect.

Wins [[Enterprise Health Systems]] · deploys [[EHR Embedding]] · generates
[[Enterprise SaaS Revenue]] · uses sales and marketing team (17.5% of headcount,
fastest-growing function)

- Hits: enterprise revenue, switching costs, health system reference customer list.
- Does not hit: individual clinician adoption, which is self-serve and free.
""")

write(os.path.join(OBJ, "Pharma Ad Sales.md"), """\
---
type: Capability
subtype: key activity
status: live
---
# Pharma Ad Sales

Direct sales to pharmaceutical and medical device companies for access to the
[[NPI-Verified Prescriber Network]] via the [[Pharma Value Proposition]].
This is not a self-serve ad platform; pharma advertising in the US is sold
through direct relationships (compliance requirements, medical-legal review,
targeting specifications). OpenEvidence competes for pharma digital marketing
budgets against Doximity (the incumbent), specialty journals, and medical
conference sponsorships. Its differentiation is the combination of NPI
verification and clinical intent signal -- the prescriber is not browsing,
they are actively researching the clinical decision. CPMs reflect this.

Sells [[Pharma Advertising Revenue]] · reaches [[Pharma Advertiser Segment]] ·
competes-with [[Doximity]] for pharma budget ·
enabled-by [[NPI-Verified Prescriber Network]]

- Hits: primary revenue; at $150M ARR, this is the business.
- Does not hit: the clinical product; ad sales and product are intentionally
  separated to protect editorial integrity.
""")

write(os.path.join(OBJ, "Clinical Documentation Capability.md"), """\
---
type: Capability
subtype: key activity / product
status: live
---
# Clinical Documentation Capability

The Visits product (launched August 2025): automatically generates medical notes
from patient conversations. Prior Authorization Agent (in rollout, via [[Tandem
Health]] partnership): drafts prior authorization letters with supporting evidence.
These two products extend OpenEvidence into the administrative and documentation
layers of clinical work -- the parts physicians most resent. Strategic logic: if
OpenEvidence saves 15-30 minutes of documentation per physician per shift, it
becomes load-bearing in the workflow in a way a search engine is not. This is
the bridge from the [[Search to Agentic Automation]] gradient toward the
[[Open Vista Suite]] commercial layer.

Extends [[Clinician Value Proposition]] · built-on [[Medical Literature Corpus]] ·
increases [[EHR Embedding]] stickiness · part-of [[Search to Agentic Automation]] ·
prior auth developed-with [[Tandem Health]]

- Hits: clinician workflow stickiness, session time, enterprise contract value.
- Does not hit: the pharma advertising layer directly.
""")

# ── KEY RESOURCES ─────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "NPI-Verified Prescriber Network.md"), """\
---
type: Shared Resource
subtype: key resource
status: live
hub: audience asset
---
# NPI-Verified Prescriber Network

760,000 NPI-verified US prescribers actively using the platform monthly.
The single most valuable asset in the business -- simultaneously the product
(what clinicians use), the audience (what pharma pays for), and the moat
(competitors cannot replicate without building the same clinician trust from
scratch). NPI verification is instant and government-backed (CMS database),
removing the fraud risk that plagues unverified professional platforms.
At 20 million clinical consultations per month, this is also one of the
largest real-world datasets of physician clinical reasoning outside of EHR data.

Held-by [[OpenEvidence]] · built-through [[Free Clinician Access Decision]] ·
onboarded-via [[NPI Self-Serve Onboarding]] · monetized-by [[Pharma Ad Sales]] ·
retained-by [[CME Credit Platform]] and [[EHR Embedding]] ·
valued-by [[Pharma Advertiser Segment]]

- Hits: everything -- the revenue, the moat, the valuation.
- Does not hit: patients, who are not part of this network.
""")

write(os.path.join(OBJ, "Medical Literature Corpus.md"), """\
---
type: Shared Resource
subtype: key resource
status: live
---
# Medical Literature Corpus

35 million peer-reviewed medical publications, continuously updated. Licensed
content from the [[Medical Society Network]] (NEJM, AMA, NCCN, ACC and 9 more)
gives the corpus institutional credibility that general LLM training corpora
lack. Every answer is grounded -- traceable to a timestamped, citable source.
This is the primary trust driver for the [[Clinician Segment]]: clinicians
cite sources to colleagues; they need the citation, not just the answer.
The corpus is also the training substrate for the [[Model Training Pipeline]]
and improves continuously as clinical query volume scales.

Maintained-by [[Corpus Curation]] · licensed-from [[Medical Society Network]] ·
powers [[RAG and LoRA Architecture]] · anchors [[Clinician Value Proposition]] ·
trained-on-by [[Model Training Pipeline]]

- Hits: answer quality, clinical trust, competitive moat depth.
- Does not hit: the pharma advertising or enterprise commercial relationships.
""")

write(os.path.join(OBJ, "Medical Society Network.md"), """\
---
type: Actor
subtype: key partner / content source
status: live
---
# Medical Society Network

The coalition of medical publishers and specialty societies that signed official
AI content partnerships with OpenEvidence, granting licensed access to their
guidelines, journals, and clinical standards. First-mover deals: NEJM and AMA
(the first official AI partnerships these bodies had granted). Full list: NCCN,
ACC, ADA, AAFP, NORD, ACOG, AUA, AAO, ACEP, AAP. The moat is not the content
itself (much of it is publicly available) but the official licensing relationship:
OpenEvidence answers carry the imprimatur of the society whose guideline is cited.
Competitor LLMs cannot claim this without renegotiating each partnership. The moat
builds over time: each society partnership increases the corpus quality, which
increases clinician trust, which increases the prescriber audience, which increases
the value of [[Pharma Advertising Revenue]].

Partners-with [[OpenEvidence]] · licenses-to [[Medical Literature Corpus]] ·
anchors-trust-of [[Clinician Segment]] · all US-based; no European equivalent built

- Hits: corpus quality, clinical credibility, regulatory defensibility.
- Does not hit: the European market -- no EU medical body partnerships were built,
  which contributed to [[EU-UK Withdrawal]] being structurally low-cost.
""")

write(os.path.join(OBJ, "RAG and LoRA Architecture.md"), """\
---
type: Shared Resource
subtype: key resource / technical method
status: live
---
# RAG and LoRA Architecture

The technical stack: Retrieval-Augmented Generation retrieves relevant passages
from [[Medical Literature Corpus]] at query time; a reranker layer prioritizes
clinical relevance; LoRA (Low-Rank Adaptation) fine-tunes specialist models on
medical subdomains without full retraining; improved models generate synthetic
training data for the next LoRA cycle. The flywheel produces continuously
improving accuracy without linear compute cost growth. Served at scale by
[[Baseten]]. The same architecture underpins [[Clinical Search Engine]], will
underpin [[Specialist Agent Network]], and provides the foundation for
[[Clinical Documentation Capability]].

Powers [[Clinical Search Engine]] · trained-by [[Model Training Pipeline]] ·
served-by [[Baseten]] · validated-by [[USMLE Benchmark]]

- Hits: answer accuracy, grounding quality, hallucination reduction.
- Does not hit: the business model layer -- architecture is neutral to revenue model.
""")

# ── KEY PARTNERS ─────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Baseten.md"), """\
---
type: Actor
subtype: key partner / infrastructure
status: live
---
# Baseten

Inference infrastructure provider. Runs billions of custom fine-tuned LLM calls
per week for OpenEvidence. Provides Multi-cloud Capacity Management (MCM),
Baseten Embeddings Inference (BEI), and Baseten Training. At 20 million clinical
consultations per month, inference is a substantial cost line and a latency-critical
operation (slow answers hurt the user experience and reduce ad impression time).
Baseten's role is not just cost management but speed -- a physician waiting 30
seconds for a clinical answer is a worse product than one waiting 3 seconds.

Serves [[OpenEvidence]] · runs [[RAG and LoRA Architecture]] ·
contributes-to [[Infrastructure and Inference Cost]]

- Hits: latency, throughput, [[Infrastructure and Inference Cost]].
- Does not hit: content quality or the commercial relationships.
""")

write(os.path.join(OBJ, "Epic and Cerner.md"), """\
---
type: Actor
subtype: key partner / distribution channel
status: live
---
# Epic and Cerner

The two dominant EHR platforms in the US. OpenEvidence's enterprise strategy
depends on integration into both. Epic integration: Sutter Health (February 2026),
Mount Sinai (March 2026). Cerner integration: also confirmed. Integration uses
HL7 [[FHIR Standard]] APIs. Epic and Cerner function as distribution channels:
a health system that has already bought Epic is not going to replace it; the
question is which AI tools get embedded in it. Being in the Epic App Orchard
or Cerner Marketplace puts OpenEvidence in front of the purchasing committee
alongside clinical workflow. This is the enterprise equivalent of the [[NPI
Self-Serve Onboarding]] channel for individuals.

Partner-of [[OpenEvidence]] · enables [[EHR Embedding]] ·
channel-to [[Enterprise Health Systems]] · uses [[FHIR Standard]]

- Hits: enterprise market access, switching cost creation, workflow stickiness.
- Does not hit: the individual clinician channel, which is NPI self-serve.
""")

write(os.path.join(OBJ, "Veeva Systems.md"), """\
---
type: Actor
subtype: key partner / Open Vista
status: live
---
# Veeva Systems

Enterprise pharma and life sciences SaaS company -- the dominant CRM and
commercial operations platform for pharmaceutical companies. Co-developing
[[Open Vista Suite]] with OpenEvidence: a product line connecting physicians
to clinical trials, supporting drug discovery, improving therapy adoption.
The strategic logic: Veeva already owns the pharma commercial relationship;
OpenEvidence owns the physician relationship. Together they can build a
data layer that connects prescribing intent to pharma commercial workflows.
First products expected 2026; no reported revenue yet.

Partners-with [[OpenEvidence]] · co-develops [[Open Vista Suite]] ·
bridges [[Pharma Advertiser Segment]] into commercial intelligence layer

- Hits: OpenEvidence's path from ad platform to pharma data platform.
- Does not hit: the core clinical search product or clinician relationships.
""")

write(os.path.join(OBJ, "Tandem Health.md"), """\
---
type: Actor
subtype: key partner
status: live
---
# Tandem Health

Clinical AI workflow company. US partnership with OpenEvidence announced April 2,
2026 (26 days before the EU exit): adds prescription generation and prior
authorization submission to OpenEvidence's platform. A prior authorization letter
supported by cited clinical evidence -- generated automatically -- is a clear
value add for clinicians and health systems. Tandem also emerged post-withdrawal
as a recommended European alternative for clinicians who lost OpenEvidence access.
The dual position (US workflow partner and EU replacement) is structurally unusual.

Partners-with [[OpenEvidence]] on [[Clinical Documentation Capability]] ·
enables [[Prior Authorization Agent]] feature ·
also positioned-as European alternative to [[European Clinician Access]] (ghost)

- Hits: prior authorization workflow, clinical documentation completeness.
- Does not hit: the core evidence retrieval or the pharma advertising layer.
""")

# ── CHANNELS ─────────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "NPI Self-Serve Onboarding.md"), """\
---
type: Instrument
subtype: channel
status: live
---
# NPI Self-Serve Onboarding

The individual clinician onboarding process: enter NPI number, verified instantly
against the CMS database, access granted. No sales call, no institutional
approval, no subscription fee. This is the primary acquisition channel for the
760,000-person [[Clinician Segment]]. The frictionlessness is deliberate: every
additional step in onboarding costs adoption, and at 65,000 new registrations
per month, the funnel is working. NPI verification simultaneously creates the
audience quality that [[Pharma Advertiser Segment]] pays a premium for -- you
cannot enter without proving you are a licensed US healthcare provider.

Onboards [[Clinician Segment]] · builds [[NPI-Verified Prescriber Network]] ·
enables [[Pharma Advertising Revenue]] · governed-by [[HIPAA]]

- Hits: individual physician adoption speed.
- Does not hit: enterprise market -- [[Enterprise Sales and Integration]] handles that.
""")

write(os.path.join(OBJ, "EHR Embedding.md"), """\
---
type: Instrument
subtype: channel / integration
status: live
---
# EHR Embedding

The enterprise distribution channel: OpenEvidence embedded inside Epic and Cerner
workflows via HL7 [[FHIR Standard]] APIs. Clinicians access evidence without
leaving the EHR. The Cedars-Sinai deployment is the furthest advanced: live
patient data (comorbidities, medications, allergies) passes into the evidence
query automatically. EHR embedding is simultaneously a channel (how enterprise
users access the product) and a moat (switching costs once workflows depend on it).

Channel-to [[Enterprise Health Systems]] · enabled-by [[Epic and Cerner]] ·
uses [[FHIR Standard]] · generates [[Enterprise SaaS Revenue]] ·
deepens [[Health System Value Proposition]]

- Hits: enterprise stickiness, clinical workflow integration depth.
- Does not hit: individual clinicians outside enterprise contracts, who use the
  web or mobile product.
""")

# ── COST STRUCTURE ────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Infrastructure and Inference Cost.md"), """\
---
type: Capability
subtype: cost structure
status: live
---
# Infrastructure and Inference Cost

The primary operational cost: serving billions of custom fine-tuned LLM calls
per week at the latency required for clinical use (seconds, not minutes).
Managed through [[Baseten]] infrastructure. At 20 million monthly consultations,
the inference cost is substantial but offset by 90% gross margins on the
[[Pharma Advertising Revenue]] -- meaning the per-query inference cost is well
below the per-query ad revenue at current CPM levels. The cost model scales with
query volume; the revenue model also scales with query volume; at current margin
levels, growth is self-funding for this cost line.

Borne-by [[OpenEvidence]] · run-on [[Baseten]] ·
offset-by [[Pharma Advertising Revenue]] gross margin

- Hits: unit economics as query volume grows; matters most if CPMs compress.
- Does not hit: content licensing or team costs.
""")

write(os.path.join(OBJ, "Content Licensing Cost.md"), """\
---
type: Capability
subtype: cost structure
status: live
---
# Content Licensing Cost

The annual cost of maintaining licensed access to [[Medical Society Network]]
content (NEJM, AMA, NCCN, ACC and 9+ others). Terms are not public. These are
ongoing relationship costs -- not one-time payments -- and represent the price
of the content moat. If any major society partnership terminates, the corpus
loses its institutional imprimatur in that specialty. The licensing cost is
the structural reason competitors cannot simply replicate the corpus: the
relationship and the fee must both be renewed.

Borne-by [[OpenEvidence]] · maintains [[Medical Society Network]] partnerships ·
protects [[Medical Literature Corpus]] quality

- Hits: corpus credibility, competitive moat maintenance.
- Does not hit: inference costs or team operations.
""")

write(os.path.join(OBJ, "Team and Operations.md"), """\
---
type: Actor
subtype: cost structure / key resource
status: live
---
# Team and Operations

Approximately 120+ employees (conflicting public data: 83 when hitting $50M ARR
in 2025; reported at various points as 119-558, likely reflecting different
counting methodologies and contractor inclusion). Functional breakdown: Finance
and Operations (49%), Engineering (33.5%), Sales and Marketing (17.5%). Sales
and Marketing is the fastest-growing function (+8.7%), signaling the push into
enterprise and pharma direct sales. The capital efficiency is notable: $50M ARR
on an 83-person team is approximately $600K revenue per employee -- strong for
a healthcare software business.

Employed-by [[OpenEvidence]] · generates [[Enterprise Sales and Integration]] and
[[Pharma Ad Sales]] capabilities · builds [[Model Training Pipeline]] and [[Corpus Curation]]

- Hits: operational capability, sales reach, product velocity.
- Does not hit: the content or infrastructure layers, which are outsourced to
  partners.
""")

# ── DECISIONS ────────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Free Clinician Access Decision.md"), """\
---
type: Decision
status: live
---
# Free Clinician Access Decision

The foundational go-to-market choice: individual access is free for any NPI-
verified US healthcare professional. No subscription. No paywall. The decision
was counter-intuitive in a market where clinical reference tools (UpToDate,
DynaMed) are expensive subscriptions. The logic: maximize prescriber audience
size, which maximizes [[Pharma Advertising Revenue]] CPM value, which funds the
product for free. It also made the [[EU-UK Withdrawal]] structurally cheap:
no paying individual European subscribers existed to be lost.

Made-by [[OpenEvidence]] · builds [[NPI-Verified Prescriber Network]] ·
enables [[Pharma Advertising Revenue]] model ·
defers monetization burden to [[Open Vista Suite]] and enterprise

- Hits: adoption velocity, audience scale, competitive moat speed.
- Does not hit: short-term revenue; the model requires pharma or enterprise to close.
""")

write(os.path.join(OBJ, "Medical Society First-Mover Deals.md"), """\
---
type: Decision
status: live
---
# Medical Society First-Mover Deals

The strategic choice to approach medical societies before competitors and before
the market understood the value of official AI content partnerships. OpenEvidence
struck the first official AI content deals with NEJM and AMA -- neither had
granted these before. By the time competitors recognized the value, 12+ societies
had signed. This decision built the content moat that anchors [[Clinician Value
Proposition]] and differentiates [[Medical Literature Corpus]] from scraped general
corpora. The moat compounds: each new society partnership increases corpus quality,
which increases clinician trust, which increases prescriber audience size, which
increases pharma CPMs.

Made-by [[OpenEvidence]] (founders) · built [[Medical Society Network]] ·
anchors [[Medical Literature Corpus]] · compounds over time

- Hits: competitive defensibility; each new competitor must re-negotiate every deal.
- Does not hit: the European content layer -- no equivalent EU society deals were pursued.
""")

write(os.path.join(OBJ, "EU-UK Withdrawal.md"), """\
---
type: Decision
status: live
---
# EU-UK Withdrawal

On April 28, 2026, OpenEvidence terminated access for EU and UK users citing
regulatory uncertainty under the [[EU AI Act and MDR]]. The [[Free Clinician
Access Decision]] made this structurally cheap: no paid European subscribers
existed to be lost. The real cost was to European clinicians who lost the tool
and to the company's stated global ambition. The decision reflects an
opportunity-cost calculation: EU compliance (conformity assessments, algorithmic
audits, dual MDR plus AI Act burden, uncertain timelines) against a US growth
trajectory at 1,803% annual revenue growth. Compliance effort would not have
generated proportionate revenue in the near term. The Lancet published a direct
response. European alternatives (Tandem Health, Vera Health) emerged within weeks.

Made-by [[OpenEvidence]] · triggered-by [[EU AI Act and MDR]] ·
structurally-enabled-by [[Free Clinician Access Decision]] ·
created [[European Clinician Access]] ghost

- Hits: European clinicians; no revenue impact disclosed.
- Does not hit: US operations or growth trajectory.
""")

write(os.path.join(OBJ, "Medical Superintelligence Framing.md"), """\
---
type: Decision
status: live
---
# Medical Superintelligence Framing

The narrative chosen for the $250M Series D (January 2026): OpenEvidence is
building "medical superintelligence" -- subspecialty AI agents that consult each
other on complex patient cases. Doubled the valuation from $6B to $12B in three
months. The framing is both a product vision ([[Specialist Agent Network]]) and
a capital story that sits in tension with two live findings: the [[Accuracy Gap]]
(less than 45% on complex subspecialty scenarios) and the EU's classification
of the same product category as high-risk AI requiring human oversight. The
company navigated the EU tension by exiting the jurisdiction ([[EU-UK Withdrawal]]);
the accuracy tension is addressed by ongoing model improvement.

Made-by [[OpenEvidence]] and [[VC Investor Coalition]] ·
names [[Specialist Agent Network]] as destination ·
creates [[Regulatory Framing Conflict]] tension ·
in-tension-with [[Accuracy Gap]]

- Hits: valuation, investor confidence, talent recruitment.
- Does not hit: clinical reality today -- the current product is a search engine
  and documentation tool, not an autonomous agent network.
""")

# ── JURISDICTIONS ─────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "HIPAA.md"), """\
---
type: Jurisdiction
status: live
---
# HIPAA

The US federal framework governing protected health information (PHI). HIPAA
compliance is required for any clinical tool that handles patient data -- which
[[EHR Embedding]] does. It is also a trust signal for [[Clinician Segment]]:
physicians will not enter patient context into a non-HIPAA-compliant tool.
HIPAA compliance enables both the core product (patient context in queries)
and the enterprise channel (health systems require it for vendor qualification).
It is table stakes for the US market; it has no standing in EU law.

Governs [[OpenEvidence]] · enables [[Clinician Segment]] trust ·
required-by [[Enterprise Health Systems]] vendor qualification ·
does-not-cover [[EU AI Act and MDR]] territory

- Hits: US market access, enterprise contract eligibility.
- Does not hit: European regulatory status.
""")

write(os.path.join(OBJ, "EU AI Act and MDR.md"), """\
---
type: Jurisdiction
status: live
---
# EU AI Act and MDR

The European regulatory double-frame: the EU Artificial Intelligence Act
classifies clinical decision support AI as high-risk, requiring conformity
assessments, technical documentation, algorithmic transparency, bias evaluations,
and human oversight obligations. The Medical Device Regulation (MDR) adds a
parallel layer for AI functioning as a medical device. Core obligations for
high-risk AI came into full effect August 2026. The two frameworks are not
fully harmonized, creating a dual compliance burden with uncertain sequencing.
The Lancet (2026) argued the framework lacks the dynamic risk-benefit analysis
clinical AI actually requires. Directly triggered [[EU-UK Withdrawal]].

Governs AI in EU and UK markets · triggered [[EU-UK Withdrawal]] ·
in-tension-with [[Medical Superintelligence Framing]] via [[Regulatory Framing Conflict]]

- Hits: any clinical AI system operating in Europe.
- Does not hit: the US market, which is governed by [[HIPAA]] and FDA guidance.
""")

# ── COMPETITIVE CONTEXT ───────────────────────────────────────────────────────

write(os.path.join(OBJ, "Doximity.md"), """\
---
type: Actor
subtype: competitor / reference
status: live
---
# Doximity

The incumbent US physician professional network: 80%+ of US physicians have
a Doximity account. Doximity also monetizes pharma attention (telehealth,
drug reference, professional messaging) and launched Doximity GPT as a clinical
AI assistant. The comparison with OpenEvidence is instructive: Doximity's
advantage is friction reduction (physicians are already in the app); OpenEvidence's
advantage is corpus depth and citation grounding (purpose-built for evidence
retrieval, not a feature added to a network). Doximity is also a publicly traded
company (DOCS) -- its pharma advertising CPMs are a published benchmark against
which OpenEvidence's claimed $70-$1,000+ CPMs can be read as a premium. Both
compete for the same pharma digital health budget.

Competes-with [[OpenEvidence]] for [[Pharma Advertiser Segment]] budget ·
overlaps-with [[Clinician Segment]] (80% of US physicians have both) ·
benchmark-for [[Pharma Advertising Revenue]] CPM claims

- Hits: framing OpenEvidence's competitive position in the pharma ad market.
- Does not hit: the enterprise EHR integration layer, where OpenEvidence is ahead.
""")

# ── GHOSTS ────────────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "European Clinician Access.md"), """\
---
type: Ghost
subtype: was real, now removed
status: ghost
---
# European Clinician Access

A real user community -- physicians across the EU and UK, including hospital
doctors in Spain, Germany, the Netherlands, Belgium -- that used OpenEvidence
in daily clinical practice until April 30, 2026. Removed by [[EU-UK Withdrawal]].
No equivalent tool with comparable corpus quality and medical society credentialing
exists in Europe. The structural cost of the withdrawal fell entirely on this
user community, not on [[OpenEvidence]] (no paid European subscribers; the
[[Free Clinician Access Decision]] made the exit financially costless for the company).

Removed-by [[EU-UK Withdrawal]] · triggered-by [[EU AI Act and MDR]] ·
research question: is re-entry planned once EU compliance pathways clarify?
Lancet response paper suggests regulatory framework may evolve.
""")

write(os.path.join(OBJ, "Organic Revenue Visibility.md"), """\
---
type: Ghost
subtype: named-but-unwired
status: ghost
---
# Organic Revenue Visibility

Revenue is confirmed: Nadler stated $100M+ to CNBC; Sacra estimates $150M ARR
in 2025 at 90% gross margins. What is not public: the split between
[[Pharma Advertising Revenue]], [[Enterprise SaaS Revenue]], and [[CME Credit
Platform]]. This matters structurally because each revenue stream has different
growth ceilings, margin profiles, and competitive dynamics. If pharma advertising
is 90%+ of revenue, then the business is essentially a pharma attention platform
with a clinical AI skin -- a very different company than if enterprise SaaS is
growing fastest. The ghost is not whether revenue exists; it is whether the
business model is as diversified as the product line implies.

Research question: which revenue stream is growing fastest heading into the
[[Open Vista Suite]] launch? The answer shapes whether Open Vista is an
acceleration or a pivot in response to a ceiling somewhere else.
""")

write(os.path.join(OBJ, "Patient-Facing Interface.md"), """\
---
type: Ghost
subtype: named-but-unwired
status: ghost
---
# Patient-Facing Interface

The "medical superintelligence" vision implies eventual patient-facing AI --
agents that support not just the clinician but the patient. No patient product
exists. The architecture is entirely clinician-facing: the loop runs from clinical
question to evidence to clinician; the patient is context in the query, not a
user of the system. The ghost is also a business model question: a patient-facing
product would require a different revenue model (the pharma advertising model
requires NPI-verified prescribers; patients are not prescribers).

Named-in [[Medical Superintelligence Framing]] · not-connected to current products ·
research question: is a patient product in the private roadmap, or is this
a narrative artefact?
""")

# ── TENSIONS ─────────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Audience-Customer Split.md"), """\
---
type: Tension
status: live
---
# Audience-Customer Split

The structural tension at the center of the three-sided model: doctors use the
product; pharma pays for it. Their interests partially conflict. Pharma wants
brand messages at prescribing moments; doctors want unbiased, evidence-first
answers. OpenEvidence's structural answer: corpus quality and citation grounding
ensure that if a branded therapy appears in an answer, it is because the evidence
supports it, not because pharma paid for it -- advertising is separated from
editorial (the answer). The loading-screen model (ad during generation, answer
after) maintains the separation. Whether this separation holds as the platform
scales, as [[Clinical Documentation Capability]] deepens pharma access to
clinical workflows, and as [[Open Vista Suite]] moves from advertising toward
commercial intelligence, is the live question the map cannot yet answer.

Lives-between [[Pharma Advertiser Segment]] and [[Clinician Segment]] ·
managed-by editorial separation in [[Pharma Advertising Revenue]] ·
may-intensify as [[Open Vista Suite]] develops

- What moves if this resolves cleanly: continued physician trust, continued
  pharma premium CPMs.
- What moves if it does not: physician backlash, CPM compression, regulatory scrutiny.
""")

write(os.path.join(OBJ, "Accuracy Gap.md"), """\
---
type: Tension
status: live
---
# Accuracy Gap

Two performance numbers in the same system that do not reconcile cleanly.
OpenEvidence scored 100% on the USMLE ([[USMLE Benchmark]]) -- the highest-
profile credentialing milestone in US medicine. An independent preprint (medRxiv,
November 2025) found accuracy on complex medical subspecialty scenarios below 45%.
A structural heart disease comparison found ChatGPT-4o outperforming OpenEvidence
on expert-judged open-ended clinical questions. The USMLE is multiple-choice and
measures breadth of standard knowledge; real-world subspecialty scenarios are
open-ended and measure depth and reasoning. The gap between the numbers is the
gap between the benchmark and clinical practice.

Measured-by [[USMLE Benchmark]] · exposed-by medRxiv preprint ·
in-tension-with [[Medical Superintelligence Framing]] ·
relevant-to [[EU AI Act and MDR]] high-risk classification logic

- What moves if this resolves: subspecialist adoption, argument for re-entry into
  regulated markets.
- What moves if it worsens: enterprise hesitation, regulatory scrutiny, media coverage.
""")

write(os.path.join(OBJ, "Regulatory Framing Conflict.md"), """\
---
type: Tension
status: live
---
# Regulatory Framing Conflict

The [[Medical Superintelligence Framing]] implies superior autonomous clinical
judgment. The [[EU AI Act and MDR]] classification implies the same product
category should not be trusted to act autonomously and requires human oversight
and conformity assessment. Both cannot be simultaneously true and cost-free.
OpenEvidence resolved the conflict by exiting the EU jurisdiction ([[EU-UK
Withdrawal]]). The conflict persists: US FDA is developing its own AI guidance
for clinical decision support; if the US adopts a similar high-risk framework,
the same trade-off recurs in the core market. The valuation premium embedded in
[[Medical Superintelligence Framing]] is exposed if either US or EU regulatory
clarity lands on the restrictive end.

Lives-between [[Medical Superintelligence Framing]] and [[EU AI Act and MDR]] ·
temporarily-resolved-by [[EU-UK Withdrawal]] · may-resurface in US market

- What moves if this resolves toward "high-risk": compliance costs, human oversight
  requirements, possible FDA clearance needed.
- What moves if it resolves toward "general purpose": re-entry into EU possible,
  valuation narrative validated.
""")

write(os.path.join(OBJ, "Investor-Customer Duality.md"), """\
---
type: Tension
status: live
---
# Investor-Customer Duality

Mayo Clinic is both a member of [[VC Investor Coalition]] (strategic investor)
and a member of [[Enterprise Health Systems]] (clinical customer). Its investment
return depends on OpenEvidence's valuation growth, which depends partly on clinical
outcomes reported at Mayo. The relationship incentivizes favorable deployment
conditions and favorable coverage. It does not make the outcomes false, but
Mayo-sourced clinical validation data should be read with the dual role in mind.

Lives-between [[VC Investor Coalition]] and [[Enterprise Health Systems]] ·
held-by Mayo Clinic · relevant-to independent validation of [[Accuracy Gap]]
""")

# ── GRADIENT ─────────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "Search to Agentic Automation.md"), """\
---
type: Gradient
status: live
---
# Search to Agentic Automation

The product direction of travel. Started as a clinical search engine
([[Clinician Value Proposition]]). Added visit documentation
([[Clinical Documentation Capability]]). Building prior authorization drafting
([[Tandem Health]] partnership). Destination: subspecialty AI agents that
consult each other ([[Specialist Agent Network]]) and a pharma commercial
intelligence layer ([[Open Vista Suite]]). The strategic logic: use free
clinical search to achieve 40%+ US physician penetration, then automate the
administrative tasks those physicians hate (notes, prior auth), then monetize
the workflow data through pharma commercial products. Each step increases
switching costs and revenue per physician.

Drives [[OpenEvidence]] product sequencing ·
deepens [[Audience-Customer Split]] as automation increases ·
intensifies [[Regulatory Framing Conflict]] as autonomy increases ·
monetizes-via [[Open Vista Suite]] and [[Enterprise SaaS Revenue]] expansion

- What accelerates this: enterprise contract growth, prior auth adoption,
  Veeva partnership launch.
- What slows this: [[Accuracy Gap]] on complex scenarios; regulatory pressure.
""")

# ── INSTRUMENTS ──────────────────────────────────────────────────────────────

write(os.path.join(OBJ, "FHIR Standard.md"), """\
---
type: Instrument
status: live
---
# FHIR Standard

HL7 Fast Healthcare Interoperability Resources -- the shared technical protocol
enabling [[EHR Embedding]] to connect with Epic, Cerner, and other EHR systems.
A neutral, government-backed standard owned by no single actor. OpenEvidence's
enterprise integration layer depends on it. The standard is the pipe; the value
is what flows through it.

Enables [[EHR Embedding]] · used-by [[Epic and Cerner]] · passes data from
[[Enterprise Health Systems]] to [[Clinical Search Engine]]
""")

write(os.path.join(OBJ, "USMLE Benchmark.md"), """\
---
type: Instrument
status: live
---
# USMLE Benchmark

The United States Medical Licensing Examination -- a standardized, multiple-choice
test of broad medical knowledge used by OpenEvidence as the primary public
performance credential (first AI to score 100%). Its limitation as a benchmark is
also its limitation as a signal: it measures breadth on standard questions, not
depth on complex open-ended subspecialty cases. The gap between the 100% USMLE
score and the less than 45% complex subspecialty accuracy (medRxiv preprint) is
the [[Accuracy Gap]] tension in compressed form.

Validates [[Clinical Search Engine]] publicly · cited-by [[OpenEvidence]] ·
in-tension-with [[Accuracy Gap]]
""")

write(os.path.join(OBJ, "Specialist Agent Network.md"), """\
---
type: Capability
subtype: future product
status: pending
---
# Specialist Agent Network

The stated long-term product destination: subspecialty AI agents that consult
each other on complex patient cases. Unveiled with the $210M round. The vision
is a "digital twin neurologist interacting with the digital twin of the
dermatologist." No deployed product exists; this is the Series D narrative and
the framing behind [[Medical Superintelligence Framing]]. Requires resolving
the [[Accuracy Gap]] in subspecialty performance before clinical deployment
would be credible.

Promised-by [[OpenEvidence]] · named-in [[Medical Superintelligence Framing]] ·
destination-of [[Search to Agentic Automation]] ·
in-tension-with [[Accuracy Gap]] and [[Regulatory Framing Conflict]]

- What must happen first: subspecialty accuracy improvement; regulatory clarity.
- Does not hit: anything a clinician can use today.
""")

write(os.path.join(OBJ, "VC Investor Coalition.md"), """\
---
type: Actor
subtype: capital coalition
status: live
---
# VC Investor Coalition

Roughly $700M raised in 12 months (mid-2025 to January 2026). Series D ($250M
at $12B, January 2026) led by Thrive Capital and DST Global. Series B ($75M at
$1B, February 2025) led by Sequoia. Other investors: Google Ventures, Nvidia,
Kleiner Perkins, Blackstone, Henry Kravis, Coatue, ICONIQ, Greycroft, Breyer
Capital, BOND, Craft Ventures, Meritech, Alkeon. Mayo Clinic as strategic investor
(see [[Investor-Customer Duality]]). The coalition co-shaped [[Medical
Superintelligence Framing]] as the narrative required to justify the $12B valuation
on a $150M ARR base.

Funds [[OpenEvidence]] · co-shaped [[Medical Superintelligence Framing]] ·
includes [[Enterprise Health Systems]] member Mayo Clinic

- Hits: growth trajectory, product roadmap ambition, narrative pressure.
- Does not hit: product architecture or clinical decisions directly.
""")

print("Map written to:", ROOT)
print("Objects written:", len(os.listdir(OBJ)))

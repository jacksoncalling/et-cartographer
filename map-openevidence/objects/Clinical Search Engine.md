---
type: Capability
status: live
hub: core product
---
# Clinical Search Engine

The flagship product: a clinician enters a question or patient case; the system
retrieves, ranks, and synthesizes answers from the [[Medical Literature Corpus]]
(35 million peer-reviewed papers) with full citations. Architecture: RAG
(Retrieval-Augmented Generation) over the corpus, reranker layer, specialist
fine-tuned models via [[RAG and LoRA Architecture]], served at scale by [[Baseten]].
Every response is grounded -- each statement traceable to a timestamped source.
Validated on the [[USMLE Benchmark]] (first AI to score 100%). Access: free for
verified US clinicians (NPI required); web and mobile.

Held-by [[OpenEvidence]] · draws-from [[Medical Literature Corpus]] ·
trained-via [[RAG and LoRA Architecture]] · served-by [[Baseten]] ·
delivered-to [[US Clinician Base]] · embedded-in [[EHR Integration Layer]] ·
formerly-available-to [[European Clinician Access]]

- Hits: time-to-answer for clinical questions, drug selection confidence,
  rare disease lookup, protocol checking.
- Does not hit: documentation workflows (that is [[Visits -- Clinical Documentation]])
  or administrative tasks (that is [[Prior Authorization Agent]]).

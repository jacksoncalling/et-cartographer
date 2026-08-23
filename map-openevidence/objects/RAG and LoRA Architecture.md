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

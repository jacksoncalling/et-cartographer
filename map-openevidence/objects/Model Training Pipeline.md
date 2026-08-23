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

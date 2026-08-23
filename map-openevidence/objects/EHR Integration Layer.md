---
type: Capability
status: live
---
# EHR Integration Layer

The technical capability enabling OpenEvidence to embed inside existing clinical
workflows rather than sitting outside them. Uses HL7 [[FHIR Standard]] APIs to
connect with Epic and Cerner. Enterprise deployments: Sutter Health and Mount Sinai
run natural-language evidence search inside Epic workflows. The Cedars-Sinai
deployment goes furthest: live patient EHR data (comorbidities, medications,
allergies, prior procedures) is passed to the literature query at point of care,
personalizing the evidence retrieval to the individual patient context.

Connects [[OpenEvidence]] to [[Enterprise Health Systems]] ·
uses [[FHIR Standard]] · deepens lock-in of [[US Clinician Base]] ·
required-by but absent-from [[European Clinician Access]]

- Hits: workflow stickiness, data richness of queries, enterprise contract value.
- Does not hit: individual NPI-verified clinicians outside enterprise contracts;
  they use the web/mobile product without EHR integration.

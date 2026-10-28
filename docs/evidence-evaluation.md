# Evidence quality evaluation (prototype)

`evidence.evaluation.evaluate_claim` evaluates only evidence supplied by the
caller. It does not retrieve sources, independently fact-check the open web,
establish objective truth, or infer intent to deceive.

Each `Evidence` item includes a source label, a stance (`supports`, `refutes`,
or `neutral`), caller-provided credibility/relevance/directness scores in
`[0, 1]`, and an optional `independence_group`. The simple quality weight is
the product of those three scores. Copies in the same source group are capped
at the strongest weight per stance.

The result distinguishes support, contradiction, mixed evidence, and
insufficient evidence. The potential-misinformation flag is conservative:
provided evidence must favor refutation, include multiple independent source
groups, and exceed a configured evidence-quality threshold. It means "review
this claim", not "the claim is definitively false" or "the speaker lied".

Run `pytest -q tests/test_evidence_evaluation.py`. The fixture in
`tests/fixtures/evidence_benchmark.json` is a synthetic logic benchmark, not a
real-world fact-check dataset. Before deployment, add independently labelled
real-world examples and evaluate precision, recall, calibration, reviewer
agreement, and subgroup performance.

This module is intentionally isolated: it is not wired into the simulation,
agent registry, UI, or any decision-making path.

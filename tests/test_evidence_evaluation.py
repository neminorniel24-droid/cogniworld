"""Test-first tests for CogniWorld evidence evaluation."""
import json
from pathlib import Path
import pytest
from evidence.evaluation import Evidence, EvidenceStance, EvidenceStatus, evaluate_claim

FIXTURE = Path(__file__).parent / "fixtures" / "evidence_benchmark.json"
BENCHMARK = json.loads(FIXTURE.read_text(encoding="utf-8"))["cases"]

def make_evidence(row):
    return Evidence(
        source=row["source"], stance=row["stance"],
        credibility=row.get("credibility", 0.5),
        relevance=row.get("relevance", 1.0),
        directness=row.get("directness", 1.0),
        independence_group=row.get("independence_group"),
    )

@pytest.mark.parametrize("case", BENCHMARK, ids=lambda c: c["id"])
def test_synthetic_benchmark_status_and_flag(case):
    result = evaluate_claim(case["claim"], [make_evidence(x) for x in case["evidence"]])
    assert result.status.value == case["expected_status"]
    assert result.potential_misinformation is case["expected_potential_misinformation"]

@pytest.mark.parametrize("case", BENCHMARK, ids=lambda c: c["id"])
def test_scores_are_bounded(case):
    result = evaluate_claim(case["claim"], [make_evidence(x) for x in case["evidence"]])
    assert 0 <= result.evidence_quality <= 1
    assert 0 <= result.confidence <= 1
    assert result.support_weight >= 0 and result.refute_weight >= 0

def test_status_and_stance_are_explicit_enums():
    assert EvidenceStatus.INSUFFICIENT_EVIDENCE.value == "insufficient_evidence"
    assert EvidenceStance.REFUTES.value == "refutes"

def test_same_source_does_not_count_as_independent():
    items = [Evidence("News Syndicate", "refutes", .95, .95, .95),
             Evidence("news syndicate", "refutes", .90, .95, .95)]
    result = evaluate_claim("Synthetic repeated-source claim", items)
    assert result.independent_source_count == 1
    assert result.potential_misinformation is False

def test_evidence_order_does_not_change_result():
    items = [Evidence("A", "supports", .9, .9, 1.0),
             Evidence("B", "refutes", .4, .9, 1.0),
             Evidence("C", "supports", .8, .9, 1.0)]
    a = evaluate_claim("Synthetic ordering claim", items)
    b = evaluate_claim("Synthetic ordering claim", list(reversed(items)))
    assert a.status == b.status
    assert a.support_weight == pytest.approx(b.support_weight)
    assert a.refute_weight == pytest.approx(b.refute_weight)
    assert a.evidence_quality == pytest.approx(b.evidence_quality)
    assert a.confidence == pytest.approx(b.confidence)

def test_empty_claim_rejected():
    with pytest.raises(ValueError, match="claim"):
        evaluate_claim("  ", [])

def test_non_evidence_item_rejected():
    with pytest.raises(TypeError, match="Evidence"):
        evaluate_claim("Synthetic claim", [object()])

@pytest.mark.parametrize("field,value", [
    ("credibility", -.01), ("relevance", 1.01),
    ("directness", float("nan")), ("credibility", float("inf")),
])
def test_scores_must_be_finite_and_in_range(field, value):
    values = {"credibility": .5, "relevance": 1.0, "directness": 1.0}
    values[field] = value
    with pytest.raises(ValueError):
        Evidence("Source", "supports", **values)

def test_unknown_stance_rejected():
    with pytest.raises(ValueError, match="stance"):
        Evidence("Source", "maybe", .8)

def test_duplicate_independence_group_does_not_amplify_weight():
    a = Evidence("A", "refutes", .8, 1.0, 1.0, "same-network")
    b = Evidence("B", "refutes", .95, 1.0, 1.0, "same-network")
    result = evaluate_claim("Synthetic duplicate claim", [a, b])
    assert result.refute_weight == pytest.approx(.95)
    assert result.independent_source_count == 1

def test_thresholds_are_validated():
    with pytest.raises(ValueError):
        evaluate_claim("Synthetic claim", [], decision_margin=1.5)
    with pytest.raises(ValueError):
        evaluate_claim("Synthetic claim", [], minimum_weight=-.1)
    with pytest.raises(ValueError):
        evaluate_claim("Synthetic claim", [], minimum_independent_sources=0)

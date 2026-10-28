"""Transparent scoring of evidence supplied for a claim.

This module does not search for sources, independently verify facts, or infer
whether a person intended to mislead. Its conservative misinformation flag
means only that the supplied evidence strongly contradicts a claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math
from typing import Iterable


class EvidenceStance(str, Enum):
    SUPPORTS = "supports"
    REFUTES = "refutes"
    NEUTRAL = "neutral"


class EvidenceStatus(str, Enum):
    SUPPORTED = "supported_by_provided_evidence"
    CONTRADICTED = "contradicted_by_provided_evidence"
    MIXED = "mixed_evidence"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


def _score(name: str, value: float) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a finite number between 0 and 1")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite number between 0 and 1") from exc
    if not math.isfinite(number) or not 0.0 <= number <= 1.0:
        raise ValueError(f"{name} must be a finite number between 0 and 1")
    return number


@dataclass(frozen=True)
class Evidence:
    """One evidence item; scores are caller-provided, not verified facts."""

    source: str
    stance: EvidenceStance | str
    credibility: float = 0.5
    relevance: float = 1.0
    directness: float = 1.0
    independence_group: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source.strip():
            raise ValueError("source must be a non-empty string")
        try:
            stance = EvidenceStance(self.stance)
        except (ValueError, TypeError) as exc:
            raise ValueError("stance must be supports, refutes, or neutral") from exc
        object.__setattr__(self, "stance", stance)
        for name in ("credibility", "relevance", "directness"):
            object.__setattr__(self, name, _score(name, getattr(self, name)))
        if self.independence_group is not None:
            if not isinstance(self.independence_group, str) or not self.independence_group.strip():
                raise ValueError("independence_group must be non-empty when supplied")
            object.__setattr__(
                self, "independence_group", self.independence_group.strip().casefold()
            )

    @property
    def quality(self) -> float:
        """Simple multiplicative evidence weight in [0, 1]."""
        return self.credibility * self.relevance * self.directness

    @property
    def source_group(self) -> str:
        """Caller-provided independence group, or normalized source label."""
        return self.independence_group or self.source.strip().casefold()


@dataclass(frozen=True)
class ClaimAssessment:
    claim: str
    status: EvidenceStatus
    support_weight: float
    refute_weight: float
    evidence_quality: float
    confidence: float
    independent_source_count: int
    potential_misinformation: bool
    rationale: tuple[str, ...]


def _threshold(name: str, value: float, *, allow_zero: bool = True) -> float:
    number = _score(name, value)
    if not allow_zero and number == 0.0:
        raise ValueError(f"{name} must be greater than zero")
    return number


def evaluate_claim(
    claim: str,
    evidence: Iterable[Evidence],
    *,
    minimum_weight: float = 0.25,
    decision_margin: float = 0.20,
    misinformation_quality_threshold: float = 0.70,
    minimum_independent_sources: int = 2,
) -> ClaimAssessment:
    """Assess the balance of supplied evidence without asserting objective truth.

    Copies from the same source group contribute at most the strongest quality
    score per stance. Neutral evidence contributes to quality reporting but not
    to the support/refutation decision.
    """
    if not isinstance(claim, str) or not claim.strip():
        raise ValueError("claim must be a non-empty string")
    minimum_weight = _threshold("minimum_weight", minimum_weight, allow_zero=False)
    decision_margin = _threshold("decision_margin", decision_margin)
    misinformation_quality_threshold = _threshold(
        "misinformation_quality_threshold", misinformation_quality_threshold
    )
    if isinstance(minimum_independent_sources, bool) or not isinstance(minimum_independent_sources, int):
        raise ValueError("minimum_independent_sources must be a positive integer")
    if minimum_independent_sources < 1:
        raise ValueError("minimum_independent_sources must be a positive integer")

    items = list(evidence)
    if any(not isinstance(item, Evidence) for item in items):
        raise TypeError("evidence must contain only Evidence items")
    if not items:
        return ClaimAssessment(
            claim=claim.strip(),
            status=EvidenceStatus.INSUFFICIENT_EVIDENCE,
            support_weight=0.0,
            refute_weight=0.0,
            evidence_quality=0.0,
            confidence=0.0,
            independent_source_count=0,
            potential_misinformation=False,
            rationale=(
                "No evidence was provided.",
                "This result is not an independent fact-check.",
            ),
        )

    quality_by_group: dict[str, float] = {}
    weight_by_group_stance: dict[tuple[str, EvidenceStance], float] = {}
    directional_groups: set[str] = set()

    for item in items:
        group = item.source_group
        quality_by_group[group] = max(quality_by_group.get(group, 0.0), item.quality)
        if item.stance is EvidenceStance.NEUTRAL:
            continue
        if item.quality > 0:
            directional_groups.add(group)
        key = (group, item.stance)
        weight_by_group_stance[key] = max(
            weight_by_group_stance.get(key, 0.0), item.quality
        )

    evidence_quality = sum(quality_by_group.values()) / len(quality_by_group)
    support_weight = sum(
        value for (_, stance), value in weight_by_group_stance.items()
        if stance is EvidenceStance.SUPPORTS
    )
    refute_weight = sum(
        value for (_, stance), value in weight_by_group_stance.items()
        if stance is EvidenceStance.REFUTES
    )
    total = support_weight + refute_weight
    source_count = len(directional_groups)

    if total < minimum_weight:
        status = EvidenceStatus.INSUFFICIENT_EVIDENCE
        rationale = (
            "Directional evidence weight is below the configured minimum.",
            "This result describes supplied evidence, not objective truth.",
        )
    else:
        balance = (support_weight - refute_weight) / total
        if balance >= decision_margin:
            status = EvidenceStatus.SUPPORTED
            rationale = (
                "The supplied evidence favors support for the claim.",
                "This result is not an independent fact-check.",
            )
        elif balance <= -decision_margin:
            status = EvidenceStatus.CONTRADICTED
            rationale = (
                "The supplied evidence favors refutation of the claim.",
                "This result is not an independent fact-check.",
            )
        else:
            status = EvidenceStatus.MIXED
            rationale = (
                "The supplied evidence is mixed or closely balanced.",
                "More independent, relevant evidence may be needed.",
            )

    confidence = (
        evidence_quality * abs(support_weight - refute_weight) / total
        if total > 0 else 0.0
    )
    potential_misinformation = (
        status is EvidenceStatus.CONTRADICTED
        and source_count >= minimum_independent_sources
        and evidence_quality >= misinformation_quality_threshold
    )
    if potential_misinformation:
        rationale += (
            "Review flag: multiple independent source groups strongly contradict the claim.",
            "The flag does not infer intent to deceive.",
        )

    return ClaimAssessment(
        claim=claim.strip(),
        status=status,
        support_weight=support_weight,
        refute_weight=refute_weight,
        evidence_quality=evidence_quality,
        confidence=max(0.0, min(1.0, confidence)),
        independent_source_count=source_count,
        potential_misinformation=potential_misinformation,
        rationale=rationale,
    )

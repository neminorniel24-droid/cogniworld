"""Apply registered environmental causal rules in deterministic order."""

from .registry import RULES

def apply_rules(world):
    for rule in RULES:
        rule(world)

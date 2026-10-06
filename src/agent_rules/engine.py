from .registry import RULES

def apply_rules(agents,world):
    for rule in RULES: rule(agents,world)

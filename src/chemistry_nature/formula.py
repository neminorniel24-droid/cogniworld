"""Dependency-free formula parser and approximate molar-mass calculator."""
import json
from collections import Counter
from pathlib import Path
_DATA=Path(__file__).with_name("data")/"reference_elements.json"

def _weights():
    with _DATA.open(encoding="utf-8") as f: return json.load(f)["elements"]

def parse_formula(formula: str) -> dict[str,int]:
    """Parse element symbols, integer subscripts and nested parentheses.

    Charges, hydrate dots, isotopes and square-bracket complexes are rejected.
    """
    if not isinstance(formula,str) or not formula or formula.strip()!=formula:
        raise ValueError("formula must be a non-empty string without surrounding whitespace")
    weights=_weights(); pos=0
    def group(nested=False):
        nonlocal pos
        result=Counter()
        while pos<len(formula) and formula[pos]!=")":
            if formula[pos]=="(":
                pos+=1; sub=group(True)
                if pos>=len(formula) or formula[pos]!=")": raise ValueError("unmatched opening parenthesis")
                pos+=1; start=pos
                while pos<len(formula) and formula[pos].isdigit(): pos+=1
                mult=int(formula[start:pos] or "1")
                if mult<1: raise ValueError("subscripts must be positive integers")
                result.update({k:v*mult for k,v in sub.items()})
            elif formula[pos].isupper():
                start=pos; pos+=1
                while pos<len(formula) and formula[pos].islower(): pos+=1
                symbol=formula[start:pos]
                if symbol not in weights: raise ValueError(f"unknown element symbol: {symbol}")
                start=pos
                while pos<len(formula) and formula[pos].isdigit(): pos+=1
                count=int(formula[start:pos] or "1")
                if count<1: raise ValueError("subscripts must be positive integers")
                result[symbol]+=count
            else: raise ValueError(f"unsupported character at position {pos}: {formula[pos]!r}")
        if nested and pos>=len(formula): raise ValueError("unmatched opening parenthesis")
        if not result: raise ValueError("empty groups/formulas are not supported")
        return result
    counts=group()
    if pos!=len(formula): raise ValueError("unmatched closing parenthesis")
    return dict(counts)

def molar_mass(formula: str) -> float:
    """Approximate molar mass in g/mol using the bundled curated subset."""
    weights=_weights()
    return sum(weights[s]["atomic_weight"]*n for s,n in parse_formula(formula).items())

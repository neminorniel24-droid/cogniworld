"""Bounded integer-coefficient reaction balancing for small equations."""
from collections import Counter
from itertools import product
import re
from math import gcd
from functools import reduce
from .formula import parse_formula
_TERM=re.compile(r"^\s*(?:(\d+)\s+)?([A-Za-z][A-Za-z0-9()]*)\s*$")

def _parse_side(side):
    terms=[]
    for raw in side.split("+"):
        m=_TERM.match(raw)
        if not m: raise ValueError(f"unsupported reaction term: {raw!r}")
        f=m.group(2); terms.append((int(m.group(1) or 1),f,parse_formula(f)))
    if not terms: raise ValueError("reaction side is empty")
    return terms

def _reaction(text):
    if not isinstance(text,str) or text.count("->")!=1: raise ValueError("reaction must contain exactly one '->'")
    a,b=text.split("->"); return _parse_side(a),_parse_side(b)

def _totals(side):
    out=Counter()
    for coeff,_,atoms in side:
        for e,n in atoms.items(): out[e]+=coeff*n
    return out

def is_balanced(reaction):
    left,right=_reaction(reaction)
    return _totals(left)==_totals(right)

def balance_reaction(reaction, *, max_coefficient=12):
    """Find a primitive lowest-sum positive integer balance within a bounded search."""
    if isinstance(max_coefficient,bool) or not isinstance(max_coefficient,int) or max_coefficient<1:
        raise ValueError("max_coefficient must be a positive integer")
    left,right=_reaction(reaction); terms=left+right
    if len(terms)>6: raise ValueError("supports at most six chemical terms")
    if len(set().union(*(a.keys() for _,_,a in terms)))>5: raise ValueError("supports at most five elements")
    candidates=[]
    for coeffs in product(range(1,max_coefficient+1),repeat=len(terms)):
        if reduce(gcd,coeffs)!=1: continue
        delta=Counter()
        for i,(_,_,atoms) in enumerate(terms):
            sign=1 if i<len(left) else -1
            for e,n in atoms.items(): delta[e]+=sign*coeffs[i]*n
        if any(delta.values()): continue
        score=sum(coeffs)
        candidates.append((score,coeffs))
    if not candidates: raise ValueError(f"no balance found with coefficients <= {max_coefficient}")
    _,c=min(candidates)
    def render(start,end):
        return " + ".join((f"{c[i]} " if c[i]!=1 else "")+terms[i][1] for i in range(start,end))
    result=f"{render(0,len(left))} -> {render(len(left),len(terms))}"
    if not is_balanced(result): raise ArithmeticError("internal balance validation failed")
    return result

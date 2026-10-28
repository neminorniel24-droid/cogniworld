"""Run with PYTHONPATH=src python scripts/smoke_chemistry_nature.py."""
from chemistry_nature import balance_reaction,molar_mass,parse_formula,simulate_carbon_cycle
assert parse_formula("Ca(OH)2")=={"Ca":1,"O":2,"H":2}
assert 18.0<molar_mass("H2O")<18.1
assert balance_reaction("H2 + O2 -> H2O")=="2 H2 + O2 -> 2 H2O"
a={"air":10.,"plant":5.}
b=simulate_carbon_cycle(a,[{"source":"air","target":"plant","rate":.1}],steps=5)
assert abs(sum(a.values())-sum(b.values()))<1e-9
print("chemistry-nature smoke checks passed")

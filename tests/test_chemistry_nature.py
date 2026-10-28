import pytest
from chemistry_nature.formula import parse_formula, molar_mass
from chemistry_nature.reactions import balance_reaction, is_balanced
from chemistry_nature.ecology import simulate_carbon_cycle
from chemistry_nature.green_chemistry import atom_economy, e_factor
from chemistry_nature.datasets import load_reference_dataset, load_natural_process_dataset

def test_formula_and_nested_groups():
    assert parse_formula("H2O")=={"H":2,"O":1}
    assert parse_formula("Ca(OH)2")=={"Ca":1,"O":2,"H":2}
    assert parse_formula("Al2(SO4)3")=={"Al":2,"S":3,"O":12}
@pytest.mark.parametrize("bad",["","2H2O","h2o","Xx2","H0","Ca(OH","H2..O","()"])
def test_invalid_formula_rejected(bad):
    with pytest.raises(ValueError): parse_formula(bad)
def test_water_molar_mass(): assert molar_mass("H2O")==pytest.approx(18.015,abs=.003)
def test_water_reaction_balance():
    out=balance_reaction("H2 + O2 -> H2O")
    assert out=="2 H2 + O2 -> 2 H2O" and is_balanced(out)
def test_photosynthesis_balance():
    out=balance_reaction("CO2 + H2O -> C6H12O6 + O2")
    assert out=="6 CO2 + 6 H2O -> C6H12O6 + 6 O2" and is_balanced(out)
def test_impossible_reaction_fails():
    with pytest.raises(ValueError): balance_reaction("H2 -> O2")
def test_carbon_cycle_conserves_mass():
    initial={"atmosphere":100.,"biosphere":40.,"soil":30.,"ocean":80.}
    flows=[{"source":"atmosphere","target":"biosphere","rate":.02},{"source":"biosphere","target":"soil","rate":.01},{"source":"ocean","target":"atmosphere","rate":.005}]
    final=simulate_carbon_cycle(initial,flows,steps=50)
    assert sum(final.values())==pytest.approx(sum(initial.values()),abs=1e-8)
    assert all(x>=0 for x in final.values())
def test_cycle_rejects_unknown_reservoir():
    with pytest.raises(ValueError): simulate_carbon_cycle({"air":1.},[{"source":"missing","target":"air","rate":.1}],steps=1)
def test_cycle_rejects_unstable_step():
    with pytest.raises(ValueError): simulate_carbon_cycle({"a":1.,"b":0.},[{"source":"a","target":"b","rate":2}],steps=1)
def test_atom_economy_for_water_formation():
    assert atom_economy(reactants=["H2","O2"],desired_product="H2O",balanced_coefficients=[2,1,2])==pytest.approx(100.,abs=.1)
def test_atom_economy_rejects_unbalanced_input():
    with pytest.raises(ValueError): atom_economy(reactants=["H2","O2"],desired_product="H2O",balanced_coefficients=[1,1,1])
def test_e_factor():
    assert e_factor(waste_mass=8.,product_mass=2.)==pytest.approx(4.)
@pytest.mark.parametrize("w,p", [(-1,1),(1,0),(float("inf"),1)])
def test_e_factor_rejects_invalid_masses(w,p):
    with pytest.raises(ValueError): e_factor(waste_mass=w,product_mass=p)
def test_reference_data_provenance():
    data=load_reference_dataset()
    assert data["metadata"]["status"]=="curated_subset"
    assert data["elements"]["C"]["atomic_weight"]==pytest.approx(12.011)
    assert data["metadata"]["sources"]
def test_natural_parameters_are_explicitly_illustrative():
    data=load_natural_process_dataset()
    assert data["metadata"]["not_for_prediction"] is True

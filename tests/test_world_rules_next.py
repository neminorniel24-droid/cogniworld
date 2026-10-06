import torch
from world_rule_helpers import make_world


def test_logic_102():
    from world_rules.logic_102_vegetation_shades_surface import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target < before)

def test_logic_103():
    from world_rules.logic_103_bare_soil_absorbs_more_heat import apply
    w = make_world()
    w.vegetation.zero_()
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

def test_logic_104():
    from world_rules.logic_104_ice_reflects_solar_energy import apply
    w = make_world()
    w.ice.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target < before)

def test_logic_105():
    from world_rules.logic_105_methane_adds_greenhouse_warming import apply
    w = make_world()
    w.methane.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

def test_logic_106():
    from world_rules.logic_106_co2_adds_greenhouse_warming import apply
    w = make_world()
    w.co2.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

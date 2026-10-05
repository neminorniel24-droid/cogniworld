import torch
from world_rule_helpers import make_world


def test_logic_002():
    from world_rules.logic_002_elevation_sets_thermal_target import apply
    w = make_world()
    w.temperature.fill_(0.5); w.elevation.fill_(0.0); apply(w); a=w.temperature_target.clone(); w.elevation.fill_(1.0); apply(w); b=w.temperature_target.clone()
    assert torch.all(a > b)


def test_logic_003():
    from world_rules.logic_003_thermal_inertia import apply
    w = make_world()
    w.temperature.fill_(0.0); w.temperature_target.fill_(1.0); apply(w);
    assert torch.allclose(w.temperature, torch.full_like(w.temperature, 0.08))


def test_logic_004():
    from world_rules.logic_004_heat_increases_evaporation_potential import apply
    w = make_world()
    w.temperature.fill_(0.0); apply(w); a=w.evaporation.clone(); w.temperature.fill_(1.0); apply(w); b=w.evaporation.clone()
    assert torch.all(b > a)

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


def test_logic_005():
    from world_rules.logic_005_evaporation_removes_surface_water import apply
    w = make_world()
    w.surface_water.fill_(1.0); w.evaporation.fill_(0.05); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.95))


def test_logic_006():
    from world_rules.logic_006_evaporation_raises_humidity import apply
    w = make_world()
    w.humidity.zero_(); w.evaporation.fill_(0.2); apply(w);
    assert torch.allclose(w.humidity, torch.full_like(w.humidity, 0.1))


def test_logic_007():
    from world_rules.logic_007_humidity_condenses_clouds import apply
    w = make_world()
    w.cloud.zero_(); w.humidity.fill_(0.4); apply(w); a=w.cloud.clone(); w.humidity.fill_(0.8); apply(w);
    assert torch.all(w.cloud > a)

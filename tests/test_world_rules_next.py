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

def test_logic_107():
    from world_rules.logic_107_humidity_adds_water_vapor_warming import apply
    w = make_world()
    w.humidity.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

def test_logic_108():
    from world_rules.logic_108_clouds_add_greenhouse_warming import apply
    w = make_world()
    w.cloud.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

def test_logic_109():
    from world_rules.logic_109_wind_increases_evaporation import apply
    w = make_world()
    w.wind_x.fill_(1.0)
    w.evaporation.zero_()
    apply(w)
    assert torch.allclose(w.evaporation, torch.full_like(w.evaporation, 0.006))

def test_logic_110():
    from world_rules.logic_110_dry_air_increases_evaporation import apply
    w = make_world()
    w.humidity.zero_()
    w.evaporation.zero_()
    apply(w)
    assert torch.allclose(w.evaporation, torch.full_like(w.evaporation, 0.005))

def test_logic_111():
    from world_rules.logic_111_ice_suppresses_evaporation import apply
    w = make_world()
    w.ice.fill_(1.0)
    w.evaporation.fill_(1.0)
    before=w.evaporation.clone()
    apply(w)
    assert torch.all(w.evaporation < before)

def test_logic_112():
    from world_rules.logic_112_surface_water_recharges_soil import apply
    w = make_world()
    w.surface_water.fill_(1.0)
    w.soil_moisture.zero_()
    apply(w)
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.01))

def test_logic_113():
    from world_rules.logic_113_rain_adds_surface_water import apply
    w = make_world()
    w.rain.fill_(1.0)
    w.surface_water.zero_()
    apply(w)
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.03))

def test_logic_114():
    from world_rules.logic_114_runoff_adds_surface_water import apply
    w = make_world()
    w.runoff.fill_(1.0)
    w.surface_water.zero_()
    apply(w)
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.02))

def test_logic_115():
    from world_rules.logic_115_deep_soil_retains_more_moisture import apply
    w = make_world()
    w.soil_depth.fill_(1.0)
    w.soil_moisture.zero_()
    apply(w)
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.005))

def test_logic_116():
    from world_rules.logic_116_shallow_soil_drains_faster import apply
    w = make_world()
    w.soil_depth.zero_()
    w.soil_moisture.fill_(1.0)
    before=w.soil_moisture.clone()
    apply(w)
    assert torch.all(w.soil_moisture < before)

def test_logic_117():
    from world_rules.logic_117_roots_reduce_erosion import apply
    w = make_world()
    w.root_density.fill_(1.0)
    w.erosion.fill_(1.0)
    before=w.erosion.clone()
    apply(w)
    assert torch.all(w.erosion < before)

def test_logic_118():
    from world_rules.logic_118_canopy_intercepts_rain import apply
    w = make_world()
    w.rain.fill_(1.0)
    w.vegetation.fill_(1.0)
    w.soil_moisture.zero_()
    apply(w)
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.01))

def test_logic_119():
    from world_rules.logic_119_wetlands_reduce_runoff import apply
    w = make_world()
    w.wetland.fill_(1.0)
    w.runoff.fill_(1.0)
    before=w.runoff.clone()
    apply(w)
    assert torch.all(w.runoff < before)

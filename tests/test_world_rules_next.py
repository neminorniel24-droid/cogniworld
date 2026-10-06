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

def test_logic_120():
    from world_rules.logic_120_wetlands_store_rainfall import apply
    w = make_world()
    w.wetland.fill_(1.0)
    w.rain.fill_(1.0)
    w.surface_water.zero_()
    apply(w)
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.01))

def test_logic_121():
    from world_rules.logic_121_waterlogging_reduces_soil_oxygen import apply
    w = make_world()
    w.soil_moisture.fill_(1.0)
    w.oxygen.fill_(1.0)
    before=w.oxygen.clone()
    apply(w)
    assert torch.all(w.oxygen < before)

def test_logic_122():
    from world_rules.logic_122_wind_reoxygenates_surface import apply
    w = make_world()
    w.wind_x.fill_(1.0)
    w.oxygen.zero_()
    apply(w)
    assert torch.allclose(w.oxygen, torch.full_like(w.oxygen, 0.005))

def test_logic_123():
    from world_rules.logic_123_vegetation_transpiration_drains_soil import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.soil_moisture.fill_(1.0)
    before=w.soil_moisture.clone()
    apply(w)
    assert torch.all(w.soil_moisture < before)

def test_logic_124():
    from world_rules.logic_124_humid_air_reduces_transpiration_loss import apply
    w = make_world()
    w.humidity.fill_(1.0)
    w.vegetation.fill_(1.0)
    w.soil_moisture.zero_()
    apply(w)
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.002))

def test_logic_125():
    from world_rules.logic_125_cloud_cover_limits_photosynthesis import apply
    w = make_world()
    w.cloud.fill_(1.0)
    w.photosynthesis_factor.fill_(1.0)
    before=w.photosynthesis_factor.clone()
    apply(w)
    assert torch.all(w.photosynthesis_factor < before)

def test_logic_126():
    from world_rules.logic_126_nutrients_raise_photosynthesis_factor import apply
    w = make_world()
    w.nutrients.fill_(1.0)
    w.photosynthesis_factor.fill_(0.5)
    before=w.photosynthesis_factor.clone()
    apply(w)
    assert torch.all(w.photosynthesis_factor > before)

def test_logic_127():
    from world_rules.logic_127_nutrient_scarcity_slows_vegetation import apply
    w = make_world()
    w.nutrients.zero_()
    w.vegetation.fill_(1.0)
    before=w.vegetation.clone()
    apply(w)
    assert torch.all(w.vegetation < before)

def test_logic_128():
    from world_rules.logic_128_co2_enrichment_grows_vegetation import apply
    w = make_world()
    w.co2.fill_(1.0)
    w.photosynthesis_factor.fill_(1.0)
    w.vegetation.zero_()
    apply(w)
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.006))

def test_logic_129():
    from world_rules.logic_129_temperature_extremes_suppress_vegetation import apply
    w = make_world()
    w.temperature.fill_(1.0)
    w.vegetation.fill_(1.0)
    before=w.vegetation.clone()
    apply(w)
    assert torch.all(w.vegetation < before)

def test_logic_130():
    from world_rules.logic_130_moderate_temperature_supports_vegetation import apply
    w = make_world()
    w.temperature.fill_(0.5)
    w.vegetation.zero_()
    apply(w)
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.004))

def test_logic_131():
    from world_rules.logic_131_oxygen_supports_decomposition import apply
    w = make_world()
    w.oxygen.fill_(1.0)
    w.decomposition_rate.zero_()
    apply(w)
    assert torch.allclose(w.decomposition_rate, torch.full_like(w.decomposition_rate, 0.01))

def test_logic_132():
    from world_rules.logic_132_detritus_feeds_decomposition import apply
    w = make_world()
    w.detritus.fill_(1.0)
    w.decomposition_rate.zero_()
    apply(w)
    assert torch.allclose(w.decomposition_rate, torch.full_like(w.decomposition_rate, 0.01))

def test_logic_133():
    from world_rules.logic_133_cold_slows_decomposition import apply
    w = make_world()
    w.temperature.zero_()
    w.decomposition_rate.fill_(1.0)
    before=w.decomposition_rate.clone()
    apply(w)
    assert torch.all(w.decomposition_rate < before)

def test_logic_134():
    from world_rules.logic_134_wet_soil_accelerates_decomposition import apply
    w = make_world()
    w.soil_moisture.fill_(1.0)
    w.decomposition_rate.zero_()
    apply(w)
    assert torch.allclose(w.decomposition_rate, torch.full_like(w.decomposition_rate, 0.008))

def test_logic_135():
    from world_rules.logic_135_decomposition_consumes_detritus import apply
    w = make_world()
    w.decomposition_rate.fill_(1.0)
    w.detritus.fill_(1.0)
    before=w.detritus.clone()
    apply(w)
    assert torch.all(w.detritus < before)

def test_logic_136():
    from world_rules.logic_136_decomposition_recycles_nutrients import apply
    w = make_world()
    w.decomposition_rate.fill_(1.0)
    w.nutrients.zero_()
    apply(w)
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.008))

def test_logic_137():
    from world_rules.logic_137_decomposition_releases_co2 import apply
    w = make_world()
    w.decomposition_rate.fill_(1.0)
    w.co2.zero_()
    apply(w)
    assert torch.allclose(w.co2, torch.full_like(w.co2, 0.004))

def test_logic_138():
    from world_rules.logic_138_decomposition_consumes_oxygen import apply
    w = make_world()
    w.decomposition_rate.fill_(1.0)
    w.oxygen.fill_(1.0)
    before=w.oxygen.clone()
    apply(w)
    assert torch.all(w.oxygen < before)

def test_logic_139():
    from world_rules.logic_139_oxygen_oxidizes_methane import apply
    w = make_world()
    w.oxygen.fill_(1.0)
    w.methane.fill_(1.0)
    before=w.methane.clone()
    apply(w)
    assert torch.all(w.methane < before)

def test_logic_140():
    from world_rules.logic_140_dry_soil_reduces_methane import apply
    w = make_world()
    w.soil_moisture.zero_()
    w.methane.fill_(1.0)
    before=w.methane.clone()
    apply(w)
    assert torch.all(w.methane < before)

def test_logic_141():
    from world_rules.logic_141_drought_releases_carbon import apply
    w = make_world()
    w.soil_moisture.zero_()
    w.carbon_storage.fill_(1.0)
    before=w.carbon_storage.clone()
    apply(w)
    assert torch.all(w.carbon_storage < before)

def test_logic_142():
    from world_rules.logic_142_biomass_builds_carbon_storage import apply
    w = make_world()
    w.biomass.fill_(1.0)
    w.carbon_storage.zero_()
    apply(w)
    assert torch.allclose(w.carbon_storage, torch.full_like(w.carbon_storage, 0.01))

def test_logic_143():
    from world_rules.logic_143_biomass_produces_oxygen import apply
    w = make_world()
    w.biomass.fill_(1.0)
    w.photosynthesis_factor.fill_(1.0)
    w.oxygen.zero_()
    apply(w)
    assert torch.allclose(w.oxygen, torch.full_like(w.oxygen, 0.008))

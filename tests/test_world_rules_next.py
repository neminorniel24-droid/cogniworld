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

def test_logic_144():
    from world_rules.logic_144_herbivory_reduces_biomass import apply
    w = make_world()
    w.herbivore.fill_(1.0)
    w.biomass.fill_(1.0)
    before=w.biomass.clone()
    apply(w)
    assert torch.all(w.biomass < before)

def test_logic_145():
    from world_rules.logic_145_grazing_creates_detritus import apply
    w = make_world()
    w.herbivore.fill_(1.0)
    w.detritus.zero_()
    apply(w)
    assert torch.allclose(w.detritus, torch.full_like(w.detritus, 0.003))

def test_logic_146():
    from world_rules.logic_146_predation_creates_carrion import apply
    w = make_world()
    w.predator.fill_(1.0)
    w.herbivore.fill_(1.0)
    w.carrion.zero_()
    apply(w)
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.004))

def test_logic_147():
    from world_rules.logic_147_carrion_decomposition_adds_decomposition import apply
    w = make_world()
    w.carrion.fill_(1.0)
    w.decomposition_rate.zero_()
    apply(w)
    assert torch.allclose(w.decomposition_rate, torch.full_like(w.decomposition_rate, 0.006))

def test_logic_148():
    from world_rules.logic_148_vegetation_raises_biodiversity import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.biodiversity.zero_()
    apply(w)
    assert torch.allclose(w.biodiversity, torch.full_like(w.biodiversity, 0.005))

def test_logic_149():
    from world_rules.logic_149_balanced_food_web_raises_biodiversity import apply
    w = make_world()
    w.herbivore.fill_(1.0)
    w.predator.fill_(1.0)
    w.biodiversity.zero_()
    apply(w)
    assert torch.allclose(w.biodiversity, torch.full_like(w.biodiversity, 0.003))

def test_logic_150():
    from world_rules.logic_150_habitat_stress_reduces_biodiversity import apply
    w = make_world()
    w.habitat_stress.fill_(1.0)
    w.biodiversity.fill_(1.0)
    before=w.biodiversity.clone()
    apply(w)
    assert torch.all(w.biodiversity < before)

def test_logic_151():
    from world_rules.logic_151_biodiversity_suppresses_pathogens import apply
    w = make_world()
    w.biodiversity.fill_(1.0)
    w.pathogen_load.fill_(1.0)
    before=w.pathogen_load.clone()
    apply(w)
    assert torch.all(w.pathogen_load < before)

def test_logic_152():
    from world_rules.logic_152_habitat_stress_increases_pathogens import apply
    w = make_world()
    w.habitat_stress.fill_(1.0)
    w.pathogen_load.zero_()
    apply(w)
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.004))

def test_logic_153():
    from world_rules.logic_153_wet_soil_supports_pathogen_survival import apply
    w = make_world()
    w.soil_moisture.fill_(1.0)
    w.pathogen_load.zero_()
    apply(w)
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.003))

def test_logic_154():
    from world_rules.logic_154_dryness_suppresses_pathogens import apply
    w = make_world()
    w.soil_moisture.zero_()
    w.pathogen_load.fill_(1.0)
    before=w.pathogen_load.clone()
    apply(w)
    assert torch.all(w.pathogen_load < before)

def test_logic_155():
    from world_rules.logic_155_warmth_increases_pathogen_growth import apply
    w = make_world()
    w.temperature.fill_(1.0)
    w.pathogen_load.zero_()
    apply(w)
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.005))

def test_logic_156():
    from world_rules.logic_156_cold_reduces_pathogens import apply
    w = make_world()
    w.temperature.zero_()
    w.pathogen_load.fill_(1.0)
    before=w.pathogen_load.clone()
    apply(w)
    assert torch.all(w.pathogen_load < before)

def test_logic_157():
    from world_rules.logic_157_rain_washes_pathogens import apply
    w = make_world()
    w.rain.fill_(1.0)
    w.pathogen_load.fill_(1.0)
    before=w.pathogen_load.clone()
    apply(w)
    assert torch.all(w.pathogen_load < before)

def test_logic_158():
    from world_rules.logic_158_vegetation_shelters_pathogens import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.biodiversity.zero_()
    w.pathogen_load.zero_()
    apply(w)
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.002))

def test_logic_159():
    from world_rules.logic_159_pathogens_raise_habitat_stress import apply
    w = make_world()
    w.pathogen_load.fill_(1.0)
    w.habitat_stress.zero_()
    apply(w)
    assert torch.allclose(w.habitat_stress, torch.full_like(w.habitat_stress, 0.003))

def test_logic_160():
    from world_rules.logic_160_low_oxygen_reduces_herbivores import apply
    w = make_world()
    w.oxygen.zero_()
    w.herbivore.fill_(1.0)
    before=w.herbivore.clone()
    apply(w)
    assert torch.all(w.herbivore < before)

def test_logic_161():
    from world_rules.logic_161_oxygen_supports_predators import apply
    w = make_world()
    w.oxygen.fill_(1.0)
    w.predator.zero_()
    apply(w)
    assert torch.allclose(w.predator, torch.full_like(w.predator, 0.003))

def test_logic_162():
    from world_rules.logic_162_prey_abundance_supports_predators import apply
    w = make_world()
    w.herbivore.fill_(1.0)
    w.predator.zero_()
    apply(w)
    assert torch.allclose(w.predator, torch.full_like(w.predator, 0.004))

def test_logic_163():
    from world_rules.logic_163_prey_scarcity_reduces_predators import apply
    w = make_world()
    w.herbivore.zero_()
    w.predator.fill_(1.0)
    before=w.predator.clone()
    apply(w)
    assert torch.all(w.predator < before)

def test_logic_164():
    from world_rules.logic_164_vegetation_buffers_habitat_stress import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.habitat_stress.fill_(1.0)
    before=w.habitat_stress.clone()
    apply(w)
    assert torch.all(w.habitat_stress < before)

def test_logic_165():
    from world_rules.logic_165_overgrazing_reduces_vegetation import apply
    w = make_world()
    w.herbivore.fill_(1.0)
    w.vegetation.fill_(1.0)
    before=w.vegetation.clone()
    apply(w)
    assert torch.all(w.vegetation < before)

def test_logic_166():
    from world_rules.logic_166_predators_curb_herbivores import apply
    w = make_world()
    w.predator.fill_(1.0)
    w.herbivore.fill_(1.0)
    before=w.herbivore.clone()
    apply(w)
    assert torch.all(w.herbivore < before)

def test_logic_167():
    from world_rules.logic_167_carrion_feeds_detritus import apply
    w = make_world()
    w.carrion.fill_(1.0)
    w.detritus.zero_()
    apply(w)
    assert torch.allclose(w.detritus, torch.full_like(w.detritus, 0.005))

def test_logic_168():
    from world_rules.logic_168_detritus_supports_biodiversity import apply
    w = make_world()
    w.detritus.fill_(1.0)
    w.biodiversity.zero_()
    apply(w)
    assert torch.allclose(w.biodiversity, torch.full_like(w.biodiversity, 0.002))

def test_logic_169():
    from world_rules.logic_169_dry_vegetation_increases_fire_risk import apply
    w = make_world()
    w.vegetation.fill_(1.0)
    w.soil_moisture.zero_()
    w.fire_risk.zero_()
    apply(w)
    assert torch.allclose(w.fire_risk, torch.full_like(w.fire_risk, 0.008))

def test_logic_170():
    from world_rules.logic_170_humidity_suppresses_fire_risk import apply
    w = make_world()
    w.humidity.fill_(1.0)
    w.fire_risk.fill_(1.0)
    before=w.fire_risk.clone()
    apply(w)
    assert torch.all(w.fire_risk < before)

def test_logic_171():
    from world_rules.logic_171_rain_quenches_fire_risk import apply
    w = make_world()
    w.rain.fill_(1.0)
    w.fire_risk.fill_(1.0)
    before=w.fire_risk.clone()
    apply(w)
    assert torch.all(w.fire_risk < before)

def test_logic_172():
    from world_rules.logic_172_wet_soil_suppresses_fire_risk import apply
    w = make_world()
    w.soil_moisture.fill_(1.0)
    w.fire_risk.fill_(1.0)
    before=w.fire_risk.clone()
    apply(w)
    assert torch.all(w.fire_risk < before)

def test_logic_173():
    from world_rules.logic_173_wind_fans_fire_risk import apply
    w = make_world()
    w.wind_x.fill_(1.0)
    w.fire_risk.zero_()
    apply(w)
    assert torch.allclose(w.fire_risk, torch.full_like(w.fire_risk, 0.004))

def test_logic_174():
    from world_rules.logic_174_ash_suppresses_future_fire_risk import apply
    w = make_world()
    w.ash.fill_(1.0)
    w.fire_risk.fill_(1.0)
    before=w.fire_risk.clone()
    apply(w)
    assert torch.all(w.fire_risk < before)

def test_logic_175():
    from world_rules.logic_175_active_fire_warms_surface import apply
    w = make_world()
    w.fire_risk.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target > before)

def test_logic_176():
    from world_rules.logic_176_ash_reflects_heat import apply
    w = make_world()
    w.ash.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target < before)

def test_logic_177():
    from world_rules.logic_177_ash_fertilizes_vegetation import apply
    w = make_world()
    w.ash.fill_(1.0)
    w.vegetation.zero_()
    apply(w)
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.005))

def test_logic_178():
    from world_rules.logic_178_erosion_removes_nutrients import apply
    w = make_world()
    w.erosion.fill_(1.0)
    w.nutrients.fill_(1.0)
    before=w.nutrients.clone()
    apply(w)
    assert torch.all(w.nutrients < before)

def test_logic_179():
    from world_rules.logic_179_runoff_removes_carbon import apply
    w = make_world()
    w.runoff.fill_(1.0)
    w.carbon_storage.fill_(1.0)
    before=w.carbon_storage.clone()
    apply(w)
    assert torch.all(w.carbon_storage < before)

def test_logic_180():
    from world_rules.logic_180_deep_soil_preserves_carbon import apply
    w = make_world()
    w.soil_depth.fill_(1.0)
    w.carbon_storage.zero_()
    apply(w)
    assert torch.allclose(w.carbon_storage, torch.full_like(w.carbon_storage, 0.004))

def test_logic_181():
    from world_rules.logic_181_wetlands_store_carbon import apply
    w = make_world()
    w.wetland.fill_(1.0)
    w.carbon_storage.zero_()
    apply(w)
    assert torch.allclose(w.carbon_storage, torch.full_like(w.carbon_storage, 0.006))

def test_logic_182():
    from world_rules.logic_182_drought_reduces_biomass import apply
    w = make_world()
    w.soil_moisture.zero_()
    w.biomass.fill_(1.0)
    before=w.biomass.clone()
    apply(w)
    assert torch.all(w.biomass < before)

def test_logic_183():
    from world_rules.logic_183_water_abundance_supports_biomass import apply
    w = make_world()
    w.soil_moisture.fill_(1.0)
    w.biomass.zero_()
    apply(w)
    assert torch.allclose(w.biomass, torch.full_like(w.biomass, 0.004))

def test_logic_184():
    from world_rules.logic_184_habitat_stress_reduces_biomass import apply
    w = make_world()
    w.habitat_stress.fill_(1.0)
    w.biomass.fill_(1.0)
    before=w.biomass.clone()
    apply(w)
    assert torch.all(w.biomass < before)

def test_logic_185():
    from world_rules.logic_185_biodiversity_buffers_stress import apply
    w = make_world()
    w.biodiversity.fill_(1.0)
    w.habitat_stress.fill_(1.0)
    before=w.habitat_stress.clone()
    apply(w)
    assert torch.all(w.habitat_stress < before)

def test_logic_186():
    from world_rules.logic_186_detritus_supports_carrion_recovery import apply
    w = make_world()
    w.detritus.fill_(1.0)
    w.carrion.zero_()
    apply(w)
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.001))

def test_logic_187():
    from world_rules.logic_187_low_nutrients_raise_habitat_stress import apply
    w = make_world()
    w.nutrients.zero_()
    w.habitat_stress.zero_()
    apply(w)
    assert torch.allclose(w.habitat_stress, torch.full_like(w.habitat_stress, 0.003))

def test_logic_188():
    from world_rules.logic_188_high_nutrients_reduce_habitat_stress import apply
    w = make_world()
    w.nutrients.fill_(1.0)
    w.habitat_stress.fill_(1.0)
    before=w.habitat_stress.clone()
    apply(w)
    assert torch.all(w.habitat_stress < before)

def test_logic_189():
    from world_rules.logic_189_carbon_storage_reduces_temperature_target import apply
    w = make_world()
    w.carbon_storage.fill_(1.0)
    w.temperature_target.fill_(0.5)
    before=w.temperature_target.clone()
    apply(w)
    assert torch.all(w.temperature_target < before)

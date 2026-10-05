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


def test_logic_008():
    from world_rules.logic_008_clouds_produce_rain import apply
    w = make_world()
    w.cloud.fill_(0.8); apply(w);
    assert torch.allclose(w.rain, torch.full_like(w.rain, 0.08))


def test_logic_009():
    from world_rules.logic_009_rain_infiltrates_soil import apply
    w = make_world()
    w.soil_moisture.zero_(); w.rain.fill_(0.4); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.2))


def test_logic_010():
    from world_rules.logic_010_saturated_soil_generates_runoff import apply
    w = make_world()
    w.soil_moisture.fill_(1.0); apply(w);
    assert torch.allclose(w.runoff, torch.full_like(w.runoff, 0.04))


def test_logic_011():
    from world_rules.logic_011_lowlands_retain_runoff import apply
    w = make_world()
    w.surface_water.zero_(); w.runoff.fill_(0.5); w.elevation.fill_(0.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.05))


def test_logic_012():
    from world_rules.logic_012_low_elevation_pools_water import apply
    w = make_world()
    w.surface_water.zero_(); w.elevation.fill_(0.0); w.soil_moisture.fill_(1.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.01))


def test_logic_013():
    from world_rules.logic_013_rivers_add_base_water import apply
    w = make_world()
    w.surface_water.zero_(); w.biome.fill_(1); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.03))


def test_logic_014():
    from world_rules.logic_014_caves_retain_moisture import apply
    w = make_world()
    w.soil_moisture.zero_(); w.biome.fill_(4); w.surface_water.fill_(1.0); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.02))


def test_logic_015():
    from world_rules.logic_015_deserts_lose_surface_water_faster import apply
    w = make_world()
    w.surface_water.fill_(1.0); w.biome.fill_(3); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.995))


def test_logic_016():
    from world_rules.logic_016_humidity_slows_evaporation import apply
    w = make_world()
    w.surface_water.fill_(0.5); w.evaporation.fill_(0.1); w.humidity.fill_(1.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.54))


def test_logic_017():
    from world_rules.logic_017_wind_advects_humidity import apply
    w = make_world()
    w.humidity.zero_(); w.humidity[:,0]=1.0; apply(w);
    assert torch.all(w.humidity[:,1] > 0)


def test_logic_018():
    from world_rules.logic_018_terrain_gradient_drives_wind import apply
    w = make_world()
    w.wind_x.zero_(); w.wind_y.zero_(); w.elevation.zero_(); w.elevation[1,1]=1.0; apply(w);
    assert torch.any(w.wind_x != 0) and torch.any(w.wind_y != 0)


def test_logic_019():
    from world_rules.logic_019_wind_disperses_clouds import apply
    w = make_world()
    w.cloud.zero_(); w.cloud[1,1]=1.0; apply(w);
    assert torch.all(w.cloud >= 0) and w.cloud[1,0] > 0


def test_logic_020():
    from world_rules.logic_020_rain_dissipates_clouds import apply
    w = make_world()
    w.cloud.fill_(1.0); w.rain.fill_(1.0); apply(w);
    assert torch.allclose(w.cloud, torch.full_like(w.cloud, 0.9))


def test_logic_021():
    from world_rules.logic_021_warm_soil_dries import apply
    w = make_world()
    w.soil_moisture.fill_(1.0); w.temperature.fill_(1.0); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.99))


def test_logic_022():
    from world_rules.logic_022_wet_soil_cools_surface import apply
    w = make_world()
    w.temperature.fill_(0.5); w.soil_moisture.fill_(1.0); apply(w);
    assert torch.allclose(w.temperature, torch.full_like(w.temperature, 0.47))


def test_logic_023():
    from world_rules.logic_023_clouds_cool_surface import apply
    w = make_world()
    w.temperature.fill_(0.5); w.cloud.fill_(1.0); apply(w);
    assert torch.allclose(w.temperature, torch.full_like(w.temperature, 0.48))


def test_logic_024():
    from world_rules.logic_024_water_moderates_temperature import apply
    w = make_world()
    w.temperature.fill_(1.0); w.surface_water.fill_(1.0); apply(w);
    assert torch.allclose(w.temperature, torch.full_like(w.temperature, 0.995))


def test_logic_025():
    from world_rules.logic_025_cold_water_freezes import apply
    w = make_world()
    w.ice.zero_(); w.surface_water.fill_(1.0); w.temperature.fill_(0.0); apply(w);
    assert torch.allclose(w.ice, torch.full_like(w.ice, 0.05)) and torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.95))


def test_logic_026():
    from world_rules.logic_026_warm_air_melts_ice import apply
    w = make_world()
    w.surface_water.zero_(); w.ice.fill_(1.0); w.temperature.fill_(1.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.1))


def test_logic_027():
    from world_rules.logic_027_high_altitude_reduces_surface_water import apply
    w = make_world()
    w.surface_water.fill_(1.0); w.elevation.fill_(1.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.98))


def test_logic_028():
    from world_rules.logic_028_lowlands_retain_soil_moisture import apply
    w = make_world()
    w.soil_moisture.zero_(); w.elevation.zero_(); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.01))


def test_logic_029():
    from world_rules.logic_029_vegetation_improves_soil_retention import apply
    w = make_world()
    w.soil_moisture.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.02))


def test_logic_030():
    from world_rules.logic_030_soil_moisture_grows_vegetation import apply
    w = make_world()
    w.vegetation.zero_(); w.soil_moisture.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.03))


def test_logic_031():
    from world_rules.logic_031_drought_suppresses_vegetation import apply
    w = make_world()
    w.vegetation.fill_(0.5); w.soil_moisture.zero_(); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.495))


def test_logic_032():
    from world_rules.logic_032_vegetation_transpiration_adds_humidity import apply
    w = make_world()
    w.humidity.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.humidity, torch.full_like(w.humidity, 0.03))


def test_logic_033():
    from world_rules.logic_033_vegetation_reduces_ground_evaporation import apply
    w = make_world()
    w.surface_water.fill_(0.5); w.evaporation.fill_(0.1); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.surface_water, torch.full_like(w.surface_water, 0.55))


def test_logic_034():
    from world_rules.logic_034_roots_consume_soil_water import apply
    w = make_world()
    w.soil_moisture.fill_(1.0); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.soil_moisture, torch.full_like(w.soil_moisture, 0.99))


def test_logic_035():
    from world_rules.logic_035_biomass_follows_vegetation import apply
    w = make_world()
    w.biomass.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.biomass, torch.full_like(w.biomass, 0.05))


def test_logic_036():
    from world_rules.logic_036_herbivores_grow_from_vegetation import apply
    w = make_world()
    w.herbivore.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.herbivore, torch.full_like(w.herbivore, 0.02))


def test_logic_037():
    from world_rules.logic_037_predators_grow_from_herbivores import apply
    w = make_world()
    w.predator.zero_(); w.herbivore.fill_(1.0); apply(w);
    assert torch.allclose(w.predator, torch.full_like(w.predator, 0.015))


def test_logic_038():
    from world_rules.logic_038_low_herbivore_biomass_creates_carrion import apply
    w = make_world()
    w.carrion.zero_(); w.herbivore.zero_(); apply(w);
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.0025))


def test_logic_039():
    from world_rules.logic_039_decomposition_recycles_carrion import apply
    w = make_world()
    w.nutrients.zero_(); w.carrion.fill_(1.0); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.02))


def test_logic_040():
    from world_rules.logic_040_nutrients_support_vegetation import apply
    w = make_world()
    w.vegetation.zero_(); w.nutrients.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.015))


def test_logic_041():
    from world_rules.logic_041_rain_leaches_nutrients import apply
    w = make_world()
    w.nutrients.fill_(1.0); w.rain.fill_(1.0); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.98))


def test_logic_042():
    from world_rules.logic_042_dry_soil_locks_nutrients import apply
    w = make_world()
    w.nutrients.fill_(1.0); w.soil_moisture.zero_(); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.998))


def test_logic_043():
    from world_rules.logic_043_heat_accelerates_decomposition import apply
    w = make_world()
    w.temperature.fill_(1.0); w.carrion.fill_(1.0); apply(w);
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.96))


def test_logic_044():
    from world_rules.logic_044_cold_slows_decomposition import apply
    w = make_world()
    w.carrion.fill_(0.8); w.decomposition_rate.fill_(0.04); w.temperature.zero_(); apply(w);
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.9))


def test_logic_045():
    from world_rules.logic_045_vegetation_produces_oxygen import apply
    w = make_world()
    w.oxygen.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.oxygen, torch.full_like(w.oxygen, 0.02))


def test_logic_046():
    from world_rules.logic_046_respiration_consumes_oxygen import apply
    w = make_world()
    w.oxygen.fill_(1.0); w.biomass.fill_(1.0); w.herbivore.fill_(1.0); w.predator.fill_(1.0); apply(w);
    assert torch.allclose(w.oxygen, torch.full_like(w.oxygen, 0.97))


def test_logic_047():
    from world_rules.logic_047_respiration_adds_co2 import apply
    w = make_world()
    w.co2.zero_(); w.biomass.fill_(1.0); w.herbivore.fill_(1.0); w.predator.fill_(1.0); apply(w);
    assert torch.allclose(w.co2, torch.full_like(w.co2, 0.03))


def test_logic_048():
    from world_rules.logic_048_photosynthesis_consumes_co2 import apply
    w = make_world()
    w.co2.fill_(1.0); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.co2, torch.full_like(w.co2, 0.98))


def test_logic_049():
    from world_rules.logic_049_clouds_dampen_photosynthesis import apply
    w = make_world()
    w.cloud.fill_(1.0); apply(w);
    assert torch.allclose(w.photosynthesis_factor, torch.full_like(w.photosynthesis_factor, 0.8))


def test_logic_050():
    from world_rules.logic_050_co2_fertilizes_vegetation import apply
    w = make_world()
    w.vegetation.zero_(); w.co2.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.01))


def test_logic_051():
    from world_rules.logic_051_heat_stresses_vegetation import apply
    w = make_world()
    w.vegetation.fill_(1.0); w.temperature.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.996))


def test_logic_052():
    from world_rules.logic_052_humidity_supports_vegetation import apply
    w = make_world()
    w.vegetation.zero_(); w.humidity.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.01))


def test_logic_053():
    from world_rules.logic_053_dry_air_harms_vegetation import apply
    w = make_world()
    w.vegetation.fill_(0.5); w.humidity.zero_(); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.49625))


def test_logic_054():
    from world_rules.logic_054_soil_moisture_boosts_plant_growth import apply
    w = make_world()
    w.vegetation.zero_(); w.soil_moisture.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.02))


def test_logic_055():
    from world_rules.logic_055_river_biomes_buffer_plant_growth import apply
    w = make_world()
    w.vegetation.zero_(); w.biome.fill_(1); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.01))


def test_logic_056():
    from world_rules.logic_056_desert_biomes_cap_vegetation import apply
    w = make_world()
    w.biome.fill_(3); w.vegetation.fill_(1.0); w.soil_moisture.zero_(); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.15))


def test_logic_057():
    from world_rules.logic_057_steep_mountains_limit_vegetation import apply
    w = make_world()
    w.vegetation.fill_(1.0); w.elevation.zero_(); w.elevation[1,1]=1.0; apply(w);
    assert torch.any(w.vegetation < 1.0)


def test_logic_058():
    from world_rules.logic_058_caves_suppress_vegetation import apply
    w = make_world()
    w.vegetation.fill_(1.0); w.biome.fill_(4); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.7))


def test_logic_059():
    from world_rules.logic_059_vegetation_loss_creates_detritus import apply
    w = make_world()
    w.detritus.zero_(); w.biomass.fill_(1.0); w.vegetation.zero_(); apply(w);
    assert torch.allclose(w.detritus, torch.full_like(w.detritus, 0.01))


def test_logic_060():
    from world_rules.logic_060_decomposers_consume_detritus import apply
    w = make_world()
    w.nutrients.zero_(); w.detritus.fill_(1.0); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.03))


def test_logic_061():
    from world_rules.logic_061_nutrient_saturation_limits_growth import apply
    w = make_world()
    w.vegetation.fill_(1.0); w.nutrients.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.998))


def test_logic_062():
    from world_rules.logic_062_runoff_removes_nutrients import apply
    w = make_world()
    w.nutrients.fill_(1.0); w.runoff.fill_(1.0); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.95))


def test_logic_063():
    from world_rules.logic_063_low_oxygen_stresses_herbivores import apply
    w = make_world()
    w.herbivore.fill_(1.0); w.oxygen.zero_(); apply(w);
    assert torch.allclose(w.herbivore, torch.full_like(w.herbivore, 0.997))


def test_logic_064():
    from world_rules.logic_064_wet_anoxic_soil_produces_methane import apply
    w = make_world()
    w.methane.zero_(); w.soil_moisture.fill_(1.0); w.oxygen.zero_(); apply(w);
    assert torch.allclose(w.methane, torch.full_like(w.methane, 0.01))


def test_logic_065():
    from world_rules.logic_065_methane_warms_surface import apply
    w = make_world()
    w.temperature.fill_(0.5); w.methane.fill_(1.0); apply(w);
    assert torch.allclose(w.temperature, torch.full_like(w.temperature, 0.51))


def test_logic_066():
    from world_rules.logic_066_wind_mixes_gases import apply
    w = make_world()
    w.co2.zero_(); w.co2[1,1]=1.0; apply(w);
    assert w.co2[1,0] > 0


def test_logic_067():
    from world_rules.logic_067_co2_diffuses_across_grid import apply
    w = make_world()
    w.co2.zero_(); w.co2[1,1]=1.0; apply(w);
    assert w.co2[1,0] > 0


def test_logic_068():
    from world_rules.logic_068_oxygen_diffuses_across_grid import apply
    w = make_world()
    w.oxygen.zero_(); w.oxygen[1,1]=1.0; apply(w);
    assert w.oxygen[1,0] > 0


def test_logic_069():
    from world_rules.logic_069_wind_mixes_temperature import apply
    w = make_world()
    w.temperature.zero_(); w.temperature[1,1]=1.0; apply(w);
    assert w.temperature[1,0] > 0


def test_logic_070():
    from world_rules.logic_070_warmth_raises_pathogen_pressure import apply
    w = make_world()
    w.pathogen_load.zero_(); w.temperature.fill_(1.0); apply(w);
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.008))


def test_logic_071():
    from world_rules.logic_071_dryness_reduces_pathogen_survival import apply
    w = make_world()
    w.pathogen_load.fill_(1.0); w.soil_moisture.zero_(); apply(w);
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.988))


def test_logic_072():
    from world_rules.logic_072_rain_washes_pathogens import apply
    w = make_world()
    w.pathogen_load.fill_(1.0); w.rain.fill_(1.0); apply(w);
    assert torch.allclose(w.pathogen_load, torch.full_like(w.pathogen_load, 0.8))


def test_logic_073():
    from world_rules.logic_073_vegetation_raises_herbivore_carrying_capacity import apply
    w = make_world()
    w.herbivore.zero_(); w.vegetation.fill_(1.0); apply(w);
    assert torch.allclose(w.herbivore, torch.full_like(w.herbivore, 0.01))


def test_logic_074():
    from world_rules.logic_074_herbivory_reduces_vegetation import apply
    w = make_world()
    w.vegetation.fill_(1.0); w.herbivore.fill_(1.0); apply(w);
    assert torch.allclose(w.vegetation, torch.full_like(w.vegetation, 0.99))


def test_logic_075():
    from world_rules.logic_075_vegetation_scarcity_reduces_herbivores import apply
    w = make_world()
    w.herbivore.fill_(1.0); w.vegetation.zero_(); apply(w);
    assert torch.allclose(w.herbivore, torch.full_like(w.herbivore, 0.998))


def test_logic_076():
    from world_rules.logic_076_predation_reduces_herbivores import apply
    w = make_world()
    w.herbivore.fill_(1.0); w.predator.fill_(1.0); apply(w);
    assert torch.allclose(w.herbivore, torch.full_like(w.herbivore, 0.99))


def test_logic_077():
    from world_rules.logic_077_prey_scarcity_reduces_predators import apply
    w = make_world()
    w.predator.fill_(1.0); w.herbivore.zero_(); apply(w);
    assert torch.allclose(w.predator, torch.full_like(w.predator, 0.996))


def test_logic_078():
    from world_rules.logic_078_predation_creates_carrion import apply
    w = make_world()
    w.carrion.zero_(); w.predator.fill_(1.0); apply(w);
    assert torch.allclose(w.carrion, torch.full_like(w.carrion, 0.006))


def test_logic_079():
    from world_rules.logic_079_carrion_boosts_nutrients import apply
    w = make_world()
    w.nutrients.zero_(); w.carrion.fill_(1.0); apply(w);
    assert torch.allclose(w.nutrients, torch.full_like(w.nutrients, 0.01))


def test_logic_080():
    from world_rules.logic_080_habitat_heterogeneity_raises_biodiversity import apply
    w = make_world()
    w.biodiversity.zero_(); w.temperature.zero_(); w.temperature[:,0]=1.0; apply(w);
    assert torch.any(w.biodiversity > 0)


def test_logic_081():
    from world_rules.logic_081_thermal_extremes_raise_habitat_stress import apply
    w = make_world()
    w.habitat_stress.zero_(); w.temperature.fill_(1.0); apply(w);
    assert torch.allclose(w.habitat_stress, torch.full_like(w.habitat_stress, 0.01))


def test_logic_082():
    from world_rules.logic_082_water_scarcity_raises_stress import apply
    w = make_world()
    w.habitat_stress.zero_(); w.surface_water.zero_(); apply(w);
    assert torch.allclose(w.habitat_stress, torch.full_like(w.habitat_stress, 0.006))


def test_logic_083():
    from world_rules.logic_083_food_scarcity_raises_stress import apply
    w = make_world()
    w.habitat_stress.zero_(); w.vegetation.zero_(); apply(w);
    assert torch.allclose(w.habitat_stress, torch.full_like(w.habitat_stress, 0.004))

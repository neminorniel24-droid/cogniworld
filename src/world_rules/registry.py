RULES = []
from .logic_002_elevation_sets_thermal_target import apply as logic_002
RULES.append(logic_002)
from .logic_003_thermal_inertia import apply as logic_003
RULES.append(logic_003)
from .logic_004_heat_increases_evaporation_potential import apply as logic_004
RULES.append(logic_004)
from .logic_005_evaporation_removes_surface_water import apply as logic_005
RULES.append(logic_005)
from .logic_006_evaporation_raises_humidity import apply as logic_006
RULES.append(logic_006)
from .logic_007_humidity_condenses_clouds import apply as logic_007
RULES.append(logic_007)
from .logic_008_clouds_produce_rain import apply as logic_008
RULES.append(logic_008)
from .logic_009_rain_infiltrates_soil import apply as logic_009
RULES.append(logic_009)
from .logic_010_saturated_soil_generates_runoff import apply as logic_010
RULES.append(logic_010)
from .logic_011_lowlands_retain_runoff import apply as logic_011
RULES.append(logic_011)
from .logic_012_low_elevation_pools_water import apply as logic_012
RULES.append(logic_012)
from .logic_013_rivers_add_base_water import apply as logic_013
RULES.append(logic_013)
from .logic_014_caves_retain_moisture import apply as logic_014
RULES.append(logic_014)
from .logic_015_deserts_lose_surface_water_faster import apply as logic_015
RULES.append(logic_015)
from .logic_016_humidity_slows_evaporation import apply as logic_016
RULES.append(logic_016)
from .logic_017_wind_advects_humidity import apply as logic_017
RULES.append(logic_017)
from .logic_018_terrain_gradient_drives_wind import apply as logic_018
RULES.append(logic_018)
from .logic_019_wind_disperses_clouds import apply as logic_019
RULES.append(logic_019)
from .logic_020_rain_dissipates_clouds import apply as logic_020
RULES.append(logic_020)
from .logic_021_warm_soil_dries import apply as logic_021
RULES.append(logic_021)
from .logic_022_wet_soil_cools_surface import apply as logic_022
RULES.append(logic_022)
from .logic_023_clouds_cool_surface import apply as logic_023
RULES.append(logic_023)
from .logic_024_water_moderates_temperature import apply as logic_024
RULES.append(logic_024)
from .logic_025_cold_water_freezes import apply as logic_025
RULES.append(logic_025)
from .logic_026_warm_air_melts_ice import apply as logic_026
RULES.append(logic_026)
from .logic_027_high_altitude_reduces_surface_water import apply as logic_027
RULES.append(logic_027)
from .logic_028_lowlands_retain_soil_moisture import apply as logic_028
RULES.append(logic_028)
from .logic_029_vegetation_improves_soil_retention import apply as logic_029
RULES.append(logic_029)
from .logic_030_soil_moisture_grows_vegetation import apply as logic_030
RULES.append(logic_030)
from .logic_031_drought_suppresses_vegetation import apply as logic_031
RULES.append(logic_031)
from .logic_032_vegetation_transpiration_adds_humidity import apply as logic_032
RULES.append(logic_032)
from .logic_033_vegetation_reduces_ground_evaporation import apply as logic_033
RULES.append(logic_033)
from .logic_034_roots_consume_soil_water import apply as logic_034
RULES.append(logic_034)
from .logic_035_biomass_follows_vegetation import apply as logic_035
RULES.append(logic_035)
from .logic_036_herbivores_grow_from_vegetation import apply as logic_036
RULES.append(logic_036)
from .logic_037_predators_grow_from_herbivores import apply as logic_037
RULES.append(logic_037)
from .logic_038_low_herbivore_biomass_creates_carrion import apply as logic_038
RULES.append(logic_038)
from .logic_039_decomposition_recycles_carrion import apply as logic_039
RULES.append(logic_039)
from .logic_040_nutrients_support_vegetation import apply as logic_040
RULES.append(logic_040)
from .logic_041_rain_leaches_nutrients import apply as logic_041
RULES.append(logic_041)
from .logic_042_dry_soil_locks_nutrients import apply as logic_042
RULES.append(logic_042)
from .logic_043_heat_accelerates_decomposition import apply as logic_043
RULES.append(logic_043)
from .logic_044_cold_slows_decomposition import apply as logic_044
RULES.append(logic_044)
from .logic_045_vegetation_produces_oxygen import apply as logic_045
RULES.append(logic_045)
from .logic_046_respiration_consumes_oxygen import apply as logic_046
RULES.append(logic_046)
from .logic_047_respiration_adds_co2 import apply as logic_047
RULES.append(logic_047)
from .logic_048_photosynthesis_consumes_co2 import apply as logic_048
RULES.append(logic_048)
from .logic_049_clouds_dampen_photosynthesis import apply as logic_049
RULES.append(logic_049)
from .logic_050_co2_fertilizes_vegetation import apply as logic_050
RULES.append(logic_050)
from .logic_051_heat_stresses_vegetation import apply as logic_051
RULES.append(logic_051)
from .logic_052_humidity_supports_vegetation import apply as logic_052
RULES.append(logic_052)
from .logic_053_dry_air_harms_vegetation import apply as logic_053
RULES.append(logic_053)
from .logic_054_soil_moisture_boosts_plant_growth import apply as logic_054
RULES.append(logic_054)
from .logic_055_river_biomes_buffer_plant_growth import apply as logic_055
RULES.append(logic_055)
from .logic_056_desert_biomes_cap_vegetation import apply as logic_056
RULES.append(logic_056)
from .logic_057_steep_mountains_limit_vegetation import apply as logic_057
RULES.append(logic_057)
from .logic_058_caves_suppress_vegetation import apply as logic_058
RULES.append(logic_058)
from .logic_059_vegetation_loss_creates_detritus import apply as logic_059
RULES.append(logic_059)
from .logic_060_decomposers_consume_detritus import apply as logic_060
RULES.append(logic_060)
from .logic_061_nutrient_saturation_limits_growth import apply as logic_061
RULES.append(logic_061)
from .logic_062_runoff_removes_nutrients import apply as logic_062
RULES.append(logic_062)
from .logic_063_low_oxygen_stresses_herbivores import apply as logic_063
RULES.append(logic_063)
from .logic_064_wet_anoxic_soil_produces_methane import apply as logic_064
RULES.append(logic_064)
from .logic_065_methane_warms_surface import apply as logic_065
RULES.append(logic_065)
from .logic_066_wind_mixes_gases import apply as logic_066
RULES.append(logic_066)
from .logic_067_co2_diffuses_across_grid import apply as logic_067
RULES.append(logic_067)
from .logic_068_oxygen_diffuses_across_grid import apply as logic_068
RULES.append(logic_068)
from .logic_069_wind_mixes_temperature import apply as logic_069
RULES.append(logic_069)
from .logic_070_warmth_raises_pathogen_pressure import apply as logic_070
RULES.append(logic_070)
from .logic_071_dryness_reduces_pathogen_survival import apply as logic_071
RULES.append(logic_071)
from .logic_072_rain_washes_pathogens import apply as logic_072
RULES.append(logic_072)
from .logic_073_vegetation_raises_herbivore_carrying_capacity import apply as logic_073
RULES.append(logic_073)
from .logic_074_herbivory_reduces_vegetation import apply as logic_074
RULES.append(logic_074)
from .logic_075_vegetation_scarcity_reduces_herbivores import apply as logic_075
RULES.append(logic_075)
from .logic_076_predation_reduces_herbivores import apply as logic_076
RULES.append(logic_076)
from .logic_077_prey_scarcity_reduces_predators import apply as logic_077
RULES.append(logic_077)
from .logic_078_predation_creates_carrion import apply as logic_078
RULES.append(logic_078)
from .logic_079_carrion_boosts_nutrients import apply as logic_079
RULES.append(logic_079)
from .logic_080_habitat_heterogeneity_raises_biodiversity import apply as logic_080
RULES.append(logic_080)
from .logic_081_thermal_extremes_raise_habitat_stress import apply as logic_081
RULES.append(logic_081)
from .logic_082_water_scarcity_raises_stress import apply as logic_082
RULES.append(logic_082)
from .logic_083_food_scarcity_raises_stress import apply as logic_083
RULES.append(logic_083)
from .logic_084_stress_reduces_vegetation import apply as logic_084
RULES.append(logic_084)
from .logic_085_stable_climate_reduces_stress import apply as logic_085
RULES.append(logic_085)
from .logic_086_storm_runoff_erodes_soil import apply as logic_086
RULES.append(logic_086)
from .logic_087_erosion_reduces_soil_depth import apply as logic_087
RULES.append(logic_087)
from .logic_088_shallow_soil_limits_vegetation import apply as logic_088
RULES.append(logic_088)
from .logic_089_deep_soil_stores_more_water import apply as logic_089
RULES.append(logic_089)
from .logic_090_high_wind_increases_erosion import apply as logic_090
RULES.append(logic_090)
from .logic_091_vegetation_prevents_erosion import apply as logic_091
RULES.append(logic_091)
from .logic_092_roots_improve_infiltration import apply as logic_092
RULES.append(logic_092)
from .logic_093_root_density_follows_vegetation import apply as logic_093
RULES.append(logic_093)
from .logic_094_canopy_reduces_runoff import apply as logic_094
RULES.append(logic_094)
from .logic_095_wetlands_retain_water import apply as logic_095
RULES.append(logic_095)
from .logic_096_wetlands_produce_methane import apply as logic_096
RULES.append(logic_096)
from .logic_097_carbon_storage_follows_biomass import apply as logic_097
RULES.append(logic_097)
from .logic_098_drought_releases_stored_carbon import apply as logic_098
RULES.append(logic_098)
from .logic_099_dry_biomass_raises_fire_risk import apply as logic_099
RULES.append(logic_099)
from .logic_100_fire_consumes_vegetation_and_creates_ash import apply as logic_100
RULES.append(logic_100)
from .logic_101_ash_returns_nutrients import apply as logic_101
RULES.append(logic_101)
from .logic_102_vegetation_shades_surface import apply as logic_102
RULES.append(logic_102)
from .logic_103_bare_soil_absorbs_more_heat import apply as logic_103
RULES.append(logic_103)
from .logic_104_ice_reflects_solar_energy import apply as logic_104
RULES.append(logic_104)
from .logic_105_methane_adds_greenhouse_warming import apply as logic_105
RULES.append(logic_105)
from .logic_106_co2_adds_greenhouse_warming import apply as logic_106
RULES.append(logic_106)
from .logic_107_humidity_adds_water_vapor_warming import apply as logic_107
RULES.append(logic_107)
from .logic_108_clouds_add_greenhouse_warming import apply as logic_108
RULES.append(logic_108)
from .logic_109_wind_increases_evaporation import apply as logic_109
RULES.append(logic_109)
from .logic_110_dry_air_increases_evaporation import apply as logic_110
RULES.append(logic_110)
from .logic_111_ice_suppresses_evaporation import apply as logic_111
RULES.append(logic_111)
from .logic_112_surface_water_recharges_soil import apply as logic_112
RULES.append(logic_112)
from .logic_113_rain_adds_surface_water import apply as logic_113
RULES.append(logic_113)
from .logic_114_runoff_adds_surface_water import apply as logic_114
RULES.append(logic_114)
from .logic_115_deep_soil_retains_more_moisture import apply as logic_115
RULES.append(logic_115)
from .logic_116_shallow_soil_drains_faster import apply as logic_116
RULES.append(logic_116)
from .logic_117_roots_reduce_erosion import apply as logic_117
RULES.append(logic_117)
from .logic_118_canopy_intercepts_rain import apply as logic_118
RULES.append(logic_118)
from .logic_119_wetlands_reduce_runoff import apply as logic_119
RULES.append(logic_119)
from .logic_120_wetlands_store_rainfall import apply as logic_120
RULES.append(logic_120)
from .logic_121_waterlogging_reduces_soil_oxygen import apply as logic_121
RULES.append(logic_121)
from .logic_122_wind_reoxygenates_surface import apply as logic_122
RULES.append(logic_122)
from .logic_123_vegetation_transpiration_drains_soil import apply as logic_123
RULES.append(logic_123)
from .logic_124_humid_air_reduces_transpiration_loss import apply as logic_124
RULES.append(logic_124)
from .logic_125_cloud_cover_limits_photosynthesis import apply as logic_125
RULES.append(logic_125)
from .logic_126_nutrients_raise_photosynthesis_factor import apply as logic_126
RULES.append(logic_126)
from .logic_127_nutrient_scarcity_slows_vegetation import apply as logic_127
RULES.append(logic_127)
from .logic_128_co2_enrichment_grows_vegetation import apply as logic_128
RULES.append(logic_128)
from .logic_129_temperature_extremes_suppress_vegetation import apply as logic_129
RULES.append(logic_129)
from .logic_130_moderate_temperature_supports_vegetation import apply as logic_130
RULES.append(logic_130)
from .logic_131_oxygen_supports_decomposition import apply as logic_131
RULES.append(logic_131)
from .logic_132_detritus_feeds_decomposition import apply as logic_132
RULES.append(logic_132)
from .logic_133_cold_slows_decomposition import apply as logic_133
RULES.append(logic_133)
from .logic_134_wet_soil_accelerates_decomposition import apply as logic_134
RULES.append(logic_134)
from .logic_135_decomposition_consumes_detritus import apply as logic_135
RULES.append(logic_135)
from .logic_136_decomposition_recycles_nutrients import apply as logic_136
RULES.append(logic_136)
from .logic_137_decomposition_releases_co2 import apply as logic_137
RULES.append(logic_137)
from .logic_138_decomposition_consumes_oxygen import apply as logic_138
RULES.append(logic_138)
from .logic_139_oxygen_oxidizes_methane import apply as logic_139
RULES.append(logic_139)
from .logic_140_dry_soil_reduces_methane import apply as logic_140
RULES.append(logic_140)
from .logic_141_drought_releases_carbon import apply as logic_141
RULES.append(logic_141)
from .logic_142_biomass_builds_carbon_storage import apply as logic_142
RULES.append(logic_142)
from .logic_143_biomass_produces_oxygen import apply as logic_143
RULES.append(logic_143)
from .logic_144_herbivory_reduces_biomass import apply as logic_144
RULES.append(logic_144)
from .logic_145_grazing_creates_detritus import apply as logic_145
RULES.append(logic_145)
from .logic_146_predation_creates_carrion import apply as logic_146
RULES.append(logic_146)
from .logic_147_carrion_decomposition_adds_decomposition import apply as logic_147
RULES.append(logic_147)
from .logic_148_vegetation_raises_biodiversity import apply as logic_148
RULES.append(logic_148)
from .logic_149_balanced_food_web_raises_biodiversity import apply as logic_149
RULES.append(logic_149)
from .logic_150_habitat_stress_reduces_biodiversity import apply as logic_150
RULES.append(logic_150)
from .logic_151_biodiversity_suppresses_pathogens import apply as logic_151
RULES.append(logic_151)
from .logic_152_habitat_stress_increases_pathogens import apply as logic_152
RULES.append(logic_152)
from .logic_153_wet_soil_supports_pathogen_survival import apply as logic_153
RULES.append(logic_153)
from .logic_154_dryness_suppresses_pathogens import apply as logic_154
RULES.append(logic_154)
from .logic_155_warmth_increases_pathogen_growth import apply as logic_155
RULES.append(logic_155)
from .logic_156_cold_reduces_pathogens import apply as logic_156
RULES.append(logic_156)
from .logic_157_rain_washes_pathogens import apply as logic_157
RULES.append(logic_157)
from .logic_158_vegetation_shelters_pathogens import apply as logic_158
RULES.append(logic_158)
from .logic_159_pathogens_raise_habitat_stress import apply as logic_159
RULES.append(logic_159)
from .logic_160_low_oxygen_reduces_herbivores import apply as logic_160
RULES.append(logic_160)
from .logic_161_oxygen_supports_predators import apply as logic_161
RULES.append(logic_161)
from .logic_162_prey_abundance_supports_predators import apply as logic_162
RULES.append(logic_162)
from .logic_163_prey_scarcity_reduces_predators import apply as logic_163
RULES.append(logic_163)
from .logic_164_vegetation_buffers_habitat_stress import apply as logic_164
RULES.append(logic_164)
from .logic_165_overgrazing_reduces_vegetation import apply as logic_165
RULES.append(logic_165)
from .logic_166_predators_curb_herbivores import apply as logic_166
RULES.append(logic_166)
from .logic_167_carrion_feeds_detritus import apply as logic_167
RULES.append(logic_167)
from .logic_168_detritus_supports_biodiversity import apply as logic_168
RULES.append(logic_168)
from .logic_169_dry_vegetation_increases_fire_risk import apply as logic_169
RULES.append(logic_169)
from .logic_170_humidity_suppresses_fire_risk import apply as logic_170
RULES.append(logic_170)
from .logic_171_rain_quenches_fire_risk import apply as logic_171
RULES.append(logic_171)
from .logic_172_wet_soil_suppresses_fire_risk import apply as logic_172
RULES.append(logic_172)

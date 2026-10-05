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

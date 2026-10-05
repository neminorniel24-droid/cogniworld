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

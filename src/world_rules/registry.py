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

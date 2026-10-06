import torch
from types import SimpleNamespace

def make_world(size=3):
    z=lambda v=0.0: torch.full((size,size), v, dtype=torch.float32)
    w=SimpleNamespace()
    w.elevation=z(0.5); w.biome=torch.zeros((size,size),dtype=torch.int64)
    w.temperature=z(0.5); w.temperature_target=z(0.5)
    for n in ["surface_water","humidity","cloud","rain","soil_moisture","runoff","wind_x","wind_y","vegetation","biomass","herbivore","predator","carrion","nutrients","decomposition_rate","oxygen","co2","photosynthesis_factor","ice","evaporation","detritus","methane","pathogen_load","biodiversity","habitat_stress","erosion","soil_depth","root_density","wetland","carbon_storage","fire_risk","ash"]:
        setattr(w,n,z(0.0 if n not in {"soil_depth","photosynthesis_factor"} else (1.0 if n=="soil_depth" else 1.0)))
    w.snowpack=z(0.0)
    w.groundwater=z(0.0)
    w.sediment=z(0.0)
    w.salinity=z(0.0)
    w.algae=z(0.0)
    w.organic_matter=z(0.0)
    w.deadwood=z(0.0)
    w.pollinators=z(0.0)
    w.flowers=z(0.0)
    w.seed_bank=z(0.0)
    w.soil_carbon=z(0.0)
    return w

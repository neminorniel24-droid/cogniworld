import torch

def apply(world):
    burn=(0.02*world.fire_risk).clamp(0.0,0.02); world.vegetation=(world.vegetation-burn).clamp(0.0,1.0); world.biomass=(world.biomass-burn).clamp(0.0,1.0); world.ash=(world.ash+0.5*burn).clamp(0.0,1.0); world.fire_risk*=0.95

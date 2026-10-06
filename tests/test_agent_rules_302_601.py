import torch
from genome.agents import Agents
class W:pass
def world():
 w=W();fs="surface_water groundwater soil_moisture rain snowpack temperature humidity wind_x vegetation biomass herbivore predator carrion nutrients oxygen pathogen_load biodiversity habitat_stress erosion soil_depth root_density wetland carbon_storage fire_risk ash surface_ice organic_matter deadwood pollinators flowers seed_bank soil_carbon salinity algae sediment runoff cloud evaporation methane co2".split();[setattr(w,f,torch.full((4,4),.5)) for f in fs];return w
def test_0302():
 a=Agents(2,4,100,torch.device("cpu"));assert a.hydration.shape==(2,)


def test_logic_303():
 from agent_rules.rules import logic_303
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'surface_water',torch.ones(4,4));logic_303(a,w);assert torch.any(a.hydration!=b)

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


def test_logic_304():
 from agent_rules.rules import logic_304
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thirst.clone();setattr(w,'surface_water',torch.ones(4,4));logic_304(a,w);assert torch.any(a.thirst!=b)


def test_logic_305():
 from agent_rules.rules import logic_305
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'surface_water',torch.ones(4,4));logic_305(a,w);assert torch.any(a.health!=b)


def test_logic_306():
 from agent_rules.rules import logic_306
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'groundwater',torch.ones(4,4));logic_306(a,w);assert torch.any(a.hydration!=b)


def test_logic_307():
 from agent_rules.rules import logic_307
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thirst.clone();setattr(w,'groundwater',torch.ones(4,4));logic_307(a,w);assert torch.any(a.thirst!=b)


def test_logic_308():
 from agent_rules.rules import logic_308
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'groundwater',torch.ones(4,4));logic_308(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_309():
 from agent_rules.rules import logic_309
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'soil_moisture',torch.ones(4,4));logic_309(a,w);assert torch.any(a.hydration!=b)


def test_logic_310():
 from agent_rules.rules import logic_310
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'soil_moisture',torch.ones(4,4));logic_310(a,w);assert torch.any(a.hunger!=b)


def test_logic_311():
 from agent_rules.rules import logic_311
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.reproduction_drive.clone();setattr(w,'soil_moisture',torch.ones(4,4));logic_311(a,w);assert torch.any(a.reproduction_drive!=b)


def test_logic_312():
 from agent_rules.rules import logic_312
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'rain',torch.ones(4,4));logic_312(a,w);assert torch.any(a.hydration!=b)


def test_logic_313():
 from agent_rules.rules import logic_313
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'rain',torch.ones(4,4));logic_313(a,w);assert torch.any(a.health!=b)

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


def test_logic_314():
 from agent_rules.rules import logic_314
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'rain',torch.ones(4,4));logic_314(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_315():
 from agent_rules.rules import logic_315
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'snowpack',torch.ones(4,4));logic_315(a,w);assert torch.any(a.hydration!=b)


def test_logic_316():
 from agent_rules.rules import logic_316
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thermal_stress.clone();setattr(w,'snowpack',torch.ones(4,4));logic_316(a,w);assert torch.any(a.thermal_stress!=b)


def test_logic_317():
 from agent_rules.rules import logic_317
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.pathogen_risk.clone();setattr(w,'snowpack',torch.ones(4,4));logic_317(a,w);assert torch.any(a.pathogen_risk!=b)


def test_logic_318():
 from agent_rules.rules import logic_318
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thermal_stress.clone();setattr(w,'temperature',torch.ones(4,4));logic_318(a,w);assert torch.any(a.thermal_stress!=b)


def test_logic_319():
 from agent_rules.rules import logic_319
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.dehydration.clone();setattr(w,'temperature',torch.ones(4,4));logic_319(a,w);assert torch.any(a.dehydration!=b)


def test_logic_320():
 from agent_rules.rules import logic_320
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.reproduction_drive.clone();setattr(w,'temperature',torch.ones(4,4));logic_320(a,w);assert torch.any(a.reproduction_drive!=b)


def test_logic_321():
 from agent_rules.rules import logic_321
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.dehydration.clone();setattr(w,'humidity',torch.ones(4,4));logic_321(a,w);assert torch.any(a.dehydration!=b)


def test_logic_322():
 from agent_rules.rules import logic_322
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thermal_stress.clone();setattr(w,'humidity',torch.ones(4,4));logic_322(a,w);assert torch.any(a.thermal_stress!=b)


def test_logic_323():
 from agent_rules.rules import logic_323
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.pathogen_risk.clone();setattr(w,'humidity',torch.ones(4,4));logic_323(a,w);assert torch.any(a.pathogen_risk!=b)


def test_logic_324():
 from agent_rules.rules import logic_324
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.dehydration.clone();setattr(w,'wind_x',torch.ones(4,4));logic_324(a,w);assert torch.any(a.dehydration!=b)


def test_logic_325():
 from agent_rules.rules import logic_325
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.thermal_stress.clone();setattr(w,'wind_x',torch.ones(4,4));logic_325(a,w);assert torch.any(a.thermal_stress!=b)


def test_logic_326():
 from agent_rules.rules import logic_326
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.exploration_drive.clone();setattr(w,'wind_x',torch.ones(4,4));logic_326(a,w);assert torch.any(a.exploration_drive!=b)


def test_logic_327():
 from agent_rules.rules import logic_327
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'vegetation',torch.ones(4,4));logic_327(a,w);assert torch.any(a.hunger!=b)


def test_logic_328():
 from agent_rules.rules import logic_328
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'vegetation',torch.ones(4,4));logic_328(a,w);assert torch.any(a.health!=b)


def test_logic_329():
 from agent_rules.rules import logic_329
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.reproduction_drive.clone();setattr(w,'vegetation',torch.ones(4,4));logic_329(a,w);assert torch.any(a.reproduction_drive!=b)


def test_logic_330():
 from agent_rules.rules import logic_330
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'biomass',torch.ones(4,4));logic_330(a,w);assert torch.any(a.hunger!=b)


def test_logic_331():
 from agent_rules.rules import logic_331
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'biomass',torch.ones(4,4));logic_331(a,w);assert torch.any(a.health!=b)


def test_logic_332():
 from agent_rules.rules import logic_332
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.wealth.clone();setattr(w,'biomass',torch.ones(4,4));logic_332(a,w);assert torch.any(a.wealth!=b)


def test_logic_333():
 from agent_rules.rules import logic_333
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.competition_pressure.clone();setattr(w,'herbivore',torch.ones(4,4));logic_333(a,w);assert torch.any(a.competition_pressure!=b)


def test_logic_334():
 from agent_rules.rules import logic_334
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.alertness.clone();setattr(w,'herbivore',torch.ones(4,4));logic_334(a,w);assert torch.any(a.alertness!=b)


def test_logic_335():
 from agent_rules.rules import logic_335
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'herbivore',torch.ones(4,4));logic_335(a,w);assert torch.any(a.hunger!=b)


def test_logic_336():
 from agent_rules.rules import logic_336
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.alertness.clone();setattr(w,'predator',torch.ones(4,4));logic_336(a,w);assert torch.any(a.alertness!=b)


def test_logic_337():
 from agent_rules.rules import logic_337
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.fear.clone();setattr(w,'predator',torch.ones(4,4));logic_337(a,w);assert torch.any(a.fear!=b)

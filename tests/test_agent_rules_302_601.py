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


def test_logic_338():
 from agent_rules.rules import logic_338
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'predator',torch.ones(4,4));logic_338(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_339():
 from agent_rules.rules import logic_339
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'carrion',torch.ones(4,4));logic_339(a,w);assert torch.any(a.hunger!=b)


def test_logic_340():
 from agent_rules.rules import logic_340
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'carrion',torch.ones(4,4));logic_340(a,w);assert torch.any(a.health!=b)


def test_logic_341():
 from agent_rules.rules import logic_341
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.pathogen_risk.clone();setattr(w,'carrion',torch.ones(4,4));logic_341(a,w);assert torch.any(a.pathogen_risk!=b)


def test_logic_342():
 from agent_rules.rules import logic_342
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'nutrients',torch.ones(4,4));logic_342(a,w);assert torch.any(a.hunger!=b)


def test_logic_343():
 from agent_rules.rules import logic_343
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'nutrients',torch.ones(4,4));logic_343(a,w);assert torch.any(a.health!=b)


def test_logic_344():
 from agent_rules.rules import logic_344
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.reproduction_drive.clone();setattr(w,'nutrients',torch.ones(4,4));logic_344(a,w);assert torch.any(a.reproduction_drive!=b)


def test_logic_345():
 from agent_rules.rules import logic_345
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'oxygen',torch.ones(4,4));logic_345(a,w);assert torch.any(a.health!=b)


def test_logic_346():
 from agent_rules.rules import logic_346
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.metabolic_cost.clone();setattr(w,'oxygen',torch.ones(4,4));logic_346(a,w);assert torch.any(a.metabolic_cost!=b)


def test_logic_347():
 from agent_rules.rules import logic_347
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.recovery.clone();setattr(w,'oxygen',torch.ones(4,4));logic_347(a,w);assert torch.any(a.recovery!=b)


def test_logic_348():
 from agent_rules.rules import logic_348
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'pathogen_load',torch.ones(4,4));logic_348(a,w);assert torch.any(a.health!=b)


def test_logic_349():
 from agent_rules.rules import logic_349
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.infection_risk.clone();setattr(w,'pathogen_load',torch.ones(4,4));logic_349(a,w);assert torch.any(a.infection_risk!=b)


def test_logic_350():
 from agent_rules.rules import logic_350
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.social_avoidance.clone();setattr(w,'pathogen_load',torch.ones(4,4));logic_350(a,w);assert torch.any(a.social_avoidance!=b)


def test_logic_351():
 from agent_rules.rules import logic_351
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'biodiversity',torch.ones(4,4));logic_351(a,w);assert torch.any(a.health!=b)


def test_logic_352():
 from agent_rules.rules import logic_352
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.habitat_stress.clone();setattr(w,'biodiversity',torch.ones(4,4));logic_352(a,w);assert torch.any(a.habitat_stress!=b)


def test_logic_353():
 from agent_rules.rules import logic_353
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.fear.clone();setattr(w,'biodiversity',torch.ones(4,4));logic_353(a,w);assert torch.any(a.fear!=b)


def test_logic_354():
 from agent_rules.rules import logic_354
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'habitat_stress',torch.ones(4,4));logic_354(a,w);assert torch.any(a.health!=b)


def test_logic_355():
 from agent_rules.rules import logic_355
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.fear.clone();setattr(w,'habitat_stress',torch.ones(4,4));logic_355(a,w);assert torch.any(a.fear!=b)


def test_logic_356():
 from agent_rules.rules import logic_356
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'habitat_stress',torch.ones(4,4));logic_356(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_357():
 from agent_rules.rules import logic_357
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.stability.clone();setattr(w,'erosion',torch.ones(4,4));logic_357(a,w);assert torch.any(a.stability!=b)


def test_logic_358():
 from agent_rules.rules import logic_358
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'erosion',torch.ones(4,4));logic_358(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_359():
 from agent_rules.rules import logic_359
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'erosion',torch.ones(4,4));logic_359(a,w);assert torch.any(a.health!=b)


def test_logic_360():
 from agent_rules.rules import logic_360
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.migration_drive.clone();setattr(w,'soil_depth',torch.ones(4,4));logic_360(a,w);assert torch.any(a.migration_drive!=b)


def test_logic_361():
 from agent_rules.rules import logic_361
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.health.clone();setattr(w,'soil_depth',torch.ones(4,4));logic_361(a,w);assert torch.any(a.health!=b)


def test_logic_362():
 from agent_rules.rules import logic_362
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hunger.clone();setattr(w,'soil_depth',torch.ones(4,4));logic_362(a,w);assert torch.any(a.hunger!=b)


def test_logic_363():
 from agent_rules.rules import logic_363
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.food_access.clone();setattr(w,'root_density',torch.ones(4,4));logic_363(a,w);assert torch.any(a.food_access!=b)


def test_logic_364():
 from agent_rules.rules import logic_364
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.stability.clone();setattr(w,'root_density',torch.ones(4,4));logic_364(a,w);assert torch.any(a.stability!=b)


def test_logic_365():
 from agent_rules.rules import logic_365
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.shelter_need.clone();setattr(w,'root_density',torch.ones(4,4));logic_365(a,w);assert torch.any(a.shelter_need!=b)


def test_logic_366():
 from agent_rules.rules import logic_366
 a=Agents(2,4,100,torch.device("cpu"));w=world();b=a.hydration.clone();setattr(w,'wetland',torch.ones(4,4));logic_366(a,w);assert torch.any(a.hydration!=b)

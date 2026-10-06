import torch

def _local(world,agents,name):
 x,y=agents.pos[:,0],agents.pos[:,1];return getattr(world,name)[y,x]

def _delta(x,d):return torch.clamp(x+d,0,2)
def logic_303(agents,world):
 v=_local(world,agents,'surface_water');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_304(agents,world):
 v=_local(world,agents,'surface_water');agents.thirst=_delta(agents.thirst,v*0.001)
def logic_305(agents,world):
 v=_local(world,agents,'surface_water');agents.health=_delta(agents.health,v*0.001)
def logic_306(agents,world):
 v=_local(world,agents,'groundwater');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_307(agents,world):
 v=_local(world,agents,'groundwater');agents.thirst=_delta(agents.thirst,v*0.001)
def logic_308(agents,world):
 v=_local(world,agents,'groundwater');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_309(agents,world):
 v=_local(world,agents,'soil_moisture');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_310(agents,world):
 v=_local(world,agents,'soil_moisture');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_311(agents,world):
 v=_local(world,agents,'soil_moisture');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_312(agents,world):
 v=_local(world,agents,'rain');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_313(agents,world):
 v=_local(world,agents,'rain');agents.health=_delta(agents.health,v*0.001)
def logic_314(agents,world):
 v=_local(world,agents,'rain');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_315(agents,world):
 v=_local(world,agents,'snowpack');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_316(agents,world):
 v=_local(world,agents,'snowpack');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_317(agents,world):
 v=_local(world,agents,'snowpack');agents.pathogen_risk=_delta(agents.pathogen_risk,v*0.001)
def logic_318(agents,world):
 v=_local(world,agents,'temperature');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_319(agents,world):
 v=_local(world,agents,'temperature');agents.dehydration=_delta(agents.dehydration,v*0.001)
def logic_320(agents,world):
 v=_local(world,agents,'temperature');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_321(agents,world):
 v=_local(world,agents,'humidity');agents.dehydration=_delta(agents.dehydration,v*0.001)
def logic_322(agents,world):
 v=_local(world,agents,'humidity');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_323(agents,world):
 v=_local(world,agents,'humidity');agents.pathogen_risk=_delta(agents.pathogen_risk,v*0.001)
def logic_324(agents,world):
 v=_local(world,agents,'wind_x');agents.dehydration=_delta(agents.dehydration,v*0.001)
def logic_325(agents,world):
 v=_local(world,agents,'wind_x');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_326(agents,world):
 v=_local(world,agents,'wind_x');agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_327(agents,world):
 v=_local(world,agents,'vegetation');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_328(agents,world):
 v=_local(world,agents,'vegetation');agents.health=_delta(agents.health,v*0.001)
def logic_329(agents,world):
 v=_local(world,agents,'vegetation');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_330(agents,world):
 v=_local(world,agents,'biomass');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_331(agents,world):
 v=_local(world,agents,'biomass');agents.health=_delta(agents.health,v*0.001)
def logic_332(agents,world):
 v=_local(world,agents,'biomass');agents.wealth=_delta(agents.wealth,v*0.001)
def logic_333(agents,world):
 v=_local(world,agents,'herbivore');agents.competition_pressure=_delta(agents.competition_pressure,v*0.001)
def logic_334(agents,world):
 v=_local(world,agents,'herbivore');agents.alertness=_delta(agents.alertness,v*0.001)
def logic_335(agents,world):
 v=_local(world,agents,'herbivore');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_336(agents,world):
 v=_local(world,agents,'predator');agents.alertness=_delta(agents.alertness,v*0.001)
def logic_337(agents,world):
 v=_local(world,agents,'predator');agents.fear=_delta(agents.fear,v*0.001)
def logic_338(agents,world):
 v=_local(world,agents,'predator');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_339(agents,world):
 v=_local(world,agents,'carrion');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_340(agents,world):
 v=_local(world,agents,'carrion');agents.health=_delta(agents.health,v*0.001)
def logic_341(agents,world):
 v=_local(world,agents,'carrion');agents.pathogen_risk=_delta(agents.pathogen_risk,v*0.001)
def logic_342(agents,world):
 v=_local(world,agents,'nutrients');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_343(agents,world):
 v=_local(world,agents,'nutrients');agents.health=_delta(agents.health,v*0.001)
def logic_344(agents,world):
 v=_local(world,agents,'nutrients');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_345(agents,world):
 v=_local(world,agents,'oxygen');agents.health=_delta(agents.health,v*0.001)
def logic_346(agents,world):
 v=_local(world,agents,'oxygen');agents.metabolic_cost=_delta(agents.metabolic_cost,v*0.001)
def logic_347(agents,world):
 v=_local(world,agents,'oxygen');agents.recovery=_delta(agents.recovery,v*0.001)
def logic_348(agents,world):
 v=_local(world,agents,'pathogen_load');agents.health=_delta(agents.health,v*0.001)
def logic_349(agents,world):
 v=_local(world,agents,'pathogen_load');agents.infection_risk=_delta(agents.infection_risk,v*0.001)
def logic_350(agents,world):
 v=_local(world,agents,'pathogen_load');agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_351(agents,world):
 v=_local(world,agents,'biodiversity');agents.health=_delta(agents.health,v*0.001)
def logic_352(agents,world):
 v=_local(world,agents,'biodiversity');agents.habitat_stress=_delta(agents.habitat_stress,v*0.001)
def logic_353(agents,world):
 v=_local(world,agents,'biodiversity');agents.fear=_delta(agents.fear,v*0.001)
def logic_354(agents,world):
 v=_local(world,agents,'habitat_stress');agents.health=_delta(agents.health,v*0.001)
def logic_355(agents,world):
 v=_local(world,agents,'habitat_stress');agents.fear=_delta(agents.fear,v*0.001)
def logic_356(agents,world):
 v=_local(world,agents,'habitat_stress');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_357(agents,world):
 v=_local(world,agents,'erosion');agents.stability=_delta(agents.stability,v*0.001)
def logic_358(agents,world):
 v=_local(world,agents,'erosion');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_359(agents,world):
 v=_local(world,agents,'erosion');agents.health=_delta(agents.health,v*0.001)
def logic_360(agents,world):
 v=_local(world,agents,'soil_depth');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_361(agents,world):
 v=_local(world,agents,'soil_depth');agents.health=_delta(agents.health,v*0.001)
def logic_362(agents,world):
 v=_local(world,agents,'soil_depth');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_363(agents,world):
 v=_local(world,agents,'root_density');agents.food_access=_delta(agents.food_access,v*0.001)
def logic_364(agents,world):
 v=_local(world,agents,'root_density');agents.stability=_delta(agents.stability,v*0.001)
def logic_365(agents,world):
 v=_local(world,agents,'root_density');agents.shelter_need=_delta(agents.shelter_need,v*0.001)
def logic_366(agents,world):
 v=_local(world,agents,'wetland');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_367(agents,world):
 v=_local(world,agents,'wetland');agents.health=_delta(agents.health,v*0.001)
def logic_368(agents,world):
 v=_local(world,agents,'wetland');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_369(agents,world):
 v=_local(world,agents,'carbon_storage');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_370(agents,world):
 v=_local(world,agents,'carbon_storage');agents.health=_delta(agents.health,v*0.001)
def logic_371(agents,world):
 v=_local(world,agents,'carbon_storage');agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_372(agents,world):
 v=_local(world,agents,'fire_risk');agents.health=_delta(agents.health,v*0.001)
def logic_373(agents,world):
 v=_local(world,agents,'fire_risk');agents.fear=_delta(agents.fear,v*0.001)
def logic_374(agents,world):
 v=_local(world,agents,'fire_risk');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_375(agents,world):
 v=_local(world,agents,'ash');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_376(agents,world):
 v=_local(world,agents,'ash');agents.recovery=_delta(agents.recovery,v*0.001)
def logic_377(agents,world):
 v=_local(world,agents,'ash');agents.health=_delta(agents.health,v*0.001)
def logic_378(agents,world):
 v=_local(world,agents,'surface_ice');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_379(agents,world):
 v=_local(world,agents,'surface_ice');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_380(agents,world):
 v=_local(world,agents,'surface_ice');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_381(agents,world):
 v=_local(world,agents,'organic_matter');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_382(agents,world):
 v=_local(world,agents,'organic_matter');agents.recovery=_delta(agents.recovery,v*0.001)
def logic_383(agents,world):
 v=_local(world,agents,'organic_matter');agents.wealth=_delta(agents.wealth,v*0.001)
def logic_384(agents,world):
 v=_local(world,agents,'deadwood');agents.wealth=_delta(agents.wealth,v*0.001)
def logic_385(agents,world):
 v=_local(world,agents,'deadwood');agents.fire_fear=_delta(agents.fire_fear,v*0.001)
def logic_386(agents,world):
 v=_local(world,agents,'deadwood');agents.resource_competition=_delta(agents.resource_competition,v*0.001)
def logic_387(agents,world):
 v=_local(world,agents,'pollinators');agents.food_access=_delta(agents.food_access,v*0.001)
def logic_388(agents,world):
 v=_local(world,agents,'pollinators');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_389(agents,world):
 v=_local(world,agents,'pollinators');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_390(agents,world):
 v=_local(world,agents,'flowers');agents.food_access=_delta(agents.food_access,v*0.001)
def logic_391(agents,world):
 v=_local(world,agents,'flowers');agents.health=_delta(agents.health,v*0.001)
def logic_392(agents,world):
 v=_local(world,agents,'flowers');agents.sharing_capacity=_delta(agents.sharing_capacity,v*0.001)
def logic_393(agents,world):
 v=_local(world,agents,'seed_bank');agents.food_access=_delta(agents.food_access,v*0.001)
def logic_394(agents,world):
 v=_local(world,agents,'seed_bank');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_395(agents,world):
 v=_local(world,agents,'seed_bank');agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_396(agents,world):
 v=_local(world,agents,'soil_carbon');agents.thermal_stress=_delta(agents.thermal_stress,v*0.001)
def logic_397(agents,world):
 v=_local(world,agents,'soil_carbon');agents.health=_delta(agents.health,v*0.001)
def logic_398(agents,world):
 v=_local(world,agents,'soil_carbon');agents.habitat_stress=_delta(agents.habitat_stress,v*0.001)
def logic_399(agents,world):
 v=_local(world,agents,'salinity');agents.health=_delta(agents.health,v*0.001)
def logic_400(agents,world):
 v=_local(world,agents,'salinity');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_401(agents,world):
 v=_local(world,agents,'salinity');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_402(agents,world):
 v=torch.clamp(agents.energy_surplus,0,2);agents.sharing_capacity=_delta(agents.sharing_capacity,v*0.001)
def logic_403(agents,world):
 v=torch.clamp(agents.energy_surplus,0,2);agents.cooperation=_delta(agents.cooperation,v*0.001)
def logic_404(agents,world):
 v=torch.clamp(agents.energy_surplus,0,2);agents.generosity=_delta(agents.generosity,v*0.001)
def logic_405(agents,world):
 v=torch.clamp(agents.energy_surplus,0,2);agents.trust=_delta(agents.trust,v*0.001)
def logic_406(agents,world):
 v=torch.clamp(agents.energy_surplus,0,2);agents.reputation=_delta(agents.reputation,v*0.001)
def logic_407(agents,world):
 v=torch.clamp(agents.hunger,0,2);agents.cooperation=_delta(agents.cooperation,v*0.001)
def logic_408(agents,world):
 v=torch.clamp(agents.hunger,0,2);agents.generosity=_delta(agents.generosity,v*0.001)
def logic_409(agents,world):
 v=torch.clamp(agents.hunger,0,2);agents.trust=_delta(agents.trust,v*0.001)
def logic_410(agents,world):
 v=torch.clamp(agents.hunger,0,2);agents.reputation=_delta(agents.reputation,v*0.001)
def logic_411(agents,world):
 v=torch.clamp(agents.hunger,0,2);agents.selfishness=_delta(agents.selfishness,v*0.001)
def logic_412(agents,world):
 v=torch.clamp(agents.health,0,2);agents.generosity=_delta(agents.generosity,v*0.001)
def logic_413(agents,world):
 v=torch.clamp(agents.health,0,2);agents.trust=_delta(agents.trust,v*0.001)
def logic_414(agents,world):
 v=torch.clamp(agents.health,0,2);agents.reputation=_delta(agents.reputation,v*0.001)
def logic_415(agents,world):
 v=torch.clamp(agents.health,0,2);agents.selfishness=_delta(agents.selfishness,v*0.001)
def logic_416(agents,world):
 v=torch.clamp(agents.health,0,2);agents.defection=_delta(agents.defection,v*0.001)
def logic_417(agents,world):
 v=torch.clamp(agents.stress,0,2);agents.trust=_delta(agents.trust,v*0.001)
def logic_418(agents,world):
 v=torch.clamp(agents.stress,0,2);agents.reputation=_delta(agents.reputation,v*0.001)
def logic_419(agents,world):
 v=torch.clamp(agents.stress,0,2);agents.selfishness=_delta(agents.selfishness,v*0.001)
def logic_420(agents,world):
 v=torch.clamp(agents.stress,0,2);agents.defection=_delta(agents.defection,v*0.001)
def logic_421(agents,world):
 v=torch.clamp(agents.stress,0,2);agents.conflict_pressure=_delta(agents.conflict_pressure,v*0.001)
def logic_422(agents,world):
 v=torch.clamp(agents.reputation,0,2);agents.reputation=_delta(agents.reputation,v*0.001)
def logic_423(agents,world):
 v=torch.clamp(agents.reputation,0,2);agents.selfishness=_delta(agents.selfishness,v*0.001)
def logic_424(agents,world):
 v=torch.clamp(agents.reputation,0,2);agents.defection=_delta(agents.defection,v*0.001)
def logic_425(agents,world):
 v=torch.clamp(agents.reputation,0,2);agents.conflict_pressure=_delta(agents.conflict_pressure,v*0.001)
def logic_426(agents,world):
 v=torch.clamp(agents.reputation,0,2);agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_427(agents,world):
 v=torch.clamp(agents.trust,0,2);agents.selfishness=_delta(agents.selfishness,v*0.001)
def logic_428(agents,world):
 v=torch.clamp(agents.trust,0,2);agents.defection=_delta(agents.defection,v*0.001)
def logic_429(agents,world):
 v=torch.clamp(agents.trust,0,2);agents.conflict_pressure=_delta(agents.conflict_pressure,v*0.001)
def logic_430(agents,world):
 v=torch.clamp(agents.trust,0,2);agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_431(agents,world):
 v=torch.clamp(agents.trust,0,2);agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_432(agents,world):
 v=torch.clamp(agents.cooperation,0,2);agents.defection=_delta(agents.defection,v*0.001)

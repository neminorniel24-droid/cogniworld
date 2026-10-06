import torch

def _local(world,agents,name):
 x,y=agents.pos[:,0],agents.pos[:,1];return getattr(world,name)[y,x]

def _delta(x,d):return torch.clamp(x+d,0,2)
def _signed_delta(x,d):
    return torch.clamp(x+d,-2,2)
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
def logic_433(agents,world):
 v=torch.clamp(agents.cooperation,0,2);agents.conflict_pressure=_delta(agents.conflict_pressure,v*0.001)
def logic_434(agents,world):
 v=torch.clamp(agents.cooperation,0,2);agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_435(agents,world):
 v=torch.clamp(agents.cooperation,0,2);agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_436(agents,world):
 v=torch.clamp(agents.cooperation,0,2);agents.fear=_delta(agents.fear,v*0.001)
def logic_437(agents,world):
 v=torch.clamp(agents.defection,0,2);agents.conflict_pressure=_delta(agents.conflict_pressure,v*0.001)
def logic_438(agents,world):
 v=torch.clamp(agents.defection,0,2);agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_439(agents,world):
 v=torch.clamp(agents.defection,0,2);agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_440(agents,world):
 v=torch.clamp(agents.defection,0,2);agents.fear=_delta(agents.fear,v*0.001)
def logic_441(agents,world):
 v=torch.clamp(agents.defection,0,2);agents.aggression=_delta(agents.aggression,v*0.001)
def logic_442(agents,world):
 v=torch.clamp(agents.help_received,0,2);agents.risk_tolerance=_delta(agents.risk_tolerance,v*0.001)
def logic_443(agents,world):
 v=torch.clamp(agents.help_received,0,2);agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_444(agents,world):
 v=torch.clamp(agents.help_received,0,2);agents.fear=_delta(agents.fear,v*0.001)
def logic_445(agents,world):
 v=torch.clamp(agents.help_received,0,2);agents.aggression=_delta(agents.aggression,v*0.001)
def logic_446(agents,world):
 v=torch.clamp(agents.help_received,0,2);agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_447(agents,world):
 v=torch.clamp(agents.help_given,0,2);agents.social_avoidance=_delta(agents.social_avoidance,v*0.001)
def logic_448(agents,world):
 v=torch.clamp(agents.help_given,0,2);agents.fear=_delta(agents.fear,v*0.001)
def logic_449(agents,world):
 v=torch.clamp(agents.help_given,0,2);agents.aggression=_delta(agents.aggression,v*0.001)
def logic_450(agents,world):
 v=torch.clamp(agents.help_given,0,2);agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_451(agents,world):
 v=torch.clamp(agents.help_given,0,2);agents.help_drive=_delta(agents.help_drive,v*0.001)
def logic_452(agents,world):
 v=torch.clamp(agents.conflict_history,0,2);agents.fear=_delta(agents.fear,v*0.001)
def logic_453(agents,world):
 v=torch.clamp(agents.conflict_history,0,2);agents.aggression=_delta(agents.aggression,v*0.001)
def logic_454(agents,world):
 v=torch.clamp(agents.conflict_history,0,2);agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_455(agents,world):
 v=torch.clamp(agents.conflict_history,0,2);agents.help_drive=_delta(agents.help_drive,v*0.001)
def logic_456(agents,world):
 v=torch.clamp(agents.conflict_history,0,2);agents.territoriality=_delta(agents.territoriality,v*0.001)
def logic_457(agents,world):
 v=torch.clamp(agents.cooperation_history,0,2);agents.aggression=_delta(agents.aggression,v*0.001)
def logic_458(agents,world):
 v=torch.clamp(agents.cooperation_history,0,2);agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_459(agents,world):
 v=torch.clamp(agents.cooperation_history,0,2);agents.help_drive=_delta(agents.help_drive,v*0.001)
def logic_460(agents,world):
 v=torch.clamp(agents.cooperation_history,0,2);agents.territoriality=_delta(agents.territoriality,v*0.001)
def logic_461(agents,world):
 v=torch.clamp(agents.cooperation_history,0,2);agents.group_stability=_delta(agents.group_stability,v*0.001)
def logic_462(agents,world):
 v=torch.clamp(agents.betrayal_memory,0,2);agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_463(agents,world):
 v=torch.clamp(agents.betrayal_memory,0,2);agents.help_drive=_delta(agents.help_drive,v*0.001)
def logic_464(agents,world):
 v=torch.clamp(agents.betrayal_memory,0,2);agents.territoriality=_delta(agents.territoriality,v*0.001)
def logic_465(agents,world):
 v=torch.clamp(agents.betrayal_memory,0,2);agents.group_stability=_delta(agents.group_stability,v*0.001)
def logic_466(agents,world):
 v=torch.clamp(agents.betrayal_memory,0,2);agents.future_help=_delta(agents.future_help,v*0.001)
def logic_467(agents,world):
 v=torch.clamp(agents.group_stability,0,2);agents.help_drive=_delta(agents.help_drive,v*0.001)
def logic_468(agents,world):
 v=torch.clamp(agents.group_stability,0,2);agents.territoriality=_delta(agents.territoriality,v*0.001)
def logic_469(agents,world):
 v=torch.clamp(agents.group_stability,0,2);agents.group_stability=_delta(agents.group_stability,v*0.001)
def logic_470(agents,world):
 v=torch.clamp(agents.group_stability,0,2);agents.future_help=_delta(agents.future_help,v*0.001)
def logic_471(agents,world):
 v=torch.clamp(agents.group_stability,0,2);agents.caution=_delta(agents.caution,v*0.001)
def logic_472(agents,world):
 v=torch.clamp(agents.resource_scarcity,0,2);agents.territoriality=_delta(agents.territoriality,v*0.001)
def logic_473(agents,world):
 v=torch.clamp(agents.resource_scarcity,0,2);agents.group_stability=_delta(agents.group_stability,v*0.001)
def logic_474(agents,world):
 v=torch.clamp(agents.resource_scarcity,0,2);agents.future_help=_delta(agents.future_help,v*0.001)
def logic_475(agents,world):
 v=torch.clamp(agents.resource_scarcity,0,2);agents.caution=_delta(agents.caution,v*0.001)
def logic_476(agents,world):
 v=torch.clamp(agents.resource_scarcity,0,2);agents.attack_threshold=_delta(agents.attack_threshold,v*0.001)
def logic_477(agents,world):
 v=torch.clamp(agents.resource_abundance,0,2);agents.group_stability=_delta(agents.group_stability,v*0.001)
def logic_478(agents,world):
 v=torch.clamp(agents.resource_abundance,0,2);agents.future_help=_delta(agents.future_help,v*0.001)
def logic_479(agents,world):
 v=torch.clamp(agents.resource_abundance,0,2);agents.caution=_delta(agents.caution,v*0.001)
def logic_480(agents,world):
 v=torch.clamp(agents.resource_abundance,0,2);agents.attack_threshold=_delta(agents.attack_threshold,v*0.001)
def logic_481(agents,world):
 v=torch.clamp(agents.resource_abundance,0,2);agents.defection_threshold=_delta(agents.defection_threshold,v*0.001)
def logic_482(agents,world):
 v=torch.clamp(agents.local_density,0,2);agents.future_help=_delta(agents.future_help,v*0.001)
def logic_483(agents,world):
 v=torch.clamp(agents.local_density,0,2);agents.caution=_delta(agents.caution,v*0.001)
def logic_484(agents,world):
 v=torch.clamp(agents.local_density,0,2);agents.attack_threshold=_delta(agents.attack_threshold,v*0.001)
def logic_485(agents,world):
 v=torch.clamp(agents.local_density,0,2);agents.defection_threshold=_delta(agents.defection_threshold,v*0.001)
def logic_486(agents,world):
 v=torch.clamp(agents.local_density,0,2);agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_487(agents,world):
 v=torch.clamp(agents.neighbor_energy_gap,0,2);agents.caution=_delta(agents.caution,v*0.001)
def logic_488(agents,world):
 v=torch.clamp(agents.neighbor_energy_gap,0,2);agents.attack_threshold=_delta(agents.attack_threshold,v*0.001)
def logic_489(agents,world):
 v=torch.clamp(agents.neighbor_energy_gap,0,2);agents.defection_threshold=_delta(agents.defection_threshold,v*0.001)
def logic_490(agents,world):
 v=torch.clamp(agents.neighbor_energy_gap,0,2);agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_491(agents,world):
 v=torch.clamp(agents.neighbor_energy_gap,0,2);agents.strategy_confidence=_delta(agents.strategy_confidence,v*0.001)
def logic_492(agents,world):
 v=torch.clamp(agents.neighbor_health_gap,0,2);agents.attack_threshold=_delta(agents.attack_threshold,v*0.001)
def logic_493(agents,world):
 v=torch.clamp(agents.neighbor_health_gap,0,2);agents.defection_threshold=_delta(agents.defection_threshold,v*0.001)
def logic_494(agents,world):
 v=torch.clamp(agents.neighbor_health_gap,0,2);agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_495(agents,world):
 v=torch.clamp(agents.neighbor_health_gap,0,2);agents.strategy_confidence=_delta(agents.strategy_confidence,v*0.001)
def logic_496(agents,world):
 v=torch.clamp(agents.neighbor_health_gap,0,2);agents.empathy=_delta(agents.empathy,v*0.001)
def logic_497(agents,world):
 v=torch.clamp(agents.risk_tolerance,0,2);agents.defection_threshold=_delta(agents.defection_threshold,v*0.001)
def logic_498(agents,world):
 v=torch.clamp(agents.risk_tolerance,0,2);agents.exploration_drive=_delta(agents.exploration_drive,v*0.001)
def logic_499(agents,world):
 v=torch.clamp(agents.risk_tolerance,0,2);agents.strategy_confidence=_delta(agents.strategy_confidence,v*0.001)
def logic_500(agents,world):
 v=torch.clamp(agents.risk_tolerance,0,2);agents.empathy=_delta(agents.empathy,v*0.001)
def logic_501(agents,world):
 v=torch.clamp(agents.risk_tolerance,0,2);agents.sharing_capacity=_delta(agents.sharing_capacity,v*0.001)
def logic_502(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.strategy_score=_delta(agents.strategy_score,signal*0.001)
def logic_503(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.exploration_score=_delta(agents.exploration_score,signal*0.001)
def logic_504(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.risk_score=_delta(agents.risk_score,signal*0.001)
def logic_505(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.payoff=_delta(agents.payoff,signal*0.001)
def logic_506(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.confidence=_delta(agents.confidence,signal*0.001)
def logic_507(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.exploration_score=_delta(agents.exploration_score,signal*0.001)
def logic_508(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.risk_score=_delta(agents.risk_score,signal*0.001)
def logic_509(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.payoff=_delta(agents.payoff,signal*0.001)
def logic_510(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.confidence=_delta(agents.confidence,signal*0.001)
def logic_511(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.caution=_delta(agents.caution,signal*0.001)
def logic_512(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.risk_score=_delta(agents.risk_score,signal*0.001)
def logic_513(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.payoff=_delta(agents.payoff,signal*0.001)
def logic_514(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.confidence=_delta(agents.confidence,signal*0.001)
def logic_515(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.caution=_delta(agents.caution,signal*0.001)
def logic_516(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.foraging_score=_delta(agents.foraging_score,signal*0.001)
def logic_517(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.payoff=_delta(agents.payoff,signal*0.001)
def logic_518(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.confidence=_delta(agents.confidence,signal*0.001)
def logic_519(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.caution=_delta(agents.caution,signal*0.001)
def logic_520(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.foraging_score=_delta(agents.foraging_score,signal*0.001)
def logic_521(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.survival_score=_delta(agents.survival_score,signal*0.001)
def logic_522(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.confidence=_delta(agents.confidence,signal*0.001)
def logic_523(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.caution=_delta(agents.caution,signal*0.001)
def logic_524(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.foraging_score=_delta(agents.foraging_score,signal*0.001)
def logic_525(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.survival_score=_delta(agents.survival_score,signal*0.001)
def logic_526(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.wealth=_delta(agents.wealth,signal*0.001)
def logic_527(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.caution=_delta(agents.caution,signal*0.001)
def logic_528(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.foraging_score=_delta(agents.foraging_score,signal*0.001)
def logic_529(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.survival_score=_delta(agents.survival_score,signal*0.001)
def logic_530(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.wealth=_delta(agents.wealth,signal*0.001)
def logic_531(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.fitness_score=_delta(agents.fitness_score,signal*0.001)
def logic_532(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.foraging_score=_delta(agents.foraging_score,signal*0.001)
def logic_533(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.survival_score=_delta(agents.survival_score,signal*0.001)
def logic_534(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.wealth=_delta(agents.wealth,signal*0.001)
def logic_535(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.fitness_score=_delta(agents.fitness_score,signal*0.001)
def logic_536(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reproduction_score=_delta(agents.reproduction_score,signal*0.001)
def logic_537(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.survival_score=_delta(agents.survival_score,signal*0.001)
def logic_538(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.wealth=_delta(agents.wealth,signal*0.001)
def logic_539(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.fitness_score=_delta(agents.fitness_score,signal*0.001)
def logic_540(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reproduction_score=_delta(agents.reproduction_score,signal*0.001)
def logic_541(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.cooperation_score=_delta(agents.cooperation_score,signal*0.001)
def logic_542(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.wealth=_delta(agents.wealth,signal*0.001)
def logic_543(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.fitness_score=_delta(agents.fitness_score,signal*0.001)
def logic_544(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reproduction_score=_delta(agents.reproduction_score,signal*0.001)
def logic_545(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.cooperation_score=_delta(agents.cooperation_score,signal*0.001)
def logic_546(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reputation=_delta(agents.reputation,signal*0.001)
def logic_547(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.fitness_score=_delta(agents.fitness_score,signal*0.001)
def logic_548(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reproduction_score=_delta(agents.reproduction_score,signal*0.001)
def logic_549(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.cooperation_score=_delta(agents.cooperation_score,signal*0.001)
def logic_550(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reputation=_delta(agents.reputation,signal*0.001)
def logic_551(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.trust=_delta(agents.trust,signal*0.001)
def logic_552(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reproduction_score=_delta(agents.reproduction_score,signal*0.001)
def logic_553(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.cooperation_score=_delta(agents.cooperation_score,signal*0.001)
def logic_554(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reputation=_delta(agents.reputation,signal*0.001)
def logic_555(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.trust=_delta(agents.trust,signal*0.001)
def logic_556(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.group_stability=_delta(agents.group_stability,signal*0.001)
def logic_557(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.cooperation_score=_delta(agents.cooperation_score,signal*0.001)
def logic_558(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reputation=_delta(agents.reputation,signal*0.001)
def logic_559(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.trust=_delta(agents.trust,signal*0.001)
def logic_560(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.group_stability=_delta(agents.group_stability,signal*0.001)
def logic_561(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.future_help=_delta(agents.future_help,signal*0.001)
def logic_562(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.reputation=_delta(agents.reputation,signal*0.001)
def logic_563(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.trust=_delta(agents.trust,signal*0.001)
def logic_564(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.group_stability=_delta(agents.group_stability,signal*0.001)
def logic_565(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.future_help=_delta(agents.future_help,signal*0.001)
def logic_566(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.defection_score=_delta(agents.defection_score,signal*0.001)
def logic_567(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.trust=_delta(agents.trust,signal*0.001)
def logic_568(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.group_stability=_delta(agents.group_stability,signal*0.001)
def logic_569(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.future_help=_delta(agents.future_help,signal*0.001)
def logic_570(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.defection_score=_delta(agents.defection_score,signal*0.001)
def logic_571(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.aggression=_delta(agents.aggression,signal*0.001)
def logic_572(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.group_stability=_delta(agents.group_stability,signal*0.001)
def logic_573(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.future_help=_delta(agents.future_help,signal*0.001)
def logic_574(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.defection_score=_delta(agents.defection_score,signal*0.001)
def logic_575(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.aggression=_delta(agents.aggression,signal*0.001)
def logic_576(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.conflict_pressure=_delta(agents.conflict_pressure,signal*0.001)
def logic_577(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.future_help=_delta(agents.future_help,signal*0.001)
def logic_578(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.defection_score=_delta(agents.defection_score,signal*0.001)
def logic_579(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.aggression=_delta(agents.aggression,signal*0.001)
def logic_580(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.conflict_pressure=_delta(agents.conflict_pressure,signal*0.001)
def logic_581(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.learning_rate=_delta(agents.learning_rate,signal*0.001)
def logic_582(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.defection_score=_delta(agents.defection_score,signal*0.001)
def logic_583(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.aggression=_delta(agents.aggression,signal*0.001)
def logic_584(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.conflict_pressure=_delta(agents.conflict_pressure,signal*0.001)
def logic_585(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.learning_rate=_delta(agents.learning_rate,signal*0.001)
def logic_586(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.strategy_score=_delta(agents.strategy_score,signal*0.001)
def logic_587(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.aggression=_delta(agents.aggression,signal*0.001)
def logic_588(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.conflict_pressure=_delta(agents.conflict_pressure,signal*0.001)
def logic_589(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.learning_rate=_delta(agents.learning_rate,signal*0.001)
def logic_590(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.strategy_score=_delta(agents.strategy_score,signal*0.001)
def logic_591(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.exploration_score=_delta(agents.exploration_score,signal*0.001)
def logic_592(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.conflict_pressure=_delta(agents.conflict_pressure,signal*0.001)
def logic_593(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.learning_rate=_delta(agents.learning_rate,signal*0.001)
def logic_594(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.strategy_score=_delta(agents.strategy_score,signal*0.001)
def logic_595(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.exploration_score=_delta(agents.exploration_score,signal*0.001)
def logic_596(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.risk_score=_delta(agents.risk_score,signal*0.001)
def logic_597(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.learning_rate=_delta(agents.learning_rate,signal*0.001)
def logic_598(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.strategy_score=_delta(agents.strategy_score,signal*0.001)
def logic_599(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.exploration_score=_delta(agents.exploration_score,signal*0.001)
def logic_600(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.risk_score=_delta(agents.risk_score,signal*0.001)
def logic_601(agents,world):
 signal=torch.sigmoid(agents.last_reward*0.05+agents.last_action.float()*0.02);agents.payoff=_delta(agents.payoff,signal*0.001)
def logic_622(agents,world):
    agents.risk_score=_delta(agents.risk_score,+0.002*agents.health)
def logic_623(agents,world):
    agents.safety_score=_delta(agents.safety_score,+0.002*agents.hydration)
def logic_624(agents,world):
    agents.survival_score=_delta(agents.survival_score,-0.002*agents.thirst)
def logic_625(agents,world):
    agents.foraging_score=_delta(agents.foraging_score,+0.002*agents.hunger)
def logic_626(agents,world):
    agents.migration_score=_delta(agents.migration_score,+0.002*agents.thermal_stress)
def logic_627(agents,world):
    agents.reproduction_score=_delta(agents.reproduction_score,-0.002*agents.dehydration)
def logic_628(agents,world):
    agents.exploration_score=_delta(agents.exploration_score,+0.002*agents.pathogen_risk)
def logic_629(agents,world):
    agents.strategy_score=_delta(agents.strategy_score,+0.002*agents.infection_risk)
def logic_630(agents,world):
    agents.strategy_confidence=_delta(agents.strategy_confidence,+0.002*agents.alertness)
def logic_631(agents,world):
    agents.caution=_delta(agents.caution,+0.002*agents.fear)
def logic_632(agents,world):
    agents.confidence=_delta(agents.confidence,+0.002*agents.recovery)
def logic_633(agents,world):
    agents.self_preservation=_delta(agents.self_preservation,+0.002*agents.metabolic_cost)
def logic_634(agents,world):
    agents.learning_rate=_delta(agents.learning_rate,+0.002*agents.reproduction_drive)
def logic_635(agents,world):
    agents.resource_discovery=_delta(agents.resource_discovery,+0.002*agents.migration_drive)
def logic_636(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,+0.002*agents.exploration_drive)
def logic_637(agents,world):
    agents.help_drive=_delta(agents.help_drive,+0.002*agents.food_access)
def logic_638(agents,world):
    agents.social_need=_delta(agents.social_need,+0.002*agents.wealth)
def logic_639(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.stability)
def logic_640(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.habitat_stress)
def logic_641(agents,world):
    agents.resource_competition=_delta(agents.resource_competition,+0.002*agents.social_tolerance)
def logic_642(agents,world):
    agents.migration_score=_delta(agents.migration_score,+0.002*agents.health)
def logic_643(agents,world):
    agents.reproduction_score=_delta(agents.reproduction_score,+0.002*agents.hydration)
def logic_644(agents,world):
    agents.exploration_score=_delta(agents.exploration_score,+0.002*agents.thirst)
def logic_645(agents,world):
    agents.strategy_score=_delta(agents.strategy_score,+0.002*agents.hunger)
def logic_646(agents,world):
    agents.strategy_confidence=_delta(agents.strategy_confidence,-0.002*agents.thermal_stress)
def logic_647(agents,world):
    agents.caution=_delta(agents.caution,+0.002*agents.dehydration)
def logic_648(agents,world):
    agents.confidence=_delta(agents.confidence,-0.002*agents.pathogen_risk)
def logic_649(agents,world):
    agents.self_preservation=_delta(agents.self_preservation,+0.002*agents.infection_risk)
def logic_650(agents,world):
    agents.learning_rate=_delta(agents.learning_rate,+0.002*agents.alertness)
def logic_651(agents,world):
    agents.resource_discovery=_delta(agents.resource_discovery,+0.002*agents.fear)
def logic_652(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,+0.002*agents.recovery)
def logic_653(agents,world):
    agents.help_drive=_delta(agents.help_drive,+0.002*agents.metabolic_cost)
def logic_654(agents,world):
    agents.social_need=_delta(agents.social_need,+0.002*agents.reproduction_drive)
def logic_655(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.migration_drive)
def logic_656(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.exploration_drive)
def logic_657(agents,world):
    agents.resource_competition=_delta(agents.resource_competition,+0.002*agents.food_access)
def logic_658(agents,world):
    agents.risk_score=_delta(agents.risk_score,+0.002*agents.wealth)
def logic_659(agents,world):
    agents.safety_score=_delta(agents.safety_score,+0.002*agents.stability)
def logic_660(agents,world):
    agents.survival_score=_delta(agents.survival_score,-0.002*agents.habitat_stress)
def logic_661(agents,world):
    agents.foraging_score=_delta(agents.foraging_score,+0.002*agents.social_tolerance)
def logic_662(agents,world):
    agents.strategy_confidence=_delta(agents.strategy_confidence,+0.002*agents.health)
def logic_663(agents,world):
    agents.caution=_delta(agents.caution,+0.002*agents.hydration)
def logic_664(agents,world):
    agents.confidence=_delta(agents.confidence,-0.002*agents.thirst)
def logic_665(agents,world):
    agents.self_preservation=_delta(agents.self_preservation,+0.002*agents.hunger)
def logic_666(agents,world):
    agents.learning_rate=_delta(agents.learning_rate,+0.002*agents.thermal_stress)
def logic_667(agents,world):
    agents.resource_discovery=_delta(agents.resource_discovery,+0.002*agents.dehydration)
def logic_668(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,-0.002*agents.pathogen_risk)
def logic_669(agents,world):
    agents.help_drive=_delta(agents.help_drive,-0.002*agents.infection_risk)
def logic_670(agents,world):
    agents.social_need=_delta(agents.social_need,+0.002*agents.alertness)
def logic_671(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.fear)
def logic_672(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.recovery)
def logic_673(agents,world):
    agents.resource_competition=_delta(agents.resource_competition,+0.002*agents.metabolic_cost)
def logic_674(agents,world):
    agents.risk_score=_delta(agents.risk_score,+0.002*agents.reproduction_drive)
def logic_675(agents,world):
    agents.safety_score=_delta(agents.safety_score,+0.002*agents.migration_drive)
def logic_676(agents,world):
    agents.survival_score=_delta(agents.survival_score,+0.002*agents.exploration_drive)
def logic_677(agents,world):
    agents.foraging_score=_delta(agents.foraging_score,+0.002*agents.food_access)
def logic_678(agents,world):
    agents.migration_score=_delta(agents.migration_score,+0.002*agents.wealth)
def logic_679(agents,world):
    agents.reproduction_score=_delta(agents.reproduction_score,+0.002*agents.stability)
def logic_680(agents,world):
    agents.exploration_score=_delta(agents.exploration_score,+0.002*agents.habitat_stress)
def logic_681(agents,world):
    agents.strategy_score=_delta(agents.strategy_score,+0.002*agents.social_tolerance)
def logic_682(agents,world):
    agents.learning_rate=_delta(agents.learning_rate,+0.002*agents.health)
def logic_683(agents,world):
    agents.resource_discovery=_delta(agents.resource_discovery,+0.002*agents.hydration)
def logic_684(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,-0.002*agents.thirst)
def logic_685(agents,world):
    agents.help_drive=_delta(agents.help_drive,-0.002*agents.hunger)
def logic_686(agents,world):
    agents.social_need=_delta(agents.social_need,+0.002*agents.thermal_stress)
def logic_687(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.dehydration)
def logic_688(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.pathogen_risk)
def logic_689(agents,world):
    agents.resource_competition=_delta(agents.resource_competition,+0.002*agents.infection_risk)
def logic_690(agents,world):
    agents.risk_score=_delta(agents.risk_score,+0.002*agents.alertness)
def logic_691(agents,world):
    agents.safety_score=_delta(agents.safety_score,+0.002*agents.fear)
def logic_692(agents,world):
    agents.survival_score=_delta(agents.survival_score,+0.002*agents.recovery)
def logic_693(agents,world):
    agents.foraging_score=_delta(agents.foraging_score,+0.002*agents.metabolic_cost)
def logic_694(agents,world):
    agents.migration_score=_delta(agents.migration_score,+0.002*agents.reproduction_drive)
def logic_695(agents,world):
    agents.reproduction_score=_delta(agents.reproduction_score,+0.002*agents.migration_drive)
def logic_696(agents,world):
    agents.exploration_score=_delta(agents.exploration_score,+0.002*agents.exploration_drive)
def logic_697(agents,world):
    agents.strategy_score=_delta(agents.strategy_score,+0.002*agents.food_access)
def logic_698(agents,world):
    agents.strategy_confidence=_delta(agents.strategy_confidence,+0.002*agents.wealth)
def logic_699(agents,world):
    agents.caution=_delta(agents.caution,+0.002*agents.stability)
def logic_700(agents,world):
    agents.confidence=_delta(agents.confidence,-0.002*agents.habitat_stress)
def logic_701(agents,world):
    agents.self_preservation=_delta(agents.self_preservation,+0.002*agents.social_tolerance)
def logic_702(agents,world):
    agents.social_need=_delta(agents.social_need,+0.002*agents.health)
def logic_703(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.hydration)
def logic_704(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.thirst)
def logic_705(agents,world):
    agents.resource_competition=_delta(agents.resource_competition,+0.002*agents.hunger)
def logic_706(agents,world):
    agents.risk_score=_delta(agents.risk_score,+0.002*agents.thermal_stress)
def logic_707(agents,world):
    agents.safety_score=_delta(agents.safety_score,-0.002*agents.dehydration)
def logic_708(agents,world):
    agents.survival_score=_delta(agents.survival_score,-0.002*agents.pathogen_risk)
def logic_709(agents,world):
    agents.foraging_score=_delta(agents.foraging_score,+0.002*agents.infection_risk)
def logic_710(agents,world):
    agents.migration_score=_delta(agents.migration_score,+0.002*agents.alertness)
def logic_711(agents,world):
    agents.reproduction_score=_delta(agents.reproduction_score,+0.002*agents.fear)
def logic_712(agents,world):
    agents.exploration_score=_delta(agents.exploration_score,+0.002*agents.recovery)
def logic_713(agents,world):
    agents.strategy_score=_delta(agents.strategy_score,+0.002*agents.metabolic_cost)
def logic_714(agents,world):
    agents.strategy_confidence=_delta(agents.strategy_confidence,+0.002*agents.reproduction_drive)
def logic_715(agents,world):
    agents.caution=_delta(agents.caution,+0.002*agents.migration_drive)
def logic_716(agents,world):
    agents.cooperation_score=_delta(agents.cooperation_score,+0.002*agents.reputation)
def logic_717(agents,world):
    agents.competition_score=_delta(agents.competition_score,+0.002*agents.trust)
def logic_718(agents,world):
    agents.defection_score=_delta(agents.defection_score,-0.002*agents.cooperation)
def logic_719(agents,world):
    agents.reciprocity_score=_delta(agents.reciprocity_score,+0.002*agents.defection)
def logic_720(agents,world):
    agents.help_score=_delta(agents.help_score,-0.002*agents.aggression)
def logic_721(agents,world):
    agents.sharing_score=_delta(agents.sharing_score,-0.002*agents.conflict_pressure)
def logic_722(agents,world):
    agents.reputation=_delta(agents.reputation,-0.002*agents.competition_pressure)
def logic_723(agents,world):
    agents.trust=_delta(agents.trust,-0.002*agents.territoriality)
def logic_724(agents,world):
    agents.cooperation=_delta(agents.cooperation,+0.002*agents.group_stability)
def logic_725(agents,world):
    agents.defection=_delta(agents.defection,+0.002*agents.sharing_capacity)
def logic_726(agents,world):
    agents.aggression=_delta(agents.aggression,+0.002*agents.help_drive)
def logic_727(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.social_avoidance)
def logic_728(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.selfishness)
def logic_729(agents,world):
    agents.group_stability=_delta(agents.group_stability,+0.002*agents.generosity)
def logic_730(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,+0.002*agents.gratitude)
def logic_731(agents,world):
    agents.help_drive=_delta(agents.help_drive,+0.002*agents.caution)
def logic_732(agents,world):
    agents.social_avoidance=_delta(agents.social_avoidance,+0.002*agents.confidence)
def logic_733(agents,world):
    agents.selfishness=_delta(agents.selfishness,+0.002*agents.strategy_confidence)
def logic_734(agents,world):
    agents.generosity=_delta(agents.generosity,+0.002*agents.future_help)
def logic_735(agents,world):
    agents.gratitude=_delta(agents.gratitude,+0.002*agents.empathy)
def logic_736(agents,world):
    agents.reciprocity_score=_delta(agents.reciprocity_score,+0.002*agents.reputation)
def logic_737(agents,world):
    agents.help_score=_delta(agents.help_score,+0.002*agents.trust)
def logic_738(agents,world):
    agents.sharing_score=_delta(agents.sharing_score,+0.002*agents.cooperation)
def logic_739(agents,world):
    agents.reputation=_delta(agents.reputation,-0.002*agents.defection)
def logic_740(agents,world):
    agents.trust=_delta(agents.trust,-0.002*agents.aggression)
def logic_741(agents,world):
    agents.cooperation=_delta(agents.cooperation,-0.002*agents.conflict_pressure)
def logic_742(agents,world):
    agents.defection=_delta(agents.defection,+0.002*agents.competition_pressure)
def logic_743(agents,world):
    agents.aggression=_delta(agents.aggression,+0.002*agents.territoriality)
def logic_744(agents,world):
    agents.conflict_pressure=_delta(agents.conflict_pressure,+0.002*agents.group_stability)
def logic_745(agents,world):
    agents.competition_pressure=_delta(agents.competition_pressure,+0.002*agents.sharing_capacity)
def logic_746(agents,world):
    agents.group_stability=_delta(agents.group_stability,+0.002*agents.help_drive)
def logic_747(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,-0.002*agents.social_avoidance)
def logic_748(agents,world):
    agents.help_drive=_delta(agents.help_drive,-0.002*agents.selfishness)
def logic_749(agents,world):
    agents.social_avoidance=_delta(agents.social_avoidance,+0.002*agents.generosity)
def logic_750(agents,world):
    agents.selfishness=_delta(agents.selfishness,+0.002*agents.gratitude)
def logic_751(agents,world):
    agents.generosity=_delta(agents.generosity,+0.002*agents.caution)
def logic_752(agents,world):
    agents.gratitude=_delta(agents.gratitude,+0.002*agents.confidence)
def logic_753(agents,world):
    agents.cooperation_score=_delta(agents.cooperation_score,+0.002*agents.strategy_confidence)
def logic_754(agents,world):
    agents.competition_score=_delta(agents.competition_score,+0.002*agents.future_help)
def logic_755(agents,world):
    agents.defection_score=_delta(agents.defection_score,+0.002*agents.empathy)
def logic_756(agents,world):
    agents.group_stability=_delta(agents.group_stability,-0.002*agents.territoriality)
def logic_757(agents,world):
    agents.sharing_capacity=_delta(agents.sharing_capacity,+0.002*agents.group_stability)
def logic_758(agents,world):
    agents.help_drive=_delta(agents.help_drive,+0.002*agents.sharing_capacity)
def logic_759(agents,world):
    agents.social_avoidance=_delta(agents.social_avoidance,+0.002*agents.help_drive)
def logic_760(agents,world):
    agents.selfishness=_delta(agents.selfishness,+0.002*agents.social_avoidance)
def logic_761(agents,world):
    agents.generosity=_delta(agents.generosity,+0.002*agents.selfishness)

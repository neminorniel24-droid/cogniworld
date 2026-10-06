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

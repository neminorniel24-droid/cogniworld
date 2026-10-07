import torch

def _local(world, agents, name):
    x,y=agents.pos[:,0],agents.pos[:,1]
    return getattr(world,name)[y,x]

def _delta(x,d): return torch.clamp(x+d,0,2)

def rule_28001(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28002(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'surface_water'))
def rule_28003(world, agents):
    agents.food_access = _delta(agents.food_access, -0.001*_local(world, agents, 'humidity'))
def rule_28004(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28005(world, agents):
    agents.stability = _delta(agents.stability, 0.001*(_local(world, agents, 'rain')-agents.stability))
def rule_28006(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28007(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'runoff'))
def rule_28008(world, agents):
    agents.reputation = _delta(agents.reputation, -0.001*_local(world, agents, 'wind_x'))
def rule_28009(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28010(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*(_local(world, agents, 'vegetation')-agents.cooperation))
def rule_28011(world, agents):
    agents.defection = _delta(agents.defection, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28012(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'herbivore'))
def rule_28013(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, -0.001*_local(world, agents, 'predator'))
def rule_28014(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28015(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*(_local(world, agents, 'nutrients')-agents.territoriality))
def rule_28016(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28017(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'oxygen'))
def rule_28018(world, agents):
    agents.help_drive = _delta(agents.help_drive, -0.001*_local(world, agents, 'co2'))
def rule_28019(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28020(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*(_local(world, agents, 'ice')-agents.selfishness))
def rule_28021(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28022(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'detritus'))
def rule_28023(world, agents):
    agents.caution = _delta(agents.caution, -0.001*_local(world, agents, 'methane'))
def rule_28024(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28025(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*(_local(world, agents, 'biodiversity')-agents.strategy_confidence))
def rule_28026(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28027(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'erosion'))
def rule_28028(world, agents):
    agents.empathy = _delta(agents.empathy, -0.001*_local(world, agents, 'soil_depth'))
def rule_28029(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28030(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*(_local(world, agents, 'wetland')-agents.defection_threshold))
def rule_28031(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28032(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'fire_risk'))
def rule_28033(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, -0.001*_local(world, agents, 'ash'))
def rule_28034(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28035(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*(_local(world, agents, 'groundwater')-agents.vegetation_expectation))
def rule_28036(world, agents):
    agents.stress = _delta(agents.stress, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28037(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'salinity'))
def rule_28038(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, -0.001*_local(world, agents, 'algae'))
def rule_28039(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28040(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*(_local(world, agents, 'deadwood')-agents.betrayal_memory))
def rule_28041(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28042(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'flowers'))
def rule_28043(world, agents):
    agents.help_received = _delta(agents.help_received, -0.001*_local(world, agents, 'seed_bank'))
def rule_28044(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28045(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*(_local(world, agents, 'surface_ice')-agents.local_density))
def rule_28046(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28047(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'surface_water'))
def rule_28048(world, agents):
    agents.last_food = _delta(agents.last_food, -0.001*_local(world, agents, 'humidity'))
def rule_28049(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28050(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*(_local(world, agents, 'rain')-agents.risk_tolerance))
def rule_28051(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28052(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'runoff'))
def rule_28053(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, -0.001*_local(world, agents, 'wind_x'))
def rule_28054(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28055(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*(_local(world, agents, 'vegetation')-agents.defection_score))
def rule_28056(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28057(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'herbivore'))
def rule_28058(world, agents):
    agents.safety_score = _delta(agents.safety_score, -0.001*_local(world, agents, 'predator'))
def rule_28059(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28060(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*(_local(world, agents, 'nutrients')-agents.foraging_score))
def rule_28061(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28062(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'oxygen'))
def rule_28063(world, agents):
    agents.help_score = _delta(agents.help_score, -0.001*_local(world, agents, 'co2'))
def rule_28064(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28065(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*(_local(world, agents, 'ice')-agents.retaliation_risk))
def rule_28066(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28067(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'detritus'))
def rule_28068(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, -0.001*_local(world, agents, 'methane'))
def rule_28069(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28070(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*(_local(world, agents, 'biodiversity')-agents.strategy_persistence))
def rule_28071(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28072(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'erosion'))
def rule_28073(world, agents):
    agents.memory_update = _delta(agents.memory_update, -0.001*_local(world, agents, 'soil_depth'))
def rule_28074(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28075(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*(_local(world, agents, 'wetland')-agents.self_preservation))
def rule_28076(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28077(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'fire_risk'))
def rule_28078(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, -0.001*_local(world, agents, 'ash'))
def rule_28079(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28080(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*(_local(world, agents, 'groundwater')-agents.resource_abundance))
def rule_28081(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28082(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'salinity'))
def rule_28083(world, agents):
    agents.hunger = _delta(agents.hunger, -0.001*_local(world, agents, 'algae'))
def rule_28084(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28085(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*(_local(world, agents, 'deadwood')-agents.thermal_stress))
def rule_28086(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28087(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'flowers'))
def rule_28088(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, -0.001*_local(world, agents, 'seed_bank'))
def rule_28089(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28090(world, agents):
    agents.fear = _delta(agents.fear, 0.001*(_local(world, agents, 'surface_ice')-agents.fear))
def rule_28091(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28092(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'surface_water'))
def rule_28093(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, -0.001*_local(world, agents, 'humidity'))
def rule_28094(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28095(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*(_local(world, agents, 'rain')-agents.exploration_drive))
def rule_28096(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28097(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'runoff'))
def rule_28098(world, agents):
    agents.stability = _delta(agents.stability, -0.001*_local(world, agents, 'wind_x'))
def rule_28099(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28100(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*(_local(world, agents, 'vegetation')-agents.social_tolerance))
def rule_28101(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28102(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'herbivore'))
def rule_28103(world, agents):
    agents.cooperation = _delta(agents.cooperation, -0.001*_local(world, agents, 'predator'))
def rule_28104(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28105(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*(_local(world, agents, 'nutrients')-agents.aggression))
def rule_28106(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28107(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'oxygen'))
def rule_28108(world, agents):
    agents.territoriality = _delta(agents.territoriality, -0.001*_local(world, agents, 'co2'))
def rule_28109(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28110(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*(_local(world, agents, 'ice')-agents.sharing_capacity))
def rule_28111(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28112(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'detritus'))
def rule_28113(world, agents):
    agents.selfishness = _delta(agents.selfishness, -0.001*_local(world, agents, 'methane'))
def rule_28114(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28115(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*(_local(world, agents, 'biodiversity')-agents.gratitude))
def rule_28116(world, agents):
    agents.caution = _delta(agents.caution, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28117(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'erosion'))
def rule_28118(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, -0.001*_local(world, agents, 'soil_depth'))
def rule_28119(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28120(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*(_local(world, agents, 'wetland')-agents.resource_discovery))
def rule_28121(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28122(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'fire_risk'))
def rule_28123(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, -0.001*_local(world, agents, 'ash'))
def rule_28124(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28125(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*(_local(world, agents, 'groundwater')-agents.shelter_need))
def rule_28126(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28127(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'salinity'))
def rule_28128(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, -0.001*_local(world, agents, 'algae'))
def rule_28129(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28130(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*(_local(world, agents, 'deadwood')-agents.social_need))
def rule_28131(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28132(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'flowers'))
def rule_28133(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, -0.001*_local(world, agents, 'seed_bank'))
def rule_28134(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28135(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*(_local(world, agents, 'surface_ice')-agents.cooperation_history))
def rule_28136(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28137(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'surface_water'))
def rule_28138(world, agents):
    agents.local_density = _delta(agents.local_density, -0.001*_local(world, agents, 'humidity'))
def rule_28139(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28140(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*(_local(world, agents, 'rain')-agents.last_energy_delta))
def rule_28141(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28142(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'runoff'))
def rule_28143(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, -0.001*_local(world, agents, 'wind_x'))
def rule_28144(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28145(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*(_local(world, agents, 'vegetation')-agents.strategy_score))
def rule_28146(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28147(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'herbivore'))
def rule_28148(world, agents):
    agents.defection_score = _delta(agents.defection_score, -0.001*_local(world, agents, 'predator'))
def rule_28149(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28150(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*(_local(world, agents, 'nutrients')-agents.risk_score))
def rule_28151(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28152(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'oxygen'))
def rule_28153(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, -0.001*_local(world, agents, 'co2'))
def rule_28154(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28155(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*(_local(world, agents, 'ice')-agents.fitness_score))
def rule_28156(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28157(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'detritus'))
def rule_28158(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, -0.001*_local(world, agents, 'methane'))
def rule_28159(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28160(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*(_local(world, agents, 'biodiversity')-agents.migration_score))
def rule_28161(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28162(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'erosion'))
def rule_28163(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, -0.001*_local(world, agents, 'soil_depth'))
def rule_28164(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28165(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*(_local(world, agents, 'wetland')-agents.learning_rate))
def rule_28166(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28167(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'fire_risk'))
def rule_28168(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, -0.001*_local(world, agents, 'ash'))
def rule_28169(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28170(world, agents):
    agents.energy = _delta(agents.energy, 0.001*(_local(world, agents, 'groundwater')-agents.energy))
def rule_28171(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28172(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'salinity'))
def rule_28173(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, -0.001*_local(world, agents, 'algae'))
def rule_28174(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28175(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*(_local(world, agents, 'deadwood')-agents.thirst))
def rule_28176(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28177(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'flowers'))
def rule_28178(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, -0.001*_local(world, agents, 'seed_bank'))
def rule_28179(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28180(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*(_local(world, agents, 'surface_ice')-agents.pathogen_risk))
def rule_28181(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28182(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'surface_water'))
def rule_28183(world, agents):
    agents.fear = _delta(agents.fear, -0.001*_local(world, agents, 'humidity'))
def rule_28184(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28185(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*(_local(world, agents, 'rain')-agents.metabolic_cost))
def rule_28186(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28187(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'runoff'))
def rule_28188(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, -0.001*_local(world, agents, 'wind_x'))
def rule_28189(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28190(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*(_local(world, agents, 'vegetation')-agents.wealth))
def rule_28191(world, agents):
    agents.stability = _delta(agents.stability, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28192(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'herbivore'))
def rule_28193(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, -0.001*_local(world, agents, 'predator'))
def rule_28194(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28195(world, agents):
    agents.trust = _delta(agents.trust, 0.001*(_local(world, agents, 'nutrients')-agents.trust))
def rule_28196(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28197(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'oxygen'))
def rule_28198(world, agents):
    agents.aggression = _delta(agents.aggression, -0.001*_local(world, agents, 'co2'))
def rule_28199(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28200(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*(_local(world, agents, 'ice')-agents.competition_pressure))
def rule_28201(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28202(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'detritus'))
def rule_28203(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, -0.001*_local(world, agents, 'methane'))
def rule_28204(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28205(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*(_local(world, agents, 'biodiversity')-agents.social_avoidance))
def rule_28206(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28207(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'erosion'))
def rule_28208(world, agents):
    agents.gratitude = _delta(agents.gratitude, -0.001*_local(world, agents, 'soil_depth'))
def rule_28209(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28210(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*(_local(world, agents, 'wetland')-agents.confidence))
def rule_28211(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28212(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'fire_risk'))
def rule_28213(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, -0.001*_local(world, agents, 'ash'))
def rule_28214(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28215(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*(_local(world, agents, 'groundwater')-agents.attack_threshold))
def rule_28216(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28217(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'salinity'))
def rule_28218(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, -0.001*_local(world, agents, 'algae'))
def rule_28219(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28220(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*(_local(world, agents, 'deadwood')-agents.resource_competition))
def rule_28221(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28222(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'flowers'))
def rule_28223(world, agents):
    agents.social_need = _delta(agents.social_need, -0.001*_local(world, agents, 'seed_bank'))
def rule_28224(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28225(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*(_local(world, agents, 'surface_ice')-agents.neighbor_health_gap))
def rule_28226(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28227(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'surface_water'))
def rule_28228(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, -0.001*_local(world, agents, 'humidity'))
def rule_28229(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28230(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*(_local(world, agents, 'rain')-agents.help_given))
def rule_28231(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28232(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'runoff'))
def rule_28233(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, -0.001*_local(world, agents, 'wind_x'))
def rule_28234(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28235(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*(_local(world, agents, 'vegetation')-agents.last_interaction))
def rule_28236(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28237(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'herbivore'))
def rule_28238(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, -0.001*_local(world, agents, 'predator'))
def rule_28239(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28240(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*(_local(world, agents, 'nutrients')-agents.competition_score))
def rule_28241(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28242(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'oxygen'))
def rule_28243(world, agents):
    agents.risk_score = _delta(agents.risk_score, -0.001*_local(world, agents, 'co2'))
def rule_28244(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28245(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*(_local(world, agents, 'ice')-agents.exploration_score))
def rule_28246(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28247(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'detritus'))
def rule_28248(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, -0.001*_local(world, agents, 'methane'))
def rule_28249(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28250(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*(_local(world, agents, 'biodiversity')-agents.attack_success))
def rule_28251(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28252(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'erosion'))
def rule_28253(world, agents):
    agents.migration_score = _delta(agents.migration_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_28254(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28255(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*(_local(world, agents, 'wetland')-agents.sharing_score))
def rule_28256(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28257(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'fire_risk'))
def rule_28258(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, -0.001*_local(world, agents, 'ash'))
def rule_28259(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28260(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*(_local(world, agents, 'groundwater')-agents.future_payoff_weight))
def rule_28261(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28262(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'salinity'))
def rule_28263(world, agents):
    agents.energy = _delta(agents.energy, -0.001*_local(world, agents, 'algae'))
def rule_28264(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28265(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*(_local(world, agents, 'deadwood')-agents.resource_scarcity))
def rule_28266(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28267(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'flowers'))
def rule_28268(world, agents):
    agents.thirst = _delta(agents.thirst, -0.001*_local(world, agents, 'seed_bank'))
def rule_28269(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28270(world, agents):
    agents.health = _delta(agents.health, 0.001*(_local(world, agents, 'surface_ice')-agents.health))
def rule_28271(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28272(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'surface_water'))
def rule_28273(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, -0.001*_local(world, agents, 'humidity'))
def rule_28274(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28275(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*(_local(world, agents, 'rain')-agents.alertness))
def rule_28276(world, agents):
    agents.fear = _delta(agents.fear, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28277(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'runoff'))
def rule_28278(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, -0.001*_local(world, agents, 'wind_x'))
def rule_28279(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28280(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*(_local(world, agents, 'vegetation')-agents.migration_drive))
def rule_28281(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28282(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'herbivore'))
def rule_28283(world, agents):
    agents.wealth = _delta(agents.wealth, -0.001*_local(world, agents, 'predator'))
def rule_28284(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28285(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*(_local(world, agents, 'nutrients')-agents.habitat_stress))
def rule_28286(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28287(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'oxygen'))
def rule_28288(world, agents):
    agents.trust = _delta(agents.trust, -0.001*_local(world, agents, 'co2'))
def rule_28289(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28290(world, agents):
    agents.defection = _delta(agents.defection, 0.001*(_local(world, agents, 'ice')-agents.defection))
def rule_28291(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28292(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'detritus'))
def rule_28293(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, -0.001*_local(world, agents, 'methane'))
def rule_28294(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28295(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*(_local(world, agents, 'biodiversity')-agents.group_stability))
def rule_28296(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28297(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'erosion'))
def rule_28298(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, -0.001*_local(world, agents, 'soil_depth'))
def rule_28299(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28300(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*(_local(world, agents, 'wetland')-agents.generosity))
def rule_28301(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28302(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'fire_risk'))
def rule_28303(world, agents):
    agents.confidence = _delta(agents.confidence, -0.001*_local(world, agents, 'ash'))
def rule_28304(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28305(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*(_local(world, agents, 'groundwater')-agents.future_help))
def rule_28306(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28307(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'salinity'))
def rule_28308(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, -0.001*_local(world, agents, 'algae'))
def rule_28309(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28310(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*(_local(world, agents, 'deadwood')-agents.oxygen_need))
def rule_28311(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28312(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'flowers'))
def rule_28313(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, -0.001*_local(world, agents, 'seed_bank'))
def rule_28314(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28315(world, agents):
    agents.stress = _delta(agents.stress, 0.001*(_local(world, agents, 'surface_ice')-agents.stress))
def rule_28316(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28317(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'surface_water'))
def rule_28318(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, -0.001*_local(world, agents, 'humidity'))
def rule_28319(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28320(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*(_local(world, agents, 'rain')-agents.conflict_history))
def rule_28321(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28322(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'runoff'))
def rule_28323(world, agents):
    agents.help_given = _delta(agents.help_given, -0.001*_local(world, agents, 'wind_x'))
def rule_28324(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28325(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*(_local(world, agents, 'vegetation')-agents.last_reward))
def rule_28326(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28327(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'herbivore'))
def rule_28328(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, -0.001*_local(world, agents, 'predator'))
def rule_28329(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28330(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*(_local(world, agents, 'nutrients')-agents.last_action))
def rule_28331(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28332(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'oxygen'))
def rule_28333(world, agents):
    agents.competition_score = _delta(agents.competition_score, -0.001*_local(world, agents, 'co2'))
def rule_28334(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28335(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*(_local(world, agents, 'ice')-agents.reciprocity_score))
def rule_28336(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28337(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'detritus'))
def rule_28338(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, -0.001*_local(world, agents, 'methane'))
def rule_28339(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28340(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*(_local(world, agents, 'biodiversity')-agents.survival_score))
def rule_28341(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28342(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'erosion'))
def rule_28343(world, agents):
    agents.attack_success = _delta(agents.attack_success, -0.001*_local(world, agents, 'soil_depth'))
def rule_28344(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28345(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*(_local(world, agents, 'wetland')-agents.defense_score))
def rule_28346(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28347(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_28348(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, -0.001*_local(world, agents, 'ash'))
def rule_28349(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28350(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*(_local(world, agents, 'groundwater')-agents.strategy_mixing))
def rule_28351(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28352(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'salinity'))
def rule_28353(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, -0.001*_local(world, agents, 'algae'))
def rule_28354(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28355(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*(_local(world, agents, 'deadwood')-agents.payoff))
def rule_28356(world, agents):
    agents.energy = _delta(agents.energy, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28357(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'flowers'))
def rule_28358(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, -0.001*_local(world, agents, 'seed_bank'))
def rule_28359(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28360(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*(_local(world, agents, 'surface_ice')-agents.hydration))
def rule_28361(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28362(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'surface_water'))
def rule_28363(world, agents):
    agents.health = _delta(agents.health, -0.001*_local(world, agents, 'humidity'))
def rule_28364(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28365(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*(_local(world, agents, 'rain')-agents.dehydration))
def rule_28366(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28367(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'runoff'))
def rule_28368(world, agents):
    agents.alertness = _delta(agents.alertness, -0.001*_local(world, agents, 'wind_x'))
def rule_28369(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28370(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*(_local(world, agents, 'vegetation')-agents.recovery))
def rule_28371(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28372(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'herbivore'))
def rule_28373(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, -0.001*_local(world, agents, 'predator'))
def rule_28374(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28375(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*(_local(world, agents, 'nutrients')-agents.food_access))
def rule_28376(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28377(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'oxygen'))
def rule_28378(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, -0.001*_local(world, agents, 'co2'))
def rule_28379(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28380(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*(_local(world, agents, 'ice')-agents.reputation))
def rule_28381(world, agents):
    agents.trust = _delta(agents.trust, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28382(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'detritus'))
def rule_28383(world, agents):
    agents.defection = _delta(agents.defection, -0.001*_local(world, agents, 'methane'))
def rule_28384(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28385(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*(_local(world, agents, 'biodiversity')-agents.conflict_pressure))
def rule_28386(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28387(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'erosion'))
def rule_28388(world, agents):
    agents.group_stability = _delta(agents.group_stability, -0.001*_local(world, agents, 'soil_depth'))
def rule_28389(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28390(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*(_local(world, agents, 'wetland')-agents.help_drive))
def rule_28391(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28392(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'fire_risk'))
def rule_28393(world, agents):
    agents.generosity = _delta(agents.generosity, -0.001*_local(world, agents, 'ash'))
def rule_28394(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28395(world, agents):
    agents.caution = _delta(agents.caution, 0.001*(_local(world, agents, 'groundwater')-agents.caution))
def rule_28396(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28397(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'salinity'))
def rule_28398(world, agents):
    agents.future_help = _delta(agents.future_help, -0.001*_local(world, agents, 'algae'))
def rule_28399(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28400(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*(_local(world, agents, 'deadwood')-agents.empathy))
def rule_28401(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28402(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'flowers'))
def rule_28403(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, -0.001*_local(world, agents, 'seed_bank'))
def rule_28404(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28405(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*(_local(world, agents, 'surface_ice')-agents.fire_fear))
def rule_28406(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28407(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'surface_water'))
def rule_28408(world, agents):
    agents.stress = _delta(agents.stress, -0.001*_local(world, agents, 'humidity'))
def rule_28409(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28410(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*(_local(world, agents, 'rain')-agents.neighbor_energy_gap))
def rule_28411(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28412(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'runoff'))
def rule_28413(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, -0.001*_local(world, agents, 'wind_x'))
def rule_28414(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28415(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*(_local(world, agents, 'vegetation')-agents.help_received))
def rule_28416(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28417(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'herbivore'))
def rule_28418(world, agents):
    agents.last_reward = _delta(agents.last_reward, -0.001*_local(world, agents, 'predator'))
def rule_28419(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28420(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*(_local(world, agents, 'nutrients')-agents.last_food))
def rule_28421(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28422(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'oxygen'))
def rule_28423(world, agents):
    agents.last_action = _delta(agents.last_action, -0.001*_local(world, agents, 'co2'))
def rule_28424(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28425(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*(_local(world, agents, 'ice')-agents.cooperation_score))
def rule_28426(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28427(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'detritus'))
def rule_28428(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, -0.001*_local(world, agents, 'methane'))
def rule_28429(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28430(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*(_local(world, agents, 'biodiversity')-agents.safety_score))
def rule_28431(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28432(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'erosion'))
def rule_28433(world, agents):
    agents.survival_score = _delta(agents.survival_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_28434(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28435(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*(_local(world, agents, 'wetland')-agents.help_score))
def rule_28436(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28437(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'fire_risk'))
def rule_28438(world, agents):
    agents.defense_score = _delta(agents.defense_score, -0.001*_local(world, agents, 'ash'))
def rule_28439(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28440(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*(_local(world, agents, 'groundwater')-agents.reproduction_score))
def rule_28441(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28442(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'salinity'))
def rule_28443(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, -0.001*_local(world, agents, 'algae'))
def rule_28444(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28445(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*(_local(world, agents, 'deadwood')-agents.memory_update))
def rule_28446(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28447(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'flowers'))
def rule_28448(world, agents):
    agents.payoff = _delta(agents.payoff, -0.001*_local(world, agents, 'seed_bank'))
def rule_28449(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28450(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*(_local(world, agents, 'surface_ice')-agents.energy_surplus))
def rule_28451(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28452(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'surface_water'))
def rule_28453(world, agents):
    agents.hydration = _delta(agents.hydration, -0.001*_local(world, agents, 'humidity'))
def rule_28454(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28455(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*(_local(world, agents, 'rain')-agents.hunger))
def rule_28456(world, agents):
    agents.health = _delta(agents.health, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28457(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'runoff'))
def rule_28458(world, agents):
    agents.dehydration = _delta(agents.dehydration, -0.001*_local(world, agents, 'wind_x'))
def rule_28459(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28460(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*(_local(world, agents, 'vegetation')-agents.infection_risk))
def rule_28461(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28462(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'herbivore'))
def rule_28463(world, agents):
    agents.recovery = _delta(agents.recovery, -0.001*_local(world, agents, 'predator'))
def rule_28464(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28465(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*(_local(world, agents, 'nutrients')-agents.reproduction_drive))
def rule_28466(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28467(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'oxygen'))
def rule_28468(world, agents):
    agents.food_access = _delta(agents.food_access, -0.001*_local(world, agents, 'co2'))
def rule_28469(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28470(world, agents):
    agents.stability = _delta(agents.stability, 0.001*(_local(world, agents, 'ice')-agents.stability))
def rule_28471(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28472(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'detritus'))
def rule_28473(world, agents):
    agents.reputation = _delta(agents.reputation, -0.001*_local(world, agents, 'methane'))
def rule_28474(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28475(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*(_local(world, agents, 'biodiversity')-agents.cooperation))
def rule_28476(world, agents):
    agents.defection = _delta(agents.defection, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28477(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'erosion'))
def rule_28478(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, -0.001*_local(world, agents, 'soil_depth'))
def rule_28479(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28480(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*(_local(world, agents, 'wetland')-agents.territoriality))
def rule_28481(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28482(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'fire_risk'))
def rule_28483(world, agents):
    agents.help_drive = _delta(agents.help_drive, -0.001*_local(world, agents, 'ash'))
def rule_28484(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28485(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*(_local(world, agents, 'groundwater')-agents.selfishness))
def rule_28486(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28487(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'salinity'))
def rule_28488(world, agents):
    agents.caution = _delta(agents.caution, -0.001*_local(world, agents, 'algae'))
def rule_28489(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28490(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*(_local(world, agents, 'deadwood')-agents.strategy_confidence))
def rule_28491(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28492(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'flowers'))
def rule_28493(world, agents):
    agents.empathy = _delta(agents.empathy, -0.001*_local(world, agents, 'seed_bank'))
def rule_28494(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28495(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*(_local(world, agents, 'surface_ice')-agents.defection_threshold))
def rule_28496(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28497(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'surface_water'))
def rule_28498(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, -0.001*_local(world, agents, 'humidity'))
def rule_28499(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28500(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*(_local(world, agents, 'rain')-agents.vegetation_expectation))
def rule_28501(world, agents):
    agents.stress = _delta(agents.stress, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28502(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'runoff'))
def rule_28503(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, -0.001*_local(world, agents, 'wind_x'))
def rule_28504(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28505(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*(_local(world, agents, 'vegetation')-agents.betrayal_memory))
def rule_28506(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28507(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'herbivore'))
def rule_28508(world, agents):
    agents.help_received = _delta(agents.help_received, -0.001*_local(world, agents, 'predator'))
def rule_28509(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28510(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*(_local(world, agents, 'nutrients')-agents.local_density))
def rule_28511(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28512(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'oxygen'))
def rule_28513(world, agents):
    agents.last_food = _delta(agents.last_food, -0.001*_local(world, agents, 'co2'))
def rule_28514(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28515(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*(_local(world, agents, 'ice')-agents.risk_tolerance))
def rule_28516(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28517(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'detritus'))
def rule_28518(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, -0.001*_local(world, agents, 'methane'))
def rule_28519(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28520(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*(_local(world, agents, 'biodiversity')-agents.defection_score))
def rule_28521(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28522(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'erosion'))
def rule_28523(world, agents):
    agents.safety_score = _delta(agents.safety_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_28524(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28525(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*(_local(world, agents, 'wetland')-agents.foraging_score))
def rule_28526(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28527(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_28528(world, agents):
    agents.help_score = _delta(agents.help_score, -0.001*_local(world, agents, 'ash'))
def rule_28529(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28530(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*(_local(world, agents, 'groundwater')-agents.retaliation_risk))
def rule_28531(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28532(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'salinity'))
def rule_28533(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, -0.001*_local(world, agents, 'algae'))
def rule_28534(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28535(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*(_local(world, agents, 'deadwood')-agents.strategy_persistence))
def rule_28536(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28537(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'flowers'))
def rule_28538(world, agents):
    agents.memory_update = _delta(agents.memory_update, -0.001*_local(world, agents, 'seed_bank'))
def rule_28539(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28540(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*(_local(world, agents, 'surface_ice')-agents.self_preservation))
def rule_28541(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28542(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'surface_water'))
def rule_28543(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, -0.001*_local(world, agents, 'humidity'))
def rule_28544(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28545(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*(_local(world, agents, 'rain')-agents.resource_abundance))
def rule_28546(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28547(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'runoff'))
def rule_28548(world, agents):
    agents.hunger = _delta(agents.hunger, -0.001*_local(world, agents, 'wind_x'))
def rule_28549(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28550(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*(_local(world, agents, 'vegetation')-agents.thermal_stress))
def rule_28551(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28552(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'herbivore'))
def rule_28553(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, -0.001*_local(world, agents, 'predator'))
def rule_28554(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28555(world, agents):
    agents.fear = _delta(agents.fear, 0.001*(_local(world, agents, 'nutrients')-agents.fear))
def rule_28556(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28557(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'oxygen'))
def rule_28558(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, -0.001*_local(world, agents, 'co2'))
def rule_28559(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28560(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*(_local(world, agents, 'ice')-agents.exploration_drive))
def rule_28561(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28562(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'detritus'))
def rule_28563(world, agents):
    agents.stability = _delta(agents.stability, -0.001*_local(world, agents, 'methane'))
def rule_28564(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28565(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*(_local(world, agents, 'biodiversity')-agents.social_tolerance))
def rule_28566(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28567(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'erosion'))
def rule_28568(world, agents):
    agents.cooperation = _delta(agents.cooperation, -0.001*_local(world, agents, 'soil_depth'))
def rule_28569(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28570(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*(_local(world, agents, 'wetland')-agents.aggression))
def rule_28571(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28572(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'fire_risk'))
def rule_28573(world, agents):
    agents.territoriality = _delta(agents.territoriality, -0.001*_local(world, agents, 'ash'))
def rule_28574(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28575(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*(_local(world, agents, 'groundwater')-agents.sharing_capacity))
def rule_28576(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28577(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'salinity'))
def rule_28578(world, agents):
    agents.selfishness = _delta(agents.selfishness, -0.001*_local(world, agents, 'algae'))
def rule_28579(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28580(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*(_local(world, agents, 'deadwood')-agents.gratitude))
def rule_28581(world, agents):
    agents.caution = _delta(agents.caution, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28582(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'flowers'))
def rule_28583(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, -0.001*_local(world, agents, 'seed_bank'))
def rule_28584(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28585(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*(_local(world, agents, 'surface_ice')-agents.resource_discovery))
def rule_28586(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28587(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'surface_water'))
def rule_28588(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, -0.001*_local(world, agents, 'humidity'))
def rule_28589(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28590(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*(_local(world, agents, 'rain')-agents.shelter_need))
def rule_28591(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28592(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'runoff'))
def rule_28593(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, -0.001*_local(world, agents, 'wind_x'))
def rule_28594(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28595(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*(_local(world, agents, 'vegetation')-agents.social_need))
def rule_28596(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28597(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'herbivore'))
def rule_28598(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, -0.001*_local(world, agents, 'predator'))
def rule_28599(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28600(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*(_local(world, agents, 'nutrients')-agents.cooperation_history))
def rule_28601(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28602(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'oxygen'))
def rule_28603(world, agents):
    agents.local_density = _delta(agents.local_density, -0.001*_local(world, agents, 'co2'))
def rule_28604(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28605(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*(_local(world, agents, 'ice')-agents.last_energy_delta))
def rule_28606(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28607(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'detritus'))
def rule_28608(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, -0.001*_local(world, agents, 'methane'))
def rule_28609(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28610(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*(_local(world, agents, 'biodiversity')-agents.strategy_score))
def rule_28611(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28612(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'erosion'))
def rule_28613(world, agents):
    agents.defection_score = _delta(agents.defection_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_28614(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28615(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*(_local(world, agents, 'wetland')-agents.risk_score))
def rule_28616(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28617(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_28618(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, -0.001*_local(world, agents, 'ash'))
def rule_28619(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28620(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*(_local(world, agents, 'groundwater')-agents.fitness_score))
def rule_28621(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28622(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'salinity'))
def rule_28623(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, -0.001*_local(world, agents, 'algae'))
def rule_28624(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28625(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*(_local(world, agents, 'deadwood')-agents.migration_score))
def rule_28626(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28627(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'flowers'))
def rule_28628(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, -0.001*_local(world, agents, 'seed_bank'))
def rule_28629(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28630(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*(_local(world, agents, 'surface_ice')-agents.learning_rate))
def rule_28631(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28632(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'surface_water'))
def rule_28633(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, -0.001*_local(world, agents, 'humidity'))
def rule_28634(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28635(world, agents):
    agents.energy = _delta(agents.energy, 0.001*(_local(world, agents, 'rain')-agents.energy))
def rule_28636(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28637(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'runoff'))
def rule_28638(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, -0.001*_local(world, agents, 'wind_x'))
def rule_28639(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28640(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*(_local(world, agents, 'vegetation')-agents.thirst))
def rule_28641(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28642(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'herbivore'))
def rule_28643(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, -0.001*_local(world, agents, 'predator'))
def rule_28644(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28645(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*(_local(world, agents, 'nutrients')-agents.pathogen_risk))
def rule_28646(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28647(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'oxygen'))
def rule_28648(world, agents):
    agents.fear = _delta(agents.fear, -0.001*_local(world, agents, 'co2'))
def rule_28649(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28650(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*(_local(world, agents, 'ice')-agents.metabolic_cost))
def rule_28651(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28652(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'detritus'))
def rule_28653(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, -0.001*_local(world, agents, 'methane'))
def rule_28654(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28655(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*(_local(world, agents, 'biodiversity')-agents.wealth))
def rule_28656(world, agents):
    agents.stability = _delta(agents.stability, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28657(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'erosion'))
def rule_28658(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, -0.001*_local(world, agents, 'soil_depth'))
def rule_28659(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28660(world, agents):
    agents.trust = _delta(agents.trust, 0.001*(_local(world, agents, 'wetland')-agents.trust))
def rule_28661(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28662(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'fire_risk'))
def rule_28663(world, agents):
    agents.aggression = _delta(agents.aggression, -0.001*_local(world, agents, 'ash'))
def rule_28664(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28665(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*(_local(world, agents, 'groundwater')-agents.competition_pressure))
def rule_28666(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28667(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'salinity'))
def rule_28668(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, -0.001*_local(world, agents, 'algae'))
def rule_28669(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28670(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*(_local(world, agents, 'deadwood')-agents.social_avoidance))
def rule_28671(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28672(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'flowers'))
def rule_28673(world, agents):
    agents.gratitude = _delta(agents.gratitude, -0.001*_local(world, agents, 'seed_bank'))
def rule_28674(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28675(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*(_local(world, agents, 'surface_ice')-agents.confidence))
def rule_28676(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28677(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'surface_water'))
def rule_28678(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, -0.001*_local(world, agents, 'humidity'))
def rule_28679(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28680(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*(_local(world, agents, 'rain')-agents.attack_threshold))
def rule_28681(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28682(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'runoff'))
def rule_28683(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, -0.001*_local(world, agents, 'wind_x'))
def rule_28684(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28685(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*(_local(world, agents, 'vegetation')-agents.resource_competition))
def rule_28686(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28687(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'herbivore'))
def rule_28688(world, agents):
    agents.social_need = _delta(agents.social_need, -0.001*_local(world, agents, 'predator'))
def rule_28689(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28690(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*(_local(world, agents, 'nutrients')-agents.neighbor_health_gap))
def rule_28691(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28692(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'oxygen'))
def rule_28693(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, -0.001*_local(world, agents, 'co2'))
def rule_28694(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28695(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*(_local(world, agents, 'ice')-agents.help_given))
def rule_28696(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28697(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'detritus'))
def rule_28698(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, -0.001*_local(world, agents, 'methane'))
def rule_28699(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28700(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*(_local(world, agents, 'biodiversity')-agents.last_interaction))
def rule_28701(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28702(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'erosion'))
def rule_28703(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_28704(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28705(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*(_local(world, agents, 'wetland')-agents.competition_score))
def rule_28706(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28707(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_28708(world, agents):
    agents.risk_score = _delta(agents.risk_score, -0.001*_local(world, agents, 'ash'))
def rule_28709(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28710(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*(_local(world, agents, 'groundwater')-agents.exploration_score))
def rule_28711(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28712(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'salinity'))
def rule_28713(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, -0.001*_local(world, agents, 'algae'))
def rule_28714(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28715(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*(_local(world, agents, 'deadwood')-agents.attack_success))
def rule_28716(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28717(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'flowers'))
def rule_28718(world, agents):
    agents.migration_score = _delta(agents.migration_score, -0.001*_local(world, agents, 'seed_bank'))
def rule_28719(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28720(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*(_local(world, agents, 'surface_ice')-agents.sharing_score))
def rule_28721(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28722(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'surface_water'))
def rule_28723(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, -0.001*_local(world, agents, 'humidity'))
def rule_28724(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28725(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*(_local(world, agents, 'rain')-agents.future_payoff_weight))
def rule_28726(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28727(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'runoff'))
def rule_28728(world, agents):
    agents.energy = _delta(agents.energy, -0.001*_local(world, agents, 'wind_x'))
def rule_28729(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28730(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*(_local(world, agents, 'vegetation')-agents.resource_scarcity))
def rule_28731(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28732(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'herbivore'))
def rule_28733(world, agents):
    agents.thirst = _delta(agents.thirst, -0.001*_local(world, agents, 'predator'))
def rule_28734(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28735(world, agents):
    agents.health = _delta(agents.health, 0.001*(_local(world, agents, 'nutrients')-agents.health))
def rule_28736(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28737(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'oxygen'))
def rule_28738(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, -0.001*_local(world, agents, 'co2'))
def rule_28739(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28740(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*(_local(world, agents, 'ice')-agents.alertness))
def rule_28741(world, agents):
    agents.fear = _delta(agents.fear, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28742(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'detritus'))
def rule_28743(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, -0.001*_local(world, agents, 'methane'))
def rule_28744(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28745(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*(_local(world, agents, 'biodiversity')-agents.migration_drive))
def rule_28746(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28747(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'erosion'))
def rule_28748(world, agents):
    agents.wealth = _delta(agents.wealth, -0.001*_local(world, agents, 'soil_depth'))
def rule_28749(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28750(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*(_local(world, agents, 'wetland')-agents.habitat_stress))
def rule_28751(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28752(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'fire_risk'))
def rule_28753(world, agents):
    agents.trust = _delta(agents.trust, -0.001*_local(world, agents, 'ash'))
def rule_28754(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28755(world, agents):
    agents.defection = _delta(agents.defection, 0.001*(_local(world, agents, 'groundwater')-agents.defection))
def rule_28756(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28757(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'salinity'))
def rule_28758(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, -0.001*_local(world, agents, 'algae'))
def rule_28759(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28760(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*(_local(world, agents, 'deadwood')-agents.group_stability))
def rule_28761(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28762(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'flowers'))
def rule_28763(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, -0.001*_local(world, agents, 'seed_bank'))
def rule_28764(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28765(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*(_local(world, agents, 'surface_ice')-agents.generosity))
def rule_28766(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28767(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'surface_water'))
def rule_28768(world, agents):
    agents.confidence = _delta(agents.confidence, -0.001*_local(world, agents, 'humidity'))
def rule_28769(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28770(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*(_local(world, agents, 'rain')-agents.future_help))
def rule_28771(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28772(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'runoff'))
def rule_28773(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, -0.001*_local(world, agents, 'wind_x'))
def rule_28774(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28775(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*(_local(world, agents, 'vegetation')-agents.oxygen_need))
def rule_28776(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28777(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'herbivore'))
def rule_28778(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, -0.001*_local(world, agents, 'predator'))
def rule_28779(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28780(world, agents):
    agents.stress = _delta(agents.stress, 0.001*(_local(world, agents, 'nutrients')-agents.stress))
def rule_28781(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28782(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'oxygen'))
def rule_28783(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, -0.001*_local(world, agents, 'co2'))
def rule_28784(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28785(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*(_local(world, agents, 'ice')-agents.conflict_history))
def rule_28786(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28787(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'detritus'))
def rule_28788(world, agents):
    agents.help_given = _delta(agents.help_given, -0.001*_local(world, agents, 'methane'))
def rule_28789(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28790(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*(_local(world, agents, 'biodiversity')-agents.last_reward))
def rule_28791(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28792(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'erosion'))
def rule_28793(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, -0.001*_local(world, agents, 'soil_depth'))
def rule_28794(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28795(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*(_local(world, agents, 'wetland')-agents.last_action))
def rule_28796(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28797(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_28798(world, agents):
    agents.competition_score = _delta(agents.competition_score, -0.001*_local(world, agents, 'ash'))
def rule_28799(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28800(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*(_local(world, agents, 'groundwater')-agents.reciprocity_score))
def rule_28801(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28802(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'salinity'))
def rule_28803(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, -0.001*_local(world, agents, 'algae'))
def rule_28804(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28805(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*(_local(world, agents, 'deadwood')-agents.survival_score))
def rule_28806(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28807(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'flowers'))
def rule_28808(world, agents):
    agents.attack_success = _delta(agents.attack_success, -0.001*_local(world, agents, 'seed_bank'))
def rule_28809(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28810(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*(_local(world, agents, 'surface_ice')-agents.defense_score))
def rule_28811(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28812(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'surface_water'))
def rule_28813(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, -0.001*_local(world, agents, 'humidity'))
def rule_28814(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28815(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*(_local(world, agents, 'rain')-agents.strategy_mixing))
def rule_28816(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28817(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'runoff'))
def rule_28818(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, -0.001*_local(world, agents, 'wind_x'))
def rule_28819(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28820(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*(_local(world, agents, 'vegetation')-agents.payoff))
def rule_28821(world, agents):
    agents.energy = _delta(agents.energy, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28822(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'herbivore'))
def rule_28823(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, -0.001*_local(world, agents, 'predator'))
def rule_28824(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28825(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*(_local(world, agents, 'nutrients')-agents.hydration))
def rule_28826(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28827(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'oxygen'))
def rule_28828(world, agents):
    agents.health = _delta(agents.health, -0.001*_local(world, agents, 'co2'))
def rule_28829(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28830(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*(_local(world, agents, 'ice')-agents.dehydration))
def rule_28831(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28832(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'detritus'))
def rule_28833(world, agents):
    agents.alertness = _delta(agents.alertness, -0.001*_local(world, agents, 'methane'))
def rule_28834(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28835(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*(_local(world, agents, 'biodiversity')-agents.recovery))
def rule_28836(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28837(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'erosion'))
def rule_28838(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, -0.001*_local(world, agents, 'soil_depth'))
def rule_28839(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28840(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*(_local(world, agents, 'wetland')-agents.food_access))
def rule_28841(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28842(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'fire_risk'))
def rule_28843(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, -0.001*_local(world, agents, 'ash'))
def rule_28844(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28845(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*(_local(world, agents, 'groundwater')-agents.reputation))
def rule_28846(world, agents):
    agents.trust = _delta(agents.trust, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28847(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'salinity'))
def rule_28848(world, agents):
    agents.defection = _delta(agents.defection, -0.001*_local(world, agents, 'algae'))
def rule_28849(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28850(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*(_local(world, agents, 'deadwood')-agents.conflict_pressure))
def rule_28851(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28852(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'flowers'))
def rule_28853(world, agents):
    agents.group_stability = _delta(agents.group_stability, -0.001*_local(world, agents, 'seed_bank'))
def rule_28854(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28855(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*(_local(world, agents, 'surface_ice')-agents.help_drive))
def rule_28856(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28857(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'surface_water'))
def rule_28858(world, agents):
    agents.generosity = _delta(agents.generosity, -0.001*_local(world, agents, 'humidity'))
def rule_28859(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28860(world, agents):
    agents.caution = _delta(agents.caution, 0.001*(_local(world, agents, 'rain')-agents.caution))
def rule_28861(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28862(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'runoff'))
def rule_28863(world, agents):
    agents.future_help = _delta(agents.future_help, -0.001*_local(world, agents, 'wind_x'))
def rule_28864(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28865(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*(_local(world, agents, 'vegetation')-agents.empathy))
def rule_28866(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28867(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'herbivore'))
def rule_28868(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, -0.001*_local(world, agents, 'predator'))
def rule_28869(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28870(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*(_local(world, agents, 'nutrients')-agents.fire_fear))
def rule_28871(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28872(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'oxygen'))
def rule_28873(world, agents):
    agents.stress = _delta(agents.stress, -0.001*_local(world, agents, 'co2'))
def rule_28874(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28875(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*(_local(world, agents, 'ice')-agents.neighbor_energy_gap))
def rule_28876(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28877(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'detritus'))
def rule_28878(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, -0.001*_local(world, agents, 'methane'))
def rule_28879(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28880(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*(_local(world, agents, 'biodiversity')-agents.help_received))
def rule_28881(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28882(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'erosion'))
def rule_28883(world, agents):
    agents.last_reward = _delta(agents.last_reward, -0.001*_local(world, agents, 'soil_depth'))
def rule_28884(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28885(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*(_local(world, agents, 'wetland')-agents.last_food))
def rule_28886(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28887(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'fire_risk'))
def rule_28888(world, agents):
    agents.last_action = _delta(agents.last_action, -0.001*_local(world, agents, 'ash'))
def rule_28889(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28890(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*(_local(world, agents, 'groundwater')-agents.cooperation_score))
def rule_28891(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28892(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'salinity'))
def rule_28893(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, -0.001*_local(world, agents, 'algae'))
def rule_28894(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28895(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*(_local(world, agents, 'deadwood')-agents.safety_score))
def rule_28896(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28897(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'flowers'))
def rule_28898(world, agents):
    agents.survival_score = _delta(agents.survival_score, -0.001*_local(world, agents, 'seed_bank'))
def rule_28899(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28900(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*(_local(world, agents, 'surface_ice')-agents.help_score))
def rule_28901(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28902(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'surface_water'))
def rule_28903(world, agents):
    agents.defense_score = _delta(agents.defense_score, -0.001*_local(world, agents, 'humidity'))
def rule_28904(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28905(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*(_local(world, agents, 'rain')-agents.reproduction_score))
def rule_28906(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28907(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'runoff'))
def rule_28908(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, -0.001*_local(world, agents, 'wind_x'))
def rule_28909(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28910(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*(_local(world, agents, 'vegetation')-agents.memory_update))
def rule_28911(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28912(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'herbivore'))
def rule_28913(world, agents):
    agents.payoff = _delta(agents.payoff, -0.001*_local(world, agents, 'predator'))
def rule_28914(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28915(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*(_local(world, agents, 'nutrients')-agents.energy_surplus))
def rule_28916(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28917(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'oxygen'))
def rule_28918(world, agents):
    agents.hydration = _delta(agents.hydration, -0.001*_local(world, agents, 'co2'))
def rule_28919(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28920(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*(_local(world, agents, 'ice')-agents.hunger))
def rule_28921(world, agents):
    agents.health = _delta(agents.health, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28922(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'detritus'))
def rule_28923(world, agents):
    agents.dehydration = _delta(agents.dehydration, -0.001*_local(world, agents, 'methane'))
def rule_28924(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28925(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*(_local(world, agents, 'biodiversity')-agents.infection_risk))
def rule_28926(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28927(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'erosion'))
def rule_28928(world, agents):
    agents.recovery = _delta(agents.recovery, -0.001*_local(world, agents, 'soil_depth'))
def rule_28929(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28930(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*(_local(world, agents, 'wetland')-agents.reproduction_drive))
def rule_28931(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28932(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'fire_risk'))
def rule_28933(world, agents):
    agents.food_access = _delta(agents.food_access, -0.001*_local(world, agents, 'ash'))
def rule_28934(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28935(world, agents):
    agents.stability = _delta(agents.stability, 0.001*(_local(world, agents, 'groundwater')-agents.stability))
def rule_28936(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28937(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'salinity'))
def rule_28938(world, agents):
    agents.reputation = _delta(agents.reputation, -0.001*_local(world, agents, 'algae'))
def rule_28939(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28940(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*(_local(world, agents, 'deadwood')-agents.cooperation))
def rule_28941(world, agents):
    agents.defection = _delta(agents.defection, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28942(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'flowers'))
def rule_28943(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, -0.001*_local(world, agents, 'seed_bank'))
def rule_28944(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28945(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*(_local(world, agents, 'surface_ice')-agents.territoriality))
def rule_28946(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28947(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'surface_water'))
def rule_28948(world, agents):
    agents.help_drive = _delta(agents.help_drive, -0.001*_local(world, agents, 'humidity'))
def rule_28949(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28950(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*(_local(world, agents, 'rain')-agents.selfishness))
def rule_28951(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28952(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'runoff'))
def rule_28953(world, agents):
    agents.caution = _delta(agents.caution, -0.001*_local(world, agents, 'wind_x'))
def rule_28954(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_28955(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*(_local(world, agents, 'vegetation')-agents.strategy_confidence))
def rule_28956(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_28957(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'herbivore'))
def rule_28958(world, agents):
    agents.empathy = _delta(agents.empathy, -0.001*_local(world, agents, 'predator'))
def rule_28959(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_28960(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*(_local(world, agents, 'nutrients')-agents.defection_threshold))
def rule_28961(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_28962(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'oxygen'))
def rule_28963(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, -0.001*_local(world, agents, 'co2'))
def rule_28964(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_28965(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*(_local(world, agents, 'ice')-agents.vegetation_expectation))
def rule_28966(world, agents):
    agents.stress = _delta(agents.stress, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_28967(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'detritus'))
def rule_28968(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, -0.001*_local(world, agents, 'methane'))
def rule_28969(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_28970(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*(_local(world, agents, 'biodiversity')-agents.betrayal_memory))
def rule_28971(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_28972(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'erosion'))
def rule_28973(world, agents):
    agents.help_received = _delta(agents.help_received, -0.001*_local(world, agents, 'soil_depth'))
def rule_28974(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_28975(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*(_local(world, agents, 'wetland')-agents.local_density))
def rule_28976(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_28977(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'fire_risk'))
def rule_28978(world, agents):
    agents.last_food = _delta(agents.last_food, -0.001*_local(world, agents, 'ash'))
def rule_28979(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_28980(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*(_local(world, agents, 'groundwater')-agents.risk_tolerance))
def rule_28981(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_28982(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'salinity'))
def rule_28983(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, -0.001*_local(world, agents, 'algae'))
def rule_28984(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_28985(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*(_local(world, agents, 'deadwood')-agents.defection_score))
def rule_28986(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_28987(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'flowers'))
def rule_28988(world, agents):
    agents.safety_score = _delta(agents.safety_score, -0.001*_local(world, agents, 'seed_bank'))
def rule_28989(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_28990(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*(_local(world, agents, 'surface_ice')-agents.foraging_score))
def rule_28991(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_28992(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'surface_water'))
def rule_28993(world, agents):
    agents.help_score = _delta(agents.help_score, -0.001*_local(world, agents, 'humidity'))
def rule_28994(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_28995(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*(_local(world, agents, 'rain')-agents.retaliation_risk))
def rule_28996(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_28997(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'runoff'))
def rule_28998(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, -0.001*_local(world, agents, 'wind_x'))
def rule_28999(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29000(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*(_local(world, agents, 'vegetation')-agents.strategy_persistence))
def rule_29001(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29002(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'herbivore'))
def rule_29003(world, agents):
    agents.memory_update = _delta(agents.memory_update, -0.001*_local(world, agents, 'predator'))
def rule_29004(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29005(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*(_local(world, agents, 'nutrients')-agents.self_preservation))
def rule_29006(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29007(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'oxygen'))
def rule_29008(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, -0.001*_local(world, agents, 'co2'))
def rule_29009(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29010(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*(_local(world, agents, 'ice')-agents.resource_abundance))
def rule_29011(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29012(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'detritus'))
def rule_29013(world, agents):
    agents.hunger = _delta(agents.hunger, -0.001*_local(world, agents, 'methane'))
def rule_29014(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29015(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*(_local(world, agents, 'biodiversity')-agents.thermal_stress))
def rule_29016(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29017(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'erosion'))
def rule_29018(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, -0.001*_local(world, agents, 'soil_depth'))
def rule_29019(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29020(world, agents):
    agents.fear = _delta(agents.fear, 0.001*(_local(world, agents, 'wetland')-agents.fear))
def rule_29021(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29022(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'fire_risk'))
def rule_29023(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, -0.001*_local(world, agents, 'ash'))
def rule_29024(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29025(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*(_local(world, agents, 'groundwater')-agents.exploration_drive))
def rule_29026(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29027(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'salinity'))
def rule_29028(world, agents):
    agents.stability = _delta(agents.stability, -0.001*_local(world, agents, 'algae'))
def rule_29029(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29030(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*(_local(world, agents, 'deadwood')-agents.social_tolerance))
def rule_29031(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29032(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'flowers'))
def rule_29033(world, agents):
    agents.cooperation = _delta(agents.cooperation, -0.001*_local(world, agents, 'seed_bank'))
def rule_29034(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29035(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*(_local(world, agents, 'surface_ice')-agents.aggression))
def rule_29036(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29037(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'surface_water'))
def rule_29038(world, agents):
    agents.territoriality = _delta(agents.territoriality, -0.001*_local(world, agents, 'humidity'))
def rule_29039(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29040(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*(_local(world, agents, 'rain')-agents.sharing_capacity))
def rule_29041(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29042(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'runoff'))
def rule_29043(world, agents):
    agents.selfishness = _delta(agents.selfishness, -0.001*_local(world, agents, 'wind_x'))
def rule_29044(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29045(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*(_local(world, agents, 'vegetation')-agents.gratitude))
def rule_29046(world, agents):
    agents.caution = _delta(agents.caution, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29047(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'herbivore'))
def rule_29048(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, -0.001*_local(world, agents, 'predator'))
def rule_29049(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29050(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*(_local(world, agents, 'nutrients')-agents.resource_discovery))
def rule_29051(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29052(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'oxygen'))
def rule_29053(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, -0.001*_local(world, agents, 'co2'))
def rule_29054(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29055(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*(_local(world, agents, 'ice')-agents.shelter_need))
def rule_29056(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29057(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'detritus'))
def rule_29058(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, -0.001*_local(world, agents, 'methane'))
def rule_29059(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29060(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*(_local(world, agents, 'biodiversity')-agents.social_need))
def rule_29061(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29062(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'erosion'))
def rule_29063(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, -0.001*_local(world, agents, 'soil_depth'))
def rule_29064(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29065(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*(_local(world, agents, 'wetland')-agents.cooperation_history))
def rule_29066(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29067(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'fire_risk'))
def rule_29068(world, agents):
    agents.local_density = _delta(agents.local_density, -0.001*_local(world, agents, 'ash'))
def rule_29069(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29070(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*(_local(world, agents, 'groundwater')-agents.last_energy_delta))
def rule_29071(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29072(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'salinity'))
def rule_29073(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, -0.001*_local(world, agents, 'algae'))
def rule_29074(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29075(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*(_local(world, agents, 'deadwood')-agents.strategy_score))
def rule_29076(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29077(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'flowers'))
def rule_29078(world, agents):
    agents.defection_score = _delta(agents.defection_score, -0.001*_local(world, agents, 'seed_bank'))
def rule_29079(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29080(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*(_local(world, agents, 'surface_ice')-agents.risk_score))
def rule_29081(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29082(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'surface_water'))
def rule_29083(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, -0.001*_local(world, agents, 'humidity'))
def rule_29084(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29085(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*(_local(world, agents, 'rain')-agents.fitness_score))
def rule_29086(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29087(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'runoff'))
def rule_29088(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, -0.001*_local(world, agents, 'wind_x'))
def rule_29089(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29090(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*(_local(world, agents, 'vegetation')-agents.migration_score))
def rule_29091(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29092(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29093(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, -0.001*_local(world, agents, 'predator'))
def rule_29094(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29095(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*(_local(world, agents, 'nutrients')-agents.learning_rate))
def rule_29096(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29097(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'oxygen'))
def rule_29098(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, -0.001*_local(world, agents, 'co2'))
def rule_29099(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29100(world, agents):
    agents.energy = _delta(agents.energy, 0.001*(_local(world, agents, 'ice')-agents.energy))
def rule_29101(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29102(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'detritus'))
def rule_29103(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, -0.001*_local(world, agents, 'methane'))
def rule_29104(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29105(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*(_local(world, agents, 'biodiversity')-agents.thirst))
def rule_29106(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29107(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'erosion'))
def rule_29108(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, -0.001*_local(world, agents, 'soil_depth'))
def rule_29109(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29110(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*(_local(world, agents, 'wetland')-agents.pathogen_risk))
def rule_29111(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29112(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'fire_risk'))
def rule_29113(world, agents):
    agents.fear = _delta(agents.fear, -0.001*_local(world, agents, 'ash'))
def rule_29114(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29115(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*(_local(world, agents, 'groundwater')-agents.metabolic_cost))
def rule_29116(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29117(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'salinity'))
def rule_29118(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, -0.001*_local(world, agents, 'algae'))
def rule_29119(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29120(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*(_local(world, agents, 'deadwood')-agents.wealth))
def rule_29121(world, agents):
    agents.stability = _delta(agents.stability, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29122(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'flowers'))
def rule_29123(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, -0.001*_local(world, agents, 'seed_bank'))
def rule_29124(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29125(world, agents):
    agents.trust = _delta(agents.trust, 0.001*(_local(world, agents, 'surface_ice')-agents.trust))
def rule_29126(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29127(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'surface_water'))
def rule_29128(world, agents):
    agents.aggression = _delta(agents.aggression, -0.001*_local(world, agents, 'humidity'))
def rule_29129(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29130(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*(_local(world, agents, 'rain')-agents.competition_pressure))
def rule_29131(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29132(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'runoff'))
def rule_29133(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, -0.001*_local(world, agents, 'wind_x'))
def rule_29134(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29135(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*(_local(world, agents, 'vegetation')-agents.social_avoidance))
def rule_29136(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29137(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'herbivore'))
def rule_29138(world, agents):
    agents.gratitude = _delta(agents.gratitude, -0.001*_local(world, agents, 'predator'))
def rule_29139(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29140(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*(_local(world, agents, 'nutrients')-agents.confidence))
def rule_29141(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29142(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'oxygen'))
def rule_29143(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, -0.001*_local(world, agents, 'co2'))
def rule_29144(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29145(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*(_local(world, agents, 'ice')-agents.attack_threshold))
def rule_29146(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29147(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'detritus'))
def rule_29148(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, -0.001*_local(world, agents, 'methane'))
def rule_29149(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29150(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*(_local(world, agents, 'biodiversity')-agents.resource_competition))
def rule_29151(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29152(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'erosion'))
def rule_29153(world, agents):
    agents.social_need = _delta(agents.social_need, -0.001*_local(world, agents, 'soil_depth'))
def rule_29154(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29155(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*(_local(world, agents, 'wetland')-agents.neighbor_health_gap))
def rule_29156(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29157(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'fire_risk'))
def rule_29158(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, -0.001*_local(world, agents, 'ash'))
def rule_29159(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29160(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*(_local(world, agents, 'groundwater')-agents.help_given))
def rule_29161(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29162(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'salinity'))
def rule_29163(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, -0.001*_local(world, agents, 'algae'))
def rule_29164(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29165(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*(_local(world, agents, 'deadwood')-agents.last_interaction))
def rule_29166(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29167(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'flowers'))
def rule_29168(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, -0.001*_local(world, agents, 'seed_bank'))
def rule_29169(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29170(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*(_local(world, agents, 'surface_ice')-agents.competition_score))
def rule_29171(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29172(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'surface_water'))
def rule_29173(world, agents):
    agents.risk_score = _delta(agents.risk_score, -0.001*_local(world, agents, 'humidity'))
def rule_29174(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29175(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*(_local(world, agents, 'rain')-agents.exploration_score))
def rule_29176(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29177(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'runoff'))
def rule_29178(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, -0.001*_local(world, agents, 'wind_x'))
def rule_29179(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29180(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*(_local(world, agents, 'vegetation')-agents.attack_success))
def rule_29181(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29182(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29183(world, agents):
    agents.migration_score = _delta(agents.migration_score, -0.001*_local(world, agents, 'predator'))
def rule_29184(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29185(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*(_local(world, agents, 'nutrients')-agents.sharing_score))
def rule_29186(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29187(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'oxygen'))
def rule_29188(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, -0.001*_local(world, agents, 'co2'))
def rule_29189(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29190(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*(_local(world, agents, 'ice')-agents.future_payoff_weight))
def rule_29191(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29192(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'detritus'))
def rule_29193(world, agents):
    agents.energy = _delta(agents.energy, -0.001*_local(world, agents, 'methane'))
def rule_29194(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29195(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*(_local(world, agents, 'biodiversity')-agents.resource_scarcity))
def rule_29196(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29197(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'erosion'))
def rule_29198(world, agents):
    agents.thirst = _delta(agents.thirst, -0.001*_local(world, agents, 'soil_depth'))
def rule_29199(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29200(world, agents):
    agents.health = _delta(agents.health, 0.001*(_local(world, agents, 'wetland')-agents.health))
def rule_29201(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29202(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'fire_risk'))
def rule_29203(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, -0.001*_local(world, agents, 'ash'))
def rule_29204(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29205(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*(_local(world, agents, 'groundwater')-agents.alertness))
def rule_29206(world, agents):
    agents.fear = _delta(agents.fear, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29207(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'salinity'))
def rule_29208(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, -0.001*_local(world, agents, 'algae'))
def rule_29209(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29210(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*(_local(world, agents, 'deadwood')-agents.migration_drive))
def rule_29211(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29212(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'flowers'))
def rule_29213(world, agents):
    agents.wealth = _delta(agents.wealth, -0.001*_local(world, agents, 'seed_bank'))
def rule_29214(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29215(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*(_local(world, agents, 'surface_ice')-agents.habitat_stress))
def rule_29216(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29217(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'surface_water'))
def rule_29218(world, agents):
    agents.trust = _delta(agents.trust, -0.001*_local(world, agents, 'humidity'))
def rule_29219(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29220(world, agents):
    agents.defection = _delta(agents.defection, 0.001*(_local(world, agents, 'rain')-agents.defection))
def rule_29221(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29222(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'runoff'))
def rule_29223(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, -0.001*_local(world, agents, 'wind_x'))
def rule_29224(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29225(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*(_local(world, agents, 'vegetation')-agents.group_stability))
def rule_29226(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29227(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'herbivore'))
def rule_29228(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, -0.001*_local(world, agents, 'predator'))
def rule_29229(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29230(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*(_local(world, agents, 'nutrients')-agents.generosity))
def rule_29231(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29232(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'oxygen'))
def rule_29233(world, agents):
    agents.confidence = _delta(agents.confidence, -0.001*_local(world, agents, 'co2'))
def rule_29234(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29235(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*(_local(world, agents, 'ice')-agents.future_help))
def rule_29236(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29237(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'detritus'))
def rule_29238(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, -0.001*_local(world, agents, 'methane'))
def rule_29239(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29240(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*(_local(world, agents, 'biodiversity')-agents.oxygen_need))
def rule_29241(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29242(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'erosion'))
def rule_29243(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, -0.001*_local(world, agents, 'soil_depth'))
def rule_29244(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29245(world, agents):
    agents.stress = _delta(agents.stress, 0.001*(_local(world, agents, 'wetland')-agents.stress))
def rule_29246(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29247(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'fire_risk'))
def rule_29248(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, -0.001*_local(world, agents, 'ash'))
def rule_29249(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29250(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*(_local(world, agents, 'groundwater')-agents.conflict_history))
def rule_29251(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29252(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'salinity'))
def rule_29253(world, agents):
    agents.help_given = _delta(agents.help_given, -0.001*_local(world, agents, 'algae'))
def rule_29254(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29255(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*(_local(world, agents, 'deadwood')-agents.last_reward))
def rule_29256(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29257(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'flowers'))
def rule_29258(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, -0.001*_local(world, agents, 'seed_bank'))
def rule_29259(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29260(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*(_local(world, agents, 'surface_ice')-agents.last_action))
def rule_29261(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29262(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'surface_water'))
def rule_29263(world, agents):
    agents.competition_score = _delta(agents.competition_score, -0.001*_local(world, agents, 'humidity'))
def rule_29264(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29265(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*(_local(world, agents, 'rain')-agents.reciprocity_score))
def rule_29266(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29267(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'runoff'))
def rule_29268(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, -0.001*_local(world, agents, 'wind_x'))
def rule_29269(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29270(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*(_local(world, agents, 'vegetation')-agents.survival_score))
def rule_29271(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29272(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29273(world, agents):
    agents.attack_success = _delta(agents.attack_success, -0.001*_local(world, agents, 'predator'))
def rule_29274(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29275(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*(_local(world, agents, 'nutrients')-agents.defense_score))
def rule_29276(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29277(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'oxygen'))
def rule_29278(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, -0.001*_local(world, agents, 'co2'))
def rule_29279(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29280(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*(_local(world, agents, 'ice')-agents.strategy_mixing))
def rule_29281(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29282(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'detritus'))
def rule_29283(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, -0.001*_local(world, agents, 'methane'))
def rule_29284(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29285(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*(_local(world, agents, 'biodiversity')-agents.payoff))
def rule_29286(world, agents):
    agents.energy = _delta(agents.energy, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29287(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'erosion'))
def rule_29288(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, -0.001*_local(world, agents, 'soil_depth'))
def rule_29289(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29290(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*(_local(world, agents, 'wetland')-agents.hydration))
def rule_29291(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29292(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'fire_risk'))
def rule_29293(world, agents):
    agents.health = _delta(agents.health, -0.001*_local(world, agents, 'ash'))
def rule_29294(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29295(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*(_local(world, agents, 'groundwater')-agents.dehydration))
def rule_29296(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29297(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'salinity'))
def rule_29298(world, agents):
    agents.alertness = _delta(agents.alertness, -0.001*_local(world, agents, 'algae'))
def rule_29299(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29300(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*(_local(world, agents, 'deadwood')-agents.recovery))
def rule_29301(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29302(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'flowers'))
def rule_29303(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, -0.001*_local(world, agents, 'seed_bank'))
def rule_29304(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29305(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*(_local(world, agents, 'surface_ice')-agents.food_access))
def rule_29306(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29307(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'surface_water'))
def rule_29308(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, -0.001*_local(world, agents, 'humidity'))
def rule_29309(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29310(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*(_local(world, agents, 'rain')-agents.reputation))
def rule_29311(world, agents):
    agents.trust = _delta(agents.trust, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29312(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'runoff'))
def rule_29313(world, agents):
    agents.defection = _delta(agents.defection, -0.001*_local(world, agents, 'wind_x'))
def rule_29314(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29315(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*(_local(world, agents, 'vegetation')-agents.conflict_pressure))
def rule_29316(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29317(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'herbivore'))
def rule_29318(world, agents):
    agents.group_stability = _delta(agents.group_stability, -0.001*_local(world, agents, 'predator'))
def rule_29319(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29320(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*(_local(world, agents, 'nutrients')-agents.help_drive))
def rule_29321(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29322(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'oxygen'))
def rule_29323(world, agents):
    agents.generosity = _delta(agents.generosity, -0.001*_local(world, agents, 'co2'))
def rule_29324(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29325(world, agents):
    agents.caution = _delta(agents.caution, 0.001*(_local(world, agents, 'ice')-agents.caution))
def rule_29326(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29327(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'detritus'))
def rule_29328(world, agents):
    agents.future_help = _delta(agents.future_help, -0.001*_local(world, agents, 'methane'))
def rule_29329(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29330(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*(_local(world, agents, 'biodiversity')-agents.empathy))
def rule_29331(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29332(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'erosion'))
def rule_29333(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, -0.001*_local(world, agents, 'soil_depth'))
def rule_29334(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29335(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*(_local(world, agents, 'wetland')-agents.fire_fear))
def rule_29336(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29337(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'fire_risk'))
def rule_29338(world, agents):
    agents.stress = _delta(agents.stress, -0.001*_local(world, agents, 'ash'))
def rule_29339(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29340(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*(_local(world, agents, 'groundwater')-agents.neighbor_energy_gap))
def rule_29341(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29342(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'salinity'))
def rule_29343(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, -0.001*_local(world, agents, 'algae'))
def rule_29344(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29345(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*(_local(world, agents, 'deadwood')-agents.help_received))
def rule_29346(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29347(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'flowers'))
def rule_29348(world, agents):
    agents.last_reward = _delta(agents.last_reward, -0.001*_local(world, agents, 'seed_bank'))
def rule_29349(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29350(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*(_local(world, agents, 'surface_ice')-agents.last_food))
def rule_29351(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29352(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'surface_water'))
def rule_29353(world, agents):
    agents.last_action = _delta(agents.last_action, -0.001*_local(world, agents, 'humidity'))
def rule_29354(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29355(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*(_local(world, agents, 'rain')-agents.cooperation_score))
def rule_29356(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29357(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'runoff'))
def rule_29358(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, -0.001*_local(world, agents, 'wind_x'))
def rule_29359(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29360(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*(_local(world, agents, 'vegetation')-agents.safety_score))
def rule_29361(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29362(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29363(world, agents):
    agents.survival_score = _delta(agents.survival_score, -0.001*_local(world, agents, 'predator'))
def rule_29364(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29365(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*(_local(world, agents, 'nutrients')-agents.help_score))
def rule_29366(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29367(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'oxygen'))
def rule_29368(world, agents):
    agents.defense_score = _delta(agents.defense_score, -0.001*_local(world, agents, 'co2'))
def rule_29369(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29370(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*(_local(world, agents, 'ice')-agents.reproduction_score))
def rule_29371(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29372(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'detritus'))
def rule_29373(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, -0.001*_local(world, agents, 'methane'))
def rule_29374(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29375(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*(_local(world, agents, 'biodiversity')-agents.memory_update))
def rule_29376(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29377(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'erosion'))
def rule_29378(world, agents):
    agents.payoff = _delta(agents.payoff, -0.001*_local(world, agents, 'soil_depth'))
def rule_29379(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29380(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*(_local(world, agents, 'wetland')-agents.energy_surplus))
def rule_29381(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29382(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'fire_risk'))
def rule_29383(world, agents):
    agents.hydration = _delta(agents.hydration, -0.001*_local(world, agents, 'ash'))
def rule_29384(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29385(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*(_local(world, agents, 'groundwater')-agents.hunger))
def rule_29386(world, agents):
    agents.health = _delta(agents.health, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29387(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'salinity'))
def rule_29388(world, agents):
    agents.dehydration = _delta(agents.dehydration, -0.001*_local(world, agents, 'algae'))
def rule_29389(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29390(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*(_local(world, agents, 'deadwood')-agents.infection_risk))
def rule_29391(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29392(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'flowers'))
def rule_29393(world, agents):
    agents.recovery = _delta(agents.recovery, -0.001*_local(world, agents, 'seed_bank'))
def rule_29394(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29395(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*(_local(world, agents, 'surface_ice')-agents.reproduction_drive))
def rule_29396(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29397(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'surface_water'))
def rule_29398(world, agents):
    agents.food_access = _delta(agents.food_access, -0.001*_local(world, agents, 'humidity'))
def rule_29399(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29400(world, agents):
    agents.stability = _delta(agents.stability, 0.001*(_local(world, agents, 'rain')-agents.stability))
def rule_29401(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29402(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'runoff'))
def rule_29403(world, agents):
    agents.reputation = _delta(agents.reputation, -0.001*_local(world, agents, 'wind_x'))
def rule_29404(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29405(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*(_local(world, agents, 'vegetation')-agents.cooperation))
def rule_29406(world, agents):
    agents.defection = _delta(agents.defection, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29407(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'herbivore'))
def rule_29408(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, -0.001*_local(world, agents, 'predator'))
def rule_29409(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29410(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*(_local(world, agents, 'nutrients')-agents.territoriality))
def rule_29411(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29412(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'oxygen'))
def rule_29413(world, agents):
    agents.help_drive = _delta(agents.help_drive, -0.001*_local(world, agents, 'co2'))
def rule_29414(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29415(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*(_local(world, agents, 'ice')-agents.selfishness))
def rule_29416(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29417(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'detritus'))
def rule_29418(world, agents):
    agents.caution = _delta(agents.caution, -0.001*_local(world, agents, 'methane'))
def rule_29419(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29420(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*(_local(world, agents, 'biodiversity')-agents.strategy_confidence))
def rule_29421(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29422(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'erosion'))
def rule_29423(world, agents):
    agents.empathy = _delta(agents.empathy, -0.001*_local(world, agents, 'soil_depth'))
def rule_29424(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29425(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*(_local(world, agents, 'wetland')-agents.defection_threshold))
def rule_29426(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29427(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'fire_risk'))
def rule_29428(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, -0.001*_local(world, agents, 'ash'))
def rule_29429(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29430(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*(_local(world, agents, 'groundwater')-agents.vegetation_expectation))
def rule_29431(world, agents):
    agents.stress = _delta(agents.stress, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29432(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'salinity'))
def rule_29433(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, -0.001*_local(world, agents, 'algae'))
def rule_29434(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29435(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*(_local(world, agents, 'deadwood')-agents.betrayal_memory))
def rule_29436(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29437(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'flowers'))
def rule_29438(world, agents):
    agents.help_received = _delta(agents.help_received, -0.001*_local(world, agents, 'seed_bank'))
def rule_29439(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29440(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*(_local(world, agents, 'surface_ice')-agents.local_density))
def rule_29441(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29442(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'surface_water'))
def rule_29443(world, agents):
    agents.last_food = _delta(agents.last_food, -0.001*_local(world, agents, 'humidity'))
def rule_29444(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29445(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*(_local(world, agents, 'rain')-agents.risk_tolerance))
def rule_29446(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29447(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'runoff'))
def rule_29448(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, -0.001*_local(world, agents, 'wind_x'))
def rule_29449(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29450(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*(_local(world, agents, 'vegetation')-agents.defection_score))
def rule_29451(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29452(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29453(world, agents):
    agents.safety_score = _delta(agents.safety_score, -0.001*_local(world, agents, 'predator'))
def rule_29454(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29455(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*(_local(world, agents, 'nutrients')-agents.foraging_score))
def rule_29456(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29457(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'oxygen'))
def rule_29458(world, agents):
    agents.help_score = _delta(agents.help_score, -0.001*_local(world, agents, 'co2'))
def rule_29459(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29460(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*(_local(world, agents, 'ice')-agents.retaliation_risk))
def rule_29461(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29462(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'detritus'))
def rule_29463(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, -0.001*_local(world, agents, 'methane'))
def rule_29464(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29465(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*(_local(world, agents, 'biodiversity')-agents.strategy_persistence))
def rule_29466(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29467(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'erosion'))
def rule_29468(world, agents):
    agents.memory_update = _delta(agents.memory_update, -0.001*_local(world, agents, 'soil_depth'))
def rule_29469(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29470(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*(_local(world, agents, 'wetland')-agents.self_preservation))
def rule_29471(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29472(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'fire_risk'))
def rule_29473(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, -0.001*_local(world, agents, 'ash'))
def rule_29474(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29475(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*(_local(world, agents, 'groundwater')-agents.resource_abundance))
def rule_29476(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29477(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'salinity'))
def rule_29478(world, agents):
    agents.hunger = _delta(agents.hunger, -0.001*_local(world, agents, 'algae'))
def rule_29479(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29480(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*(_local(world, agents, 'deadwood')-agents.thermal_stress))
def rule_29481(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29482(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'flowers'))
def rule_29483(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, -0.001*_local(world, agents, 'seed_bank'))
def rule_29484(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29485(world, agents):
    agents.fear = _delta(agents.fear, 0.001*(_local(world, agents, 'surface_ice')-agents.fear))
def rule_29486(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29487(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'surface_water'))
def rule_29488(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, -0.001*_local(world, agents, 'humidity'))
def rule_29489(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29490(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*(_local(world, agents, 'rain')-agents.exploration_drive))
def rule_29491(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29492(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'runoff'))
def rule_29493(world, agents):
    agents.stability = _delta(agents.stability, -0.001*_local(world, agents, 'wind_x'))
def rule_29494(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29495(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*(_local(world, agents, 'vegetation')-agents.social_tolerance))
def rule_29496(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29497(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'herbivore'))
def rule_29498(world, agents):
    agents.cooperation = _delta(agents.cooperation, -0.001*_local(world, agents, 'predator'))
def rule_29499(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29500(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*(_local(world, agents, 'nutrients')-agents.aggression))
def rule_29501(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29502(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'oxygen'))
def rule_29503(world, agents):
    agents.territoriality = _delta(agents.territoriality, -0.001*_local(world, agents, 'co2'))
def rule_29504(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29505(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*(_local(world, agents, 'ice')-agents.sharing_capacity))
def rule_29506(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29507(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'detritus'))
def rule_29508(world, agents):
    agents.selfishness = _delta(agents.selfishness, -0.001*_local(world, agents, 'methane'))
def rule_29509(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29510(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*(_local(world, agents, 'biodiversity')-agents.gratitude))
def rule_29511(world, agents):
    agents.caution = _delta(agents.caution, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29512(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'erosion'))
def rule_29513(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, -0.001*_local(world, agents, 'soil_depth'))
def rule_29514(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29515(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*(_local(world, agents, 'wetland')-agents.resource_discovery))
def rule_29516(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29517(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'fire_risk'))
def rule_29518(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, -0.001*_local(world, agents, 'ash'))
def rule_29519(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29520(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*(_local(world, agents, 'groundwater')-agents.shelter_need))
def rule_29521(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29522(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'salinity'))
def rule_29523(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, -0.001*_local(world, agents, 'algae'))
def rule_29524(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29525(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*(_local(world, agents, 'deadwood')-agents.social_need))
def rule_29526(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29527(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'flowers'))
def rule_29528(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, -0.001*_local(world, agents, 'seed_bank'))
def rule_29529(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29530(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*(_local(world, agents, 'surface_ice')-agents.cooperation_history))
def rule_29531(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29532(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'surface_water'))
def rule_29533(world, agents):
    agents.local_density = _delta(agents.local_density, -0.001*_local(world, agents, 'humidity'))
def rule_29534(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29535(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*(_local(world, agents, 'rain')-agents.last_energy_delta))
def rule_29536(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29537(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'runoff'))
def rule_29538(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, -0.001*_local(world, agents, 'wind_x'))
def rule_29539(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29540(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*(_local(world, agents, 'vegetation')-agents.strategy_score))
def rule_29541(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29542(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'herbivore'))
def rule_29543(world, agents):
    agents.defection_score = _delta(agents.defection_score, -0.001*_local(world, agents, 'predator'))
def rule_29544(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29545(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*(_local(world, agents, 'nutrients')-agents.risk_score))
def rule_29546(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29547(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'oxygen'))
def rule_29548(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, -0.001*_local(world, agents, 'co2'))
def rule_29549(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29550(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*(_local(world, agents, 'ice')-agents.fitness_score))
def rule_29551(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29552(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'detritus'))
def rule_29553(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, -0.001*_local(world, agents, 'methane'))
def rule_29554(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29555(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*(_local(world, agents, 'biodiversity')-agents.migration_score))
def rule_29556(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29557(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'erosion'))
def rule_29558(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, -0.001*_local(world, agents, 'soil_depth'))
def rule_29559(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29560(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*(_local(world, agents, 'wetland')-agents.learning_rate))
def rule_29561(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29562(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'fire_risk'))
def rule_29563(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, -0.001*_local(world, agents, 'ash'))
def rule_29564(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29565(world, agents):
    agents.energy = _delta(agents.energy, 0.001*(_local(world, agents, 'groundwater')-agents.energy))
def rule_29566(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29567(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'salinity'))
def rule_29568(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, -0.001*_local(world, agents, 'algae'))
def rule_29569(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29570(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*(_local(world, agents, 'deadwood')-agents.thirst))
def rule_29571(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29572(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'flowers'))
def rule_29573(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, -0.001*_local(world, agents, 'seed_bank'))
def rule_29574(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29575(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*(_local(world, agents, 'surface_ice')-agents.pathogen_risk))
def rule_29576(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29577(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'surface_water'))
def rule_29578(world, agents):
    agents.fear = _delta(agents.fear, -0.001*_local(world, agents, 'humidity'))
def rule_29579(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29580(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*(_local(world, agents, 'rain')-agents.metabolic_cost))
def rule_29581(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29582(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'runoff'))
def rule_29583(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, -0.001*_local(world, agents, 'wind_x'))
def rule_29584(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29585(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*(_local(world, agents, 'vegetation')-agents.wealth))
def rule_29586(world, agents):
    agents.stability = _delta(agents.stability, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29587(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'herbivore'))
def rule_29588(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, -0.001*_local(world, agents, 'predator'))
def rule_29589(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29590(world, agents):
    agents.trust = _delta(agents.trust, 0.001*(_local(world, agents, 'nutrients')-agents.trust))
def rule_29591(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29592(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'oxygen'))
def rule_29593(world, agents):
    agents.aggression = _delta(agents.aggression, -0.001*_local(world, agents, 'co2'))
def rule_29594(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29595(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*(_local(world, agents, 'ice')-agents.competition_pressure))
def rule_29596(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29597(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'detritus'))
def rule_29598(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, -0.001*_local(world, agents, 'methane'))
def rule_29599(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29600(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*(_local(world, agents, 'biodiversity')-agents.social_avoidance))
def rule_29601(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29602(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'erosion'))
def rule_29603(world, agents):
    agents.gratitude = _delta(agents.gratitude, -0.001*_local(world, agents, 'soil_depth'))
def rule_29604(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29605(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*(_local(world, agents, 'wetland')-agents.confidence))
def rule_29606(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29607(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'fire_risk'))
def rule_29608(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, -0.001*_local(world, agents, 'ash'))
def rule_29609(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29610(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*(_local(world, agents, 'groundwater')-agents.attack_threshold))
def rule_29611(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29612(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'salinity'))
def rule_29613(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, -0.001*_local(world, agents, 'algae'))
def rule_29614(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29615(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*(_local(world, agents, 'deadwood')-agents.resource_competition))
def rule_29616(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29617(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'flowers'))
def rule_29618(world, agents):
    agents.social_need = _delta(agents.social_need, -0.001*_local(world, agents, 'seed_bank'))
def rule_29619(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29620(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*(_local(world, agents, 'surface_ice')-agents.neighbor_health_gap))
def rule_29621(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29622(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'surface_water'))
def rule_29623(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, -0.001*_local(world, agents, 'humidity'))
def rule_29624(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29625(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*(_local(world, agents, 'rain')-agents.help_given))
def rule_29626(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29627(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'runoff'))
def rule_29628(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, -0.001*_local(world, agents, 'wind_x'))
def rule_29629(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29630(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*(_local(world, agents, 'vegetation')-agents.last_interaction))
def rule_29631(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29632(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*_local(world, agents, 'herbivore'))
def rule_29633(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, -0.001*_local(world, agents, 'predator'))
def rule_29634(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29635(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*(_local(world, agents, 'nutrients')-agents.competition_score))
def rule_29636(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29637(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*_local(world, agents, 'oxygen'))
def rule_29638(world, agents):
    agents.risk_score = _delta(agents.risk_score, -0.001*_local(world, agents, 'co2'))
def rule_29639(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29640(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*(_local(world, agents, 'ice')-agents.exploration_score))
def rule_29641(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29642(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*_local(world, agents, 'detritus'))
def rule_29643(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, -0.001*_local(world, agents, 'methane'))
def rule_29644(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29645(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*(_local(world, agents, 'biodiversity')-agents.attack_success))
def rule_29646(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29647(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*_local(world, agents, 'erosion'))
def rule_29648(world, agents):
    agents.migration_score = _delta(agents.migration_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_29649(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29650(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*(_local(world, agents, 'wetland')-agents.sharing_score))
def rule_29651(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29652(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*_local(world, agents, 'fire_risk'))
def rule_29653(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, -0.001*_local(world, agents, 'ash'))
def rule_29654(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29655(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*(_local(world, agents, 'groundwater')-agents.future_payoff_weight))
def rule_29656(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29657(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*_local(world, agents, 'salinity'))
def rule_29658(world, agents):
    agents.energy = _delta(agents.energy, -0.001*_local(world, agents, 'algae'))
def rule_29659(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29660(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*(_local(world, agents, 'deadwood')-agents.resource_scarcity))
def rule_29661(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29662(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*_local(world, agents, 'flowers'))
def rule_29663(world, agents):
    agents.thirst = _delta(agents.thirst, -0.001*_local(world, agents, 'seed_bank'))
def rule_29664(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29665(world, agents):
    agents.health = _delta(agents.health, 0.001*(_local(world, agents, 'surface_ice')-agents.health))
def rule_29666(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29667(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*_local(world, agents, 'surface_water'))
def rule_29668(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, -0.001*_local(world, agents, 'humidity'))
def rule_29669(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29670(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*(_local(world, agents, 'rain')-agents.alertness))
def rule_29671(world, agents):
    agents.fear = _delta(agents.fear, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29672(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*_local(world, agents, 'runoff'))
def rule_29673(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, -0.001*_local(world, agents, 'wind_x'))
def rule_29674(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29675(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*(_local(world, agents, 'vegetation')-agents.migration_drive))
def rule_29676(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29677(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*_local(world, agents, 'herbivore'))
def rule_29678(world, agents):
    agents.wealth = _delta(agents.wealth, -0.001*_local(world, agents, 'predator'))
def rule_29679(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29680(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*(_local(world, agents, 'nutrients')-agents.habitat_stress))
def rule_29681(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29682(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*_local(world, agents, 'oxygen'))
def rule_29683(world, agents):
    agents.trust = _delta(agents.trust, -0.001*_local(world, agents, 'co2'))
def rule_29684(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29685(world, agents):
    agents.defection = _delta(agents.defection, 0.001*(_local(world, agents, 'ice')-agents.defection))
def rule_29686(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29687(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*_local(world, agents, 'detritus'))
def rule_29688(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, -0.001*_local(world, agents, 'methane'))
def rule_29689(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29690(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*(_local(world, agents, 'biodiversity')-agents.group_stability))
def rule_29691(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29692(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*_local(world, agents, 'erosion'))
def rule_29693(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, -0.001*_local(world, agents, 'soil_depth'))
def rule_29694(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29695(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*(_local(world, agents, 'wetland')-agents.generosity))
def rule_29696(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29697(world, agents):
    agents.caution = _delta(agents.caution, 0.001*_local(world, agents, 'fire_risk'))
def rule_29698(world, agents):
    agents.confidence = _delta(agents.confidence, -0.001*_local(world, agents, 'ash'))
def rule_29699(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29700(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*(_local(world, agents, 'groundwater')-agents.future_help))
def rule_29701(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29702(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*_local(world, agents, 'salinity'))
def rule_29703(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, -0.001*_local(world, agents, 'algae'))
def rule_29704(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29705(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*(_local(world, agents, 'deadwood')-agents.oxygen_need))
def rule_29706(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29707(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*_local(world, agents, 'flowers'))
def rule_29708(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, -0.001*_local(world, agents, 'seed_bank'))
def rule_29709(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29710(world, agents):
    agents.stress = _delta(agents.stress, 0.001*(_local(world, agents, 'surface_ice')-agents.stress))
def rule_29711(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29712(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*_local(world, agents, 'surface_water'))
def rule_29713(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, -0.001*_local(world, agents, 'humidity'))
def rule_29714(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29715(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*(_local(world, agents, 'rain')-agents.conflict_history))
def rule_29716(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29717(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*_local(world, agents, 'runoff'))
def rule_29718(world, agents):
    agents.help_given = _delta(agents.help_given, -0.001*_local(world, agents, 'wind_x'))
def rule_29719(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29720(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*(_local(world, agents, 'vegetation')-agents.last_reward))
def rule_29721(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29722(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*_local(world, agents, 'herbivore'))
def rule_29723(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, -0.001*_local(world, agents, 'predator'))
def rule_29724(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29725(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*(_local(world, agents, 'nutrients')-agents.last_action))
def rule_29726(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29727(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*_local(world, agents, 'oxygen'))
def rule_29728(world, agents):
    agents.competition_score = _delta(agents.competition_score, -0.001*_local(world, agents, 'co2'))
def rule_29729(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29730(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*(_local(world, agents, 'ice')-agents.reciprocity_score))
def rule_29731(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29732(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*_local(world, agents, 'detritus'))
def rule_29733(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, -0.001*_local(world, agents, 'methane'))
def rule_29734(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29735(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*(_local(world, agents, 'biodiversity')-agents.survival_score))
def rule_29736(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29737(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*_local(world, agents, 'erosion'))
def rule_29738(world, agents):
    agents.attack_success = _delta(agents.attack_success, -0.001*_local(world, agents, 'soil_depth'))
def rule_29739(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29740(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*(_local(world, agents, 'wetland')-agents.defense_score))
def rule_29741(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29742(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_29743(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, -0.001*_local(world, agents, 'ash'))
def rule_29744(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29745(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*(_local(world, agents, 'groundwater')-agents.strategy_mixing))
def rule_29746(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29747(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*_local(world, agents, 'salinity'))
def rule_29748(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, -0.001*_local(world, agents, 'algae'))
def rule_29749(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29750(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*(_local(world, agents, 'deadwood')-agents.payoff))
def rule_29751(world, agents):
    agents.energy = _delta(agents.energy, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29752(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*_local(world, agents, 'flowers'))
def rule_29753(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, -0.001*_local(world, agents, 'seed_bank'))
def rule_29754(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29755(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*(_local(world, agents, 'surface_ice')-agents.hydration))
def rule_29756(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29757(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*_local(world, agents, 'surface_water'))
def rule_29758(world, agents):
    agents.health = _delta(agents.health, -0.001*_local(world, agents, 'humidity'))
def rule_29759(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29760(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*(_local(world, agents, 'rain')-agents.dehydration))
def rule_29761(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29762(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*_local(world, agents, 'runoff'))
def rule_29763(world, agents):
    agents.alertness = _delta(agents.alertness, -0.001*_local(world, agents, 'wind_x'))
def rule_29764(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29765(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*(_local(world, agents, 'vegetation')-agents.recovery))
def rule_29766(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29767(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*_local(world, agents, 'herbivore'))
def rule_29768(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, -0.001*_local(world, agents, 'predator'))
def rule_29769(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29770(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*(_local(world, agents, 'nutrients')-agents.food_access))
def rule_29771(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29772(world, agents):
    agents.stability = _delta(agents.stability, 0.001*_local(world, agents, 'oxygen'))
def rule_29773(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, -0.001*_local(world, agents, 'co2'))
def rule_29774(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29775(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*(_local(world, agents, 'ice')-agents.reputation))
def rule_29776(world, agents):
    agents.trust = _delta(agents.trust, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29777(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*_local(world, agents, 'detritus'))
def rule_29778(world, agents):
    agents.defection = _delta(agents.defection, -0.001*_local(world, agents, 'methane'))
def rule_29779(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29780(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*(_local(world, agents, 'biodiversity')-agents.conflict_pressure))
def rule_29781(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29782(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*_local(world, agents, 'erosion'))
def rule_29783(world, agents):
    agents.group_stability = _delta(agents.group_stability, -0.001*_local(world, agents, 'soil_depth'))
def rule_29784(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29785(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*(_local(world, agents, 'wetland')-agents.help_drive))
def rule_29786(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29787(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*_local(world, agents, 'fire_risk'))
def rule_29788(world, agents):
    agents.generosity = _delta(agents.generosity, -0.001*_local(world, agents, 'ash'))
def rule_29789(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29790(world, agents):
    agents.caution = _delta(agents.caution, 0.001*(_local(world, agents, 'groundwater')-agents.caution))
def rule_29791(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29792(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*_local(world, agents, 'salinity'))
def rule_29793(world, agents):
    agents.future_help = _delta(agents.future_help, -0.001*_local(world, agents, 'algae'))
def rule_29794(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29795(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*(_local(world, agents, 'deadwood')-agents.empathy))
def rule_29796(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29797(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*_local(world, agents, 'flowers'))
def rule_29798(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, -0.001*_local(world, agents, 'seed_bank'))
def rule_29799(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29800(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*(_local(world, agents, 'surface_ice')-agents.fire_fear))
def rule_29801(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29802(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*_local(world, agents, 'surface_water'))
def rule_29803(world, agents):
    agents.stress = _delta(agents.stress, -0.001*_local(world, agents, 'humidity'))
def rule_29804(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29805(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*(_local(world, agents, 'rain')-agents.neighbor_energy_gap))
def rule_29806(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29807(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*_local(world, agents, 'runoff'))
def rule_29808(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, -0.001*_local(world, agents, 'wind_x'))
def rule_29809(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29810(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*(_local(world, agents, 'vegetation')-agents.help_received))
def rule_29811(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29812(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*_local(world, agents, 'herbivore'))
def rule_29813(world, agents):
    agents.last_reward = _delta(agents.last_reward, -0.001*_local(world, agents, 'predator'))
def rule_29814(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29815(world, agents):
    agents.last_food = _delta(agents.last_food, 0.001*(_local(world, agents, 'nutrients')-agents.last_food))
def rule_29816(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29817(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*_local(world, agents, 'oxygen'))
def rule_29818(world, agents):
    agents.last_action = _delta(agents.last_action, -0.001*_local(world, agents, 'co2'))
def rule_29819(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29820(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, 0.001*(_local(world, agents, 'ice')-agents.cooperation_score))
def rule_29821(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29822(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*_local(world, agents, 'detritus'))
def rule_29823(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, -0.001*_local(world, agents, 'methane'))
def rule_29824(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29825(world, agents):
    agents.safety_score = _delta(agents.safety_score, 0.001*(_local(world, agents, 'biodiversity')-agents.safety_score))
def rule_29826(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29827(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*_local(world, agents, 'erosion'))
def rule_29828(world, agents):
    agents.survival_score = _delta(agents.survival_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_29829(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29830(world, agents):
    agents.help_score = _delta(agents.help_score, 0.001*(_local(world, agents, 'wetland')-agents.help_score))
def rule_29831(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29832(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*_local(world, agents, 'fire_risk'))
def rule_29833(world, agents):
    agents.defense_score = _delta(agents.defense_score, -0.001*_local(world, agents, 'ash'))
def rule_29834(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29835(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, 0.001*(_local(world, agents, 'groundwater')-agents.reproduction_score))
def rule_29836(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29837(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*_local(world, agents, 'salinity'))
def rule_29838(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, -0.001*_local(world, agents, 'algae'))
def rule_29839(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29840(world, agents):
    agents.memory_update = _delta(agents.memory_update, 0.001*(_local(world, agents, 'deadwood')-agents.memory_update))
def rule_29841(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29842(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*_local(world, agents, 'flowers'))
def rule_29843(world, agents):
    agents.payoff = _delta(agents.payoff, -0.001*_local(world, agents, 'seed_bank'))
def rule_29844(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29845(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, 0.001*(_local(world, agents, 'surface_ice')-agents.energy_surplus))
def rule_29846(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29847(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*_local(world, agents, 'surface_water'))
def rule_29848(world, agents):
    agents.hydration = _delta(agents.hydration, -0.001*_local(world, agents, 'humidity'))
def rule_29849(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29850(world, agents):
    agents.hunger = _delta(agents.hunger, 0.001*(_local(world, agents, 'rain')-agents.hunger))
def rule_29851(world, agents):
    agents.health = _delta(agents.health, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29852(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*_local(world, agents, 'runoff'))
def rule_29853(world, agents):
    agents.dehydration = _delta(agents.dehydration, -0.001*_local(world, agents, 'wind_x'))
def rule_29854(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29855(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, 0.001*(_local(world, agents, 'vegetation')-agents.infection_risk))
def rule_29856(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29857(world, agents):
    agents.fear = _delta(agents.fear, 0.001*_local(world, agents, 'herbivore'))
def rule_29858(world, agents):
    agents.recovery = _delta(agents.recovery, -0.001*_local(world, agents, 'predator'))
def rule_29859(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29860(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, 0.001*(_local(world, agents, 'nutrients')-agents.reproduction_drive))
def rule_29861(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29862(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*_local(world, agents, 'oxygen'))
def rule_29863(world, agents):
    agents.food_access = _delta(agents.food_access, -0.001*_local(world, agents, 'co2'))
def rule_29864(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29865(world, agents):
    agents.stability = _delta(agents.stability, 0.001*(_local(world, agents, 'ice')-agents.stability))
def rule_29866(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29867(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*_local(world, agents, 'detritus'))
def rule_29868(world, agents):
    agents.reputation = _delta(agents.reputation, -0.001*_local(world, agents, 'methane'))
def rule_29869(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29870(world, agents):
    agents.cooperation = _delta(agents.cooperation, 0.001*(_local(world, agents, 'biodiversity')-agents.cooperation))
def rule_29871(world, agents):
    agents.defection = _delta(agents.defection, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29872(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*_local(world, agents, 'erosion'))
def rule_29873(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, -0.001*_local(world, agents, 'soil_depth'))
def rule_29874(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29875(world, agents):
    agents.territoriality = _delta(agents.territoriality, 0.001*(_local(world, agents, 'wetland')-agents.territoriality))
def rule_29876(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29877(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*_local(world, agents, 'fire_risk'))
def rule_29878(world, agents):
    agents.help_drive = _delta(agents.help_drive, -0.001*_local(world, agents, 'ash'))
def rule_29879(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29880(world, agents):
    agents.selfishness = _delta(agents.selfishness, 0.001*(_local(world, agents, 'groundwater')-agents.selfishness))
def rule_29881(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29882(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*_local(world, agents, 'salinity'))
def rule_29883(world, agents):
    agents.caution = _delta(agents.caution, -0.001*_local(world, agents, 'algae'))
def rule_29884(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29885(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, 0.001*(_local(world, agents, 'deadwood')-agents.strategy_confidence))
def rule_29886(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29887(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*_local(world, agents, 'flowers'))
def rule_29888(world, agents):
    agents.empathy = _delta(agents.empathy, -0.001*_local(world, agents, 'seed_bank'))
def rule_29889(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29890(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, 0.001*(_local(world, agents, 'surface_ice')-agents.defection_threshold))
def rule_29891(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29892(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*_local(world, agents, 'surface_water'))
def rule_29893(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, -0.001*_local(world, agents, 'humidity'))
def rule_29894(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29895(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, 0.001*(_local(world, agents, 'rain')-agents.vegetation_expectation))
def rule_29896(world, agents):
    agents.stress = _delta(agents.stress, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29897(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*_local(world, agents, 'runoff'))
def rule_29898(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, -0.001*_local(world, agents, 'wind_x'))
def rule_29899(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29900(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, 0.001*(_local(world, agents, 'vegetation')-agents.betrayal_memory))
def rule_29901(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29902(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*_local(world, agents, 'herbivore'))
def rule_29903(world, agents):
    agents.help_received = _delta(agents.help_received, -0.001*_local(world, agents, 'predator'))
def rule_29904(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29905(world, agents):
    agents.local_density = _delta(agents.local_density, 0.001*(_local(world, agents, 'nutrients')-agents.local_density))
def rule_29906(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29907(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*_local(world, agents, 'oxygen'))
def rule_29908(world, agents):
    agents.last_food = _delta(agents.last_food, -0.001*_local(world, agents, 'co2'))
def rule_29909(world, agents):
    agents.last_interaction = _delta(agents.last_interaction, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29910(world, agents):
    agents.risk_tolerance = _delta(agents.risk_tolerance, 0.001*(_local(world, agents, 'ice')-agents.risk_tolerance))
def rule_29911(world, agents):
    agents.last_action = _delta(agents.last_action, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29912(world, agents):
    agents.strategy_score = _delta(agents.strategy_score, 0.001*_local(world, agents, 'detritus'))
def rule_29913(world, agents):
    agents.cooperation_score = _delta(agents.cooperation_score, -0.001*_local(world, agents, 'methane'))
def rule_29914(world, agents):
    agents.competition_score = _delta(agents.competition_score, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29915(world, agents):
    agents.defection_score = _delta(agents.defection_score, 0.001*(_local(world, agents, 'biodiversity')-agents.defection_score))
def rule_29916(world, agents):
    agents.reciprocity_score = _delta(agents.reciprocity_score, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29917(world, agents):
    agents.risk_score = _delta(agents.risk_score, 0.001*_local(world, agents, 'erosion'))
def rule_29918(world, agents):
    agents.safety_score = _delta(agents.safety_score, -0.001*_local(world, agents, 'soil_depth'))
def rule_29919(world, agents):
    agents.exploration_score = _delta(agents.exploration_score, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29920(world, agents):
    agents.foraging_score = _delta(agents.foraging_score, 0.001*(_local(world, agents, 'wetland')-agents.foraging_score))
def rule_29921(world, agents):
    agents.survival_score = _delta(agents.survival_score, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29922(world, agents):
    agents.fitness_score = _delta(agents.fitness_score, 0.001*_local(world, agents, 'fire_risk'))
def rule_29923(world, agents):
    agents.help_score = _delta(agents.help_score, -0.001*_local(world, agents, 'ash'))
def rule_29924(world, agents):
    agents.attack_success = _delta(agents.attack_success, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29925(world, agents):
    agents.retaliation_risk = _delta(agents.retaliation_risk, 0.001*(_local(world, agents, 'groundwater')-agents.retaliation_risk))
def rule_29926(world, agents):
    agents.defense_score = _delta(agents.defense_score, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29927(world, agents):
    agents.migration_score = _delta(agents.migration_score, 0.001*_local(world, agents, 'salinity'))
def rule_29928(world, agents):
    agents.reproduction_score = _delta(agents.reproduction_score, -0.001*_local(world, agents, 'algae'))
def rule_29929(world, agents):
    agents.sharing_score = _delta(agents.sharing_score, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29930(world, agents):
    agents.strategy_persistence = _delta(agents.strategy_persistence, 0.001*(_local(world, agents, 'deadwood')-agents.strategy_persistence))
def rule_29931(world, agents):
    agents.strategy_mixing = _delta(agents.strategy_mixing, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29932(world, agents):
    agents.learning_rate = _delta(agents.learning_rate, 0.001*_local(world, agents, 'flowers'))
def rule_29933(world, agents):
    agents.memory_update = _delta(agents.memory_update, -0.001*_local(world, agents, 'seed_bank'))
def rule_29934(world, agents):
    agents.future_payoff_weight = _delta(agents.future_payoff_weight, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29935(world, agents):
    agents.self_preservation = _delta(agents.self_preservation, 0.001*(_local(world, agents, 'surface_ice')-agents.self_preservation))
def rule_29936(world, agents):
    agents.payoff = _delta(agents.payoff, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29937(world, agents):
    agents.energy = _delta(agents.energy, 0.001*_local(world, agents, 'surface_water'))
def rule_29938(world, agents):
    agents.energy_surplus = _delta(agents.energy_surplus, -0.001*_local(world, agents, 'humidity'))
def rule_29939(world, agents):
    agents.resource_scarcity = _delta(agents.resource_scarcity, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29940(world, agents):
    agents.resource_abundance = _delta(agents.resource_abundance, 0.001*(_local(world, agents, 'rain')-agents.resource_abundance))
def rule_29941(world, agents):
    agents.hydration = _delta(agents.hydration, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29942(world, agents):
    agents.thirst = _delta(agents.thirst, 0.001*_local(world, agents, 'runoff'))
def rule_29943(world, agents):
    agents.hunger = _delta(agents.hunger, -0.001*_local(world, agents, 'wind_x'))
def rule_29944(world, agents):
    agents.health = _delta(agents.health, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29945(world, agents):
    agents.thermal_stress = _delta(agents.thermal_stress, 0.001*(_local(world, agents, 'vegetation')-agents.thermal_stress))
def rule_29946(world, agents):
    agents.dehydration = _delta(agents.dehydration, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29947(world, agents):
    agents.pathogen_risk = _delta(agents.pathogen_risk, 0.001*_local(world, agents, 'herbivore'))
def rule_29948(world, agents):
    agents.infection_risk = _delta(agents.infection_risk, -0.001*_local(world, agents, 'predator'))
def rule_29949(world, agents):
    agents.alertness = _delta(agents.alertness, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29950(world, agents):
    agents.fear = _delta(agents.fear, 0.001*(_local(world, agents, 'nutrients')-agents.fear))
def rule_29951(world, agents):
    agents.recovery = _delta(agents.recovery, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29952(world, agents):
    agents.metabolic_cost = _delta(agents.metabolic_cost, 0.001*_local(world, agents, 'oxygen'))
def rule_29953(world, agents):
    agents.reproduction_drive = _delta(agents.reproduction_drive, -0.001*_local(world, agents, 'co2'))
def rule_29954(world, agents):
    agents.migration_drive = _delta(agents.migration_drive, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_29955(world, agents):
    agents.exploration_drive = _delta(agents.exploration_drive, 0.001*(_local(world, agents, 'ice')-agents.exploration_drive))
def rule_29956(world, agents):
    agents.food_access = _delta(agents.food_access, 0.001*torch.tanh(_local(world, agents, 'evaporation')))
def rule_29957(world, agents):
    agents.wealth = _delta(agents.wealth, 0.001*_local(world, agents, 'detritus'))
def rule_29958(world, agents):
    agents.stability = _delta(agents.stability, -0.001*_local(world, agents, 'methane'))
def rule_29959(world, agents):
    agents.habitat_stress = _delta(agents.habitat_stress, 0.001*_local(world, agents, 'pathogen_load')*_local(world, agents, 'pathogen_load'))
def rule_29960(world, agents):
    agents.social_tolerance = _delta(agents.social_tolerance, 0.001*(_local(world, agents, 'biodiversity')-agents.social_tolerance))
def rule_29961(world, agents):
    agents.reputation = _delta(agents.reputation, 0.001*torch.tanh(_local(world, agents, 'habitat_stress')))
def rule_29962(world, agents):
    agents.trust = _delta(agents.trust, 0.001*_local(world, agents, 'erosion'))
def rule_29963(world, agents):
    agents.cooperation = _delta(agents.cooperation, -0.001*_local(world, agents, 'soil_depth'))
def rule_29964(world, agents):
    agents.defection = _delta(agents.defection, 0.001*_local(world, agents, 'root_density')*_local(world, agents, 'root_density'))
def rule_29965(world, agents):
    agents.aggression = _delta(agents.aggression, 0.001*(_local(world, agents, 'wetland')-agents.aggression))
def rule_29966(world, agents):
    agents.conflict_pressure = _delta(agents.conflict_pressure, 0.001*torch.tanh(_local(world, agents, 'carbon_storage')))
def rule_29967(world, agents):
    agents.competition_pressure = _delta(agents.competition_pressure, 0.001*_local(world, agents, 'fire_risk'))
def rule_29968(world, agents):
    agents.territoriality = _delta(agents.territoriality, -0.001*_local(world, agents, 'ash'))
def rule_29969(world, agents):
    agents.group_stability = _delta(agents.group_stability, 0.001*_local(world, agents, 'snowpack')*_local(world, agents, 'snowpack'))
def rule_29970(world, agents):
    agents.sharing_capacity = _delta(agents.sharing_capacity, 0.001*(_local(world, agents, 'groundwater')-agents.sharing_capacity))
def rule_29971(world, agents):
    agents.help_drive = _delta(agents.help_drive, 0.001*torch.tanh(_local(world, agents, 'sediment')))
def rule_29972(world, agents):
    agents.social_avoidance = _delta(agents.social_avoidance, 0.001*_local(world, agents, 'salinity'))
def rule_29973(world, agents):
    agents.selfishness = _delta(agents.selfishness, -0.001*_local(world, agents, 'algae'))
def rule_29974(world, agents):
    agents.generosity = _delta(agents.generosity, 0.001*_local(world, agents, 'organic_matter')*_local(world, agents, 'organic_matter'))
def rule_29975(world, agents):
    agents.gratitude = _delta(agents.gratitude, 0.001*(_local(world, agents, 'deadwood')-agents.gratitude))
def rule_29976(world, agents):
    agents.caution = _delta(agents.caution, 0.001*torch.tanh(_local(world, agents, 'pollinators')))
def rule_29977(world, agents):
    agents.confidence = _delta(agents.confidence, 0.001*_local(world, agents, 'flowers'))
def rule_29978(world, agents):
    agents.strategy_confidence = _delta(agents.strategy_confidence, -0.001*_local(world, agents, 'seed_bank'))
def rule_29979(world, agents):
    agents.future_help = _delta(agents.future_help, 0.001*_local(world, agents, 'soil_carbon')*_local(world, agents, 'soil_carbon'))
def rule_29980(world, agents):
    agents.resource_discovery = _delta(agents.resource_discovery, 0.001*(_local(world, agents, 'surface_ice')-agents.resource_discovery))
def rule_29981(world, agents):
    agents.empathy = _delta(agents.empathy, 0.001*torch.tanh(_local(world, agents, 'temperature')))
def rule_29982(world, agents):
    agents.attack_threshold = _delta(agents.attack_threshold, 0.001*_local(world, agents, 'surface_water'))
def rule_29983(world, agents):
    agents.defection_threshold = _delta(agents.defection_threshold, -0.001*_local(world, agents, 'humidity'))
def rule_29984(world, agents):
    agents.oxygen_need = _delta(agents.oxygen_need, 0.001*_local(world, agents, 'cloud')*_local(world, agents, 'cloud'))
def rule_29985(world, agents):
    agents.shelter_need = _delta(agents.shelter_need, 0.001*(_local(world, agents, 'rain')-agents.shelter_need))
def rule_29986(world, agents):
    agents.fire_fear = _delta(agents.fire_fear, 0.001*torch.tanh(_local(world, agents, 'soil_moisture')))
def rule_29987(world, agents):
    agents.resource_competition = _delta(agents.resource_competition, 0.001*_local(world, agents, 'runoff'))
def rule_29988(world, agents):
    agents.vegetation_expectation = _delta(agents.vegetation_expectation, -0.001*_local(world, agents, 'wind_x'))
def rule_29989(world, agents):
    agents.stress = _delta(agents.stress, 0.001*_local(world, agents, 'wind_y')*_local(world, agents, 'wind_y'))
def rule_29990(world, agents):
    agents.social_need = _delta(agents.social_need, 0.001*(_local(world, agents, 'vegetation')-agents.social_need))
def rule_29991(world, agents):
    agents.neighbor_energy_gap = _delta(agents.neighbor_energy_gap, 0.001*torch.tanh(_local(world, agents, 'biomass')))
def rule_29992(world, agents):
    agents.neighbor_health_gap = _delta(agents.neighbor_health_gap, 0.001*_local(world, agents, 'herbivore'))
def rule_29993(world, agents):
    agents.betrayal_memory = _delta(agents.betrayal_memory, -0.001*_local(world, agents, 'predator'))
def rule_29994(world, agents):
    agents.conflict_history = _delta(agents.conflict_history, 0.001*_local(world, agents, 'carrion')*_local(world, agents, 'carrion'))
def rule_29995(world, agents):
    agents.cooperation_history = _delta(agents.cooperation_history, 0.001*(_local(world, agents, 'nutrients')-agents.cooperation_history))
def rule_29996(world, agents):
    agents.help_received = _delta(agents.help_received, 0.001*torch.tanh(_local(world, agents, 'decomposition_rate')))
def rule_29997(world, agents):
    agents.help_given = _delta(agents.help_given, 0.001*_local(world, agents, 'oxygen'))
def rule_29998(world, agents):
    agents.local_density = _delta(agents.local_density, -0.001*_local(world, agents, 'co2'))
def rule_29999(world, agents):
    agents.last_reward = _delta(agents.last_reward, 0.001*_local(world, agents, 'photosynthesis_factor')*_local(world, agents, 'photosynthesis_factor'))
def rule_30000(world, agents):
    agents.last_energy_delta = _delta(agents.last_energy_delta, 0.001*(_local(world, agents, 'ice')-agents.last_energy_delta))

RULES=[rule_28001,rule_28002,rule_28003,rule_28004,rule_28005,rule_28006,rule_28007,rule_28008,rule_28009,rule_28010,rule_28011,rule_28012,rule_28013,rule_28014,rule_28015,rule_28016,rule_28017,rule_28018,rule_28019,rule_28020,rule_28021,rule_28022,rule_28023,rule_28024,rule_28025,rule_28026,rule_28027,rule_28028,rule_28029,rule_28030,rule_28031,rule_28032,rule_28033,rule_28034,rule_28035,rule_28036,rule_28037,rule_28038,rule_28039,rule_28040,rule_28041,rule_28042,rule_28043,rule_28044,rule_28045,rule_28046,rule_28047,rule_28048,rule_28049,rule_28050,rule_28051,rule_28052,rule_28053,rule_28054,rule_28055,rule_28056,rule_28057,rule_28058,rule_28059,rule_28060,rule_28061,rule_28062,rule_28063,rule_28064,rule_28065,rule_28066,rule_28067,rule_28068,rule_28069,rule_28070,rule_28071,rule_28072,rule_28073,rule_28074,rule_28075,rule_28076,rule_28077,rule_28078,rule_28079,rule_28080,rule_28081,rule_28082,rule_28083,rule_28084,rule_28085,rule_28086,rule_28087,rule_28088,rule_28089,rule_28090,rule_28091,rule_28092,rule_28093,rule_28094,rule_28095,rule_28096,rule_28097,rule_28098,rule_28099,rule_28100,rule_28101,rule_28102,rule_28103,rule_28104,rule_28105,rule_28106,rule_28107,rule_28108,rule_28109,rule_28110,rule_28111,rule_28112,rule_28113,rule_28114,rule_28115,rule_28116,rule_28117,rule_28118,rule_28119,rule_28120,rule_28121,rule_28122,rule_28123,rule_28124,rule_28125,rule_28126,rule_28127,rule_28128,rule_28129,rule_28130,rule_28131,rule_28132,rule_28133,rule_28134,rule_28135,rule_28136,rule_28137,rule_28138,rule_28139,rule_28140,rule_28141,rule_28142,rule_28143,rule_28144,rule_28145,rule_28146,rule_28147,rule_28148,rule_28149,rule_28150,rule_28151,rule_28152,rule_28153,rule_28154,rule_28155,rule_28156,rule_28157,rule_28158,rule_28159,rule_28160,rule_28161,rule_28162,rule_28163,rule_28164,rule_28165,rule_28166,rule_28167,rule_28168,rule_28169,rule_28170,rule_28171,rule_28172,rule_28173,rule_28174,rule_28175,rule_28176,rule_28177,rule_28178,rule_28179,rule_28180,rule_28181,rule_28182,rule_28183,rule_28184,rule_28185,rule_28186,rule_28187,rule_28188,rule_28189,rule_28190,rule_28191,rule_28192,rule_28193,rule_28194,rule_28195,rule_28196,rule_28197,rule_28198,rule_28199,rule_28200,rule_28201,rule_28202,rule_28203,rule_28204,rule_28205,rule_28206,rule_28207,rule_28208,rule_28209,rule_28210,rule_28211,rule_28212,rule_28213,rule_28214,rule_28215,rule_28216,rule_28217,rule_28218,rule_28219,rule_28220,rule_28221,rule_28222,rule_28223,rule_28224,rule_28225,rule_28226,rule_28227,rule_28228,rule_28229,rule_28230,rule_28231,rule_28232,rule_28233,rule_28234,rule_28235,rule_28236,rule_28237,rule_28238,rule_28239,rule_28240,rule_28241,rule_28242,rule_28243,rule_28244,rule_28245,rule_28246,rule_28247,rule_28248,rule_28249,rule_28250,rule_28251,rule_28252,rule_28253,rule_28254,rule_28255,rule_28256,rule_28257,rule_28258,rule_28259,rule_28260,rule_28261,rule_28262,rule_28263,rule_28264,rule_28265,rule_28266,rule_28267,rule_28268,rule_28269,rule_28270,rule_28271,rule_28272,rule_28273,rule_28274,rule_28275,rule_28276,rule_28277,rule_28278,rule_28279,rule_28280,rule_28281,rule_28282,rule_28283,rule_28284,rule_28285,rule_28286,rule_28287,rule_28288,rule_28289,rule_28290,rule_28291,rule_28292,rule_28293,rule_28294,rule_28295,rule_28296,rule_28297,rule_28298,rule_28299,rule_28300,rule_28301,rule_28302,rule_28303,rule_28304,rule_28305,rule_28306,rule_28307,rule_28308,rule_28309,rule_28310,rule_28311,rule_28312,rule_28313,rule_28314,rule_28315,rule_28316,rule_28317,rule_28318,rule_28319,rule_28320,rule_28321,rule_28322,rule_28323,rule_28324,rule_28325,rule_28326,rule_28327,rule_28328,rule_28329,rule_28330,rule_28331,rule_28332,rule_28333,rule_28334,rule_28335,rule_28336,rule_28337,rule_28338,rule_28339,rule_28340,rule_28341,rule_28342,rule_28343,rule_28344,rule_28345,rule_28346,rule_28347,rule_28348,rule_28349,rule_28350,rule_28351,rule_28352,rule_28353,rule_28354,rule_28355,rule_28356,rule_28357,rule_28358,rule_28359,rule_28360,rule_28361,rule_28362,rule_28363,rule_28364,rule_28365,rule_28366,rule_28367,rule_28368,rule_28369,rule_28370,rule_28371,rule_28372,rule_28373,rule_28374,rule_28375,rule_28376,rule_28377,rule_28378,rule_28379,rule_28380,rule_28381,rule_28382,rule_28383,rule_28384,rule_28385,rule_28386,rule_28387,rule_28388,rule_28389,rule_28390,rule_28391,rule_28392,rule_28393,rule_28394,rule_28395,rule_28396,rule_28397,rule_28398,rule_28399,rule_28400,rule_28401,rule_28402,rule_28403,rule_28404,rule_28405,rule_28406,rule_28407,rule_28408,rule_28409,rule_28410,rule_28411,rule_28412,rule_28413,rule_28414,rule_28415,rule_28416,rule_28417,rule_28418,rule_28419,rule_28420,rule_28421,rule_28422,rule_28423,rule_28424,rule_28425,rule_28426,rule_28427,rule_28428,rule_28429,rule_28430,rule_28431,rule_28432,rule_28433,rule_28434,rule_28435,rule_28436,rule_28437,rule_28438,rule_28439,rule_28440,rule_28441,rule_28442,rule_28443,rule_28444,rule_28445,rule_28446,rule_28447,rule_28448,rule_28449,rule_28450,rule_28451,rule_28452,rule_28453,rule_28454,rule_28455,rule_28456,rule_28457,rule_28458,rule_28459,rule_28460,rule_28461,rule_28462,rule_28463,rule_28464,rule_28465,rule_28466,rule_28467,rule_28468,rule_28469,rule_28470,rule_28471,rule_28472,rule_28473,rule_28474,rule_28475,rule_28476,rule_28477,rule_28478,rule_28479,rule_28480,rule_28481,rule_28482,rule_28483,rule_28484,rule_28485,rule_28486,rule_28487,rule_28488,rule_28489,rule_28490,rule_28491,rule_28492,rule_28493,rule_28494,rule_28495,rule_28496,rule_28497,rule_28498,rule_28499,rule_28500,rule_28501,rule_28502,rule_28503,rule_28504,rule_28505,rule_28506,rule_28507,rule_28508,rule_28509,rule_28510,rule_28511,rule_28512,rule_28513,rule_28514,rule_28515,rule_28516,rule_28517,rule_28518,rule_28519,rule_28520,rule_28521,rule_28522,rule_28523,rule_28524,rule_28525,rule_28526,rule_28527,rule_28528,rule_28529,rule_28530,rule_28531,rule_28532,rule_28533,rule_28534,rule_28535,rule_28536,rule_28537,rule_28538,rule_28539,rule_28540,rule_28541,rule_28542,rule_28543,rule_28544,rule_28545,rule_28546,rule_28547,rule_28548,rule_28549,rule_28550,rule_28551,rule_28552,rule_28553,rule_28554,rule_28555,rule_28556,rule_28557,rule_28558,rule_28559,rule_28560,rule_28561,rule_28562,rule_28563,rule_28564,rule_28565,rule_28566,rule_28567,rule_28568,rule_28569,rule_28570,rule_28571,rule_28572,rule_28573,rule_28574,rule_28575,rule_28576,rule_28577,rule_28578,rule_28579,rule_28580,rule_28581,rule_28582,rule_28583,rule_28584,rule_28585,rule_28586,rule_28587,rule_28588,rule_28589,rule_28590,rule_28591,rule_28592,rule_28593,rule_28594,rule_28595,rule_28596,rule_28597,rule_28598,rule_28599,rule_28600,rule_28601,rule_28602,rule_28603,rule_28604,rule_28605,rule_28606,rule_28607,rule_28608,rule_28609,rule_28610,rule_28611,rule_28612,rule_28613,rule_28614,rule_28615,rule_28616,rule_28617,rule_28618,rule_28619,rule_28620,rule_28621,rule_28622,rule_28623,rule_28624,rule_28625,rule_28626,rule_28627,rule_28628,rule_28629,rule_28630,rule_28631,rule_28632,rule_28633,rule_28634,rule_28635,rule_28636,rule_28637,rule_28638,rule_28639,rule_28640,rule_28641,rule_28642,rule_28643,rule_28644,rule_28645,rule_28646,rule_28647,rule_28648,rule_28649,rule_28650,rule_28651,rule_28652,rule_28653,rule_28654,rule_28655,rule_28656,rule_28657,rule_28658,rule_28659,rule_28660,rule_28661,rule_28662,rule_28663,rule_28664,rule_28665,rule_28666,rule_28667,rule_28668,rule_28669,rule_28670,rule_28671,rule_28672,rule_28673,rule_28674,rule_28675,rule_28676,rule_28677,rule_28678,rule_28679,rule_28680,rule_28681,rule_28682,rule_28683,rule_28684,rule_28685,rule_28686,rule_28687,rule_28688,rule_28689,rule_28690,rule_28691,rule_28692,rule_28693,rule_28694,rule_28695,rule_28696,rule_28697,rule_28698,rule_28699,rule_28700,rule_28701,rule_28702,rule_28703,rule_28704,rule_28705,rule_28706,rule_28707,rule_28708,rule_28709,rule_28710,rule_28711,rule_28712,rule_28713,rule_28714,rule_28715,rule_28716,rule_28717,rule_28718,rule_28719,rule_28720,rule_28721,rule_28722,rule_28723,rule_28724,rule_28725,rule_28726,rule_28727,rule_28728,rule_28729,rule_28730,rule_28731,rule_28732,rule_28733,rule_28734,rule_28735,rule_28736,rule_28737,rule_28738,rule_28739,rule_28740,rule_28741,rule_28742,rule_28743,rule_28744,rule_28745,rule_28746,rule_28747,rule_28748,rule_28749,rule_28750,rule_28751,rule_28752,rule_28753,rule_28754,rule_28755,rule_28756,rule_28757,rule_28758,rule_28759,rule_28760,rule_28761,rule_28762,rule_28763,rule_28764,rule_28765,rule_28766,rule_28767,rule_28768,rule_28769,rule_28770,rule_28771,rule_28772,rule_28773,rule_28774,rule_28775,rule_28776,rule_28777,rule_28778,rule_28779,rule_28780,rule_28781,rule_28782,rule_28783,rule_28784,rule_28785,rule_28786,rule_28787,rule_28788,rule_28789,rule_28790,rule_28791,rule_28792,rule_28793,rule_28794,rule_28795,rule_28796,rule_28797,rule_28798,rule_28799,rule_28800,rule_28801,rule_28802,rule_28803,rule_28804,rule_28805,rule_28806,rule_28807,rule_28808,rule_28809,rule_28810,rule_28811,rule_28812,rule_28813,rule_28814,rule_28815,rule_28816,rule_28817,rule_28818,rule_28819,rule_28820,rule_28821,rule_28822,rule_28823,rule_28824,rule_28825,rule_28826,rule_28827,rule_28828,rule_28829,rule_28830,rule_28831,rule_28832,rule_28833,rule_28834,rule_28835,rule_28836,rule_28837,rule_28838,rule_28839,rule_28840,rule_28841,rule_28842,rule_28843,rule_28844,rule_28845,rule_28846,rule_28847,rule_28848,rule_28849,rule_28850,rule_28851,rule_28852,rule_28853,rule_28854,rule_28855,rule_28856,rule_28857,rule_28858,rule_28859,rule_28860,rule_28861,rule_28862,rule_28863,rule_28864,rule_28865,rule_28866,rule_28867,rule_28868,rule_28869,rule_28870,rule_28871,rule_28872,rule_28873,rule_28874,rule_28875,rule_28876,rule_28877,rule_28878,rule_28879,rule_28880,rule_28881,rule_28882,rule_28883,rule_28884,rule_28885,rule_28886,rule_28887,rule_28888,rule_28889,rule_28890,rule_28891,rule_28892,rule_28893,rule_28894,rule_28895,rule_28896,rule_28897,rule_28898,rule_28899,rule_28900,rule_28901,rule_28902,rule_28903,rule_28904,rule_28905,rule_28906,rule_28907,rule_28908,rule_28909,rule_28910,rule_28911,rule_28912,rule_28913,rule_28914,rule_28915,rule_28916,rule_28917,rule_28918,rule_28919,rule_28920,rule_28921,rule_28922,rule_28923,rule_28924,rule_28925,rule_28926,rule_28927,rule_28928,rule_28929,rule_28930,rule_28931,rule_28932,rule_28933,rule_28934,rule_28935,rule_28936,rule_28937,rule_28938,rule_28939,rule_28940,rule_28941,rule_28942,rule_28943,rule_28944,rule_28945,rule_28946,rule_28947,rule_28948,rule_28949,rule_28950,rule_28951,rule_28952,rule_28953,rule_28954,rule_28955,rule_28956,rule_28957,rule_28958,rule_28959,rule_28960,rule_28961,rule_28962,rule_28963,rule_28964,rule_28965,rule_28966,rule_28967,rule_28968,rule_28969,rule_28970,rule_28971,rule_28972,rule_28973,rule_28974,rule_28975,rule_28976,rule_28977,rule_28978,rule_28979,rule_28980,rule_28981,rule_28982,rule_28983,rule_28984,rule_28985,rule_28986,rule_28987,rule_28988,rule_28989,rule_28990,rule_28991,rule_28992,rule_28993,rule_28994,rule_28995,rule_28996,rule_28997,rule_28998,rule_28999,rule_29000,rule_29001,rule_29002,rule_29003,rule_29004,rule_29005,rule_29006,rule_29007,rule_29008,rule_29009,rule_29010,rule_29011,rule_29012,rule_29013,rule_29014,rule_29015,rule_29016,rule_29017,rule_29018,rule_29019,rule_29020,rule_29021,rule_29022,rule_29023,rule_29024,rule_29025,rule_29026,rule_29027,rule_29028,rule_29029,rule_29030,rule_29031,rule_29032,rule_29033,rule_29034,rule_29035,rule_29036,rule_29037,rule_29038,rule_29039,rule_29040,rule_29041,rule_29042,rule_29043,rule_29044,rule_29045,rule_29046,rule_29047,rule_29048,rule_29049,rule_29050,rule_29051,rule_29052,rule_29053,rule_29054,rule_29055,rule_29056,rule_29057,rule_29058,rule_29059,rule_29060,rule_29061,rule_29062,rule_29063,rule_29064,rule_29065,rule_29066,rule_29067,rule_29068,rule_29069,rule_29070,rule_29071,rule_29072,rule_29073,rule_29074,rule_29075,rule_29076,rule_29077,rule_29078,rule_29079,rule_29080,rule_29081,rule_29082,rule_29083,rule_29084,rule_29085,rule_29086,rule_29087,rule_29088,rule_29089,rule_29090,rule_29091,rule_29092,rule_29093,rule_29094,rule_29095,rule_29096,rule_29097,rule_29098,rule_29099,rule_29100,rule_29101,rule_29102,rule_29103,rule_29104,rule_29105,rule_29106,rule_29107,rule_29108,rule_29109,rule_29110,rule_29111,rule_29112,rule_29113,rule_29114,rule_29115,rule_29116,rule_29117,rule_29118,rule_29119,rule_29120,rule_29121,rule_29122,rule_29123,rule_29124,rule_29125,rule_29126,rule_29127,rule_29128,rule_29129,rule_29130,rule_29131,rule_29132,rule_29133,rule_29134,rule_29135,rule_29136,rule_29137,rule_29138,rule_29139,rule_29140,rule_29141,rule_29142,rule_29143,rule_29144,rule_29145,rule_29146,rule_29147,rule_29148,rule_29149,rule_29150,rule_29151,rule_29152,rule_29153,rule_29154,rule_29155,rule_29156,rule_29157,rule_29158,rule_29159,rule_29160,rule_29161,rule_29162,rule_29163,rule_29164,rule_29165,rule_29166,rule_29167,rule_29168,rule_29169,rule_29170,rule_29171,rule_29172,rule_29173,rule_29174,rule_29175,rule_29176,rule_29177,rule_29178,rule_29179,rule_29180,rule_29181,rule_29182,rule_29183,rule_29184,rule_29185,rule_29186,rule_29187,rule_29188,rule_29189,rule_29190,rule_29191,rule_29192,rule_29193,rule_29194,rule_29195,rule_29196,rule_29197,rule_29198,rule_29199,rule_29200,rule_29201,rule_29202,rule_29203,rule_29204,rule_29205,rule_29206,rule_29207,rule_29208,rule_29209,rule_29210,rule_29211,rule_29212,rule_29213,rule_29214,rule_29215,rule_29216,rule_29217,rule_29218,rule_29219,rule_29220,rule_29221,rule_29222,rule_29223,rule_29224,rule_29225,rule_29226,rule_29227,rule_29228,rule_29229,rule_29230,rule_29231,rule_29232,rule_29233,rule_29234,rule_29235,rule_29236,rule_29237,rule_29238,rule_29239,rule_29240,rule_29241,rule_29242,rule_29243,rule_29244,rule_29245,rule_29246,rule_29247,rule_29248,rule_29249,rule_29250,rule_29251,rule_29252,rule_29253,rule_29254,rule_29255,rule_29256,rule_29257,rule_29258,rule_29259,rule_29260,rule_29261,rule_29262,rule_29263,rule_29264,rule_29265,rule_29266,rule_29267,rule_29268,rule_29269,rule_29270,rule_29271,rule_29272,rule_29273,rule_29274,rule_29275,rule_29276,rule_29277,rule_29278,rule_29279,rule_29280,rule_29281,rule_29282,rule_29283,rule_29284,rule_29285,rule_29286,rule_29287,rule_29288,rule_29289,rule_29290,rule_29291,rule_29292,rule_29293,rule_29294,rule_29295,rule_29296,rule_29297,rule_29298,rule_29299,rule_29300,rule_29301,rule_29302,rule_29303,rule_29304,rule_29305,rule_29306,rule_29307,rule_29308,rule_29309,rule_29310,rule_29311,rule_29312,rule_29313,rule_29314,rule_29315,rule_29316,rule_29317,rule_29318,rule_29319,rule_29320,rule_29321,rule_29322,rule_29323,rule_29324,rule_29325,rule_29326,rule_29327,rule_29328,rule_29329,rule_29330,rule_29331,rule_29332,rule_29333,rule_29334,rule_29335,rule_29336,rule_29337,rule_29338,rule_29339,rule_29340,rule_29341,rule_29342,rule_29343,rule_29344,rule_29345,rule_29346,rule_29347,rule_29348,rule_29349,rule_29350,rule_29351,rule_29352,rule_29353,rule_29354,rule_29355,rule_29356,rule_29357,rule_29358,rule_29359,rule_29360,rule_29361,rule_29362,rule_29363,rule_29364,rule_29365,rule_29366,rule_29367,rule_29368,rule_29369,rule_29370,rule_29371,rule_29372,rule_29373,rule_29374,rule_29375,rule_29376,rule_29377,rule_29378,rule_29379,rule_29380,rule_29381,rule_29382,rule_29383,rule_29384,rule_29385,rule_29386,rule_29387,rule_29388,rule_29389,rule_29390,rule_29391,rule_29392,rule_29393,rule_29394,rule_29395,rule_29396,rule_29397,rule_29398,rule_29399,rule_29400,rule_29401,rule_29402,rule_29403,rule_29404,rule_29405,rule_29406,rule_29407,rule_29408,rule_29409,rule_29410,rule_29411,rule_29412,rule_29413,rule_29414,rule_29415,rule_29416,rule_29417,rule_29418,rule_29419,rule_29420,rule_29421,rule_29422,rule_29423,rule_29424,rule_29425,rule_29426,rule_29427,rule_29428,rule_29429,rule_29430,rule_29431,rule_29432,rule_29433,rule_29434,rule_29435,rule_29436,rule_29437,rule_29438,rule_29439,rule_29440,rule_29441,rule_29442,rule_29443,rule_29444,rule_29445,rule_29446,rule_29447,rule_29448,rule_29449,rule_29450,rule_29451,rule_29452,rule_29453,rule_29454,rule_29455,rule_29456,rule_29457,rule_29458,rule_29459,rule_29460,rule_29461,rule_29462,rule_29463,rule_29464,rule_29465,rule_29466,rule_29467,rule_29468,rule_29469,rule_29470,rule_29471,rule_29472,rule_29473,rule_29474,rule_29475,rule_29476,rule_29477,rule_29478,rule_29479,rule_29480,rule_29481,rule_29482,rule_29483,rule_29484,rule_29485,rule_29486,rule_29487,rule_29488,rule_29489,rule_29490,rule_29491,rule_29492,rule_29493,rule_29494,rule_29495,rule_29496,rule_29497,rule_29498,rule_29499,rule_29500,rule_29501,rule_29502,rule_29503,rule_29504,rule_29505,rule_29506,rule_29507,rule_29508,rule_29509,rule_29510,rule_29511,rule_29512,rule_29513,rule_29514,rule_29515,rule_29516,rule_29517,rule_29518,rule_29519,rule_29520,rule_29521,rule_29522,rule_29523,rule_29524,rule_29525,rule_29526,rule_29527,rule_29528,rule_29529,rule_29530,rule_29531,rule_29532,rule_29533,rule_29534,rule_29535,rule_29536,rule_29537,rule_29538,rule_29539,rule_29540,rule_29541,rule_29542,rule_29543,rule_29544,rule_29545,rule_29546,rule_29547,rule_29548,rule_29549,rule_29550,rule_29551,rule_29552,rule_29553,rule_29554,rule_29555,rule_29556,rule_29557,rule_29558,rule_29559,rule_29560,rule_29561,rule_29562,rule_29563,rule_29564,rule_29565,rule_29566,rule_29567,rule_29568,rule_29569,rule_29570,rule_29571,rule_29572,rule_29573,rule_29574,rule_29575,rule_29576,rule_29577,rule_29578,rule_29579,rule_29580,rule_29581,rule_29582,rule_29583,rule_29584,rule_29585,rule_29586,rule_29587,rule_29588,rule_29589,rule_29590,rule_29591,rule_29592,rule_29593,rule_29594,rule_29595,rule_29596,rule_29597,rule_29598,rule_29599,rule_29600,rule_29601,rule_29602,rule_29603,rule_29604,rule_29605,rule_29606,rule_29607,rule_29608,rule_29609,rule_29610,rule_29611,rule_29612,rule_29613,rule_29614,rule_29615,rule_29616,rule_29617,rule_29618,rule_29619,rule_29620,rule_29621,rule_29622,rule_29623,rule_29624,rule_29625,rule_29626,rule_29627,rule_29628,rule_29629,rule_29630,rule_29631,rule_29632,rule_29633,rule_29634,rule_29635,rule_29636,rule_29637,rule_29638,rule_29639,rule_29640,rule_29641,rule_29642,rule_29643,rule_29644,rule_29645,rule_29646,rule_29647,rule_29648,rule_29649,rule_29650,rule_29651,rule_29652,rule_29653,rule_29654,rule_29655,rule_29656,rule_29657,rule_29658,rule_29659,rule_29660,rule_29661,rule_29662,rule_29663,rule_29664,rule_29665,rule_29666,rule_29667,rule_29668,rule_29669,rule_29670,rule_29671,rule_29672,rule_29673,rule_29674,rule_29675,rule_29676,rule_29677,rule_29678,rule_29679,rule_29680,rule_29681,rule_29682,rule_29683,rule_29684,rule_29685,rule_29686,rule_29687,rule_29688,rule_29689,rule_29690,rule_29691,rule_29692,rule_29693,rule_29694,rule_29695,rule_29696,rule_29697,rule_29698,rule_29699,rule_29700,rule_29701,rule_29702,rule_29703,rule_29704,rule_29705,rule_29706,rule_29707,rule_29708,rule_29709,rule_29710,rule_29711,rule_29712,rule_29713,rule_29714,rule_29715,rule_29716,rule_29717,rule_29718,rule_29719,rule_29720,rule_29721,rule_29722,rule_29723,rule_29724,rule_29725,rule_29726,rule_29727,rule_29728,rule_29729,rule_29730,rule_29731,rule_29732,rule_29733,rule_29734,rule_29735,rule_29736,rule_29737,rule_29738,rule_29739,rule_29740,rule_29741,rule_29742,rule_29743,rule_29744,rule_29745,rule_29746,rule_29747,rule_29748,rule_29749,rule_29750,rule_29751,rule_29752,rule_29753,rule_29754,rule_29755,rule_29756,rule_29757,rule_29758,rule_29759,rule_29760,rule_29761,rule_29762,rule_29763,rule_29764,rule_29765,rule_29766,rule_29767,rule_29768,rule_29769,rule_29770,rule_29771,rule_29772,rule_29773,rule_29774,rule_29775,rule_29776,rule_29777,rule_29778,rule_29779,rule_29780,rule_29781,rule_29782,rule_29783,rule_29784,rule_29785,rule_29786,rule_29787,rule_29788,rule_29789,rule_29790,rule_29791,rule_29792,rule_29793,rule_29794,rule_29795,rule_29796,rule_29797,rule_29798,rule_29799,rule_29800,rule_29801,rule_29802,rule_29803,rule_29804,rule_29805,rule_29806,rule_29807,rule_29808,rule_29809,rule_29810,rule_29811,rule_29812,rule_29813,rule_29814,rule_29815,rule_29816,rule_29817,rule_29818,rule_29819,rule_29820,rule_29821,rule_29822,rule_29823,rule_29824,rule_29825,rule_29826,rule_29827,rule_29828,rule_29829,rule_29830,rule_29831,rule_29832,rule_29833,rule_29834,rule_29835,rule_29836,rule_29837,rule_29838,rule_29839,rule_29840,rule_29841,rule_29842,rule_29843,rule_29844,rule_29845,rule_29846,rule_29847,rule_29848,rule_29849,rule_29850,rule_29851,rule_29852,rule_29853,rule_29854,rule_29855,rule_29856,rule_29857,rule_29858,rule_29859,rule_29860,rule_29861,rule_29862,rule_29863,rule_29864,rule_29865,rule_29866,rule_29867,rule_29868,rule_29869,rule_29870,rule_29871,rule_29872,rule_29873,rule_29874,rule_29875,rule_29876,rule_29877,rule_29878,rule_29879,rule_29880,rule_29881,rule_29882,rule_29883,rule_29884,rule_29885,rule_29886,rule_29887,rule_29888,rule_29889,rule_29890,rule_29891,rule_29892,rule_29893,rule_29894,rule_29895,rule_29896,rule_29897,rule_29898,rule_29899,rule_29900,rule_29901,rule_29902,rule_29903,rule_29904,rule_29905,rule_29906,rule_29907,rule_29908,rule_29909,rule_29910,rule_29911,rule_29912,rule_29913,rule_29914,rule_29915,rule_29916,rule_29917,rule_29918,rule_29919,rule_29920,rule_29921,rule_29922,rule_29923,rule_29924,rule_29925,rule_29926,rule_29927,rule_29928,rule_29929,rule_29930,rule_29931,rule_29932,rule_29933,rule_29934,rule_29935,rule_29936,rule_29937,rule_29938,rule_29939,rule_29940,rule_29941,rule_29942,rule_29943,rule_29944,rule_29945,rule_29946,rule_29947,rule_29948,rule_29949,rule_29950,rule_29951,rule_29952,rule_29953,rule_29954,rule_29955,rule_29956,rule_29957,rule_29958,rule_29959,rule_29960,rule_29961,rule_29962,rule_29963,rule_29964,rule_29965,rule_29966,rule_29967,rule_29968,rule_29969,rule_29970,rule_29971,rule_29972,rule_29973,rule_29974,rule_29975,rule_29976,rule_29977,rule_29978,rule_29979,rule_29980,rule_29981,rule_29982,rule_29983,rule_29984,rule_29985,rule_29986,rule_29987,rule_29988,rule_29989,rule_29990,rule_29991,rule_29992,rule_29993,rule_29994,rule_29995,rule_29996,rule_29997,rule_29998,rule_29999,rule_30000]

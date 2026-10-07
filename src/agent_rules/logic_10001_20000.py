import torch

RATE = 0.008


def _field(world, name):
    x = getattr(world, name, None)
    if x is None:
        return None
    return torch.nan_to_num(x).float()


def _local(world, agents, name):
    x = agents.pos[:, 0].long()
    y = agents.pos[:, 1].long()
    field = getattr(world, name, None)
    if field is None:
        return None
    return torch.nan_to_num(field[y, x]).to(dtype=agents.energy.dtype)


def _sigmoid(x):
    return torch.sigmoid(torch.nan_to_num(x))


def _mode(s, t, mode):
    if mode == "inverse": return 1 - s
    if mode == "square": return s * s
    if mode == "sqrt": return torch.sqrt(s.clamp_min(0))
    if mode == "pulse": return 4 * s * (1 - s)
    if mode == "threshold": return (s > 0.5).to(s.dtype)
    if mode == "saturation": return s / (0.25 + s)
    if mode == "reciprocal": return 1 / (1 + s)
    if mode == "gap": return torch.abs(s - t)
    if mode == "feedback": return s * t
    return s


def _world_apply(world, source, target, mode):
    s = _field(world, source)
    t = _field(world, target)
    if s is None or t is None:
        return
    s = _sigmoid(s)
    t = torch.nan_to_num(t)
    d = _mode(s, _sigmoid(t), mode)
    setattr(world, target, t + RATE * (d - t))


def _agent_source(world, agents, name):
    if hasattr(agents, name):
        return torch.nan_to_num(getattr(agents, name)).to(dtype=agents.energy.dtype)
    return _local(world, agents, name)


def _agent_apply(world, agents, source, target, mode):
    s = _agent_source(world, agents, source)
    if s is None or not hasattr(agents, target):
        return
    s = _sigmoid(s)
    raw = torch.nan_to_num(getattr(agents, target))
    t = _sigmoid(raw)
    d = _mode(s, t, mode)
    setattr(agents, target, torch.logit((t + RATE * (d - t)).clamp(1e-5, 1 - 1e-5)))

def logic_18001(agents, world):
    _agent_apply(world, agents, 'temperature', 'hydration', 'direct')

def logic_18002(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hydration', 'direct')

def logic_18003(agents, world):
    _agent_apply(world, agents, 'humidity', 'hydration', 'direct')

def logic_18004(agents, world):
    _agent_apply(world, agents, 'cloud', 'hydration', 'direct')

def logic_18005(agents, world):
    _agent_apply(world, agents, 'rain', 'hydration', 'direct')

def logic_18006(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hydration', 'direct')

def logic_18007(agents, world):
    _agent_apply(world, agents, 'runoff', 'hydration', 'direct')

def logic_18008(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hydration', 'direct')

def logic_18009(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hydration', 'direct')

def logic_18010(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hydration', 'direct')

def logic_18011(agents, world):
    _agent_apply(world, agents, 'biomass', 'hydration', 'direct')

def logic_18012(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hydration', 'direct')

def logic_18013(agents, world):
    _agent_apply(world, agents, 'predator', 'hydration', 'direct')

def logic_18014(agents, world):
    _agent_apply(world, agents, 'carrion', 'hydration', 'direct')

def logic_18015(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hydration', 'direct')

def logic_18016(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hydration', 'direct')

def logic_18017(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hydration', 'direct')

def logic_18018(agents, world):
    _agent_apply(world, agents, 'co2', 'hydration', 'direct')

def logic_18019(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hydration', 'direct')

def logic_18020(agents, world):
    _agent_apply(world, agents, 'ice', 'hydration', 'direct')

def logic_18021(agents, world):
    _agent_apply(world, agents, 'evaporation', 'thirst', 'direct')

def logic_18022(agents, world):
    _agent_apply(world, agents, 'detritus', 'thirst', 'direct')

def logic_18023(agents, world):
    _agent_apply(world, agents, 'methane', 'thirst', 'direct')

def logic_18024(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'thirst', 'direct')

def logic_18025(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'thirst', 'direct')

def logic_18026(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'thirst', 'direct')

def logic_18027(agents, world):
    _agent_apply(world, agents, 'erosion', 'thirst', 'direct')

def logic_18028(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'thirst', 'direct')

def logic_18029(agents, world):
    _agent_apply(world, agents, 'root_density', 'thirst', 'direct')

def logic_18030(agents, world):
    _agent_apply(world, agents, 'wetland', 'thirst', 'direct')

def logic_18031(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'thirst', 'direct')

def logic_18032(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'thirst', 'direct')

def logic_18033(agents, world):
    _agent_apply(world, agents, 'ash', 'thirst', 'direct')

def logic_18034(agents, world):
    _agent_apply(world, agents, 'snowpack', 'thirst', 'direct')

def logic_18035(agents, world):
    _agent_apply(world, agents, 'groundwater', 'thirst', 'direct')

def logic_18036(agents, world):
    _agent_apply(world, agents, 'sediment', 'thirst', 'direct')

def logic_18037(agents, world):
    _agent_apply(world, agents, 'salinity', 'thirst', 'direct')

def logic_18038(agents, world):
    _agent_apply(world, agents, 'algae', 'thirst', 'direct')

def logic_18039(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'thirst', 'direct')

def logic_18040(agents, world):
    _agent_apply(world, agents, 'deadwood', 'thirst', 'direct')

def logic_18041(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hunger', 'direct')

def logic_18042(agents, world):
    _agent_apply(world, agents, 'flowers', 'hunger', 'direct')

def logic_18043(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hunger', 'direct')

def logic_18044(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hunger', 'direct')

def logic_18045(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hunger', 'direct')

def logic_18046(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hunger', 'direct')

def logic_18047(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hunger', 'direct')

def logic_18048(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hunger', 'direct')

def logic_18049(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hunger', 'direct')

def logic_18050(agents, world):
    _agent_apply(world, agents, 'hydration', 'hunger', 'direct')

def logic_18051(agents, world):
    _agent_apply(world, agents, 'thirst', 'hunger', 'direct')

def logic_18052(agents, world):
    _agent_apply(world, agents, 'hunger', 'health', 'direct')

def logic_18053(agents, world):
    _agent_apply(world, agents, 'health', 'hunger', 'direct')

def logic_18054(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'hunger', 'direct')

def logic_18055(agents, world):
    _agent_apply(world, agents, 'dehydration', 'hunger', 'direct')

def logic_18056(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'hunger', 'direct')

def logic_18057(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'hunger', 'direct')

def logic_18058(agents, world):
    _agent_apply(world, agents, 'alertness', 'hunger', 'direct')

def logic_18059(agents, world):
    _agent_apply(world, agents, 'fear', 'hunger', 'direct')

def logic_18060(agents, world):
    _agent_apply(world, agents, 'recovery', 'hunger', 'direct')

def logic_18061(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'health', 'direct')

def logic_18062(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'health', 'direct')

def logic_18063(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'health', 'direct')

def logic_18064(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'health', 'direct')

def logic_18065(agents, world):
    _agent_apply(world, agents, 'food_access', 'health', 'direct')

def logic_18066(agents, world):
    _agent_apply(world, agents, 'wealth', 'health', 'direct')

def logic_18067(agents, world):
    _agent_apply(world, agents, 'stability', 'health', 'direct')

def logic_18068(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'health', 'direct')

def logic_18069(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'health', 'direct')

def logic_18070(agents, world):
    _agent_apply(world, agents, 'reputation', 'health', 'direct')

def logic_18071(agents, world):
    _agent_apply(world, agents, 'trust', 'health', 'direct')

def logic_18072(agents, world):
    _agent_apply(world, agents, 'cooperation', 'health', 'direct')

def logic_18073(agents, world):
    _agent_apply(world, agents, 'defection', 'health', 'direct')

def logic_18074(agents, world):
    _agent_apply(world, agents, 'aggression', 'health', 'direct')

def logic_18075(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'health', 'direct')

def logic_18076(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'health', 'direct')

def logic_18077(agents, world):
    _agent_apply(world, agents, 'territoriality', 'health', 'direct')

def logic_18078(agents, world):
    _agent_apply(world, agents, 'group_stability', 'health', 'direct')

def logic_18079(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'health', 'direct')

def logic_18080(agents, world):
    _agent_apply(world, agents, 'help_drive', 'thermal_stress', 'direct')

def logic_18081(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'thermal_stress', 'direct')

def logic_18082(agents, world):
    _agent_apply(world, agents, 'selfishness', 'thermal_stress', 'direct')

def logic_18083(agents, world):
    _agent_apply(world, agents, 'generosity', 'thermal_stress', 'direct')

def logic_18084(agents, world):
    _agent_apply(world, agents, 'gratitude', 'thermal_stress', 'direct')

def logic_18085(agents, world):
    _agent_apply(world, agents, 'caution', 'thermal_stress', 'direct')

def logic_18086(agents, world):
    _agent_apply(world, agents, 'confidence', 'thermal_stress', 'direct')

def logic_18087(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'thermal_stress', 'direct')

def logic_18088(agents, world):
    _agent_apply(world, agents, 'future_help', 'thermal_stress', 'direct')

def logic_18089(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'thermal_stress', 'direct')

def logic_18090(agents, world):
    _agent_apply(world, agents, 'empathy', 'thermal_stress', 'inverse')

def logic_18091(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'thermal_stress', 'inverse')

def logic_18092(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'thermal_stress', 'inverse')

def logic_18093(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'thermal_stress', 'inverse')

def logic_18094(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'thermal_stress', 'inverse')

def logic_18095(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'thermal_stress', 'inverse')

def logic_18096(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'thermal_stress', 'inverse')

def logic_18097(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'thermal_stress', 'inverse')

def logic_18098(agents, world):
    _agent_apply(world, agents, 'stress', 'thermal_stress', 'inverse')

def logic_18099(agents, world):
    _agent_apply(world, agents, 'social_need', 'thermal_stress', 'inverse')

def logic_18100(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'dehydration', 'inverse')

def logic_18101(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'dehydration', 'inverse')

def logic_18102(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'dehydration', 'inverse')

def logic_18103(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'dehydration', 'inverse')

def logic_18104(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'dehydration', 'inverse')

def logic_18105(agents, world):
    _agent_apply(world, agents, 'help_received', 'dehydration', 'inverse')

def logic_18106(agents, world):
    _agent_apply(world, agents, 'help_given', 'dehydration', 'inverse')

def logic_18107(agents, world):
    _agent_apply(world, agents, 'local_density', 'dehydration', 'inverse')

def logic_18108(agents, world):
    _agent_apply(world, agents, 'last_reward', 'dehydration', 'inverse')

def logic_18109(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'dehydration', 'inverse')

def logic_18110(agents, world):
    _agent_apply(world, agents, 'last_food', 'dehydration', 'inverse')

def logic_18111(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'dehydration', 'inverse')

def logic_18112(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'dehydration', 'inverse')

def logic_18113(agents, world):
    _agent_apply(world, agents, 'last_action', 'dehydration', 'inverse')

def logic_18114(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'dehydration', 'inverse')

def logic_18115(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'dehydration', 'inverse')

def logic_18116(agents, world):
    _agent_apply(world, agents, 'competition_score', 'dehydration', 'inverse')

def logic_18117(agents, world):
    _agent_apply(world, agents, 'defection_score', 'dehydration', 'inverse')

def logic_18118(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'dehydration', 'inverse')

def logic_18119(agents, world):
    _agent_apply(world, agents, 'risk_score', 'dehydration', 'inverse')

def logic_18120(agents, world):
    _agent_apply(world, agents, 'safety_score', 'pathogen_risk', 'inverse')

def logic_18121(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'pathogen_risk', 'inverse')

def logic_18122(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'pathogen_risk', 'inverse')

def logic_18123(agents, world):
    _agent_apply(world, agents, 'survival_score', 'pathogen_risk', 'inverse')

def logic_18124(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'pathogen_risk', 'inverse')

def logic_18125(agents, world):
    _agent_apply(world, agents, 'help_score', 'pathogen_risk', 'inverse')

def logic_18126(agents, world):
    _agent_apply(world, agents, 'attack_success', 'pathogen_risk', 'inverse')

def logic_18127(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'pathogen_risk', 'inverse')

def logic_18128(agents, world):
    _agent_apply(world, agents, 'defense_score', 'pathogen_risk', 'inverse')

def logic_18129(agents, world):
    _agent_apply(world, agents, 'migration_score', 'pathogen_risk', 'inverse')

def logic_18130(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'pathogen_risk', 'inverse')

def logic_18131(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'pathogen_risk', 'inverse')

def logic_18132(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'pathogen_risk', 'inverse')

def logic_18133(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'pathogen_risk', 'inverse')

def logic_18134(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'pathogen_risk', 'inverse')

def logic_18135(agents, world):
    _agent_apply(world, agents, 'memory_update', 'pathogen_risk', 'inverse')

def logic_18136(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'pathogen_risk', 'inverse')

def logic_18137(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'pathogen_risk', 'inverse')

def logic_18138(agents, world):
    _agent_apply(world, agents, 'payoff', 'pathogen_risk', 'inverse')

def logic_18139(agents, world):
    _agent_apply(world, agents, 'temperature', 'infection_risk', 'inverse')

def logic_18140(agents, world):
    _agent_apply(world, agents, 'surface_water', 'infection_risk', 'inverse')

def logic_18141(agents, world):
    _agent_apply(world, agents, 'humidity', 'infection_risk', 'inverse')

def logic_18142(agents, world):
    _agent_apply(world, agents, 'cloud', 'infection_risk', 'inverse')

def logic_18143(agents, world):
    _agent_apply(world, agents, 'rain', 'infection_risk', 'inverse')

def logic_18144(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'infection_risk', 'inverse')

def logic_18145(agents, world):
    _agent_apply(world, agents, 'runoff', 'infection_risk', 'inverse')

def logic_18146(agents, world):
    _agent_apply(world, agents, 'wind_x', 'infection_risk', 'inverse')

def logic_18147(agents, world):
    _agent_apply(world, agents, 'wind_y', 'infection_risk', 'inverse')

def logic_18148(agents, world):
    _agent_apply(world, agents, 'vegetation', 'infection_risk', 'inverse')

def logic_18149(agents, world):
    _agent_apply(world, agents, 'biomass', 'infection_risk', 'inverse')

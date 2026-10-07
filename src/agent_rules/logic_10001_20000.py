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

def logic_18150(agents, world):
    _agent_apply(world, agents, 'herbivore', 'infection_risk', 'inverse')

def logic_18151(agents, world):
    _agent_apply(world, agents, 'predator', 'infection_risk', 'inverse')

def logic_18152(agents, world):
    _agent_apply(world, agents, 'carrion', 'infection_risk', 'inverse')

def logic_18153(agents, world):
    _agent_apply(world, agents, 'nutrients', 'infection_risk', 'inverse')

def logic_18154(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'infection_risk', 'inverse')

def logic_18155(agents, world):
    _agent_apply(world, agents, 'oxygen', 'infection_risk', 'inverse')

def logic_18156(agents, world):
    _agent_apply(world, agents, 'co2', 'infection_risk', 'inverse')

def logic_18157(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'infection_risk', 'inverse')

def logic_18158(agents, world):
    _agent_apply(world, agents, 'ice', 'infection_risk', 'inverse')

def logic_18159(agents, world):
    _agent_apply(world, agents, 'evaporation', 'alertness', 'inverse')

def logic_18160(agents, world):
    _agent_apply(world, agents, 'detritus', 'alertness', 'inverse')

def logic_18161(agents, world):
    _agent_apply(world, agents, 'methane', 'alertness', 'inverse')

def logic_18162(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'alertness', 'inverse')

def logic_18163(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'alertness', 'inverse')

def logic_18164(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'alertness', 'inverse')

def logic_18165(agents, world):
    _agent_apply(world, agents, 'erosion', 'alertness', 'inverse')

def logic_18166(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'alertness', 'inverse')

def logic_18167(agents, world):
    _agent_apply(world, agents, 'root_density', 'alertness', 'inverse')

def logic_18168(agents, world):
    _agent_apply(world, agents, 'wetland', 'alertness', 'inverse')

def logic_18169(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'alertness', 'inverse')

def logic_18170(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'alertness', 'inverse')

def logic_18171(agents, world):
    _agent_apply(world, agents, 'ash', 'alertness', 'inverse')

def logic_18172(agents, world):
    _agent_apply(world, agents, 'snowpack', 'alertness', 'inverse')

def logic_18173(agents, world):
    _agent_apply(world, agents, 'groundwater', 'alertness', 'inverse')

def logic_18174(agents, world):
    _agent_apply(world, agents, 'sediment', 'alertness', 'inverse')

def logic_18175(agents, world):
    _agent_apply(world, agents, 'salinity', 'alertness', 'inverse')

def logic_18176(agents, world):
    _agent_apply(world, agents, 'algae', 'alertness', 'inverse')

def logic_18177(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'alertness', 'inverse')

def logic_18178(agents, world):
    _agent_apply(world, agents, 'deadwood', 'alertness', 'inverse')

def logic_18179(agents, world):
    _agent_apply(world, agents, 'pollinators', 'fear', 'square')

def logic_18180(agents, world):
    _agent_apply(world, agents, 'flowers', 'fear', 'square')

def logic_18181(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'fear', 'square')

def logic_18182(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'fear', 'square')

def logic_18183(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'fear', 'square')

def logic_18184(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'fear', 'square')

def logic_18185(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'fear', 'square')

def logic_18186(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'fear', 'square')

def logic_18187(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'fear', 'square')

def logic_18188(agents, world):
    _agent_apply(world, agents, 'hydration', 'fear', 'square')

def logic_18189(agents, world):
    _agent_apply(world, agents, 'thirst', 'fear', 'square')

def logic_18190(agents, world):
    _agent_apply(world, agents, 'hunger', 'fear', 'square')

def logic_18191(agents, world):
    _agent_apply(world, agents, 'health', 'fear', 'square')

def logic_18192(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'fear', 'square')

def logic_18193(agents, world):
    _agent_apply(world, agents, 'dehydration', 'fear', 'square')

def logic_18194(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'fear', 'square')

def logic_18195(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'fear', 'square')

def logic_18196(agents, world):
    _agent_apply(world, agents, 'alertness', 'fear', 'square')

def logic_18197(agents, world):
    _agent_apply(world, agents, 'fear', 'recovery', 'square')

def logic_18198(agents, world):
    _agent_apply(world, agents, 'recovery', 'fear', 'square')

def logic_18199(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'recovery', 'square')

def logic_18200(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'recovery', 'square')

def logic_18201(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'recovery', 'square')

def logic_18202(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'recovery', 'square')

def logic_18203(agents, world):
    _agent_apply(world, agents, 'food_access', 'recovery', 'square')

def logic_18204(agents, world):
    _agent_apply(world, agents, 'wealth', 'recovery', 'square')

def logic_18205(agents, world):
    _agent_apply(world, agents, 'stability', 'recovery', 'square')

def logic_18206(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'recovery', 'square')

def logic_18207(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'recovery', 'square')

def logic_18208(agents, world):
    _agent_apply(world, agents, 'reputation', 'recovery', 'square')

def logic_18209(agents, world):
    _agent_apply(world, agents, 'trust', 'recovery', 'square')

def logic_18210(agents, world):
    _agent_apply(world, agents, 'cooperation', 'recovery', 'square')

def logic_18211(agents, world):
    _agent_apply(world, agents, 'defection', 'recovery', 'square')

def logic_18212(agents, world):
    _agent_apply(world, agents, 'aggression', 'recovery', 'square')

def logic_18213(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'recovery', 'square')

def logic_18214(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'recovery', 'square')

def logic_18215(agents, world):
    _agent_apply(world, agents, 'territoriality', 'recovery', 'square')

def logic_18216(agents, world):
    _agent_apply(world, agents, 'group_stability', 'recovery', 'square')

def logic_18217(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'recovery', 'square')

def logic_18218(agents, world):
    _agent_apply(world, agents, 'help_drive', 'metabolic_cost', 'square')

def logic_18219(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'metabolic_cost', 'square')

def logic_18220(agents, world):
    _agent_apply(world, agents, 'selfishness', 'metabolic_cost', 'square')

def logic_18221(agents, world):
    _agent_apply(world, agents, 'generosity', 'metabolic_cost', 'square')

def logic_18222(agents, world):
    _agent_apply(world, agents, 'gratitude', 'metabolic_cost', 'square')

def logic_18223(agents, world):
    _agent_apply(world, agents, 'caution', 'metabolic_cost', 'square')

def logic_18224(agents, world):
    _agent_apply(world, agents, 'confidence', 'metabolic_cost', 'square')

def logic_18225(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'metabolic_cost', 'square')

def logic_18226(agents, world):
    _agent_apply(world, agents, 'future_help', 'metabolic_cost', 'square')

def logic_18227(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'metabolic_cost', 'square')

def logic_18228(agents, world):
    _agent_apply(world, agents, 'empathy', 'metabolic_cost', 'square')

def logic_18229(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'metabolic_cost', 'square')

def logic_18230(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'metabolic_cost', 'square')

def logic_18231(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'metabolic_cost', 'square')

def logic_18232(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'metabolic_cost', 'square')

def logic_18233(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'metabolic_cost', 'square')

def logic_18234(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'metabolic_cost', 'square')

def logic_18235(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'metabolic_cost', 'square')

def logic_18236(agents, world):
    _agent_apply(world, agents, 'stress', 'metabolic_cost', 'square')

def logic_18237(agents, world):
    _agent_apply(world, agents, 'social_need', 'metabolic_cost', 'square')

def logic_18238(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'reproduction_drive', 'square')

def logic_18239(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'reproduction_drive', 'square')

def logic_18240(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'reproduction_drive', 'square')

def logic_18241(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'reproduction_drive', 'square')

def logic_18242(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'reproduction_drive', 'square')

def logic_18243(agents, world):
    _agent_apply(world, agents, 'help_received', 'reproduction_drive', 'square')

def logic_18244(agents, world):
    _agent_apply(world, agents, 'help_given', 'reproduction_drive', 'square')

def logic_18245(agents, world):
    _agent_apply(world, agents, 'local_density', 'reproduction_drive', 'square')

def logic_18246(agents, world):
    _agent_apply(world, agents, 'last_reward', 'reproduction_drive', 'square')

def logic_18247(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'reproduction_drive', 'square')

def logic_18248(agents, world):
    _agent_apply(world, agents, 'last_food', 'reproduction_drive', 'square')

def logic_18249(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'reproduction_drive', 'square')

def logic_18250(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'reproduction_drive', 'square')

def logic_18251(agents, world):
    _agent_apply(world, agents, 'last_action', 'reproduction_drive', 'square')

def logic_18252(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'reproduction_drive', 'square')

def logic_18253(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'reproduction_drive', 'square')

def logic_18254(agents, world):
    _agent_apply(world, agents, 'competition_score', 'reproduction_drive', 'square')

def logic_18255(agents, world):
    _agent_apply(world, agents, 'defection_score', 'reproduction_drive', 'square')

def logic_18256(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'reproduction_drive', 'square')

def logic_18257(agents, world):
    _agent_apply(world, agents, 'risk_score', 'reproduction_drive', 'square')

def logic_18258(agents, world):
    _agent_apply(world, agents, 'safety_score', 'migration_drive', 'square')

def logic_18259(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'migration_drive', 'square')

def logic_18260(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'migration_drive', 'square')

def logic_18261(agents, world):
    _agent_apply(world, agents, 'survival_score', 'migration_drive', 'square')

def logic_18262(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'migration_drive', 'square')

def logic_18263(agents, world):
    _agent_apply(world, agents, 'help_score', 'migration_drive', 'square')

def logic_18264(agents, world):
    _agent_apply(world, agents, 'attack_success', 'migration_drive', 'square')

def logic_18265(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'migration_drive', 'square')

def logic_18266(agents, world):
    _agent_apply(world, agents, 'defense_score', 'migration_drive', 'square')

def logic_18267(agents, world):
    _agent_apply(world, agents, 'migration_score', 'migration_drive', 'square')

def logic_18268(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'migration_drive', 'sqrt')

def logic_18269(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'migration_drive', 'sqrt')

def logic_18270(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'migration_drive', 'sqrt')

def logic_18271(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'migration_drive', 'sqrt')

def logic_18272(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'migration_drive', 'sqrt')

def logic_18273(agents, world):
    _agent_apply(world, agents, 'memory_update', 'migration_drive', 'sqrt')

def logic_18274(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'migration_drive', 'sqrt')

def logic_18275(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'migration_drive', 'sqrt')

def logic_18276(agents, world):
    _agent_apply(world, agents, 'payoff', 'migration_drive', 'sqrt')

def logic_18277(agents, world):
    _agent_apply(world, agents, 'temperature', 'exploration_drive', 'sqrt')

def logic_18278(agents, world):
    _agent_apply(world, agents, 'surface_water', 'exploration_drive', 'sqrt')

def logic_18279(agents, world):
    _agent_apply(world, agents, 'humidity', 'exploration_drive', 'sqrt')

def logic_18280(agents, world):
    _agent_apply(world, agents, 'cloud', 'exploration_drive', 'sqrt')

def logic_18281(agents, world):
    _agent_apply(world, agents, 'rain', 'exploration_drive', 'sqrt')

def logic_18282(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'exploration_drive', 'sqrt')

def logic_18283(agents, world):
    _agent_apply(world, agents, 'runoff', 'exploration_drive', 'sqrt')

def logic_18284(agents, world):
    _agent_apply(world, agents, 'wind_x', 'exploration_drive', 'sqrt')

def logic_18285(agents, world):
    _agent_apply(world, agents, 'wind_y', 'exploration_drive', 'sqrt')

def logic_18286(agents, world):
    _agent_apply(world, agents, 'vegetation', 'exploration_drive', 'sqrt')

def logic_18287(agents, world):
    _agent_apply(world, agents, 'biomass', 'exploration_drive', 'sqrt')

def logic_18288(agents, world):
    _agent_apply(world, agents, 'herbivore', 'exploration_drive', 'sqrt')

def logic_18289(agents, world):
    _agent_apply(world, agents, 'predator', 'exploration_drive', 'sqrt')

def logic_18290(agents, world):
    _agent_apply(world, agents, 'carrion', 'exploration_drive', 'sqrt')

def logic_18291(agents, world):
    _agent_apply(world, agents, 'nutrients', 'exploration_drive', 'sqrt')

def logic_18292(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'exploration_drive', 'sqrt')

def logic_18293(agents, world):
    _agent_apply(world, agents, 'oxygen', 'exploration_drive', 'sqrt')

def logic_18294(agents, world):
    _agent_apply(world, agents, 'co2', 'exploration_drive', 'sqrt')

def logic_18295(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'exploration_drive', 'sqrt')

def logic_18296(agents, world):
    _agent_apply(world, agents, 'ice', 'exploration_drive', 'sqrt')

def logic_18297(agents, world):
    _agent_apply(world, agents, 'evaporation', 'food_access', 'sqrt')

def logic_18298(agents, world):
    _agent_apply(world, agents, 'detritus', 'food_access', 'sqrt')

def logic_18299(agents, world):
    _agent_apply(world, agents, 'methane', 'food_access', 'sqrt')

def logic_18300(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'food_access', 'sqrt')

def logic_18301(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'food_access', 'sqrt')

def logic_18302(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'food_access', 'sqrt')

def logic_18303(agents, world):
    _agent_apply(world, agents, 'erosion', 'food_access', 'sqrt')

def logic_18304(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'food_access', 'sqrt')

def logic_18305(agents, world):
    _agent_apply(world, agents, 'root_density', 'food_access', 'sqrt')

def logic_18306(agents, world):
    _agent_apply(world, agents, 'wetland', 'food_access', 'sqrt')

def logic_18307(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'food_access', 'sqrt')

def logic_18308(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'food_access', 'sqrt')

def logic_18309(agents, world):
    _agent_apply(world, agents, 'ash', 'food_access', 'sqrt')

def logic_18310(agents, world):
    _agent_apply(world, agents, 'snowpack', 'food_access', 'sqrt')

def logic_18311(agents, world):
    _agent_apply(world, agents, 'groundwater', 'food_access', 'sqrt')

def logic_18312(agents, world):
    _agent_apply(world, agents, 'sediment', 'food_access', 'sqrt')

def logic_18313(agents, world):
    _agent_apply(world, agents, 'salinity', 'food_access', 'sqrt')

def logic_18314(agents, world):
    _agent_apply(world, agents, 'algae', 'food_access', 'sqrt')

def logic_18315(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'food_access', 'sqrt')

def logic_18316(agents, world):
    _agent_apply(world, agents, 'deadwood', 'food_access', 'sqrt')

def logic_18317(agents, world):
    _agent_apply(world, agents, 'pollinators', 'wealth', 'sqrt')

def logic_18318(agents, world):
    _agent_apply(world, agents, 'flowers', 'wealth', 'sqrt')

def logic_18319(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'wealth', 'sqrt')

def logic_18320(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'wealth', 'sqrt')

def logic_18321(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'wealth', 'sqrt')

def logic_18322(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'wealth', 'sqrt')

def logic_18323(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'wealth', 'sqrt')

def logic_18324(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'wealth', 'sqrt')

def logic_18325(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'wealth', 'sqrt')

def logic_18326(agents, world):
    _agent_apply(world, agents, 'hydration', 'wealth', 'sqrt')

def logic_18327(agents, world):
    _agent_apply(world, agents, 'thirst', 'wealth', 'sqrt')

def logic_18328(agents, world):
    _agent_apply(world, agents, 'hunger', 'wealth', 'sqrt')

def logic_18329(agents, world):
    _agent_apply(world, agents, 'health', 'wealth', 'sqrt')

def logic_18330(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'wealth', 'sqrt')

def logic_18331(agents, world):
    _agent_apply(world, agents, 'dehydration', 'wealth', 'sqrt')

def logic_18332(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'wealth', 'sqrt')

def logic_18333(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'wealth', 'sqrt')

def logic_18334(agents, world):
    _agent_apply(world, agents, 'alertness', 'wealth', 'sqrt')

def logic_18335(agents, world):
    _agent_apply(world, agents, 'fear', 'wealth', 'sqrt')

def logic_18336(agents, world):
    _agent_apply(world, agents, 'recovery', 'wealth', 'sqrt')

def logic_18337(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'stability', 'sqrt')

def logic_18338(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'stability', 'sqrt')

def logic_18339(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'stability', 'sqrt')

def logic_18340(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'stability', 'sqrt')

def logic_18341(agents, world):
    _agent_apply(world, agents, 'food_access', 'stability', 'sqrt')

def logic_18342(agents, world):
    _agent_apply(world, agents, 'wealth', 'stability', 'sqrt')

def logic_18343(agents, world):
    _agent_apply(world, agents, 'stability', 'habitat_stress', 'sqrt')

def logic_18344(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'stability', 'sqrt')

def logic_18345(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'stability', 'sqrt')

def logic_18346(agents, world):
    _agent_apply(world, agents, 'reputation', 'stability', 'sqrt')

def logic_18347(agents, world):
    _agent_apply(world, agents, 'trust', 'stability', 'sqrt')

def logic_18348(agents, world):
    _agent_apply(world, agents, 'cooperation', 'stability', 'sqrt')

def logic_18349(agents, world):
    _agent_apply(world, agents, 'defection', 'stability', 'sqrt')

def logic_18350(agents, world):
    _agent_apply(world, agents, 'aggression', 'stability', 'sqrt')

def logic_18351(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'stability', 'sqrt')

def logic_18352(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'stability', 'sqrt')

def logic_18353(agents, world):
    _agent_apply(world, agents, 'territoriality', 'stability', 'sqrt')

def logic_18354(agents, world):
    _agent_apply(world, agents, 'group_stability', 'stability', 'sqrt')

def logic_18355(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'stability', 'sqrt')

def logic_18356(agents, world):
    _agent_apply(world, agents, 'help_drive', 'habitat_stress', 'sqrt')

def logic_18357(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'habitat_stress', 'pulse')

def logic_18358(agents, world):
    _agent_apply(world, agents, 'selfishness', 'habitat_stress', 'pulse')

def logic_18359(agents, world):
    _agent_apply(world, agents, 'generosity', 'habitat_stress', 'pulse')

def logic_18360(agents, world):
    _agent_apply(world, agents, 'gratitude', 'habitat_stress', 'pulse')

def logic_18361(agents, world):
    _agent_apply(world, agents, 'caution', 'habitat_stress', 'pulse')

def logic_18362(agents, world):
    _agent_apply(world, agents, 'confidence', 'habitat_stress', 'pulse')

def logic_18363(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'habitat_stress', 'pulse')

def logic_18364(agents, world):
    _agent_apply(world, agents, 'future_help', 'habitat_stress', 'pulse')

def logic_18365(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'habitat_stress', 'pulse')

def logic_18366(agents, world):
    _agent_apply(world, agents, 'empathy', 'habitat_stress', 'pulse')

def logic_18367(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'habitat_stress', 'pulse')

def logic_18368(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'habitat_stress', 'pulse')

def logic_18369(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'habitat_stress', 'pulse')

def logic_18370(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'habitat_stress', 'pulse')

def logic_18371(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'habitat_stress', 'pulse')

def logic_18372(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'habitat_stress', 'pulse')

def logic_18373(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'habitat_stress', 'pulse')

def logic_18374(agents, world):
    _agent_apply(world, agents, 'stress', 'habitat_stress', 'pulse')

def logic_18375(agents, world):
    _agent_apply(world, agents, 'social_need', 'habitat_stress', 'pulse')

def logic_18376(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'social_tolerance', 'pulse')

def logic_18377(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'social_tolerance', 'pulse')

def logic_18378(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'social_tolerance', 'pulse')

def logic_18379(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'social_tolerance', 'pulse')

def logic_18380(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'social_tolerance', 'pulse')

def logic_18381(agents, world):
    _agent_apply(world, agents, 'help_received', 'social_tolerance', 'pulse')

def logic_18382(agents, world):
    _agent_apply(world, agents, 'help_given', 'social_tolerance', 'pulse')

def logic_18383(agents, world):
    _agent_apply(world, agents, 'local_density', 'social_tolerance', 'pulse')

def logic_18384(agents, world):
    _agent_apply(world, agents, 'last_reward', 'social_tolerance', 'pulse')

def logic_18385(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'social_tolerance', 'pulse')

def logic_18386(agents, world):
    _agent_apply(world, agents, 'last_food', 'social_tolerance', 'pulse')

def logic_18387(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'social_tolerance', 'pulse')

def logic_18388(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'social_tolerance', 'pulse')

def logic_18389(agents, world):
    _agent_apply(world, agents, 'last_action', 'social_tolerance', 'pulse')

def logic_18390(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'social_tolerance', 'pulse')

def logic_18391(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'social_tolerance', 'pulse')

def logic_18392(agents, world):
    _agent_apply(world, agents, 'competition_score', 'social_tolerance', 'pulse')

def logic_18393(agents, world):
    _agent_apply(world, agents, 'defection_score', 'social_tolerance', 'pulse')

def logic_18394(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'social_tolerance', 'pulse')

def logic_18395(agents, world):
    _agent_apply(world, agents, 'risk_score', 'social_tolerance', 'pulse')

def logic_18396(agents, world):
    _agent_apply(world, agents, 'safety_score', 'reputation', 'pulse')

def logic_18397(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'reputation', 'pulse')

def logic_18398(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'reputation', 'pulse')

def logic_18399(agents, world):
    _agent_apply(world, agents, 'survival_score', 'reputation', 'pulse')

def logic_18400(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'reputation', 'pulse')

def logic_18401(agents, world):
    _agent_apply(world, agents, 'help_score', 'reputation', 'pulse')

def logic_18402(agents, world):
    _agent_apply(world, agents, 'attack_success', 'reputation', 'pulse')

def logic_18403(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'reputation', 'pulse')

def logic_18404(agents, world):
    _agent_apply(world, agents, 'defense_score', 'reputation', 'pulse')

def logic_18405(agents, world):
    _agent_apply(world, agents, 'migration_score', 'reputation', 'pulse')

def logic_18406(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'reputation', 'pulse')

def logic_18407(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'reputation', 'pulse')

def logic_18408(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'reputation', 'pulse')

def logic_18409(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'reputation', 'pulse')

def logic_18410(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'reputation', 'pulse')

def logic_18411(agents, world):
    _agent_apply(world, agents, 'memory_update', 'reputation', 'pulse')

def logic_18412(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'reputation', 'pulse')

def logic_18413(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'reputation', 'pulse')

def logic_18414(agents, world):
    _agent_apply(world, agents, 'payoff', 'reputation', 'pulse')

def logic_18415(agents, world):
    _agent_apply(world, agents, 'temperature', 'trust', 'pulse')

def logic_18416(agents, world):
    _agent_apply(world, agents, 'surface_water', 'trust', 'pulse')

def logic_18417(agents, world):
    _agent_apply(world, agents, 'humidity', 'trust', 'pulse')

def logic_18418(agents, world):
    _agent_apply(world, agents, 'cloud', 'trust', 'pulse')

def logic_18419(agents, world):
    _agent_apply(world, agents, 'rain', 'trust', 'pulse')

def logic_18420(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'trust', 'pulse')

def logic_18421(agents, world):
    _agent_apply(world, agents, 'runoff', 'trust', 'pulse')

def logic_18422(agents, world):
    _agent_apply(world, agents, 'wind_x', 'trust', 'pulse')

def logic_18423(agents, world):
    _agent_apply(world, agents, 'wind_y', 'trust', 'pulse')

def logic_18424(agents, world):
    _agent_apply(world, agents, 'vegetation', 'trust', 'pulse')

def logic_18425(agents, world):
    _agent_apply(world, agents, 'biomass', 'trust', 'pulse')

def logic_18426(agents, world):
    _agent_apply(world, agents, 'herbivore', 'trust', 'pulse')

def logic_18427(agents, world):
    _agent_apply(world, agents, 'predator', 'trust', 'pulse')

def logic_18428(agents, world):
    _agent_apply(world, agents, 'carrion', 'trust', 'pulse')

def logic_18429(agents, world):
    _agent_apply(world, agents, 'nutrients', 'trust', 'pulse')

def logic_18430(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'trust', 'pulse')

def logic_18431(agents, world):
    _agent_apply(world, agents, 'oxygen', 'trust', 'pulse')

def logic_18432(agents, world):
    _agent_apply(world, agents, 'co2', 'trust', 'pulse')

def logic_18433(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'trust', 'pulse')

def logic_18434(agents, world):
    _agent_apply(world, agents, 'ice', 'trust', 'pulse')

def logic_18435(agents, world):
    _agent_apply(world, agents, 'evaporation', 'cooperation', 'pulse')

def logic_18436(agents, world):
    _agent_apply(world, agents, 'detritus', 'cooperation', 'pulse')

def logic_18437(agents, world):
    _agent_apply(world, agents, 'methane', 'cooperation', 'pulse')

def logic_18438(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'cooperation', 'pulse')

def logic_18439(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'cooperation', 'pulse')

def logic_18440(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'cooperation', 'pulse')

def logic_18441(agents, world):
    _agent_apply(world, agents, 'erosion', 'cooperation', 'pulse')

def logic_18442(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'cooperation', 'pulse')

def logic_18443(agents, world):
    _agent_apply(world, agents, 'root_density', 'cooperation', 'pulse')

def logic_18444(agents, world):
    _agent_apply(world, agents, 'wetland', 'cooperation', 'pulse')

def logic_18445(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'cooperation', 'pulse')

def logic_18446(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'cooperation', 'threshold')

def logic_18447(agents, world):
    _agent_apply(world, agents, 'ash', 'cooperation', 'threshold')

def logic_18448(agents, world):
    _agent_apply(world, agents, 'snowpack', 'cooperation', 'threshold')

def logic_18449(agents, world):
    _agent_apply(world, agents, 'groundwater', 'cooperation', 'threshold')

def logic_18450(agents, world):
    _agent_apply(world, agents, 'sediment', 'cooperation', 'threshold')

def logic_18451(agents, world):
    _agent_apply(world, agents, 'salinity', 'cooperation', 'threshold')

def logic_18452(agents, world):
    _agent_apply(world, agents, 'algae', 'cooperation', 'threshold')

def logic_18453(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'cooperation', 'threshold')

def logic_18454(agents, world):
    _agent_apply(world, agents, 'deadwood', 'cooperation', 'threshold')

def logic_18455(agents, world):
    _agent_apply(world, agents, 'pollinators', 'defection', 'threshold')

def logic_18456(agents, world):
    _agent_apply(world, agents, 'flowers', 'defection', 'threshold')

def logic_18457(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'defection', 'threshold')

def logic_18458(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'defection', 'threshold')

def logic_18459(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'defection', 'threshold')

def logic_18460(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'defection', 'threshold')

def logic_18461(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'defection', 'threshold')

def logic_18462(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'defection', 'threshold')

def logic_18463(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'defection', 'threshold')

def logic_18464(agents, world):
    _agent_apply(world, agents, 'hydration', 'defection', 'threshold')

def logic_18465(agents, world):
    _agent_apply(world, agents, 'thirst', 'defection', 'threshold')

def logic_18466(agents, world):
    _agent_apply(world, agents, 'hunger', 'defection', 'threshold')

def logic_18467(agents, world):
    _agent_apply(world, agents, 'health', 'defection', 'threshold')

def logic_18468(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'defection', 'threshold')

def logic_18469(agents, world):
    _agent_apply(world, agents, 'dehydration', 'defection', 'threshold')

def logic_18470(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'defection', 'threshold')

def logic_18471(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'defection', 'threshold')

def logic_18472(agents, world):
    _agent_apply(world, agents, 'alertness', 'defection', 'threshold')

def logic_18473(agents, world):
    _agent_apply(world, agents, 'fear', 'defection', 'threshold')

def logic_18474(agents, world):
    _agent_apply(world, agents, 'recovery', 'defection', 'threshold')

def logic_18475(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'aggression', 'threshold')

def logic_18476(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'aggression', 'threshold')

def logic_18477(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'aggression', 'threshold')

def logic_18478(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'aggression', 'threshold')

def logic_18479(agents, world):
    _agent_apply(world, agents, 'food_access', 'aggression', 'threshold')

def logic_18480(agents, world):
    _agent_apply(world, agents, 'wealth', 'aggression', 'threshold')

def logic_18481(agents, world):
    _agent_apply(world, agents, 'stability', 'aggression', 'threshold')

def logic_18482(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'aggression', 'threshold')

def logic_18483(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'aggression', 'threshold')

def logic_18484(agents, world):
    _agent_apply(world, agents, 'reputation', 'aggression', 'threshold')

def logic_18485(agents, world):
    _agent_apply(world, agents, 'trust', 'aggression', 'threshold')

def logic_18486(agents, world):
    _agent_apply(world, agents, 'cooperation', 'aggression', 'threshold')

def logic_18487(agents, world):
    _agent_apply(world, agents, 'defection', 'aggression', 'threshold')

def logic_18488(agents, world):
    _agent_apply(world, agents, 'aggression', 'conflict_pressure', 'threshold')

def logic_18489(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'aggression', 'threshold')

def logic_18490(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'aggression', 'threshold')

def logic_18491(agents, world):
    _agent_apply(world, agents, 'territoriality', 'aggression', 'threshold')

def logic_18492(agents, world):
    _agent_apply(world, agents, 'group_stability', 'aggression', 'threshold')

def logic_18493(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'aggression', 'threshold')

def logic_18494(agents, world):
    _agent_apply(world, agents, 'help_drive', 'conflict_pressure', 'threshold')

def logic_18495(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'conflict_pressure', 'threshold')

def logic_18496(agents, world):
    _agent_apply(world, agents, 'selfishness', 'conflict_pressure', 'threshold')

def logic_18497(agents, world):
    _agent_apply(world, agents, 'generosity', 'conflict_pressure', 'threshold')

def logic_18498(agents, world):
    _agent_apply(world, agents, 'gratitude', 'conflict_pressure', 'threshold')

def logic_18499(agents, world):
    _agent_apply(world, agents, 'caution', 'conflict_pressure', 'threshold')

def logic_18500(agents, world):
    _agent_apply(world, agents, 'confidence', 'conflict_pressure', 'threshold')

def logic_18501(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'conflict_pressure', 'threshold')

def logic_18502(agents, world):
    _agent_apply(world, agents, 'future_help', 'conflict_pressure', 'threshold')

def logic_18503(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'conflict_pressure', 'threshold')

def logic_18504(agents, world):
    _agent_apply(world, agents, 'empathy', 'conflict_pressure', 'threshold')

def logic_18505(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'conflict_pressure', 'threshold')

def logic_18506(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'conflict_pressure', 'threshold')

def logic_18507(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'conflict_pressure', 'threshold')

def logic_18508(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'conflict_pressure', 'threshold')

def logic_18509(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'conflict_pressure', 'threshold')

def logic_18510(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'conflict_pressure', 'threshold')

def logic_18511(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'conflict_pressure', 'threshold')

def logic_18512(agents, world):
    _agent_apply(world, agents, 'stress', 'conflict_pressure', 'threshold')

def logic_18513(agents, world):
    _agent_apply(world, agents, 'social_need', 'conflict_pressure', 'threshold')

def logic_18514(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'competition_pressure', 'threshold')

def logic_18515(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'competition_pressure', 'threshold')

def logic_18516(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'competition_pressure', 'threshold')

def logic_18517(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'competition_pressure', 'threshold')

def logic_18518(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'competition_pressure', 'threshold')

def logic_18519(agents, world):
    _agent_apply(world, agents, 'help_received', 'competition_pressure', 'threshold')

def logic_18520(agents, world):
    _agent_apply(world, agents, 'help_given', 'competition_pressure', 'threshold')

def logic_18521(agents, world):
    _agent_apply(world, agents, 'local_density', 'competition_pressure', 'threshold')

def logic_18522(agents, world):
    _agent_apply(world, agents, 'last_reward', 'competition_pressure', 'threshold')

def logic_18523(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'competition_pressure', 'threshold')

def logic_18524(agents, world):
    _agent_apply(world, agents, 'last_food', 'competition_pressure', 'threshold')

def logic_18525(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'competition_pressure', 'threshold')

def logic_18526(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'competition_pressure', 'threshold')

def logic_18527(agents, world):
    _agent_apply(world, agents, 'last_action', 'competition_pressure', 'threshold')

def logic_18528(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'competition_pressure', 'threshold')

def logic_18529(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'competition_pressure', 'threshold')

def logic_18530(agents, world):
    _agent_apply(world, agents, 'competition_score', 'competition_pressure', 'threshold')

def logic_18531(agents, world):
    _agent_apply(world, agents, 'defection_score', 'competition_pressure', 'threshold')

def logic_18532(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'competition_pressure', 'threshold')

def logic_18533(agents, world):
    _agent_apply(world, agents, 'risk_score', 'competition_pressure', 'threshold')

def logic_18534(agents, world):
    _agent_apply(world, agents, 'safety_score', 'territoriality', 'threshold')

def logic_18535(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'territoriality', 'saturation')

def logic_18536(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'territoriality', 'saturation')

def logic_18537(agents, world):
    _agent_apply(world, agents, 'survival_score', 'territoriality', 'saturation')

def logic_18538(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'territoriality', 'saturation')

def logic_18539(agents, world):
    _agent_apply(world, agents, 'help_score', 'territoriality', 'saturation')

def logic_18540(agents, world):
    _agent_apply(world, agents, 'attack_success', 'territoriality', 'saturation')

def logic_18541(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'territoriality', 'saturation')

def logic_18542(agents, world):
    _agent_apply(world, agents, 'defense_score', 'territoriality', 'saturation')

def logic_18543(agents, world):
    _agent_apply(world, agents, 'migration_score', 'territoriality', 'saturation')

def logic_18544(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'territoriality', 'saturation')

def logic_18545(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'territoriality', 'saturation')

def logic_18546(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'territoriality', 'saturation')

def logic_18547(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'territoriality', 'saturation')

def logic_18548(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'territoriality', 'saturation')

def logic_18549(agents, world):
    _agent_apply(world, agents, 'memory_update', 'territoriality', 'saturation')

def logic_18550(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'territoriality', 'saturation')

def logic_18551(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'territoriality', 'saturation')

def logic_18552(agents, world):
    _agent_apply(world, agents, 'payoff', 'territoriality', 'saturation')

def logic_18553(agents, world):
    _agent_apply(world, agents, 'temperature', 'group_stability', 'saturation')

def logic_18554(agents, world):
    _agent_apply(world, agents, 'surface_water', 'group_stability', 'saturation')

def logic_18555(agents, world):
    _agent_apply(world, agents, 'humidity', 'group_stability', 'saturation')

def logic_18556(agents, world):
    _agent_apply(world, agents, 'cloud', 'group_stability', 'saturation')

def logic_18557(agents, world):
    _agent_apply(world, agents, 'rain', 'group_stability', 'saturation')

def logic_18558(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'group_stability', 'saturation')

def logic_18559(agents, world):
    _agent_apply(world, agents, 'runoff', 'group_stability', 'saturation')

def logic_18560(agents, world):
    _agent_apply(world, agents, 'wind_x', 'group_stability', 'saturation')

def logic_18561(agents, world):
    _agent_apply(world, agents, 'wind_y', 'group_stability', 'saturation')

def logic_18562(agents, world):
    _agent_apply(world, agents, 'vegetation', 'group_stability', 'saturation')

def logic_18563(agents, world):
    _agent_apply(world, agents, 'biomass', 'group_stability', 'saturation')

def logic_18564(agents, world):
    _agent_apply(world, agents, 'herbivore', 'group_stability', 'saturation')

def logic_18565(agents, world):
    _agent_apply(world, agents, 'predator', 'group_stability', 'saturation')

def logic_18566(agents, world):
    _agent_apply(world, agents, 'carrion', 'group_stability', 'saturation')

def logic_18567(agents, world):
    _agent_apply(world, agents, 'nutrients', 'group_stability', 'saturation')

def logic_18568(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'group_stability', 'saturation')

def logic_18569(agents, world):
    _agent_apply(world, agents, 'oxygen', 'group_stability', 'saturation')

def logic_18570(agents, world):
    _agent_apply(world, agents, 'co2', 'group_stability', 'saturation')

def logic_18571(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'group_stability', 'saturation')

def logic_18572(agents, world):
    _agent_apply(world, agents, 'ice', 'group_stability', 'saturation')

def logic_18573(agents, world):
    _agent_apply(world, agents, 'evaporation', 'sharing_capacity', 'saturation')

def logic_18574(agents, world):
    _agent_apply(world, agents, 'detritus', 'sharing_capacity', 'saturation')

def logic_18575(agents, world):
    _agent_apply(world, agents, 'methane', 'sharing_capacity', 'saturation')

def logic_18576(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'sharing_capacity', 'saturation')

def logic_18577(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'sharing_capacity', 'saturation')

def logic_18578(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'sharing_capacity', 'saturation')

def logic_18579(agents, world):
    _agent_apply(world, agents, 'erosion', 'sharing_capacity', 'saturation')

def logic_18580(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'sharing_capacity', 'saturation')

def logic_18581(agents, world):
    _agent_apply(world, agents, 'root_density', 'sharing_capacity', 'saturation')

def logic_18582(agents, world):
    _agent_apply(world, agents, 'wetland', 'sharing_capacity', 'saturation')

def logic_18583(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'sharing_capacity', 'saturation')

def logic_18584(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'sharing_capacity', 'saturation')

def logic_18585(agents, world):
    _agent_apply(world, agents, 'ash', 'sharing_capacity', 'saturation')

def logic_18586(agents, world):
    _agent_apply(world, agents, 'snowpack', 'sharing_capacity', 'saturation')

def logic_18587(agents, world):
    _agent_apply(world, agents, 'groundwater', 'sharing_capacity', 'saturation')

def logic_18588(agents, world):
    _agent_apply(world, agents, 'sediment', 'sharing_capacity', 'saturation')

def logic_18589(agents, world):
    _agent_apply(world, agents, 'salinity', 'sharing_capacity', 'saturation')

def logic_18590(agents, world):
    _agent_apply(world, agents, 'algae', 'sharing_capacity', 'saturation')

def logic_18591(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'sharing_capacity', 'saturation')

def logic_18592(agents, world):
    _agent_apply(world, agents, 'deadwood', 'sharing_capacity', 'saturation')

def logic_18593(agents, world):
    _agent_apply(world, agents, 'pollinators', 'help_drive', 'saturation')

def logic_18594(agents, world):
    _agent_apply(world, agents, 'flowers', 'help_drive', 'saturation')

def logic_18595(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'help_drive', 'saturation')

def logic_18596(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'help_drive', 'saturation')

def logic_18597(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'help_drive', 'saturation')

def logic_18598(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'help_drive', 'saturation')

def logic_18599(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'help_drive', 'saturation')

def logic_18600(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'help_drive', 'saturation')

def logic_18601(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'help_drive', 'saturation')

def logic_18602(agents, world):
    _agent_apply(world, agents, 'hydration', 'help_drive', 'saturation')

def logic_18603(agents, world):
    _agent_apply(world, agents, 'thirst', 'help_drive', 'saturation')

def logic_18604(agents, world):
    _agent_apply(world, agents, 'hunger', 'help_drive', 'saturation')

def logic_18605(agents, world):
    _agent_apply(world, agents, 'health', 'help_drive', 'saturation')

def logic_18606(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'help_drive', 'saturation')

def logic_18607(agents, world):
    _agent_apply(world, agents, 'dehydration', 'help_drive', 'saturation')

def logic_18608(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'help_drive', 'saturation')

def logic_18609(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'help_drive', 'saturation')

def logic_18610(agents, world):
    _agent_apply(world, agents, 'alertness', 'help_drive', 'saturation')

def logic_18611(agents, world):
    _agent_apply(world, agents, 'fear', 'help_drive', 'saturation')

def logic_18612(agents, world):
    _agent_apply(world, agents, 'recovery', 'help_drive', 'saturation')

def logic_18613(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'social_avoidance', 'saturation')

def logic_18614(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'social_avoidance', 'saturation')

def logic_18615(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'social_avoidance', 'saturation')

def logic_18616(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'social_avoidance', 'saturation')

def logic_18617(agents, world):
    _agent_apply(world, agents, 'food_access', 'social_avoidance', 'saturation')

def logic_18618(agents, world):
    _agent_apply(world, agents, 'wealth', 'social_avoidance', 'saturation')

def logic_18619(agents, world):
    _agent_apply(world, agents, 'stability', 'social_avoidance', 'saturation')

def logic_18620(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'social_avoidance', 'saturation')

def logic_18621(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'social_avoidance', 'saturation')

def logic_18622(agents, world):
    _agent_apply(world, agents, 'reputation', 'social_avoidance', 'saturation')

def logic_18623(agents, world):
    _agent_apply(world, agents, 'trust', 'social_avoidance', 'saturation')

def logic_18624(agents, world):
    _agent_apply(world, agents, 'cooperation', 'social_avoidance', 'reciprocal')

def logic_18625(agents, world):
    _agent_apply(world, agents, 'defection', 'social_avoidance', 'reciprocal')

def logic_18626(agents, world):
    _agent_apply(world, agents, 'aggression', 'social_avoidance', 'reciprocal')

def logic_18627(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'social_avoidance', 'reciprocal')

def logic_18628(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'social_avoidance', 'reciprocal')

def logic_18629(agents, world):
    _agent_apply(world, agents, 'territoriality', 'social_avoidance', 'reciprocal')

def logic_18630(agents, world):
    _agent_apply(world, agents, 'group_stability', 'social_avoidance', 'reciprocal')

def logic_18631(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'social_avoidance', 'reciprocal')

def logic_18632(agents, world):
    _agent_apply(world, agents, 'help_drive', 'selfishness', 'reciprocal')

def logic_18633(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'selfishness', 'reciprocal')

def logic_18634(agents, world):
    _agent_apply(world, agents, 'selfishness', 'generosity', 'reciprocal')

def logic_18635(agents, world):
    _agent_apply(world, agents, 'generosity', 'selfishness', 'reciprocal')

def logic_18636(agents, world):
    _agent_apply(world, agents, 'gratitude', 'selfishness', 'reciprocal')

def logic_18637(agents, world):
    _agent_apply(world, agents, 'caution', 'selfishness', 'reciprocal')

def logic_18638(agents, world):
    _agent_apply(world, agents, 'confidence', 'selfishness', 'reciprocal')

def logic_18639(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'selfishness', 'reciprocal')

def logic_18640(agents, world):
    _agent_apply(world, agents, 'future_help', 'selfishness', 'reciprocal')

def logic_18641(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'selfishness', 'reciprocal')

def logic_18642(agents, world):
    _agent_apply(world, agents, 'empathy', 'selfishness', 'reciprocal')

def logic_18643(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'selfishness', 'reciprocal')

def logic_18644(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'selfishness', 'reciprocal')

def logic_18645(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'selfishness', 'reciprocal')

def logic_18646(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'selfishness', 'reciprocal')

def logic_18647(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'selfishness', 'reciprocal')

def logic_18648(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'selfishness', 'reciprocal')

def logic_18649(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'selfishness', 'reciprocal')

def logic_18650(agents, world):
    _agent_apply(world, agents, 'stress', 'selfishness', 'reciprocal')

def logic_18651(agents, world):
    _agent_apply(world, agents, 'social_need', 'selfishness', 'reciprocal')

def logic_18652(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'generosity', 'reciprocal')

def logic_18653(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'generosity', 'reciprocal')

def logic_18654(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'generosity', 'reciprocal')

def logic_18655(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'generosity', 'reciprocal')

def logic_18656(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'generosity', 'reciprocal')

def logic_18657(agents, world):
    _agent_apply(world, agents, 'help_received', 'generosity', 'reciprocal')

def logic_18658(agents, world):
    _agent_apply(world, agents, 'help_given', 'generosity', 'reciprocal')

def logic_18659(agents, world):
    _agent_apply(world, agents, 'local_density', 'generosity', 'reciprocal')

def logic_18660(agents, world):
    _agent_apply(world, agents, 'last_reward', 'generosity', 'reciprocal')

def logic_18661(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'generosity', 'reciprocal')

def logic_18662(agents, world):
    _agent_apply(world, agents, 'last_food', 'generosity', 'reciprocal')

def logic_18663(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'generosity', 'reciprocal')

def logic_18664(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'generosity', 'reciprocal')

def logic_18665(agents, world):
    _agent_apply(world, agents, 'last_action', 'generosity', 'reciprocal')

def logic_18666(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'generosity', 'reciprocal')

def logic_18667(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'generosity', 'reciprocal')

def logic_18668(agents, world):
    _agent_apply(world, agents, 'competition_score', 'generosity', 'reciprocal')

def logic_18669(agents, world):
    _agent_apply(world, agents, 'defection_score', 'generosity', 'reciprocal')

def logic_18670(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'generosity', 'reciprocal')

def logic_18671(agents, world):
    _agent_apply(world, agents, 'risk_score', 'generosity', 'reciprocal')

def logic_18672(agents, world):
    _agent_apply(world, agents, 'safety_score', 'gratitude', 'reciprocal')

def logic_18673(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'gratitude', 'reciprocal')

def logic_18674(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'gratitude', 'reciprocal')

def logic_18675(agents, world):
    _agent_apply(world, agents, 'survival_score', 'gratitude', 'reciprocal')

def logic_18676(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'gratitude', 'reciprocal')

def logic_18677(agents, world):
    _agent_apply(world, agents, 'help_score', 'gratitude', 'reciprocal')

def logic_18678(agents, world):
    _agent_apply(world, agents, 'attack_success', 'gratitude', 'reciprocal')

def logic_18679(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'gratitude', 'reciprocal')

def logic_18680(agents, world):
    _agent_apply(world, agents, 'defense_score', 'gratitude', 'reciprocal')

def logic_18681(agents, world):
    _agent_apply(world, agents, 'migration_score', 'gratitude', 'reciprocal')

def logic_18682(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'gratitude', 'reciprocal')

def logic_18683(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'gratitude', 'reciprocal')

def logic_18684(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'gratitude', 'reciprocal')

def logic_18685(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'gratitude', 'reciprocal')

def logic_18686(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'gratitude', 'reciprocal')

def logic_18687(agents, world):
    _agent_apply(world, agents, 'memory_update', 'gratitude', 'reciprocal')

def logic_18688(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'gratitude', 'reciprocal')

def logic_18689(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'gratitude', 'reciprocal')

def logic_18690(agents, world):
    _agent_apply(world, agents, 'payoff', 'gratitude', 'reciprocal')

def logic_18691(agents, world):
    _agent_apply(world, agents, 'temperature', 'caution', 'reciprocal')

def logic_18692(agents, world):
    _agent_apply(world, agents, 'surface_water', 'caution', 'reciprocal')

def logic_18693(agents, world):
    _agent_apply(world, agents, 'humidity', 'caution', 'reciprocal')

def logic_18694(agents, world):
    _agent_apply(world, agents, 'cloud', 'caution', 'reciprocal')

def logic_18695(agents, world):
    _agent_apply(world, agents, 'rain', 'caution', 'reciprocal')

def logic_18696(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'caution', 'reciprocal')

def logic_18697(agents, world):
    _agent_apply(world, agents, 'runoff', 'caution', 'reciprocal')

def logic_18698(agents, world):
    _agent_apply(world, agents, 'wind_x', 'caution', 'reciprocal')

def logic_18699(agents, world):
    _agent_apply(world, agents, 'wind_y', 'caution', 'reciprocal')

def logic_18700(agents, world):
    _agent_apply(world, agents, 'vegetation', 'caution', 'reciprocal')

def logic_18701(agents, world):
    _agent_apply(world, agents, 'biomass', 'caution', 'reciprocal')

def logic_18702(agents, world):
    _agent_apply(world, agents, 'herbivore', 'caution', 'reciprocal')

def logic_18703(agents, world):
    _agent_apply(world, agents, 'predator', 'caution', 'reciprocal')

def logic_18704(agents, world):
    _agent_apply(world, agents, 'carrion', 'caution', 'reciprocal')

def logic_18705(agents, world):
    _agent_apply(world, agents, 'nutrients', 'caution', 'reciprocal')

def logic_18706(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'caution', 'reciprocal')

def logic_18707(agents, world):
    _agent_apply(world, agents, 'oxygen', 'caution', 'reciprocal')

def logic_18708(agents, world):
    _agent_apply(world, agents, 'co2', 'caution', 'reciprocal')

def logic_18709(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'caution', 'reciprocal')

def logic_18710(agents, world):
    _agent_apply(world, agents, 'ice', 'caution', 'reciprocal')

def logic_18711(agents, world):
    _agent_apply(world, agents, 'evaporation', 'confidence', 'reciprocal')

def logic_18712(agents, world):
    _agent_apply(world, agents, 'detritus', 'confidence', 'reciprocal')

def logic_18713(agents, world):
    _agent_apply(world, agents, 'methane', 'confidence', 'gap')

def logic_18714(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'confidence', 'gap')

def logic_18715(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'confidence', 'gap')

def logic_18716(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'confidence', 'gap')

def logic_18717(agents, world):
    _agent_apply(world, agents, 'erosion', 'confidence', 'gap')

def logic_18718(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'confidence', 'gap')

def logic_18719(agents, world):
    _agent_apply(world, agents, 'root_density', 'confidence', 'gap')

def logic_18720(agents, world):
    _agent_apply(world, agents, 'wetland', 'confidence', 'gap')

def logic_18721(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'confidence', 'gap')

def logic_18722(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'confidence', 'gap')

def logic_18723(agents, world):
    _agent_apply(world, agents, 'ash', 'confidence', 'gap')

def logic_18724(agents, world):
    _agent_apply(world, agents, 'snowpack', 'confidence', 'gap')

def logic_18725(agents, world):
    _agent_apply(world, agents, 'groundwater', 'confidence', 'gap')

def logic_18726(agents, world):
    _agent_apply(world, agents, 'sediment', 'confidence', 'gap')

def logic_18727(agents, world):
    _agent_apply(world, agents, 'salinity', 'confidence', 'gap')

def logic_18728(agents, world):
    _agent_apply(world, agents, 'algae', 'confidence', 'gap')

def logic_18729(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'confidence', 'gap')

def logic_18730(agents, world):
    _agent_apply(world, agents, 'deadwood', 'confidence', 'gap')

def logic_18731(agents, world):
    _agent_apply(world, agents, 'pollinators', 'strategy_confidence', 'gap')

def logic_18732(agents, world):
    _agent_apply(world, agents, 'flowers', 'strategy_confidence', 'gap')

def logic_18733(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'strategy_confidence', 'gap')

def logic_18734(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'strategy_confidence', 'gap')

def logic_18735(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'strategy_confidence', 'gap')

def logic_18736(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'strategy_confidence', 'gap')

def logic_18737(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'strategy_confidence', 'gap')

def logic_18738(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'strategy_confidence', 'gap')

def logic_18739(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'strategy_confidence', 'gap')

def logic_18740(agents, world):
    _agent_apply(world, agents, 'hydration', 'strategy_confidence', 'gap')

def logic_18741(agents, world):
    _agent_apply(world, agents, 'thirst', 'strategy_confidence', 'gap')

def logic_18742(agents, world):
    _agent_apply(world, agents, 'hunger', 'strategy_confidence', 'gap')

def logic_18743(agents, world):
    _agent_apply(world, agents, 'health', 'strategy_confidence', 'gap')

def logic_18744(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'strategy_confidence', 'gap')

def logic_18745(agents, world):
    _agent_apply(world, agents, 'dehydration', 'strategy_confidence', 'gap')

def logic_18746(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'strategy_confidence', 'gap')

def logic_18747(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'strategy_confidence', 'gap')

def logic_18748(agents, world):
    _agent_apply(world, agents, 'alertness', 'strategy_confidence', 'gap')

def logic_18749(agents, world):
    _agent_apply(world, agents, 'fear', 'strategy_confidence', 'gap')

def logic_18750(agents, world):
    _agent_apply(world, agents, 'recovery', 'strategy_confidence', 'gap')

def logic_18751(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'future_help', 'gap')

def logic_18752(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'future_help', 'gap')

def logic_18753(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'future_help', 'gap')

def logic_18754(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'future_help', 'gap')

def logic_18755(agents, world):
    _agent_apply(world, agents, 'food_access', 'future_help', 'gap')

def logic_18756(agents, world):
    _agent_apply(world, agents, 'wealth', 'future_help', 'gap')

def logic_18757(agents, world):
    _agent_apply(world, agents, 'stability', 'future_help', 'gap')

def logic_18758(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'future_help', 'gap')

def logic_18759(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'future_help', 'gap')

def logic_18760(agents, world):
    _agent_apply(world, agents, 'reputation', 'future_help', 'gap')

def logic_18761(agents, world):
    _agent_apply(world, agents, 'trust', 'future_help', 'gap')

def logic_18762(agents, world):
    _agent_apply(world, agents, 'cooperation', 'future_help', 'gap')

def logic_18763(agents, world):
    _agent_apply(world, agents, 'defection', 'future_help', 'gap')

def logic_18764(agents, world):
    _agent_apply(world, agents, 'aggression', 'future_help', 'gap')

def logic_18765(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'future_help', 'gap')

def logic_18766(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'future_help', 'gap')

def logic_18767(agents, world):
    _agent_apply(world, agents, 'territoriality', 'future_help', 'gap')

def logic_18768(agents, world):
    _agent_apply(world, agents, 'group_stability', 'future_help', 'gap')

def logic_18769(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'future_help', 'gap')

def logic_18770(agents, world):
    _agent_apply(world, agents, 'help_drive', 'resource_discovery', 'gap')

def logic_18771(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'resource_discovery', 'gap')

def logic_18772(agents, world):
    _agent_apply(world, agents, 'selfishness', 'resource_discovery', 'gap')

def logic_18773(agents, world):
    _agent_apply(world, agents, 'generosity', 'resource_discovery', 'gap')

def logic_18774(agents, world):
    _agent_apply(world, agents, 'gratitude', 'resource_discovery', 'gap')

def logic_18775(agents, world):
    _agent_apply(world, agents, 'caution', 'resource_discovery', 'gap')

def logic_18776(agents, world):
    _agent_apply(world, agents, 'confidence', 'resource_discovery', 'gap')

def logic_18777(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'resource_discovery', 'gap')

def logic_18778(agents, world):
    _agent_apply(world, agents, 'future_help', 'resource_discovery', 'gap')

def logic_18779(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'empathy', 'gap')

def logic_18780(agents, world):
    _agent_apply(world, agents, 'empathy', 'resource_discovery', 'gap')

def logic_18781(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'resource_discovery', 'gap')

def logic_18782(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'resource_discovery', 'gap')

def logic_18783(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'resource_discovery', 'gap')

def logic_18784(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'resource_discovery', 'gap')

def logic_18785(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'resource_discovery', 'gap')

def logic_18786(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'resource_discovery', 'gap')

def logic_18787(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'resource_discovery', 'gap')

def logic_18788(agents, world):
    _agent_apply(world, agents, 'stress', 'resource_discovery', 'gap')

def logic_18789(agents, world):
    _agent_apply(world, agents, 'social_need', 'resource_discovery', 'gap')

def logic_18790(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'empathy', 'gap')

def logic_18791(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'empathy', 'gap')

def logic_18792(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'empathy', 'gap')

def logic_18793(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'empathy', 'gap')

def logic_18794(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'empathy', 'gap')

def logic_18795(agents, world):
    _agent_apply(world, agents, 'help_received', 'empathy', 'gap')

def logic_18796(agents, world):
    _agent_apply(world, agents, 'help_given', 'empathy', 'gap')

def logic_18797(agents, world):
    _agent_apply(world, agents, 'local_density', 'empathy', 'gap')

def logic_18798(agents, world):
    _agent_apply(world, agents, 'last_reward', 'empathy', 'gap')

def logic_18799(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'empathy', 'gap')

def logic_18800(agents, world):
    _agent_apply(world, agents, 'last_food', 'empathy', 'gap')

def logic_18801(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'empathy', 'gap')

def logic_18802(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'empathy', 'feedback')

def logic_18803(agents, world):
    _agent_apply(world, agents, 'last_action', 'empathy', 'feedback')

def logic_18804(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'empathy', 'feedback')

def logic_18805(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'empathy', 'feedback')

def logic_18806(agents, world):
    _agent_apply(world, agents, 'competition_score', 'empathy', 'feedback')

def logic_18807(agents, world):
    _agent_apply(world, agents, 'defection_score', 'empathy', 'feedback')

def logic_18808(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'empathy', 'feedback')

def logic_18809(agents, world):
    _agent_apply(world, agents, 'risk_score', 'empathy', 'feedback')

def logic_18810(agents, world):
    _agent_apply(world, agents, 'safety_score', 'attack_threshold', 'feedback')

def logic_18811(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'attack_threshold', 'feedback')

def logic_18812(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'attack_threshold', 'feedback')

def logic_18813(agents, world):
    _agent_apply(world, agents, 'survival_score', 'attack_threshold', 'feedback')

def logic_18814(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'attack_threshold', 'feedback')

def logic_18815(agents, world):
    _agent_apply(world, agents, 'help_score', 'attack_threshold', 'feedback')

def logic_18816(agents, world):
    _agent_apply(world, agents, 'attack_success', 'attack_threshold', 'feedback')

def logic_18817(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'attack_threshold', 'feedback')

def logic_18818(agents, world):
    _agent_apply(world, agents, 'defense_score', 'attack_threshold', 'feedback')

def logic_18819(agents, world):
    _agent_apply(world, agents, 'migration_score', 'attack_threshold', 'feedback')

def logic_18820(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'attack_threshold', 'feedback')

def logic_18821(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'attack_threshold', 'feedback')

def logic_18822(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'attack_threshold', 'feedback')

def logic_18823(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'attack_threshold', 'feedback')

def logic_18824(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'attack_threshold', 'feedback')

def logic_18825(agents, world):
    _agent_apply(world, agents, 'memory_update', 'attack_threshold', 'feedback')

def logic_18826(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'attack_threshold', 'feedback')

def logic_18827(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'attack_threshold', 'feedback')

def logic_18828(agents, world):
    _agent_apply(world, agents, 'payoff', 'attack_threshold', 'feedback')

def logic_18829(agents, world):
    _agent_apply(world, agents, 'temperature', 'defection_threshold', 'feedback')

def logic_18830(agents, world):
    _agent_apply(world, agents, 'surface_water', 'defection_threshold', 'feedback')

def logic_18831(agents, world):
    _agent_apply(world, agents, 'humidity', 'defection_threshold', 'feedback')

def logic_18832(agents, world):
    _agent_apply(world, agents, 'cloud', 'defection_threshold', 'feedback')

def logic_18833(agents, world):
    _agent_apply(world, agents, 'rain', 'defection_threshold', 'feedback')

def logic_18834(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'defection_threshold', 'feedback')

def logic_18835(agents, world):
    _agent_apply(world, agents, 'runoff', 'defection_threshold', 'feedback')

def logic_18836(agents, world):
    _agent_apply(world, agents, 'wind_x', 'defection_threshold', 'feedback')

def logic_18837(agents, world):
    _agent_apply(world, agents, 'wind_y', 'defection_threshold', 'feedback')

def logic_18838(agents, world):
    _agent_apply(world, agents, 'vegetation', 'defection_threshold', 'feedback')

def logic_18839(agents, world):
    _agent_apply(world, agents, 'biomass', 'defection_threshold', 'feedback')

def logic_18840(agents, world):
    _agent_apply(world, agents, 'herbivore', 'defection_threshold', 'feedback')

def logic_18841(agents, world):
    _agent_apply(world, agents, 'predator', 'defection_threshold', 'feedback')

def logic_18842(agents, world):
    _agent_apply(world, agents, 'carrion', 'defection_threshold', 'feedback')

def logic_18843(agents, world):
    _agent_apply(world, agents, 'nutrients', 'defection_threshold', 'feedback')

def logic_18844(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'defection_threshold', 'feedback')

def logic_18845(agents, world):
    _agent_apply(world, agents, 'oxygen', 'defection_threshold', 'feedback')

def logic_18846(agents, world):
    _agent_apply(world, agents, 'co2', 'defection_threshold', 'feedback')

def logic_18847(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'defection_threshold', 'feedback')

def logic_18848(agents, world):
    _agent_apply(world, agents, 'ice', 'defection_threshold', 'feedback')

def logic_18849(agents, world):
    _agent_apply(world, agents, 'evaporation', 'oxygen_need', 'feedback')

def logic_18850(agents, world):
    _agent_apply(world, agents, 'detritus', 'oxygen_need', 'feedback')

def logic_18851(agents, world):
    _agent_apply(world, agents, 'methane', 'oxygen_need', 'feedback')

def logic_18852(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'oxygen_need', 'feedback')

def logic_18853(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'oxygen_need', 'feedback')

def logic_18854(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'oxygen_need', 'feedback')

def logic_18855(agents, world):
    _agent_apply(world, agents, 'erosion', 'oxygen_need', 'feedback')

def logic_18856(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'oxygen_need', 'feedback')

def logic_18857(agents, world):
    _agent_apply(world, agents, 'root_density', 'oxygen_need', 'feedback')

def logic_18858(agents, world):
    _agent_apply(world, agents, 'wetland', 'oxygen_need', 'feedback')

def logic_18859(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'oxygen_need', 'feedback')

def logic_18860(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'oxygen_need', 'feedback')

def logic_18861(agents, world):
    _agent_apply(world, agents, 'ash', 'oxygen_need', 'feedback')

def logic_18862(agents, world):
    _agent_apply(world, agents, 'snowpack', 'oxygen_need', 'feedback')

def logic_18863(agents, world):
    _agent_apply(world, agents, 'groundwater', 'oxygen_need', 'feedback')

def logic_18864(agents, world):
    _agent_apply(world, agents, 'sediment', 'oxygen_need', 'feedback')

def logic_18865(agents, world):
    _agent_apply(world, agents, 'salinity', 'oxygen_need', 'feedback')

def logic_18866(agents, world):
    _agent_apply(world, agents, 'algae', 'oxygen_need', 'feedback')

def logic_18867(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'oxygen_need', 'feedback')

def logic_18868(agents, world):
    _agent_apply(world, agents, 'deadwood', 'oxygen_need', 'feedback')

def logic_18869(agents, world):
    _agent_apply(world, agents, 'pollinators', 'shelter_need', 'feedback')

def logic_18870(agents, world):
    _agent_apply(world, agents, 'flowers', 'shelter_need', 'feedback')

def logic_18871(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'shelter_need', 'feedback')

def logic_18872(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'shelter_need', 'feedback')

def logic_18873(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'shelter_need', 'feedback')

def logic_18874(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'shelter_need', 'feedback')

def logic_18875(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'shelter_need', 'feedback')

def logic_18876(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'shelter_need', 'feedback')

def logic_18877(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'shelter_need', 'feedback')

def logic_18878(agents, world):
    _agent_apply(world, agents, 'hydration', 'shelter_need', 'feedback')

def logic_18879(agents, world):
    _agent_apply(world, agents, 'thirst', 'shelter_need', 'feedback')

def logic_18880(agents, world):
    _agent_apply(world, agents, 'hunger', 'shelter_need', 'feedback')

def logic_18881(agents, world):
    _agent_apply(world, agents, 'health', 'shelter_need', 'feedback')

def logic_18882(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'shelter_need', 'feedback')

def logic_18883(agents, world):
    _agent_apply(world, agents, 'dehydration', 'shelter_need', 'feedback')

def logic_18884(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'shelter_need', 'feedback')

def logic_18885(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'shelter_need', 'feedback')

def logic_18886(agents, world):
    _agent_apply(world, agents, 'alertness', 'shelter_need', 'feedback')

def logic_18887(agents, world):
    _agent_apply(world, agents, 'fear', 'shelter_need', 'feedback')

def logic_18888(agents, world):
    _agent_apply(world, agents, 'recovery', 'shelter_need', 'feedback')

def logic_18889(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'fire_fear', 'feedback')

def logic_18890(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'fire_fear', 'feedback')

def logic_18891(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'fire_fear', 'direct')

def logic_18892(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'fire_fear', 'direct')

def logic_18893(agents, world):
    _agent_apply(world, agents, 'food_access', 'fire_fear', 'direct')

def logic_18894(agents, world):
    _agent_apply(world, agents, 'wealth', 'fire_fear', 'direct')

def logic_18895(agents, world):
    _agent_apply(world, agents, 'stability', 'fire_fear', 'direct')

def logic_18896(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'fire_fear', 'direct')

def logic_18897(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'fire_fear', 'direct')

def logic_18898(agents, world):
    _agent_apply(world, agents, 'reputation', 'fire_fear', 'direct')

def logic_18899(agents, world):
    _agent_apply(world, agents, 'trust', 'fire_fear', 'direct')

def logic_18900(agents, world):
    _agent_apply(world, agents, 'cooperation', 'fire_fear', 'direct')

def logic_18901(agents, world):
    _agent_apply(world, agents, 'defection', 'fire_fear', 'direct')

def logic_18902(agents, world):
    _agent_apply(world, agents, 'aggression', 'fire_fear', 'direct')

def logic_18903(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'fire_fear', 'direct')

def logic_18904(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'fire_fear', 'direct')

def logic_18905(agents, world):
    _agent_apply(world, agents, 'territoriality', 'fire_fear', 'direct')

def logic_18906(agents, world):
    _agent_apply(world, agents, 'group_stability', 'fire_fear', 'direct')

def logic_18907(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'fire_fear', 'direct')

def logic_18908(agents, world):
    _agent_apply(world, agents, 'help_drive', 'resource_competition', 'direct')

def logic_18909(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'resource_competition', 'direct')

def logic_18910(agents, world):
    _agent_apply(world, agents, 'selfishness', 'resource_competition', 'direct')

def logic_18911(agents, world):
    _agent_apply(world, agents, 'generosity', 'resource_competition', 'direct')

def logic_18912(agents, world):
    _agent_apply(world, agents, 'gratitude', 'resource_competition', 'direct')

def logic_18913(agents, world):
    _agent_apply(world, agents, 'caution', 'resource_competition', 'direct')

def logic_18914(agents, world):
    _agent_apply(world, agents, 'confidence', 'resource_competition', 'direct')

def logic_18915(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'resource_competition', 'direct')

def logic_18916(agents, world):
    _agent_apply(world, agents, 'future_help', 'resource_competition', 'direct')

def logic_18917(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'resource_competition', 'direct')

def logic_18918(agents, world):
    _agent_apply(world, agents, 'empathy', 'resource_competition', 'direct')

def logic_18919(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'resource_competition', 'direct')

def logic_18920(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'resource_competition', 'direct')

def logic_18921(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'resource_competition', 'direct')

def logic_18922(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'resource_competition', 'direct')

def logic_18923(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'resource_competition', 'direct')

def logic_18924(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'vegetation_expectation', 'direct')

def logic_18925(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'resource_competition', 'direct')

def logic_18926(agents, world):
    _agent_apply(world, agents, 'stress', 'resource_competition', 'direct')

def logic_18927(agents, world):
    _agent_apply(world, agents, 'social_need', 'resource_competition', 'direct')

def logic_18928(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'vegetation_expectation', 'direct')

def logic_18929(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'vegetation_expectation', 'direct')

def logic_18930(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'vegetation_expectation', 'direct')

def logic_18931(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'vegetation_expectation', 'direct')

def logic_18932(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'vegetation_expectation', 'direct')

def logic_18933(agents, world):
    _agent_apply(world, agents, 'help_received', 'vegetation_expectation', 'direct')

def logic_18934(agents, world):
    _agent_apply(world, agents, 'help_given', 'vegetation_expectation', 'direct')

def logic_18935(agents, world):
    _agent_apply(world, agents, 'local_density', 'vegetation_expectation', 'direct')

def logic_18936(agents, world):
    _agent_apply(world, agents, 'last_reward', 'vegetation_expectation', 'direct')

def logic_18937(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'vegetation_expectation', 'direct')

def logic_18938(agents, world):
    _agent_apply(world, agents, 'last_food', 'vegetation_expectation', 'direct')

def logic_18939(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'vegetation_expectation', 'direct')

def logic_18940(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'vegetation_expectation', 'direct')

def logic_18941(agents, world):
    _agent_apply(world, agents, 'last_action', 'vegetation_expectation', 'direct')

def logic_18942(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'vegetation_expectation', 'direct')

def logic_18943(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'vegetation_expectation', 'direct')

def logic_18944(agents, world):
    _agent_apply(world, agents, 'competition_score', 'vegetation_expectation', 'direct')

def logic_18945(agents, world):
    _agent_apply(world, agents, 'defection_score', 'vegetation_expectation', 'direct')

def logic_18946(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'vegetation_expectation', 'direct')

def logic_18947(agents, world):
    _agent_apply(world, agents, 'risk_score', 'vegetation_expectation', 'direct')

def logic_18948(agents, world):
    _agent_apply(world, agents, 'safety_score', 'stress', 'direct')

def logic_18949(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'stress', 'direct')

def logic_18950(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'stress', 'direct')

def logic_18951(agents, world):
    _agent_apply(world, agents, 'survival_score', 'stress', 'direct')

def logic_18952(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'stress', 'direct')

def logic_18953(agents, world):
    _agent_apply(world, agents, 'help_score', 'stress', 'direct')

def logic_18954(agents, world):
    _agent_apply(world, agents, 'attack_success', 'stress', 'direct')

def logic_18955(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'stress', 'direct')

def logic_18956(agents, world):
    _agent_apply(world, agents, 'defense_score', 'stress', 'direct')

def logic_18957(agents, world):
    _agent_apply(world, agents, 'migration_score', 'stress', 'direct')

def logic_18958(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'stress', 'direct')

def logic_18959(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'stress', 'direct')

def logic_18960(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'stress', 'direct')

def logic_18961(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'stress', 'direct')

def logic_18962(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'stress', 'direct')

def logic_18963(agents, world):
    _agent_apply(world, agents, 'memory_update', 'stress', 'direct')

def logic_18964(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'stress', 'direct')

def logic_18965(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'stress', 'direct')

def logic_18966(agents, world):
    _agent_apply(world, agents, 'payoff', 'stress', 'direct')

def logic_18967(agents, world):
    _agent_apply(world, agents, 'temperature', 'social_need', 'direct')

def logic_18968(agents, world):
    _agent_apply(world, agents, 'surface_water', 'social_need', 'direct')

def logic_18969(agents, world):
    _agent_apply(world, agents, 'humidity', 'social_need', 'direct')

def logic_18970(agents, world):
    _agent_apply(world, agents, 'cloud', 'social_need', 'direct')

def logic_18971(agents, world):
    _agent_apply(world, agents, 'rain', 'social_need', 'direct')

def logic_18972(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'social_need', 'direct')

def logic_18973(agents, world):
    _agent_apply(world, agents, 'runoff', 'social_need', 'direct')

def logic_18974(agents, world):
    _agent_apply(world, agents, 'wind_x', 'social_need', 'direct')

def logic_18975(agents, world):
    _agent_apply(world, agents, 'wind_y', 'social_need', 'direct')

def logic_18976(agents, world):
    _agent_apply(world, agents, 'vegetation', 'social_need', 'direct')

def logic_18977(agents, world):
    _agent_apply(world, agents, 'biomass', 'social_need', 'direct')

def logic_18978(agents, world):
    _agent_apply(world, agents, 'herbivore', 'social_need', 'direct')

def logic_18979(agents, world):
    _agent_apply(world, agents, 'predator', 'social_need', 'direct')

def logic_18980(agents, world):
    _agent_apply(world, agents, 'carrion', 'social_need', 'inverse')

def logic_18981(agents, world):
    _agent_apply(world, agents, 'nutrients', 'social_need', 'inverse')

def logic_18982(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'social_need', 'inverse')

def logic_18983(agents, world):
    _agent_apply(world, agents, 'oxygen', 'social_need', 'inverse')

def logic_18984(agents, world):
    _agent_apply(world, agents, 'co2', 'social_need', 'inverse')

def logic_18985(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'social_need', 'inverse')

def logic_18986(agents, world):
    _agent_apply(world, agents, 'ice', 'social_need', 'inverse')

def logic_18987(agents, world):
    _agent_apply(world, agents, 'evaporation', 'neighbor_energy_gap', 'inverse')

def logic_18988(agents, world):
    _agent_apply(world, agents, 'detritus', 'neighbor_energy_gap', 'inverse')

def logic_18989(agents, world):
    _agent_apply(world, agents, 'methane', 'neighbor_energy_gap', 'inverse')

def logic_18990(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'neighbor_energy_gap', 'inverse')

def logic_18991(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'neighbor_energy_gap', 'inverse')

def logic_18992(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'neighbor_energy_gap', 'inverse')

def logic_18993(agents, world):
    _agent_apply(world, agents, 'erosion', 'neighbor_energy_gap', 'inverse')

def logic_18994(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'neighbor_energy_gap', 'inverse')

def logic_18995(agents, world):
    _agent_apply(world, agents, 'root_density', 'neighbor_energy_gap', 'inverse')

def logic_18996(agents, world):
    _agent_apply(world, agents, 'wetland', 'neighbor_energy_gap', 'inverse')

def logic_18997(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'neighbor_energy_gap', 'inverse')

def logic_18998(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'neighbor_energy_gap', 'inverse')

def logic_18999(agents, world):
    _agent_apply(world, agents, 'ash', 'neighbor_energy_gap', 'inverse')

def logic_19000(agents, world):
    _agent_apply(world, agents, 'snowpack', 'neighbor_energy_gap', 'inverse')

def logic_19001(agents, world):
    _agent_apply(world, agents, 'groundwater', 'neighbor_energy_gap', 'inverse')

def logic_19002(agents, world):
    _agent_apply(world, agents, 'sediment', 'neighbor_energy_gap', 'inverse')

def logic_19003(agents, world):
    _agent_apply(world, agents, 'salinity', 'neighbor_energy_gap', 'inverse')

def logic_19004(agents, world):
    _agent_apply(world, agents, 'algae', 'neighbor_energy_gap', 'inverse')

def logic_19005(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'neighbor_energy_gap', 'inverse')

def logic_19006(agents, world):
    _agent_apply(world, agents, 'deadwood', 'neighbor_energy_gap', 'inverse')

def logic_19007(agents, world):
    _agent_apply(world, agents, 'pollinators', 'neighbor_health_gap', 'inverse')

def logic_19008(agents, world):
    _agent_apply(world, agents, 'flowers', 'neighbor_health_gap', 'inverse')

def logic_19009(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'neighbor_health_gap', 'inverse')

def logic_19010(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'neighbor_health_gap', 'inverse')

def logic_19011(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'neighbor_health_gap', 'inverse')

def logic_19012(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'neighbor_health_gap', 'inverse')

def logic_19013(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'neighbor_health_gap', 'inverse')

def logic_19014(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'neighbor_health_gap', 'inverse')

def logic_19015(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'neighbor_health_gap', 'inverse')

def logic_19016(agents, world):
    _agent_apply(world, agents, 'hydration', 'neighbor_health_gap', 'inverse')

def logic_19017(agents, world):
    _agent_apply(world, agents, 'thirst', 'neighbor_health_gap', 'inverse')

def logic_19018(agents, world):
    _agent_apply(world, agents, 'hunger', 'neighbor_health_gap', 'inverse')

def logic_19019(agents, world):
    _agent_apply(world, agents, 'health', 'neighbor_health_gap', 'inverse')

def logic_19020(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'neighbor_health_gap', 'inverse')

def logic_19021(agents, world):
    _agent_apply(world, agents, 'dehydration', 'neighbor_health_gap', 'inverse')

def logic_19022(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'neighbor_health_gap', 'inverse')

def logic_19023(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'neighbor_health_gap', 'inverse')

def logic_19024(agents, world):
    _agent_apply(world, agents, 'alertness', 'neighbor_health_gap', 'inverse')

def logic_19025(agents, world):
    _agent_apply(world, agents, 'fear', 'neighbor_health_gap', 'inverse')

def logic_19026(agents, world):
    _agent_apply(world, agents, 'recovery', 'neighbor_health_gap', 'inverse')

def logic_19027(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'betrayal_memory', 'inverse')

def logic_19028(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'betrayal_memory', 'inverse')

def logic_19029(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'betrayal_memory', 'inverse')

def logic_19030(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'betrayal_memory', 'inverse')

def logic_19031(agents, world):
    _agent_apply(world, agents, 'food_access', 'betrayal_memory', 'inverse')

def logic_19032(agents, world):
    _agent_apply(world, agents, 'wealth', 'betrayal_memory', 'inverse')

def logic_19033(agents, world):
    _agent_apply(world, agents, 'stability', 'betrayal_memory', 'inverse')

def logic_19034(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'betrayal_memory', 'inverse')

def logic_19035(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'betrayal_memory', 'inverse')

def logic_19036(agents, world):
    _agent_apply(world, agents, 'reputation', 'betrayal_memory', 'inverse')

def logic_19037(agents, world):
    _agent_apply(world, agents, 'trust', 'betrayal_memory', 'inverse')

def logic_19038(agents, world):
    _agent_apply(world, agents, 'cooperation', 'betrayal_memory', 'inverse')

def logic_19039(agents, world):
    _agent_apply(world, agents, 'defection', 'betrayal_memory', 'inverse')

def logic_19040(agents, world):
    _agent_apply(world, agents, 'aggression', 'betrayal_memory', 'inverse')

def logic_19041(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'betrayal_memory', 'inverse')

def logic_19042(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'betrayal_memory', 'inverse')

def logic_19043(agents, world):
    _agent_apply(world, agents, 'territoriality', 'betrayal_memory', 'inverse')

def logic_19044(agents, world):
    _agent_apply(world, agents, 'group_stability', 'betrayal_memory', 'inverse')

def logic_19045(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'betrayal_memory', 'inverse')

def logic_19046(agents, world):
    _agent_apply(world, agents, 'help_drive', 'conflict_history', 'inverse')

def logic_19047(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'conflict_history', 'inverse')

def logic_19048(agents, world):
    _agent_apply(world, agents, 'selfishness', 'conflict_history', 'inverse')

def logic_19049(agents, world):
    _agent_apply(world, agents, 'generosity', 'conflict_history', 'inverse')

def logic_19050(agents, world):
    _agent_apply(world, agents, 'gratitude', 'conflict_history', 'inverse')

def logic_19051(agents, world):
    _agent_apply(world, agents, 'caution', 'conflict_history', 'inverse')

def logic_19052(agents, world):
    _agent_apply(world, agents, 'confidence', 'conflict_history', 'inverse')

def logic_19053(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'conflict_history', 'inverse')

def logic_19054(agents, world):
    _agent_apply(world, agents, 'future_help', 'conflict_history', 'inverse')

def logic_19055(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'conflict_history', 'inverse')

def logic_19056(agents, world):
    _agent_apply(world, agents, 'empathy', 'conflict_history', 'inverse')

def logic_19057(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'conflict_history', 'inverse')

def logic_19058(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'conflict_history', 'inverse')

def logic_19059(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'conflict_history', 'inverse')

def logic_19060(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'conflict_history', 'inverse')

def logic_19061(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'conflict_history', 'inverse')

def logic_19062(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'conflict_history', 'inverse')

def logic_19063(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'conflict_history', 'inverse')

def logic_19064(agents, world):
    _agent_apply(world, agents, 'stress', 'conflict_history', 'inverse')

def logic_19065(agents, world):
    _agent_apply(world, agents, 'social_need', 'conflict_history', 'inverse')

def logic_19066(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'cooperation_history', 'inverse')

def logic_19067(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'cooperation_history', 'inverse')

def logic_19068(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'cooperation_history', 'inverse')

def logic_19069(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'cooperation_history', 'square')

def logic_19070(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'help_received', 'square')

def logic_19071(agents, world):
    _agent_apply(world, agents, 'help_received', 'cooperation_history', 'square')

def logic_19072(agents, world):
    _agent_apply(world, agents, 'help_given', 'cooperation_history', 'square')

def logic_19073(agents, world):
    _agent_apply(world, agents, 'local_density', 'cooperation_history', 'square')

def logic_19074(agents, world):
    _agent_apply(world, agents, 'last_reward', 'cooperation_history', 'square')

def logic_19075(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'cooperation_history', 'square')

def logic_19076(agents, world):
    _agent_apply(world, agents, 'last_food', 'cooperation_history', 'square')

def logic_19077(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'cooperation_history', 'square')

def logic_19078(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'cooperation_history', 'square')

def logic_19079(agents, world):
    _agent_apply(world, agents, 'last_action', 'cooperation_history', 'square')

def logic_19080(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'cooperation_history', 'square')

def logic_19081(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'cooperation_history', 'square')

def logic_19082(agents, world):
    _agent_apply(world, agents, 'competition_score', 'cooperation_history', 'square')

def logic_19083(agents, world):
    _agent_apply(world, agents, 'defection_score', 'cooperation_history', 'square')

def logic_19084(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'cooperation_history', 'square')

def logic_19085(agents, world):
    _agent_apply(world, agents, 'risk_score', 'cooperation_history', 'square')

def logic_19086(agents, world):
    _agent_apply(world, agents, 'safety_score', 'help_received', 'square')

def logic_19087(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'help_received', 'square')

def logic_19088(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'help_received', 'square')

def logic_19089(agents, world):
    _agent_apply(world, agents, 'survival_score', 'help_received', 'square')

def logic_19090(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'help_received', 'square')

def logic_19091(agents, world):
    _agent_apply(world, agents, 'help_score', 'help_received', 'square')

def logic_19092(agents, world):
    _agent_apply(world, agents, 'attack_success', 'help_received', 'square')

def logic_19093(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'help_received', 'square')

def logic_19094(agents, world):
    _agent_apply(world, agents, 'defense_score', 'help_received', 'square')

def logic_19095(agents, world):
    _agent_apply(world, agents, 'migration_score', 'help_received', 'square')

def logic_19096(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'help_received', 'square')

def logic_19097(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'help_received', 'square')

def logic_19098(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'help_received', 'square')

def logic_19099(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'help_received', 'square')

def logic_19100(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'help_received', 'square')

def logic_19101(agents, world):
    _agent_apply(world, agents, 'memory_update', 'help_received', 'square')

def logic_19102(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'help_received', 'square')

def logic_19103(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'help_received', 'square')

def logic_19104(agents, world):
    _agent_apply(world, agents, 'payoff', 'help_received', 'square')

def logic_19105(agents, world):
    _agent_apply(world, agents, 'temperature', 'help_given', 'square')

def logic_19106(agents, world):
    _agent_apply(world, agents, 'surface_water', 'help_given', 'square')

def logic_19107(agents, world):
    _agent_apply(world, agents, 'humidity', 'help_given', 'square')

def logic_19108(agents, world):
    _agent_apply(world, agents, 'cloud', 'help_given', 'square')

def logic_19109(agents, world):
    _agent_apply(world, agents, 'rain', 'help_given', 'square')

def logic_19110(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'help_given', 'square')

def logic_19111(agents, world):
    _agent_apply(world, agents, 'runoff', 'help_given', 'square')

def logic_19112(agents, world):
    _agent_apply(world, agents, 'wind_x', 'help_given', 'square')

def logic_19113(agents, world):
    _agent_apply(world, agents, 'wind_y', 'help_given', 'square')

def logic_19114(agents, world):
    _agent_apply(world, agents, 'vegetation', 'help_given', 'square')

def logic_19115(agents, world):
    _agent_apply(world, agents, 'biomass', 'help_given', 'square')

def logic_19116(agents, world):
    _agent_apply(world, agents, 'herbivore', 'help_given', 'square')

def logic_19117(agents, world):
    _agent_apply(world, agents, 'predator', 'help_given', 'square')

def logic_19118(agents, world):
    _agent_apply(world, agents, 'carrion', 'help_given', 'square')

def logic_19119(agents, world):
    _agent_apply(world, agents, 'nutrients', 'help_given', 'square')

def logic_19120(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'help_given', 'square')

def logic_19121(agents, world):
    _agent_apply(world, agents, 'oxygen', 'help_given', 'square')

def logic_19122(agents, world):
    _agent_apply(world, agents, 'co2', 'help_given', 'square')

def logic_19123(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'help_given', 'square')

def logic_19124(agents, world):
    _agent_apply(world, agents, 'ice', 'help_given', 'square')

def logic_19125(agents, world):
    _agent_apply(world, agents, 'evaporation', 'local_density', 'square')

def logic_19126(agents, world):
    _agent_apply(world, agents, 'detritus', 'local_density', 'square')

def logic_19127(agents, world):
    _agent_apply(world, agents, 'methane', 'local_density', 'square')

def logic_19128(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'local_density', 'square')

def logic_19129(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'local_density', 'square')

def logic_19130(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'local_density', 'square')

def logic_19131(agents, world):
    _agent_apply(world, agents, 'erosion', 'local_density', 'square')

def logic_19132(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'local_density', 'square')

def logic_19133(agents, world):
    _agent_apply(world, agents, 'root_density', 'local_density', 'square')

def logic_19134(agents, world):
    _agent_apply(world, agents, 'wetland', 'local_density', 'square')

def logic_19135(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'local_density', 'square')

def logic_19136(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'local_density', 'square')

def logic_19137(agents, world):
    _agent_apply(world, agents, 'ash', 'local_density', 'square')

def logic_19138(agents, world):
    _agent_apply(world, agents, 'snowpack', 'local_density', 'square')

def logic_19139(agents, world):
    _agent_apply(world, agents, 'groundwater', 'local_density', 'square')

def logic_19140(agents, world):
    _agent_apply(world, agents, 'sediment', 'local_density', 'square')

def logic_19141(agents, world):
    _agent_apply(world, agents, 'salinity', 'local_density', 'square')

def logic_19142(agents, world):
    _agent_apply(world, agents, 'algae', 'local_density', 'square')

def logic_19143(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'local_density', 'square')

def logic_19144(agents, world):
    _agent_apply(world, agents, 'deadwood', 'local_density', 'square')

def logic_19145(agents, world):
    _agent_apply(world, agents, 'pollinators', 'last_reward', 'square')

def logic_19146(agents, world):
    _agent_apply(world, agents, 'flowers', 'last_reward', 'square')

def logic_19147(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'last_reward', 'square')

def logic_19148(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'last_reward', 'square')

def logic_19149(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'last_reward', 'square')

def logic_19150(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'last_reward', 'square')

def logic_19151(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'last_reward', 'square')

def logic_19152(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'last_reward', 'square')

def logic_19153(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'last_reward', 'square')

def logic_19154(agents, world):
    _agent_apply(world, agents, 'hydration', 'last_reward', 'square')

def logic_19155(agents, world):
    _agent_apply(world, agents, 'thirst', 'last_reward', 'square')

def logic_19156(agents, world):
    _agent_apply(world, agents, 'hunger', 'last_reward', 'square')

def logic_19157(agents, world):
    _agent_apply(world, agents, 'health', 'last_reward', 'square')

def logic_19158(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'last_reward', 'sqrt')

def logic_19159(agents, world):
    _agent_apply(world, agents, 'dehydration', 'last_reward', 'sqrt')

def logic_19160(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'last_reward', 'sqrt')

def logic_19161(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'last_reward', 'sqrt')

def logic_19162(agents, world):
    _agent_apply(world, agents, 'alertness', 'last_reward', 'sqrt')

def logic_19163(agents, world):
    _agent_apply(world, agents, 'fear', 'last_reward', 'sqrt')

def logic_19164(agents, world):
    _agent_apply(world, agents, 'recovery', 'last_reward', 'sqrt')

def logic_19165(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'last_energy_delta', 'sqrt')

def logic_19166(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'last_energy_delta', 'sqrt')

def logic_19167(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'last_energy_delta', 'sqrt')

def logic_19168(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'last_energy_delta', 'sqrt')

def logic_19169(agents, world):
    _agent_apply(world, agents, 'food_access', 'last_energy_delta', 'sqrt')

def logic_19170(agents, world):
    _agent_apply(world, agents, 'wealth', 'last_energy_delta', 'sqrt')

def logic_19171(agents, world):
    _agent_apply(world, agents, 'stability', 'last_energy_delta', 'sqrt')

def logic_19172(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'last_energy_delta', 'sqrt')

def logic_19173(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'last_energy_delta', 'sqrt')

def logic_19174(agents, world):
    _agent_apply(world, agents, 'reputation', 'last_energy_delta', 'sqrt')

def logic_19175(agents, world):
    _agent_apply(world, agents, 'trust', 'last_energy_delta', 'sqrt')

def logic_19176(agents, world):
    _agent_apply(world, agents, 'cooperation', 'last_energy_delta', 'sqrt')

def logic_19177(agents, world):
    _agent_apply(world, agents, 'defection', 'last_energy_delta', 'sqrt')

def logic_19178(agents, world):
    _agent_apply(world, agents, 'aggression', 'last_energy_delta', 'sqrt')

def logic_19179(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'last_energy_delta', 'sqrt')

def logic_19180(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'last_energy_delta', 'sqrt')

def logic_19181(agents, world):
    _agent_apply(world, agents, 'territoriality', 'last_energy_delta', 'sqrt')

def logic_19182(agents, world):
    _agent_apply(world, agents, 'group_stability', 'last_energy_delta', 'sqrt')

def logic_19183(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'last_energy_delta', 'sqrt')

def logic_19184(agents, world):
    _agent_apply(world, agents, 'help_drive', 'last_food', 'sqrt')

def logic_19185(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'last_food', 'sqrt')

def logic_19186(agents, world):
    _agent_apply(world, agents, 'selfishness', 'last_food', 'sqrt')

def logic_19187(agents, world):
    _agent_apply(world, agents, 'generosity', 'last_food', 'sqrt')

def logic_19188(agents, world):
    _agent_apply(world, agents, 'gratitude', 'last_food', 'sqrt')

def logic_19189(agents, world):
    _agent_apply(world, agents, 'caution', 'last_food', 'sqrt')

def logic_19190(agents, world):
    _agent_apply(world, agents, 'confidence', 'last_food', 'sqrt')

def logic_19191(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'last_food', 'sqrt')

def logic_19192(agents, world):
    _agent_apply(world, agents, 'future_help', 'last_food', 'sqrt')

def logic_19193(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'last_food', 'sqrt')

def logic_19194(agents, world):
    _agent_apply(world, agents, 'empathy', 'last_food', 'sqrt')

def logic_19195(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'last_food', 'sqrt')

def logic_19196(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'last_food', 'sqrt')

def logic_19197(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'last_food', 'sqrt')

def logic_19198(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'last_food', 'sqrt')

def logic_19199(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'last_food', 'sqrt')

def logic_19200(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'last_food', 'sqrt')

def logic_19201(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'last_food', 'sqrt')

def logic_19202(agents, world):
    _agent_apply(world, agents, 'stress', 'last_food', 'sqrt')

def logic_19203(agents, world):
    _agent_apply(world, agents, 'social_need', 'last_food', 'sqrt')

def logic_19204(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'last_interaction', 'sqrt')

def logic_19205(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'last_interaction', 'sqrt')

def logic_19206(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'last_interaction', 'sqrt')

def logic_19207(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'last_interaction', 'sqrt')

def logic_19208(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'last_interaction', 'sqrt')

def logic_19209(agents, world):
    _agent_apply(world, agents, 'help_received', 'last_interaction', 'sqrt')

def logic_19210(agents, world):
    _agent_apply(world, agents, 'help_given', 'last_interaction', 'sqrt')

def logic_19211(agents, world):
    _agent_apply(world, agents, 'local_density', 'last_interaction', 'sqrt')

def logic_19212(agents, world):
    _agent_apply(world, agents, 'last_reward', 'last_interaction', 'sqrt')

def logic_19213(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'last_interaction', 'sqrt')

def logic_19214(agents, world):
    _agent_apply(world, agents, 'last_food', 'last_interaction', 'sqrt')

def logic_19215(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'risk_tolerance', 'sqrt')

def logic_19216(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'last_interaction', 'sqrt')

def logic_19217(agents, world):
    _agent_apply(world, agents, 'last_action', 'last_interaction', 'sqrt')

def logic_19218(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'last_interaction', 'sqrt')

def logic_19219(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'last_interaction', 'sqrt')

def logic_19220(agents, world):
    _agent_apply(world, agents, 'competition_score', 'last_interaction', 'sqrt')

def logic_19221(agents, world):
    _agent_apply(world, agents, 'defection_score', 'last_interaction', 'sqrt')

def logic_19222(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'last_interaction', 'sqrt')

def logic_19223(agents, world):
    _agent_apply(world, agents, 'risk_score', 'last_interaction', 'sqrt')

def logic_19224(agents, world):
    _agent_apply(world, agents, 'safety_score', 'risk_tolerance', 'sqrt')

def logic_19225(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'risk_tolerance', 'sqrt')

def logic_19226(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'risk_tolerance', 'sqrt')

def logic_19227(agents, world):
    _agent_apply(world, agents, 'survival_score', 'risk_tolerance', 'sqrt')

def logic_19228(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'risk_tolerance', 'sqrt')

def logic_19229(agents, world):
    _agent_apply(world, agents, 'help_score', 'risk_tolerance', 'sqrt')

def logic_19230(agents, world):
    _agent_apply(world, agents, 'attack_success', 'risk_tolerance', 'sqrt')

def logic_19231(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'risk_tolerance', 'sqrt')

def logic_19232(agents, world):
    _agent_apply(world, agents, 'defense_score', 'risk_tolerance', 'sqrt')

def logic_19233(agents, world):
    _agent_apply(world, agents, 'migration_score', 'risk_tolerance', 'sqrt')

def logic_19234(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'risk_tolerance', 'sqrt')

def logic_19235(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'risk_tolerance', 'sqrt')

def logic_19236(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'risk_tolerance', 'sqrt')

def logic_19237(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'risk_tolerance', 'sqrt')

def logic_19238(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'risk_tolerance', 'sqrt')

def logic_19239(agents, world):
    _agent_apply(world, agents, 'memory_update', 'risk_tolerance', 'sqrt')

def logic_19240(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'risk_tolerance', 'sqrt')

def logic_19241(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'risk_tolerance', 'sqrt')

def logic_19242(agents, world):
    _agent_apply(world, agents, 'payoff', 'risk_tolerance', 'sqrt')

def logic_19243(agents, world):
    _agent_apply(world, agents, 'temperature', 'last_action', 'sqrt')

def logic_19244(agents, world):
    _agent_apply(world, agents, 'surface_water', 'last_action', 'sqrt')

def logic_19245(agents, world):
    _agent_apply(world, agents, 'humidity', 'last_action', 'sqrt')

def logic_19246(agents, world):
    _agent_apply(world, agents, 'cloud', 'last_action', 'sqrt')

def logic_19247(agents, world):
    _agent_apply(world, agents, 'rain', 'last_action', 'pulse')

def logic_19248(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'last_action', 'pulse')

def logic_19249(agents, world):
    _agent_apply(world, agents, 'runoff', 'last_action', 'pulse')

def logic_19250(agents, world):
    _agent_apply(world, agents, 'wind_x', 'last_action', 'pulse')

def logic_19251(agents, world):
    _agent_apply(world, agents, 'wind_y', 'last_action', 'pulse')

def logic_19252(agents, world):
    _agent_apply(world, agents, 'vegetation', 'last_action', 'pulse')

def logic_19253(agents, world):
    _agent_apply(world, agents, 'biomass', 'last_action', 'pulse')

def logic_19254(agents, world):
    _agent_apply(world, agents, 'herbivore', 'last_action', 'pulse')

def logic_19255(agents, world):
    _agent_apply(world, agents, 'predator', 'last_action', 'pulse')

def logic_19256(agents, world):
    _agent_apply(world, agents, 'carrion', 'last_action', 'pulse')

def logic_19257(agents, world):
    _agent_apply(world, agents, 'nutrients', 'last_action', 'pulse')

def logic_19258(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'last_action', 'pulse')

def logic_19259(agents, world):
    _agent_apply(world, agents, 'oxygen', 'last_action', 'pulse')

def logic_19260(agents, world):
    _agent_apply(world, agents, 'co2', 'last_action', 'pulse')

def logic_19261(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'last_action', 'pulse')

def logic_19262(agents, world):
    _agent_apply(world, agents, 'ice', 'last_action', 'pulse')

def logic_19263(agents, world):
    _agent_apply(world, agents, 'evaporation', 'strategy_score', 'pulse')

def logic_19264(agents, world):
    _agent_apply(world, agents, 'detritus', 'strategy_score', 'pulse')

def logic_19265(agents, world):
    _agent_apply(world, agents, 'methane', 'strategy_score', 'pulse')

def logic_19266(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'strategy_score', 'pulse')

def logic_19267(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'strategy_score', 'pulse')

def logic_19268(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'strategy_score', 'pulse')

def logic_19269(agents, world):
    _agent_apply(world, agents, 'erosion', 'strategy_score', 'pulse')

def logic_19270(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'strategy_score', 'pulse')

def logic_19271(agents, world):
    _agent_apply(world, agents, 'root_density', 'strategy_score', 'pulse')

def logic_19272(agents, world):
    _agent_apply(world, agents, 'wetland', 'strategy_score', 'pulse')

def logic_19273(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'strategy_score', 'pulse')

def logic_19274(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'strategy_score', 'pulse')

def logic_19275(agents, world):
    _agent_apply(world, agents, 'ash', 'strategy_score', 'pulse')

def logic_19276(agents, world):
    _agent_apply(world, agents, 'snowpack', 'strategy_score', 'pulse')

def logic_19277(agents, world):
    _agent_apply(world, agents, 'groundwater', 'strategy_score', 'pulse')

def logic_19278(agents, world):
    _agent_apply(world, agents, 'sediment', 'strategy_score', 'pulse')

def logic_19279(agents, world):
    _agent_apply(world, agents, 'salinity', 'strategy_score', 'pulse')

def logic_19280(agents, world):
    _agent_apply(world, agents, 'algae', 'strategy_score', 'pulse')

def logic_19281(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'strategy_score', 'pulse')

def logic_19282(agents, world):
    _agent_apply(world, agents, 'deadwood', 'strategy_score', 'pulse')

def logic_19283(agents, world):
    _agent_apply(world, agents, 'pollinators', 'cooperation_score', 'pulse')

def logic_19284(agents, world):
    _agent_apply(world, agents, 'flowers', 'cooperation_score', 'pulse')

def logic_19285(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'cooperation_score', 'pulse')

def logic_19286(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'cooperation_score', 'pulse')

def logic_19287(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'cooperation_score', 'pulse')

def logic_19288(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'cooperation_score', 'pulse')

def logic_19289(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'cooperation_score', 'pulse')

def logic_19290(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'cooperation_score', 'pulse')

def logic_19291(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'cooperation_score', 'pulse')

def logic_19292(agents, world):
    _agent_apply(world, agents, 'hydration', 'cooperation_score', 'pulse')

def logic_19293(agents, world):
    _agent_apply(world, agents, 'thirst', 'cooperation_score', 'pulse')

def logic_19294(agents, world):
    _agent_apply(world, agents, 'hunger', 'cooperation_score', 'pulse')

def logic_19295(agents, world):
    _agent_apply(world, agents, 'health', 'cooperation_score', 'pulse')

def logic_19296(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'cooperation_score', 'pulse')

def logic_19297(agents, world):
    _agent_apply(world, agents, 'dehydration', 'cooperation_score', 'pulse')

def logic_19298(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'cooperation_score', 'pulse')

def logic_19299(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'cooperation_score', 'pulse')

def logic_19300(agents, world):
    _agent_apply(world, agents, 'alertness', 'cooperation_score', 'pulse')

def logic_19301(agents, world):
    _agent_apply(world, agents, 'fear', 'cooperation_score', 'pulse')

def logic_19302(agents, world):
    _agent_apply(world, agents, 'recovery', 'cooperation_score', 'pulse')

def logic_19303(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'competition_score', 'pulse')

def logic_19304(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'competition_score', 'pulse')

def logic_19305(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'competition_score', 'pulse')

def logic_19306(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'competition_score', 'pulse')

def logic_19307(agents, world):
    _agent_apply(world, agents, 'food_access', 'competition_score', 'pulse')

def logic_19308(agents, world):
    _agent_apply(world, agents, 'wealth', 'competition_score', 'pulse')

def logic_19309(agents, world):
    _agent_apply(world, agents, 'stability', 'competition_score', 'pulse')

def logic_19310(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'competition_score', 'pulse')

def logic_19311(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'competition_score', 'pulse')

def logic_19312(agents, world):
    _agent_apply(world, agents, 'reputation', 'competition_score', 'pulse')

def logic_19313(agents, world):
    _agent_apply(world, agents, 'trust', 'competition_score', 'pulse')

def logic_19314(agents, world):
    _agent_apply(world, agents, 'cooperation', 'competition_score', 'pulse')

def logic_19315(agents, world):
    _agent_apply(world, agents, 'defection', 'competition_score', 'pulse')

def logic_19316(agents, world):
    _agent_apply(world, agents, 'aggression', 'competition_score', 'pulse')

def logic_19317(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'competition_score', 'pulse')

def logic_19318(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'competition_score', 'pulse')

def logic_19319(agents, world):
    _agent_apply(world, agents, 'territoriality', 'competition_score', 'pulse')

def logic_19320(agents, world):
    _agent_apply(world, agents, 'group_stability', 'competition_score', 'pulse')

def logic_19321(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'competition_score', 'pulse')

def logic_19322(agents, world):
    _agent_apply(world, agents, 'help_drive', 'defection_score', 'pulse')

def logic_19323(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'defection_score', 'pulse')

def logic_19324(agents, world):
    _agent_apply(world, agents, 'selfishness', 'defection_score', 'pulse')

def logic_19325(agents, world):
    _agent_apply(world, agents, 'generosity', 'defection_score', 'pulse')

def logic_19326(agents, world):
    _agent_apply(world, agents, 'gratitude', 'defection_score', 'pulse')

def logic_19327(agents, world):
    _agent_apply(world, agents, 'caution', 'defection_score', 'pulse')

def logic_19328(agents, world):
    _agent_apply(world, agents, 'confidence', 'defection_score', 'pulse')

def logic_19329(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'defection_score', 'pulse')

def logic_19330(agents, world):
    _agent_apply(world, agents, 'future_help', 'defection_score', 'pulse')

def logic_19331(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'defection_score', 'pulse')

def logic_19332(agents, world):
    _agent_apply(world, agents, 'empathy', 'defection_score', 'pulse')

def logic_19333(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'defection_score', 'pulse')

def logic_19334(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'defection_score', 'pulse')

def logic_19335(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'defection_score', 'pulse')

def logic_19336(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'defection_score', 'threshold')

def logic_19337(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'defection_score', 'threshold')

def logic_19338(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'defection_score', 'threshold')

def logic_19339(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'defection_score', 'threshold')

def logic_19340(agents, world):
    _agent_apply(world, agents, 'stress', 'defection_score', 'threshold')

def logic_19341(agents, world):
    _agent_apply(world, agents, 'social_need', 'defection_score', 'threshold')

def logic_19342(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'reciprocity_score', 'threshold')

def logic_19343(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'reciprocity_score', 'threshold')

def logic_19344(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'reciprocity_score', 'threshold')

def logic_19345(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'reciprocity_score', 'threshold')

def logic_19346(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'reciprocity_score', 'threshold')

def logic_19347(agents, world):
    _agent_apply(world, agents, 'help_received', 'reciprocity_score', 'threshold')

def logic_19348(agents, world):
    _agent_apply(world, agents, 'help_given', 'reciprocity_score', 'threshold')

def logic_19349(agents, world):
    _agent_apply(world, agents, 'local_density', 'reciprocity_score', 'threshold')

def logic_19350(agents, world):
    _agent_apply(world, agents, 'last_reward', 'reciprocity_score', 'threshold')

def logic_19351(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'reciprocity_score', 'threshold')

def logic_19352(agents, world):
    _agent_apply(world, agents, 'last_food', 'reciprocity_score', 'threshold')

def logic_19353(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'reciprocity_score', 'threshold')

def logic_19354(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'reciprocity_score', 'threshold')

def logic_19355(agents, world):
    _agent_apply(world, agents, 'last_action', 'reciprocity_score', 'threshold')

def logic_19356(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'reciprocity_score', 'threshold')

def logic_19357(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'reciprocity_score', 'threshold')

def logic_19358(agents, world):
    _agent_apply(world, agents, 'competition_score', 'reciprocity_score', 'threshold')

def logic_19359(agents, world):
    _agent_apply(world, agents, 'defection_score', 'reciprocity_score', 'threshold')

def logic_19360(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'risk_score', 'threshold')

def logic_19361(agents, world):
    _agent_apply(world, agents, 'risk_score', 'reciprocity_score', 'threshold')

def logic_19362(agents, world):
    _agent_apply(world, agents, 'safety_score', 'risk_score', 'threshold')

def logic_19363(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'risk_score', 'threshold')

def logic_19364(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'risk_score', 'threshold')

def logic_19365(agents, world):
    _agent_apply(world, agents, 'survival_score', 'risk_score', 'threshold')

def logic_19366(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'risk_score', 'threshold')

def logic_19367(agents, world):
    _agent_apply(world, agents, 'help_score', 'risk_score', 'threshold')

def logic_19368(agents, world):
    _agent_apply(world, agents, 'attack_success', 'risk_score', 'threshold')

def logic_19369(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'risk_score', 'threshold')

def logic_19370(agents, world):
    _agent_apply(world, agents, 'defense_score', 'risk_score', 'threshold')

def logic_19371(agents, world):
    _agent_apply(world, agents, 'migration_score', 'risk_score', 'threshold')

def logic_19372(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'risk_score', 'threshold')

def logic_19373(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'risk_score', 'threshold')

def logic_19374(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'risk_score', 'threshold')

def logic_19375(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'risk_score', 'threshold')

def logic_19376(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'risk_score', 'threshold')

def logic_19377(agents, world):
    _agent_apply(world, agents, 'memory_update', 'risk_score', 'threshold')

def logic_19378(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'risk_score', 'threshold')

def logic_19379(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'risk_score', 'threshold')

def logic_19380(agents, world):
    _agent_apply(world, agents, 'payoff', 'risk_score', 'threshold')

def logic_19381(agents, world):
    _agent_apply(world, agents, 'temperature', 'safety_score', 'threshold')

def logic_19382(agents, world):
    _agent_apply(world, agents, 'surface_water', 'safety_score', 'threshold')

def logic_19383(agents, world):
    _agent_apply(world, agents, 'humidity', 'safety_score', 'threshold')

def logic_19384(agents, world):
    _agent_apply(world, agents, 'cloud', 'safety_score', 'threshold')

def logic_19385(agents, world):
    _agent_apply(world, agents, 'rain', 'safety_score', 'threshold')

def logic_19386(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'safety_score', 'threshold')

def logic_19387(agents, world):
    _agent_apply(world, agents, 'runoff', 'safety_score', 'threshold')

def logic_19388(agents, world):
    _agent_apply(world, agents, 'wind_x', 'safety_score', 'threshold')

def logic_19389(agents, world):
    _agent_apply(world, agents, 'wind_y', 'safety_score', 'threshold')

def logic_19390(agents, world):
    _agent_apply(world, agents, 'vegetation', 'safety_score', 'threshold')

def logic_19391(agents, world):
    _agent_apply(world, agents, 'biomass', 'safety_score', 'threshold')

def logic_19392(agents, world):
    _agent_apply(world, agents, 'herbivore', 'safety_score', 'threshold')

def logic_19393(agents, world):
    _agent_apply(world, agents, 'predator', 'safety_score', 'threshold')

def logic_19394(agents, world):
    _agent_apply(world, agents, 'carrion', 'safety_score', 'threshold')

def logic_19395(agents, world):
    _agent_apply(world, agents, 'nutrients', 'safety_score', 'threshold')

def logic_19396(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'safety_score', 'threshold')

def logic_19397(agents, world):
    _agent_apply(world, agents, 'oxygen', 'safety_score', 'threshold')

def logic_19398(agents, world):
    _agent_apply(world, agents, 'co2', 'safety_score', 'threshold')

def logic_19399(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'safety_score', 'threshold')

def logic_19400(agents, world):
    _agent_apply(world, agents, 'ice', 'safety_score', 'threshold')

def logic_19401(agents, world):
    _agent_apply(world, agents, 'evaporation', 'exploration_score', 'threshold')

def logic_19402(agents, world):
    _agent_apply(world, agents, 'detritus', 'exploration_score', 'threshold')

def logic_19403(agents, world):
    _agent_apply(world, agents, 'methane', 'exploration_score', 'threshold')

def logic_19404(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'exploration_score', 'threshold')

def logic_19405(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'exploration_score', 'threshold')

def logic_19406(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'exploration_score', 'threshold')

def logic_19407(agents, world):
    _agent_apply(world, agents, 'erosion', 'exploration_score', 'threshold')

def logic_19408(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'exploration_score', 'threshold')

def logic_19409(agents, world):
    _agent_apply(world, agents, 'root_density', 'exploration_score', 'threshold')

def logic_19410(agents, world):
    _agent_apply(world, agents, 'wetland', 'exploration_score', 'threshold')

def logic_19411(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'exploration_score', 'threshold')

def logic_19412(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'exploration_score', 'threshold')

def logic_19413(agents, world):
    _agent_apply(world, agents, 'ash', 'exploration_score', 'threshold')

def logic_19414(agents, world):
    _agent_apply(world, agents, 'snowpack', 'exploration_score', 'threshold')

def logic_19415(agents, world):
    _agent_apply(world, agents, 'groundwater', 'exploration_score', 'threshold')

def logic_19416(agents, world):
    _agent_apply(world, agents, 'sediment', 'exploration_score', 'threshold')

def logic_19417(agents, world):
    _agent_apply(world, agents, 'salinity', 'exploration_score', 'threshold')

def logic_19418(agents, world):
    _agent_apply(world, agents, 'algae', 'exploration_score', 'threshold')

def logic_19419(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'exploration_score', 'threshold')

def logic_19420(agents, world):
    _agent_apply(world, agents, 'deadwood', 'exploration_score', 'threshold')

def logic_19421(agents, world):
    _agent_apply(world, agents, 'pollinators', 'foraging_score', 'threshold')

def logic_19422(agents, world):
    _agent_apply(world, agents, 'flowers', 'foraging_score', 'threshold')

def logic_19423(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'foraging_score', 'threshold')

def logic_19424(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'foraging_score', 'threshold')

def logic_19425(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'foraging_score', 'saturation')

def logic_19426(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'foraging_score', 'saturation')

def logic_19427(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'foraging_score', 'saturation')

def logic_19428(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'foraging_score', 'saturation')

def logic_19429(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'foraging_score', 'saturation')

def logic_19430(agents, world):
    _agent_apply(world, agents, 'hydration', 'foraging_score', 'saturation')

def logic_19431(agents, world):
    _agent_apply(world, agents, 'thirst', 'foraging_score', 'saturation')

def logic_19432(agents, world):
    _agent_apply(world, agents, 'hunger', 'foraging_score', 'saturation')

def logic_19433(agents, world):
    _agent_apply(world, agents, 'health', 'foraging_score', 'saturation')

def logic_19434(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'foraging_score', 'saturation')

def logic_19435(agents, world):
    _agent_apply(world, agents, 'dehydration', 'foraging_score', 'saturation')

def logic_19436(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'foraging_score', 'saturation')

def logic_19437(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'foraging_score', 'saturation')

def logic_19438(agents, world):
    _agent_apply(world, agents, 'alertness', 'foraging_score', 'saturation')

def logic_19439(agents, world):
    _agent_apply(world, agents, 'fear', 'foraging_score', 'saturation')

def logic_19440(agents, world):
    _agent_apply(world, agents, 'recovery', 'foraging_score', 'saturation')

def logic_19441(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'survival_score', 'saturation')

def logic_19442(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'survival_score', 'saturation')

def logic_19443(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'survival_score', 'saturation')

def logic_19444(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'survival_score', 'saturation')

def logic_19445(agents, world):
    _agent_apply(world, agents, 'food_access', 'survival_score', 'saturation')

def logic_19446(agents, world):
    _agent_apply(world, agents, 'wealth', 'survival_score', 'saturation')

def logic_19447(agents, world):
    _agent_apply(world, agents, 'stability', 'survival_score', 'saturation')

def logic_19448(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'survival_score', 'saturation')

def logic_19449(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'survival_score', 'saturation')

def logic_19450(agents, world):
    _agent_apply(world, agents, 'reputation', 'survival_score', 'saturation')

def logic_19451(agents, world):
    _agent_apply(world, agents, 'trust', 'survival_score', 'saturation')

def logic_19452(agents, world):
    _agent_apply(world, agents, 'cooperation', 'survival_score', 'saturation')

def logic_19453(agents, world):
    _agent_apply(world, agents, 'defection', 'survival_score', 'saturation')

def logic_19454(agents, world):
    _agent_apply(world, agents, 'aggression', 'survival_score', 'saturation')

def logic_19455(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'survival_score', 'saturation')

def logic_19456(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'survival_score', 'saturation')

def logic_19457(agents, world):
    _agent_apply(world, agents, 'territoriality', 'survival_score', 'saturation')

def logic_19458(agents, world):
    _agent_apply(world, agents, 'group_stability', 'survival_score', 'saturation')

def logic_19459(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'survival_score', 'saturation')

def logic_19460(agents, world):
    _agent_apply(world, agents, 'help_drive', 'fitness_score', 'saturation')

def logic_19461(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'fitness_score', 'saturation')

def logic_19462(agents, world):
    _agent_apply(world, agents, 'selfishness', 'fitness_score', 'saturation')

def logic_19463(agents, world):
    _agent_apply(world, agents, 'generosity', 'fitness_score', 'saturation')

def logic_19464(agents, world):
    _agent_apply(world, agents, 'gratitude', 'fitness_score', 'saturation')

def logic_19465(agents, world):
    _agent_apply(world, agents, 'caution', 'fitness_score', 'saturation')

def logic_19466(agents, world):
    _agent_apply(world, agents, 'confidence', 'fitness_score', 'saturation')

def logic_19467(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'fitness_score', 'saturation')

def logic_19468(agents, world):
    _agent_apply(world, agents, 'future_help', 'fitness_score', 'saturation')

def logic_19469(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'fitness_score', 'saturation')

def logic_19470(agents, world):
    _agent_apply(world, agents, 'empathy', 'fitness_score', 'saturation')

def logic_19471(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'fitness_score', 'saturation')

def logic_19472(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'fitness_score', 'saturation')

def logic_19473(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'fitness_score', 'saturation')

def logic_19474(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'fitness_score', 'saturation')

def logic_19475(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'fitness_score', 'saturation')

def logic_19476(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'fitness_score', 'saturation')

def logic_19477(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'fitness_score', 'saturation')

def logic_19478(agents, world):
    _agent_apply(world, agents, 'stress', 'fitness_score', 'saturation')

def logic_19479(agents, world):
    _agent_apply(world, agents, 'social_need', 'fitness_score', 'saturation')

def logic_19480(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'help_score', 'saturation')

def logic_19481(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'help_score', 'saturation')

def logic_19482(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'help_score', 'saturation')

def logic_19483(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'help_score', 'saturation')

def logic_19484(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'help_score', 'saturation')

def logic_19485(agents, world):
    _agent_apply(world, agents, 'help_received', 'help_score', 'saturation')

def logic_19486(agents, world):
    _agent_apply(world, agents, 'help_given', 'help_score', 'saturation')

def logic_19487(agents, world):
    _agent_apply(world, agents, 'local_density', 'help_score', 'saturation')

def logic_19488(agents, world):
    _agent_apply(world, agents, 'last_reward', 'help_score', 'saturation')

def logic_19489(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'help_score', 'saturation')

def logic_19490(agents, world):
    _agent_apply(world, agents, 'last_food', 'help_score', 'saturation')

def logic_19491(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'help_score', 'saturation')

def logic_19492(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'help_score', 'saturation')

def logic_19493(agents, world):
    _agent_apply(world, agents, 'last_action', 'help_score', 'saturation')

def logic_19494(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'help_score', 'saturation')

def logic_19495(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'help_score', 'saturation')

def logic_19496(agents, world):
    _agent_apply(world, agents, 'competition_score', 'help_score', 'saturation')

def logic_19497(agents, world):
    _agent_apply(world, agents, 'defection_score', 'help_score', 'saturation')

def logic_19498(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'help_score', 'saturation')

def logic_19499(agents, world):
    _agent_apply(world, agents, 'risk_score', 'help_score', 'saturation')

def logic_19500(agents, world):
    _agent_apply(world, agents, 'safety_score', 'attack_success', 'saturation')

def logic_19501(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'attack_success', 'saturation')

def logic_19502(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'attack_success', 'saturation')

def logic_19503(agents, world):
    _agent_apply(world, agents, 'survival_score', 'attack_success', 'saturation')

def logic_19504(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'attack_success', 'saturation')

def logic_19505(agents, world):
    _agent_apply(world, agents, 'help_score', 'attack_success', 'saturation')

def logic_19506(agents, world):
    _agent_apply(world, agents, 'attack_success', 'retaliation_risk', 'saturation')

def logic_19507(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'attack_success', 'saturation')

def logic_19508(agents, world):
    _agent_apply(world, agents, 'defense_score', 'attack_success', 'saturation')

def logic_19509(agents, world):
    _agent_apply(world, agents, 'migration_score', 'attack_success', 'saturation')

def logic_19510(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'attack_success', 'saturation')

def logic_19511(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'attack_success', 'saturation')

def logic_19512(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'attack_success', 'saturation')

def logic_19513(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'attack_success', 'saturation')

def logic_19514(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'attack_success', 'reciprocal')

def logic_19515(agents, world):
    _agent_apply(world, agents, 'memory_update', 'attack_success', 'reciprocal')

def logic_19516(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'attack_success', 'reciprocal')

def logic_19517(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'attack_success', 'reciprocal')

def logic_19518(agents, world):
    _agent_apply(world, agents, 'payoff', 'attack_success', 'reciprocal')

def logic_19519(agents, world):
    _agent_apply(world, agents, 'temperature', 'retaliation_risk', 'reciprocal')

def logic_19520(agents, world):
    _agent_apply(world, agents, 'surface_water', 'retaliation_risk', 'reciprocal')

def logic_19521(agents, world):
    _agent_apply(world, agents, 'humidity', 'retaliation_risk', 'reciprocal')

def logic_19522(agents, world):
    _agent_apply(world, agents, 'cloud', 'retaliation_risk', 'reciprocal')

def logic_19523(agents, world):
    _agent_apply(world, agents, 'rain', 'retaliation_risk', 'reciprocal')

def logic_19524(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'retaliation_risk', 'reciprocal')

def logic_19525(agents, world):
    _agent_apply(world, agents, 'runoff', 'retaliation_risk', 'reciprocal')

def logic_19526(agents, world):
    _agent_apply(world, agents, 'wind_x', 'retaliation_risk', 'reciprocal')

def logic_19527(agents, world):
    _agent_apply(world, agents, 'wind_y', 'retaliation_risk', 'reciprocal')

def logic_19528(agents, world):
    _agent_apply(world, agents, 'vegetation', 'retaliation_risk', 'reciprocal')

def logic_19529(agents, world):
    _agent_apply(world, agents, 'biomass', 'retaliation_risk', 'reciprocal')

def logic_19530(agents, world):
    _agent_apply(world, agents, 'herbivore', 'retaliation_risk', 'reciprocal')

def logic_19531(agents, world):
    _agent_apply(world, agents, 'predator', 'retaliation_risk', 'reciprocal')

def logic_19532(agents, world):
    _agent_apply(world, agents, 'carrion', 'retaliation_risk', 'reciprocal')

def logic_19533(agents, world):
    _agent_apply(world, agents, 'nutrients', 'retaliation_risk', 'reciprocal')

def logic_19534(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'retaliation_risk', 'reciprocal')

def logic_19535(agents, world):
    _agent_apply(world, agents, 'oxygen', 'retaliation_risk', 'reciprocal')

def logic_19536(agents, world):
    _agent_apply(world, agents, 'co2', 'retaliation_risk', 'reciprocal')

def logic_19537(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'retaliation_risk', 'reciprocal')

def logic_19538(agents, world):
    _agent_apply(world, agents, 'ice', 'retaliation_risk', 'reciprocal')

def logic_19539(agents, world):
    _agent_apply(world, agents, 'evaporation', 'defense_score', 'reciprocal')

def logic_19540(agents, world):
    _agent_apply(world, agents, 'detritus', 'defense_score', 'reciprocal')

def logic_19541(agents, world):
    _agent_apply(world, agents, 'methane', 'defense_score', 'reciprocal')

def logic_19542(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'defense_score', 'reciprocal')

def logic_19543(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'defense_score', 'reciprocal')

def logic_19544(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'defense_score', 'reciprocal')

def logic_19545(agents, world):
    _agent_apply(world, agents, 'erosion', 'defense_score', 'reciprocal')

def logic_19546(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'defense_score', 'reciprocal')

def logic_19547(agents, world):
    _agent_apply(world, agents, 'root_density', 'defense_score', 'reciprocal')

def logic_19548(agents, world):
    _agent_apply(world, agents, 'wetland', 'defense_score', 'reciprocal')

def logic_19549(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'defense_score', 'reciprocal')

def logic_19550(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'defense_score', 'reciprocal')

def logic_19551(agents, world):
    _agent_apply(world, agents, 'ash', 'defense_score', 'reciprocal')

def logic_19552(agents, world):
    _agent_apply(world, agents, 'snowpack', 'defense_score', 'reciprocal')

def logic_19553(agents, world):
    _agent_apply(world, agents, 'groundwater', 'defense_score', 'reciprocal')

def logic_19554(agents, world):
    _agent_apply(world, agents, 'sediment', 'defense_score', 'reciprocal')

def logic_19555(agents, world):
    _agent_apply(world, agents, 'salinity', 'defense_score', 'reciprocal')

def logic_19556(agents, world):
    _agent_apply(world, agents, 'algae', 'defense_score', 'reciprocal')

def logic_19557(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'defense_score', 'reciprocal')

def logic_19558(agents, world):
    _agent_apply(world, agents, 'deadwood', 'defense_score', 'reciprocal')

def logic_19559(agents, world):
    _agent_apply(world, agents, 'pollinators', 'migration_score', 'reciprocal')

def logic_19560(agents, world):
    _agent_apply(world, agents, 'flowers', 'migration_score', 'reciprocal')

def logic_19561(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'migration_score', 'reciprocal')

def logic_19562(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'migration_score', 'reciprocal')

def logic_19563(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'migration_score', 'reciprocal')

def logic_19564(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'migration_score', 'reciprocal')

def logic_19565(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'migration_score', 'reciprocal')

def logic_19566(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'migration_score', 'reciprocal')

def logic_19567(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'migration_score', 'reciprocal')

def logic_19568(agents, world):
    _agent_apply(world, agents, 'hydration', 'migration_score', 'reciprocal')

def logic_19569(agents, world):
    _agent_apply(world, agents, 'thirst', 'migration_score', 'reciprocal')

def logic_19570(agents, world):
    _agent_apply(world, agents, 'hunger', 'migration_score', 'reciprocal')

def logic_19571(agents, world):
    _agent_apply(world, agents, 'health', 'migration_score', 'reciprocal')

def logic_19572(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'migration_score', 'reciprocal')

def logic_19573(agents, world):
    _agent_apply(world, agents, 'dehydration', 'migration_score', 'reciprocal')

def logic_19574(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'migration_score', 'reciprocal')

def logic_19575(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'migration_score', 'reciprocal')

def logic_19576(agents, world):
    _agent_apply(world, agents, 'alertness', 'migration_score', 'reciprocal')

def logic_19577(agents, world):
    _agent_apply(world, agents, 'fear', 'migration_score', 'reciprocal')

def logic_19578(agents, world):
    _agent_apply(world, agents, 'recovery', 'migration_score', 'reciprocal')

def logic_19579(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'reproduction_score', 'reciprocal')

def logic_19580(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'reproduction_score', 'reciprocal')

def logic_19581(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'reproduction_score', 'reciprocal')

def logic_19582(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'reproduction_score', 'reciprocal')

def logic_19583(agents, world):
    _agent_apply(world, agents, 'food_access', 'reproduction_score', 'reciprocal')

def logic_19584(agents, world):
    _agent_apply(world, agents, 'wealth', 'reproduction_score', 'reciprocal')

def logic_19585(agents, world):
    _agent_apply(world, agents, 'stability', 'reproduction_score', 'reciprocal')

def logic_19586(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'reproduction_score', 'reciprocal')

def logic_19587(agents, world):
    _agent_apply(world, agents, 'social_tolerance', 'reproduction_score', 'reciprocal')

def logic_19588(agents, world):
    _agent_apply(world, agents, 'reputation', 'reproduction_score', 'reciprocal')

def logic_19589(agents, world):
    _agent_apply(world, agents, 'trust', 'reproduction_score', 'reciprocal')

def logic_19590(agents, world):
    _agent_apply(world, agents, 'cooperation', 'reproduction_score', 'reciprocal')

def logic_19591(agents, world):
    _agent_apply(world, agents, 'defection', 'reproduction_score', 'reciprocal')

def logic_19592(agents, world):
    _agent_apply(world, agents, 'aggression', 'reproduction_score', 'reciprocal')

def logic_19593(agents, world):
    _agent_apply(world, agents, 'conflict_pressure', 'reproduction_score', 'reciprocal')

def logic_19594(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'reproduction_score', 'reciprocal')

def logic_19595(agents, world):
    _agent_apply(world, agents, 'territoriality', 'reproduction_score', 'reciprocal')

def logic_19596(agents, world):
    _agent_apply(world, agents, 'group_stability', 'reproduction_score', 'reciprocal')

def logic_19597(agents, world):
    _agent_apply(world, agents, 'sharing_capacity', 'reproduction_score', 'reciprocal')

def logic_19598(agents, world):
    _agent_apply(world, agents, 'help_drive', 'sharing_score', 'reciprocal')

def logic_19599(agents, world):
    _agent_apply(world, agents, 'social_avoidance', 'sharing_score', 'reciprocal')

def logic_19600(agents, world):
    _agent_apply(world, agents, 'selfishness', 'sharing_score', 'reciprocal')

def logic_19601(agents, world):
    _agent_apply(world, agents, 'generosity', 'sharing_score', 'reciprocal')

def logic_19602(agents, world):
    _agent_apply(world, agents, 'gratitude', 'sharing_score', 'reciprocal')

def logic_19603(agents, world):
    _agent_apply(world, agents, 'caution', 'sharing_score', 'gap')

def logic_19604(agents, world):
    _agent_apply(world, agents, 'confidence', 'sharing_score', 'gap')

def logic_19605(agents, world):
    _agent_apply(world, agents, 'strategy_confidence', 'sharing_score', 'gap')

def logic_19606(agents, world):
    _agent_apply(world, agents, 'future_help', 'sharing_score', 'gap')

def logic_19607(agents, world):
    _agent_apply(world, agents, 'resource_discovery', 'sharing_score', 'gap')

def logic_19608(agents, world):
    _agent_apply(world, agents, 'empathy', 'sharing_score', 'gap')

def logic_19609(agents, world):
    _agent_apply(world, agents, 'attack_threshold', 'sharing_score', 'gap')

def logic_19610(agents, world):
    _agent_apply(world, agents, 'defection_threshold', 'sharing_score', 'gap')

def logic_19611(agents, world):
    _agent_apply(world, agents, 'oxygen_need', 'sharing_score', 'gap')

def logic_19612(agents, world):
    _agent_apply(world, agents, 'shelter_need', 'sharing_score', 'gap')

def logic_19613(agents, world):
    _agent_apply(world, agents, 'fire_fear', 'sharing_score', 'gap')

def logic_19614(agents, world):
    _agent_apply(world, agents, 'resource_competition', 'sharing_score', 'gap')

def logic_19615(agents, world):
    _agent_apply(world, agents, 'vegetation_expectation', 'sharing_score', 'gap')

def logic_19616(agents, world):
    _agent_apply(world, agents, 'stress', 'sharing_score', 'gap')

def logic_19617(agents, world):
    _agent_apply(world, agents, 'social_need', 'sharing_score', 'gap')

def logic_19618(agents, world):
    _agent_apply(world, agents, 'neighbor_energy_gap', 'strategy_persistence', 'gap')

def logic_19619(agents, world):
    _agent_apply(world, agents, 'neighbor_health_gap', 'strategy_persistence', 'gap')

def logic_19620(agents, world):
    _agent_apply(world, agents, 'betrayal_memory', 'strategy_persistence', 'gap')

def logic_19621(agents, world):
    _agent_apply(world, agents, 'conflict_history', 'strategy_persistence', 'gap')

def logic_19622(agents, world):
    _agent_apply(world, agents, 'cooperation_history', 'strategy_persistence', 'gap')

def logic_19623(agents, world):
    _agent_apply(world, agents, 'help_received', 'strategy_persistence', 'gap')

def logic_19624(agents, world):
    _agent_apply(world, agents, 'help_given', 'strategy_persistence', 'gap')

def logic_19625(agents, world):
    _agent_apply(world, agents, 'local_density', 'strategy_persistence', 'gap')

def logic_19626(agents, world):
    _agent_apply(world, agents, 'last_reward', 'strategy_persistence', 'gap')

def logic_19627(agents, world):
    _agent_apply(world, agents, 'last_energy_delta', 'strategy_persistence', 'gap')

def logic_19628(agents, world):
    _agent_apply(world, agents, 'last_food', 'strategy_persistence', 'gap')

def logic_19629(agents, world):
    _agent_apply(world, agents, 'last_interaction', 'strategy_persistence', 'gap')

def logic_19630(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'strategy_persistence', 'gap')

def logic_19631(agents, world):
    _agent_apply(world, agents, 'last_action', 'strategy_persistence', 'gap')

def logic_19632(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'strategy_persistence', 'gap')

def logic_19633(agents, world):
    _agent_apply(world, agents, 'cooperation_score', 'strategy_persistence', 'gap')

def logic_19634(agents, world):
    _agent_apply(world, agents, 'competition_score', 'strategy_persistence', 'gap')

def logic_19635(agents, world):
    _agent_apply(world, agents, 'defection_score', 'strategy_persistence', 'gap')

def logic_19636(agents, world):
    _agent_apply(world, agents, 'reciprocity_score', 'strategy_persistence', 'gap')

def logic_19637(agents, world):
    _agent_apply(world, agents, 'risk_score', 'strategy_persistence', 'gap')

def logic_19638(agents, world):
    _agent_apply(world, agents, 'safety_score', 'strategy_mixing', 'gap')

def logic_19639(agents, world):
    _agent_apply(world, agents, 'exploration_score', 'strategy_mixing', 'gap')

def logic_19640(agents, world):
    _agent_apply(world, agents, 'foraging_score', 'strategy_mixing', 'gap')

def logic_19641(agents, world):
    _agent_apply(world, agents, 'survival_score', 'strategy_mixing', 'gap')

def logic_19642(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'strategy_mixing', 'gap')

def logic_19643(agents, world):
    _agent_apply(world, agents, 'help_score', 'strategy_mixing', 'gap')

def logic_19644(agents, world):
    _agent_apply(world, agents, 'attack_success', 'strategy_mixing', 'gap')

def logic_19645(agents, world):
    _agent_apply(world, agents, 'retaliation_risk', 'strategy_mixing', 'gap')

def logic_19646(agents, world):
    _agent_apply(world, agents, 'defense_score', 'strategy_mixing', 'gap')

def logic_19647(agents, world):
    _agent_apply(world, agents, 'migration_score', 'strategy_mixing', 'gap')

def logic_19648(agents, world):
    _agent_apply(world, agents, 'reproduction_score', 'strategy_mixing', 'gap')

def logic_19649(agents, world):
    _agent_apply(world, agents, 'sharing_score', 'strategy_mixing', 'gap')

def logic_19650(agents, world):
    _agent_apply(world, agents, 'strategy_persistence', 'strategy_mixing', 'gap')

def logic_19651(agents, world):
    _agent_apply(world, agents, 'strategy_mixing', 'learning_rate', 'gap')

def logic_19652(agents, world):
    _agent_apply(world, agents, 'learning_rate', 'strategy_mixing', 'gap')

def logic_19653(agents, world):
    _agent_apply(world, agents, 'memory_update', 'strategy_mixing', 'gap')

def logic_19654(agents, world):
    _agent_apply(world, agents, 'future_payoff_weight', 'strategy_mixing', 'gap')

def logic_19655(agents, world):
    _agent_apply(world, agents, 'self_preservation', 'strategy_mixing', 'gap')

def logic_19656(agents, world):
    _agent_apply(world, agents, 'payoff', 'strategy_mixing', 'gap')

def logic_19657(agents, world):
    _agent_apply(world, agents, 'temperature', 'learning_rate', 'gap')

def logic_19658(agents, world):
    _agent_apply(world, agents, 'surface_water', 'learning_rate', 'gap')

def logic_19659(agents, world):
    _agent_apply(world, agents, 'humidity', 'learning_rate', 'gap')

def logic_19660(agents, world):
    _agent_apply(world, agents, 'cloud', 'learning_rate', 'gap')

def logic_19661(agents, world):
    _agent_apply(world, agents, 'rain', 'learning_rate', 'gap')

def logic_19662(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'learning_rate', 'gap')

def logic_19663(agents, world):
    _agent_apply(world, agents, 'runoff', 'learning_rate', 'gap')

def logic_19664(agents, world):
    _agent_apply(world, agents, 'wind_x', 'learning_rate', 'gap')

def logic_19665(agents, world):
    _agent_apply(world, agents, 'wind_y', 'learning_rate', 'gap')

def logic_19666(agents, world):
    _agent_apply(world, agents, 'vegetation', 'learning_rate', 'gap')

def logic_19667(agents, world):
    _agent_apply(world, agents, 'biomass', 'learning_rate', 'gap')

def logic_19668(agents, world):
    _agent_apply(world, agents, 'herbivore', 'learning_rate', 'gap')

def logic_19669(agents, world):
    _agent_apply(world, agents, 'predator', 'learning_rate', 'gap')

def logic_19670(agents, world):
    _agent_apply(world, agents, 'carrion', 'learning_rate', 'gap')

def logic_19671(agents, world):
    _agent_apply(world, agents, 'nutrients', 'learning_rate', 'gap')

def logic_19672(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'learning_rate', 'gap')

def logic_19673(agents, world):
    _agent_apply(world, agents, 'oxygen', 'learning_rate', 'gap')

def logic_19674(agents, world):
    _agent_apply(world, agents, 'co2', 'learning_rate', 'gap')

def logic_19675(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'learning_rate', 'gap')

def logic_19676(agents, world):
    _agent_apply(world, agents, 'ice', 'learning_rate', 'gap')

def logic_19677(agents, world):
    _agent_apply(world, agents, 'evaporation', 'memory_update', 'gap')

def logic_19678(agents, world):
    _agent_apply(world, agents, 'detritus', 'memory_update', 'gap')

def logic_19679(agents, world):
    _agent_apply(world, agents, 'methane', 'memory_update', 'gap')

def logic_19680(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'memory_update', 'gap')

def logic_19681(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'memory_update', 'gap')

def logic_19682(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'memory_update', 'gap')

def logic_19683(agents, world):
    _agent_apply(world, agents, 'erosion', 'memory_update', 'gap')

def logic_19684(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'memory_update', 'gap')

def logic_19685(agents, world):
    _agent_apply(world, agents, 'root_density', 'memory_update', 'gap')

def logic_19686(agents, world):
    _agent_apply(world, agents, 'wetland', 'memory_update', 'gap')

def logic_19687(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'memory_update', 'gap')

def logic_19688(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'memory_update', 'gap')

def logic_19689(agents, world):
    _agent_apply(world, agents, 'ash', 'memory_update', 'gap')

def logic_19690(agents, world):
    _agent_apply(world, agents, 'snowpack', 'memory_update', 'gap')

def logic_19691(agents, world):
    _agent_apply(world, agents, 'groundwater', 'memory_update', 'gap')

def logic_19692(agents, world):
    _agent_apply(world, agents, 'sediment', 'memory_update', 'feedback')

def logic_19693(agents, world):
    _agent_apply(world, agents, 'salinity', 'memory_update', 'feedback')

def logic_19694(agents, world):
    _agent_apply(world, agents, 'algae', 'memory_update', 'feedback')

def logic_19695(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'memory_update', 'feedback')

def logic_19696(agents, world):
    _agent_apply(world, agents, 'deadwood', 'memory_update', 'feedback')

def logic_19697(agents, world):
    _agent_apply(world, agents, 'pollinators', 'future_payoff_weight', 'feedback')

def logic_19698(agents, world):
    _agent_apply(world, agents, 'flowers', 'future_payoff_weight', 'feedback')

def logic_19699(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'future_payoff_weight', 'feedback')

def logic_19700(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'future_payoff_weight', 'feedback')

def logic_19701(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'future_payoff_weight', 'feedback')

def logic_19702(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'future_payoff_weight', 'feedback')

def logic_19703(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'future_payoff_weight', 'feedback')

def logic_19704(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'future_payoff_weight', 'feedback')

def logic_19705(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'future_payoff_weight', 'feedback')

def logic_19706(agents, world):
    _agent_apply(world, agents, 'hydration', 'future_payoff_weight', 'feedback')

def logic_19707(agents, world):
    _agent_apply(world, agents, 'thirst', 'future_payoff_weight', 'feedback')

def logic_19708(agents, world):
    _agent_apply(world, agents, 'hunger', 'future_payoff_weight', 'feedback')

def logic_19709(agents, world):
    _agent_apply(world, agents, 'health', 'future_payoff_weight', 'feedback')

def logic_19710(agents, world):
    _agent_apply(world, agents, 'thermal_stress', 'future_payoff_weight', 'feedback')

def logic_19711(agents, world):
    _agent_apply(world, agents, 'dehydration', 'future_payoff_weight', 'feedback')

def logic_19712(agents, world):
    _agent_apply(world, agents, 'pathogen_risk', 'future_payoff_weight', 'feedback')

def logic_19713(agents, world):
    _agent_apply(world, agents, 'infection_risk', 'future_payoff_weight', 'feedback')

def logic_19714(agents, world):
    _agent_apply(world, agents, 'alertness', 'future_payoff_weight', 'feedback')

def logic_19715(agents, world):
    _agent_apply(world, agents, 'fear', 'future_payoff_weight', 'feedback')

def logic_19716(agents, world):
    _agent_apply(world, agents, 'recovery', 'future_payoff_weight', 'feedback')

def logic_19717(agents, world):
    _agent_apply(world, agents, 'metabolic_cost', 'self_preservation', 'feedback')

def logic_19718(agents, world):
    _agent_apply(world, agents, 'reproduction_drive', 'self_preservation', 'feedback')

def logic_19719(agents, world):
    _agent_apply(world, agents, 'migration_drive', 'self_preservation', 'feedback')

def logic_19720(agents, world):
    _agent_apply(world, agents, 'exploration_drive', 'self_preservation', 'feedback')

def logic_19721(agents, world):
    _agent_apply(world, agents, 'food_access', 'self_preservation', 'feedback')

def logic_19722(agents, world):
    _agent_apply(world, agents, 'wealth', 'self_preservation', 'feedback')

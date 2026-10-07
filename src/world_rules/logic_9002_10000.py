import torch

RATE = 0.008


def _world_signal(world, name):
    x = getattr(world, name, None)
    if x is None:
        return None
    return torch.nan_to_num(x).float()


def _agent_local(world, agents, name):
    x = agents.pos[:, 0].long()
    y = agents.pos[:, 1].long()
    field = getattr(world, name, None)
    if field is None:
        return None
    return torch.nan_to_num(field[y, x]).to(dtype=agents.energy.dtype)


def _norm(x):
    return torch.sigmoid(torch.nan_to_num(x))


def _world_apply(world, source, target, mode):
    s = _world_signal(world, source)
    t = _world_signal(world, target)
    if s is None or t is None:
        return
    s = _norm(s)
    if mode == "inverse": d = 1 - s
    elif mode == "square": d = s * s
    elif mode == "sqrt": d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse": d = 4 * s * (1 - s)
    elif mode == "threshold": d = (s > 0.5).float()
    elif mode == "saturation": d = s / (0.25 + s)
    elif mode == "reciprocal": d = 1 / (1 + s)
    else: d = s
    t = torch.nan_to_num(t)
    setattr(world, target, t + RATE * (d - t))


def _agent_source(world, agents, name):
    if hasattr(agents, name):
        return torch.nan_to_num(getattr(agents, name)).to(dtype=agents.energy.dtype)
    return _agent_local(world, agents, name)


def _agent_apply(world, agents, source, target, mode):
    s = _agent_source(world, agents, source)
    if s is None or not hasattr(agents, target):
        return
    s = _norm(s)
    x = torch.nan_to_num(getattr(agents, target))
    t = _norm(x)
    if mode == "inverse": d = 1 - s
    elif mode == "square": d = s * s
    elif mode == "sqrt": d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse": d = 4 * s * (1 - s)
    elif mode == "feedback": d = s * t
    elif mode == "scarcity": d = (1 - s) * _norm(getattr(agents, "hunger"))
    elif mode == "reserve": d = s * _norm(getattr(agents, "energy_surplus"))
    elif mode == "stress": d = s * _norm(getattr(agents, "stress"))
    elif mode == "recovery": d = s * _norm(getattr(agents, "health"))
    elif mode == "persistence": d = s * _norm(getattr(agents, "memory_update"))
    elif mode == "risk": d = s * _norm(getattr(agents, "risk_tolerance"))
    elif mode == "competition": d = s * _norm(getattr(agents, "competition_pressure"))
    elif mode == "social": d = s * _norm(getattr(agents, "social_need"))
    elif mode == "resource": d = s * _norm(getattr(agents, "resource_abundance"))
    elif mode == "threshold": d = (s > 0.5).to(s.dtype)
    elif mode == "saturation": d = s / (0.25 + s)
    elif mode == "gap": d = torch.abs(s - t)
    elif mode == "reciprocal": d = 1 / (1 + s)
    else: d = s
    new_signal = t + RATE * (d - t)
    setattr(agents, target, torch.logit(new_signal.clamp(1e-5, 1 - 1e-5)))

def logic_9002(world):
    _world_apply(world, 'temperature', 'evaporation', 'direct')

def logic_9003(world):
    _world_apply(world, 'evaporation', 'humidity', 'inverse')

def logic_9004(world):
    _world_apply(world, 'humidity', 'cloud', 'square')

def logic_9005(world):
    _world_apply(world, 'cloud', 'rain', 'sqrt')

def logic_9006(world):
    _world_apply(world, 'rain', 'surface_water', 'pulse')

def logic_9007(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'threshold')

def logic_9008(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'saturation')

def logic_9009(world):
    _world_apply(world, 'groundwater', 'surface_water', 'reciprocal')

def logic_9010(world):
    _world_apply(world, 'surface_water', 'wetland', 'direct')

def logic_9011(world):
    _world_apply(world, 'wetland', 'humidity', 'inverse')

def logic_9012(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'square')

def logic_9013(world):
    _world_apply(world, 'photosynthesis_factor', 'vegetation', 'sqrt')

def logic_9014(world):
    _world_apply(world, 'vegetation', 'carbon_storage', 'pulse')

def logic_9015(world):
    _world_apply(world, 'carbon_storage', 'co2', 'threshold')

def logic_9016(world):
    _world_apply(world, 'co2', 'photosynthesis_factor', 'saturation')

def logic_9017(world):
    _world_apply(world, 'vegetation', 'organic_matter', 'reciprocal')

def logic_9018(world):
    _world_apply(world, 'organic_matter', 'soil_carbon', 'direct')

def logic_9019(world):
    _world_apply(world, 'soil_carbon', 'carbon_storage', 'inverse')

def logic_9020(world):
    _world_apply(world, 'fire_risk', 'co2', 'square')

def logic_9021(world):
    _world_apply(world, 'co2', 'vegetation', 'sqrt')

def logic_9022(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'pulse')

def logic_9023(world):
    _world_apply(world, 'vegetation', 'biomass', 'threshold')

def logic_9024(world):
    _world_apply(world, 'biomass', 'herbivore', 'saturation')

def logic_9025(world):
    _world_apply(world, 'herbivore', 'predator', 'reciprocal')

def logic_9026(world):
    _world_apply(world, 'predator', 'herbivore', 'direct')

def logic_9027(world):
    _world_apply(world, 'predator', 'carrion', 'inverse')

def logic_9028(world):
    _world_apply(world, 'carrion', 'nutrients', 'square')

def logic_9029(world):
    _world_apply(world, 'nutrients', 'vegetation', 'sqrt')

def logic_9030(world):
    _world_apply(world, 'deadwood', 'decomposition_rate', 'pulse')

def logic_9031(world):
    _world_apply(world, 'decomposition_rate', 'nutrients', 'threshold')

def logic_9032(world):
    _world_apply(world, 'rain', 'runoff', 'saturation')

def logic_9033(world):
    _world_apply(world, 'runoff', 'sediment', 'reciprocal')

def logic_9034(world):
    _world_apply(world, 'sediment', 'soil_depth', 'direct')

def logic_9035(world):
    _world_apply(world, 'soil_depth', 'root_density', 'inverse')

def logic_9036(world):
    _world_apply(world, 'root_density', 'soil_carbon', 'square')

def logic_9037(world):
    _world_apply(world, 'erosion', 'soil_depth', 'sqrt')

def logic_9038(world):
    _world_apply(world, 'erosion', 'habitat_stress', 'pulse')

def logic_9039(world):
    _world_apply(world, 'habitat_stress', 'vegetation', 'threshold')

def logic_9040(world):
    _world_apply(world, 'salinity', 'vegetation', 'saturation')

def logic_9041(world):
    _world_apply(world, 'salinity', 'biodiversity', 'reciprocal')

def logic_9042(world):
    _world_apply(world, 'pathogen_load', 'biodiversity', 'direct')

def logic_9043(world):
    _world_apply(world, 'biodiversity', 'pathogen_load', 'inverse')

def logic_9044(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'square')

def logic_9045(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'sqrt')

def logic_9046(world):
    _world_apply(world, 'wetland', 'biodiversity', 'pulse')

def logic_9047(world):
    _world_apply(world, 'biodiversity', 'habitat_stress', 'threshold')

def logic_9048(world):
    _world_apply(world, 'habitat_stress', 'pathogen_load', 'saturation')

def logic_9049(world):
    _world_apply(world, 'oxygen', 'pathogen_load', 'reciprocal')

def logic_9050(world):
    _world_apply(world, 'fire_risk', 'habitat_stress', 'direct')

def logic_9051(world):
    _world_apply(world, 'habitat_stress', 'fire_risk', 'inverse')

def logic_9052(world):
    _world_apply(world, 'snowpack', 'runoff', 'square')

def logic_9053(world):
    _world_apply(world, 'snowpack', 'surface_ice', 'sqrt')

def logic_9054(world):
    _world_apply(world, 'surface_ice', 'surface_water', 'pulse')

def logic_9055(world):
    _world_apply(world, 'ice', 'surface_ice', 'threshold')

def logic_9056(world):
    _world_apply(world, 'surface_ice', 'snowpack', 'saturation')

def logic_9057(world):
    _world_apply(world, 'temperature', 'snowpack', 'reciprocal')

def logic_9058(world):
    _world_apply(world, 'temperature', 'surface_ice', 'direct')

def logic_9059(world):
    _world_apply(world, 'cloud', 'temperature', 'inverse')

def logic_9060(world):
    _world_apply(world, 'wind_x', 'cloud', 'square')

def logic_9061(world):
    _world_apply(world, 'wind_y', 'cloud', 'sqrt')

def logic_9062(world):
    _world_apply(world, 'temperature', 'surface_water', 'pulse')

def logic_9063(world):
    _world_apply(world, 'temperature', 'humidity', 'threshold')

def logic_9064(world):
    _world_apply(world, 'temperature', 'cloud', 'saturation')

def logic_9065(world):
    _world_apply(world, 'temperature', 'rain', 'reciprocal')

def logic_9066(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'direct')

def logic_9067(world):
    _world_apply(world, 'temperature', 'runoff', 'inverse')

def logic_9068(world):
    _world_apply(world, 'temperature', 'wind_x', 'square')

def logic_9069(world):
    _world_apply(world, 'temperature', 'wind_y', 'sqrt')

def logic_9070(world):
    _world_apply(world, 'temperature', 'vegetation', 'pulse')

def logic_9071(world):
    _world_apply(world, 'temperature', 'biomass', 'threshold')

def logic_9072(world):
    _world_apply(world, 'temperature', 'herbivore', 'saturation')

def logic_9073(world):
    _world_apply(world, 'temperature', 'predator', 'reciprocal')

def logic_9074(world):
    _world_apply(world, 'temperature', 'carrion', 'direct')

def logic_9075(world):
    _world_apply(world, 'temperature', 'nutrients', 'inverse')

def logic_9076(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'square')

def logic_9077(world):
    _world_apply(world, 'temperature', 'oxygen', 'sqrt')

def logic_9078(world):
    _world_apply(world, 'temperature', 'co2', 'pulse')

def logic_9079(world):
    _world_apply(world, 'temperature', 'ice', 'threshold')

def logic_9080(world):
    _world_apply(world, 'temperature', 'detritus', 'saturation')

def logic_9081(world):
    _world_apply(world, 'temperature', 'methane', 'reciprocal')

def logic_9082(world):
    _world_apply(world, 'temperature', 'biodiversity', 'direct')

def logic_9083(world):
    _world_apply(world, 'temperature', 'habitat_stress', 'inverse')

def logic_9084(world):
    _world_apply(world, 'temperature', 'erosion', 'square')

def logic_9085(world):
    _world_apply(world, 'temperature', 'soil_depth', 'sqrt')

def logic_9086(world):
    _world_apply(world, 'temperature', 'root_density', 'pulse')

def logic_9087(world):
    _world_apply(world, 'temperature', 'wetland', 'threshold')

def logic_9088(world):
    _world_apply(world, 'temperature', 'carbon_storage', 'saturation')

def logic_9089(world):
    _world_apply(world, 'temperature', 'fire_risk', 'reciprocal')

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
    return torch.sigmoid(x)


def _world_apply(world, source, target, mode):
    s = _world_signal(world, source)
    t = _world_signal(world, target)
    if s is None or t is None:
        return
    s = _norm(s)
    if mode == "inverse":
        d = 1 - s
    elif mode == "square":
        d = s * s
    elif mode == "sqrt":
        d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse":
        d = 4 * s * (1 - s)
    elif mode == "threshold":
        d = (s > 0.5).float()
    elif mode == "saturation":
        d = s / (0.25 + s)
    elif mode == "reciprocal":
        d = 1 / (1 + s)
    else:
        d = s
    setattr(world, target, torch.nan_to_num(t) + RATE * (d - torch.nan_to_num(t)))


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
    if mode == "inverse":
        d = 1 - s
    elif mode == "square":
        d = s * s
    elif mode == "sqrt":
        d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse":
        d = 4 * s * (1 - s)
    elif mode == "feedback":
        d = s * t
    elif mode == "scarcity":
        d = (1 - s) * _norm(getattr(agents, "hunger"))
    elif mode == "reserve":
        d = s * _norm(getattr(agents, "energy_surplus"))
    elif mode == "stress":
        d = s * _norm(getattr(agents, "stress"))
    elif mode == "recovery":
        d = s * _norm(getattr(agents, "health"))
    elif mode == "persistence":
        d = s * _norm(getattr(agents, "memory_update"))
    elif mode == "risk":
        d = s * _norm(getattr(agents, "risk_tolerance"))
    elif mode == "competition":
        d = s * _norm(getattr(agents, "competition_pressure"))
    elif mode == "social":
        d = s * _norm(getattr(agents, "social_need"))
    elif mode == "resource":
        d = s * _norm(getattr(agents, "resource_abundance"))
    elif mode == "threshold":
        d = (s > 0.5).to(s.dtype)
    elif mode == "saturation":
        d = s / (0.25 + s)
    elif mode == "gap":
        d = torch.abs(s - t)
    elif mode == "reciprocal":
        d = 1 / (1 + s)
    else:
        d = s
    new_signal = t + RATE * (d - t)
    setattr(agents, target, torch.logit(new_signal.clamp(1e-5, 1 - 1e-5)))

def logic_4002(world):
    _world_apply(world, 'rain', 'surface_water', 'direct')

def logic_4003(world):
    _world_apply(world, 'groundwater', 'surface_water', 'inverse')

def logic_4004(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'square')

def logic_4005(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'sqrt')

def logic_4006(world):
    _world_apply(world, 'vegetation', 'biomass', 'pulse')

def logic_4007(world):
    _world_apply(world, 'biomass', 'herbivore', 'threshold')

def logic_4008(world):
    _world_apply(world, 'herbivore', 'predator', 'saturation')

def logic_4009(world):
    _world_apply(world, 'predator', 'carrion', 'reciprocal')

def logic_4010(world):
    _world_apply(world, 'carrion', 'nutrients', 'direct')

def logic_4011(world):
    _world_apply(world, 'nutrients', 'vegetation', 'inverse')

def logic_4012(world):
    _world_apply(world, 'organic_matter', 'soil_carbon', 'square')

def logic_4013(world):
    _world_apply(world, 'soil_carbon', 'vegetation', 'sqrt')

def logic_4014(world):
    _world_apply(world, 'decomposition_rate', 'nutrients', 'pulse')

def logic_4015(world):
    _world_apply(world, 'temperature', 'evaporation', 'threshold')

def logic_4016(world):
    _world_apply(world, 'humidity', 'evaporation', 'saturation')

def logic_4017(world):
    _world_apply(world, 'wind_x', 'evaporation', 'reciprocal')

def logic_4018(world):
    _world_apply(world, 'snowpack', 'runoff', 'direct')

def logic_4019(world):
    _world_apply(world, 'runoff', 'sediment', 'inverse')

def logic_4020(world):
    _world_apply(world, 'sediment', 'soil_depth', 'square')

def logic_4021(world):
    _world_apply(world, 'fire_risk', 'ash', 'sqrt')

def logic_4022(world):
    _world_apply(world, 'ash', 'nutrients', 'pulse')

def logic_4023(world):
    _world_apply(world, 'wetland', 'methane', 'threshold')

def logic_4024(world):
    _world_apply(world, 'algae', 'organic_matter', 'saturation')

def logic_4025(world):
    _world_apply(world, 'flowers', 'pollinators', 'reciprocal')

def logic_4026(world):
    _world_apply(world, 'pollinators', 'flowers', 'direct')

def logic_4027(world):
    _world_apply(world, 'seed_bank', 'vegetation', 'inverse')

def logic_4028(world):
    _world_apply(world, 'deadwood', 'decomposition_rate', 'square')

def logic_4029(world):
    _world_apply(world, 'surface_ice', 'surface_water', 'sqrt')

def logic_4030(world):
    _world_apply(world, 'ice', 'surface_water', 'pulse')

def logic_4031(world):
    _world_apply(world, 'cloud', 'rain', 'threshold')

def logic_4032(world):
    _world_apply(world, 'rain', 'groundwater', 'saturation')

def logic_4033(world):
    _world_apply(world, 'groundwater', 'wetland', 'reciprocal')

def logic_4034(world):
    _world_apply(world, 'wetland', 'surface_water', 'direct')

def logic_4035(world):
    _world_apply(world, 'fire_risk', 'vegetation', 'inverse')

def logic_4036(world):
    _world_apply(world, 'fire_risk', 'biomass', 'square')

def logic_4037(world):
    _world_apply(world, 'fire_risk', 'deadwood', 'sqrt')

def logic_4038(world):
    _world_apply(world, 'erosion', 'soil_carbon', 'pulse')

def logic_4039(world):
    _world_apply(world, 'carbon_storage', 'co2', 'threshold')

def logic_4040(world):
    _world_apply(world, 'co2', 'photosynthesis_factor', 'saturation')

def logic_4041(world):
    _world_apply(world, 'photosynthesis_factor', 'vegetation', 'reciprocal')

def logic_4042(world):
    _world_apply(world, 'salinity', 'vegetation', 'direct')

def logic_4043(world):
    _world_apply(world, 'habitat_stress', 'biodiversity', 'inverse')

def logic_4044(world):
    _world_apply(world, 'biodiversity', 'habitat_stress', 'square')

def logic_4045(world):
    _world_apply(world, 'soil_depth', 'root_density', 'sqrt')

def logic_4046(world):
    _world_apply(world, 'root_density', 'soil_carbon', 'pulse')

def logic_4047(world):
    _world_apply(world, 'oxygen', 'health', 'threshold')

def logic_4048(world):
    _world_apply(world, 'pathogen_load', 'infection_risk', 'saturation')

def logic_4049(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'reciprocal')

def logic_4050(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'direct')

def logic_4051(world):
    _world_apply(world, 'habitat_stress', 'fire_risk', 'inverse')

def logic_4052(world):
    _world_apply(world, 'vegetation', 'evaporation', 'square')

def logic_4053(world):
    _world_apply(world, 'cloud', 'temperature', 'sqrt')

def logic_4054(world):
    _world_apply(world, 'snowpack', 'temperature', 'pulse')

def logic_4055(world):
    _world_apply(world, 'groundwater', 'soil_moisture', 'threshold')

def logic_4056(world):
    _world_apply(world, 'runoff', 'surface_water', 'saturation')

def logic_4057(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'reciprocal')

def logic_4058(world):
    _world_apply(world, 'erosion', 'sediment', 'direct')

def logic_4059(world):
    _world_apply(world, 'wetland', 'biodiversity', 'inverse')

def logic_4060(world):
    _world_apply(world, 'biodiversity', 'vegetation', 'square')

def logic_4061(world):
    _world_apply(world, 'algae', 'oxygen', 'sqrt')

def logic_4062(world):
    _world_apply(world, 'photosynthesis_factor', 'oxygen', 'pulse')

def logic_4063(world):
    _world_apply(world, 'co2', 'vegetation', 'threshold')

def logic_4064(world):
    _world_apply(world, 'methane', 'co2', 'saturation')

def logic_4065(world):
    _world_apply(world, 'fire_risk', 'co2', 'reciprocal')

def logic_4066(world):
    _world_apply(world, 'ash', 'soil_carbon', 'direct')

def logic_4067(world):
    _world_apply(world, 'surface_water', 'salinity', 'inverse')

def logic_4068(world):
    _world_apply(world, 'evaporation', 'humidity', 'square')

def logic_4069(world):
    _world_apply(world, 'temperature', 'humidity', 'sqrt')

def logic_4070(world):
    _world_apply(world, 'wind_y', 'cloud', 'pulse')

def logic_4071(world):
    _world_apply(world, 'wind_x', 'cloud', 'threshold')

def logic_4072(world):
    _world_apply(world, 'snowpack', 'surface_ice', 'saturation')

def logic_4073(world):
    _world_apply(world, 'surface_ice', 'snowpack', 'reciprocal')

def logic_4074(world):
    _world_apply(world, 'ice', 'surface_ice', 'direct')

def logic_4075(world):
    _world_apply(world, 'soil_moisture', 'organic_matter', 'inverse')

def logic_4076(world):
    _world_apply(world, 'deadwood', 'organic_matter', 'square')

def logic_4077(world):
    _world_apply(world, 'carrion', 'organic_matter', 'sqrt')

def logic_4078(world):
    _world_apply(world, 'herbivore', 'vegetation', 'pulse')

def logic_4079(world):
    _world_apply(world, 'predator', 'herbivore', 'threshold')

def logic_4080(world):
    _world_apply(world, 'vegetation', 'seed_bank', 'saturation')

def logic_4081(world):
    _world_apply(world, 'flowers', 'seed_bank', 'reciprocal')

def logic_4082(world):
    _world_apply(world, 'pollinators', 'seed_bank', 'direct')

def logic_4083(world):
    _world_apply(world, 'rain', 'wetland', 'inverse')

def logic_4084(world):
    _world_apply(world, 'runoff', 'wetland', 'square')

def logic_4085(world):
    _world_apply(world, 'groundwater', 'surface_water', 'sqrt')

def logic_4086(world):
    _world_apply(world, 'surface_water', 'algae', 'pulse')

def logic_4087(world):
    _world_apply(world, 'nutrients', 'algae', 'threshold')

def logic_4088(world):
    _world_apply(world, 'algae', 'surface_water', 'saturation')

def logic_4089(world):
    _world_apply(world, 'temperature', 'vegetation', 'reciprocal')

def logic_4090(world):
    _world_apply(world, 'temperature', 'biodiversity', 'direct')

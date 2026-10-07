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

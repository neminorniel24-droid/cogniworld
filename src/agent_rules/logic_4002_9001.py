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

def logic_4102(agents, world):
    _agent_apply(world, agents, 'temperature', 'hydration', 'direct')

def logic_4103(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hydration', 'direct')

def logic_4104(agents, world):
    _agent_apply(world, agents, 'humidity', 'hydration', 'direct')

def logic_4105(agents, world):
    _agent_apply(world, agents, 'cloud', 'hydration', 'direct')

def logic_4106(agents, world):
    _agent_apply(world, agents, 'rain', 'hydration', 'direct')

def logic_4107(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hydration', 'direct')

def logic_4108(agents, world):
    _agent_apply(world, agents, 'runoff', 'hydration', 'direct')

def logic_4109(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hydration', 'direct')

def logic_4110(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hydration', 'direct')

def logic_4111(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hydration', 'direct')

def logic_4112(agents, world):
    _agent_apply(world, agents, 'biomass', 'hydration', 'direct')

def logic_4113(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hydration', 'direct')

def logic_4114(agents, world):
    _agent_apply(world, agents, 'predator', 'hydration', 'direct')

def logic_4115(agents, world):
    _agent_apply(world, agents, 'carrion', 'hydration', 'direct')

def logic_4116(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hydration', 'direct')

def logic_4117(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hydration', 'direct')

def logic_4118(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hydration', 'direct')

def logic_4119(agents, world):
    _agent_apply(world, agents, 'co2', 'hydration', 'direct')

def logic_4120(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hydration', 'direct')

def logic_4121(agents, world):
    _agent_apply(world, agents, 'ice', 'hydration', 'direct')

def logic_4122(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hydration', 'direct')

def logic_4123(agents, world):
    _agent_apply(world, agents, 'detritus', 'hydration', 'direct')

def logic_4124(agents, world):
    _agent_apply(world, agents, 'methane', 'hydration', 'direct')

def logic_4125(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hydration', 'direct')

def logic_4126(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hydration', 'direct')

def logic_4127(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hydration', 'direct')

def logic_4128(agents, world):
    _agent_apply(world, agents, 'erosion', 'hydration', 'direct')

def logic_4129(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hydration', 'direct')

def logic_4130(agents, world):
    _agent_apply(world, agents, 'root_density', 'hydration', 'direct')

def logic_4131(agents, world):
    _agent_apply(world, agents, 'wetland', 'hydration', 'direct')

def logic_4132(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hydration', 'direct')

def logic_4133(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hydration', 'direct')

def logic_4134(agents, world):
    _agent_apply(world, agents, 'ash', 'hydration', 'direct')

def logic_4135(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hydration', 'direct')

def logic_4136(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hydration', 'direct')

def logic_4137(agents, world):
    _agent_apply(world, agents, 'sediment', 'hydration', 'direct')

def logic_4138(agents, world):
    _agent_apply(world, agents, 'salinity', 'hydration', 'direct')

def logic_4139(agents, world):
    _agent_apply(world, agents, 'algae', 'hydration', 'direct')

def logic_4140(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hydration', 'direct')

def logic_4141(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hydration', 'direct')

def logic_4142(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hydration', 'direct')

def logic_4143(agents, world):
    _agent_apply(world, agents, 'flowers', 'hydration', 'direct')

def logic_4144(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hydration', 'direct')

def logic_4145(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hydration', 'direct')

def logic_4146(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hydration', 'direct')

def logic_4147(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hydration', 'direct')

def logic_4148(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hydration', 'direct')

def logic_4149(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hydration', 'direct')

def logic_4150(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hydration', 'direct')

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

def logic_9201(agents, world):
    _agent_apply(world, agents, 'temperature', 'hydration', 'direct')

def logic_9202(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hydration', 'direct')

def logic_9203(agents, world):
    _agent_apply(world, agents, 'humidity', 'hydration', 'direct')

def logic_9204(agents, world):
    _agent_apply(world, agents, 'cloud', 'hydration', 'direct')

def logic_9205(agents, world):
    _agent_apply(world, agents, 'rain', 'hydration', 'direct')

def logic_9206(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hydration', 'direct')

def logic_9207(agents, world):
    _agent_apply(world, agents, 'runoff', 'hydration', 'direct')

def logic_9208(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hydration', 'direct')

def logic_9209(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hydration', 'direct')

def logic_9210(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hydration', 'direct')

def logic_9211(agents, world):
    _agent_apply(world, agents, 'biomass', 'hydration', 'direct')

def logic_9212(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hydration', 'direct')

def logic_9213(agents, world):
    _agent_apply(world, agents, 'predator', 'hydration', 'direct')

def logic_9214(agents, world):
    _agent_apply(world, agents, 'carrion', 'hydration', 'direct')

def logic_9215(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hydration', 'direct')

def logic_9216(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hydration', 'direct')

def logic_9217(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hydration', 'direct')

def logic_9218(agents, world):
    _agent_apply(world, agents, 'co2', 'hydration', 'direct')

def logic_9219(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hydration', 'direct')

def logic_9220(agents, world):
    _agent_apply(world, agents, 'ice', 'hydration', 'direct')

def logic_9221(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hydration', 'direct')

def logic_9222(agents, world):
    _agent_apply(world, agents, 'detritus', 'hydration', 'direct')

def logic_9223(agents, world):
    _agent_apply(world, agents, 'methane', 'hydration', 'direct')

def logic_9224(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hydration', 'direct')

def logic_9225(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hydration', 'direct')

def logic_9226(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hydration', 'direct')

def logic_9227(agents, world):
    _agent_apply(world, agents, 'erosion', 'hydration', 'direct')

def logic_9228(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hydration', 'direct')

def logic_9229(agents, world):
    _agent_apply(world, agents, 'root_density', 'hydration', 'direct')

def logic_9230(agents, world):
    _agent_apply(world, agents, 'wetland', 'hydration', 'direct')

def logic_9231(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hydration', 'direct')

def logic_9232(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hydration', 'direct')

def logic_9233(agents, world):
    _agent_apply(world, agents, 'ash', 'hydration', 'direct')

def logic_9234(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hydration', 'direct')

def logic_9235(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hydration', 'direct')

def logic_9236(agents, world):
    _agent_apply(world, agents, 'sediment', 'hydration', 'direct')

def logic_9237(agents, world):
    _agent_apply(world, agents, 'salinity', 'hydration', 'direct')

def logic_9238(agents, world):
    _agent_apply(world, agents, 'algae', 'hydration', 'direct')

def logic_9239(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hydration', 'direct')

def logic_9240(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hydration', 'direct')

def logic_9241(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hydration', 'direct')

def logic_9242(agents, world):
    _agent_apply(world, agents, 'flowers', 'hydration', 'direct')

def logic_9243(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hydration', 'direct')

def logic_9244(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hydration', 'direct')

def logic_9245(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hydration', 'direct')

def logic_9246(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hydration', 'direct')

def logic_9247(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hydration', 'direct')

def logic_9248(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hydration', 'direct')

def logic_9249(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hydration', 'direct')

def logic_9250(agents, world):
    _agent_apply(world, agents, 'hydration', 'hydration', 'direct')

def logic_9251(agents, world):
    _agent_apply(world, agents, 'thirst', 'hydration', 'direct')

def logic_9252(agents, world):
    _agent_apply(world, agents, 'hunger', 'hydration', 'direct')

def logic_9253(agents, world):
    _agent_apply(world, agents, 'health', 'hydration', 'direct')

def logic_9254(agents, world):
    _agent_apply(world, agents, 'stress', 'hydration', 'direct')

def logic_9255(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'hydration', 'direct')

def logic_9256(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'hydration', 'direct')

def logic_9257(agents, world):
    _agent_apply(world, agents, 'social_need', 'hydration', 'direct')

def logic_9258(agents, world):
    _agent_apply(world, agents, 'cooperation', 'hydration', 'direct')

def logic_9259(agents, world):
    _agent_apply(world, agents, 'defection', 'hydration', 'direct')

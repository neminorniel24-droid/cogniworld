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

def logic_10001(world):
    _world_apply(world, 'temperature', 'surface_water', 'direct')

def logic_10002(world):
    _world_apply(world, 'temperature', 'humidity', 'square')

def logic_10003(world):
    _world_apply(world, 'temperature', 'cloud', 'pulse')

def logic_10004(world):
    _world_apply(world, 'temperature', 'rain', 'saturation')

def logic_10005(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'gap')

def logic_10006(world):
    _world_apply(world, 'temperature', 'runoff', 'direct')

def logic_10007(world):
    _world_apply(world, 'temperature', 'wind_x', 'square')

def logic_10008(world):
    _world_apply(world, 'temperature', 'wind_y', 'pulse')

def logic_10009(world):
    _world_apply(world, 'temperature', 'vegetation', 'gap')

def logic_10010(world):
    _world_apply(world, 'temperature', 'biomass', 'direct')

def logic_10011(world):
    _world_apply(world, 'temperature', 'herbivore', 'square')

def logic_10012(world):
    _world_apply(world, 'temperature', 'predator', 'pulse')

def logic_10013(world):
    _world_apply(world, 'temperature', 'carrion', 'saturation')

def logic_10014(world):
    _world_apply(world, 'temperature', 'nutrients', 'gap')

def logic_10015(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'direct')

def logic_10016(world):
    _world_apply(world, 'temperature', 'oxygen', 'square')

def logic_10017(world):
    _world_apply(world, 'temperature', 'co2', 'saturation')

def logic_10018(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'gap')

def logic_10019(world):
    _world_apply(world, 'temperature', 'ice', 'direct')

def logic_10020(world):
    _world_apply(world, 'temperature', 'evaporation', 'square')

def logic_10021(world):
    _world_apply(world, 'temperature', 'detritus', 'pulse')

def logic_10022(world):
    _world_apply(world, 'temperature', 'methane', 'saturation')

def logic_10023(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'gap')

def logic_10024(world):
    _world_apply(world, 'temperature', 'biodiversity', 'direct')

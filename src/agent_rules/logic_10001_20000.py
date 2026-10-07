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

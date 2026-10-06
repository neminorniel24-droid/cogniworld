import torch

_RATE = 0.012

def _local(world, agents, name):
    x = agents.pos[:,0].long()
    y = agents.pos[:,1].long()
    field = getattr(world, name)
    return field[y, x].to(dtype=agents.energy.dtype).clamp(0.0, 1.0)

def _a(agents, name):
    return getattr(agents, name)

def _update(agents, target, desired):
    x = _a(agents, target)
    desired = torch.nan_to_num(desired).clamp(0.0, 1.0)
    setattr(agents, target, torch.nan_to_num(x + _RATE * (desired - x)).clamp(0.0, 1.0))

def _desired(agents, world, source, target, mode):
    s = _local(world, agents, source)
    t = _a(agents, target).clamp(0.0, 1.0)
    if mode == "direct": return s
    if mode == "inverse": return 1.0 - s
    if mode == "threshold": return (s > 0.5).to(s.dtype)
    if mode == "strong": return s * s
    if mode == "limited": return torch.sqrt(s.clamp_min(0.0))
    if mode == "pulse": return (4.0 * s * (1.0-s)).clamp(0.0,1.0)
    if mode == "feedback": return s * t
    if mode == "counterpressure": return 1.0 - s * t
    if mode == "capacity": return s * _a(agents, "resource_abundance").clamp(0.0,1.0)
    if mode == "reserve": return s * _a(agents, "energy_surplus").clamp(0.0,1.0)
    if mode == "scarcity": return (1.0-s) * _a(agents, "hunger").clamp(0.0,1.0)
    if mode == "stress": return s * _a(agents, "stress").clamp(0.0,1.0)
    if mode == "recovery": return s * _a(agents, "health").clamp(0.0,1.0)
    if mode == "persistence": return s * _a(agents, "memory_update").clamp(0.0,1.0)
    raise ValueError(mode)

def logic_3002(agents, world):
    # surface_water -> hydration; direct coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'direct'))

def logic_3003(agents, world):
    # surface_water -> hydration; inverse coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'inverse'))

def logic_3004(agents, world):
    # surface_water -> hydration; threshold coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'threshold'))

def logic_3005(agents, world):
    # surface_water -> hydration; strong coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'strong'))

def logic_3006(agents, world):
    # surface_water -> hydration; limited coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'limited'))

def logic_3007(agents, world):
    # surface_water -> hydration; pulse coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'pulse'))

def logic_3008(agents, world):
    # surface_water -> hydration; feedback coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'feedback'))

def logic_3009(agents, world):
    # surface_water -> hydration; counterpressure coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'counterpressure'))

def logic_3010(agents, world):
    # surface_water -> hydration; capacity coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'capacity'))

def logic_3011(agents, world):
    # surface_water -> hydration; reserve coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'reserve'))

def logic_3012(agents, world):
    # surface_water -> hydration; scarcity coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'scarcity'))

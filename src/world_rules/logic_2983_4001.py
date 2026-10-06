import torch

_RATE = 0.018

def _bounded(x):
    return torch.nan_to_num(x).clamp(0.0, 1.0)

def _apply(world, source_name, target_name, sign=1.0):
    source = _bounded(getattr(world, source_name))
    target = _bounded(getattr(world, target_name))
    desired = source if sign > 0 else (1.0 - source)
    setattr(world, target_name, _bounded(target + _RATE * (desired - target)))

def logic_2983(world):
    # rainfall sustains surface water.
    _apply(world, 'rain', 'surface_water', 1.0)

def logic_2984(world):
    # groundwater discharge sustains surface water.
    _apply(world, 'groundwater', 'surface_water', 1.0)

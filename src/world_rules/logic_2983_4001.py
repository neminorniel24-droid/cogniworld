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

def logic_2985(world):
    # surface water replenishes soil moisture.
    _apply(world, 'surface_water', 'soil_moisture', -1.0)

def logic_2986(world):
    # soil moisture supports vegetation.
    _apply(world, 'soil_moisture', 'vegetation', 1.0)

def logic_2987(world):
    # vegetation contributes biomass.
    _apply(world, 'vegetation', 'biomass', 1.0)

def logic_2988(world):
    # biomass contributes organic matter.
    _apply(world, 'biomass', 'organic_matter', -1.0)

def logic_2989(world):
    # organic matter supports soil carbon.
    _apply(world, 'organic_matter', 'soil_carbon', 1.0)

def logic_2990(world):
    # decomposition releases nutrients.
    _apply(world, 'decomposition_rate', 'nutrients', 1.0)

def logic_2991(world):
    # nutrients support vegetation.
    _apply(world, 'nutrients', 'vegetation', -1.0)

def logic_2992(world):
    # vegetation alters evaporative demand.
    _apply(world, 'vegetation', 'evaporation', 1.0)

def logic_2993(world):
    # temperature raises evaporation.
    _apply(world, 'temperature', 'evaporation', 1.0)

def logic_2994(world):
    # humidity suppresses evaporation.
    _apply(world, 'humidity', 'evaporation', -1.0)

def logic_2995(world):
    # wind increases evaporative loss.
    _apply(world, 'wind_x', 'evaporation', 1.0)

def logic_2996(world):
    # snowpack supplies runoff.
    _apply(world, 'snowpack', 'runoff', 1.0)

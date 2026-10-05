import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.4 * world.evaporation * world.humidity).clamp(0.0, 1.0)

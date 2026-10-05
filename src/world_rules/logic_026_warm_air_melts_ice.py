import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.1 * (world.temperature > 0.3) * world.ice).clamp(0.0, 1.0); world.ice = (world.ice - 0.1 * (world.temperature > 0.3) * world.ice).clamp(0.0, 1.0)

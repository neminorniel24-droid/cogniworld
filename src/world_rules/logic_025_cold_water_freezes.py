import torch

def apply(world):
    world.ice = (world.ice + 0.05 * (world.temperature < 0.25) * world.surface_water).clamp(0.0, 1.0); world.surface_water = (world.surface_water - 0.05 * (world.temperature < 0.25) * world.surface_water).clamp(0.0,1.0)

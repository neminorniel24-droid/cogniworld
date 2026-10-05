import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.01 * (1.0 - world.elevation) * world.soil_moisture).clamp(0.0, 1.0)

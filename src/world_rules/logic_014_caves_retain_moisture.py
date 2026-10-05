import torch

def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.02 * (world.biome == 4) * world.surface_water).clamp(0.0, 1.0)

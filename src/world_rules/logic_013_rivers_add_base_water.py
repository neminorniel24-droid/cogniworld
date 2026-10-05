import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.03 * (world.biome == 1)).clamp(0.0, 1.0)

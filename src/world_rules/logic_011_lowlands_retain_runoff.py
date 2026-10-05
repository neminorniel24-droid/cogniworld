import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.1 * world.runoff * (1.0 - world.elevation)).clamp(0.0, 1.0)

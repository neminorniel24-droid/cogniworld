import torch

def apply(world):
    world.surface_water *= (1.0 - 0.02 * world.elevation).clamp(0.0, 1.0)

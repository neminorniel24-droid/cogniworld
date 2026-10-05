import torch

def apply(world):
    world.surface_water = (world.surface_water - world.evaporation).clamp_min(0.0)

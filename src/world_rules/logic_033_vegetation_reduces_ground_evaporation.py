import torch

def apply(world):
    world.surface_water = (world.surface_water + 0.5 * world.evaporation * world.vegetation).clamp(0.0, 1.0)

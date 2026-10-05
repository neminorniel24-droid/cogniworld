import torch

def apply(world):
    world.temperature += 0.01 * (0.5 - world.temperature) * world.surface_water

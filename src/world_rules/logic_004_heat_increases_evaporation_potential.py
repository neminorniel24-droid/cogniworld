import torch

def apply(world):
    world.evaporation = (0.01 + 0.04 * world.temperature).clamp(0.0, 0.1)

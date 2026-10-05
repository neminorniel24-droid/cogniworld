import torch

def apply(world):
    world.humidity = (world.humidity + 0.5 * world.evaporation).clamp(0.0, 1.0)

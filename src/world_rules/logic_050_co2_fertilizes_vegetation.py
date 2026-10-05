import torch

def apply(world):
    world.vegetation = (world.vegetation + 0.01 * world.co2 * (1.0 - world.vegetation) * world.photosynthesis_factor).clamp(0.0,1.0)

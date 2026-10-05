import torch

def apply(world):
    world.nutrients *= (1.0 - 0.02 * world.rain).clamp(0.0,1.0)

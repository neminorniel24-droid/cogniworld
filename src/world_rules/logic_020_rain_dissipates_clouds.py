import torch

def apply(world):
    world.cloud *= (1.0 - 0.1 * world.rain).clamp(0.0, 1.0)

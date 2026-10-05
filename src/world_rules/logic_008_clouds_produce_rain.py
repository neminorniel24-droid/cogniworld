import torch

def apply(world):
    world.rain = (0.1 * world.cloud).clamp(0.0, 1.0)

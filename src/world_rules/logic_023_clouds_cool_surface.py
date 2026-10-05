import torch

def apply(world):
    world.temperature = (world.temperature - 0.02 * world.cloud).clamp(0.0, 1.0)

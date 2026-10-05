import torch

def apply(world):
    world.photosynthesis_factor = (1.0 - 0.2 * world.cloud).clamp(0.0,1.0)

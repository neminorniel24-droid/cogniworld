import torch

def apply(world):
    world.nutrients = (world.nutrients - 0.05 * world.runoff).clamp(0.0,1.0)

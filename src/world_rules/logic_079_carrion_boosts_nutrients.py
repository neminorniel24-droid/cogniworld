import torch

def apply(world):
    world.nutrients = (world.nutrients + 0.01 * world.carrion).clamp(0.0,1.0)

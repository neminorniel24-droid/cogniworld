import torch

def apply(world):
    world.methane = (world.methane + 0.005 * world.wetland).clamp(0.0,1.0)

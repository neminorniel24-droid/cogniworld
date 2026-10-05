import torch

def apply(world):
    world.temperature = (world.temperature + 0.01 * world.methane).clamp(0.0,1.0)

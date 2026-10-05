import torch

def apply(world):
    world.co2 = (world.co2 - 0.02 * world.vegetation * world.co2).clamp(0.0,1.0)

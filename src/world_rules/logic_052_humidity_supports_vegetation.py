import torch

def apply(world):
    world.vegetation = (world.vegetation + 0.01 * world.humidity * (1.0 - world.vegetation)).clamp(0.0,1.0)

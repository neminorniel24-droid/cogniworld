import torch

def apply(world):
    world.vegetation = (world.vegetation + 0.01 * (world.biome == 1)).clamp(0.0,1.0)

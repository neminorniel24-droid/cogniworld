import torch

def apply(world):
    world.vegetation = torch.where(world.biome == 4, world.vegetation * 0.7, world.vegetation)

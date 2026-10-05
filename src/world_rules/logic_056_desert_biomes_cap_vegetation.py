import torch

def apply(world):
    world.vegetation = torch.where(world.biome == 3, torch.minimum(world.vegetation, 0.15 + 0.1 * world.soil_moisture), world.vegetation)

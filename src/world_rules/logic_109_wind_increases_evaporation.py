import torch

def apply(world):
    world.evaporation = (world.evaporation + 0.006 * torch.sqrt(world.wind_x**2 + world.wind_y**2)).clamp(0.0, 1.0)

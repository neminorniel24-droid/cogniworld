import torch

def apply(world):
    world.oxygen = (world.oxygen + 0.005 * torch.sqrt(world.wind_x**2 + world.wind_y**2)).clamp(0.0, 1.0)

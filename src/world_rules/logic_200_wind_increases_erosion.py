import torch

def apply(world):
    world.erosion = (world.erosion + 0.003 * torch.sqrt(world.wind_x**2 + world.wind_y**2) * (1.0 - world.root_density)).clamp(0.0, 1.0)

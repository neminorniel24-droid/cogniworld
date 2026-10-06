import torch

def apply(world):
    world.fire_risk = (world.fire_risk + 0.004 * torch.sqrt(world.wind_x**2 + world.wind_y**2)).clamp(0.0, 1.0)

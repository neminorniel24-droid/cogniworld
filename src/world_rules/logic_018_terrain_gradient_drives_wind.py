import torch

def apply(world):
    world.wind_x += 0.05 * (torch.roll(world.elevation, -1, 1) - torch.roll(world.elevation, 1, 1))
    world.wind_y += 0.05 * (torch.roll(world.elevation, -1, 0) - torch.roll(world.elevation, 1, 0))

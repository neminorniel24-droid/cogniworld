import torch

def apply(world):
    world.cloud = 0.8 * world.cloud + 0.05 * (torch.roll(world.cloud, 1, 0) + torch.roll(world.cloud, -1, 0) + torch.roll(world.cloud, 1, 1) + torch.roll(world.cloud, -1, 1))

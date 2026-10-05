import torch

def apply(world):
    world.biodiversity = (world.biodiversity + 0.02 * torch.abs(world.temperature - torch.roll(world.temperature,1,1))).clamp(0.0,1.0)

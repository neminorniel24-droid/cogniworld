import torch

def apply(world):
    world.vegetation = (world.vegetation - 0.02 * torch.relu(world.temperature - 0.8)).clamp(0.0,1.0)

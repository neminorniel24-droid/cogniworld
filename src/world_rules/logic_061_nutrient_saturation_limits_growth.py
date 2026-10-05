import torch

def apply(world):
    world.vegetation *= (1.0 - 0.01 * torch.relu(world.nutrients - 0.8)).clamp(0.9,1.0)

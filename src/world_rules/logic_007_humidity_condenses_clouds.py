import torch

def apply(world):
    world.cloud = (world.cloud + 0.05 * torch.relu(world.humidity - 0.6)).clamp(0.0, 1.0)

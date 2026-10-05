import torch

def apply(world):
    world.carrion = (world.carrion + world.carrion * 0.25 * torch.relu(0.5 - world.temperature)).clamp(0.0,1.0)

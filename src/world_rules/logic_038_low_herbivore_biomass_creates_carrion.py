import torch

def apply(world):
    world.carrion = (world.carrion + 0.005 * torch.relu(0.5 - world.herbivore)).clamp(0.0,1.0)

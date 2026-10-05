import torch

def apply(world):
    world.herbivore = (world.herbivore - 0.01 * torch.relu(0.3 - world.oxygen)).clamp(0.0,1.0)

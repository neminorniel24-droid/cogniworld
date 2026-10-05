import torch

def apply(world):
    world.predator *= (1.0 - 0.02 * torch.relu(0.2 - world.herbivore)).clamp(0.0,1.0)

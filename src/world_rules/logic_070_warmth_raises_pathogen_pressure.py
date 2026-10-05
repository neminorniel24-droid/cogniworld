import torch

def apply(world):
    world.pathogen_load = (world.pathogen_load + 0.02 * torch.relu(world.temperature - 0.6)).clamp(0.0,1.0)

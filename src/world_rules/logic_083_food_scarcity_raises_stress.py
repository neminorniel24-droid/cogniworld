import torch

def apply(world):
    world.habitat_stress = (world.habitat_stress + 0.02 * torch.relu(0.2 - world.vegetation)).clamp(0.0,1.0)

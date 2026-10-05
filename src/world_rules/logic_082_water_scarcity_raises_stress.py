import torch

def apply(world):
    world.habitat_stress = (world.habitat_stress + 0.03 * torch.relu(0.2 - world.surface_water)).clamp(0.0,1.0)

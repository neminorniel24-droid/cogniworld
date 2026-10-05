import torch

def apply(world):
    world.habitat_stress = (world.habitat_stress + 0.02 * torch.abs(world.temperature - 0.5)).clamp(0.0,1.0)

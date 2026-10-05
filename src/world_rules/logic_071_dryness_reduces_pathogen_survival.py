import torch

def apply(world):
    world.pathogen_load *= (1.0 - 0.03 * torch.relu(0.4 - world.soil_moisture)).clamp(0.0,1.0)

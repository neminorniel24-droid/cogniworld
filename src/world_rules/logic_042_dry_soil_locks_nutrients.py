import torch

def apply(world):
    world.nutrients *= (1.0 - 0.01 * torch.relu(0.2 - world.soil_moisture)).clamp(0.0,1.0)

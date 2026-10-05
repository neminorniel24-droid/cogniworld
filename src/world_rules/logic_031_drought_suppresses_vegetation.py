import torch

def apply(world):
    world.vegetation = (world.vegetation - 0.02 * torch.relu(0.25 - world.soil_moisture)).clamp(0.0, 1.0)

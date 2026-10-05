import torch

def apply(world):
    world.vegetation = (world.vegetation - 0.01 * torch.relu(0.3 - world.soil_depth)).clamp(0.0,1.0)

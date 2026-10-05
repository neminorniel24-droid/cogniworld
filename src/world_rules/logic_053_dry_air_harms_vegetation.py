import torch

def apply(world):
    world.vegetation = (world.vegetation - 0.015 * torch.relu(0.25 - world.humidity)).clamp(0.0,1.0)

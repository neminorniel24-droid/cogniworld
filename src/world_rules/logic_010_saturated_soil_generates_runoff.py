import torch

def apply(world):
    world.runoff = (0.2 * torch.relu(world.soil_moisture - 0.8)).clamp(0.0, 1.0); world.soil_moisture = (world.soil_moisture - world.runoff).clamp(0.0, 1.0)

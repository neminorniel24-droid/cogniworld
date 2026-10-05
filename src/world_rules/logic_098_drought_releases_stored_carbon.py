import torch

def apply(world):
    world.carbon_storage = (world.carbon_storage - 0.02 * torch.relu(0.2 - world.soil_moisture) * world.carbon_storage).clamp(0.0,1.0)

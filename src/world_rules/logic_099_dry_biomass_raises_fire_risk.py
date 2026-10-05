import torch

def apply(world):
    world.fire_risk = (world.fire_risk + 0.02 * torch.relu(0.3-world.soil_moisture) * world.vegetation).clamp(0.0,1.0)

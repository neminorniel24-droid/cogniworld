import torch

def apply(world):
    src = world.soil_moisture
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.evaporation = torch.clamp(world.evaporation + delta, -2.0, 2.0)

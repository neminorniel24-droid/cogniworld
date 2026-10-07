import torch

def apply(world):
    src = world.temperature_target
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.soil_depth = torch.clamp(world.soil_depth + delta, -2.0, 2.0)

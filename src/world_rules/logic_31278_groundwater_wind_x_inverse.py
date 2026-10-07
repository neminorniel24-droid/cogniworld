import torch

def apply(world):
    src = world.groundwater
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.wind_x = torch.clamp(world.wind_x + delta, -2.0, 2.0)

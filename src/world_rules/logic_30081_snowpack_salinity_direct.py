import torch

def apply(world):
    src = world.snowpack
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.salinity = torch.clamp(world.salinity + delta, -2.0, 2.0)

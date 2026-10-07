import torch

def apply(world):
    src = world.biomass
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.carrion = torch.clamp(world.carrion + delta, -2.0, 2.0)

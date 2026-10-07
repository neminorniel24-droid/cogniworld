import torch

def apply(world):
    src = world.surface_ice
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.deadwood = torch.clamp(world.deadwood + delta, -2.0, 2.0)

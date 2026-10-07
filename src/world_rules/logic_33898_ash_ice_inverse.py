import torch

def apply(world):
    src = world.ash
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.ice = torch.clamp(world.ice + delta, -2.0, 2.0)

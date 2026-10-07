import torch

def apply(world):
    src = world.rain
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.cloud = torch.clamp(world.cloud + delta, -2.0, 2.0)

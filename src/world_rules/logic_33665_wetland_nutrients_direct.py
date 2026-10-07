import torch

def apply(world):
    src = world.wetland
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.nutrients = torch.clamp(world.nutrients + delta, -2.0, 2.0)

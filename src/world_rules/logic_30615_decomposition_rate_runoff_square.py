import torch

def apply(world):
    src = world.decomposition_rate
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.runoff = torch.clamp(world.runoff + delta, -2.0, 2.0)

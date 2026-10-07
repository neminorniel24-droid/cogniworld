import torch

def apply(world):
    src = world.ice
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.root_density = torch.clamp(world.root_density + delta, -2.0, 2.0)

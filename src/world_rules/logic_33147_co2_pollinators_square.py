import torch

def apply(world):
    src = world.co2
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.pollinators = torch.clamp(world.pollinators + delta, -2.0, 2.0)

import torch

def apply(world):
    src = world.photosynthesis_factor
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.herbivore = torch.clamp(world.herbivore + delta, -2.0, 2.0)

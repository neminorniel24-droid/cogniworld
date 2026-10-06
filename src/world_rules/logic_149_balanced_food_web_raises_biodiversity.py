import torch

def apply(world):
    world.biodiversity = (world.biodiversity + 0.003 * torch.minimum(world.herbivore, world.predator)).clamp(0.0, 1.0)

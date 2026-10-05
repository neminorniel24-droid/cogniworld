import torch

def apply(world):
    world.herbivore *= (1.0 - 0.01 * torch.relu(0.2 - world.vegetation)).clamp(0.0,1.0)

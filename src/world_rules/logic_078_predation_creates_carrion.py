import torch

def apply(world):
    world.carrion = (world.carrion + 0.01 * torch.relu(world.predator - 0.4)).clamp(0.0,1.0)

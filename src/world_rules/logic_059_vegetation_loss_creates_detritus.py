import torch

def apply(world):
    world.detritus = (world.detritus + 0.01 * torch.relu(world.biomass - world.vegetation)).clamp(0.0,1.0)

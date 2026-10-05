import torch

def apply(world):
    world.temperature = 0.8 * world.temperature + 0.05 * (torch.roll(world.temperature,1,0)+torch.roll(world.temperature,-1,0)+torch.roll(world.temperature,1,1)+torch.roll(world.temperature,-1,1))

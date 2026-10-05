import torch

def apply(world):
    world.co2 = 0.75 * world.co2 + 0.0625 * (torch.roll(world.co2,1,0)+torch.roll(world.co2,-1,0)+torch.roll(world.co2,1,1)+torch.roll(world.co2,-1,1))

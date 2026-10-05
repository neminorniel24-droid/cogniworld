import torch

def apply(world):
    world.oxygen = 0.75 * world.oxygen + 0.0625 * (torch.roll(world.oxygen,1,0)+torch.roll(world.oxygen,-1,0)+torch.roll(world.oxygen,1,1)+torch.roll(world.oxygen,-1,1))

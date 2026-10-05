import torch

def apply(world):
    world.co2 = 0.9 * world.co2 + 0.025 * (torch.roll(world.co2,1,0)+torch.roll(world.co2,-1,0)+torch.roll(world.co2,1,1)+torch.roll(world.co2,-1,1))
    world.oxygen = 0.9 * world.oxygen + 0.025 * (torch.roll(world.oxygen,1,0)+torch.roll(world.oxygen,-1,0)+torch.roll(world.oxygen,1,1)+torch.roll(world.oxygen,-1,1))

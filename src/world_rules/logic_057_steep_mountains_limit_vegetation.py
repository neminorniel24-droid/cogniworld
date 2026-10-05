import torch

def apply(world):
    world.slope = (torch.abs(torch.roll(world.elevation,-1,1)-torch.roll(world.elevation,1,1)) + torch.abs(torch.roll(world.elevation,-1,0)-torch.roll(world.elevation,1,0))).clamp(0.0,1.0); world.vegetation = (world.vegetation - 0.02 * world.slope).clamp(0.0,1.0)

import torch

def apply(world):
    world.nutrients = (world.nutrients + 0.03 * world.detritus).clamp(0.0,1.0); world.detritus *= 0.97

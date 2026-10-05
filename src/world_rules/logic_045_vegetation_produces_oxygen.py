import torch

def apply(world):
    world.oxygen = (world.oxygen + 0.02 * world.vegetation).clamp(0.0,1.0)

import torch

def apply(world):
    world.erosion = (world.erosion + 0.02 * world.runoff * world.rain).clamp(0.0,1.0)

import torch

def apply(world):
    world.soil_depth = (world.soil_depth - 0.05 * world.erosion).clamp(0.0,1.0)

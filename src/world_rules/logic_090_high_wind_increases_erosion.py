import torch

def apply(world):
    world.erosion = (world.erosion + 0.01 * (world.wind_x.abs() + world.wind_y.abs())).clamp(0.0,1.0)

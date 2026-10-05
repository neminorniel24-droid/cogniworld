import torch

def apply(world):
    world.methane = (world.methane + 0.01 * world.soil_moisture * (1.0 - world.oxygen)).clamp(0.0,1.0)

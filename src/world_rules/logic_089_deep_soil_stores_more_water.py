import torch

def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.02 * world.soil_depth * (1.0 - world.soil_moisture)).clamp(0.0,1.0)

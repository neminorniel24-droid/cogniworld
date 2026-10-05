import torch

def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.01 * (1.0 - world.elevation) * (1.0 - world.soil_moisture)).clamp(0.0, 1.0)

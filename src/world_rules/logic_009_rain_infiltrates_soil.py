import torch

def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.5 * world.rain).clamp(0.0, 1.0)

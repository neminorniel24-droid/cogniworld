import torch

def apply(world):
    world.temperature = (world.temperature - 0.03 * world.soil_moisture).clamp(0.0, 1.0)

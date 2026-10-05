import torch

def apply(world):
    world.soil_moisture = (world.soil_moisture - 0.01 * world.vegetation).clamp(0.0,1.0)

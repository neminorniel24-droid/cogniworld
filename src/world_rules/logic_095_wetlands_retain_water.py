import torch

def apply(world):
    world.wetland = (world.wetland + 0.02 * world.rain * world.soil_moisture).clamp(0.0,1.0); world.surface_water = (world.surface_water + 0.01 * world.wetland).clamp(0.0,1.0)

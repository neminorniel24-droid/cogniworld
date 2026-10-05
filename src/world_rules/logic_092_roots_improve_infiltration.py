import torch

def apply(world):
    world.root_density = (world.root_density + 0.02 * world.vegetation).clamp(0.0,1.0); world.soil_moisture = (world.soil_moisture + 0.01 * world.root_density * (1.0-world.soil_moisture)).clamp(0.0,1.0)

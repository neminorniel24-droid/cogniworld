import torch

def apply(world):
    world.temperature_target = 1.0 - 0.65 * world.elevation

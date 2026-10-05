import torch

def apply(world):
    world.humidity = (world.humidity + 0.03 * world.vegetation).clamp(0.0, 1.0)

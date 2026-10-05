import torch

def apply(world):
    world.temperature += 0.08 * (world.temperature_target - world.temperature)

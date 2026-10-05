import torch

def apply(world):
    world.vegetation = (world.vegetation * (1.0 - 0.02 * world.habitat_stress)).clamp(0.0,1.0)

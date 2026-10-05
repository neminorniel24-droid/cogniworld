import torch

def apply(world):
    world.vegetation = (world.vegetation + 0.015 * world.nutrients * (1.0 - world.vegetation)).clamp(0.0,1.0)

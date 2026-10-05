import torch

def apply(world):
    world.runoff *= (1.0 - 0.3 * world.vegetation).clamp(0.0,1.0)

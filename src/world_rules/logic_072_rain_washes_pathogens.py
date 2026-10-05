import torch

def apply(world):
    world.pathogen_load *= (1.0 - 0.2 * world.rain).clamp(0.0,1.0)

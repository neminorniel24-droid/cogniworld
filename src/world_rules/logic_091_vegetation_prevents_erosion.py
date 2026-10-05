import torch

def apply(world):
    world.erosion *= (1.0 - 0.4 * world.vegetation).clamp(0.0,1.0)

import torch

def apply(world):
    world.decomposition_rate = (0.01 + 0.03 * world.temperature).clamp(0.0,0.05); world.carrion *= (1.0 - world.decomposition_rate)

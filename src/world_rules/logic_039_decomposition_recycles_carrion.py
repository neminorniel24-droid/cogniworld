import torch

def apply(world):
    world.nutrients = (world.nutrients + 0.02 * world.carrion).clamp(0.0,1.0); world.carrion *= 0.98

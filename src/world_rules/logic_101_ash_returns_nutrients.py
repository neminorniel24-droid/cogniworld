import torch

def apply(world):
    world.nutrients = (world.nutrients + world.ash).clamp(0.0,1.0); world.ash *= 0.9

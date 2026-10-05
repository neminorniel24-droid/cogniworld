import torch

def apply(world):
    world.predator = (world.predator + 0.015 * world.herbivore - 0.008 * world.predator).clamp(0.0,1.0)

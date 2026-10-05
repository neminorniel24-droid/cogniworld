import torch

def apply(world):
    world.herbivore = (world.herbivore - 0.01 * world.predator).clamp(0.0,1.0)

import torch

def apply(world):
    world.herbivore = (world.herbivore + 0.01 * world.vegetation * (1.0 - world.herbivore)).clamp(0.0,1.0)

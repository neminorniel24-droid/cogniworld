import torch

def apply(world):
    world.herbivore = (world.herbivore + 0.02 * world.vegetation - 0.01 * world.herbivore).clamp(0.0,1.0)

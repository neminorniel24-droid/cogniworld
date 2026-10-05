import torch

def apply(world):
    world.root_density += 0.03 * (world.vegetation - world.root_density)

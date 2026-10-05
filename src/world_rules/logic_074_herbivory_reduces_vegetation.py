import torch

def apply(world):
    world.vegetation = (world.vegetation - 0.01 * world.herbivore).clamp(0.0,1.0)

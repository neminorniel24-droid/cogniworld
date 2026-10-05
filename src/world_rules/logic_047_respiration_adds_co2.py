import torch

def apply(world):
    world.co2 = (world.co2 + 0.01 * (world.biomass + world.herbivore + world.predator)).clamp(0.0,1.0)

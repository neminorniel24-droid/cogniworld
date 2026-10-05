import torch

def apply(world):
    world.biomass += 0.05 * (world.vegetation - world.biomass)

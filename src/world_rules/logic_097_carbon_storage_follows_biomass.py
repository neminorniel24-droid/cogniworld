import torch

def apply(world):
    world.carbon_storage += 0.02 * (world.biomass - world.carbon_storage)

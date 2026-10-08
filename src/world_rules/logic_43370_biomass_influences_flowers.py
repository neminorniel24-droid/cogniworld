"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.biomass
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.flowers = torch.clamp(world.flowers + delta, -2.0, 2.0)

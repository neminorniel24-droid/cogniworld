"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.ice
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.evaporation = torch.clamp(world.evaporation + delta, -2.0, 2.0)

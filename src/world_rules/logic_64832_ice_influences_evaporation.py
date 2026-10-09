"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.ice
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.evaporation = torch.clamp(world.evaporation + delta, -2.0, 2.0)

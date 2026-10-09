"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.ash
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.salinity = torch.clamp(world.salinity + delta, -2.0, 2.0)

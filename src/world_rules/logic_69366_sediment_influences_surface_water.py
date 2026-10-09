"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.sediment
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.surface_water = torch.clamp(world.surface_water + delta, -2.0, 2.0)

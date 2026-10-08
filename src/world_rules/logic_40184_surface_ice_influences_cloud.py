"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.surface_ice
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.cloud = torch.clamp(world.cloud + delta, -2.0, 2.0)

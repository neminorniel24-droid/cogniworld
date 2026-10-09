"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.carbon_storage
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.surface_ice = torch.clamp(world.surface_ice + delta, -2.0, 2.0)

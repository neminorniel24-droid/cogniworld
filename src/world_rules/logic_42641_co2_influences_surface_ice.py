"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.co2
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.surface_ice = torch.clamp(world.surface_ice + delta, -2.0, 2.0)

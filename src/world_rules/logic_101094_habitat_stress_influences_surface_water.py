"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.habitat_stress
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.surface_water = torch.clamp(world.surface_water + delta, -2.0, 2.0)

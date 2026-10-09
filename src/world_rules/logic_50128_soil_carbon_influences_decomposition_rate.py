"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.soil_carbon
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.decomposition_rate = torch.clamp(world.decomposition_rate + delta, -2.0, 2.0)

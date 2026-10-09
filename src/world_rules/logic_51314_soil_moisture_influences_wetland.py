"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.soil_moisture
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.wetland = torch.clamp(world.wetland + delta, -2.0, 2.0)

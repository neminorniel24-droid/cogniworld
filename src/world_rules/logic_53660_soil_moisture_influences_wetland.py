"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.soil_moisture
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.wetland = torch.clamp(world.wetland + delta, -2.0, 2.0)

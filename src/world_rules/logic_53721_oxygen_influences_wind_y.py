"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.oxygen
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.wind_y = torch.clamp(world.wind_y + delta, -2.0, 2.0)

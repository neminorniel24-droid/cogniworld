"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.wind_y
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.pollinators = torch.clamp(world.pollinators + delta, -2.0, 2.0)

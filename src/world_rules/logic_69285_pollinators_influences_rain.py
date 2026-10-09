"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.pollinators
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.rain = torch.clamp(world.rain + delta, -2.0, 2.0)

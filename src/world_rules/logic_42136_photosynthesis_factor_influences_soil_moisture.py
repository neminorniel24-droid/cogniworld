"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.photosynthesis_factor
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.soil_moisture = torch.clamp(world.soil_moisture + delta, -2.0, 2.0)

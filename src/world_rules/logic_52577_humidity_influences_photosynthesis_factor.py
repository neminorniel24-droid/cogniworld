"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.humidity
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor + delta, -2.0, 2.0)

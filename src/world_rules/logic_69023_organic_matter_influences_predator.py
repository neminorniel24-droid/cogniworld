"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.organic_matter
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.predator = torch.clamp(world.predator + delta, -2.0, 2.0)

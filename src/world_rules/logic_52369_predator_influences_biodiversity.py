"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.predator
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.biodiversity = torch.clamp(world.biodiversity + delta, -2.0, 2.0)

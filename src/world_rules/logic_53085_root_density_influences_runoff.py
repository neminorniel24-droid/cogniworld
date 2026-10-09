"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.root_density
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.runoff = torch.clamp(world.runoff + delta, -2.0, 2.0)

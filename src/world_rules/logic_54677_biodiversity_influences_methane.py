"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.biodiversity
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.methane = torch.clamp(world.methane + delta, -2.0, 2.0)

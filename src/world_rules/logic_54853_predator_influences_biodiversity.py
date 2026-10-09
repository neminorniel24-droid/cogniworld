"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.predator
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.biodiversity = torch.clamp(world.biodiversity + delta, -2.0, 2.0)

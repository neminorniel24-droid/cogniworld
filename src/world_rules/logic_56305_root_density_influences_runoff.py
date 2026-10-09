"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.root_density
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.runoff = torch.clamp(world.runoff + delta, -2.0, 2.0)

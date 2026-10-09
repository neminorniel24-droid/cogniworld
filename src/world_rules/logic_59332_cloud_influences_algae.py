"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.cloud
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.algae = torch.clamp(world.algae + delta, -2.0, 2.0)

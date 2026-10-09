"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.runoff
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.humidity = torch.clamp(world.humidity + delta, -2.0, 2.0)

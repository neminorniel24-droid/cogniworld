"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.snowpack
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.vegetation = torch.clamp(world.vegetation + delta, -2.0, 2.0)

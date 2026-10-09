"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.groundwater
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.root_density = torch.clamp(world.root_density + delta, -2.0, 2.0)

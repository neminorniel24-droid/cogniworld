"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.methane
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.carbon_storage = torch.clamp(world.carbon_storage + delta, -2.0, 2.0)

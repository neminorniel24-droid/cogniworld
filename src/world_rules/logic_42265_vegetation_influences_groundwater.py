"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.vegetation
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.groundwater = torch.clamp(world.groundwater + delta, -2.0, 2.0)

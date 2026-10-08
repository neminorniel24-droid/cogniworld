"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.wetland
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.salinity = torch.clamp(world.salinity + delta, -2.0, 2.0)

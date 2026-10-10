"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.surface_water
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.sediment = torch.clamp(world.sediment + delta, -2.0, 2.0)

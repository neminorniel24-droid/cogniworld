"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.sediment
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.ash = torch.clamp(world.ash + delta, -2.0, 2.0)

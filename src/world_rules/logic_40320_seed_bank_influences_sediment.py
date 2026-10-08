"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.seed_bank
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.sediment = torch.clamp(world.sediment + delta, -2.0, 2.0)

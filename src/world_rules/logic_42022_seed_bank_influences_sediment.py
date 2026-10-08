"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.seed_bank
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.sediment = torch.clamp(world.sediment + delta, -2.0, 2.0)

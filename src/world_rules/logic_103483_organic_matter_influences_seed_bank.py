"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.organic_matter
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.seed_bank = torch.clamp(world.seed_bank + delta, -2.0, 2.0)

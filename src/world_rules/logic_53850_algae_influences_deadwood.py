"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.algae
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.deadwood = torch.clamp(world.deadwood + delta, -2.0, 2.0)

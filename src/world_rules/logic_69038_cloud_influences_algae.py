"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.cloud
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.algae = torch.clamp(world.algae + delta, -2.0, 2.0)

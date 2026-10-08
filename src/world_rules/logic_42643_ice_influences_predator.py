"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.ice
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.predator = torch.clamp(world.predator + delta, -2.0, 2.0)

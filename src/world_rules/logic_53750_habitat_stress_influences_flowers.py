"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.habitat_stress
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.flowers = torch.clamp(world.flowers + delta, -2.0, 2.0)

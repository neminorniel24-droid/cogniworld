"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.habitat_stress
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.wind_y = torch.clamp(world.wind_y + delta, -2.0, 2.0)

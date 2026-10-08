"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.temperature_target
    delta = torch.clamp(torch.sqrt(torch.clamp(src, min=0.0)) * 0.00035, -0.01, 0.01)
    world.co2 = torch.clamp(world.co2 + delta, -2.0, 2.0)

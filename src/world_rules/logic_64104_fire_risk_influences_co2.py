"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.fire_risk
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.co2 = torch.clamp(world.co2 + delta, -2.0, 2.0)

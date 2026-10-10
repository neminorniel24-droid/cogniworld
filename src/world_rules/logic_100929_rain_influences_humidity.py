"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.rain
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.humidity = torch.clamp(world.humidity + delta, -2.0, 2.0)

"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.temperature
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.wind_x = torch.clamp(world.wind_x + delta, -2.0, 2.0)

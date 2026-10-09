"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.temperature_target
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.erosion = torch.clamp(world.erosion + delta, -2.0, 2.0)

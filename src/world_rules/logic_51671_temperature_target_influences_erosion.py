"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.temperature_target
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.erosion = torch.clamp(world.erosion + delta, -2.0, 2.0)

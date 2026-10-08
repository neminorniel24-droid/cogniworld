"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.algae
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.temperature_target = torch.clamp(world.temperature_target + delta, -2.0, 2.0)

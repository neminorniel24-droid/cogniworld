"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.herbivore
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.soil_moisture = torch.clamp(world.soil_moisture + delta, -2.0, 2.0)

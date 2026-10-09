"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.herbivore
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.soil_moisture = torch.clamp(world.soil_moisture + delta, -2.0, 2.0)

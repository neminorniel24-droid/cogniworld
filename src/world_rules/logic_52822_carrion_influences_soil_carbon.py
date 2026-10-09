"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.carrion
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.soil_carbon = torch.clamp(world.soil_carbon + delta, -2.0, 2.0)

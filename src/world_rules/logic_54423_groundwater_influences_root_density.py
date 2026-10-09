"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.groundwater
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.root_density = torch.clamp(world.root_density + delta, -2.0, 2.0)

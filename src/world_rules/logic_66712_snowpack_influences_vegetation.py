"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.snowpack
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.vegetation = torch.clamp(world.vegetation + delta, -2.0, 2.0)

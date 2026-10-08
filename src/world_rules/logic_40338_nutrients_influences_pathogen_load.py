"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.nutrients
    delta = torch.clamp((1.0 - src) * 0.0004, -0.01, 0.01)
    world.pathogen_load = torch.clamp(world.pathogen_load + delta, -2.0, 2.0)

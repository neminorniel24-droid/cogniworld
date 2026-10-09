"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.flowers
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.pathogen_load = torch.clamp(world.pathogen_load + delta, -2.0, 2.0)

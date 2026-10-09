"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.pathogen_load
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.cloud = torch.clamp(world.cloud + delta, -2.0, 2.0)

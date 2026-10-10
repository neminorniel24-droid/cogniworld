"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.detritus
    delta = torch.clamp(src * 0.0005, -0.01, 0.01)
    world.temperature = torch.clamp(world.temperature + delta, -2.0, 2.0)

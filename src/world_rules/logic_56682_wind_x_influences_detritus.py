"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.wind_x
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.detritus = torch.clamp(world.detritus + delta, -2.0, 2.0)

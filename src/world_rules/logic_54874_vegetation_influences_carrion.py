"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.vegetation
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.carrion = torch.clamp(world.carrion + delta, -2.0, 2.0)

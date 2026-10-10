"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.deadwood
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.fire_risk = torch.clamp(world.fire_risk + delta, -2.0, 2.0)

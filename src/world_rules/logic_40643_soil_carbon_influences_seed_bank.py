"""Deterministic environmental causal rule."""
import torch

def apply(world):
    src = world.soil_carbon
    delta = torch.clamp(src.square() * 0.00025, -0.01, 0.01)
    world.seed_bank = torch.clamp(world.seed_bank + delta, -2.0, 2.0)
